[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md) · [🛡️ Menu ZAP](../capitulos-zap/README.md)

---

# 🪶 Capítulo 06: Dados CSV, variáveis e funções

![Trilha](https://img.shields.io/badge/JMeter-06_de_10-D55A37)

**Objetivo:** aplicar dados csv, variáveis e funções ao laboratório local, verificando resultados observáveis. Reserve 35–60 minutos.

## Ler uma massa de verdade

Use [massa_estudantes.csv](../exemplos/jmeter/massa_estudantes.csv), com 15 registros e cabeçalho `nome,nota1,nota2,status_esperado,media_esperada`.

1. Adicione Config Element → CSV Data Set Config ao grupo funcional.
2. Filename: caminho absoluto para o CSV ou `${__P(csv,massa_estudantes.csv)}` quando iniciar na pasta exemplos/jmeter.
3. File encoding `UTF-8`; Variable Names vazio (a primeira linha fornece os nomes); Delimiter `,`; Allow quoted data true.
4. Recycle on EOF false; Stop thread on EOF true; Sharing mode **All threads**. Cada iteração consome uma linha globalmente. Current thread dá uma leitura própria por usuário.
5. No POST, use o corpo abaixo; notas não levam aspas:

```json
{"nome":"${nome}","nota1":${nota1},"nota2":${nota2}}
```

6. JSON Assertion: `$.status` igual a `${status_esperado}` e `$.media` igual a `${media_esperada}`. O plano usa valores de média compatíveis com a serialização numérica JSON.

Para consumir as 15 linhas, configure uma thread e 15 loops. Não use esse grupo como gerador de carga prolongada: ao terminar o CSV, ele para. O grupo de carga pronto usa leitura sem CSV e controla duração separadamente.

## Variáveis e propriedades

User Defined Variables pode definir `HOST=localhost`, `PORTA=8080`, `AMBIENTE=local`. Variáveis usam `${HOST}` e vivem por thread; propriedades CLI usam `${__P(host,localhost)}` e são compartilhadas no processo.

| Recurso | Exemplo | Uso |
| --- | --- | --- |
| Counter | início 1, incremento 1, referência matricula | Sequência, escolha escopo por usuário/global |
| Random Variable | min 0, max 10, referência nota | Inteiro aleatório |
| Função aleatória | `${__Random(0,10)}` | Nota aleatória |
| UUID | `${__UUID()}` | Identificador único |
| Data | `${__time(yyyy-MM-dd)}` | Data de execução |
| Thread | `${__threadNum}` | Número do usuário |
| Propriedade | `${__P(porta,8080)}` | Parametrização CLI |

Abra Tools → Function Helper Dialog para montar funções. O atalho pode variar por plataforma; confirme o menu. CSV não escapa automaticamente valores para JSON: a massa fornecida não contém aspas nem quebras de linha; para dados arbitrários serialize com Groovy JsonOutput antes de enviar.

## Laboratório guiado

Execute 15 linhas e prove que as duas classes de resultado foram verificadas.

<details>
<summary>Gabarito comentado</summary>

Confira 15 amostras Criar avaliação com status esperado e média esperada. A massa contém notas-limite 0, 7 e 10, aprovações e reprovações; cada registro criado é removido no fim da iteração.

</details>

## Checklist

- [ ] Executei o procedimento com o servidor local.
- [ ] Conferi resposta, assertion e evidência.
- [ ] Consigo explicar o resultado e uma limitação do ensaio.

## Referências

Consulte a [referência oficial dos componentes](https://jmeter.apache.org/usermanual/component_reference.html) e o [manual de execução](https://jmeter.apache.org/usermanual/get-started.html).

---

[← Anterior](05-correlacao-autenticacao-jwt-e-sessoes.md) · [Menu](README.md) · [Próximo →](07-gravador-web-proxy-e-controladores-logicos.md)
