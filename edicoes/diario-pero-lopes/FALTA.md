# Diário da navegação (Pero Lopes de Sousa): estado

Branch `pedido-diario-pero-lopes`. Não-ficção; autor novo `pero-lopes-de-sousa`. **Pronta para juntar e publicar** (12/11).

## Fonte
- Base: Varnhagen, *Diário da navegação da armada que foi à terra do Brasil em 1530…* (Lisboa, 1839), pp. 3–59, 1.ª ed.
  Fac-símile do Internet Archive `diario_navegacao_souza` (pdf pp. 29–85; página impressa = pdf − 26). Outras leituras:
  Google `bub_gb_-F8CAAAAYAAJ` (mesma ed.), 4.ª ed. de 1867 (`diariodenavegao00varngoog`). Eugênio de Castro (1927) não usado.
- `1839/NN.txt`: transcrição linha a linha de cada página impressa, conferida nas imagens (subagente Sonnet; dúvidas
  em `1839/DUVIDAS.md`; ~530 correções ao OCR em `CONFERENCIA.tsv`). Grafia 1839 já regularizada por Varnhagen.

## Como foi feito (refazer: na raiz do repo)
`python3 edicoes/diario-pero-lopes/montar.py --publicar`: junta as páginas, divide por dia (203 entradas), grafia de hoje
(`decisoes.py`: PRE/MANUAL/POS + léxico da São Bernardo), grava `conteudo/pero-lopes-de-sousa/diario-da-navegacao.js`
(8 partes por trecho da viagem, títulos com datas) e a linha do `index.html`. Autor novo em `conteudo/autores.js`.
Vocabulário: `edicoes/vocabulario/diario-pero-lopes.json` (96 verbetes, `conferir` ok). `revisao.json`: 8 decisões.

## Para o principal
- Gerar; Catálogo `obras` (obra nova); `traducoes_revisao.py --revisao` (8 escolhas). Sem `_redirects`.
- Notas gerais: não feitas. Fora: notas e documentos de Varnhagen e o fragmento da volta (pp. 109–113, ver revisao.json).
