# Notas do tradutor: Terceira parte, capítulos XIV a XXVII

Arquivo: `traducao/03-terceira-parte-b.txt`. Texto-base: `original/03-terceira-parte-b.txt` (Boulenger, 1909, texto de 1619, via Wikisource).
Texto de conferência: Annecy, t. III (1893), no OCR de `ferramentas/cache/filoteia/annecy3.txt` (pp. 184–232 do volume), lido parágrafo a parágrafo, e o léxico do fim do volume para as palavras raras.

## O que foi conferido

- **Parágrafos.** 89 no francês e 89 na tradução, mais os 14 títulos e o cabeçalho, na mesma ordem. Onde Annecy junta dois parágrafos de Boulenger num só (por exemplo, III.14 P5–P6, III.15 P2–P4, III.19 P3–P4), segui a divisão de Boulenger, que é o texto-base.
- **Títulos.** Os 14 títulos `## Chapitre` viraram `## Capítulo XIV` … `## Capítulo XXVII`, com os romanos como estão.
- **Marcas.** As 14 marcas, de `[III.14]` a `[III.27]`, iguais e na mesma ordem, no começo do primeiro parágrafo de cada capítulo. Não há chamadas `[n]` nem notas `¤`.
- **Cabeçalho.** Só `# titulo: Terceira parte da Introdução, capítulos XIV a XXVII`, como manda o CONVENCOES e como em `00-oracao-e-prefacio.txt`.
- **Numeração do autor.** Os «1.», «2.», «3.» de III.17 ficaram.
- **Itálicos.** Os dois do original: _aproxis_ (III.18) e _Penitência_ (III.21, o título da obra de santo Ambrósio).
- **Tamanho.** Cada parágrafo traduzido tem entre 85% e 103% do tamanho do original. O de 85% (III.17, P2, «Nem todo amor é amizade») está inteiro; é o português que sai mais curto.
- **Pontuação.** Mesmo número de «!» e de «?», menos onde corrigi erro de transcrição (ver Emendas: dois «!» parasitas em III.24 e um «?» em III.18).
- **Aspas.** O original tem 55 «» abrindo e 52 fechando: três citações abrem e não fecham (ver Emendas). Na tradução, 48 e 48.
- **Mesóclise.** O `grep` do CONVENCOES e a varredura em Python com `(?![A-Za-zÀ-ÿ])` não acharam nada. Na redação, quatro lugares que pediam mesóclise foram resolvidos de outro modo: *Celui-là te plaira* → «Há de agradar-te aquele» (III.18); *me dira quelqu'un* → «me dirá alguém» (III.18); *je m'habillerais ainsi* → «eu me vestiria assim» (III.15); *on demandera* → «perguntarão» (III.25).
- **Versos.** Não há versos neste arquivo (os dois dísticos da obra estão em III.1 e V.18).

## Decisões gerais

- **Tratamento.**
  - Filoteia por **vós**, sempre, com os adjetivos no feminino («verdadeiramente avarenta», «sois pobre de espírito... e bem-aventurada», «ser descortês e rústica»).
  - **Tu** onde o francês tem *tu*: a mulher a quem fala são Gregório Nazianzeno (III.18); a moça e o rapaz de santo Ambrósio (III.21); a jumenta, o anjo e Balaão (III.23); a carne que fala à alma e o autor que fala à «pobre alma» (III.23); «Pensa em ti mesmo» de são Bernardo (III.24); as citações bíblicas no singular («Meu filho, dá-me o teu coração»; «Põe-me como um selo sobre o teu coração»; «Pelas tuas palavras...»).
  - **Vós** a Deus na citação do salmo de III.21 («Ó Senhor, vós rompestes os meus laços»).
  - «chère amie» de III.23 (a mulher que corre ao cilício quando o marido adoece): «cara amiga», por **vós**, como no francês.
- **Vocativos.** Pela regra do CONVENCOES: *très chère Philothée* → «caríssima Filoteia»; *chère Philothée* → «cara Filoteia»; *ma Philothée* → «minha Filoteia»; *ma chère Philothée* → «minha cara Filoteia».
- **Colocação.** Evitei as contrações e ênclises lusitanas que o francês convida (*Dieu les nous a données*, *il vous le rendra*, *on le vous présente*): «Deus as deu a nós», «Deus vos devolverá tudo», «na mesma ordem em que o apresentam». Nada de «no-las», «vo-lo», «lho».
- **Minúscula depois de «?» e «!»** onde o francês continua a frase em minúscula («Mas por que isso? porque, sem dúvida...»; «que impaciências temos com isso! mas quando...»), como fez a tradução do Prefácio.
- **Citações.** Escritura e Padres traduzidos do francês do autor, sem referência onde ele não a dá: Mt 5,3 (duas vezes, e uma vez como paráfrase em III.15); Ex 3,2; 1 Rs 21 (Acab e Nabot); Os 9,10; 2 Cor 11,29; Jo 13,16; Mt 25,34–36; Gn 27; Sl 132,1.3; Eclo 12,13; Mt 12,36; Rm 1,31; Sl 115,16–17; Jr 15,19; Eclo 6,17; Tg 4,4; Jl 2,12; Pr 23,26; Ct 8,6; Gl 2,20; Lc 10,8; Zc 3,8; Ct 6,9; Nm 22; 2 Sm 12,16; Jl 2,13; Mt 22,39; Rm 12,15; Fl 4,4–5; Mc 6,31; 1 Tm 2,9; 1 Pd 3,3; Mt 12,37; Sl 36,30; Ct 4,11; Tg 3,2; Mt 12,34; Ef 5,3; 1 Cor 15,33. As referências (dadas aqui só para quem revisa) são as da margem de Annecy; nenhuma entrou no texto.
  - Os versículos que viraram fórmula foram traduzidos de modo a ficarem reconhecíveis, mas pelo francês: «Bem-aventurados são os pobres de espírito, porque o reino dos céus é deles»; «Comei o que for posto diante de vós»; «Eu vivo, mas já não eu, antes é Jesus Cristo que vive em mim»; «a hóstia de louvor».
  - Em III.23 o autor repete o versículo de Lc 10,8 com outra forma (*Mangez ce qui vous sera mis devant*); a segunda vez ficou «Comei o que vos for posto à frente», para guardar a pequena diferença.

## Termos

