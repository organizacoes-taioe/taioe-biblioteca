# Romeo and Juliet: o que falta

Pedido da rodada de 27/11 (regras: `~/.cache/claude-pedidos-2711/BRIEF.md`). Modelo: o *Macbeth*.

- Texto: pronto. Cambridge 1865 (vol. VII), PG 47715, recorte da peça em
  `~/.cache/claude-pedidos-2711/romeo-and-juliet/dl/rj.html` (de `~/.cache/claude-pedidos-0511/macbeth/baixados/pg47715.html`,
  linhas 1032–16604). `ferramentas/extrair.py rj.html cenas.json` e `ferramentas/montar.py cenas.json partes .`
  (numeração conferida com a da edição em todas as cenas; acertos em `FORCAR`, `JUNTAR`, `DIVIDIR`).
- Glossário: Atos I a III prontos (fora do rascunho). Atos IV–V: fichas → lotes → `juntar.py`, depois mapear e revisar, como no Macbeth (`~/.cache/claude-pedidos-2711/romeo-and-juliet/BRIEF-GLOSSARIO.md`).
  As partes ficam com `"rascunho": true` em `obras.json` até o glossário delas fechar.
- Tradução ao lado: pesquisada; nenhuma completa em verso e em domínio público acessível. Decisão «sem tradução ao lado» em `../revisao-romeo-and-juliet.json` (recomendação aplicada).
- Verbete «t» («'t» = it) sem uso nos Atos I–II (o «t'» de II.4 é «t#2»); se ninguém o usar no fim, apagar.
