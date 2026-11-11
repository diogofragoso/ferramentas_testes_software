[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md) · [🛡️ Menu ZAP](../capitulos-zap/README.md)

---

# 🪶 Capítulo 01: Introdução, instalação e métricas

![Trilha](https://img.shields.io/badge/JMeter-01_de_10-D55A37)

**Objetivo:** aplicar introdução, instalação e métricas ao laboratório local, verificando resultados observáveis. Reserve 35–60 minutos.

## O que vamos testar

O navegador apresenta a interface; a API aplica regras e autenticação; o banco persiste dados. JMeter envia protocolos HTTP/JDBC e não executa JavaScript nem renderiza pixels. Use OculiX para verificar a experiência visual.

| Ensaio | Pergunta | Exemplo local |
| --- | --- | --- |
| Funcional | A regra está correta? | Média 9 retorna APROVADO |
| Carga | O sistema atende ao volume previsto? | 10 usuários por 60 s |
| Estresse | Em que volume o serviço degrada? | Aumentar patamares e observar erros |
| Pico (spike) | Como reage a uma chegada súbita? | 10 threads em uma barreira |
| Resistência (soak) | Há degradação com o tempo? | Carga moderada por horas |

## Instalação guiada

1. Instale um JDK 17 ou 21 e confirme `java -version` no terminal.
2. Obtenha o **binário**, não o pacote de fontes, na [página Apache](https://jmeter.apache.org/download_jmeter.cgi). Os exemplos usam o formato JMeter 5.6.3; confira os requisitos da versão baixada.
3. Extraia o ZIP em uma pasta com permissão de escrita.
4. No Windows, abra `bin/jmeter.bat` pelo Explorador de Arquivos ou pelo PowerShell.
5. GUI serve para construir e depurar. Execute carga pelo terminal com `jmeter -n`.
6. Em outro terminal, na raiz deste repositório: `python exemplos/app-alvo-teste/servidor_fullstack.py`. No Windows, `py -3` pode substituir `python`.
7. Abra `http://localhost:8080` e `http://localhost:8080/api/health`.

## Métricas sem confusão

Elapsed é o tempo total da amostra; latency mede até o início da resposta. Média pode esconder lentidão de uma minoria; mediana é P50, P95 indica que aproximadamente 95% das amostras ficaram até aquele valor. Throughput é trabalho por unidade de tempo: confira se o relatório usa segundo ou minuto. Threads são usuários virtuais, não RPS.

Em regime estável, concorrência aproximada = RPS × (tempo de resposta + pausas), em segundos. Registre também CPU, memória e taxa de erro: desempenho sem correção não basta.

## Laboratório guiado

Inicie o laboratório e explique por que 20 threads não garantem 20 RPS.

<details>
<summary>Gabarito comentado</summary>

GET /api/health retorna 200 e status ok. Cada thread espera a resposta e seus timers; portanto a vazão depende da duração da jornada.

</details>

## Checklist

- [ ] Executei o procedimento com o servidor local.
- [ ] Conferi resposta, assertion e evidência.
- [ ] Consigo explicar o resultado e uma limitação do ensaio.

## Referências

Consulte a [referência oficial dos componentes](https://jmeter.apache.org/usermanual/component_reference.html) e o [manual de execução](https://jmeter.apache.org/usermanual/get-started.html).

---

[← Menu](README.md) · [Menu](README.md) · [Próximo →](02-conhecendo-a-interface-jmeter.md)
