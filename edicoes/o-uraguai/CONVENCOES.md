# O Uraguai: convenções da edição

Texto da 1ª edição (Lisboa, Régia Oficina Tipográfica, 1769) na grafia brasileira de hoje. Passo a passo em
`montar.py` (versos), `notas.py` (notas) e `publicar.py` (site).

## Lição
- Vale a 1ª edição, nos dois exemplares do Internet Archive (Boston e Toronto). O esqueleto das palavras é o texto
  moderno do Wikisource (o mesmo do Domínio Público), corrigido pela 1ª edição: 27 lições (`decisoes.json`,
  `palavras` e `linhas`), todas conferidas nas imagens, e três linhas de nota que ele metia entre os versos.
- Pontuação de 1769, inclusive a vírgula antes de «e» e o vocativo sem vírgula. Voto das quatro leituras OCR; o
  Tesseract acha as vírgulas que a camada OCR dos PDFs perde, mas lê às vezes o ponto final como vírgula: onde as
  leituras discordam, ou onde o ponto final diverge do texto moderno, decidiu a imagem (`pontuacao_conferida.json`).
- Maiúsculas: as do texto moderno (gentílicos e nomes comuns em minúscula), salvo onde a 1ª edição pede outra
  coisa (depois de ponto e vírgula ou de exclamação no meio do verso).
- Nenhum erro de impressão nos versos. Nas notas, um ponto que falta (lista na «Sobre»).

## Grafia
- Muda a maneira de escrever (ſ, y, ph, letras dobradas, acentos, he → é, hum → um, pretérito em -ão → -am).
- Formas antigas: ficam só as que mudam o número de sílabas do decassílabo (inda, mui, exprimentada, galopear,
  até li, co'o/co'a/co'os/co'as); as outras passam à forma de hoje (coisa, dois, coberto, flecha, artilharia,
  cavalaria, infantaria, felizes, valoroso, várzeas, selvagens, surpreender). Pedido do pedido de 2026-11-23;
  é diferente d'Os Lusíadas (decisão em `revisao.json`).
- Nomes na forma do autor (Cepé, Gerardo, Catâneo, Baldetta, Kobbé → Cobé só na grafia), com a grafia de hoje
  (Lindoia, Troia, Madri). Cepé × Sepé e Cobé × Kobbé em `revisao.json`.
- Notas: `notas1769.txt` é a transcrição diplomática (s por ſ), feita das imagens dos dois exemplares; `notas.py`
  passa à grafia de hoje com o léxico de `edicoes/sao-bernardo/grafia1990.py` e o que ele não resolve em
  `notas_manual.json`. Latim, francês e referências ficam como no impresso. Gentílicos e meses em minúscula.

## Formato no site
- Partes: «Dedicatória» (dedicatória da folha de rosto, epígrafes de Virgílio, soneto ao Conde de Oeiras), os cinco
  cantos e «Ao Autor» (os dois sonetos de Seixas Brandão e Alvarenga Peixoto, que fecham o livro de 1769).
- Os versos de cada canto num bloco só (1769 não separa parágrafos); o número do verso à margem de 10 em 10 pela
  marca `{e N}` do gerador (o título do número diz «estrofe»: ver FALTA.md).
- As notas do autor, de rodapé em 1769, no fim de cada canto («¤ »), com o lema em itálico, como no impresso.
