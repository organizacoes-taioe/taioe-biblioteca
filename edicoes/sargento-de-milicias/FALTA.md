# Memórias de um Sargento de Milícias: estado (2026-11-05)

**Pronto para publicar.** Texto conferido, `texto.py --publicar` feito (`conteudo/manuel-antonio-de-almeida/
sargento-de-milicias.js`, linha no `index.html`), autor novo em `conteudo/autores.js`, vocabulário
(`edicoes/vocabulario/sargento-de-milicias.json`, 290 verbetes, `conferir` ok). `gerar.mjs` e `conferir.mjs` sem erro.

Falta só o do principal: juntar a branch, gerar o site, PR, Catálogo `obras.sql` no teste e na produção, merge,
tirar o pedido de `sugestoes.json` (Catálogo `sugestoes`). Notas gerais: na fila dos lotes, como os outros.

## Como foi feito (para refazer)
- Cache em `ferramentas/cache/sargento-de-milicias/` (só no desktop): `bbm4846.pdf` (BBM 4846), `tess-bbm4846/`
  (Tesseract, 297 páginas), `commons.txt` (camada do DjVu do Commons, `djvutxt --page=N` página a página,
  djvulibre em `~/.cache/djvu-local/raiz`), `wikisource_paginas.json`, páginas renderizadas em `ver/pag/`.
  O cache de 02/11 tinha sumido; foi refeito em 05/11 (o do Tesseract veio da worktree de 30/10).
- `python3 ferramentas/texto.py sargento-de-milicias [--publicar]`: voto das três leituras (config.py), grafia
  pela moderna (`config.modernizar`), depois `decisoes.corrigir()`:
  1. `conferencia.json`, cods `fix`/`erro`/`ws`: os pontos de `revisao.py` (o texto pronto contra o Wikisource,
     palavra por palavra) conferidos nas imagens por subagentes (474 pontos em 05/11, mais os manuais 1001+ e os
     versos 2001–2005); `erro` vai para a «Sobre» (21 erros de 1854–55; `sobre` dá o par curto quando o trecho
     tinha lixo de OCR);
  2. `FINAL`: grafia das formas de 1854 que sobraram (-ão → -am, couces → coices…); `ITALICO_SEMPRE`;
  3. quebras de parágrafo falsas (antes de minúscula ou «?»), `_pontuacao()` (sujeira «'», «•», «<»; pares
     «.,», «?.», «.:»; ponto antes de minúscula fora de abreviatura; «— —»);
  4. cod `ital`: 78 itálicos conferidos nas imagens (candidatos de `italico.py`, pela inclinação das letras).
- `python3 edicoes/sargento-de-milicias/revisao.py [--pranchas]` refaz a lista do que ainda difere do Wikisource
  (pula o já decidido); em 05/11 não sobrava ponto novo.

## Deixado como está (de propósito)
- Lições de 1854 que o Wikisource muda: «espanava», «havia custar», «havia pôr», «o havia ensinar», «tão pouco»,
  «uma irregularidade», «o quer que fosse», «haviam dizer», «cinteiro», «intercortada», «esconjúrio»,
  «incontinente», «as caçoados».
- Separadores de cena (linha de pontos) do impresso em dois lugares do tomo II (antes de «No dia seguinte» e de
  «Passado o tempo»): não representados.
- O itálico foi achado pelo detector; palavras em itálico que ele não pegou podem faltar.
- Vocabulário sem «toma-largura» (sem fonte segura) e sem comadre/compadre.
