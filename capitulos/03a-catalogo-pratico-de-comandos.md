[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md)

---

# 📚 Catálogo prático de comandos e combinações do OculiX

Material de consulta do [capítulo 03](03-primeiro-script-e-captura-de-tela.md). Consulte a tabela geral por categoria, encontre a ação desejada e adapte as capturas à sua tela. Os exemplos são independentes: não execute uma tabela inteira como se fosse um único roteiro.

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

## Tabela geral de comandos

Leia cada linha como uma possibilidade independente. A coluna **Comando / exemplo** mostra o que digitar; **Quando usar** indica o contexto. As categorias seguem a ordem do índice acima.

| Categoria | Ação desejada | Comando / exemplo | Quando usar |
| --- | --- | --- | --- |
| <a id="cliques"></a>**1. Cliques** | Clique esquerdo em captura | `click("botao_salvar.png")` | Acionar um botão |
| Cliques | Duplo clique | `doubleClick("icone_pasta.png")` | Abrir item que exige dois cliques |
| Cliques | Clique direito | `rightClick("registro.png")` | Abrir menu de contexto |
| Cliques | Clique na posição atual | `click()` | Clicar onde o ponteiro já está |
| Cliques | Clique em coordenadas | `click(Location(400, 300))` | Ponto conhecido da tela |
| Cliques | Ctrl + clique | `click("item.png", KeyModifier.CTRL)` | Seleção múltipla, se o programa permitir |
| Cliques | Shift + clique | `click("ultimo_item.png", KeyModifier.SHIFT)` | Selecionar intervalo após selecionar o primeiro |
| Cliques | Clicar após esperar | `click(wait("botao_pronto.png", 5))` | Acionar assim que o alvo aparecer |
| <a id="movimento"></a>**2. Movimento do mouse e arraste** | Mover até uma captura | `hover("menu.png")` | Abrir submenu ou tooltip |
| Movimento do mouse e arraste | Mover até um ponto | `hover(Location(400, 300))` | Tirar o ponteiro de cima de um botão |
| Movimento do mouse e arraste | Arrastar entre capturas | `dragDrop("cartao.png", "destino.png")` | Quadro de tarefas |
| Movimento do mouse e arraste | Arrastar entre pontos | `dragDrop(Location(300, 400), Location(600, 400))` | Slider em posição conhecida |
| Movimento do mouse e arraste | Segurar botão esquerdo | `mouseDown(Button.LEFT)` | Início de gesto na posição atual |
| Movimento do mouse e arraste | Soltar botão esquerdo | `mouseUp(Button.LEFT)` | Encerrar o gesto |
| Movimento do mouse e arraste | Segurar botão direito | `mouseDown(Button.RIGHT)` | Gesto específico do aplicativo |
| Movimento do mouse e arraste | Soltar botão direito | `mouseUp(Button.RIGHT)` | Encerrar esse gesto |
| <a id="rolagem"></a>**3. Rolagem e deslocamento da página** | Rolar para baixo | `wheel(WHEEL_DOWN, 5)` | Avançar alguns passos |
| Rolagem e deslocamento da página | Rolar para cima | `wheel(WHEEL_UP, 5)` | Voltar alguns passos |
| Rolagem e deslocamento da página | Avançar uma página | `type(Key.PAGE_DOWN)` | Deslocar o painel com foco |
| Rolagem e deslocamento da página | Voltar uma página | `type(Key.PAGE_UP)` | Deslocamento inverso |
| Rolagem e deslocamento da página | Início da linha | `type(Key.HOME)` | Campo de texto |
| Rolagem e deslocamento da página | Fim da linha | `type(Key.END)` | Campo de texto |
| Rolagem e deslocamento da página | Início do conteúdo | `type(Key.HOME, Key.CTRL)` | Documento ou página com foco |
| Rolagem e deslocamento da página | Fim do conteúdo | `type(Key.END, Key.CTRL)` | Ir ao final, se suportado |
| <a id="texto"></a>**4. Preenchimento, seleção e edição de texto** | Colar texto | `paste("Ana Silva")` | Campo já selecionado |
| Preenchimento, seleção e edição de texto | Clicar e colar | `paste("campo_nome.png", "Ana Silva")` | Preencher em uma linha |
| Preenchimento, seleção e edição de texto | Digitar caracteres | `type("12345")` | Simular digitação |
| Preenchimento, seleção e edição de texto | Clicar e digitar | `type("campo_codigo.png", "12345")` | Preencher código |
| Preenchimento, seleção e edição de texto | Selecionar tudo | `type("a", Key.CTRL)` | Preparar substituição |
| Preenchimento, seleção e edição de texto | Apagar à esquerda | `type(Key.BACKSPACE)` | Remover seleção ou caractere anterior |
| Preenchimento, seleção e edição de texto | Apagar à direita | `type(Key.DELETE)` | Remover seleção ou próximo caractere |
| Preenchimento, seleção e edição de texto | Copiar seleção | `type("c", Key.CTRL)` | Copiar conteúdo do aplicativo |
| Preenchimento, seleção e edição de texto | Recortar seleção | `type("x", Key.CTRL)` | Mover conteúdo editável |
| Preenchimento, seleção e edição de texto | Colar área de transferência | `type("v", Key.CTRL)` | Colar o que foi copiado antes |
| Preenchimento, seleção e edição de texto | Desfazer | `type("z", Key.CTRL)` | Reverter edição, se suportado |
| Preenchimento, seleção e edição de texto | Refazer | `type("y", Key.CTRL)` | Comum no Windows; varia por editor |
| Preenchimento, seleção e edição de texto | Selecionar até o fim da linha | `type(Key.END, Key.SHIFT)` | Seleção de texto por teclado |
| Preenchimento, seleção e edição de texto | Selecionar até o início da linha | `type(Key.HOME, Key.SHIFT)` | Seleção no sentido inverso |
| <a id="teclas"></a>**5. Teclas especiais** | Enter | `type(Key.ENTER)` | Confirmar ou quebrar linha |
| Teclas especiais | Tab | `type(Key.TAB)` | Próximo controle |
| Teclas especiais | Escape | `type(Key.ESC)` | Fechar menu ou cancelar |
| Teclas especiais | Espaço | `type(Key.SPACE)` | Marcar opção com foco |
| Teclas especiais | Seta para cima | `type(Key.UP)` | Item anterior |
| Teclas especiais | Seta para baixo | `type(Key.DOWN)` | Próximo item |
| Teclas especiais | Seta esquerda | `type(Key.LEFT)` | Cursor ou opção anterior |
| Teclas especiais | Seta direita | `type(Key.RIGHT)` | Cursor ou próxima opção |
| Teclas especiais | Home / End | `type(Key.HOME)` / `type(Key.END)` | Início/fim |
| Teclas especiais | Page Up / Page Down | `type(Key.PAGE_UP)` / `type(Key.PAGE_DOWN)` | Navegação por página |
| Teclas especiais | Backspace / Delete | `type(Key.BACKSPACE)` / `type(Key.DELETE)` | Apagar |
| Teclas especiais | Teclas F1 a F12 | `type(Key.F1)` / `type(Key.F12)` | Funções definidas pelo aplicativo |
| Teclas especiais | Dígitos do teclado numérico | `type(Key.NUM0)` até `type(Key.NUM9)` | Exercitar entrada numérica |
| Teclas especiais | Operações numéricas | `type(Key.ADD)` / `type(Key.MINUS)` | Soma e subtração |
| Teclas especiais | Multiplicação e divisão | `type(Key.MULTIPLY)` / `type(Key.DIVIDE)` | Calculadora ou campo compatível |
| <a id="atalhos"></a>**6. Modificadores e combinações de teclas** | Ctrl com letra | `type("s", Key.CTRL)` | Salvar no aplicativo com foco |
| Modificadores e combinações de teclas | Alt com tecla | `type(Key.F4, Key.ALT)` | Fechar janela no Windows |
| Modificadores e combinações de teclas | Shift com Tab | `type(Key.TAB, Key.SHIFT)` | Voltar ao controle anterior |
| Modificadores e combinações de teclas | Ctrl + Shift com letra | `type("t", KeyModifier.CTRL + KeyModifier.SHIFT)` | Reabrir aba em muitos navegadores |
| Modificadores e combinações de teclas | Cmd com letra | `type("a", Key.CMD)` | Selecionar tudo no macOS |
| Modificadores e combinações de teclas | Manter Shift pressionado | `keyDown(Key.SHIFT)` | Começar uma seleção |
| Modificadores e combinações de teclas | Soltar Shift | `keyUp(Key.SHIFT)` | Terminar a seleção |
| Modificadores e combinações de teclas | Manter Ctrl pressionado | `keyDown(Key.CTRL)` | Combinação com várias ações |
| Modificadores e combinações de teclas | Soltar Ctrl | `keyUp(Key.CTRL)` | Encerrar a combinação |
| <a id="navegador"></a>**7. Navegador: endereços, abas e visualização** | Selecionar endereço | `type("l", Key.CTRL)` | Depois cole a URL e pressione Enter |
| Navegador: endereços, abas e visualização | Nova aba | `type("t", Key.CTRL)` | Abrir página de teste separada |
| Navegador: endereços, abas e visualização | Próxima aba | `type(Key.TAB, Key.CTRL)` | Alternar para a seguinte |
| Navegador: endereços, abas e visualização | Aba anterior | `type(Key.TAB, KeyModifier.CTRL + KeyModifier.SHIFT)` | Alternar no sentido inverso |
| Navegador: endereços, abas e visualização | Fechar aba atual | `type("w", Key.CTRL)` | Encerrar a aba de teste |
| Navegador: endereços, abas e visualização | Reabrir aba fechada | `type("t", KeyModifier.CTRL + KeyModifier.SHIFT)` | Recuperar a aba |
| Navegador: endereços, abas e visualização | Recarregar | `type("r", Key.CTRL)` | Atualizar a página |
| Navegador: endereços, abas e visualização | Voltar | `type(Key.LEFT, Key.ALT)` | Histórico anterior |
| Navegador: endereços, abas e visualização | Avançar | `type(Key.RIGHT, Key.ALT)` | Próxima entrada do histórico |
| Navegador: endereços, abas e visualização | Buscar na página | `type("f", Key.CTRL)` | Depois `paste("texto")` |
| Navegador: endereços, abas e visualização | Próxima ocorrência | `type(Key.ENTER)` | Com a busca da página aberta |
| Navegador: endereços, abas e visualização | Fechar busca | `type(Key.ESC)` | Voltar à página |
| Navegador: endereços, abas e visualização | Restaurar zoom | `type("0", Key.CTRL)` | Escala de página padrão |
| Navegador: endereços, abas e visualização | Tela cheia | `type(Key.F11)` | Alternar, quando suportado |
| Navegador: endereços, abas e visualização | Imprimir | `type("p", Key.CTRL)` | Abrir diálogo de impressão |
| Navegador: endereços, abas e visualização | Abrir arquivo local | `type("o", Key.CTRL)` | Escolher HTML/arquivo suportado |
| <a id="formularios"></a>**8. Formulários e controles** | Campo de nome | `paste("campo_nome.png", "Ana Silva")` | Campo vazio |
| Formulários e controles | E-mail | `paste("campo_email.png", "ana@example.com")` | Campo correto em foco |
| Formulários e controles | Senha de teste | `paste("campo_senha.png", "senha_de_teste")` | Usar conta fictícia |
| Formulários e controles | Número decimal | `paste("campo_nota.png", "8.5")` | Conferir formato aceito |
| Formulários e controles | Campo obrigatório vazio | `click("botao_enviar.png")` | Deixe o campo vazio antes |
| Formulários e controles | Checkbox desmarcado | `click("checkbox_vazio.png")` | Capture especificamente o estado vazio |
| Formulários e controles | Desmarcar checkbox | `click("checkbox_marcado.png")` | Capture o estado marcado |
| Formulários e controles | Checkbox pelo teclado | `type(Key.SPACE)` | Checkbox precisa ter foco |
| Formulários e controles | Botão de opção (rádio) | `click("opcao_presencial.png")` | Capturar opção e rótulo únicos |
| Formulários e controles | Abrir lista | `click("lista_curso.png")` | Capturar o seletor |
| Formulários e controles | Escolher item visível | `click("opcao_informatica.png")` | Lista já aberta |
| Formulários e controles | Navegar em lista nativa | `type(Key.DOWN)` e `type(Key.ENTER)` | Seletor em foco; estado inicial conhecido |
| Formulários e controles | Data digitável | `paste("campo_data.png", "10/11/2026")` | Apenas se o controle aceitar colagem nesse formato |
| Formulários e controles | Abrir calendário | `click("icone_calendario.png")` | Campo com seletor visual |
| Formulários e controles | Limpar formulário | `click("botao_limpar.png")` | Verifique os campos vazios depois |
| <a id="arquivos"></a>**9. Arquivos, upload, download e diálogos nativos** | Escolher arquivo | `click("botao_escolher_arquivo.png")` | Abrir diálogo nativo |
| Arquivos, upload, download e diálogos nativos | Informar caminho Windows | `paste(r"C:\Testes\comprovante.pdf")` | Campo de nome/caminho do diálogo com foco |
| Arquivos, upload, download e diálogos nativos | Informar caminho Linux | `paste("/home/aluno/Testes/comprovante.pdf")` | Ajustar ao arquivo real |
| Arquivos, upload, download e diálogos nativos | Confirmar escolha | `type(Key.ENTER)` | Com o caminho preenchido |
| Arquivos, upload, download e diálogos nativos | Enviar arquivo selecionado | `click("botao_enviar_arquivo.png")` | Acionar upload da aplicação |
| Arquivos, upload, download e diálogos nativos | Abrir Salvar como | `type("s", KeyModifier.CTRL + KeyModifier.SHIFT)` | Se o aplicativo usar esse atalho |
| Arquivos, upload, download e diálogos nativos | Informar nome de saída | `paste("relatorio_teste.pdf")` | Campo Nome do arquivo selecionado |
| Arquivos, upload, download e diálogos nativos | Confirmar salvamento | `click("botao_salvar_arquivo.png")` | Diálogo com destino preparado |
| Arquivos, upload, download e diálogos nativos | Cancelar diálogo | `type(Key.ESC)` | Se o diálogo aceitar cancelamento por Esc |
| Arquivos, upload, download e diálogos nativos | Iniciar download | `click("botao_baixar.png")` | Página/aplicação aberta |
| <a id="esperas"></a>**10. Pausas, presença e desaparecimento** | Pausa de 1 segundo | `sleep(1)` | Espera sempre 1 s |
| Pausas, presença e desaparecimento | Pausa fracionada | `sleep(0.5)` | Espera meio segundo |
| Pausas, presença e desaparecimento | Pausa pela API de espera | `wait(2)` | Pausa fixa de 2 s |
| Pausas, presença e desaparecimento | Esperar botão | `wait("botao.png", 5)` | Continua quando aparece; falha após o limite |
| Pausas, presença e desaparecimento | Esperar mensagem | `wait("salvo.png", 10)` | Mesmo comportamento, outro alvo |
| Pausas, presença e desaparecimento | Esperar sumir | `waitVanish("carregando.png", 10)` | Retorna True/False; confira o retorno |
| Pausas, presença e desaparecimento | Exigir que desapareça | `assert waitVanish("carregando.png", 10)` | Reprova se continuar presente |
| Pausas, presença e desaparecimento | Presença com prazo | `exists("aviso.png", 3)` | Retorna Match ou None |
| <a id="busca"></a>**11. Buscar e conferir o resultado** | Localizar uma imagem | `find("registro.png")` | Retorna a correspondência ou gera FindFailed |
| Buscar e conferir o resultado | Localizar e clicar | `click(find("registro.png"))` | Ação no resultado localizado |
| Buscar e conferir o resultado | Marcar posição visualmente | `find("registro.png").highlight(2)` | Depuração por 2 segundos |
| Buscar e conferir o resultado | Conferir presença | `assert exists("sucesso.png", 5)` | Reprovar se a confirmação não aparecer |
| Buscar e conferir o resultado | Conferir ausência | `assert not exists("erro.png", 2)` | Reprovar se o erro aparecer durante a consulta |
| Buscar e conferir o resultado | Mensagem de falha própria | `assert exists("total_correto.png", 3), "Total incorreto"` | Explicar a asserção |
| Buscar e conferir o resultado | Obter vários alvos | `list(findAll("icone_linha.png"))` | Lista de correspondências visíveis |
| Buscar e conferir o resultado | Contar alvos | `print(len(list(findAll("icone_linha.png"))))` | Mostrar quantidade no console |
| <a id="capturas"></a>**12. Capturas de tela e evidências** | Captura principal em arquivo temporário | `print(capture(SCREEN))` | Mostra o caminho no console |
| Capturas de tela e evidências | Salvar no bundle | `capture(SCREEN, getBundlePath(), "resultado")` | Grava resultado.png |
| Capturas de tela e evidências | Capturar recorte conhecido | `capture(Region(100, 200, 600, 300), getBundlePath(), "formulario")` | Grava formulário nessa área |
| Capturas de tela e evidências | Capturar segundo monitor | `capture(Screen(1), getBundlePath(), "monitor_2")` | Exige segundo monitor disponível |
| Capturas de tela e evidências | Selecionar uma região manualmente | `Screen().selectRegion()` | Pausa para a pessoa escolher uma área |
| Capturas de tela e evidências | Mostrar pasta do script | `print(getBundlePath())` | Local onde estão código e imagens |
| <a id="aplicativos"></a>**13. Aplicativos e janelas** | Abrir Calculadora no Windows | `App.open("calc.exe")` | Exemplo local dependente do SO |
| Aplicativos e janelas | Abrir executável por caminho | `App.open(r"C:\MeuPrograma\programa.exe")` | Ajustar ao aplicativo instalado |
| Aplicativos e janelas | Focar por título/nome | `App.focus("Calculadora")` | Depende do nome reconhecido no ambiente |
| Aplicativos e janelas | Alternar janela | `type(Key.TAB, Key.ALT)` | Alternância comum no Windows/Linux |
| Aplicativos e janelas | Fechar janela | `type(Key.F4, Key.ALT)` | Janela ativa no Windows |
| Aplicativos e janelas | Fechar pelo botão capturado | `click("fechar_janela.png")` | Controle do próprio aplicativo |
| <a id="padroes"></a>**14. Ajustes de imagem, regiões e OCR** | Exigir maior semelhança | `click(Pattern("botao.png").similar(0.90))` | Reduzir correspondência ambígua |
| Ajustes de imagem, regiões e OCR | Correspondência quase exata | `find(Pattern("selo.png").exact())` | Limiar 0.99; não implica igualdade perfeita de pixels |
| Ajustes de imagem, regiões e OCR | Clicar ao lado do rótulo | `click(Pattern("rotulo_nome.png").targetOffset(120, 0))` | Campo à direita do rótulo |
| Ajustes de imagem, regiões e OCR | Clicar abaixo do rótulo | `click(Pattern("rotulo_nome.png").targetOffset(0, 40))` | Campo abaixo |
| Ajustes de imagem, regiões e OCR | Buscar apenas em um painel | `Region(100, 200, 600, 300).find("salvar.png")` | Evitar outro botão igual |
| Ajustes de imagem, regiões e OCR | Clicar apenas nesse painel | `Region(100, 200, 600, 300).click("salvar.png")` | Busca e ação restritas |
| Ajustes de imagem, regiões e OCR | Destacar uma área | `Region(100, 200, 600, 300).highlight(2)` | Conferir coordenadas |
| Ajustes de imagem, regiões e OCR | Ler texto de uma área | `print(Region(100, 200, 600, 100).text())` | OCR do conteúdo visível |
| Ajustes de imagem, regiões e OCR | Ler abaixo de uma âncora | `print(find("rotulo_total.png").below(60).text())` | OCR próximo de um rótulo |
| <a id="mensagens"></a>**15. Console, avisos e controle da execução** | Escrever no console | `print("Etapa 1: preenchendo nome")` | Acompanhar o roteiro |
| Console, avisos e controle da execução | Exibir aviso | `popup("Prepare o formulario e clique OK")` | Preparação assistida |
| Console, avisos e controle da execução | Exibir mensagem de erro | `popError("Confira os dados do teste")` | Aviso visual para a pessoa |
| Console, avisos e controle da execução | Solicitar texto | `nome = input("Nome do estudante:")` | Entrada manual em aula |
| Console, avisos e controle da execução | Colar o texto recebido | `paste(nome)` | Campo já em foco; confira cancelamento antes |
| Console, avisos e controle da execução | Encerrar normalmente | `exit(0)` | Parar o script com código zero |
| Console, avisos e controle da execução | Encerrar com falha | `exit(1)` | Parar com código diferente de zero |

