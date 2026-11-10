"""Testes de contrato por HTTP real, com isolamento de dados por teste."""
import concurrent.futures
import hashlib
import importlib.util
import json
from pathlib import Path
import threading
import time
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

SOURCE = Path(__file__).resolve().parents[1] / 'exemplos/app-alvo-teste/servidor_fullstack.py'
spec = importlib.util.spec_from_file_location('laboratorio', SOURCE)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = app.ThreadingHTTPServer(('127.0.0.1', 0), app.Handler)
        cls.worker = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.worker.start()
        cls.base = 'http://127.0.0.1:%s' % cls.server.server_port

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.worker.join()

    def setUp(self):
        with app.LOCK:
            app.RECORDS.clear()
            app.UPLOADS.clear()
        _, data = self.call('POST', '/api/auth/login', {'usuario': 'estudante_qa', 'senha': 'oculix123'}, auth=False)
        self.token = data['token']

    def call(self, method, path, data=None, auth=True, raw=None, content_type='application/json'):
        headers = {'Content-Type': content_type}
        if auth:
            headers['Authorization'] = 'Bearer ' + self.token
        body = raw if raw is not None else json.dumps(data).encode() if data is not None else None
        request = Request(self.base + path, body, headers, method=method)
        try:
            response = urlopen(request, timeout=10)
        except HTTPError as error:
            response = error
        with response:
            payload = response.read()
            if response.headers.get_content_type() == 'application/json':
                payload = json.loads(payload)
            return response.status, payload

    def test_frontend_health_and_delay(self):
        code, html = self.call('GET', '/', auth=False)
        self.assertEqual(code, 200)
        self.assertIn(b'async function fazerLogin', html)
        start = time.monotonic()
        code, data = self.call('GET', '/api/health?latencia_ms=40', auth=False)
        self.assertEqual((code, data['status']), (200, 'ok'))
        self.assertGreaterEqual(time.monotonic() - start, .035)
        self.assertGreater(data['requisicoes'], 0)
        self.assertEqual(self.call('GET', '/api/health?latencia_ms=NaN', auth=False)[0], 400)

    def test_authentication(self):
        self.assertEqual(self.call('POST', '/api/auth/login', {'usuario': 'estudante_qa', 'senha': 'errada'}, auth=False)[0], 401)
        self.assertEqual(self.call('GET', '/api/avaliacoes', auth=False)[0], 401)
        self.token = self.token[:-5] + 'ABCDE'
        self.assertEqual(self.call('GET', '/api/avaliacoes')[0], 401)

    def test_expired_and_malformed_tokens(self):
        self.assertFalse(app.valid_token('invalid'))
        payload = app.b64(json.dumps({'sub': 'estudante_qa', 'exp': 0}).encode())
        message = app.b64(b'{"alg":"HS256","typ":"JWT"}') + b'.' + payload
        token = (message + b'.' + app.b64(app.hmac.digest(app.SECRET, message, 'sha256'))).decode()
        self.assertFalse(app.valid_token(token))

    def test_crud_filters_and_statuses(self):
        code, row = self.call('POST', '/api/avaliacoes', {'nome': 'Ana', 'nota1': 8.5, 'nota2': 9.5})
        self.assertEqual((code, row['media'], row['status']), (201, 9, 'APROVADO'))
        path = '/api/avaliacoes/%s' % row['id']
        self.assertEqual(self.call('GET', path)[1], row)
        self.assertEqual(len(self.call('GET', '/api/avaliacoes?status=APROVADO')[1]), 1)
        code, row = self.call('PUT', path, {'nome': 'Ana', 'nota1': 4, 'nota2': 5})
        self.assertEqual((code, row['media'], row['status']), (200, 4.5, 'REPROVADO'))
        self.assertEqual(self.call('GET', '/api/avaliacoes?status=APROVADO')[1], [])
        self.assertEqual(self.call('PATCH', path, {'nota1': 9})[1]['media'], 7)
        self.assertEqual(self.call('DELETE', path)[0], 200)
        self.assertEqual(self.call('GET', path)[0], 404)
        self.assertEqual(self.call('DELETE', path)[0], 404)
        self.assertEqual(self.call('GET', '/api/inexistente')[0], 404)

    def test_validation_and_boundaries(self):
        for value in (-1, 11, '8', True, None, float('nan'), float('inf')):
            with self.subTest(value=value):
                self.assertEqual(self.call('POST', '/api/avaliacoes', {'nome': 'Ana', 'nota1': value, 'nota2': 8})[0], 400)
        for data in ({}, [], {'nome': ' ', 'nota1': 8, 'nota2': 9}):
            self.assertEqual(self.call('POST', '/api/avaliacoes', data)[0], 400)
        self.assertEqual(self.call('POST', '/api/avaliacoes', raw=b'{')[0], 400)
        for grade, expected in [(0, 'REPROVADO'), (6.99, 'REPROVADO'), (7, 'APROVADO'), (10, 'APROVADO')]:
            code, row = self.call('POST', '/api/avaliacoes', {'nome': 'Limite', 'nota1': grade, 'nota2': grade})
            self.assertEqual((code, row['status']), (201, expected))

    def test_upload_download(self):
        content = 'Comprovante de teste com acentuação.'.encode()
        raw = b'--AulaBoundary\r\nContent-Disposition: form-data; name="arquivo"; filename="../comprovante.txt"\r\nContent-Type: text/plain\r\n\r\n' + content + b'\r\n--AulaBoundary--\r\n'
        code, data = self.call('POST', '/api/upload-comprovante', raw=raw, content_type='multipart/form-data; boundary=AulaBoundary')
        self.assertEqual(code, 201)
        self.assertEqual(data['nome'], 'comprovante.txt')
        self.assertEqual(data['bytes'], len(content))
        self.assertEqual(data['sha256'], hashlib.sha256(content).hexdigest())
        self.assertEqual(self.call('GET', data['download']), (200, content))
        self.assertEqual(self.call('GET', data['download'], auth=False)[0], 401)
        self.assertEqual(self.call('GET', '/api/arquivos/ausente')[0], 404)
        self.assertEqual(self.call('POST', '/api/upload-comprovante', raw=b'{}')[0], 400)

    def test_concurrent_ids(self):
        def create(i):
            code, row = self.call('POST', '/api/avaliacoes', {'nome': 'Aluno %s' % i, 'nota1': 8, 'nota2': 9})
            self.assertEqual(code, 201)
            return row['id']
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            ids = list(pool.map(create, range(30)))
        self.assertEqual(len(set(ids)), 30)
        self.assertEqual(len(self.call('GET', '/api/avaliacoes')[1]), 30)


if __name__ == '__main__':
    unittest.main()
