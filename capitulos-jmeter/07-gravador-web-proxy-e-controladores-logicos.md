[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md) · [🛡️ Menu ZAP](../capitulos-zap/README.md)

---

# 🪶 Capítulo 07: Gravador proxy e jornadas

![Trilha](https://img.shields.io/badge/JMeter-07_de_10-D55A37)

**Objetivo:** aplicar gravador proxy e jornadas ao laboratório local, verificando resultados observáveis. Reserve 35–60 minutos.

## Capturar o tráfego da interface

1. Inicie o servidor local. Em Test Plan → Add → Non-Test Elements, adicione HTTP(S) Test Script Recorder; crie também Thread Group → Recording Controller.
2. No recorder escolha porta 8888 e Target Controller apontando para Recording Controller. Use o template Recording se preferir uma árvore inicial.
3. Configure o proxy HTTP do navegador dedicado para `localhost:8888`. No Firefox, a captura de localhost pode exigir `network.proxy.allow_hijacking_localhost=true` em about:config; anote o valor anterior para restaurar.
4. Para HTTPS, inicie o recorder para gerar `ApacheJMeterTemporaryRootCA.crt` e importe esse certificado somente no perfil de teste. O laboratório HTTP não exige certificado. Remova a confiança e desative o proxy ao terminar.
5. Exclua estáticos com `.*\.(bmp|css|js|gif|ico|jpe?g|png|swf|woff2?)(\?.*)?$`.
6. Navegue em `http://localhost:8080`, faça login e processe uma avaliação. O modo `file://` não gera chamadas REST para capturar.
7. Pare a gravação; substitua tokens e IDs capturados por extratores do capítulo 05. Remova headers de transporte gravados que não sejam necessários.

## Modelar uma jornada

| Controller | Receita | Cuidado |
| --- | --- | --- |
| Once Only | Login uma vez por thread | Escopo/loops aninhados afetam o comportamento |
| Transaction | Agrupar perfil + listagem | Decide se inclui timers e gera amostra pai |
| If | `${JMeterThread.last_sample_ok}` | Interpret condition as variable expression selecionado |
| While | `${__groovy(vars.get('continuar') == 'true')}` | Atualize a variável e imponha limite para não ficar infinito |
| Loop | Repetir uma busca 5 vezes | Não equivale a 5 usuários |
| Throughput | Percent execution 70 / 20 / 10 | Percentual de execuções, não limite de RPS |

Crie três Throughput Controllers para leitura (70), cadastro (20) e relatório (10). São decisões independentes ao longo das iterações, não uma seleção mutuamente exclusiva garantida. Para exatamente uma rota por iteração, gere um número 1..100 em pré-processador e use If Controllers com faixas sem sobreposição. O laboratório não tem rota de relatório; use health como operação substituta identificada.

## Laboratório guiado

Grave um cadastro e identifique dois valores que não podem permanecer fixos.

<details>
<summary>Gabarito comentado</summary>

Authorization precisa vir do login de cada thread; o id precisa vir da criação daquela avaliação. Uma gravação sem correlação tende a falhar na próxima execução ou a editar o registro de outro usuário.

</details>

## Checklist

- [ ] Executei o procedimento com o servidor local.
- [ ] Conferi resposta, assertion e evidência.
- [ ] Consigo explicar o resultado e uma limitação do ensaio.

## Referências

Consulte a [referência oficial dos componentes](https://jmeter.apache.org/usermanual/component_reference.html) e o [manual de execução](https://jmeter.apache.org/usermanual/get-started.html).

---

[← Anterior](06-testes-orientados-a-dados-csv-e-variaveis.md) · [Menu](README.md) · [Próximo →](08-timers-banco-de-dados-jdbc-e-upload.md)