## Orientações por categoria

Consulte os detalhes quando precisar preparar o alvo ou entender uma limitação do comando.

<details>
<summary>1. Cliques — orientações de uso</summary>

Coordenadas são pixels da tela e precisam ser ajustadas ao computador. Para botões que mudam de posição, prefira capturas. Um Ctrl + clique depende do contexto: numa lista pode selecionar; num link pode abrir outra aba.

</details>

<details>
<summary>2. Movimento do mouse e arraste — orientações de uso</summary>

Prefira `dragDrop` para arrastar. `mouseDown` deve ser acompanhado de `mouseUp`; não execute a linha de pressionar isoladamente. Para gestos longos, o capítulo 08 explica como tratar interrupções. Um tooltip pode desaparecer quando o mouse sai do alvo: capture-o nesse estado antes de montar o teste.

</details>

<details>
<summary>3. Rolagem e deslocamento da página — orientações de uso</summary>

Antes de `wheel`, posicione o mouse no painel correto com `hover("painel.png")`. Antes de teclas de navegação, confira qual controle tem foco. Se houver um campo de texto selecionado, Ctrl + End pode mover o cursor dentro dele em vez de rolar a página.

</details>

<details>
<summary>4. Preenchimento, seleção e edição de texto — orientações de uso</summary>

