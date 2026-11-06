# Autobiografia de Franklin: o que falta (branch `pedido-autobiografia-franklin`)

Worktree: `~/.cache/claude-wt5-autobiografia-franklin`. Scripts e downloads do texto inglês:
`~/.cache/claude-pedidos-0511/autobiografia-franklin/` (só neste PC; `scripts/montar.py` e `dividir.py`
refazem `original/` a partir do Gutenberg 148 e dos três OCRs de 1868 — mas `original/` já foi corrigido à
mão depois: não rodar de novo sem conferir o diff).

Feito (2026-11-06): tudo. Texto inglês de Bigelow 1868 (`original/`, `LEIAME.md`), 4 partes e 22 capítulos nossos,
tradução completa (`traducao/trechos/*.txt` → `trechos.py juntar` → `traducao/parte-1..4.txt`; notas dos tradutores em
`traducao/notas-*.md`), versos conferidos no `molde.mjs` (Folger, Pope em alexandrinos, Dryden ×2, Addison, Thomson; só ✓ e ~),
`revisao.json` (8 decisões, todas com a recomendação aplicada: nenhuma muda o texto), vocabulário
(`edicoes/vocabulario/autobiografia-franklin.json`, 30 palavras, `conferir` ok), `traducoes.py autobiografia-franklin` gravou
`conteudo/benjamin-franklin/autobiografia.js` e a linha em `conteudo/nao-ficcao-traducoes.js`; autor novo em `conteudo/autores.js`.
`gerar.mjs` e `conferir.mjs` sem erro (29 páginas em `/biblioteca/benjamin-franklin/autobiografia/`).

Falta (do principal): juntar a branch, gerar o site, Catálogo `obras` (obra nova), `traducoes_revisao.py --revisao`,
tirar dos pedidos. Sem regras de `_redirects`. Notas gerais: não feitas (vão por lotes).

Se mudar um capítulo: editar `traducao/trechos/<parte>-<nn>.txt`, `trechos.py conferir <parte> <n>`, `trechos.py juntar`,
`python3 ferramentas/traducoes.py autobiografia-franklin`.
