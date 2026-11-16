# Livro da Vida: o que falta (branch `pedido-livro-da-vida`)

Worktree: `~/.cache/claude-wt5-livro-da-vida`. Downloads e scripts: `~/.cache/claude-pedidos-0511/livro-da-vida/`
(cópia dos scripts em `fonte/`).

Feito:
- texto castelhano de Silverio 1915 montado (`original/`, `LEIAME.md`), 42 arquivos, ~113 mil palavras;
- `CONVENCOES.md` (termos místicos: os mesmos do *Castelo Interior*), `trechos.py`, `obra.py`, autor novo em `conteudo/autores.js`.

Falta:
- tradução: `python3 edicoes/livro-da-vida/trechos.py estado` diz o que já está em `traducao/NN.txt`;
  um tradutor por vez, por blocos de capítulos, com `trechos.py conferir N`;
- dúvidas de OCR que sobraram (`~/.cache/claude-pedidos-0511/livro-da-vida/dl/duvidas.tsv`), a corrigir no `original/`;
- uniformização final dos termos; `revisao.json` (~8 pontos); vocabulário; `traducoes.py livro-da-vida`; gerar e conferir.
