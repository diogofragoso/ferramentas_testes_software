[🏠 Hub](../README.md) · [🛡️ Menu ZAP](README.md)

# Capítulo 05: API, JWT e testes de autenticação

**Objetivo:** comparar respostas com token válido, ausente e alterado. Reserve 40 minutos.

## 1. Capturar uma chamada autenticada

1. Mantenha o laboratório na porta 8081 e o contexto em escopo. Selecione **Protected Mode**, pois vamos reenviar requisições.
2. No navegador aberto pelo ZAP, faça login novamente se o servidor foi reiniciado ou se passou uma hora.
3. Crie uma avaliação com nome `Autenticacao ZAP` e notas `8` e `6`.
4. Em **History**, localize o POST `/api/avaliacoes?latencia_ms=1800` com resposta 201.
5. Confira o cabeçalho `Authorization: Bearer ...` nessa requisição e o token na resposta do login. Não publique o token.

O servidor emite JWT HS256 com validade de uma hora e chave efêmera. As rotas de avaliações exigem token; `/api/health` não exige. Referência do exercício: [contrato HTTP local](../exemplos/README.md).

## 2. Preparar uma consulta de leitura

1. Clique com o botão direito na requisição capturada e abra **Open/Resend with Request Editor**. Conforme os complementos, pode aparecer uma opção equivalente no Requester.
2. No editor, mude o método para **GET** e a URL para `http://localhost:8081/api/avaliacoes`.
3. Apague o corpo JSON. Remova `Content-Length` e `Content-Type` que tenham sido copiados do POST; deixe o editor recalcular o tamanho, se necessário.
4. Preserve o cabeçalho Authorization original. Confira destino e método antes de clicar em **Send**.
5. Espere **200**, com uma lista JSON de avaliações.

O editor permite modificar e reenviar uma mensagem sem repetir a jornada visual. Referência: [Manual Request Editor](https://www.zaproxy.org/docs/desktop/ui/dialogs/man_req/).

## 3. Executar os três casos

Parta sempre da consulta GET acima, mantendo URL e método iguais:

| Caso | Alteração no editor | Esperado |
| --- | --- | --- |
| CT-01 | Authorization com token válido | 200 e lista JSON |
| CT-02 | Remover a linha Authorization inteira | 401 e mensagem de token ausente, inválido ou expirado |
| CT-03 | Restaurar a linha e trocar o primeiro caractere da assinatura, após o último ponto do JWT, por outro caractere | 401 |

1. Envie CT-01 e registre o status e o corpo.
2. Remova Authorization, envie CT-02 e registre o resultado.
3. Restaure o token válido, altere a assinatura como indicado e envie CT-03.
4. Restaure o token original e repita CT-01 para confirmar que a diferença vem da credencial.

Se CT-01 der 401, obtenha um token novo pelo login e repita. Se o editor não permitir enviar, confira o modo e a correspondência da URL com o contexto.

## 4. Registrar o limite da conclusão

Esses casos verificam rejeição de requisições sem credencial válida. O laboratório tem um único usuário: não permite concluir sobre isolamento entre contas ou perfis. Também não configuramos renovação automática de JWT no scanner. Uma varredura que recebe somente 401 nas rotas protegidas tem cobertura limitada.

## Exercício e evidência

Entregue uma tabela esperado/obtido com os três casos e trechos de resposta sem tokens. Explique por que um 401 esperado representa aprovação do caso de teste.

- [ ] CT-01 retornou 200 com token válido.
- [ ] CT-02 e CT-03 retornaram 401.
- [ ] Diferenciei autenticação de autorização entre usuários.

[← Anterior](04-spider-e-varredura-ativa.md) · [Menu](README.md) · [Próximo: relatório →](06-alertas-relatorio-e-projeto-pratico.md)
