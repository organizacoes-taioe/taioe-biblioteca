# Branch pedido-magisterio-6 (pedidos de 05/11): o que falta

Dois documentos de Pio XI: *Ad Catholici Sacerdotii* (1935, latim, AAS 28 (1936), p. 5-53) e *Non Abbiamo
Bisogno* (1931, italiano, AAS 23 (1931), p. 285-312). Rascunhos e scripts (fora do git) em
`~/.cache/claude-pedidos-0511/magisterio-6/` (só neste PC).

- [x] Originais montados e conferidos com o OCR das AAS (`<doc>/original/<doc>.txt`, com {§ n} da versão inglesa).
- [ ] Tradução (`<doc>/traducao/<doc>.txt`) e notas do tradutor (`traducao/notas-<doc>.md`).
- [ ] `obras.py` (DOCS, CORRECOES) → `python3 edicoes/magisterio/obras.py <doc>`; linhas em `conteudo/catolicismo.js`
      e `conteudo/igreja-catolica/<doc>.js` pelo `python3 ferramentas/traducoes.py magisterio/<doc>`.
- [ ] `revisao-<doc>.json` (1–2 decisões), vocabulário `edicoes/vocabulario/<doc>.json` (`conferir` ok).
- [ ] gerar/conferir na worktree, sem commitar `public/`, `enderecos.json`, `obras.sql`.

Falta ao principal: juntar a branch, gerar o site, Catálogos e tirar os dois dos pedidos.
