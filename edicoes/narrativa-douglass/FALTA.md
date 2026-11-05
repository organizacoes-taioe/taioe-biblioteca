# Narrativa da vida de Frederick Douglass: o que falta

Branch `pedido-narrativa-douglass` (worktree `~/.cache/claude-wt5-narrativa-douglass`). Regras da rodada:
`~/.cache/claude-pedidos-0511/BRIEF.md`. Downloads e scripts: `~/.cache/claude-pedidos-0511/narrativa-douglass/`.

- [x] texto inglês estabelecido (`original/`, `original/LEIAME.md`)
- [x] autor novo em `conteudo/autores.js`, `obra.py`
- [ ] tradução, parte por parte (`traducao/<mesmo nome>.txt`, um parágrafo por parágrafo):
      prefácio, carta, I–XI, apêndice
- [ ] versos pelo Versificador (`versos/`): cantiga do cap. II, Whittier no cap. VIII e no apêndice, a paródia
- [ ] `revisao.json` (~8 decisões) e `python3 ferramentas/traducoes_revisao.py`
- [ ] `edicoes/vocabulario/narrativa-douglass.json` (`node ferramentas/vocabulario.mjs conferir`)
- [ ] `python3 ferramentas/traducoes.py narrativa-douglass`, gerar e conferir o site; commit só das fontes
