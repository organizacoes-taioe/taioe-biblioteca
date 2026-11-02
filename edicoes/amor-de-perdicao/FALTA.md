# Amor de Perdição: o que falta (2026-11-02)

Pronto e conferido pelas ferramentas: texto da 1ª edição (1862) na grafia brasileira, dedicatória,
prefácio, capítulos I–XX, conclusão, as 6 notas do autor no fim dos capítulos, «Sobre esta edição»,
vocabulário (`edicoes/vocabulario/amor-de-perdicao.json`, 50 palavras, `conferir` ok),
`gerar.mjs` e `conferir.mjs` sem erro.

Falta:
- Conferir no fac-símile de 1862 (Commons, `Amor de Perdição (1862).pdf`) as 22 emendas `ocr` de
  `decisoes.py` (vieram do relatório `sem_par.tsv`, sem olhar as imagens) e os 105 pontos de
  `ferramentas/cache/amor-de-perdicao/relatorios/sitios.tsv` (quase todos `v. s.ª` e cabeçalhos;
  os de palavra estão no fim do arquivo).
- O Wikisource de 1862 copiou o Gutenberg (só 105 divergências): os erros de OCR que os dois
  partilham e que formam palavra real não aparecem em `sem_par`. Ler `modernas.tsv` (1034 linhas, a
  maioria é revisão da 5ª edição) atrás deles.
- A BVEB (referência de grafia) é OCR: já se acharam e corrigiram leituras dela que passavam ao texto
  (hífens perdidos, «locura», «Cas'telo», «d'a»); vale uma leitura corrida do `texto.txt`.
- Edição revista (5ª, 1879, com o prefácio da 5ª): só em imagem no Wikisource. Se um dia for
  transcrita (ou passada no Tesseract), dá para fazê-la base, como pede o guia.
