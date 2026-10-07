# Notas do tradutor: Quinta parte

Arquivo: `traducao/05-quinta-parte.txt`. Texto-base: `original/05-quinta-parte.txt` (Boulenger, 1909, texto de 1619, via Wikisource).
Texto de conferência: Annecy, t. III (1893), no OCR de `ferramentas/cache/filoteia/annecy3.txt`, lido parágrafo a parágrafo (Quinta parte inteira, cap. I a XVIII).

## O que foi conferido

- **Parágrafos.** 99 blocos no francês e 99 na tradução, sem contar o cabeçalho: 18 títulos `## ` e 81 parágrafos (o sumário em itálico, os parágrafos do texto e o dístico final). Mesma ordem; cada bloco é do mesmo tipo do original (título, sumário em itálico, verso).
- **Títulos.** Os 18 títulos traduzidos, «## Capítulo I — ...» a «## Capítulo XVIII — ...».
- **Marcas.** As 18 marcas, de `[V.1]` a `[V.18]`, iguais e na mesma ordem, no começo do primeiro parágrafo de cada capítulo.
- **Numeração do autor.** Os «1.», «2.»... dos pontos ficaram nos mesmos parágrafos (ver Emendas e Dúvidas sobre os números que faltam em Boulenger).
- **Chamadas e notas.** O arquivo não tem `[n]` nem `¤`, como diz o LEIAME.
- **Cabeçalho.** Só `# titulo: Quinta parte da Introdução`.
- **Pontuação.** «!» igual (43 e 43). As diferenças de «?», «;», «:» e «« »» são todas deliberadas: as emendas listadas abaixo e uns poucos «:» postos onde o português pede (V.1 «têm isto de próprio:», V.2 «Mas dizei em verdade:», V.11 «têm isto de admirável:», V.13 «Vedes, minha Filoteia:», V.18 «assim vos direi eu também:»).
- **Tamanho.** Cada parágrafo traduzido tem entre 75% e 131% do tamanho do original. Os abaixo de 85% são perguntas curtas em que o francês gasta mais palavras («Êtes-vous point prompte...» → «Não sois pronta...»); nada foi omitido. O de 131% é «Offrez-lui votre cœur...» (uma linha).
- **Mesóclise.** O `grep` do CONVENCOES e a varredura em Python com `(?![A-Za-zÀ-ÿ])` não acharam nada.
- **Versos.** O dístico de V.18, pelo método do Versificador (ver abaixo).

## Decisões gerais

- **Tratamento.**
  - Filoteia por **vós** do começo ao fim, com as concordâncias no feminino («retirada», «bem acordada», «desgostosa», «inclinada», «pronta», «prostrada», «vos renove toda»).
  - Deus e Jesus por **vós** nos colóquios (V.2, V.13, V.15, V.18).
  - A alma: em V.10, «O ma belle âme, devez-vous dire, vous pouvez...» ficou **vós**; logo depois, «O mon âme, tu es capable de Dieu» ficou **tu**. Segui o original passagem por passagem.
  - Os apóstrofes a coisas vão por **vós**, como no francês: a vida devota (V.11), a resolução (V.13), as resoluções (V.15), o mundo (V.16, «ó mundo, vós sois sempre vós mesmo»).
  - Agostinho fala à Beleza por **tu** (V.2); Deus fala pelo Profeta por **tu** (V.14); a mãe de Sinforiano fala ao filho por **tu** (V.18).
