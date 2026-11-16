# São Francisco de Assis (Chesterton): o que falta (branch `pedido-sao-francisco-chesterton`)

Worktree: `~/.cache/claude-wt5-sao-francisco-chesterton`. Downloads, scripts da conferência e recortes:
`~/.cache/claude-pedidos-0511/sao-francisco-chesterton/` (só neste PC). Regras da rodada:
`~/.cache/claude-pedidos-0511/BRIEF.md`.

## Feito (2026-11-16): tudo

- Texto inglês da 1ª ed. (1923) em `original/` (`montar.py` a partir do Gutenberg 63084, com 5 emendas pela
  impressão; `LEIAME.md`), conferido palavra por palavra com três OCRs de três exemplares de 1923.
- Tradução dos 10 capítulos (`traducao/capitulo-1..10.txt`, parágrafos iguais aos do original: 139), notas
  dos tradutores em `traducao/notas-1..10.md`. Cap. I pelo principal; II–X por subagentes Opus, um por vez, com
  o `CONVENCOES.md`; termos uniformizados no fim (Jograis de Deus, aspas dos versos). Grep de mesóclise vazio.
- Versos de Belloc (cap. III) em octossílabos, rimas aabb, no `molde.mjs` sem ✗ nem ≠ (`notas-3.md`).
- `revisao.json`: 10 decisões, todas com a recomendação aplicada (nenhuma muda o texto).
- Vocabulário `edicoes/vocabulario/sao-francisco-de-assis.json` (33 verbetes, `conferir` ok).
- `traducoes.py sao-francisco-de-assis` gravou `conteudo/g-k-chesterton/sao-francisco-de-assis.js` e a linha
  em `conteudo/catolicismo.js`. `gerar.mjs` e `conferir.mjs` sem erro (12 páginas em
  `/biblioteca/g-k-chesterton/sao-francisco-de-assis/`).

## Falta (do principal)

Juntar a branch, gerar o site, Catálogo `obras` (obra nova), `traducoes_revisao.py --revisao`, tirar dos pedidos.
Sem regras de `_redirects`. Autor já existia. Notas gerais: não feitas (vão por lotes).

Se mudar o inglês: editar `EMENDAS` no `montar.py` e rodar (`python3 edicoes/sao-francisco-de-assis/montar.py`).
Se mudar a tradução: editar `traducao/capitulo-N.txt` e `python3 ferramentas/traducoes.py sao-francisco-de-assis`.
