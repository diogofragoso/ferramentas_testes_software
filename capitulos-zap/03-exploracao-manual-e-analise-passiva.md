[🏠 Hub](../README.md) · [🛡️ Menu ZAP](README.md)

# Capítulo 03: Exploração manual e análise passiva

**Objetivo:** observar uma jornada real e relacionar um alerta à resposta HTTP. Reserve 40 minutos.

## 1. Executar uma jornada

1. Selecione **Safe Mode** e abra o navegador por **Manual Explore**, como no capítulo anterior.
2. Visite `http://localhost:8081/` e faça login com `estudante_qa` / `oculix123`.
3. Preencha o nome `Aula ZAP`, nota 1 igual a `8` e nota 2 igual a `6`; acione o cálculo.
4. Confira média `7` (a interface pode mostrar `7.0`) e situação **APROVADO**.
5. Abra `/api/health` no mesmo navegador e retorne ao ZAP.
6. Em **History**, localize o POST `/api/auth/login` e o POST `/api/avaliacoes?latencia_ms=1800`. Observe a resposta 200 do login e a 201 da criação.

O teste passivo inspeciona mensagens que passam pelo ZAP sem inserir ataques. As ações normais do navegador, como cadastrar uma avaliação, continuam alterando o estado da aplicação. Referência: [Passive Scan](https://www.zaproxy.org/docs/desktop/start/features/pscan/).

## 2. Ler uma troca HTTP

Selecione a criação de avaliação e compare:

| Parte | O que procurar |
| --- | --- |
| Request | Método POST e caminho `/api/avaliacoes` |
| Cabeçalhos enviados | `Content-Type: application/json` e `Authorization: Bearer ...` |
| Corpo enviado | `nome`, `nota1: 8`, `nota2: 6` |
| Response | Status 201, `id`, `media: 7` e `status: "APROVADO"` |

O token retornado no login é usado pela interface nas chamadas protegidas. Nas evidências compartilhadas, substitua seu valor por `[REMOVIDO]`.

## 3. Examinar a análise passiva

1. Aguarde a fila de análise passiva chegar a zero no indicador do ZAP antes de registrar os resultados.
2. Abra **Alerts** e filtre os alertas para URLs no escopo.
3. Expanda um alerta e selecione uma ocorrência. Leia URL, risco, confiança, descrição, evidência e solução.
4. Localize a resposta associada e compare o conteúdo com a descrição do alerta.

Podem aparecer avisos sobre ausência de Content Security Policy ou proteção contra enquadramento. São possibilidades, não resultados garantidos: regras e complementos influenciam a saída. O servidor didático não define esses cabeçalhos, mas a classificação e a relevância precisam de revisão. Consulte a [aba Alerts](https://www.zaproxy.org/docs/desktop/ui/tabs/alerts/).

## Exercício e evidência

Escolha uma ocorrência e escreva: “O ZAP sinalizou ___ na URL ___. A resposta mostra ___. Para avaliar o impacto ainda preciso de ___”. Se não houver alertas, registre as URLs observadas, a fila concluída e os limites da exploração.

<details>
<summary>Exemplo de interpretação</summary>

Uma resposta HTML sem cabeçalho de proteção contra enquadramento merece análise do risco de clickjacking. A ausência do cabeçalho, sozinha, não demonstra que uma ação sensível foi explorada. Em uma API JSON, a relevância pode ser diferente da página HTML.

</details>

- [ ] Capturei login e criação de avaliação por HTTP.
- [ ] Aguardei a fila passiva terminar.
- [ ] Relacionei um alerta à evidência, ou documentei sua ausência.

[← Anterior](02-interface-proxy-e-escopo.md) · [Menu](README.md) · [Próximo: varredura ativa →](04-spider-e-varredura-ativa.md)
