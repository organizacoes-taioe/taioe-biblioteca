# A democracia na América (seleção): o que falta

Branch `pedido-democracia-na-america`. Rascunhos e scripts fora do git em
`~/.cache/claude-pedidos-0511/democracia-na-america/` (só neste PC): `scripts/gut.sh` remonta `original/`
a partir do Gutenberg (`extrair_gut.py` + `montar.py`, com a lista de capítulos e as correções);
`scripts/checar.sh` confere blocos, chamadas de nota e mesóclise das traduções.

Feito: `original/` (14 arquivos, conferidos, `LEIAME.md`, `conferencia.tsv`), `CONVENCOES.md`,
`obra.py`, `revisao.json` (8 decisões), autor novo em `conteudo/autores.js`; tradução de 01–12 e 14.

Falta:
- tradução do 13 (despotismo), se não estiver em `traducao/`;
- ajustar em `obra.py` os títulos das partes 10 e 13 ao `# titulo` da tradução;
- `python3 ferramentas/traducoes.py democracia-na-america` (grava `conteudo/alexis-de-tocqueville/…` e
  `conteudo/nao-ficcao-traducoes.js`); vocabulário `edicoes/vocabulario/democracia-na-america.json`
  (`node ferramentas/vocabulario.mjs candidatos democracia-na-america`, depois `conferir`);
- gerar e conferir o site (sem commitar `public/`, `enderecos.json`, `obras.sql`).
