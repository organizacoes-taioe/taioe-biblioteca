# Castelo interior: o que falta (branch `pedido-castelo-interior`)

Worktree: `~/.cache/claude-wt5-castelo-interior`. Downloads e trabalho do texto castelhano em
`~/.cache/claude-pedidos-0511/castelo-interior/` (só neste PC); scripts copiados em `estabelecer/`.

Feito:
- texto castelhano (Silverio 1917) estabelecido por quatro OCRs e conferido nas imagens: `original/` (9 arquivos,
  ~59 mil palavras), `original/LEIAME.md`; `CONVENCOES.md`, `obra.py`, `trechos.py`; autor novo em `conteudo/autores.js`.

Falta:
- tradução, por capítulo: `python3 edicoes/castelo-interior/trechos.py mostrar I 1` (ler um trecho por vez),
  gravar `traducao/trechos/I-01.txt`, `trechos.py conferir I 1`; estado com `trechos.py estado`.
  (P = prólogo e E = epílogo, trecho 0; nas moradas o trecho 0 é a linha «Hay en ellas…».)
- `trechos.py juntar`, `python3 ferramentas/traducoes.py castelo-interior`, `revisao.json` (~8 decisões),
  vocabulário (`edicoes/vocabulario/castelo-interior.json`), uniformizar termos, grep de mesóclise, gerar e conferir.
