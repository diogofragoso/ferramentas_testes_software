[🏠 Hub](../README.md) · [🛡️ Menu ZAP](README.md)

# Capítulo 06: Alertas, relatório e projeto prático

**Objetivo:** transformar os resultados em uma entrega revisável. Reserve 45 minutos.

## 1. Revisar os alertas

1. Confirme que Spider e Active Scan terminaram e a fila passiva chegou a zero.
2. Em **Alerts**, filtre para URLs no escopo e selecione uma ocorrência.
3. Leia risco e confiança separadamente: risco descreve a gravidade potencial; confiança expressa a certeza da detecção.
4. Compare URL, método, parâmetro e evidência com a mensagem HTTP correspondente.
5. Classifique sua revisão como confirmado, pendente de investigação ou falso positivo justificado. Preserve a evidência antes de alterar a classificação no ZAP.

Um mesmo tipo de alerta pode ter várias ocorrências. Conte tipos e ocorrências separadamente e evite interpretar toda observação informativa como vulnerabilidade explorável. Consulte [Alerts](https://www.zaproxy.org/docs/desktop/ui/tabs/alerts/).

## 2. Gerar o relatório HTML

1. Abra **Report → Generate Report**.
2. Em **Scope**, preencha título, nome e pasta do relatório. Selecione somente o contexto `Laboratorio-ZAP` e o site `http://localhost:8081`.
3. Em **Template**, escolha um modelo HTML disponível.
4. Em **Filter**, confira os níveis de risco e confiança incluídos. Registre qualquer exclusão.
5. Gere o arquivo e abra-o. Confira o alvo, os totais e as ocorrências.
6. Se não houver alertas, marque **Generate If No Alerts** e descreva a cobertura no texto da entrega.

Se a opção não estiver disponível, instale ou habilite **Report Generation** em **Manage Add-ons**. Veja os campos no [manual de geração de relatórios](https://www.zaproxy.org/docs/desktop/addons/report-generation/).

Revise relatório, capturas e sessão antes de compartilhar: mensagens podem conter credenciais, tokens e dados enviados. A sessão persistida permite retomar a investigação; o HTML registra os resultados exportados.

## 3. Preencher uma ficha de achado

Copie o modelo e substitua os campos com dados observados:

```text
ID / título:
Data / responsável:
Ambiente: Windows, ZAP 2.17.0, Java __, complementos __
Alvo / método / parâmetro:
Origem: análise passiva, ativa ou teste manual
Risco informado pelo ZAP / confiança:
Passos para reproduzir:
Resultado esperado:
Resultado observado:
Evidência HTTP sanitizada:
Impacto e condições necessárias:
Estado da revisão e justificativa:
Correção proposta:
Passos e resultado do reteste:
Limitações:
```

Exemplo de proposta: para um alerta de ausência de CSP em HTML, estudar uma política compatível com os scripts e estilos da página. O laboratório possui conteúdo inline; simplesmente adicionar uma política restritiva pode quebrar a interface. A correção precisa preservar a jornada funcional e ser verificada novamente.

## 4. Projeto de conclusão

1. Registre versões, alvo, contexto e modos usados.
2. Execute login e cálculo de média 7, guardando evidências de UI e HTTP.
3. Compare descoberta manual e Spider; faça a varredura pequena do capítulo 04.
4. Execute os três casos de autenticação do capítulo 05.
5. Exporte o HTML e anexe uma ficha revisada. Se não houver alertas, documente essa condição e escolha uma melhoria para investigar, identificada como hipótese.
6. Proponha um reteste após correção, repetindo a requisição relevante e a jornada funcional. Só registre “corrigido” após executá-lo.

| Critério de avaliação | Evidência mínima |
| --- | --- |
| Escopo | Contexto restrito ao localhost:8081 e modo registrado |
| Exploração | Login e avaliação encontrados em History |
| Cobertura | URLs descobertas versus URLs efetivamente testadas |
| Autenticação | Tabela 200/401/401 com esperado e obtido |
| Análise | Achado com evidência ou ausência de achados contextualizada |
| Comunicação | HTML revisado, limitações e plano de reteste |

## Folha de consulta

| Preciso… | Caminho |
| --- | --- |
| Iniciar o alvo | `python exemplos/app-alvo-teste/servidor_fullstack.py --port 8081` |
| Abrir navegador com proxy | Quick Start → Manual Explore |
| Observar sem ataques automáticos | Safe Mode e navegação manual |
| Executar ações no escopo | Protected Mode |
| Analisar um nó | History/Sites → Attack → Active Scan |
| Reenviar uma mensagem | History → Open/Resend with Request Editor |
| Exportar resultados | Report → Generate Report |
| Encerrar a aula | Parar scans, fechar navegador do ZAP e encerrar Python com Ctrl+C |

Integre a entrega aos [testes de UI](../capitulos/12-testes-hibridos-ui-api.md) e aos [testes de API e desempenho](../capitulos-jmeter/10-projeto-pratico-fullstack-e-cheat-sheet.md). A análise automatizada não substitui investigação manual de regras de negócio e controle de acesso, conforme os [limites do Active Scan](https://www.zaproxy.org/docs/desktop/start/features/ascan/).

[← Anterior](05-api-jwt-e-autenticacao.md) · [Menu ZAP](README.md) · [Voltar ao portal →](../README.md)
