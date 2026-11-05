# Pau Brasil (Oswald de Andrade, 1925): estado

## Feito (2026-11-05), pronto para publicar
- Obra `pau-brasil` (Literatura, autor novo `oswald-de-andrade`, 1890–1954), livro de poemas como obra própria
  (não há poemas de Oswald no corpus do Versificador, então nada muda em `ferramentas/poesia.py`).
  `python3 edicoes/pau-brasil/montar.py` grava `conteudo/oswald-de-andrade/pau-brasil.js`: 122 partes (prefácio de
  Paulo Prado, dedicatória, Escapulário, Falação; «História do Brasil» com um cronista por página; as outras
  seções, um poema por página; «Secretário dos amantes» numa página só), ~134 poemas, 1.217 linhas de verso,
  6.829 palavras. Desenhos de Tarsila: fora (protegidos).
- Fonte: `original/pau-brasil-1925.txt`, o texto de 1925 na grafia do livro, do Gutenberg 79326 (DP, exemplar da
  HathiTrust), confrontado palavra por palavra com o Wikisource (exemplar da BBM 7829) e com dois OCRs das imagens
  da BBM (camada do PDF e Tesseract); ~40 pontos conferidos no fac-símile. O Gutenberg tinha trocado 5 lições
  (rosa/resa, modos/modas, Perdôa/Peredôa, do/de Paraty, um/un), restabelecidas.
- Grafia: `tabela.py` → `grafia.tsv` (758 trocas, revisada; MANUAL e MANTER no topo do tabela.py); no
  `montar.py`, CORRECOES (24 erros de composição, listados na «Sobre»), FRASES (compostos) e LINHAS (tem/têm).
- `edicao.json` («Sobre»), `revisao.json` (7 decisões, todas com a recomendação aplicada; nenhuma muda o texto),
  vocabulário `edicoes/vocabulario/pau-brasil.json` (70 palavras, `conferir` ok).

## Ao publicar (o principal)
- Catálogo `obras.sql` (obra nova); `_redirects`: nada (obra nova, sem endereço antigo). Tirar dos pedidos.
- Notas gerais: o livro entra na fila dos lotes (`edicoes/notas/`).

## Dúvidas que ficaram
- «Mivam» (Levante), «babeis de borracha» (Falação), «Temperatura de bolina» (Capital da República), «O fera»:
  mantidos como impressos, sem nota no vocabulário (sentido incerto).
