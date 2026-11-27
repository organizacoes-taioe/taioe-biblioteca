# Romeo and Juliet: o que falta

Pedido da rodada de 27/11 (regras: `~/.cache/claude-pedidos-2711/BRIEF.md`). Modelo: o *Macbeth*.

- Texto: pronto. Cambridge 1865 (vol. VII), PG 47715, recorte da peça em
  `~/.cache/claude-pedidos-2711/romeo-and-juliet/dl/rj.html` (de `~/.cache/claude-pedidos-0511/macbeth/baixados/pg47715.html`,
  linhas 1032–16604). `ferramentas/extrair.py rj.html cenas.json` e `ferramentas/montar.py cenas.json partes .`
  (numeração conferida com a da edição em todas as cenas; acertos em `FORCAR`, `JUNTAR`, `DIVIDIR`).
- Glossário: a fazer, ato por ato (fichas → lotes → `juntar.py`; do Ato II em diante, mapear e revisar), como no Macbeth.
  As partes ficam com `"rascunho": true` em `obras.json` até o glossário delas fechar.
- Tradução ao lado: a pesquisar (decisão em `../revisao-romeo-and-juliet.json`).
