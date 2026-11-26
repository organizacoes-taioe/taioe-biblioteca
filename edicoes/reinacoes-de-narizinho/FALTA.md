# Reinações de Narizinho: estado e o que falta (2026-11-26)

Branch `pedido-reinacoes-de-narizinho`. Pedido do Gere (rodada de 26/11; regras em
`~/.cache/claude-pedidos-2611/BRIEF.md`, só no notebook).

## Fontes (decididas)
- **Edição-base: a 1ª, 1931** (Companhia Editora Nacional, «Bibliotheca Pedagogica Brasileira, série 1,
  vol. I»; rosto: «As Reinações de Narizinho»), a única com fac-símile livre achado: o do Museu Monteiro
  Lobato (Taubaté, item `mml_obr0024`), que o Wikisource hospeda como «As Reinações de Narizinho.pdf»
  (175 MB, 321 páginas; fotos de um exemplar, com as ilustrações de J. G. Villin, †1979, protegidas até
  2050: nada delas entra). Transcrição do Wikisource sobre esse PDF: 297 páginas de texto, nível 3
  (revisadas uma vez, um transcritor só), salvo PDF 260 e 294 (nível 2).
- **Faltam no fac-símile as pp. 249 e 282 do livro** (PDF 260 e 294, ambas de «A Penna de Papagaio»):
  o Wikisource as preencheu com o texto de outra edição, na grafia de hoje («com algumas adaptações»,
  diz a página do índice). Ver decisão no `revisao.json`.
- Obras Completas (Brasiliense, 1947, a última revisão do autor): **nenhum fac-símile livre achado**
  (Brasiliana USP, BN Digital, Internet Archive, Museu Monteiro Lobato, HathiTrust atrás de CAPTCHA;
  o registro «Reinações de Narizinho» da BBM é a tradução *Las travesuras de Naricita*, Buenos Aires,
  1944). O Internet Archive `reinacoes-de-narizinho` é um ebook moderno («Digitalização e Revisão Arlindo
  San»), do texto da Brasiliense, só com as duas primeiras histórias: não serve de base.
- Segundo testemunho: OCR próprio (Tesseract) das imagens do mesmo PDF
  (`~/.cache/claude-pedidos-2611/reinacoes-de-narizinho/scr/ocr.sh`: `pdfimages -j` das pp. 9–321, fundo
  normalizado por `prep.py`, `tesseract -l por --psm 3`, com o Tesseract de `~/.cache/tesseract-local/raiz`).

## Passos
1. `python3 -I edicoes/reinacoes-de-narizinho/paginas.py` → `1931/paginas.json` (texto de 1931 por página). FEITO.
2. Comparar com o Tesseract página a página e conferir nas imagens as divergências. EM ANDAMENTO.
3. Grafia de hoje, montagem das 11 histórias e «Sobre». FALTA.
4. Vocabulário. FALTA.
