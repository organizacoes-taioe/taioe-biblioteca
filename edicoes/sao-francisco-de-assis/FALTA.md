# São Francisco de Assis (Chesterton): o que falta (branch `pedido-sao-francisco-chesterton`)

Worktree: `~/.cache/claude-wt5-sao-francisco-chesterton`. Downloads, scripts da conferência e recortes:
`~/.cache/claude-pedidos-0511/sao-francisco-chesterton/` (só neste PC). Regras da rodada:
`~/.cache/claude-pedidos-0511/BRIEF.md`.

## Feito

- Texto inglês de 1923 (`original/`, `LEIAME.md`, `montar.py`), conferido com três OCRs de 1923.
- `CONVENCOES.md`, `obra.py` (gênero «Hagiografia»).

## Falta

- Tradução: `traducao/capitulo-N.txt` (1 a 10) e `notas-N.md`. Estado de cada capítulo abaixo.
- Versos de Belloc (cap. III) no `molde.mjs`.
- Uniformizar os termos no fim (CONVENCOES § 3), grep de mesóclise.
- `revisao.json` (~8 decisões), `python3 ferramentas/traducoes_revisao.py`.
- Vocabulário `edicoes/vocabulario/sao-francisco-de-assis.json` (`node ferramentas/vocabulario.mjs conferir`).
- `python3 ferramentas/traducoes.py sao-francisco-de-assis`, `gerar.mjs`, `conferir.mjs`, olhar as páginas;
  desfazer `public/`, `enderecos.json`, `obras.sql` antes do commit.

## Capítulos

| cap. | estado |
|---|---|
| I–III | por traduzir (tradutor principal) |
| IV–VI | traduzidos (subagente Opus, 16/11), notas em `notas-4..6.md` com candidatos ao `revisao.json` |
| VII–IX | com um subagente Opus (16/11) |
| X | por traduzir |
