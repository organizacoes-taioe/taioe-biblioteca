# Confissão (Tolstói): o que falta

Branch `pedido-confissao-tolstoi` (worktree `~/.cache/claude-wt5-confissao-tolstoi`). Regras da rodada:
`~/.cache/claude-pedidos-0511/BRIEF.md`. Rascunhos e scripts: `~/.cache/claude-pedidos-0511/confissao-tolstoi/`
(`scripts/montar_original.py` refaz o original a partir do Wikisource; `img/` tem as páginas conferidas).

- [x] original russo montado e conferido (`original/`, LEIAME)
- [x] autor novo `liev-tolstoi` em `conteudo/autores.js`; `obra.py`
- [ ] tradução, capítulo por capítulo (feitos: I–IV) (`traducao/capitulo-NN.txt`, mesmo número de parágrafos)
- [ ] `CONVENCOES.md` com os termos fixados
- [ ] `revisao.json` (~8 decisões), conferir com `python3 ferramentas/traducoes_revisao.py`
- [ ] vocabulário `edicoes/vocabulario/confissao.json` (`node ferramentas/vocabulario.mjs conferir`)
- [ ] `python3 ferramentas/traducoes.py confissao-tolstoi`, gerar, conferir, olhar as páginas; não commitar `public/`
