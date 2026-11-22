# Representação sobre a escravatura (José Bonifácio): estado (2026-11-22)

Não-ficção; autor novo `jose-bonifacio`. **Completa.** Fora: notas gerais (fila dos lotes).

## Fonte
- Base: Paris, Firmin Didot, 1825. Fac-símile do Internet Archive `representaoassem00boni` (página impressa = pdf − 12).
  Segunda leitura: `DELTA53975FA`. Ponto de partida: páginas do Wikisource (`1825/NNN.txt`; NNN = página do PDF do
  Wikisource = pdf do IA − 2), cada uma conferida nas imagens; as 31 correções estão em `conferencia.tsv`.

## Refazer (na raiz do repositório)
`python3 edicoes/representacao-escravatura/montar.py --publicar`: junta as páginas, aplica a conferência e a grafia de
hoje (`decisoes.py`) e grava `conteudo/jose-bonifacio/representacao-sobre-a-escravatura.js`.

## Decisões
- Quatro partes (Advertência, Representação, Artigos, Conclusão); «Conclusão» é título nosso.
- As formas em -ão do passado viram -am, caso a caso (`continuarão` fica no futuro em «somente continuarão a ser surdos»).
- «pela mor parte» fica. «capitaes» = capitais (dinheiro). Citações de Pradt em francês, como no impresso.
- 2 decisões nas pendências (`revisao.json`): «me emprego» e «premissas».
