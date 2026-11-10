[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md)

---

<div align="center">

[⬅️ Anterior: Projeto Prático Completo](09-projeto-pratico-completo.md) · [🏠 Início](../README.md) · **Capítulo 10 de 12**

# 📋 Capítulo 10: Folha de Consulta Rápida (Cheat Sheet) e Glossário Ilustrado

![Progresso](https://img.shields.io/badge/Progresso-Cap._10_%2F_12_(83%25)-4ADE80?style=flat-square)
![Tipo](https://img.shields.io/badge/Material-Consulta_Rápida_em_Aula-00D2FF?style=flat-square)

</div>

---

## ⚡ 1. Folha de Consulta de Comandos (OculiX Cheat Sheet)

Mantenha esta página aberta durante as aulas e provas práticas para consultar rapidamente a sintaxe de qualquer comando no **OculiX IDE**:

Para uma lista mais ampla de ações e combinações, consulte o [tabela única de comandos e exemplos do capítulo 03](03-primeiro-script-e-captura-de-tela.md#5-tabela-única-de-comandos-e-exemplos), com exemplos diretos e sequências para adaptar.

### 🖱️ Ações de Mouse

| Comando | O que faz? | Exemplo Prático |
| :--- | :--- | :--- |
| **`click(alvo)`** | Clica com o botão esquerdo no centro da imagem. | `click("btn_salvar.png")` |
| **`doubleClick(alvo)`** | Dá um duplo clique rápido na imagem. | `doubleClick("icone_pasta.png")` |
| **`rightClick(alvo)`** | Clica com o botão direito do mouse (menu de contexto). | `rightClick("item_lista.png")` |
| **`hover(alvo)`** | Apenas move o cursor do mouse para cima da imagem. | `hover("menu_opcoes.png")` |
| **`dragDrop(orig, dest)`** | Clica e segura na 1ª imagem, arrasta e solta na 2ª. | `dragDrop("card.png", "coluna_fim.png")` |
| **`wheel(WHEEL_DOWN, n)`** | Gira a rodinha do mouse `n` etapas para baixo (`WHEEL_UP` para cima). | `wheel(WHEEL_DOWN, 5)` |

---

### ⌨️ Ações de Teclado

| Comando | O que faz? | Exemplo Prático |
| :--- | :--- | :--- |
| **`paste("texto")`** | Cola o texto no campo em foco (**ideal para acentos: `ã`, `ç`, `é`**). | `paste("Avaliação de João")` |
| **`paste(img, "texto")`** | Clica na imagem e já cola o texto dentro dela. | `paste("inp_nome.png", "Maria")` |
| **`type("texto")`** | Digita tecla por tecla (ou aperta teclas especiais `Key`). | `type(Key.ENTER)` / `type(Key.TAB)` |
| **`type(tecla, mod)`** | Pressiona uma combinação de teclas (<kbd>Ctrl</kbd>, <kbd>Alt</kbd>, <kbd>Shift</kbd>). | `type("a", KeyModifier.CTRL)` |

---

### ⏳ Esperas, Sincronização e Verificação (Oráculo)

| Comando | O que faz? | Exemplo Prático |
| :--- | :--- | :--- |
| **`wait(img, seg)`** | Espera até `seg` segundos para a imagem aparecer (dá erro se não aparecer). | `wait("btn_ok.png", 10).click()` |
| **`waitVanish(img, seg)`** | Espera até `seg` segundos para a imagem **sumir** da tela. | `waitVanish("carregando.png", 15)` |
| **`exists(img, seg)`** | Verifica se a imagem aparece em até `seg` segundos (**não dá erro** se falhar; retorna `None`). | `if exists("aviso.png", 3):` |
| **`assert exists(...)`** | Aprova (`PASS`) se a imagem existir, ou reprova (`FAIL`) o Caso de Teste se não existir. | `assert exists("sucesso.png", 5)` |
| **`sleep(seg)`** | Pausa fixa obrigatória em segundos. | `sleep(1.5)` |

---

### 🎯 Ajuste Fino de Padrões (`Pattern`)

| Comando | O que faz? | Exemplo Prático |
| :--- | :--- | :--- |
| **`Pattern(img).similar(n)`** | Exige similaridade mínima `n` (de `0.01` a `0.99`; padrão `0.70`). | `Pattern("selo.png").similar(0.88)` |
| **`Pattern(img).targetOffset(x, y)`** | Desloca o clique `x` pixels na horizontal e `y` na vertical a partir do centro. | `Pattern("rotulo.png").targetOffset(90, 0)` |
| **`Pattern(img).exact()`** | Atalho para exigir `0.99` de similaridade. | `Pattern("numero_10.png").exact()` |

---

### 📐 Regiões de Busca (ROI) e Leitura de Texto (OCR)

| Comando | O que faz? | Exemplo Prático |
| :--- | :--- | :--- |
| **`find(img).right(px)`** | Cria uma região `px` pixels à **direita** da imagem âncora. | `wait("lbl_total.png", 5).right(120)` |
| **`find(img).below(px)`** | Cria uma região `px` pixels **abaixo** da imagem âncora. | `wait("lbl_media.png", 5).below(55)` |
| **`find(img).left(px)` / `.above(px)`** | Cria uma região à **esquerda** ou **acima** da âncora. | `find("icone.png").left(100)` |
| **`regiao.highlight(seg)`** | Desenha uma borda vermelha na tela por `seg` segundos mostrando a região. | `regiao.highlight(2)` |
| **`regiao.text()`** | Usa o **OCR Tesseract** embutido para ler o texto escrito dentro da região! | `valor = regiao.text().strip()` |

---

### 🚀 Controle de Aplicativos (`App`) e Evidências

| Comando | O que faz? | Exemplo Prático |
| :--- | :--- | :--- |
| **`App.open("caminho")`** | Inicia um programa local no sistema operacional. | `app = App.open("calc.exe")` |
| **`app.focus()`** | Traz a janela do aplicativo para a frente da tela. | `app.focus()` |
| **`app.close()`** | Fecha o aplicativo aberto. | `app.close()` |
| **`getBundlePath()`** | Retorna o caminho da pasta `.sikuli` atual onde o script está salvo. | `print(getBundlePath())` |

---

## ⌨️ 2. Tabela Completa de Atalhos do OculiX IDE

| Ação | Windows |
| :--- | :---: |
| **🛑 PARADA DE EMERGÊNCIA (Abortar Script)** | <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd> |
| **▶️ Executar Script Atual** | <kbd>Ctrl</kbd> + <kbd>R</kbd> |
| **🐢 Executar em Câmera Lenta (Slow Motion)** | <kbd>Alt</kbd> + <kbd>Ctrl</kbd> + <kbd>R</kbd> |
| **✂️ Executar Apenas Linhas Selecionadas** | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> |
| **📷 Captura Rápida de Imagem** | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>2</kbd> |
| **📄 Novo Script** | <kbd>Ctrl</kbd> + <kbd>N</kbd> |
| **📂 Abrir Script** | <kbd>Ctrl</kbd> + <kbd>O</kbd> |
| **💾 Salvar Script** | <kbd>Ctrl</kbd> + <kbd>S</kbd> |
| **📦 Exportar Pacote Compactado (`.zip`)** | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd> |
| **⚙️ Abrir Preferências** | <kbd>Ctrl</kbd> + <kbd>P</kbd> |
| **🔄 Alternar entre Abas Abertas** | <kbd>Ctrl</kbd> + <kbd>Tab</kbd> |

---

## 📖 3. Glossário Ilustrado de Testes de Software e OculiX

<details open>
<summary><b>🔤 Termos de A a Z (Clique para recolher/expandir)</b></summary>
<br/>

- **Âncora Visual (*Visual Anchor*):** Elemento fixo e imutável na tela (como o rótulo `"Nome do Aluno:"`) usado como ponto de referência para localizar campos em branco ou textos variáveis ao seu redor.
- **Asserção (*Assertion*):** Verificação automática no código (`assert`) que avalia se uma condição esperada do teste é verdadeira. Se for falsa, o teste é marcado como reprovado (*Failed*).
- **Bundle `.sikuli`:** Pasta especial gerada pelo OculiX IDE que agrupa o código-fonte do script (`.py`) e todas as capturas de imagem (`.png`) em um mesmo diretório.
- **Caso de Teste (*Test Case*):** Conjunto documentado de entradas, ações de execução e resultados esperados criado para validar um requisito específico de um software.
- **Desvio do Alvo (*Target Offset*):** Deslocamento em pixels `(X, Y)` configurado na janela *Configurações de Padrão* para que o clique aconteça fora do centro geométrico da imagem capturada.
- **`FindFailed`:** Exceção lançada pelo OculiX quando o motor OpenCV não encontra na tela nenhuma região com similaridade igual ou superior ao limite configurado dentro do tempo de espera (*timeout*).
- **OCR (*Optical Character Recognition*):** Tecnologia de Reconhecimento Óptico de Caracteres (como o **Tesseract** embutido no OculiX) capaz de converter pixels de letras e números da tela em texto pesquisável (`regiao.text()`).
- **Oráculo de Teste (*Test Oracle*):** Mecanismo ou critério usado para determinar se o software passou ou falhou em um teste (comparando o resultado esperado com o resultado obtido).
- **ROI (*Region of Interest* / Região de Interesse):** Subárea retangular da tela onde o OculiX restringe sua busca visual, aumentando a velocidade e evitando cliques em elementos repetidos fora daquela área.
- **Similaridade (*Similarity Score*):** Valor decimal entre `0.00` (0%) e `1.00` (100%) que mede o grau de coincidência visual entre a imagem recortada e os pixels exibidos na tela.
- **Template Matching (OpenCV):** Algoritmo de visão computacional usado pelo OculiX que desliza a imagem recortada sobre a captura da tela inteira para encontrar a coordenada de maior semelhança.
- **Teste de Caixa-Preta (*Black-Box Testing*):** Técnica de teste em que o avaliador verifica as entradas e saídas visíveis do sistema sem precisar ler ou alterar o código-fonte interno da aplicação.
</details>

---

## 🧩 4. Template Base Pronto para Copiar e Usar nas Aulas

Sempre que for começar um novo exercício prático ou prova no OculiX IDE, você pode copiar esta estrutura base limpa e organizada:

```python
# ==============================================================================
# Script de Teste: [Nome do Teste]
# Autor(a): [Seu Nome]
# Objetivo: [Descrever o que este Caso de Teste valida]
# ==============================================================================
from sikuli import *
import os
import shutil

# Tempo máximo padrão de espera por imagens (em segundos)
Settings.AutoWaitTimeout = 5.0

def registrar_evidencia(nome_png):
    """Captura a tela atual e salva na pasta .sikuli do projeto."""
    captura = Screen().capture(Screen().getBounds()).getFile()
    shutil.copy(captura, os.path.join(getBundlePath(), nome_png))
    print("📸 Evidência gerada:", nome_png)

try:
    print("▶️ Passo 1: Preparando dados de entrada...")
    # Coloque seus comandos click() / paste() aqui:
    
    print("▶️ Passo 2: Executando ação principal...")
    # Exemplo: wait("btn_confirmar.png", 5).click()
    
    print("▶️ Passo 3: Validando o Resultado Esperado (Oráculo)...")
    # Exemplo:
    # resultado = exists("msg_sucesso.png", 5)
    # assert resultado is not None, "A mensagem esperada não apareceu!"
    # resultado.highlight(2)
    
    registrar_evidencia("evidencia_sucesso.png")
    print("✅ TESTE CONCLUÍDO COM SUCESSO!")

except FindFailed as erro:
    registrar_evidencia("evidencia_erro_findfailed.png")
    print("❌ ERRO VISUAL (FindFailed):", erro)
    raise
```

---

<div align="center">

### 🎉 Você concluiu os fundamentos do OculiX IDE!

| [⬅️ Capítulo 09: Projeto Prático Completo](09-projeto-pratico-completo.md) | [🏠 Voltar ao Início do Guia (README)](../README.md) |
| :--- | ---: |

</div>


**Continue a trilha:** [Capítulo 11: Recursos avançados Web Full Stack](11-recursos-avancados-web-fullstack.md) → [Capítulo 12: UI + API](12-testes-hibridos-ui-api.md).
