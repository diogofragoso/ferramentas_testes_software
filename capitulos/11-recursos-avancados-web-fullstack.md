[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md)

---

# 🦎 Capítulo 11: Recursos avançados para Web Full Stack

**Objetivo:** automatizar arquivos, listagens, observadores, CSV e gráficos. Pré-requisito: capítulos 01–10. Os exemplos usam Jython 2.7 do OculiX; o servidor separado usa Python 3. Imagens como `enviar.png` são capturas que você deve criar no seu próprio ambiente e salvar no pacote `.sikuli`.

## 1. Upload e download em diálogos nativos

Inicie o laboratório e faça login. Clique no campo de arquivo e capture o botão de seleção. No Windows, digite o caminho absoluto no campo Nome do arquivo do diálogo Abrir e confirme.

```python
from sikuli import *
import os

arquivo = os.path.join(getBundlePath(), "comprovante.txt")
assert os.path.isfile(arquivo)
click("selecionar_arquivo.png")
wait("dialogo_abrir.png", 5)
paste(arquivo)
type(Key.ENTER)
wait("arquivo_selecionado.png", 5)
click("enviar_comprovante.png")
wait("comprovante_enviado.png", 10)
click("baixar_comprovante.png")
```

Copie antes o [comprovante](../exemplos/jmeter/comprovante.txt) para o bundle. O navegador pode salvar diretamente em Downloads; para exercitar Salvar como, habilite perguntar onde salvar nas configurações. Capture o diálogo do seu SO; não presuma que <kbd>Enter</kbd> confirma o mesmo campo em todos os sistemas. Confira o arquivo baixado pelo tamanho/conteúdo, além do toast visual.

## 2. Vários elementos com findAll

Em uma página do projeto que tenha cards ou linhas repetidas, capture um ícone exclusivo de cada linha e restrinja a região à tabela. O laboratório de notas tem apenas um painel de resultado, portanto não invente uma listagem nele.

```python
tabela = Region(100, 200, 800, 400)  # ajuste à sua tela
if tabela.exists("icone_linha.png", 3):
    linhas = list(tabela.findAll("icone_linha.png"))
    linhas.sort(key=lambda m: (m.getY(), m.getX()))
    assert len(linhas) >= 2
    for linha in linhas:
        linha.highlight(0.3)
```

`findAll` retorna um iterador e pode gerar FindFailed se não houver correspondências. A ordem visual não é garantida: converta em lista e ordene. Elementos fora da área visível exigem rolagem e deduplicação por informação estável, não por coordenadas antigas.

## 3. CSV no OculiX

Copie a massa CSV para o bundle. Capture o campo de nome, de cada nota e os botões. No Jython 2.7, csv trabalha com bytes; decodifique nomes UTF-8 ao colar:

```python
import csv
import os

with open(os.path.join(getBundlePath(), "massa_estudantes.csv"), "rb") as massa:
    for caso in csv.DictReader(massa):
        click("limpar_formulario.png")
        click("campo_nome.png")
        paste(caso["nome"].decode("utf-8"))
        click("campo_nota1.png")
        paste(caso["nota1"])
        click("campo_nota2.png")
        paste(caso["nota2"])
        click("processar.png")
        esperado = "aprovado.png" if caso["status_esperado"] == "APROVADO" else "reprovado.png"
        wait(esperado, 10)
        assert exists(esperado)
```

Capture o badge completo para distinguir APROVADO de REPROVADO. O conjunto tem 15 linhas; acrescente 5 para exercitar 20 entradas. Execute sem mexer no teclado e mantenha a escala de tela constante.

## 4. Observadores e notificações

```python
avisos = Region(50, 100, 900, 600)  # ajuste
eventos = []
def apareceu(event):
    eventos.append("erro_visual")
    event.stopObserver()

avisos.onAppear("erro_api.png", apareceu)
avisos.observeInBackground(30)
try:
    click("processar.png")
    wait("aprovado.png", 10)
finally:
    avisos.stopObserver()
assert not eventos, "Mensagem de erro apareceu durante a jornada"
```

`observe(30)` observa de forma bloqueante; `observeInBackground(30)` permite continuar o roteiro. `onVanish` registra o desaparecimento. Restrinja a região, encerre sempre o observador e evite clicar dentro do callback, concorrendo com o roteiro principal. Um toast muito curto pode escapar ao intervalo de varredura; prefira um oráculo persistente quando disponível.

## 5. Canvas e responsividade

O laboratório desenha uma barra em `<canvas>` depois do processamento. Capture a região da barra aprovada e reprovada em escala fixa, compare-a com `Pattern(...).similar(0.9)` e confira o badge e a média por OCR. Pixels comprovam aparência; a API comprova o valor numérico.

No Chromium, abra DevTools com <kbd>F12</kbd> e alterne Device Toolbar com <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd>. Esses atalhos dependem do navegador. Teste uma largura móvel e outra desktop, recapture padrões por viewport e verifique se formulário, resultado e upload continuam acessíveis; a emulação não substitui um dispositivo real.

## Laboratório

Envie o comprovante, execute duas linhas do CSV e registre a barra correspondente. Provoque um token inválido reiniciando o servidor após o login para exercitar o erro visual.

<details>
<summary>Gabarito comentado</summary>

O upload exibe o nome do arquivo, o download preserva seu conteúdo, nota 7 aprova e nota 6 reprova. Após reiniciar o servidor, o token antigo causa 401; a interface informa falha em vez de apresentar resultado falso. Faça novo login antes de repetir. Salve capturas e anote viewport/DPI.

</details>

Referências: [Jython no OculiX](https://www.oculix.org/guides/jython/) e [Region / observadores](https://docs.oculix.org/region/).

---

[← Capítulo 10](10-glossario-e-folha-de-consulta.md) · [Menu](README.md) · [Capítulo 12 →](12-testes-hibridos-ui-api.md)
