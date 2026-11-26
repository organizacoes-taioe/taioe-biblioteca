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
- **Faltam no fac-símile as pp. 249 e 282 do livro** (PDF 260 e 294, «A Penna de Papagaio»): o Wikisource
  as preencheu com o texto de outra edição, na grafia de hoje. Ficam assim (decisão no `revisao.json`).
- Obras Completas (Brasiliense, 1947): **nenhum fac-símile livre achado** (Brasiliana USP, BN Digital,
  Internet Archive, Museu Monteiro Lobato; HathiTrust atrás de CAPTCHA; o registro «Reinações de Narizinho»
  da BBM é a tradução *Las travesuras de Naricita*, Buenos Aires, 1944). Edições gratuitas de 2019: o
  Internet Archive `reinacoes-de-narizinho` (ebook «Arlindo San», texto da Brasiliense, só as duas primeiras
  histórias) e o `marques-de-rabico` (Iba Mendes, «Projeto Livro Livre», 2019: diz «publicado
  originalmente em 1931», mas o texto é o revisto, da Brasiliense). Nenhuma serve de base.
- Duas leituras próprias das imagens (cópia dos scripts em `ocr/`): `scr/ocr.sh` (fundo normalizado por `scr/prep.py`, `--psm 3`) e
  `scr/ocr2.sh` (imagem original, `--psm 6`), em `~/.cache/claude-pedidos-2611/reinacoes-de-narizinho/`
  (imagens: `pdfimages -j` das pp. 9–321 em `dl/pag/NNN.jpg`; Tesseract de `~/.cache/tesseract-local/raiz`).

## Como refazer
1. `python3 -I edicoes/reinacoes-de-narizinho/paginas.py` → `1931/paginas.json`.
2. `python3 -I edicoes/reinacoes-de-narizinho/comparar.py` → `rel/pontos.tsv` (as duas leituras concordam
   contra o Wikisource) e `rel/raras.tsv`; `conferir.py <png> <pág>:<palavra>…` recorta as linhas;
   decisões em `conferencia.tsv` (ws | erro | ok).
3. `python3 -I edicoes/reinacoes-de-narizinho/montar.py [--publicar]` (grafia: `grafia.py`, decisões:
   `decisoes.py`, «Sobre»: `notas.py`).
4. Vocabulário: `edicoes/vocabulario/reinacoes-de-narizinho.json` (100 verbetes, `conferir` ok).

## Estado
- **Pronto para publicar.** Texto (11 histórias, 81 capítulos, ~79 mil palavras), grafia, «Sobre» (17 erros
  de 1931 listados; 21 leituras da transcrição corrigidas; 69 pontos conferidos nas imagens), `revisao.json`
  (5 decisões, recomendação aplicada), vocabulário (100 verbetes), autor novo `monteiro-lobato`.
  `gerar.mjs` e `conferir.mjs` sem erro; sem regra nova de `_redirects`.
- O principal: juntar, gerar, Catálogo `obras`, `traducoes_revisao.py --revisao` (as 5 decisões), tirar dos
  pedidos. Lista do advogado: nos EUA a edição de 1931 só entra em domínio público em 1º/1/2027.

## Dúvidas que ficaram
- «canudos incões» (p. 216 do livro): assim no impresso; palavra não achada nos dicionários.
- «philophoso» (Narizinho, p. 70) e «criminalogicos» (o visconde, p. 164) tratados como erros do impresso
  («philosopho», «criminologicos»); podem ser de propósito.
- p. 283: a ordem das linhas recompostas (ver `decisoes.py`) é reconstrução nossa.
