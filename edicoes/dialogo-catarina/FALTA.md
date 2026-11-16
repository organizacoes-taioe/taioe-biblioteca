# Diálogo de Santa Catarina de Sena: o que falta (branch `pedido-dialogo-catarina`)

Worktree: `~/.cache/claude-wt5-dialogo-catarina`. Downloads e scripts do texto italiano:
`~/.cache/claude-pedidos-0511/dialogo-catarina/` (só neste PC; `scripts/paginas.py` baixa as páginas do Wikisource
em lotes de 50, `montar.py` e `gravar.py` refazem `original/`).

Feito (2026-11-16): tudo. Italiano de Fiorilli 1912 (`original/`, `LEIAME.md`), 5 partes (prólogo e os quatro
tratados), 167 capítulos, 1.037 parágrafos; tradução completa (`traducao/capitulos/000–167.txt` → `trechos.py juntar`
→ `traducao/<tratado>.txt`; notas dos tradutores em `traducao/notas-*.md`), `trechos.py conferir` 168/168 ok, sem
mesóclise; `revisao.json` (9 decisões, todas com a recomendação aplicada: nenhuma muda o texto); vocabulário
(`edicoes/vocabulario/dialogo-catarina.json`, 37 palavras, `conferir` ok); `traducoes.py dialogo-catarina` gravou
`conteudo/santa-catarina-de-sena/dialogo.js` e a linha em `conteudo/catolicismo.js`; autora nova em
`conteudo/autores.js`. `gerar.mjs` e `conferir.mjs` sem erro (`/biblioteca/santa-catarina-de-sena/dialogo/`).

Falta (do principal): juntar a branch, gerar o site, Catálogo `obras` (obra nova), `traducoes_revisao.py --revisao`,
tirar dos pedidos. Sem regras de `_redirects`. Notas gerais: não feitas (vão por lotes).

Se mudar um capítulo: editar `traducao/capitulos/<nnn>.txt`, `trechos.py conferir <n>`, `trechos.py juntar`,
`python3 ferramentas/traducoes.py dialogo-catarina`.
