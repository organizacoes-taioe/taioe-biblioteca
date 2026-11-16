# Castelo interior: o que falta (branch `pedido-castelo-interior`)

Worktree: `~/.cache/claude-wt5-castelo-interior`. Downloads e trabalho do texto castelhano em
`~/.cache/claude-pedidos-0511/castelo-interior/` (só neste PC); os scripts e as decisões estão copiados em `estabelecer/`
(`montar.py` refaz `original/` a partir de `trab/votado2.json` + `decisoes-ctx.json`, `ementas.json`, `remendos.json`).

Feito (2026-11-16): texto castelhano (Silverio 1917; quatro OCRs, ~120 pontos conferidos nas imagens); tradução inteira
(prólogo, I–VII, epílogo; ~59 mil palavras; trechos em `traducao/trechos/`, notas dos tradutores em `traducao/notas-*.md`);
`revisao.json` (9 decisões, todas com a recomendação aplicada); autor novo em `conteudo/autores.js`;
`traducoes.py castelo-interior` gravou `conteudo/santa-teresa-de-jesus/castelo-interior.js` e a linha em `conteudo/catolicismo.js`;
`gerar.mjs` e `conferir.mjs` sem erro (`/biblioteca/santa-teresa-de-jesus/castelo-interior/`, um capítulo por página).

Falta: vocabulário (`edicoes/vocabulario/castelo-interior.json`, se ainda não estiver). Do principal: juntar a branch, gerar,
Catálogo `obras` (obra nova), `traducoes_revisao.py --revisao`, tirar dos pedidos. Sem regras de `_redirects`.

Se mudar um capítulo: editar `traducao/trechos/<morada>-<nn>.txt`, `trechos.py conferir <morada> <n>`, `trechos.py juntar`,
`python3 ferramentas/traducoes.py castelo-interior`.
