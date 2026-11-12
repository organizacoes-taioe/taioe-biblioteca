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
- [x] fontes baixadas; `original/prefacio.txt`, `parte-1.txt`, `parte-2.txt` = 1917 cru (falta aplicar as mudanças de 1920)
- [ ] aplicar as mudanças de 1920 nas partes I–II (por script) e conferir nas imagens
- [ ] parte III e Anhang do OCR (por script), conferidos nas imagens; Nachtrag
- [ ] tradução, parte por parte (`traducao/`), `CONVENCOES.md`, `obra.py`, `revisao.json`, vocabulário
