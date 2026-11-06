# Un cœur simple: o que falta

- [x] Texto (`poema.txt`): Gutenberg 12065 conferido com a 1ª edição (IA `troiscontesuncu00flaugoog`);
  correções e modernizações na nota da fonte em `obras.json`. Script de montagem fora do git:
  `~/.cache/claude-pedidos-0511/un-coeur-simple/scripts/montar_texto.py` (só neste PC).
- [x] Partes I–V numa obra só: `::parte I` no `poema.txt`; o `lingua_original.py` faz uma página por parte.
- [ ] Glossário: 3.196 chaves, 11.691 palavras, em 14 lotes feitos por subagentes Sonnet, um de cada vez, em
  `lotes/<lote>.json` (regras: `~/.cache/claude-pedidos-0511/un-coeur-simple/BRIEF-GLOSSARIO.md`; fichas de
  trabalho: `.../fichas/ficha-<lote>.txt`, feitas por `.../scripts/fichas.py` a partir do cache do fr.wiktionary,
  já completo em `ferramentas/cache/wiktionary/fr/c2`; tudo isso só neste PC).
  - **Feitos (13 de 14)**: R1a R1b R2a R2b R3a R3b R4a R4b R5a R5b R6a R6b (palavras de conteúdo) e F1 (le, la,
    les, l’, un, une, des, du, de, d’, au, aux, en, y, lui, leur, leurs, com os sentidos `#n` separados).
  - **Falta F2**: `fichas/ficha-F2.txt` (que, qui, si, tout, plus, pas, ne, même, comme, pronomes, preposições,
    conjunções…; lista em `fichas/F2.txt`). Lançar um subagente como os anteriores, com as regras de F1 (a chave
    simples com o uso mais comum, `#n` com todas as referências) e o aviso: `vous` em 53.9 e 61.10 é parte de
    «rendez-vous» (o tokenizador separa «-vous»): `vous#n` com nota que remete a «rendez».
  - Depois: juntar os 14 lotes num `glossario.json` (verbetes e ocorrencias; nenhuma chave repetida entre lotes),
    apagar `lotes/`, `python3 ferramentas/lingua_original.py conferir un-coeur-simple` até «tudo certo».
  - Revisão a fazer ao juntar: `vérole` (def «varíola», é «petite vérole»), `saint-melaine` (dizer só «lugar de
    Pont-l’Évêque onde Mme Aubain morava antes», sem «bairro»), as dúvidas que os relatórios dos lotes listaram
    (nomes próprios com nota de contexto; `y`, `en` #2/#4, `de` #2).
  - Por fim: `publicar`, `gerar.mjs` e `conferir.mjs`, olhar as páginas (I–V), commit de `conteudo/` (não de
    `public/`, `enderecos.json` nem `obras.sql`) e o relatório ao principal.
- [x] Tradução ao lado: nenhuma utilizável. A de 1897 (Lisboa, anônima) e a de Galeão Coutinho (~1942) não estão
  digitalizadas; a de José Osório de Oliveira (1940) é protegida (†1964). Sai sem tradução.
- [ ] Gerar e olhar o site na worktree; relatório ao principal.
