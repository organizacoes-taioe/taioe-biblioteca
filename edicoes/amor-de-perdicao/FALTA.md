# Amor de Perdição: o que falta (2026-11-02, 15:30)

Pronto e conferido pelas ferramentas: o texto da 1ª edição (1862) na grafia brasileira, com
dedicatória, prefácio, capítulos I–XX e conclusão; as 6 notas do autor no fim dos capítulos;
«Sobre esta edição»; o vocabulário (`edicoes/vocabulario/amor-de-perdicao.json`, 50 palavras,
`conferir` dá ok). `gerar.mjs` e `conferir.mjs` rodam sem erro.

## Conferido no fac-símile de 1862 (Commons, `Amor de Perdição (1862).pdf`, 272 pp.)
- As 23 emendas `ocr` de `decisoes.py`, uma a uma nas imagens: todas confirmadas (a 1ª edição traz a
  forma correta). «pergutou» é erro da transcrição, não da edição.
- Lições estranhas que a 1ª edição imprime de fato, e que ficam: «sasões» (p. 41; grafia de hoje
  sazões), «promenores» (p. 147), «meus dezoitos annos» (p. 247; a mesma carta diz «dezoito» na
  p. 243: erro provável, mantido), «estorturoso», «rentando», «su villão», «coração sinil», «groseta».
- `sitios.tsv` (105): nos pontos de palavra valeu a leitura do Gutenberg, e o Wikisource só
  difere por OCR partido («Mis eraveis», «Vallon go», «elos», «E'» = É, como imprime 1862). Os
  outros são `v. s.ª` (escrito igual nos dois) e os cabeçalhos dos capítulos: nada a mudar.

## Falta
- O PDF do Commons tem camada de texto (OCR próprio, que difere do Gutenberg em vários pontos):
  pode entrar como terceiro testemunho (`pdftotext`, partido pelos cabeçalhos e com
  `ocr.paragrafos_como`), o que acharia os erros do Gutenberg que formam palavra existente e que
  nenhum relatório marca hoje. Até lá, ler `modernas.tsv` (1034 linhas, quase todas revisões da 5ª).
- A BVEB (referência de grafia) é OCR: já se corrigiram leituras dela que passavam ao texto (hífens
  perdidos, «locura», «Cas'telo», «d'a», «Vila-Real»); falta uma leitura corrida do `texto.txt`.
- Edição-base: a regra da Biblioteca prefere a última revista pelo autor (5ª, 1879, com o prefácio
  da 5ª), que só existe em imagem no Wikisource. O Gere decide 1862 × 1879; para 1879, passar as
  imagens no Tesseract (como em São Bernardo) e usar a BVEB, que é da 5ª, como segundo testemunho.
