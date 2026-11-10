[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md)

---

# Laboratório Web Full Stack

## Iniciar e usar

Requer Python 3.10+; nenhuma instalação de pacote. Na raiz:

```shell
python exemplos/app-alvo-teste/servidor_fullstack.py
```

Windows com launcher: `py -3 exemplos/app-alvo-teste/servidor_fullstack.py`. Porta alternativa: acrescente `--port 8081`. Abra `http://localhost:8080` e use `estudante_qa` / `oculix123`. Pare com Ctrl+C. O bind é somente 127.0.0.1, para treino local.

O HTML por `file://` calcula notas e simula arquivos localmente. Por HTTP, login, cálculo, upload e download passam pela API. Dados, arquivos e chave JWT desaparecem ao reiniciar. Não há banco persistente nem dependências externas. O botão Pular Login usa as mesmas credenciais pelo endpoint quando online.

## Contrato HTTP

Todas as rotas abaixo, exceto login e health, exigem `Authorization: Bearer TOKEN`. JSON usa UTF-8 e `Content-Type: application/json`.

| Método / rota | Entrada | Saída |
| --- | --- | --- |
| POST /api/auth/login | `{"usuario":"estudante_qa","senha":"oculix123"}` | 200 com token/expires_in ou 401 |
| GET /api/health | nenhuma | 200 com status/requisicoes |
| GET /api/avaliacoes | filtro opcional `?status=APROVADO` | 200, array |
| POST /api/avaliacoes | nome string não vazia, nota1/nota2 números 0..10 | 201 com id/nome/notas/media/status |
| GET /api/avaliacoes/{id} | ID criado | 200 ou 404 |
| PUT /api/avaliacoes/{id} | nome e ambas as notas | 200 ou 400/404 |
| PATCH /api/avaliacoes/{id} | campos parciais | 200 ou 400/404 |
| DELETE /api/avaliacoes/{id} | ID | 200 com removido=true ou 404 |
| POST /api/upload-comprovante | multipart, campo arquivo | 201 com id/nome/bytes/sha256/download |
| GET /api/arquivos/{id} | ID do upload | 200 octet-stream ou 404 |

Notas inválidas, JSON malformado e corpo acima de 2 MiB retornam 400. Token ausente, alterado ou expirado retorna 401. O JWT é HS256 com expiração de uma hora e chave efêmera. Média ≥ 7 aprova; a API arredonda sua representação para duas casas, a UI para uma, preservando a classificação pela média original.

Adicione `latencia_ms=800` a qualquer rota para atrasar a resposta (0..3000 ms). O contador health inclui a própria consulta. Uploads ficam em memória, sem escrita de nomes enviados pelo usuário. Use arquivos pequenos; este servidor é um alvo didático de volume limitado.

## Plano JMeter pronto

```shell
cd exemplos/jmeter
jmeter -n -t plano_api_e_carga_fullstack.jmx -l resultados_funcional.jtl -e -o relatorio_dashboard_funcional
jmeter -n -t plano_api_e_carga_fullstack.jmx -Jfuncional=false -Jcarga=true -Jusuarios=10 -Jrampup=10 -Jduracao=60 -l resultados_carga.jtl -e -o relatorio_dashboard_carga
```

| Propriedade CLI | Padrão | Papel |
| --- | --- | --- |
| funcional | true | Executar CRUD e negativos com CSV |
| carga | false | Executar grupo de leitura |
| usuarios | 5 | Threads de carga |
| rampup | 5 | Segundos para iniciar threads |
| duracao | 30 | Duração total da carga em segundos |
| host / porta | localhost / 8080 | Destino |
| csv | massa_estudantes.csv | Caminho relativo à pasta de execução |

No GUI, ajuste a propriedade csv por `-Jcsv=C:/caminho/absoluto/massa_estudantes.csv` ao iniciar JMeter, ou edite Filename. O grupo funcional usa 15 loops e para no fim da massa. O grupo de carga faz login uma vez e consulta listagem, sem criar dados. Não mistura upload/JDBC no baseline: esses exercícios possuem configuração própria descrita no capítulo 08. Use JTL novo e pasta de dashboard vazia.

## Verificar o repositório

```shell
python scripts/verificar_repositorio.py
python -m unittest discover -s tests -v
node --test tests/test_frontend.cjs
```

Os testes iniciam um servidor em porta efêmera, validam autenticação, regras, CRUD, filtros, arquivos e concorrência. A verificação estática confere caminhos locais, XML SVG/JMX e pares elemento/hashTree do plano. Para confirmar a execução JMeter, rode o comando funcional acima e confira todas as amostras e assertions; XML bem formado sozinho não comprova execução.
