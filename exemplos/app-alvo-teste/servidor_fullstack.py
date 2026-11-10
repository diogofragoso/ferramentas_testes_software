"""Laboratório local: Python 3.10+, apenas biblioteca padrão, dados em memória."""
import argparse
import base64
import hashlib
import hmac
import json
import math
import secrets
import threading
import time
from email.parser import BytesParser
from email.policy import default
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parent
SECRET = secrets.token_bytes(32)
LOCK = threading.Lock()
RECORDS = {}
UPLOADS = {}
NEXT_ID = 1
REQUESTS = 0
MAX_BODY = 2 * 1024 * 1024


def b64(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=")


def issue_token():
    header = b64(b'{"alg":"HS256","typ":"JWT"}')
    payload = b64(json.dumps({"sub": "estudante_qa", "exp": int(time.time()) + 3600}).encode())
    message = header + b"." + payload
    return (message + b"." + b64(hmac.digest(SECRET, message, "sha256"))).decode()


def valid_token(token):
    try:
        header, payload, signature = token.encode().split(b".")
        expected = b64(hmac.digest(SECRET, header + b"." + payload, "sha256"))
        claims = json.loads(base64.urlsafe_b64decode(payload + b"=" * (-len(payload) % 4)))
        return (hmac.compare_digest(expected, signature)
                and claims["sub"] == "estudante_qa" and claims["exp"] > time.time())
    except (ValueError, KeyError, TypeError, UnicodeError):
        return False


def evaluation(data):
    if not isinstance(data, dict) or not isinstance(data.get("nome"), str) or not data["nome"].strip():
        raise ValueError("Informe nome e notas numéricas de 0 a 10")
    grades = [data.get("nota1"), data.get("nota2")]
    if any(isinstance(n, bool) or not isinstance(n, (int, float))
           or not math.isfinite(n) or not 0 <= n <= 10 for n in grades):
        raise ValueError("Informe nome e notas numéricas de 0 a 10")
    mean = sum(grades) / 2
    return {"nome": data["nome"].strip(), "nota1": grades[0], "nota2": grades[1],
            "media": round(mean, 2), "status": "APROVADO" if mean >= 7 else "REPROVADO"}


class Handler(BaseHTTPRequestHandler):
    server_version = "LaboratorioFullStack/1.0"

    def send(self, code, data, content_type="application/json; charset=utf-8"):
        body = json.dumps(data, ensure_ascii=False, allow_nan=False).encode() if isinstance(data, (dict, list)) else data
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def body(self):
        size = int(self.headers.get("Content-Length", "0"))
        if not 0 <= size <= MAX_BODY:
            raise ValueError("Corpo limitado a 2 MiB")
        return self.rfile.read(size)

    def dispatch(self):
        global REQUESTS, NEXT_ID
        with LOCK:
            REQUESTS += 1
            count = REQUESTS
        url = urlsplit(self.path)
        path = url.path
        try:
            delay = float(parse_qs(url.query).get("latencia_ms", [0])[0])
            if not math.isfinite(delay) or not 0 <= delay <= 3000:
                raise ValueError("latencia_ms deve estar entre 0 e 3000")
            time.sleep(delay / 1000)
            method = self.command
            if path == "/" and method == "GET":
                return self.send(200, (ROOT / "index.html").read_bytes(), "text/html; charset=utf-8")
            if path == "/api/health" and method == "GET":
                return self.send(200, {"status": "ok", "requisicoes": count})
            if path in ("/api/auth/login", "/api/login") and method == "POST":
                data = json.loads(self.body())
                if isinstance(data, dict) and data.get("usuario") == "estudante_qa" and data.get("senha") == "oculix123":
                    return self.send(200, {"token": issue_token(), "expires_in": 3600})
                return self.send(401, {"erro": "Credenciais inválidas"})
            if not path.startswith("/api/"):
                return self.send(404, {"erro": "Rota inexistente"})
            auth = self.headers.get("Authorization", "")
            if not auth.startswith("Bearer ") or not valid_token(auth[7:]):
                return self.send(401, {"erro": "Token ausente, inválido ou expirado"})
            if path == "/api/upload-comprovante" and method == "POST":
                mime = self.headers.get("Content-Type", "")
                if not mime.lower().startswith("multipart/form-data"):
                    raise ValueError("Envie multipart/form-data com campo arquivo")
                message = BytesParser(policy=default).parsebytes(
                    ("Content-Type: " + mime + "\r\nMIME-Version: 1.0\r\n\r\n").encode() + self.body())
                for part in message.iter_parts():
                    if part.get_param("name", header="content-disposition") == "arquivo" and part.get_filename():
                        content = part.get_payload(decode=True)
                        key = secrets.token_hex(12)
                        with LOCK:
                            UPLOADS[key] = content
                        return self.send(201, {"id": key, "nome": Path(part.get_filename().replace("\\", "/")).name,
                                               "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest(),
                                               "download": "/api/arquivos/" + key})
                raise ValueError("Campo arquivo ausente")
            if path.startswith("/api/arquivos/") and method == "GET":
                with LOCK:
                    content = UPLOADS.get(path.rsplit("/", 1)[1])
                return self.send(404, {"erro": "Arquivo inexistente"}) if content is None else self.send(200, content, "application/octet-stream")
            if path == "/api/avaliacoes":
                if method == "GET":
                    status = parse_qs(url.query).get("status", [None])[0]
                    with LOCK:
                        rows = [r.copy() for r in RECORDS.values() if status is None or r["status"] == status]
                    return self.send(200, rows)
                if method == "POST":
                    row = evaluation(json.loads(self.body()))
                    with LOCK:
                        row["id"] = NEXT_ID
                        NEXT_ID += 1
                        RECORDS[row["id"]] = row
                    return self.send(201, row)
            if path.startswith("/api/avaliacoes/"):
                try:
                    key = int(path.rsplit("/", 1)[1])
                except ValueError:
                    return self.send(404, {"erro": "Avaliação inexistente"})
                with LOCK:
                    row = RECORDS.get(key)
                    if row is None:
                        return self.send(404, {"erro": "Avaliação inexistente"})
                    if method in ("PUT", "PATCH"):
                        data = json.loads(self.body())
                        if not isinstance(data, dict):
                            raise ValueError("Objeto JSON esperado")
                        row = evaluation(dict(row, **data) if method == "PATCH" else data)
                        row["id"] = key
                        RECORDS[key] = row
                    elif method == "DELETE":
                        del RECORDS[key]
                        return self.send(200, {"id": key, "removido": True})
                    elif method != "GET":
                        return self.send(405, {"erro": "Método não permitido"})
                    return self.send(200, row)
            return self.send(404, {"erro": "Rota inexistente"})
        except (ValueError, UnicodeError) as error:
            return self.send(400, {"erro": str(error)})

    do_GET = dispatch
    do_POST = dispatch
    do_PUT = dispatch
    do_PATCH = dispatch
    do_DELETE = dispatch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print("Laboratório em http://localhost:%s — Ctrl+C para parar" % args.port, flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
