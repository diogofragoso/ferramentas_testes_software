[🏠 Hub](../README.md) · [🛡️ Menu ZAP](README.md)

# Capítulo 04: Spider e varredura ativa

**Objetivo:** descobrir URLs e executar uma análise ativa pequena e delimitada. Reserve 40 minutos.

## 1. Preparar o ensaio

1. Termine e registre a etapa passiva antes de continuar.
2. Confira o contexto `Laboratorio-ZAP`, sua expressão `^http://localhost:8081/.*$` e a opção **In Scope**.
3. Selecione **Protected Mode** na barra superior.
4. Use apenas dados descartáveis. Se necessário, pare e reinicie o servidor com o comando do capítulo 01; isso apaga os dados e invalida o JWT anterior.

## 2. Descobrir URLs com o Spider

1. Em **Sites**, clique com o botão direito no nó `http://localhost:8081`.
2. Escolha **Attack → Spider**. Confira a URL inicial e, se disponível, selecione somente o contexto da aula.
3. Inicie a descoberta e acompanhe a aba **Spider** até terminar.
4. Compare as URLs descobertas com as capturadas durante a navegação manual.

O Spider tradicional segue referências na aplicação e não reproduz toda a interação JavaScript. Por isso, o formulário que você preencheu manualmente pode revelar chamadas de API que ele não percorreu. O AJAX Spider usa navegador e pode ampliar essa exploração, mas exige complementos e navegador compatíveis. Ele é opcional nesta trilha. Veja o [guia de exploração oficial](https://www.zaproxy.org/getting-started/).

## 3. Executar uma varredura pequena

1. No navegador do ZAP, visite `http://localhost:8081/api/health?latencia_ms=0` para registrar uma requisição com parâmetro.
2. Em **History**, selecione essa requisição exata e escolha **Attack → Active Scan**.
3. Confira o destino: `localhost`, porta `8081`, caminho `/api/health`. Desmarque **Recurse**, caso apareça, para testar somente o nó selecionado.
4. Mantenha a política padrão para este primeiro ensaio e inicie **Scan**.
5. Acompanhe **Active Scan**. Se o alvo ficar indisponível, use **Stop** nessa aba e registre a interrupção.
6. Ao terminar, aguarde também a fila passiva zerar. Registre duração, URL analisada e alertas observados.

A análise ativa envia ataques ao destino selecionado; não equivale a uma auditoria completa. Esta execução cobre somente o endpoint health e seus parâmetros, sem demonstrar cobertura das rotas protegidas. Referência: [Active Scan](https://www.zaproxy.org/docs/desktop/start/features/ascan/).

## 4. Conhecer o atalho Automated Scan

**Quick Start → Automated Scan** permite informar uma URL, selecionar os mecanismos de descoberta e clicar em **Attack** para combinar descoberta e análise ativa. Para repetir com o laboratório, confira primeiro o escopo em Protected Mode e use somente `http://localhost:8081/`.

Esse atalho pode ampliar o volume e o conjunto de requisições em relação ao ensaio de um nó. Não é necessário executá-lo para concluir a aula. O login feito no navegador não configura automaticamente a autenticação do scanner. Referência: [guia 2.17](https://www.zaproxy.org/pdf/ZAPGettingStartedGuide-2.17.pdf).

## Exercício e evidência

Monte uma tabela com URLs vistas manualmente, URLs encontradas pelo Spider e URL efetivamente analisada. Explique por que “100% concluído” no scanner não significa “100% da aplicação testada”.

- [ ] Usei Protected Mode e conferi o destino antes de iniciar.
- [ ] Diferenciei descoberta de URLs e teste ativo.
- [ ] Registrei a cobertura real, mesmo sem alertas.

[← Anterior](03-exploracao-manual-e-analise-passiva.md) · [Menu](README.md) · [Próximo: API e JWT →](05-api-jwt-e-autenticacao.md)
