# A democracia na América (seleção): o que falta

Branch `pedido-democracia-na-america`. Rascunhos e scripts fora do git em
`~/.cache/claude-pedidos-0511/democracia-na-america/` (só neste PC): `scripts/gut.sh` remonta `original/`
a partir do Gutenberg (`extrair_gut.py` + `montar.py`, com a lista de capítulos e as correções).

Feito:
- `original/`: 14 arquivos (Introdução e 13 capítulos), 12ª ed. 1848 pela transcrição do Gutenberg
  (30513–30516, DP, da BnF/Gallica), conferida com o Wikisource 1848 e 1866 e, nas divergências, no
  fac-símile 1848 do Commons (`conferencia.tsv` no rascunho).
- `CONVENCOES.md` (termos fixos).

Falta:
- traduzir os 14 arquivos (`traducao/`, mesmo número de blocos), commit e push a cada um;
- `original/LEIAME.md`, `obra.py`, `revisao.json`, vocabulário, `traducoes.py democracia-na-america`,
  autor novo em `conteudo/autores.js`, gerar e conferir o site (sem commitar `public/`).
