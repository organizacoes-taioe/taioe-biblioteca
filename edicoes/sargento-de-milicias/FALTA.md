# Memórias de um Sargento de Milícias: o que falta (2026-11-02, fim da rodada das 15:45)

Estado: **fontes e confronto montados e rodando; texto ainda não conferido nem publicado.**

## Feito
- Edição-base achada: a 1ª em livro (Typographia Brasiliense de Maximiano Gomes Ribeiro, tomo I 1854,
  tomo II 1855), fac-símile da Brasiliana USP, BBM 4846 (`config.PDF`; o mesmo exemplar é o DjVu do
  Commons/Wikisource, com a mesma numeração de páginas).
- `config.py`: os 48 capítulos (23 + 25) com as páginas e os títulos de 1854–55 na grafia de hoje
  (lidos na camada do PDF; o Wikisource troca alguns: «batismo», «Despedidas»); três leitores:
  `camada()` (OCR da Brasiliana, pdftotext), `tesseract()` (OCR novo, já rodado: cache
  `ferramentas/cache/sargento-de-milicias/tess-bbm4846/`, 301 páginas) e `wikisource_moderno()`
  (texto moderno, Formulário de 1943, posto sobre as páginas do DjVu; dá parágrafos e grafia).
  `python3 edicoes/sargento-de-milicias/config.py` mostra as palavras por capítulo: as três fontes
  batem capítulo a capítulo (ws 59.530, pdf 59.565, bt 60.033 palavras).
- `transcricoes()`, `modernizar()`, `agrupar()` (dois tomos, «## Capítulo N — título» + «{§ T.c}») e `rotulos()`.
- `python3 ferramentas/texto.py sargento-de-milicias` roda: 48 partes, 1.456 parágrafos; relatórios
  em `ferramentas/cache/sargento-de-milicias/relatorios/` (3.364 sítios sem maioria, 722 em
  `modernas.tsv`, 1.711 em `pontuacao.tsv`, 620 em `sem_par.tsv`, 471 em `vocabulario.tsv`).
- `decisoes.py` e `notas.py` com a estrutura e um rascunho da «Sobre» (Texto-base, Fontes).

## Falta (na ordem)
1. **Desempate dos 3.364 sítios**: só há dois OCRs do mesmo exemplar, então nada tem maioria. Seguir
   *Caetés*/*Angústia*: `rever()` próprio (léxico + Wikisource), `revisao.py` para juntar os pontos a
   conferir, pranchas nas imagens (`conferir.py` de Policarpo/Caetés, renderizando antes as páginas com
   `pdftoppm` em paralelo) e `conferencia.json`. Talvez valha um terceiro OCR (outra página ou outro
   exemplar da 1ª edição: procurar na HathiTrust/Google Books/BN Digital) para ter maioria.
2. **Formas de 1854**: `transcricoes()` dá ao `ocr.limpar` o léxico das palavras que os dois OCRs leram
   iguais, senão a guia moderna «corrigia» as formas da época («passavão» → «passavam»). A 3ª do plural
   em -ão passa a -am em `config.modernizar` quando o Wikisource, no mesmo ponto, traz -am (610 trocas;
   o futuro em -ão fica). Sobram umas 30 onde o alinhamento não é 1:1 («puzerão», «havião», «vião»):
   ver `sem_par.tsv` e `modernas.tsv` e resolver em `MANUAL`/`AJUSTES` (cuidado com o futuro).
3. **Ruído no começo**: «chamava-se nesse tempo-O — O. canto dos meirinhos —» (o Wikisource tem
   «tempo-O canto dos meirinhos-», com hífens no lugar de travessões; 1854: «— O canto dos meirinhos —»).
   Os travessões de citação e as aspas do Wikisource não são de fiar.
4. **Itálico**: nenhum dos OCRs marca; ver se *Angústia* (`italico.py`, inclinação das letras) serve.
5. **Versos** (modinhas, p. 10 e outras) em `decisoes.VERSOS` ou pelo `<poem>` do Wikisource.
6. Grafia final (`MANUAL`), `notas.py` completa (erros corrigidos, lista, descrição das fontes) e
   `texto.py --publicar`.
7. Autor novo em `conteudo/autores.js` (`manuel-antonio-de-almeida`, 1831–1861, Rio de Janeiro; nota
   curta, sem marketing), a linha em `conteudo/obras.json`/`index.html` se o gerador pedir.
8. `edicoes/vocabulario/sargento-de-milicias.json` (`edicoes/vocabulario/LEIA.md`;
   `node ferramentas/vocabulario.mjs … conferir` dá `ok`): o livro tem muito léxico de época (meirinho,
   chicana, rótula, mantilha, granadeiro, ucharia, malsinar…).
9. Gerar e conferir (`gerar.mjs`, `conferir.mjs`) sem commitar o gerado; commit e push na branch.

Publicação, depois do merge (com o principal): Catálogo `obras.sql` no teste e na produção e tirar o
pedido de `sugestoes.json` (Catálogo `sugestoes`).
