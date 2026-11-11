# Validação da implementação Full Stack

## Inclusão da trilha ZAP 2.17 — 11/11/2026

- Conferidos os procedimentos com a documentação oficial do ZAP, incluindo o [guia da versão 2.17](https://www.zaproxy.org/pdf/ZAPGettingStartedGuide-2.17.pdf).
- Verificadas 371 referências locais de Markdown/HTML, incluindo os seis capítulos novos e os links de navegação para a trilha ZAP.
- Conferidos fechamento de blocos de código e elementos `details` da trilha, leitura dos XML SVG/JMX e `git diff --check`, sem erros.
- O launcher `py -3` aponta para um Python inexistente neste ambiente. A checagem de caminhos foi executada com Node.js e a leitura XML com PowerShell; o verificador Python não foi executado nesta atualização.
- A interface do ZAP, a captura pelo navegador, o Spider, o scan ativo e a exportação HTML **não foram executados neste ambiente**. São procedimentos documentados para validação prática pelo estudante; não há contagem de alertas ou resultado de scan apresentado como medido.
- Alteração restrita à documentação e navegação; servidor, interface do laboratório e planos JMeter não foram modificados.

## Validação anterior do laboratório

Executada em 10/11/2026, Windows, Python 3.13.9 portátil, Node.js 24.13.0, Java 25 e Apache JMeter 5.6.3.

| Verificação | Resultado |
| --- | --- |
| Contrato HTTP | 7 testes aprovados: JWT, expiração, CRUD, filtros, limites, upload/download e IDs concorrentes |
| Interface JavaScript | 3 testes aprovados: offline, chamadas online/falhas e limpeza durante requisição |
| Integridade | Caminhos locais de Markdown/HTML existentes e XML SVG/JMX válido |
| JMeter funcional | 151 amostras, 15 criações orientadas a CSV, zero falhas |
| JMeter carga curta | 3 threads, ramp-up 2 s, duração 6 s, 54 amostras, zero falhas |
| Dashboards | HTML funcional e de carga gerados com sucesso |
| Diff | Sem erros de whitespace |

O ensaio curto confirma a execução do plano e de seus parâmetros; não demonstra capacidade de produção. A execução funcional confirma também que 400/401/404 esperados são classificados corretamente e que as extrações de token/ID e assertions de negócio funcionam no JMeter.

Os testes JavaScript executam o script real do HTML em um DOM simulado; não validam layout ou diálogos de SO. A revisão visual no GitHub, a automação real no OculiX, o proxy HTTPS e JDBC permanecem como atividades manuais descritas nos capítulos. Imagens usadas pelos scripts OculiX devem ser capturadas no ambiente do estudante.

Para reproduzir as verificações, consulte os comandos em [exemplos/README.md](exemplos/README.md), o [verificador de integridade](scripts/verificar_repositorio.py), os [testes HTTP](tests/test_servidor_fullstack.py) e os [testes da interface](tests/test_frontend.cjs). Runtimes baixados e relatórios locais ficam em `.tools/`, ignorada pelo Git; não são dependências do material distribuído.