| francês | tradução | onde / observação |
|---|---|---|
| *pauvreté d'esprit*; *pauvres / riches d'esprit* | pobreza de espírito; pobres / ricos de espírito | III.14–16 |
| *pauvreté réelle et effectuelle* | pobreza real e efetiva | III.15 |
| *avare*, *avaricieux*, *avarice* | avarento, avaro, avareza | III.14 |
| *moyens*, *facultés* | bens, haveres | «bens e haveres»; «diminuições de haveres» |
| *s'embesogner*, *embesognée* | afadigar-se; ocupada | III.14, III.15 |
| *empressé*, *empressement* | ansioso, açodado; sofreguidão, ânsia | III.14, III.15, III.18 |
| *fébricitants* | os febris | III.14 |
| *ladres, chancreux* | leprosos, cancerosos | III.15 |
| *bicoque* | casebre | III.15 |
| *chicaneur* | chicaneiro | III.15 |
| *amitié*; *amitié particulière* | amizade; amizade particular | III.17–22 |
| *amourettes* | namoricos | III.18–21; título de III.18: «Dos namoricos» |
| *folâtre*, *folâtrerie* | leviano, leviandade | «amizades levianas», «virtude leviana» |
| *muguetteries* | requebros; faceirices | III.18 (galanteios amorosos) «requebros»; III.25 (cuidado efeminado com o cabelo) «faceirices» |
| *cajoler*, *cajolerie* | galantear, galanteio | III.17, III.18, III.20 |
| *galanterie* | galantaria | III.20 |
| *barguigner* | solicitar | III.20; o léxico de Annecy dá «marchander, solliciter» |
| *pavoner*, *pavonnade* | pavonear-se; fazer a roda e pavonear-se | III.20 |
| *morgue*; *babillerie* | empáfia; tagarelice | III.17 |
| *communication*; *communiquer* | comunicação; comunicar | o termo técnico da teoria da amizade (III.17–22), mantido sempre |
| *commerce* | trato | III.19, III.22 |
| *partialité* / *particularité* | parcialidade / particularidade | III.19; o jogo de palavras passa |
| *religions* (ordens) | ordens religiosas | III.19 («ceux qui sont ès religions») |
| *alliés* | afins | III.19 (parentes por casamento) |
| *jayet* | azeviche | III.19 |
| *frelons*; *taons*; *bourdons* | vespões; moscardos; zangões | III.19, III.24 |
| *aconit* | acônito | III.17, III.20, III.22 |
| *miel d'Héraclée (du Pont)* | mel de Heracleia (do Ponto) | III.17, III.20, III.22 |
| *renardeaux* | raposinhas | III.21 (Ct 2,15) |
| *changeurs et monnayeurs* | cambistas e moedeiros | III.22 |
| *le bas or* | o ouro de baixo quilate | III.22 |
| *apostème* | apostema | III.22 |
| *haire*; *discipline* | cilício; disciplina | III.23 |
| *mater* | domar | III.23 |
| *viandes* | comidas; prato | III.23 («viande» = alimento em geral) |
| *fumeuses, venteuses* | fumosas, ventosas | III.23, termos da medicina antiga |
| *conversation(s)* | conversação, conversações | III.24, III.27; ver Dúvidas |
| *conversation particulière*; *devis*; *entretiens* | conversa particular; conversas; entretenimentos, conversas | III.21, III.26, III.27, III.18 |
| *honnêteté*, *honnête* | honestidade, honesto | no sentido de decoro e pudor; em III.24 («conversations qui ont pour leur fin l'honnêteté», visitas e reuniões de cortesia) ficou «cortesia» |
| *bienséance*; *bienséant* | decoro; decoroso | III.25 |
| *netteté*; *propre* | asseio; asseada | III.25 |
| *se démettre* | renunciar aos adornos | III.25; léxico de Annecy: «renoncer à la parure» |
| *affiquets* | enfeites | III.25 |
| *veuves à marier* | viúvas casadouras | III.25 |
| *attrempé* | temperado | III.25 |
| *afféteries*, *affétés* | afetações, afetados | III.25, III.27 |
| *curiosités* | requintes | III.25 |
| *moqueur*, *moquerie*; *dérision* | zombeteiro, zombaria; escárnio | III.27 |
| *mépris et contemnement* | desprezo e menosprezo | III.27 (o par de sinônimos do autor) |
| *eutrapélie* | eutrapelia | III.27; sem itálico, como no original |
| *gausserie*; *joyeuseté et quolibets* | gracejo; algum gracejo e alguns ditos chistosos | III.27 |
| *avis* | aviso(s) | III.15 «este aviso», título de III.21 e III.22, III.23; como propõe a nota da Oração dedicatória |
| *loisir* | vagar | III.18, III.24; idem |
| *protestation(s)* | protestação, protestações | III.21; idem |
| *directeur*; *guide* | diretor; guia | III.21, III.23 |
| *cuider* | julgar | III.18, III.19, III.20 |

**Nomes:** alcíones; Moisés; Acab, Nabot; Parrásio; são Luís; santa Isabel da Hungria; Esaú, Jacó; santo Aleixo, santa Paula, são Paulino, santa Ângela; Heracleia do Ponto; são Gregório Nazianzeno, são Basílio; o Sábio; são João, Lázaro (o francês diz *le Lazare*), Marta, Madalena; são Pedro, são Marcos, santa Petronila; são Paulo, Timóteo, santa Tecla; santo Agostinho, santo Ambrósio, santa Mônica; são Jerônimo, são Gregório, são Bernardo, santo Tomás; Satanás; Alcméon, Aristóteles; Tagaste, Cartago; o Tejo; a senhora Leta; Balaão, Balac; Davi; são Romualdo; santo Antão (*saint Antoine*, o abade do deserto, nas duas ocorrências de III.24); santa Maria Egipcíaca; são Paulo (o eremita); Arsênio; são Francisco (de Assis); são Tiago.

## Passagens difíceis

- **III.14, P1, *comme une paume*.** A *paume* é a bola do jogo da péla. Plínio diz que o ninho dos alcíones tem forma de bola, e o manuscrito do santo traz *ronds* (Annecy, variante a). Daí «como uma bola», e não «como a palma da mão».
- **III.14, P3, *son altération insatiable*.** *Altération* é a sede da febre. Para não repetir «sede» duas vezes na mesma linha, ficou «tem o seu ardor insaciável na conta de uma sede de todo natural e suave».
- **III.14, P5.** A sequência de *justement* («ter justamente o que outro possui justamente...») é de propósito, e ficou toda.
- **III.15, P11, *il se fût bien échauffé à la défense*.** «Teria posto muito calor em se defender»: a forma direta, com o verbo pronominal no condicional, pediria mesóclise.
- **III.16, P2, *témoin saint Alexis...*.** «Como o testemunham santo Aleixo...», que é o sentido do *témoin* invariável do francês.
- **III.17, P4, *ne peut non plus porter le nom d'amitié... que celles des ânes et chevaux*.** «Não pode levar o nome de amizade entre os homens, assim como não o pode a dos asnos e dos cavalos». A comparação negativa do francês, ao pé da letra, ficaria ambígua em português.
- **III.17, P5, *qui n'ont encore aucune vertu qu'en bourre ni nul jugement qu'en bouton*.** *Bourre* é a primeira penugem. Ficou «que ainda não têm virtude senão em penugem, nem juízo senão em botão», e a imagem passa.
- **III.17, P5, *ils ne se feindront nullement*.** *Se feindre* é hesitar (léxico de Annecy). Ficou «não hesitarão de modo algum».
- **III.18, P5, *qui prend est pris en ce jeu*.** O jogo é com *prendre de l'amour*. Fixei «tomar» em todo o parágrafo («sem que o tome necessariamente; neste jogo, quem toma é tomado»; «Bem quero tomar um pouco dele»), para que o trocadilho passe.
- **III.18, P6, *ces folles déduites*.** O léxico de Annecy dá *déduite* = «déduction, diminution». A imagem é contábil: Deus reservara para si todo o nosso amor e nos pedirá contas do que dele tiramos. Ficou «dessas loucas subtrações que dele fazemos».
- **III.18, P7, *le jouet des cours, mais la peste des cœurs*.** O trocadilho *cours* / *cœurs* não passa. «O brinquedo das cortes, mas a peste dos corações» guarda ao menos a aliteração em «cor-». Perda registrada.
- **III.19, P5, *ceux qui sont ès chemins scabreux... s'entretiennent l'un l'autre*.** *S'entretenir* é «segurar-se mutuamente» (léxico de Annecy): «se seguram uns aos outros». O mesmo verbo em III.21 (*le cœur et les oreilles s'entretiennent l'un à l'autre*) virou «estão ligados um ao outro».
- **III.20, P1, *Satan donne le change*; *prendre le change*.** É termo de caça: fazer os cães largarem a presa por outra. Ficou «Satanás lança os que amam numa pista falsa» e «tomar a pista falsa».
- **III.21, P4, *je suis bien moi-même* / *je ne suis pas moi-même*.** «Eu sou bem eu mesma» / «mas eu não sou eu mesmo», para que a réplica do rapaz feche o jogo.
- **III.21, P5, *Il ne faut point ménager pour un amour...*.** «Não se deve ter contemplações com um amor...».
- **III.21, P6, *encore m'en restera-t-il quelque ressentiment*.** *Ressentiment* é o sentimento que fica, não o rancor: «ainda me restará algum resquício dela». O «?» de Boulenger ficou: é uma objeção, a que o autor responde «Não ficarão» (*Non feront*). Annecy tem ponto.
- **III.22, P1 e P2, *supporter... porter... transporter*.** O autor joga com os três verbos: suportar o amigo nas imperfeições, mas não o *porter* (apoiar, levar adiante) nelas, e menos ainda transportá-las para nós. Ficou «suportar... mas não o apoiar nelas, e muito menos transportá-las para nós»; e, no parágrafo seguinte, «não se devem nem apoiar nem suportar no amigo». Perde-se parte do eco.
- **III.23, P3, *gourmander la gourmandise même*.** *Gourmander* é repreender, refrear. O trocadilho com *gourmandise* não passa: «refrear a própria gula». Perda registrada.
- **III.23, P5, *la peine du travail que celle du jeûne*.** Usei «fadiga» para *peine* em todo o parágrafo, para guardar a comparação («Um sente fadiga em jejuar, outro sente-a em servir os doentes... esta fadiga vale mais que aquela»).
- **III.23, P10, *pour l'outrepercer*.** O pronome pode ser o homem ou a consciência. Ficou «para traspassá-la», com a consciência, que é o substantivo mais próximo.
- **III.24, P1, *on doit demeurer en soi-même quand on y est. Or, on y est quand on est seul*.** «Devemos permanecer em nós mesmos quando estamos em nós. Ora, estamos em nós quando estamos sós.»
- **III.24, P6, *noircir l'autre*.** É a brincadeira de enfarruscar alguém com fuligem: «enfarruscar outro». *Faire du mal à un fol*: «fazer mal a um doido».
- **III.25, P2, *auprès des princes on rehausse l'état, lequel on doit abaisser entre les domestiques*.** *L'état* é o aparato, o luxo do trajar: «eleva-se o aparato, que se deve abaixar entre os de casa».
- **III.25, P2, *Qui ne veut recevoir les hôtes, il faut qu'il ôte l'enseigne de son logis*.** «Quem não quer receber hóspedes deve tirar a tabuleta da sua hospedaria.» O eco *hôtes* / *ôte* não passa.
- **III.25, P3, *que le diable en y pense toujours*.** Remete a III.27 (o *malin* que «pensa muito» nas palavras desonestas). Ficou «que o diabo sempre pensa», em paralelo com «não pensam mal nisso».
- **III.25, P3, *« Vous en faites trop »... « Vous en faites trop peu »*.** «Fazeis demais» / «Fazeis de menos».
- **III.26, P5, *par manière d'acquit et d'entretien*; *par manière d'entregent*.** «Por desencargo e para entreter a conversa»; *entregent* é «convenance, bienséance» no léxico de Annecy: «por mera conveniência». O fim, *qu'ils sont tels que les paroles témoignent ce qui n'est pas*, foi lido com a vírgula de Annecy (*témoignent, ce qui n'est pas*): «que são tais como as palavras testemunham, o que não é verdade».
- **III.27, P1, *il n'a pas tenu à sa malice qu'elle ne les ait fait mourir*.** «Não foi por falta de malícia dela que não os fez morrer.»
- **III.27, P4, *alléguer*; *après dîner*.** *Alléguer* é citar autoridades (a conversa erudita que os religiosos queriam): «Não é tempo de citar autoridades». O *dîner* do século XVII é a refeição do meio-dia; para não dizer «jantar», que no Brasil é a da noite, ficou «depois da refeição».

## Emendas pela edição de Annecy

Boulenger (no Wikisource) tem vários erros evidentes de transcrição. A tradução segue Annecy:

1. **III.14, P1, «le royaume des deux»** → «des cieux»: «o reino dos céus». (O OCR de Annecy erra do mesmo jeito em três lugares; é a leitura de *cieux*.)
2. **III.14, P1, «Celui lest riche»** → Annecy, «Celuy est riche».
3. **III.14, P5, «îcar»** → «car».
4. **III.14, P7, «d affection»**; **III.15, P5, «d autant»** → apóstrofo.
5. **III.15, P1, «cour- tois»** → «courtois».
6. **III.15, P6, «omme dit l'Écriture»** → Annecy, «comme dit».
7. **III.15, P7, «contentez-pas»** → Annecy, «contentes pas»; **«blanchisseuse, O ma Philothée»** → Annecy, «blanchisseuse. O ma»: ponto final antes do vocativo.
8. **III.15, P8, «eut su faire»** → Annecy, «eust sceu»: mais-que-perfeito do subjuntivo, «teria sabido».
9. **III.15, P11, «avec douceurs ces diminutlions»** → Annecy, «avec douceur ces diminutions»; **«Jacob en fît de même»** → «fit».
10. **III.16, P3, «extrêmement, pure»** → Annecy, sem vírgula.
11. **III.16, P7, «supporter, Si vous»** → Annecy, «supporter. Si vous».
12. **III.18, P6, «à beaucoup près de ce que nous avons besoin ?»** → Annecy, «besoin ;». O «?» não faz sentido antes de «je veux dire»; traduzi como afirmação.
13. **III.19, P5, «de peur que en particulier ce qui est commun»** → Annecy, «de peur que **cherchant** en particulier ce qui est commun». Falta o gerúndio em Boulenger; traduzi «para que, buscando em particular o que é comum, não se passe das particularidades às parcialidades».
14. **III.19, P7, «beaucoup de personnes, La perfection»** → Annecy, «personnes. La perfection».
15. **III.20, P3, «excite grandement feles femelles»** → Annecy, «les femelles».
16. **III.21, P1, «N'écoutez nulle sorte I de propositions»** → sem o «I».
17. **III.21, P6, «Philothëe»** → «Philothée».
18. **III.22, P1, «il n'y a presque celui qui nait quelque imperfection»** → Annecy, «qui n'ait»: «quase não há ninguém que não tenha alguma imperfeição».
19. **III.23, P4, «cette modération ès jeunes, disciplines»** → Annecy, «es jeusnes»: «nos jejuns».
20. **III.23, P9, «tu m as battue»** → «tu m'as battue».
21. **III.23, P10, «je n'aurais pas de mauvais mouvements»** → Annecy, «je n'auray pas»: futuro, em paralelo com «je ne serai point agitée». Traduzi «eu não terei maus movimentos».
22. **III.24, P6, «présomption.il faut pour l(ordinaire qu'une joie modérée ! prédomine»** → Annecy, «présomption. Il faut pour l'ordinaire qu'une joye modérée prédomine»; e **«afin que votre modestie ! paraisse»** → sem o «!». Os dois «!» são parasitas.
23. **III.24, P7, «Et à [l'exemple»** → sem o colchete.
24. **III.25, P1, «la bien- séance»** e **«La netteté extérieure | représente»** → sem o hífen de quebra e sem a barra.
25. **III.27, P1, «qu'elle ne lésait fait mourir»** → Annecy, «qu'elle ne les ait fait mourir».

**Aspas que não fecham em Boulenger** (Annecy não usa aspas nesses lugares; a citação vem em itálico, ou o texto é do autor):

26. **III.14, P1.** «Bienheureux sont les pauvres d'esprit, car le royaume des cieux est à eux ; malheureux donc...» abre e não fecha. Fechei depois de «é deles»: a bem-aventurança (Mt 5,3) é a citação; o resto é comentário do autor, como mostra a margem de Annecy.
27. **III.18, P5.** «O fols et insensés...» abre e não fecha. Fechei no fim do parágrafo, depois de «de alma e de honra».
28. **III.21, P7.** «Ah ! ce me direz-vous, mais ne sera-ce point une ingratitude...» abre e não fecha. Fechei depois de «uma amizade?», que é a objeção de Filoteia; a resposta é do autor.
29. **III.27, P1.** «Si quelqu'un ne pèche point en parole, dit saint Jacques, il est homme » parfait.» Fechei depois de «perfeito», que é parte do versículo (Tg 3,2; Annecy põe *parfait* no itálico da citação).

**Diferenças de Annecy que não mudam a tradução:** «Il se passera» × «Ilz se passeront» (III.18); «Vous voulez jouer avec lui» × «Vous vous voulés jouer» (III.18); «ce serait donc sacrilège» × «un sacrilège» (III.21); «Soyez bons changeurs et monnayeurs » × «Soyes bons changeurs » et monnoyeurs» (III.22, posição da aspa); «s'en faut détourner» × «il s'en faut destourner», «Restent» × «Reste» (III.24); «les vraies indices» × «les vrays indices» (III.26); «si nous n'y pensons pas» × «pensions» (III.27); «La communion des voluptés» × «La communication» (III.17, ver Dúvidas).

## Remissões

O texto remete a outros lugares do livro, sem número de página, e assim ficou:

- III.15, P4: «além do que eu disse no capítulo anterior» (III.14).
- III.21, P6: «conforme o que vos ensinei antes» (a solidão mental, II.12).
- III.24, P7: «como eu disse acima» (II.12) e «que vos referi em outro lugar» (o pensamento de são Gregório à beira-mar, II.13).
- III.25, P3: «como fiz em outro lugar» (III.27).

Nenhuma remissão de página a trocar.

## Dúvidas para quem coordena

1. ***Conversation*.** Usei «conversação» (no plural, «conversações») para o *conversation* do capítulo XXIV e dos lugares em que ele significa o trato social, as reuniões e visitas («as más conversações», «sair em conversação ou recebê-la em vossa casa»). É o termo das traduções portuguesas antigas da Filoteia e o sentido está nos dicionários, mas em português do Brasil corrente «conversação» lembra só «conversa». A alternativa é «convívio» ou «companhia», que se lê melhor, mas não serve em todos os lugares (*les conversations sont faites pour...*, *bonne conversation* = eutrapelia). **Proposta para o guia:** *conversation* (trato social) → conversação; *conversation particulière*, *devis*, *entretien* → conversa. O termo volta muito na Terceira Parte (cap. XXVIII–XLI) e na Quinta.
2. ***Amourettes*.** Usei «namoricos» (título de III.18: «Dos namoricos»). Guarda o diminutivo e o desdém do francês; «amores frívolos» seria mais neutro. O termo volta em III.21 e adiante. **Proposta para o guia:** *amourettes* → namoricos.
3. ***Honnêteté* em III.24.** Nas «conversações que têm por fim a *honnêteté*» (visitas mútuas e reuniões para honrar o próximo), traduzi «cortesia», porque «honestidade» se leria como pudor. Em todos os outros lugares do arquivo, *honnête* / *honnêteté* ficou «honesto» / «honestidade», como manda o guia.
4. ***Une grande ambition* (III.16, P6).** Boulenger: «c'est une grande ambition»; Annecy: «c'est une **trop** grande ambition». Segui Boulenger («é uma grande ambição»). Se a casa preferir Annecy nas diferenças de uma palavra, fica «uma ambição grande demais».
5. ***La communion des voluptés charnelles* (III.17, P4).** Boulenger: *communion*; Annecy: *communication*, que é a palavra de todo o capítulo. Segui Boulenger («A comunhão dos prazeres carnais»), porque o sentido é o mesmo; com Annecy seria «A comunicação».
6. **Santo Antão.** Traduzi o *saint Antoine* de III.24 por «santo Antão», a forma usual em português para o abade do deserto, para não confundir com santo Antônio de Pádua. Convém pôr no quadro de nomes do CONVENCOES.
