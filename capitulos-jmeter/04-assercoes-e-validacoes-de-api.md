[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md)

---

# 🪶 Capítulo 04: Asserções e oráculos

![Trilha](https://img.shields.io/badge/JMeter-04_de_10-D55A37)

**Objetivo:** aplicar asserções e oráculos ao laboratório local, verificando resultados observáveis. Reserve 35–60 minutos.

## Construir validações úteis

Um HTTP 200 com média errada é uma falha de negócio. Em cada sampler, clique Add → Assertions e combine status, conteúdo e orçamento de tempo.

| Assertion | Configuração de exemplo | Falha que encontra |
| --- | --- | --- |
| Response Assertion | Response Code, Equals, `201` | Criação não ocorreu |
| Response Assertion | Response Headers, Contains, `application/json` | Formato inesperado |
| JSON Assertion | JSONPath `$.status`, Assert value, `APROVADO` | Regra incorreta |
| JSON Assertion | JSONPath `$.media`, Assert value, `9` | Cálculo incorreto |
| Duration Assertion | Duration `500` ms | Resposta acima do orçamento didático |
| Size Assertion | Response Body, maior que `2` bytes | Corpo vazio |

Response Message pode validar uma mensagem de protocolo, mas não substitui o código. Contains/Matches tratam padrões como expressões regulares; Substring/Equals fazem comparação literal conforme a opção escolhida. Evite comparar JSON inteiro: ordem de propriedades e espaços podem mudar.

## Fluxos negativos que devem passar

1. Envie POST com nota1=15 usando token válido: espere 400 e `$.erro` existente.
2. Envie GET /api/avaliacoes sem Authorization: espere 401.
3. Faça login com senha incorreta: espere 401 e ausência de token.
4. Consulte um ID excluído: espere 404.

Para um erro HTTP esperado, marque **Ignore Status** na Response Assertion e compare Response Code com o erro exato. Isso redefine o sucesso HTTP para essa amostra; mantenha as demais assertions para que um erro inesperado continue falhando. Não aplique Ignore Status globalmente.

O plano pronto inclui 400/401/404 esperados e validação de média/status por CSV. O limite de 500 ms é uma hipótese para o exercício, não uma garantia para todo computador. `latencia_ms=800` permite provocar uma falha de duração controlada.

## Laboratório guiado

Faça a asserção de duração falhar e depois corrija o cenário sem remover o oráculo.

<details>
<summary>Gabarito comentado</summary>

GET /api/health?latencia_ms=800 excede 500 ms. Remova o atraso para o teste normal ou documente um orçamento coerente para a jornada; não esconda uma regressão elevando o limite sem justificativa.

</details>

## Checklist

- [ ] Executei o procedimento com o servidor local.
- [ ] Conferi resposta, assertion e evidência.
- [ ] Consigo explicar o resultado e uma limitação do ensaio.

## Referências

Consulte a [referência oficial dos componentes](https://jmeter.apache.org/usermanual/component_reference.html) e o [manual de execução](https://jmeter.apache.org/usermanual/get-started.html).

---

[← Anterior](03-testando-apis-rest-fullstack.md) · [Menu](README.md) · [Próximo →](05-correlacao-autenticacao-jwt-e-sessoes.md)
