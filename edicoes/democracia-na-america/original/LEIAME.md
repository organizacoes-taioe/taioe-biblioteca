# A democracia na América (seleção): texto francês

Base: Alexis de Tocqueville, *De la démocratie en Amérique*, «douzième édition, revue, corrigée et
augmentée d'un Avertissement et d'un Examen comparatif de la démocratie aux États-Unis et en Suisse»,
Paris, Pagnerre, 1848, 4 tomos (t. I–II = a 1ª parte, de 1835; t. III–IV = a 2ª parte, de 1840). É a
última edição revista pelo autor: a 13ª (1850) a reimprime, e as *Œuvres complètes* (Michel Lévy,
1864–66) saíram depois da morte dele, preparadas por Gustave de Beaumont. Tocqueville (†1859) está em
domínio público em toda parte.

Testemunhos (baixados em 2026-11-12):
- **GUT**: a transcrição do Project Gutenberg (ebooks 30513–30516), feita pelos revisores do
  Distributed Proofreaders sobre as imagens da BnF/Gallica dessa mesma edição. É o texto de base.
- **WS48**: a transcrição do Wikisource em francês, «Édition 1848» (sobre os djvu do Commons
  `Alexis de Tocqueville - De la démocratie en Amérique, Pagnerre, 1848, tome N.djvu`), marcada como
  validada, mas que traz muitas lições de outra edição (singular e plural trocados, palavras a mais ou
  a menos) e moderniza parte da grafia.
- **WS66**: o Wikisource, «Édition 1866» (*Œuvres complètes*, t. 1–3), só para achar divergências.
- **FAC**: as imagens da edição de 1848 no Commons, para decidir.

## Como foi montado

Os capítulos escolhidos foram extraídos do GUT (`extrair_gut.py`, fora do git) e comparados palavra
por palavra com o WS48 e, este, com o WS66. Toda divergência de palavra dentro da seleção (91 pontos,
`conferencia.tsv`) foi vista no FAC. O WS48 errou em 48 deles; o GUT só em 5, corrigidos pela imagem:
- Introdução: «Le clergé ouvre ses rangs» (GUT «ces»);
- I,2, notas: «History of Virginia from the earliest period» (GUT «front»), «Pitkin's History, p. 35,
  t. I» (GUT «t. 1»), «Dès 1641» (GUT «1645»);
- I,2,9: «leur empire sur les mœurs» (GUT «amours»).
Lições do impresso mantidas, mesmo estranhas (o FAC as confirma): «Madisson», «Spinosa»,
«siége de l'État» (as *Œuvres complètes* corrigem para «chef de l'État»; ver `CONVENCOES.md` e a
decisão `siege`), «mais elle plus juste» (II,4,8, sem «est»).

## Apresentação

- Grafia do impresso (1848): «priviléges», «long-temps», «très-grand», «avénement», «dévoûment».
  Só o apóstrofo virou ’. O GUT não traz os espaços antes de «; : ? !», e assim ficou.
- Cada arquivo é um capítulo, sem o «CHAPITRE N.» e o título (que vão no `# titulo:` e no `obra.py`).
  Os títulos de seção, em versalete no impresso, vão em `## ` com só a inicial maiúscula; os
  sumários do autor (no começo do capítulo e das seções), em itálico.
- I,2,9: só a parte dos costumes e da religião (as seções «De l'influence des mœurs…» até «Des
  principales causes qui rendent la religion puissante en Amérique», inclusive), sem as causas
  acidentais, as leis, as luzes e a comparação com a Europa.
- Notas de rodapé do autor: chamada `[n]` e bloco `¤ [n]` no fim do arquivo, renumeradas a partir de 1
  em cada capítulo. As notas finais dos tomos («Notes», por letra ou página) ficam de fora.
