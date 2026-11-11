[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md) · [🛡️ Menu ZAP](../capitulos-zap/README.md)

---

# 🪶 Capítulo 03: CRUD REST passo a passo

![Trilha](https://img.shields.io/badge/JMeter-03_de_10-D55A37)

**Objetivo:** aplicar crud rest passo a passo ao laboratório local, verificando resultados observáveis. Reserve 35–60 minutos.

## Preparar o plano

1. Adicione HTTP Request Defaults no grupo: Protocol `http`, Server `localhost`, Port `8080`.
2. Adicione HTTP Header Manager: `Content-Type: application/json` e `Accept: application/json`.
3. Faça login e extraia o token conforme o [capítulo 05](05-correlacao-autenticacao-jwt-e-sessoes.md). Todas as rotas de avaliações exigem Bearer.
4. No HTTP Request, use **Body Data** para JSON; não preencha Parameters ao mesmo tempo para esse corpo.

| Ordem | Método e caminho | Corpo / resultado |
| --- | --- | --- |
| 1 | POST /api/avaliacoes | `{"nome":"Ana","nota1":8.5,"nota2":9.5}` → 201, média 9 |
| 2 | GET /api/avaliacoes/${ID_AVALIACAO} | 200, mesmo registro |
| 3 | PUT /api/avaliacoes/${ID_AVALIACAO} | `{"nome":"Ana","nota1":6,"nota2":6}` → média 6 |
| 4 | PATCH /api/avaliacoes/${ID_AVALIACAO} | `{"nota2":8}` → média 7 |
| 5 | GET /api/avaliacoes?status=APROVADO | 200, array filtrado |
| 6 | DELETE /api/avaliacoes/${ID_AVALIACAO} | 200, removido true |
| 7 | GET /api/avaliacoes/${ID_AVALIACAO} | 404 após exclusão |

Extraia `$.id` do POST com JSON Extractor, variável `ID_AVALIACAO`, match 1, default `ID_AUSENTE`. Não fixe `/1`: execuções concorrentes criam IDs diferentes. O PUT exige nome e ambas as notas; PATCH aceita alteração parcial. Notas devem ser números JSON finitos entre 0 e 10. Aprovação considera a média real ≥ 7; a API apresenta duas casas de precisão e a UI uma.

## Inspecionar o protocolo

Na View Results Tree, Sampler Result mostra status e tempos, Request mostra headers/corpo enviado e Response Data apresenta o JSON. Selecione o renderizador JSON/JSON Path Tester disponível e teste `$.media` no objeto criado. A listagem é um array, portanto use `$[0].media` para seu primeiro elemento.

Não use o tempo artificial da interface como SLA da API: a UI chama `?latencia_ms=1800` para ensinar sincronização. Chamadas diretas não têm atraso artificial por padrão.

## Laboratório guiado

Crie uma avaliação reprovada, transforme-a em aprovada por PATCH e remova-a.

<details>
<summary>Gabarito comentado</summary>

POST com 4 e 6 produz média 5; PATCH com nota1=10 produz média 8. Extraia o id de cada POST e use esse id no PATCH e DELETE. Guarde o JSON de cada etapa como evidência.

</details>

## Checklist

- [ ] Executei o procedimento com o servidor local.
- [ ] Conferi resposta, assertion e evidência.
- [ ] Consigo explicar o resultado e uma limitação do ensaio.

## Referências

Consulte a [referência oficial dos componentes](https://jmeter.apache.org/usermanual/component_reference.html) e o [manual de execução](https://jmeter.apache.org/usermanual/get-started.html).

---

[← Anterior](02-conhecendo-a-interface-jmeter.md) · [Menu](README.md) · [Próximo →](04-assercoes-e-validacoes-de-api.md)
