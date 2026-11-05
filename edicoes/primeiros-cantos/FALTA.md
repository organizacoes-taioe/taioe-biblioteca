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

Feito depois (rodada de 02/11, à tarde):
- **notas do autor** no fim de cada poema, como «¤ » (o site as mostra em «Notas do autor»):
  `notas.json`, na grafia de hoje, lido pelo `montar.py`. As 13 «Notas às Poesias Americanas»
  (Wikisource, páginas 34 a 36 do PDF, revisadas), agrupadas por poema conforme as chamadas no texto
  (Guerreiro 1–5, Piaga 6–11, Índio 12, Morro do Alecrim 13), e as de rodapé (Canção do Exílio,
  Visões 3, À Tarde). Fica de fora a «Nota» do fim (p. 257–259: trechos do «Hino à Tarde» de
  Frederico José Corrêa, outro autor);
- **diferenças com 1860**: `diferencas-1860.txt`, 310 diferenças de palavra (sem as de grafia),
  poema por poema. Quase todas são revisões do autor para Leipzig; nos poemas 2 a 6 o Wikisource
  (1ª ed. revisada) confirma o nosso texto.

Falta:
- conferir no fac-símile de 1846 (Commons, `File:Primeiros_cantos-_poesias.pdf`) os casos de
  `diferencas-1860.txt` dos poemas 7 em diante em que o nosso texto pareça errado (métrica, sentido);
  e achar os três poemas sem âncora (O Soldado Espanhol, Lágrimas sem Dor, Miserrimus);
- pontos das notas a confirmar no fac-símile (mantidos como o Wikisource os dá): «Rolonx Baro»
  (o viajante é conhecido como Roulox Baro), «cabaça ervada», «Hans Stade» (o Wikisource lê «Haus
  Stade»), «Orosmane e Arimane»; e «Figli» posto como «figle» (o instrumento). Corrigidos como
  erro de composição: «lle» e «he» → lhe, «tenivel» → terrível, «calanidade» → calamidade,
  «es Tupis» → os tupis, «eutre» → entre;
- as três partes do livro (Poesias Americanas, Poesias Diversas, Hinos) estão em `secao` de cada
  parte, mas o gerador ainda não as mostra.
