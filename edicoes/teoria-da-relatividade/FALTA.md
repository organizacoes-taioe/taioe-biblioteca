# Teoria da relatividade (Einstein): o que falta

Branch `pedido-teoria-da-relatividade`. Rascunhos e scripts fora do git em `~/.cache/claude-pedidos-0511/teoria-da-relatividade/`
(`dl/`: Gutenberg 77850, 1ª ed. 1917, e os dois exemplares da 5ª ed., 1920, do Internet Archive, PDF e OCR;
`scripts/montar_g.py` divide o Gutenberg; `scripts/diff1920*.py` lista as mudanças de 1917 → 1920; `pag/`: páginas em PNG).

Edição-base: **5ª ed. (Vieweg, 1920)**, com o «Nachtrag zur dritten Auflage», a parte III («Betrachtungen über die Welt
als Ganzes», §§ 30–32) e o Anhang (derivação de Lorentz e mundo de Minkowski). Livre no Brasil (†1955) e nos EUA
(publicada antes de 1931). O texto de 1917 (Gutenberg, revisado pelo DP) é a base das partes I e II, com as mudanças
de 1920 aplicadas (lista em `diff1920.txt` no rascunho); parte III, Anhang e notas novas vêm do OCR das duas cópias
de 1920, conferido nas imagens. **O alemão só entra por script** (nunca colado à mão).

Estado (2026-11-12):
- [x] alemão montado por script: `bash ~/.cache/claude-pedidos-0511/teoria-da-relatividade/scripts/construir.sh`
  (cópia dos scripts e das listas de correção em `.../fontes-git/`; reconstrói `original/` inteiro)
- [x] tradução: prefácio + adendo, parte I (§§ 1–17). Trechos em `~/.cache/claude-pedidos-0511/teoria-da-relatividade/trad/p<N>-*.txt`,
  juntados por `scripts/juntar.sh` em `traducao/parte-<N>.txt` (confere blocos e marcas com o original)
- [ ] tradução: parte II (§§ 18–29), parte III (§§ 30–32), apêndice
- [ ] figuras (4: Fig. 1, 2, 3 e a do tubo de Fizeau): hoje são blocos `{fig N}` nos dois lados; falta decidir o desenho (SVG) e o gerador
- [ ] `obra.py`, `CONVENCOES.md`, `original/LEIAME.md`, `revisao.json` (~8), vocabulário, `traducoes.py`, gerar e conferir
