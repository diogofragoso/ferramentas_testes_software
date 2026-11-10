[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md)

---

# 📚 Catálogo prático de comandos e combinações do OculiX

Material de consulta do [capítulo 03](03-primeiro-script-e-captura-de-tela.md). Encontre a ação desejada, capture os elementos na sua tela e adapte a sequência. Os exemplos são independentes: não execute uma tabela inteira como se fosse um único roteiro.

**Como usar:** onde aparece `"botao.png"`, insira sua captura pelo IDE; ela será mostrada como miniatura. Textos como `"Ana Silva"` são dados para preencher. As imagens citadas precisam existir no seu bundle `.sikuli`; não são arquivos fornecidos por este catálogo.

Os comandos pressupõem o editor Jython do OculiX, que disponibiliza a API de automação. Se seu ambiente exigir importação explícita, coloque `from sikuli import *` no início. Os atalhos de aplicativos abaixo usam Windows/Linux; no macOS, selecionar/copiar/colar geralmente usam `Key.CMD`. Cada programa define seus próprios atalhos.

## Escolha a categoria

| Categoria | O que consultar |
| --- | --- |
| [1. Cliques](#cliques) | Simples, duplo, direito, com modificador |
| [2. Movimento e arraste](#movimento) | Hover, coordenadas, arrastar, segurar mouse |
| [3. Rolagem](#rolagem) | Rodinha, Page Up/Down, início e fim |
| [4. Texto e edição](#texto) | Colar, digitar, apagar, copiar e desfazer |
| [5. Teclas especiais](#teclas) | Tab, Enter, setas, função e teclado numérico |
| [6. Combinações de teclas](#atalhos) | Ctrl, Shift, Alt e teclas mantidas |
| [7. Navegador](#navegador) | URL, abas, histórico, busca, zoom e recarga |
| [8. Formulários](#formularios) | Campos, checkbox, rádio, lista e calendário |
| [9. Arquivos e diálogos](#arquivos) | Abrir, salvar, upload e download |
| [10. Pausas e esperas](#esperas) | Aguardar presença ou desaparecimento |
| [11. Busca e verificação](#busca) | Encontrar, testar presença, conferir resultado |
| [12. Capturas e evidências](#capturas) | Tela inteira, recorte e segundo monitor |
| [13. Aplicativos e janelas](#aplicativos) | Abrir, focar, alternar e fechar |
| [14. Padrões e regiões](#padroes) | Similaridade, offset, área de busca e OCR |
| [15. Mensagens e execução](#mensagens) | Console, avisos, entrada manual e encerramento |
| [16. Sequências prontas](#sequencias) | Receitas para combinar os comandos |

<a id="cliques"></a>

## 1. Cliques

| Possibilidade | Exemplo direto | Aplicação |
| --- | --- | --- |
| Clique esquerdo em captura | `click("botao_salvar.png")` | Acionar um botão |
| Duplo clique | `doubleClick("icone_pasta.png")` | Abrir item que exige dois cliques |
| Clique direito | `rightClick("registro.png")` | Abrir menu de contexto |
| Clique na posição atual | `click()` | Clicar onde o ponteiro já está |
| Clique em coordenadas | `click(Location(400, 300))` | Ponto conhecido da tela |
| Ctrl + clique | `click("item.png", KeyModifier.CTRL)` | Seleção múltipla, se o programa permitir |
| Shift + clique | `click("ultimo_item.png", KeyModifier.SHIFT)` | Selecionar intervalo após selecionar o primeiro |
| Clicar após esperar | `click(wait("botao_pronto.png", 5))` | Acionar assim que o alvo aparecer |

Coordenadas são pixels da tela e precisam ser ajustadas ao computador. Para botões que mudam de posição, prefira capturas. Um Ctrl + clique depende do contexto: numa lista pode selecionar; num link pode abrir outra aba.

<a id="movimento"></a>

## 2. Movimento do mouse e arraste

| Possibilidade | Exemplo direto | Aplicação |
| --- | --- | --- |
| Mover até uma captura | `hover("menu.png")` | Abrir submenu ou tooltip |
| Mover até um ponto | `hover(Location(400, 300))` | Tirar o ponteiro de cima de um botão |
| Arrastar entre capturas | `dragDrop("cartao.png", "destino.png")` | Quadro de tarefas |
| Arrastar entre pontos | `dragDrop(Location(300, 400), Location(600, 400))` | Slider em posição conhecida |
| Segurar botão esquerdo | `mouseDown(Button.LEFT)` | Início de gesto na posição atual |
| Soltar botão esquerdo | `mouseUp(Button.LEFT)` | Encerrar o gesto |
| Segurar botão direito | `mouseDown(Button.RIGHT)` | Gesto específico do aplicativo |
| Soltar botão direito | `mouseUp(Button.RIGHT)` | Encerrar esse gesto |

Prefira `dragDrop` para arrastar. `mouseDown` deve ser acompanhado de `mouseUp`; não execute a linha de pressionar isoladamente. Para gestos longos, o capítulo 08 explica como tratar interrupções. Um tooltip pode desaparecer quando o mouse sai do alvo: capture-o nesse estado antes de montar o teste.

<a id="rolagem"></a>

## 3. Rolagem e deslocamento da página

| Possibilidade | Exemplo direto | Aplicação |
| --- | --- | --- |
| Rolar para baixo | `wheel(WHEEL_DOWN, 5)` | Avançar alguns passos |
| Rolar para cima | `wheel(WHEEL_UP, 5)` | Voltar alguns passos |
| Avançar uma página | `type(Key.PAGE_DOWN)` | Deslocar o painel com foco |
| Voltar uma página | `type(Key.PAGE_UP)` | Deslocamento inverso |
| Início da linha | `type(Key.HOME)` | Campo de texto |
| Fim da linha | `type(Key.END)` | Campo de texto |
| Início do conteúdo | `type(Key.HOME, Key.CTRL)` | Documento ou página com foco |
| Fim do conteúdo | `type(Key.END, Key.CTRL)` | Ir ao final, se suportado |

Antes de `wheel`, posicione o mouse no painel correto com `hover("painel.png")`. Antes de teclas de navegação, confira qual controle tem foco. Se houver um campo de texto selecionado, Ctrl + End pode mover o cursor dentro dele em vez de rolar a página.

<a id="texto"></a>

## 4. Preenchimento, seleção e edição de texto

| Possibilidade | Exemplo direto | Aplicação |
| --- | --- | --- |
| Colar texto | `paste("Ana Silva")` | Campo já selecionado |
| Clicar e colar | `paste("campo_nome.png", "Ana Silva")` | Preencher em uma linha |
| Digitar caracteres | `type("12345")` | Simular digitação |
| Clicar e digitar | `type("campo_codigo.png", "12345")` | Preencher código |
| Selecionar tudo | `type("a", Key.CTRL)` | Preparar substituição |
| Apagar à esquerda | `type(Key.BACKSPACE)` | Remover seleção ou caractere anterior |
| Apagar à direita | `type(Key.DELETE)` | Remover seleção ou próximo caractere |
| Copiar seleção | `type("c", Key.CTRL)` | Copiar conteúdo do aplicativo |
| Recortar seleção | `type("x", Key.CTRL)` | Mover conteúdo editável |
| Colar área de transferência | `type("v", Key.CTRL)` | Colar o que foi copiado antes |
| Desfazer | `type("z", Key.CTRL)` | Reverter edição, se suportado |
| Refazer | `type("y", Key.CTRL)` | Comum no Windows; varia por editor |
| Selecionar até o fim da linha | `type(Key.END, Key.SHIFT)` | Seleção de texto por teclado |
| Selecionar até o início da linha | `type(Key.HOME, Key.SHIFT)` | Seleção no sentido inverso |

`paste("texto")` muda a área de transferência. Portanto, depois de copiar algo com Ctrl + C, use `type("v", Key.CTRL)` para colar aquele conteúdo; um `paste("outro texto")` o substituiria. Acentos podem exigir ajustes do ambiente: prefira `paste` e confira o valor preenchido.

<a id="teclas"></a>

## 5. Teclas especiais

| Tecla | Exemplo | Uso comum |
| --- | --- | --- |
| Enter | `type(Key.ENTER)` | Confirmar ou quebrar linha |
| Tab | `type(Key.TAB)` | Próximo controle |
| Escape | `type(Key.ESC)` | Fechar menu ou cancelar |
| Espaço | `type(Key.SPACE)` | Marcar opção com foco |
| Seta para cima | `type(Key.UP)` | Item anterior |
| Seta para baixo | `type(Key.DOWN)` | Próximo item |
| Seta esquerda | `type(Key.LEFT)` | Cursor ou opção anterior |
| Seta direita | `type(Key.RIGHT)` | Cursor ou próxima opção |
| Home / End | `type(Key.HOME)` / `type(Key.END)` | Início/fim |
| Page Up / Page Down | `type(Key.PAGE_UP)` / `type(Key.PAGE_DOWN)` | Navegação por página |
| Backspace / Delete | `type(Key.BACKSPACE)` / `type(Key.DELETE)` | Apagar |
| Teclas F1 a F12 | `type(Key.F1)` / `type(Key.F12)` | Funções definidas pelo aplicativo |
| Dígitos do teclado numérico | `type(Key.NUM0)` até `type(Key.NUM9)` | Exercitar entrada numérica |
| Operações numéricas | `type(Key.ADD)` / `type(Key.MINUS)` | Soma e subtração |
| Multiplicação e divisão | `type(Key.MULTIPLY)` / `type(Key.DIVIDE)` | Calculadora ou campo compatível |

F1 pode abrir ajuda e F12 pode abrir ferramentas do navegador, mas isso depende do aplicativo/SO. Teclas numéricas também dependem do estado do teclado. Para digitar o valor de uma nota, `paste("8.5")` costuma ser mais simples.

<a id="atalhos"></a>

## 6. Modificadores e combinações de teclas

| Possibilidade | Exemplo direto | Uso comum |
| --- | --- | --- |
| Ctrl com letra | `type("s", Key.CTRL)` | Salvar no aplicativo com foco |
| Alt com tecla | `type(Key.F4, Key.ALT)` | Fechar janela no Windows |
| Shift com Tab | `type(Key.TAB, Key.SHIFT)` | Voltar ao controle anterior |
| Ctrl + Shift com letra | `type("t", KeyModifier.CTRL + KeyModifier.SHIFT)` | Reabrir aba em muitos navegadores |
| Cmd com letra | `type("a", Key.CMD)` | Selecionar tudo no macOS |
| Manter Shift pressionado | `keyDown(Key.SHIFT)` | Começar uma seleção |
| Soltar Shift | `keyUp(Key.SHIFT)` | Terminar a seleção |
| Manter Ctrl pressionado | `keyDown(Key.CTRL)` | Combinação com várias ações |
| Soltar Ctrl | `keyUp(Key.CTRL)` | Encerrar a combinação |

`Key.CTRL`, `Key.SHIFT`, `Key.ALT` e `Key.CMD` representam essas teclas. Nos exemplos com múltiplos modificadores, `KeyModifier` fornece a combinação esperada pela API. Para começar, prefira `type(tecla, modificador)`, que já pressiona e solta; não deixe um `keyDown` sem seu `keyUp`.

<a id="navegador"></a>

## 7. Navegador: endereços, abas e visualização

Estas são combinações de teclado enviadas ao navegador, não métodos próprios de navegação do OculiX. Confira os atalhos na versão usada em aula e coloque a janela correta em foco.

| Possibilidade | Comando ou sequência | Uso |
| --- | --- | --- |
| Selecionar endereço | `type("l", Key.CTRL)` | Depois cole a URL e pressione Enter |
| Nova aba | `type("t", Key.CTRL)` | Abrir página de teste separada |
| Próxima aba | `type(Key.TAB, Key.CTRL)` | Alternar para a seguinte |
| Aba anterior | `type(Key.TAB, KeyModifier.CTRL + KeyModifier.SHIFT)` | Alternar no sentido inverso |
| Fechar aba atual | `type("w", Key.CTRL)` | Encerrar a aba de teste |
| Reabrir aba fechada | `type("t", KeyModifier.CTRL + KeyModifier.SHIFT)` | Recuperar a aba |
| Recarregar | `type("r", Key.CTRL)` | Atualizar a página |
| Voltar | `type(Key.LEFT, Key.ALT)` | Histórico anterior |
| Avançar | `type(Key.RIGHT, Key.ALT)` | Próxima entrada do histórico |
| Buscar na página | `type("f", Key.CTRL)` | Depois `paste("texto")` |
| Próxima ocorrência | `type(Key.ENTER)` | Com a busca da página aberta |
| Fechar busca | `type(Key.ESC)` | Voltar à página |
| Restaurar zoom | `type("0", Key.CTRL)` | Escala de página padrão |
| Tela cheia | `type(Key.F11)` | Alternar, quando suportado |
| Imprimir | `type("p", Key.CTRL)` | Abrir diálogo de impressão |
| Abrir arquivo local | `type("o", Key.CTRL)` | Escolher HTML/arquivo suportado |

Recarregar pode reenviar formulários; fechar uma aba pode descartar dados de teste. Voltar e Avançar dependem do histórico existente. Mudanças de zoom exigem novas capturas ou retorno à escala em que as imagens foram feitas.

<a id="formularios"></a>

## 8. Formulários e controles

| Controle ou ação | Exemplo direto | Preparação |
| --- | --- | --- |
| Campo de nome | `paste("campo_nome.png", "Ana Silva")` | Campo vazio |
| E-mail | `paste("campo_email.png", "ana@example.com")` | Campo correto em foco |
| Senha de teste | `paste("campo_senha.png", "senha_de_teste")` | Usar conta fictícia |
| Número decimal | `paste("campo_nota.png", "8.5")` | Conferir formato aceito |
| Campo obrigatório vazio | `click("botao_enviar.png")` | Deixe o campo vazio antes |
| Checkbox desmarcado | `click("checkbox_vazio.png")` | Capture especificamente o estado vazio |
| Desmarcar checkbox | `click("checkbox_marcado.png")` | Capture o estado marcado |
| Checkbox pelo teclado | `type(Key.SPACE)` | Checkbox precisa ter foco |
| Botão de opção (rádio) | `click("opcao_presencial.png")` | Capturar opção e rótulo únicos |
| Abrir lista | `click("lista_curso.png")` | Capturar o seletor |
| Escolher item visível | `click("opcao_informatica.png")` | Lista já aberta |
| Navegar em lista nativa | `type(Key.DOWN)` e `type(Key.ENTER)` | Seletor em foco; estado inicial conhecido |
| Data digitável | `paste("campo_data.png", "10/11/2026")` | Apenas se o controle aceitar colagem nesse formato |
| Abrir calendário | `click("icone_calendario.png")` | Campo com seletor visual |
| Limpar formulário | `click("botao_limpar.png")` | Verifique os campos vazios depois |

Checkbox alterna a cada clique: clicar duas vezes desfaz a primeira ação. Datas, listas e componentes personalizados variam; teste manualmente primeiro. Não existe um único comando visual que configure todo tipo de calendário, dropdown ou máscara de campo.

<a id="arquivos"></a>

## 9. Arquivos, upload, download e diálogos nativos

| Possibilidade | Exemplo direto | Uso |
| --- | --- | --- |
| Escolher arquivo | `click("botao_escolher_arquivo.png")` | Abrir diálogo nativo |
| Informar caminho Windows | `paste(r"C:\Testes\comprovante.pdf")` | Campo de nome/caminho do diálogo com foco |
| Informar caminho Linux | `paste("/home/aluno/Testes/comprovante.pdf")` | Ajustar ao arquivo real |
| Confirmar escolha | `type(Key.ENTER)` | Com o caminho preenchido |
| Enviar arquivo selecionado | `click("botao_enviar_arquivo.png")` | Acionar upload da aplicação |
| Abrir Salvar como | `type("s", KeyModifier.CTRL + KeyModifier.SHIFT)` | Se o aplicativo usar esse atalho |
| Informar nome de saída | `paste("relatorio_teste.pdf")` | Campo Nome do arquivo selecionado |
| Confirmar salvamento | `click("botao_salvar_arquivo.png")` | Diálogo com destino preparado |
| Cancelar diálogo | `type(Key.ESC)` | Se o diálogo aceitar cancelamento por Esc |
| Iniciar download | `click("botao_baixar.png")` | Página/aplicação aberta |

O arquivo de entrada deve existir e o destino deve ser uma pasta de teste. Se já existir um arquivo com o mesmo nome, pode surgir confirmação de substituição. O navegador pode baixar diretamente em Downloads sem abrir Salvar como; o teste precisa seguir a configuração usada. Veja [arquivos no capítulo 11](11-recursos-avancados-web-fullstack.md).

<a id="esperas"></a>

## 10. Pausas, presença e desaparecimento

| Possibilidade | Exemplo direto | Resultado |
| --- | --- | --- |
| Pausa de 1 segundo | `sleep(1)` | Espera sempre 1 s |
| Pausa fracionada | `sleep(0.5)` | Espera meio segundo |
| Pausa pela API de espera | `wait(2)` | Pausa fixa de 2 s |
| Esperar botão | `wait("botao.png", 5)` | Continua quando aparece; falha após o limite |
| Esperar mensagem | `wait("salvo.png", 10)` | Mesmo comportamento, outro alvo |
| Esperar sumir | `waitVanish("carregando.png", 10)` | Retorna True/False; confira o retorno |
| Exigir que desapareça | `assert waitVanish("carregando.png", 10)` | Reprova se continuar presente |
| Presença com prazo | `exists("aviso.png", 3)` | Retorna Match ou None |

**Regra de leitura:** `sleep(2)` espera tempo; `wait("imagem.png", 2)` espera imagem. `waitVanish` sozinho não reprova o roteiro quando retorna False. A ausência de um alvo em `exists` não gera FindFailed, mas a imagem de referência precisa estar disponível no bundle.

<a id="busca"></a>

## 11. Buscar e conferir o resultado

| Possibilidade | Exemplo direto | Uso |
| --- | --- | --- |
| Localizar uma imagem | `find("registro.png")` | Retorna a correspondência ou gera FindFailed |
| Localizar e clicar | `click(find("registro.png"))` | Ação no resultado localizado |
| Marcar posição visualmente | `find("registro.png").highlight(2)` | Depuração por 2 segundos |
| Conferir presença | `assert exists("sucesso.png", 5)` | Reprovar se a confirmação não aparecer |
| Conferir ausência | `assert not exists("erro.png", 2)` | Reprovar se o erro aparecer durante a consulta |
| Mensagem de falha própria | `assert exists("total_correto.png", 3), "Total incorreto"` | Explicar a asserção |
| Obter vários alvos | `list(findAll("icone_linha.png"))` | Lista de correspondências visíveis |
| Contar alvos | `print(len(list(findAll("icone_linha.png"))))` | Mostrar quantidade no console |

`findAll` pode gerar FindFailed se não encontrar nada. Contar resultados visuais não inclui outras páginas nem linhas fora da tela. `assert not exists` consulta por um período limitado; não é um monitor contínuo. Observação em segundo plano está no [capítulo 11](11-recursos-avancados-web-fullstack.md).

<a id="capturas"></a>

## 12. Capturas de tela e evidências

| Possibilidade | Exemplo direto | Resultado |
| --- | --- | --- |
| Captura principal em arquivo temporário | `print(capture(SCREEN))` | Mostra o caminho no console |
| Salvar no bundle | `capture(SCREEN, getBundlePath(), "resultado")` | Grava resultado.png |
| Capturar recorte conhecido | `capture(Region(100, 200, 600, 300), getBundlePath(), "formulario")` | Grava formulário nessa área |
| Capturar segundo monitor | `capture(Screen(1), getBundlePath(), "monitor_2")` | Exige segundo monitor disponível |
| Selecionar uma região manualmente | `Screen().selectRegion()` | Pausa para a pessoa escolher uma área |
| Mostrar pasta do script | `print(getBundlePath())` | Local onde estão código e imagens |

Use nomes de saída diferentes para preservar execuções anteriores. Uma captura não é uma validação: combine-a com `wait` ou `assert`. A captura interativa serve para preparação ou aula assistida; ela exige uma pessoa e não deve ficar no meio de uma execução autônoma.

<a id="aplicativos"></a>

## 13. Aplicativos e janelas

| Possibilidade | Exemplo direto | Uso |
| --- | --- | --- |
| Abrir Calculadora no Windows | `App.open("calc.exe")` | Exemplo local dependente do SO |
| Abrir executável por caminho | `App.open(r"C:\MeuPrograma\programa.exe")` | Ajustar ao aplicativo instalado |
| Focar por título/nome | `App.focus("Calculadora")` | Depende do nome reconhecido no ambiente |
| Alternar janela | `type(Key.TAB, Key.ALT)` | Alternância comum no Windows/Linux |
| Fechar janela | `type(Key.F4, Key.ALT)` | Janela ativa no Windows |
| Fechar pelo botão capturado | `click("fechar_janela.png")` | Controle do próprio aplicativo |

Para manter uma referência ao aplicativo aberto, são suficientes duas linhas:

```python
app = App.open("calc.exe")
app.focus()
```

Depois do exercício, `app.close()` tenta fechá-lo. O comportamento de `App` varia por plataforma e por aplicativos que criam processos auxiliares. Espere uma captura da janela antes de começar a digitar e feche somente o aplicativo preparado para o teste.

<a id="padroes"></a>

## 14. Ajustes de imagem, regiões e OCR

Esta parte complementa as ações básicas. Use quando precisar resolver uma ambiguidade concreta; há exemplos detalhados nos capítulos 05 e 07.

| Possibilidade | Exemplo direto | Uso |
| --- | --- | --- |
| Exigir maior semelhança | `click(Pattern("botao.png").similar(0.90))` | Reduzir correspondência ambígua |
| Correspondência quase exata | `find(Pattern("selo.png").exact())` | Limiar 0.99; não implica igualdade perfeita de pixels |
| Clicar ao lado do rótulo | `click(Pattern("rotulo_nome.png").targetOffset(120, 0))` | Campo à direita do rótulo |
| Clicar abaixo do rótulo | `click(Pattern("rotulo_nome.png").targetOffset(0, 40))` | Campo abaixo |
| Buscar apenas em um painel | `Region(100, 200, 600, 300).find("salvar.png")` | Evitar outro botão igual |
| Clicar apenas nesse painel | `Region(100, 200, 600, 300).click("salvar.png")` | Busca e ação restritas |
| Destacar uma área | `Region(100, 200, 600, 300).highlight(2)` | Conferir coordenadas |
| Ler texto de uma área | `print(Region(100, 200, 600, 100).text())` | OCR do conteúdo visível |
| Ler abaixo de uma âncora | `print(find("rotulo_total.png").below(60).text())` | OCR próximo de um rótulo |

Offset é medido a partir do centro da captura: x positivo vai para a direita, y positivo para baixo; valores negativos vão no sentido oposto. Coordenadas e medidas são exemplos. OCR exige contraste/idioma adequados e pode errar caracteres. Não abaixe a similaridade apenas para esconder uma falha.

<a id="mensagens"></a>

## 15. Console, avisos e controle da execução

| Possibilidade | Exemplo direto | Uso |
| --- | --- | --- |
| Escrever no console | `print("Etapa 1: preenchendo nome")` | Acompanhar o roteiro |
| Exibir aviso | `popup("Prepare o formulario e clique OK")` | Preparação assistida |
| Exibir mensagem de erro | `popError("Confira os dados do teste")` | Aviso visual para a pessoa |
| Solicitar texto | `nome = input("Nome do estudante:")` | Entrada manual em aula |
| Colar o texto recebido | `paste(nome)` | Campo já em foco; confira cancelamento antes |
| Encerrar normalmente | `exit(0)` | Parar o script com código zero |
| Encerrar com falha | `exit(1)` | Parar com código diferente de zero |

`input` retorna None quando a pessoa cancela; não envie esse valor a `paste`. `popup` e `popError` são mensagens do script, não capturas de mensagens da aplicação; mostrar `popError` não equivale, sozinho, a reprovar uma asserção. Em testes autônomos, use logs e validações, pois diálogos exigem intervenção.

<a id="sequencias"></a>

## 16. Sequências prontas para combinar as possibilidades

### Substituir um valor existente

```python
click("campo_nome.png")
type("a", Key.CTRL)
type(Key.BACKSPACE)
paste("Ana Silva")
```

### Preencher campos consecutivos e voltar um campo

```python
click("campo_nome.png")
paste("Ana Silva")
type(Key.TAB)
paste("ana@example.com")
type(Key.TAB, Key.SHIFT)
```

O último comando deve retornar ao campo Nome, se essa for a ordem real de foco.

### Marcar um checkbox conhecido e confirmar

```python
click("checkbox_aceite_vazio.png")
wait("checkbox_aceite_marcado.png", 3)
click("botao_continuar.png")
wait("titulo_proxima_etapa.png", 5)
```

### Escolher um item de lista visual

```python
click("lista_curso.png")
wait("opcao_informatica.png", 3)
click("opcao_informatica.png")
wait("curso_informatica_selecionado.png", 3)
```

### Copiar o conteúdo de um campo para outro

```python
click("campo_origem.png")
type("a", Key.CTRL)
type("c", Key.CTRL)
click("campo_destino.png")
type("a", Key.CTRL)
type("v", Key.CTRL)
```

### Acessar uma URL numa aba nova

```python
type("t", Key.CTRL)
paste("http://localhost:8080")
type(Key.ENTER)
wait("titulo_portal.png", 10)
```

### Escolher e enviar um arquivo no Windows

```python
click("botao_escolher_arquivo.png")
wait("dialogo_abrir.png", 5)
paste(r"C:\Testes\comprovante.pdf")
type(Key.ENTER)
click("botao_enviar_arquivo.png")
wait("arquivo_enviado.png", 10)
```

O diálogo deve abrir com foco no campo de caminho; se não abrir assim, capture e clique nesse campo antes de colar. O arquivo precisa existir e a captura de arquivo enviado deve identificar o resultado esperado.

### Salvar e guardar evidência

```python
click("botao_salvar.png")
wait("mensagem_salvo.png", 10)
assert not exists("mensagem_erro.png", 1)
capture(SCREEN, getBundlePath(), "cadastro_salvo")
```

Capture as duas mensagens de referência antes de executar, inclusive a de erro. O exemplo sobrescreve uma evidência anterior com o mesmo nome.

### Esperar uma operação terminar

```python
click("botao_processar.png")
wait("resultado_pronto.png", 10)
assert waitVanish("carregando.png", 3)
```

Esperar o resultado primeiro evita concluir sucesso só porque o indicador de carregamento ainda não havia aparecido.

## Referências e continuação

Este catálogo reúne as possibilidades de automação de interface utilizadas no guia; assinaturas adicionais, integrações e recursos específicos de versão estão na [API oficial](https://www.oculix.org/reference/api/). Consulte também [ações de Region](https://docs.oculix.org/region/), [teclas](https://docs.oculix.org/keys/), [Screen e capturas](https://docs.oculix.org/screen/), [interação e aplicativos](https://docs.oculix.org/interaction/) e [Pattern](https://docs.oculix.org/pattern/).

[← Receitas do capítulo 03](03-primeiro-script-e-captura-de-tela.md) · [Folha de consulta do capítulo 10](10-glossario-e-folha-de-consulta.md) · [Menu OculiX](README.md)
