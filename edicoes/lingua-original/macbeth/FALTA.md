# Macbeth: o que falta

Texto: Cambridge 1865 (PG 47715, HTML), montado em `partes/` por `ferramentas/extrair.py` e `ferramentas/montar.py`
(numeração conferida com a da edição em todas as cenas; meios-versos recuados). Ferramenta e gerador já aceitam
teatro em partes (`lingua_original.py`: `partes`, `rascunho`, `teatro`, `::rubrica`; `gerar.mjs`: `marcarFala`,
`.teatro`).

Glossário (um só, `glossario.json`), ato por ato:
- fichas: `python3 edicoes/lingua-original/macbeth/ferramentas/fichas.py <worktree> <partes> 150 <saída>`
  (rascunhos em `~/.cache/claude-pedidos-0511/macbeth/fichas-atoN/`, só neste PC);
- cada lote: `python3 edicoes/lingua-original/macbeth/ferramentas/juntar.py <lote.json> <partes…>`;
- ato fechado: tirar `"rascunho": true` das partes dele em `obras.json`.

Estado:
- [x] Personagens + Ato I (1.393 verbetes; no ar no local)
- [x] Ato II (fichas, mapear e revisar)
- [ ] Ato III
- [ ] Ato IV
- [ ] Ato V
- [ ] revisão das notas difíceis (principal)
- [x] `edicoes/lingua-original/revisao-macbeth.json` (tradução ao lado: sem, recomendado)
