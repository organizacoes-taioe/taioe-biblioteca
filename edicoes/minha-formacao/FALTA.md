# Minha Formação: o que falta (2026-11-05)

Branch `pedido-minha-formacao`, worktree `~/.cache/claude-wt5-minha-formacao`.

## Feito
- Fontes (cache em `ferramentas/cache/minha-formacao/`, só neste PC; cópias em `~/.cache/claude-pedidos-0511/minha-formacao/`):
  `pg76030.txt` (Gutenberg 76030, transcrição de 1900 sobre o exemplar de Toronto), `ia_djvu.xml` (OCR ABBYY
  do Internet Archive, minhaformao00nabuuoft), `harvard.txt` (djvutxt do DjVu do Commons, exemplar de Harvard,
  `@@PAGINA n@@` por página; djvulibre em `~/.cache/djvu-local/raiz`), `ws/wikisource_paginas.json` (páginas do
  Wikisource: texto moderno posto por robô), `ob1949.pdf/.txt` (Obras Completas 1949, BBM 4743).
- `config.py` (voto pg + ia + hv; modernas ws e ob; notas de rodapé fora do fluxo, em `notas-autor.txt`).

## Falta
- Conferir no fac-símile os pontos de `relatorios/sitios.tsv`, `modernas.tsv`, `sem_par.tsv`; decisões em
  `conferencia.json` / `decisoes.py`.
- `notas.py` (Sobre esta edição), autor em `conteudo/autores.js` (área nao-ficcao), `--publicar`.
- Vocabulário `edicoes/vocabulario/minha-formacao.json`; `revisao.json`.
