# Un cœur simple: o que falta

- [x] Texto (`poema.txt`): Gutenberg 12065 conferido com a 1ª edição (IA `troiscontesuncu00flaugoog`);
  correções e modernizações na nota da fonte em `obras.json`. Script de montagem fora do git:
  `~/.cache/claude-pedidos-0511/un-coeur-simple/scripts/montar_texto.py` (só neste PC).
- [x] Partes I–V numa obra só: `::parte I` no `poema.txt`; o `lingua_original.py` faz uma página por parte.
- [ ] Glossário: 3.196 chaves, 11.691 palavras. Feito em 14 lotes por subagentes, um de cada vez, em
  `lotes/<lote>.json` (regras em `~/.cache/claude-pedidos-0511/un-coeur-simple/BRIEF-GLOSSARIO.md`; fichas
  de trabalho em `.../fichas/ficha-<lote>.txt`, feitas por `.../scripts/fichas.py` do cache do fr.wiktionary,
  já completo em `ferramentas/cache/wiktionary/fr/c2`). Lotes: R1a R1b R2a R2b R3a R3b R4a R4b R5a R5b R6a R6b
  (palavras de conteúdo, na ordem do texto) e F1, F2 (palavras gramaticais, com todos os contextos, para os
  sentidos `#n`). Depois: juntar os lotes em `glossario.json`, apagar `lotes/`, `conferir un-coeur-simple`.
- [x] Tradução ao lado: nenhuma utilizável. A de 1897 (Lisboa, anônima) e a de Galeão Coutinho (~1942) não estão
  digitalizadas; a de José Osório de Oliveira (1940) é protegida (†1964). Sai sem tradução.
- [ ] Gerar e olhar o site na worktree; relatório ao principal.
