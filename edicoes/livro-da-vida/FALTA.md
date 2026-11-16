# Livro da Vida: o que falta (branch `pedido-livro-da-vida`)

Worktree: `~/.cache/claude-wt5-livro-da-vida`. Downloads (OCRs, hOCR): `~/.cache/claude-pedidos-0511/livro-da-vida/dl/`
(só neste PC); cópia dos scripts em `fonte/`.

Feito (2026-11-16): tudo.
- Castelhano de Silverio 1915 (`original/`, `LEIAME.md`): 42 arquivos (prólogo, 40 capítulos, epílogo), ~113 mil palavras,
  OCR corrigido por regra (`fonte/corrigir.py`, `corrigir2.py`), pela colação com a BAE 53 e a Heitz e pelas leituras
  anotadas pelos tradutores (`original/correcoes-ocr.tsv`, 410 trocas, `fonte/aplicar.py`); uma linha perdida pelo OCR
  reposta (31.3), notas do editor e cabeços tirados (6.1, 17.4, 20.15, 37.11).
- Tradução inteira (`traducao/00.txt`…`41.txt`, `trechos.py estado` todo ok), 8 lotes, notas dos tradutores em
  `traducao/notas-*.md`; termos iguais aos do *Castelo Interior* (arroubamento, embevecimento, aspas «», `[Trad.: …]`,
  «Nele»); `CONVENCOES.md` com a tabela de termos de todos os lotes.
- `revisao.json` (8 decisões, recomendação aplicada em todas); vocabulário (`edicoes/vocabulario/livro-da-vida.json`,
  69 palavras, `conferir` ok); `traducoes.py livro-da-vida` gravou `conteudo/santa-teresa-de-jesus/livro-da-vida.js` e
  a linha em `conteudo/catolicismo.js`; autor: o bloco do *Castelo Interior* (na main). `gerar.mjs`/`conferir.mjs` sem erro.

Falta (do principal): juntar a branch, gerar o site, Catálogo `obras` (obra nova), `traducoes_revisao.py --revisao`,
tirar dos pedidos. Sem regras de `_redirects`. Notas gerais: não feitas (vão por lotes).

Pontos abertos, nas notas dos tradutores («Para o Gere decidir»): 13.13 «Digo todos» (talvez «No digo todos»), 28.9 (a
tradução pôs em pergunta uma frase que se contradiz), 40.20 (dois pontos de leitura). Se mudar um capítulo: editar
`traducao/NN.txt`, `trechos.py conferir N`, `python3 ferramentas/traducoes.py livro-da-vida`.
