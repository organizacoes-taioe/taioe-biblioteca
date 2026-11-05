# Autobiografia de Franklin: o que falta (branch `pedido-autobiografia-franklin`)

Worktree: `~/.cache/claude-wt5-autobiografia-franklin`. Scripts e downloads do texto inglês:
`~/.cache/claude-pedidos-0511/autobiografia-franklin/` (só neste PC; `scripts/montar.py` e `dividir.py`
refazem `original/` a partir do Gutenberg 148 e dos três OCRs de 1868 — mas `original/` já foi corrigido à
mão depois: não rodar de novo sem conferir o diff).

Feito:
- [x] texto inglês (`original/parte-1..4.txt`, `LEIAME.md`), divisão em capítulos, `obra.py`, `CONVENCOES.md`, autor novo em `conteudo/autores.js`.

Falta (na ordem):
- [ ] tradução, um arquivo por parte em `traducao/` (mesmo número de blocos; marcas e títulos `## n.` iguais);
      ver o estado de cada capítulo abaixo.
- [ ] versos (Folger, Pope ×3, Dryden ×2, Addison, Thomson) em verso, conferidos com `molde.mjs`.
- [ ] uniformizar termos (CONVENCOES §3), grep de mesóclise, contar blocos.
- [ ] `revisao.json` (~8 decisões) e `python3 ferramentas/traducoes_revisao.py`.
- [ ] `edicoes/vocabulario/autobiografia-franklin.json` e `node ferramentas/vocabulario.mjs conferir`.
- [ ] `python3 ferramentas/traducoes.py autobiografia-franklin`, `gerar.mjs`, `conferir.mjs`, olhar as páginas;
      depois `git checkout -- public ferramentas/site/enderecos.json ferramentas/sql/obras.sql` e `git clean -fd public`.

Estado da tradução por capítulo:
