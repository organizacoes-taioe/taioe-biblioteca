# Pau Brasil (Oswald de Andrade, 1925): o que está feito e o que falta

## Fontes (achadas em 2026-11-05)
- Fac-símile da 1ª edição (Paris, Au Sans Pareil, 1925), Brasiliana USP, `bbm/7829`
  (https://digital.bbm.usp.br/handle/bbm/7829; PDF de 128 páginas, com camada de OCR). É o mesmo exemplar
  do Commons «Pau Brasil (Andrade, 1925).pdf» (sem as ilustrações de Tarsila).
- Wikisource, «Pau Brasil» (índice «Pau Brasil (Andrade, 1925).pdf»): transcrição página a página desse
  exemplar, 95 páginas revisadas (nível 3).
- Project Gutenberg 79326 (2026): transcrição do Distributed Proofreaders sobre as imagens da HathiTrust
  (outro exemplar da mesma edição); diz ter corrigido «os erros tipográficos evidentes», sem lista.
- Downloads e rascunhos em `~/.cache/claude-pedidos-0511/pau-brasil/` (só neste PC).

## Feito
- `original/pau-brasil-1925.txt`: o texto de 1925 (grafia do livro), montado do Gutenberg e posto no
  formato desta pasta (ver o topo de `montar.py`, quando existir). Ilustrações de Tarsila: fora (protegidas).

## Falta
- Conferir as ~30 diferenças Gutenberg × Wikisource nas imagens da BBM e procurar as correções caladas do
  Gutenberg (onde as duas transcrições concordam e os OCRs do fac-símile não).
- `montar.py` (grafia de hoje, só acento e letra), `edicao.json` («Sobre»), autor `oswald-de-andrade`,
  linha no `index.html`, `revisao.json`, vocabulário `edicoes/vocabulario/pau-brasil.json`.
