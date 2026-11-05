# Macunaíma: estado (2026-11-05)

**Pronto para publicar** (branch `pedido-macunaima`): `conteudo/mario-de-andrade/macunaima.js` (19 partes,
~44 mil palavras), linha no `index.html`, «Sobre», `revisao.json` (8 decisões, todas com a recomendação
já aplicada; nenhuma muda o texto se ele aceitar) e `edicoes/vocabulario/macunaima.json` (262 verbetes,
`conferir` ok). O autor (`mario-de-andrade`) já existia. `gerar.mjs` e `conferir.mjs` sem erro.

O principal: juntar, gerar, Catálogo `obras`, `traducoes_revisao.py --revisao` (as 8 decisões) e tirar dos
pedidos. Sem regra nova de `_redirects`.

## Para refazer o texto do zero (cache fora do git)
- `ferramentas/cache/macunaima/`: `wikisource_paginas.json` e `ia_or182096.txt` baixam sozinhos; `tess/`
  = Tesseract das 253 páginas de `https://archive.org/download/or182096/or182096.pdf` (`pdftoppm -r 300
  -gray -png`, `tesseract -l por --psm 6`, um `NNN.txt` por página com 3 dígitos), com o Tesseract de
  `~/.cache/tesseract-local/raiz`. Script: `~/.cache/claude-pedidos-0511/macunaima/scr/ocr.sh` (só neste PC).
  Com o mesmo Tesseract, as leituras saem idênticas e as chaves de `conferencia.json` acham o lugar.
- Pranchas e listas de conferência: `~/.cache/claude-pedidos-0511/macunaima/` (só neste PC).

## Pendências menores (não impedem a publicação)
- Os erros de OCR dos caps. I–XI foram achados pela comparação com uma edição moderna e pelas palavras
  fora do léxico; uma leitura corrida do cap. I–XI nas imagens ainda pegaria algum resto (palavra
  existente trocada por outra, em sítios onde os dois OCRs erram juntos).
- Vocabulário: as definições de tupi foram escritas por um subagente; ~40 conferidas na web, as outras de
  conhecimento geral. Ficaram de fora por falta de fonte (zungu, puíto, sairê, pacuera, papiri, pixé…).
