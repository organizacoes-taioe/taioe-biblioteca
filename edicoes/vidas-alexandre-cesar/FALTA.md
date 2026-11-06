# Vidas paralelas, Alexandre e César: estado

Branch `pedido-vidas-alexandre-cesar` do `taioe-biblioteca`. Regras da rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`.

## Pronto (2026-11-06)
- Grego de Perrin (1919) conferido com o fac-símile (`original/LEIAME.md`; scripts em `ferramentas/`, rodados de
  `~/.cache/claude-pedidos-0511/vidas-alexandre-cesar/`, onde estão os downloads do Perseus e do Internet Archive).
- Tradução inteira (18 arquivos, ~45 mil palavras), feita por três tradutores e revisada por um quarto contra o grego;
  notas dos tradutores em `traducao/notas-*.md`.
- `obra.py` com a «Sobre», `revisao.json` (8 decisões), autor `plutarco`, `conteudo/plutarco/`,
  `edicoes/vocabulario/vidas-alexandre-cesar.json` (47 verbetes, `conferir` ok).

## Para o principal
- Juntar a branch, `node ferramentas/site/gerar.mjs`, Catálogo `obras` (obra nova), `traducoes_revisao.py --revisao`
  e Catálogo `traducoes`; tirar dos pedidos. Nenhuma regra de `_redirects`.
- Notas gerais (lote futuro): o trocadilho de Amon (Alex. 27.5, ver `revisao.json`), os jogos de 24.5 (sátiro, σὰ
  Τύρος), 37.1 (λύκος, Λύκιος) e 2.5 (θρησκεύειν), Corfínio = Cornifício (César 43.1, 51.2).