`paste("texto")` muda a área de transferência. Portanto, depois de copiar algo com Ctrl + C, use `type("v", Key.CTRL)` para colar aquele conteúdo; um `paste("outro texto")` o substituiria. Acentos podem exigir ajustes do ambiente: prefira `paste` e confira o valor preenchido.

</details>

<details>
<summary>5. Teclas especiais — orientações de uso</summary>

F1 pode abrir ajuda e F12 pode abrir ferramentas do navegador, mas isso depende do aplicativo/SO. Teclas numéricas também dependem do estado do teclado. Para digitar o valor de uma nota, `paste("8.5")` costuma ser mais simples.

</details>

<details>
<summary>6. Modificadores e combinações de teclas — orientações de uso</summary>

`Key.CTRL`, `Key.SHIFT`, `Key.ALT` e `Key.CMD` representam essas teclas. Nos exemplos com múltiplos modificadores, `KeyModifier` fornece a combinação esperada pela API. Para começar, prefira `type(tecla, modificador)`, que já pressiona e solta; não deixe um `keyDown` sem seu `keyUp`.

</details>

<details>
<summary>7. Navegador: endereços, abas e visualização — orientações de uso</summary>

Estas são combinações de teclado enviadas ao navegador, não métodos próprios de navegação do OculiX. Confira os atalhos na versão usada em aula e coloque a janela correta em foco.


