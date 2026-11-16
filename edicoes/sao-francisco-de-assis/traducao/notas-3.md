# São Francisco de Assis — notas do tradutor, capítulo III (Francisco, o combatente)

Parágrafos: 14/14 (o bloco dos quatro versos de Belloc conta como um). Grep de mesóclise sem resultado. A
variante do LEIAME deste capítulo («market place» na p. 43, «market-place» na p. 44) não muda nada na tradução
(«praças de mercado» e «praça do mercado»).

## Os versos de Belloc (§ 3)

Original (Hilaire Belloc, *Courtesy*, última estrofe):

    'Of Courtesy, it is much less
    Than courage of heart or holiness,
    Yet in my walks it seems to me
    That the grace of God is in Courtesy.'

Tradução:

    | ‘A cortesia é bem menor
    | que a santidade e que o valor;
    | mas sinto, andando, dia a dia,
    | graça de Deus na cortesia.’

- **Metro.** O inglês é um tetrâmetro jâmbico solto, com anapestos (8, 9, 8 e 9 sílabas; quatro tempos por
  verso). Pela tabela do manual (tetrâmetro jâmbico → octossílabo 4-8), a tradução vai em **octossílabos** com a
  4.ª e a 8.ª fixas e 1.ª, 2.ª e 6.ª livres (molde `8: (1)-(2)-4-(6)-8`). O eneassílabo foi descartado: com a 3-6-9
  daria só três tempos, e o verso de quatro tempos ternário pede 11 ou 12 sílabas, longo demais para esta estrofe.
- **Rimas.** aabb, como no original: *menor / valor* (aguda, como *less / holiness*) e *dia / cortesia* (grave;
  no inglês, *me / Courtesy*, rima em sílaba fraca). Mantive a moldura: a estrofe abre e fecha com «cortesia»,
  como o inglês com *Courtesy*.
- **Escolhas.** *courage of heart* → «valor» (perde-se *of heart*; «valor» no sentido de bravura); a ordem
  santidade/valor inverte a do inglês, pela rima. *In my walks it seems to me* → «sinto, andando, dia a dia»
  («vejo graça» e «acho graça» foram recusados: são idiotismos de achar engraçado). *That the grace of God is in
  Courtesy* → «graça de Deus na cortesia», objeto de «sinto», sem artigo: «a graça de Deus» não cabe no
  octossílabo (cairia no 2-5-8, que a tradição não usa).
- **Eco na prosa.** O § 4 retoma as palavras dos versos; a tradução segue a estrofe: «tivesse valor, até do tipo
  mais comum, viril e militar» e «a santidade e a graça de Deus».
