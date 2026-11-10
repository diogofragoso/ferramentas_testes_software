[🏠 Hub Full Stack](../README.md) · [🦎 Menu OculiX](../capitulos/README.md) · [🪶 Menu JMeter](../capitulos-jmeter/README.md)

---

# 🪶 Capítulo 09: CLI, listeners e dashboard HTML

![Trilha](https://img.shields.io/badge/JMeter-09_de_10-D55A37)

**Objetivo:** aplicar cli, listeners e dashboard html ao laboratório local, verificando resultados observáveis. Reserve 35–60 minutos.

## Executar sem a interface gráfica

Abra um terminal na raiz do repositório com o servidor ativo. Primeiro faça o teste funcional, depois carga. Use uma pasta de dashboard inexistente ou vazia em cada execução.

```powershell
cd exemplos/jmeter
jmeter -n -t plano_api_e_carga_fullstack.jmx -l resultados_funcional.jtl -e -o relatorio_dashboard_funcional
jmeter -n -t plano_api_e_carga_fullstack.jmx -Jfuncional=false -Jcarga=true -Jusuarios=10 -Jrampup=10 -Jduracao=60 -l resultados_carga.jtl -e -o relatorio_dashboard_carga
```

No PowerShell, use `jmeter.bat` se o diretório bin estiver no PATH. Para um caminho completo entre aspas, use o operador `&`, por exemplo: `& "C:\Ferramentas\apache-jmeter\bin\jmeter.bat" -n -t plano_api_e_carga_fullstack.jmx -l resultados.jtl`. `-Jhost=localhost` e `-Jporta=8080` alteram o destino. `-Jcsv=C:/caminho/massa_estudantes.csv` remove dependência da pasta atual. Não reutilize JTL antigo: JMeter pode acrescentar amostras e misturar execuções.

## Escolher o listener

View Results Tree é útil com 1 usuário e poucos loops, mas consome memória armazenando corpos; não faz parte do plano pronto de carga. Summary Report mostra amostras, média, min/max, desvio, erros e throughput. Aggregate Report acrescenta mediana e percentis. Os nomes e colunas dependem do listener, portanto não procure P95 no Summary Report.

| Medida | Como interpretar |
| --- | --- |
| Samples | Quantas amostras foram registradas por rótulo |
| Average / Median | Média e P50 em ms |
| 90% / 95% / 99% | Cauda da distribuição |
| Error % | HTTP inesperado ou falha em assertion |
| Throughput | Amostras por segundo/minuto, confira unidade |
| Received KB/sec | Volume de resposta, não velocidade do banco |

## Ler o dashboard

Abra `relatorio_dashboard_carga/index.html`. APDEX depende dos limiares de satisfação e tolerância configurados; registre-os no relatório. Response Times Over Time revela mudanças; Active Threads Over Time mostra se houve o perfil planejado; Transactions per Second indica vazão. Latency não equivale ao tempo total da resposta.

Procure uma combinação de crescimento de P95, throughput que deixa de aumentar e taxa de erro crescente. Correlacione com CPU/memória, logs da aplicação e recursos do gerador antes de atribuir um gargalo. Use rótulos separados para login, consulta e CRUD: agregá-los esconde diferenças. Não chame um pico isolado de ponto de quebra.

O plano permite apenas funcional (padrão), apenas carga ou ambos. Para medir carga isolada, desligue funcional como no comando acima. O servidor e o gerador na mesma máquina disputam recursos; os números servem ao exercício, não ao dimensionamento de produção.

## Laboratório guiado

Compare 5 e 10 usuários com as mesmas pausas e duração. Que evidência sustenta uma conclusão?

<details>
<summary>Gabarito comentado</summary>

Guarde dois JTLs e dashboards distintos, parâmetros e configuração da máquina. Compare throughput, P95 e erro da mesma operação. Se não houver degradação, relate esse resultado sem inventar um gargalo.

</details>

## Checklist

- [ ] Executei o procedimento com o servidor local.
- [ ] Conferi resposta, assertion e evidência.
- [ ] Consigo explicar o resultado e uma limitação do ensaio.

## Referências

Consulte a [referência oficial dos componentes](https://jmeter.apache.org/usermanual/component_reference.html) e o [manual de execução](https://jmeter.apache.org/usermanual/get-started.html).

---

[← Anterior](08-timers-banco-de-dados-jdbc-e-upload.md) · [Menu](README.md) · [Próximo →](10-projeto-pratico-fullstack-e-cheat-sheet.md)