Recarregar pode reenviar formulários; fechar uma aba pode descartar dados de teste. Voltar e Avançar dependem do histórico existente. Mudanças de zoom exigem novas capturas ou retorno à escala em que as imagens foram feitas.

</details>

<details>
<summary>8. Formulários e controles — orientações de uso</summary>

Checkbox alterna a cada clique: clicar duas vezes desfaz a primeira ação. Datas, listas e componentes personalizados variam; teste manualmente primeiro. Não existe um único comando visual que configure todo tipo de calendário, dropdown ou máscara de campo.

</details>

<details>
<summary>9. Arquivos, upload, download e diálogos nativos — orientações de uso</summary>

O arquivo de entrada deve existir e o destino deve ser uma pasta de teste. Se já existir um arquivo com o mesmo nome, pode surgir confirmação de substituição. O navegador pode baixar diretamente em Downloads sem abrir Salvar como; o teste precisa seguir a configuração usada. Veja [arquivos no capítulo 11](11-recursos-avancados-web-fullstack.md).

</details>

<details>
<summary>10. Pausas, presença e desaparecimento — orientações de uso</summary>

**Regra de leitura:** `sleep(2)` espera tempo; `wait("imagem.png", 2)` espera imagem. `waitVanish` sozinho não reprova o roteiro quando retorna False. A ausência de um alvo em `exists` não gera FindFailed, mas a imagem de referência precisa estar disponível no bundle.

