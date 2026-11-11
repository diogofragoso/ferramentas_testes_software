[🏠 Hub](../README.md) · [🛡️ Menu ZAP](README.md)

# Capítulo 01: Introdução, instalação e laboratório

**Objetivo:** abrir o ZAP 2.17.0 e preparar um alvo HTTP local. Reserve 30 minutos.

## 1. Entender a ferramenta

ZAP é um proxy para testes de segurança Web: permite examinar as mensagens entre navegador e servidor. Na análise passiva, observa o tráfego; na ativa, envia entradas de teste ao alvo. A trilha começa pela observação e avança para testes controlados.

## 2. Instalar no Windows

1. No PowerShell, execute `java -version`. O ZAP 2.17 requer **Java 17 ou superior**; se necessário, instale um JDK compatível, como o [Eclipse Temurin](https://adoptium.net/), e reabra o terminal.
2. Acesse o [download oficial](https://www.zaproxy.org/download/). Para acompanhar exatamente esta trilha, use o instalador Windows da [release v2.17.0](https://github.com/zaproxy/zaproxy/releases/tag/v2.17.0), caso o download principal já ofereça outra versão.
3. Execute o instalador e conclua o assistente. Abra o ZAP pelo menu Iniciar.
4. Leia os termos e prossiga se concordar. Na pergunta sobre persistir a sessão, escolha a opção de persistir com nome e selecione uma pasta de aula, por exemplo `Documentos/aula-zap/sessao-inicial`.
5. Confira a versão em **Help → About** (Ajuda → Sobre). Registre também a versão do Java.
6. Na barra superior, selecione **Safe Mode**. Os nomes desta trilha estão em inglês; a tradução e os complementos podem mudar os rótulos.

Requisitos e instalação: [Getting Started oficial](https://www.zaproxy.org/getting-started/).

## 3. Iniciar o laboratório

1. Abra outro PowerShell na raiz do repositório.
2. Execute:

```powershell
python exemplos/app-alvo-teste/servidor_fullstack.py --port 8081
```

3. Se seu Windows usa o launcher, substitua `python` por `py -3`.
4. Mantenha o terminal aberto. Visite `http://localhost:8081/api/health`: espere HTTP 200 e JSON com `status: "ok"`.
5. Abra `http://localhost:8081/` e entre com `estudante_qa` / `oculix123`.

O servidor usa Python 3.10+ sem pacotes adicionais, aceita conexões somente em loopback e mantém dados em memória. Reiniciar apaga registros e invalida tokens. Consulte o [contrato HTTP](../exemplos/README.md).

## 4. Resolver os primeiros problemas

| Sintoma | Ação |
| --- | --- |
| Java não encontrado | Instale Java 17+, reabra o terminal e repita `java -version` |
| Porta em uso | Encerre a instância anterior do laboratório com Ctrl+C; confirme que o app está na 8081 e o proxy na 8080 |
| Navegador não conecta | Confira se o processo Python continua aberto e se a URL usa HTTP e porta 8081 |
| HTML funciona, mas não aparece tráfego | Use a URL HTTP; `file://` não executa o laboratório de API |

## Exercício e evidência

Registre as versões e capture a resposta de `/api/health`. Explique a função de cada porta.

<details>
<summary>Conferir resposta</summary>

8081 recebe as requisições da aplicação; 8080 recebe as conexões do navegador ao proxy ZAP. São processos distintos e precisam de portas distintas.

</details>

- [ ] ZAP 2.17.0 aberto em Safe Mode.
- [ ] Laboratório respondendo na porta 8081.
- [ ] Versões e evidência registradas.

[← Menu](README.md) · [Próximo: interface e escopo →](02-interface-proxy-e-escopo.md)