- **Minúsculas depois de «?» e «!».** O francês continua a frase em minúscula depois de uma pergunta ou exclamação interna («arriver ? et cette résolution», «rien sans doute»). Mantive, como o «ai!» e o «ah!» em meio de frase.
- **Maiúsculas.** As de reverência ficaram (*Salvador*, *divina Majestade*, *divina Bondade*, *Cruz*, *Paixão*, *Princípio*, *Aquele*). *Sainte Vierge* → «santa Virgem»; *Sainte Catherine de Gênes* → «santa Catarina de Gênova»; *Saint-Augustin* (V.12, com hífen) → «santo Agostinho». *Partie* com maiúscula, como no Prefácio («segunda Parte», «primeira Parte»). *Ange*, *Patron* (V.8) ficaram em minúscula: hábito tipográfico.
- **Afeições × afetos.** *Affection(s)* tem dois sentidos aqui. Quando são as inclinações do coração (V.1 «ses bonnes affections», V.1 «affections et passions», V.4 «restreindre ses affections», V.7 título e fim, V.18 «d'une spéciale affection»), ficou **afeições**. Quando são os atos da meditação, no sentido do guia (V.2 fim, V.3 «la fin qui comprend les affections», V.8 título e texto, V.9, V.15 título e texto), ficou **afetos**.
- **«VIVE JÉSUS»** em versalete no livro: ficou «VIVA JESUS», como no Prefácio.

## Termos

| francês | tradução | observação |
|---|---|---|
| *bons propos* | bons propósitos | |
| *protestation* | protestação | como no arquivo 00 |
| *avis* | avisos | como no arquivo 00 |
| *entreprise* | empresa | V.12, V.18; como no arquivo 00 |
| *loisir* | vagar | V.17; como no arquivo 00 |
| *peine* (de la vie dévote) | canseira | V.18; como no arquivo 00 |
| *avancement*, *s'avancer* | progresso, progredir | «adiantamento» seria mais antigo; *avancé* → «avançastes» (V.8) |
| *détraquement*, *détraqué* | desarranjo, desarranjou-se | o termo vem do relógio de V.1 |
| *déportement* | procedimento | V.3 |
| *accoiser* | aquietar | V.2, V.10 |
| *amorcer* | ir atraindo | V.2 «Comme vous alla-t-il amorçant»; ver Passagens |
| *remonter ou bander* (horloge) | dar corda ou armar a mola | V.1 |
| *mouvants* | peças móveis | V.1 |
| *démontement* | desmonte | V.1 |
| *conversations* | conversações | o trato social, como «retiro das conversações» |
| *amusements*, *s'amuser à* | entretenimentos, entreter-se com | V.10; no sentido antigo de ocupação que detém |
| *bluette* | fagulha | V.5, «fagulha ou centelha de fogo» |
| *souève* | suave | V.11 (forma antiga de *suave*) |
| *recrue* | exausta | V.11 |
| *nonpareil* | sem igual | V.11, V.17 |
| *chagrin* | despeito | V.11, ao lado da ira |
| *veillées* | serões | V.5 |
| *ressentiments* | sentimentos | título de V.16: os sentimentos duradouros, não o rancor |
| *chérir* | prezar | V.13 («prezar e nutrir a vossa resolução») |
| *dessein* | desígnio | V.15 |
| *semonces* | solicitações | V.18 |
| *infirmité* | fraqueza | V.18 |
| *conducteur* | condutor | V.9, V.17, como no guia |
| *Digestes et Code* | Digesto e Código | V.17 |
| *vêpres et complies* | vésperas e completas | V.17 |
| *prendre la discipline* | tomar a disciplina | V.17 |

**Nomes:** são Gregório, bispo de Nazianzo (V.1) e são Gregório Nazianzeno (V.18), como o autor varia; são José; são Luís; santo Agostinho; são Francisco; Davi; Jeremias; são Paulo; Noé; Esaú e Jacó (plurais «uns Esaús», «Jacós»); a Samaritana; a Madre Teresa (Teresa de Ávila, ainda não canonizada em 1619); santa Catarina de Gênova; santa Mônica; são Jerônimo e Paula; Josué; Sinforiano.

## Passagens difíceis

- **V.1, *remonter en Dieu*.** O autor continua a imagem do relógio: «deve dar-lhe corda em Deus à noite e de manhã». Guardei o «dar corda», que é a imagem, em vez de «elevar».
- **V.2, 2, *mon cœur a projeté cette bonne parole*.** É o *eructavit cor meum verbum bonum* (Sl 44). «Concebeu» guarda o sentido de *projeter* no século XVII (conceber, formar); o mesmo verbo volta em V.14, onde ficou «vos concebia» e «projetou».
- **V.2, 3, *On fit une joie particulière*.** «Houve por isso uma festa particular»: *faire une joie* é festejar. *On en fera la commémoration* → «se fará memória dela».
- **V.2, 4, *Comme vous alla-t-il amorçant*.** *Amorcer* é pôr isca. «Engodar» seria exato mas soa a engano em português; ficou «Como vos foi ele atraindo com o seu açúcar divino», e a isca fica sugerida pelo açúcar. Perda pequena.
- **V.2, 6, *a fait vertu*.** É o *fecit virtutem* do Sl 117: «fez proezas».
- **V.4, 2, *qui a le goût en bom état ..., il aime*.** O pronome pleonástico do francês ficou como «esse ama».
- **V.4, 5, *se fait-il point faire place*.** «Não se faz dar lugar»: a lembrança de Deus abre espaço para si no meio das ocupações.
- **V.4, 5, *elles perdent presque contenance à tout le reste*.** «Quase perdem o tino para todo o resto»: ficam como alheias a tudo o mais. *Violente considération* → «consideração imperiosa».
- **V.5, 4, *surestimer aux autres*.** «Estimar-se acima dos outros».
- **V.7, *quels nous avons été*.** «O que fomos e como nos portamos».
- **V.7, *on craint trop l'un, et trop peu l'autre*.** Ficou literal («teme-se demais um, e pouco demais o outro»), com a mesma ambiguidade do francês sobre qual dos dois.
- **V.7, o tocador de alaúde.** O anacoluto «celles qu'il trouve dissonantes il les accorde» ficou: «as que encontra dissonantes ele as afina». *Tâter* → «provar» (pôr à prova, como quem experimenta cada corda); «tatear» soaria a apalpar no escuro.
- **V.8, *des grâces exercées en votre endroit, pour vous retirer de vos inclinations à ce petit amendement*.** «Pelas graças exercidas para convosco, para vos retirar das vossas inclinações até esta pequena emenda»: o *à* marca o termo do movimento.
- **V.10, *non plus que la colombe*.** «Assim como a pomba saída da arca de Noé», que também não achou onde pousar.
- **V.10, *enflez-lui le courage*.** «Inflai-lhe o ânimo», guardando a imagem.
- **V.12, *plutôt que de renoncer*.** «Em vez de renunciar», «em vez de deixar»: «antes de» seria lido como tempo.
- **V.12, *variétés d'accidents*.** «Variedades de contratempos»: *accident* é o revés.
- **V.13, *faites-moi la grâce que je meure plutôt que de les perdre*.** «Concedei-me a graça de que eu antes morra do que as perca».
- **V.13, *Voyez-vous*.** «Vedes, minha Filoteia:», com dois-pontos, que é o que o português pede depois do «vedes» de chamada.
- **V.14, *à vous faire faire vos résolutions*.** «Em vos levar a fazer as vossas resoluções».
- **V.14, *Non pas certes si tout le monde devait périr*.** «Não, decerto, nem que o mundo inteiro devesse perecer».
- **V.16, *je n'ai plus de moi ni de mien: mon moi, c'est Jésus; mon mien, c'est d'être sienne*.** O jogo passa inteiro: «já não tenho eu nem meu: o meu eu é Jesus; o meu meu é ser sua». O «meu meu» é estranho de propósito, como o *mon mien* do francês.
- **V.16, *nous nous trouverons des Jacob*.** «E nós nos acharemos feitos Jacós»: o mundo, como Isaac, pensa ter diante de si Esaú, e é Jacó.
- **V.16, *tout bellement*.** «Muito mansamente».
- **V.17, *qu'il ne fît et n'exécutât diligemment*.** «Não perdia uma só ocasião de bem público exterior sem a realizar e executar diligentemente».
- **V.18, *nous oblige de réputation à la poursuite*.** «Nos obriga, pela reputação, a prosseguir».
- **V.18, *Les philosophes se publiaient pour philosophes*.** «Os filósofos se apregoavam filósofos».
- **Citações.** Todas traduzidas do francês do autor, sem acrescentar referência: Sl 26/44/118 (V.2, 2), Agostinho, *Confissões* X (V.2, 5), Sl 70 (V.2, 5), Sl 117 (V.2, 6), Sl 76 (V.4, 5), Sl 25 (V.4, 9, sem aspas no original), Agostinho, *Solilóquios*, e o «Quem sois vós e quem sou eu?» de são Francisco (V.3), Jo 4 (V.11, com o latim em itálico: «_Domine, da mihi hanc aquam_: Senhor, dai-me dessa água»), Jr 1 e Jr 31 (V.13, V.14), Gl 2 (V.13), Sl 118 (V.18, «justificações», o termo da Vulgata), o dito atribuído a Gregório Nazianzeno e as palavras da mãe de Sinforiano (V.18).

## O dístico de V.18

| «A cause des biens que j'attends,
| Les travaux me sont passe-temps».

- **Original.** Dois octossílabos franceses, rima masculina emparelhada (*attends / temps*). Molde do original: `8: 2-5-8` e `8: 3-(6)-8`. É a versão francesa do dito de são Francisco nos *Fioretti* («Tanto è il bene ch'io aspetto, ch'ogni pena m'è diletto»).
- **Metro de chegada.** Octossílabo português (a conta francesa é igual à portuguesa, diz o manual), com a 4.ª acentuada (§ 5, regra 11). O 2-5-8 do primeiro verso francês não tem tradição em português (regra 2), por isso o molde é `8: 4-8` nos dois. Rima masculina → rima aguda, emparelhada.
- **Tradução:**

  | «Graças aos bens que espero ter,
  | os meus trabalhos são prazer».

- **molde.mjs:** 2 versos, 2 exatos (✓), nenhum ~, nenhum ✗, nenhum ≠.
  - v. 1: 1-4-6-8 (corpus 7,11%, #5); sinalefa *que‿es*;
  - v. 2: 4-6-8, fraco na 2.ª (corpus 5,25%, #6).
  - Os dois versos têm desenhos diferentes.
- **Perdas.** *À cause de* virou «graças a», que guarda a causa e acrescenta um matiz de agradecimento. *Passe-temps* virou «prazer»: «passatempo» não dá rima aguda nem cabe nas 8 sílabas com o resto; «prazer» é também o *diletto* do original italiano. O «meus» corresponde ao *me* de *me sont*.
- **Pontuação.** Boulenger tem ponto no fim do primeiro verso («j'attends.»); Annecy tem vírgula. Segui Annecy.
- Arquivos de trabalho (temporários): `C:\Users\geren\AppData\Local\Temp\claude\introducao-a-vida-devota-05\` (`trad.txt`, `molde.txt`, `molde-original.txt`).

## Emendas pela edição de Annecy

Erros evidentes de Boulenger (no Wikisource), corrigidos na tradução segundo Annecy:

1. **V.2, 2, «mon cœur Ta dit»** → Annecy «l'a dit»: «o meu coração o disse».
2. **V.2, 5, «des années précédentes. Dieu vous ait appelée»** → Annecy tem ponto também, mas a frase continua («quelle grâce qu'après avoir ... Dieu vous ait appelée»); traduzi como frase única, com vírgula.
3. **V.2, 6, aspas de David sem fecho** («« La bonne main de Dieu ... les merveilles de sa bonté.») → fechei depois de «bondade», onde termina o itálico da citação em Annecy.
4. **V.3, «Invoquez le Saint-Esprit, qui demandant lumière»** → Annecy «luy demandant»: «pedindo-lhe luz e claridade».
5. **V.4, 3, «à l'endroit des péchés véniels, On ne saurait»** → Annecy «venielz?»: ponto de interrogação.
6. **V.4, 4, «4,»** → «4.».
7. **V.4, 5, «Ah ! dit David, je me suis ressouvenu de Dieu et m'en suis délecté ».** Falta a aspa de abertura; Annecy dá a citação em itálico desde «je me suis». Abri a aspa antes de «Ah!», como em V.2, 2 («« Ah ! Seigneur, disait David...»).
8. **V.5, 5, «en parlant ; de vous»** → Annecy «en parlant de vous»: sem o ponto e vírgula.
9. **V.7, «l'avancement spirituel qu'on i fait»** → Annecy «qu'on a fait»: «que se fez».
10. **V.7, «cela est pour es confessions»** → Annecy «pour les confessions».
11. **V.18, «regardez, le ciel»** → Annecy «regardes le Ciel»: sem vírgula.
12. **V.18, «j'attends.»** → vírgula (ver o dístico).

Erros só de digitação, sem efeito na tradução: «d avoir» (V.2, 6), «d en» (V.14), «résolu- tions» e «0 résolution» (V.13), «dé- lices» (V.15), «occurences» (V.13).

Diferenças de Annecy sem efeito, ou que não segui:

- **Divisão de parágrafos.** Annecy junta em V.1 o 2.º e o 3.º parágrafos e em V.15 os três primeiros e o 4.º e o 5.º; divide V.3 e V.7 em outro lugar. Segui Boulenger, como manda o formato.
- **V.3, «que tout se fasse»** (Boulenger) × «que le tout se face» (Annecy): mesmo sentido.
- **V.13, «et entre autres nos résolutions»**: Annecy também tem «nos» (e não «vos»); ficou «as nossas resoluções».
- **V.14, «je t'ai attirée»** (Boulenger) × «attiré» (Annecy): sem efeito no português («te atraí»).
- **V.18, «La mère de Symphorien»** (Boulenger) × «La mère de saint Simphorien» (Annecy). Segui Boulenger: «A mãe de Sinforiano». Ver Dúvidas.

## Remissões de página

Não há. As remissões internas são à «segunda Parte» (V.1, o método da meditação), à «primeira Parte» (V.9, V.18) e ao «segundo ponto» (V.2, V.15), traduzidas como estão.

## Dúvidas para quem coordena

1. **Números que faltam em Boulenger.** Annecy numera três pontos que Boulenger (no Wikisource) deixa sem número:
   - V.2: «6. Considérez les effets de cette vocation»;
   - V.4: «10. Sauriez-vous remarquer...»;
   - V.5: «6. Quant aux œuvres...».

   Deixei sem número, como no texto-base, porque não sei se a falta é do impresso de Boulenger ou da transcrição. Como a numeração é do autor e as três séries ficam truncadas (1–5 sem o 6; 1–9 sem o 10; 1–5 sem o 6), **proponho acrescentar «6.», «10.» e «6.»**, seguindo Annecy. São três inserções no começo de parágrafo, sem outro efeito.
2. **«São Sinforiano».** Annecy tem «saint Simphorien»; Boulenger, só «Symphorien». Segui Boulenger. Se a casa preferir Annecy, troca-se por «A mãe de são Sinforiano».
3. **Afeições × afetos.** Ver Decisões gerais. Convém fixar no guia a distinção (*affections* da meditação → afetos; *affections* do coração → afeições), porque a Segunda e a Terceira Partes usam muito as duas.
4. **«Progresso» por *avancement*.** Escolhi «progresso», mais natural hoje, em vez do antigo «adiantamento» ou «aproveitamento». Se outra parte já usou «adiantamento», convém uniformizar.
5. **O dístico.** «Graças aos bens que espero ter, / os meus trabalhos são prazer». Se se quiser «por causa» literal, a alternativa que passa no molde é «Por tantos bens que espero ter» (2-4-6-8), que acrescenta «tantos» (eco do *tanto è il bene* italiano).