</details>

<details>
<summary>11. Buscar e conferir o resultado — orientações de uso</summary>

`findAll` pode gerar FindFailed se não encontrar nada. Contar resultados visuais não inclui outras páginas nem linhas fora da tela. `assert not exists` consulta por um período limitado; não é um monitor contínuo. Observação em segundo plano está no [capítulo 11](11-recursos-avancados-web-fullstack.md).

</details>

<details>
<summary>12. Capturas de tela e evidências — orientações de uso</summary>

Use nomes de saída diferentes para preservar execuções anteriores. Uma captura não é uma validação: combine-a com `wait` ou `assert`. A captura interativa serve para preparação ou aula assistida; ela exige uma pessoa e não deve ficar no meio de uma execução autônoma.

</details>

<details>
<summary>13. Aplicativos e janelas — orientações de uso</summary>

Para manter uma referência ao aplicativo aberto, são suficientes duas linhas:

```python
app = App.open("calc.exe")
app.focus()
```

Depois do exercício, `app.close()` tenta fechá-lo. O comportamento de `App` varia por plataforma e por aplicativos que criam processos auxiliares. Espere uma captura da janela antes de começar a digitar e feche somente o aplicativo preparado para o teste.

</details>

<details>
<summary>14. Ajustes de imagem, regiões e OCR — orientações de uso</summary>

Esta parte complementa as ações básicas. Use quando precisar resolver uma ambiguidade concreta; há exemplos detalhados nos capítulos 05 e 07.


Offset é medido a partir do centro da captura: x positivo vai para a direita, y positivo para baixo; valores negativos vão no sentido oposto. Coordenadas e medidas são exemplos. OCR exige contraste/idioma adequados e pode errar caracteres. Não abaixe a similaridade apenas para esconder uma falha.

</details>

<details>
<summary>15. Console, avisos e controle da execução — orientações de uso</summary>

`input` retorna None quando a pessoa cancela; não envie esse valor a `paste`. `popup` e `popError` são mensagens do script, não capturas de mensagens da aplicação; mostrar `popError` não equivale, sozinho, a reprovar uma asserção. Em testes autônomos, use logs e validações, pois diálogos exigem intervenção.

</details>

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
