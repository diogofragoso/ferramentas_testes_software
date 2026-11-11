[🏠 Hub](../README.md) · [🛡️ Menu ZAP](README.md)

# Capítulo 02: Interface, proxy e escopo

**Objetivo:** capturar uma requisição e limitar as ações ao laboratório. Reserve 30 minutos.

## 1. Localizar os painéis

| Painel | Uso na aula |
| --- | --- |
| Quick Start | Abrir navegador pelo ZAP |
| Sites | Encontrar URLs visitadas |
| History | Selecionar uma troca HTTP |
| Request / Response | Ler método, cabeçalhos e corpo |
| Alerts | Investigar possíveis problemas |
| Spider / Active Scan | Acompanhar descoberta e testes ativos |

Veja o [mapa oficial da interface](https://www.zaproxy.org/docs/desktop/ui/).

## 2. Abrir o navegador pelo ZAP

1. Com o laboratório ativo, abra **Quick Start → Manual Explore**.
2. Informe `http://localhost:8081/` em **URL to explore**.
3. Escolha um navegador instalado, como Firefox ou Chrome, e clique em **Launch Browser**. Para simplificar a aula, deixe o HUD desativado, se a opção aparecer.
4. No navegador lançado, abra também `http://localhost:8081/api/health`.
5. Volte ao ZAP. Em **History**, selecione o GET dessa rota e confira o status 200 em **Response**.

Esse navegador é iniciado com o proxy configurado. Se a abertura falhar, verifique os complementos Selenium/WebDriver em **Manage Add-ons** e a compatibilidade com o navegador instalado. Evite mudar o proxy do navegador pessoal para esta aula. Procedimento: [guia de início rápido 2.17](https://www.zaproxy.org/pdf/ZAPGettingStartedGuide-2.17.pdf).

## 3. Criar o contexto da aula

1. Em **Sites**, clique com o botão direito em `http://localhost:8081`.
2. Escolha **Include in Context → New Context** e dê o nome `Laboratorio-ZAP`.
3. Abra as propriedades do contexto e confira **Include in Context**. Use apenas a expressão abaixo para incluir o alvo:

```regex
^http://localhost:8081/.*$
```

4. Na configuração do contexto, marque **In Scope**. Remova inclusões amplas que tenham sido criadas automaticamente.
5. Mantenha os demais contextos fora do escopo. Use sempre `localhost`; a URL `127.0.0.1` não corresponde à expressão acima.

Contextos agrupam URLs por expressões regulares que precisam corresponder à URL inteira. Referência: [Contexts](https://www.zaproxy.org/docs/desktop/start/features/contexts/).

## 4. Entender os modos

| Modo | Comportamento |
| --- | --- |
| Safe | Bloqueia operações potencialmente perigosas; use na exploração passiva |
| Protected | Permite essas operações somente em URLs no escopo |
| Standard | Não impõe essa restrição de escopo |
| ATTACK | Inicia análise ativa de novos nós no escopo automaticamente |

Nas próximas etapas, use **Protected** somente quando solicitado. O modo persiste entre sessões: confira-o ao abrir o programa. Referência: [Modes](https://www.zaproxy.org/docs/desktop/start/features/modes/).

## Exercício e evidência

Capture o contexto e a requisição GET `/api/health`. Sem enviar tráfego a outros destinos, confira por leitura da expressão: `http://localhost:8081/api/health` está incluída; `http://localhost:8080/` e `http://example.com/` estão excluídas.

- [ ] Requisição do navegador aparece em History.
- [ ] Contexto inclui somente o laboratório na porta 8081.
- [ ] Sei distinguir contexto, escopo e modo.

[← Anterior](01-introducao-instalacao-e-laboratorio.md) · [Menu](README.md) · [Próximo: análise passiva →](03-exploracao-manual-e-analise-passiva.md)
