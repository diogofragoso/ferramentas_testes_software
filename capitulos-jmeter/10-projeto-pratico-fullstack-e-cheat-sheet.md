[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md) · [🛡️ Menu ZAP](../capitulos-zap/README.md)

---

# 🪶 Capítulo 10: Projeto integrador e folha de consulta

![Trilha](https://img.shields.io/badge/JMeter-10_de_10-D55A37)

**Objetivo:** aplicar projeto integrador e folha de consulta ao laboratório local, verificando resultados observáveis. Reserve 35–60 minutos.

## Três cenários para entregar

Use o [plano pronto](../exemplos/jmeter/plano_api_e_carga_fullstack.jmx), o [servidor](../exemplos/app-alvo-teste/servidor_fullstack.py) e o [roteiro do laboratório](../exemplos/README.md).

1. **Funcional:** inicie o servidor, rode o plano padrão com 1 thread × 15 linhas. Comprove login, média/status, consulta, PUT/PATCH, exclusão, 404 após exclusão, 400 com nota inválida e 401 sem token. Erros esperados com assertion correta contam como sucesso do teste.
2. **Carga gradual:** use `-Jfuncional=false -Jcarga=true -Jusuarios=50 -Jrampup=50 -Jduracao=120`. Faça antes um ensaio com 5 usuários. O login ocorre uma vez por thread e as consultas incluem 300 ms de pausa. Duração inclui ramp-up; não é um patamar adicional de 120 s.
3. **Integração:** durante uma carga moderada de 5–10 usuários, execute o roteiro visual do [capítulo 12 OculiX](../capitulos/12-testes-hibridos-ui-api.md). Compare tempo percebido na tela e tempo HTTP; a UI introduz 1800 ms intencionais. Registre capturas e resultado sem afirmar igualdade entre tempos de camadas distintas.

## Modelo de entrega

| Campo | Preencher com evidência |
| --- | --- |
| Ambiente | SO, Java/JMeter/Python, CPU/RAM, commit |
| Perfil | Usuários, ramp-up, duração, pausas, dataset |
| Oráculo | Status HTTP, média, status de aprovação, limites |
| Resultado | Amostras, erros, RPS, P50/P95/P99 por operação |
| Evidência | JTL, dashboard, capturas OculiX |
| Análise | Observações, limitações e próxima hipótese |

## Cheat sheet

| Necessidade | Componente / expressão |
| --- | --- |
| Destino comum | HTTP Request Defaults |
| JSON / Bearer | HTTP Header Manager |
| Usuários | Thread Group |
| Token / ID | JSON Extractor: `$.token`, `$.id` |
| Campo de array | `$[0].status` |
| Dado por iteração | CSV Data Set Config |
| Regra de negócio | JSON Assertion |
| Orçamento | Duration Assertion |
| Sessão de cookie | HTTP Cookie Manager |
| Uma vez por thread | Once Only Controller |
| Jornada | Transaction Controller |
| Linha de comando | `-n -t plano.jmx -l resultados.jtl` |
| HTML | `-e -o pasta_nova` |
| Propriedade | `-Jusuarios=10` e `${__P(usuarios,1)}` |

| HTTP | Significado no laboratório |
| --- | --- |
| 200 | Consulta/login/alteração/exclusão bem-sucedidos |
| 201 | Avaliação ou arquivo criado |
| 400 | JSON ou dados inválidos |
| 401 | Credenciais/token inválidos ou ausentes |
| 404 | Rota ou recurso inexistente |

**Glossário:** correlação transporta valores dinâmicos entre requisições; throughput mede vazão; ramp-up distribui partidas; think time simula pausa; percentil descreve distribuição; SLA é compromisso acordado, não um valor escolhido sem contexto. Um teste HTTP não comprova renderização, acessibilidade ou persistência em banco.

## Laboratório guiado

Produza um relatório com uma falha funcional provocada e uma execução corrigida.

<details>
<summary>Gabarito comentado</summary>

Altere temporariamente a média esperada no CSV: a JSON Assertion deve falhar. Restaure a massa, execute novamente e anexe os dois resultados identificados. Não apresente números ilustrativos como medições reais.

</details>

## Checklist

- [ ] Executei o procedimento com o servidor local.
- [ ] Conferi resposta, assertion e evidência.
- [ ] Consigo explicar o resultado e uma limitação do ensaio.

## Referências

Consulte a [referência oficial dos componentes](https://jmeter.apache.org/usermanual/component_reference.html) e o [manual de execução](https://jmeter.apache.org/usermanual/get-started.html).

---

[← Anterior](09-metricas-listeners-cli-e-relatorio-html.md) · [Menu](README.md) · [Integração OculiX →](../capitulos/12-testes-hibridos-ui-api.md)