- **Saída do molde** (`node ferramentas/molde.mjs traducao.txt molde.txt`):

      1 ~ A cortesia é bem menor
          molde 8: (1)-(2)-4-(6)-8 | obtido 8: 4-5-6-8 | corpus: 0.66% (#24)
          A/cor/te/si/a‿é/bem/me/nor  — choque 5
      2 ✓ que a santidade e que o valor;
          molde 8: (1)-(2)-4-(6)-8 | obtido 8: 4-8 | corpus: 10.21% (#3)
      3 ✓ mas sinto, andando, dia a dia,
          molde 8: (1)-(2)-4-(6)-8 | obtido 8: 2-4-6-8 | corpus: 8.79% (#4)
      4 ✓ graça de Deus na cortesia.
          molde 8: (1)-(2)-4-(6)-8 | obtido 8: 1-4-8 | corpus: 13.35% (#2)
      4 versos: 3 exatos, 1 aceitáveis, 0 falhos, 0 fora da medida; forçamento médio 0; custo total 0.85

  Nenhum ✗ nem ≠. O ~ do verso 1 é o «é» de ligação, fundido com o «a» de «cortesia» e lido átono na fala;
  o script o conta forte. Alternativa toda exata no candidato 1.

## Nomes e termos novos

- *"Frenchy"*, *"Francesco" or "The little Frenchman"* → “Francês”, “Francesco”, ou “o Francesinho”;
  *signifying the Frank or Frenchman* → «que significa o franco, ou o francês».
- *Pietro Bernardone* → **Pedro Bernardone** (guia); *Francesco Bernardone* (§ 12, forma italiana no original) →
  Francisco Bernardone, como no resto do livro.
- *the guild of the cloth merchants* → a corporação dos mercadores de tecidos; *booth* → barraca; *the market* →
  a feira; *market place* → praça do mercado.
- *employed people but he was not an employer* → «pode ter empregado gente, mas não era um empregador» — o jogo
  passa.
- *guileless swagger as a Troubadour and leader of French fashions* → «a sua ostentação sem malícia de trovador
  e de lançador das modas francesas»; *ringleader* → cabecilha.
- *"liberal and hilarious"* (eco de Celano, *hilaris et liberalis*) → “liberal e jovial”: *hilarious* tem aqui o
  sentido antigo de alegre, e «hilariante» seria engraçado.
- *largeness, or in the fine medieval phrase largesse* → «largueza... ou, na bela expressão medieval, por
  _largesse_» (o francês fica, em itálico; «largueza» é também o termo da cavalaria em português).
- *_caritas caritatum_* → fica em latim e itálico, sem tradução (guia, § 5).
- *Gauthier de Brienne* → fica na forma francesa do original (as biografias portuguesas dizem «Gualtério»; a
  forma francesa casa com a piada do «nome francês» logo depois). *Apulia* → a Apúlia; *Perugia* → Perúsia
  (guia); *Toulouse*, *Salerno*, *the Midi* → Toulouse, Salerno, o Midi; *Clapham*, *Wimbledon* → ficam.
- *Michael Angelo, Titian, Columbus, Catherine of Siena, Charlemagne* → Michelangelo, Ticiano, Colombo, Catarina de
  Sena, Carlos Magno.
- *tocsin* → «o sino a rebate».
- *the valley of humiliation* (Bunyan) → «o vale da humilhação», em minúscula como no original.
- A voz do sonho (§ 13) fala em **tu** («Entendeste mal o sentido da visão. Volta para a tua cidade»), como as
  falas de Deus na *Ortodoxia* (decisão do Gere).

## Citações

- § 6, *the text that makes angels winds and messengers a flaming fire* (Sl 104,4; Hb 1,7, como ele cita) →
  «o texto que faz dos anjos ventos, e dos mensageiros um fogo ardente».
- § 10, *"He listens to those to whom God himself will not listen."* → “Ele escuta aqueles a quem nem o próprio
  Deus quer escutar.”

## Passagens difíceis

- § 2, *This is a rule that is proved even in the exception* → «É uma regra que a própria exceção confirma» (o
  provérbio português).
- § 2, *put the mendicant more than normally in the wrong ... people who had been put hopelessly in the wrong* →
  «deixasse o mendigo mais em falta do que de costume ... pessoas que tinham ficado irremediavelmente em falta».
- § 2, *politeness* → polidez (cortesia fica para *courtesy*, a palavra de Belloc).
- § 4, *The sweeping simplicity of this undertaking* → «A simplicidade arrebatadora desse compromisso»
  (*undertaking*, promessa; aqui «compromisso» é empenho de palavra, não o *compromise* do cap. X).
- § 4, *one riot of rash vows* → «uma folia de votos temerários».
- § 6, *A certain precipitancy was the very poise of his soul* → «Uma certa precipitação era o próprio
  equilíbrio da sua alma» — o paradoxo passa.
- § 6, *courage actually means running*: a etimologia é de Chesterton (*courage* vem de *cor*, coração, não de
  *currere*); a tradução a mantém como está, sem corrigir: «coragem queira dizer, de fato, correr ... sair
  correndo ... arremeter».
- § 6, *flinging himself round corners* → «virar as esquinas num arranco»; *at every turn* → «a cada volta», que
  casa com as esquinas.
- § 8, *a sort of sentimental sediment* → «uma espécie de sedimento sentimental» — o jogo passa inteiro.
- § 9, *only being asked to die for the things with which they had always lived* → «só lhes pedirem que
  morressem pelas coisas com que sempre tinham vivido».
- § 10, *those whom everybody disliked him for liking* → «daqueles de quem todo mundo não gostava que ele
  gostasse»; *all those things that hold many decent societies together, could never hold this man* → «dão
  coesão ... nunca conseguiram conter»: o jogo do mesmo verbo se perde em parte.
- § 11, *pacifists and prigs* → «os pacifistas e os pedantes» (perdeu-se a aliteração).
- § 11, *the light was blank and the plain was flat* → «a luz era vazia, e a planície, rasa».
- § 14, *drifting, one may even say mooning* → «vagava, pode-se até dizer enquanto andava no mundo da lua».
- § 14, *knowing nothing between stillness and swiftness* → «sem conhecer meio-termo entre a imobilidade e a
  rapidez».

## Candidatos a decisão do Gere

1. **§ 3, Belloc, versos 1–2: *Of Courtesy, it is much less / Than courage of heart or holiness.***
   - (a) **«A cortesia é bem menor / que a santidade e que o valor;»** — recomendada: diz o *much less* e soa
     natural; o único ~ do molde é o «é» átono.
   - (b) «A cortesia, na verdade, / cede ao valor e à santidade;» — exata no molde (✓ ✓) e na ordem do inglês,
     mas «na verdade» é enchimento, perde-se o *much*, e «ceder a» pode ler-se «render-se a».
2. **§ 4, *if there was one thing about which he was punctilious, it was punctiliousness.***
   - (a) **«se havia uma coisa em que ele era cerimonioso, era a cerimônia»** — recomendada: guarda a repetição e
     o campo das boas maneiras, que é o assunto.
   - (b) «... em que ele era escrupuloso, era o escrúpulo» — guarda a repetição, mas puxa para a moral.
   - (c) «... em que ele era meticuloso, era a meticulosidade» — mais literal, palavra pesada.
3. **§ 5, *If he did not paint the town red, he would probably have preferred to paint it all the colours of the
   rainbow.***
   - (a) **«Se não pintava o sete pela cidade, provavelmente teria preferido pintá-la com todas as cores do
     arco-íris»** — recomendada: o idiotismo brasileiro de farra, e o «pintar» segue para o arco-íris.
   - (b) «Se não pintou a cidade de vermelho...» — literal; guarda a cor, mas o idiotismo não existe em português.
