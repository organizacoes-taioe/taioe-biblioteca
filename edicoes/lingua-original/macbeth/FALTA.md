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
- [x] Ato III (fichas, mapear e revisar)
- [~] Ato IV: fichas 01–05 feitas (lotes ato4-lote-01…05; glossário com 3.408 verbetes); faltam o mapear e o revisar
  (refazer com `fichas.py <wt> 4-1,4-2,4-3 150 ~/.cache/claude-pedidos-0511/macbeth/revisao-ato4`, que dá 0 chaves
  novas e o mapear.txt/revisar.txt em dia; seção final do `BRIEF-GLOSSARIO.md`), a conferência (`juntar.py <lote> 4-1 4-2 4-3`)
  e tirar o `rascunho` das partes 4-* em `obras.json`. Pendente do revisar: `gall` (19:29.2) pede variante.
- [ ] Ato V: fichas já geradas em `~/.cache/claude-pedidos-0511/macbeth/fichas-ato5/` (01–03; o mapear/revisar de lá é velho:
  refazer como no Ato IV depois das fichas)
- [ ] revisão das notas difíceis (principal)
- [x] `edicoes/lingua-original/revisao-macbeth.json` (tradução ao lado: sem, recomendado)

Como retomar (um subagente Sonnet por vez, instruções em `~/.cache/claude-pedidos-0511/macbeth/BRIEF-GLOSSARIO.md`, só neste PC):
fichas de um ato → lotes `atoN-lote-NN.json` → `revisao-atoN/` (mapear e revisar) → conferência → tirar o `rascunho`.
Sem fichas no outro PC: `fichas.py` as refaz (o cache do Wiktionary fica em `ferramentas/cache/`).
Atos I–III no ar no local; publicar só depois do V (ou publicar I–III, que já saem sem as partes em rascunho).
