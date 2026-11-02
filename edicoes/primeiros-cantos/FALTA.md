# Primeiros Cantos: o que falta (2026-11-02)

Pronto: a obra `primeiros-cantos` (conteudo/goncalves-dias/primeiros-cantos.js, gerado por `montar.py`
desta pasta): prólogo, os 44 poemas da 1ª edição na ordem do livro e a «Deprecação» (1860) em
apêndice; «Sobre esta edição» (`sobre.md`); vocabulário (`edicoes/vocabulario/primeiros-cantos.json`,
215 palavras, `conferir` ok). Os 45 poemas saíram dos avulsos do autor (`OBRAS_PROPRIAS` em
`ferramentas/poesia.py`; `conteudo/poesia.js` e `conteudo/goncalves-dias/poesia.js` regenerados) e
do `goncalves-dias-poesia.json` (730 palavras, `conferir` ok).

Ao publicar (o principal):
- acrescentar ao `public/_redirects` as linhas de `redirects.txt` (os 45 endereços antigos
  `/biblioteca/goncalves-dias/primeiros-cantos-<poema>/` levam ao poema na obra);
- Catálogo `obras.sql` no teste e na produção: as 45 obras antigas saem e entra a nova (a posição de
  leitura de quem lia um poema avulso se perde);
- Cards (`taioe-cards`): o texto `goncalves-dias/primeiros-cantos-cancao-do-exilio` aponta para o
  endereço antigo (`data/textos-pt.json` e `fonte/textos/pt/…`, campo `biblioteca`); trocar por
  `/biblioteca/goncalves-dias/primeiros-cantos/cancao-do-exilio/`, ou o botão «Aprender as palavras
  deste poema» some da Canção do Exílio.

Falta:
- as notas do autor: «Notas às Poesias Americanas» (livro p. 30–34; Wikisource, Página:Primeiros
  cantos- poesias.pdf/34 a 37, revisadas) e a «Nota» do fim (p. 257–259, sem transcrição no
  Wikisource; o corpus do Versificador guarda as notas de rodapé no campo `nota`). Entrariam como
  «¤ » no fim de cada poema ou como parte própria depois de «O Morro do Alecrim»;
- o confronto com a edição de Leipzig (_Cantos_, 1860) rodou palavra por palavra, mas as diferenças
  (quase todas grafia, OCR ou revisão do autor) não foram revistas uma a uma; o Wikisource só
  cobre umas 40 páginas da 1ª edição, e ali só houve diferença de grafia;
- as três partes do livro (Poesias Americanas, Poesias Diversas, Hinos) estão em `secao` de cada
  parte, mas o gerador ainda não as mostra.
