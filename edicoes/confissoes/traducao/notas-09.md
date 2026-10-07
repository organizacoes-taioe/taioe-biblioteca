# Notas do tradutor: Confissões, Livro IX

Arquivo: `traducao/livro-09.txt`. Texto-base: `original/livro-09.txt` (O'Donnell, do The Latin Library).
Conferência: Knöll, CSEL 33 (1896), pp. 196–226 do OCR (`ferramentas/cache/confissoes/csel33_djvu.txt`,
a partir de `LIBER NONVS`), lido parágrafo a parágrafo, com o aparato.

38 parágrafos no original e 38 na tradução: 37 com marca, de `[I.1]` a `[XIII.37]`, iguais e na mesma
ordem, mais o parágrafo sem marca do hino de Ambrósio (continuação de `[XII.32]`), com 8 versos nos dois.
Grep de mesóclise, com `\b` e sem ele: nada.

## O hino de Ambrósio (XII.32, *Deus, creator omnium*)

Método do Versificador (`MANUAL-DE-TRADUCAO.md`; `ESTUDO-DO-RITMO.md`, § 5), como pede o guia da obra.

- **Original.** Oito dímetros jâmbicos (8 sílabas latinas, quatro jambos), as duas primeiras estrofes do
  hino; sem rima regular (*omnium, vestiens, lumine, gratia, quies, usui, allevet, anxios*). O Latin
  Library dá os oito versos seguidos, sem divisão de estrofe, e assim ficaram (um só parágrafo, para não
  alterar a contagem).
- **Metro de chegada.** Octossílabo com acento na 4.ª e na 8.ª, final grave, sem rima (o original não a
  tem: inventá-la seria acréscimo). Molde, um verso por linha: `8: 4-8 (2) (6) +1` (com `(1)` facultativo
  no primeiro).
- **Conferência.** `node ferramentas/molde.mjs versos.txt molde.txt` (temporários em
  `C:\Users\geren\AppData\Local\Temp\claude\confissoes-livro09\`): **8 exatos, nenhum ~, nenhum ✗, nenhum ≠,
  nenhuma leitura forçada**. Esqueletos: 1-2-4-6-8, 4-6-8, 2-4-6-8, 2-4-8, 2-4-8, 2-4-8, 4-6-8, 4-6-8
  (no máximo três iguais seguidos).
- **Rascunhos descartados.** «Deus, criador de quanto existe» (o leitor faz *cria-dor* em duas sílabas e o
  verso fica com 7: daí o «Ó» inicial); «que a quietude os membros soltos» (mesmo problema: *quie-tude*);
  «e solte o luto dos aflitos» (soaria como «soltar o pranto», o contrário do sentido).
- **Sentido, verso a verso.** *creator omnium* → «criador de quanto existe»; *poli rector* → «regedor do
  céu» (*polus* = a abóbada celeste); *vestiens diem decoro lumine* → «que o dia de luz formosa tu
  revestes» (a 2.ª pessoa vem do *tu es enim* de Agostinho); *noctem sopora gratia* → «e a noite, em graça
  soporosa» (*soporoso*, «que dá sono», é o equivalente exato de *soporus*); *artus solutos ut quies reddat
  laboris usui* → «que os membros soltos o repouso devolva ao uso do trabalho» (o *que* final vale «para
  que»); *mentes fessas allevet* → «e as fatigadas mentes erga»; *luctu solvat anxios* → «e do seu luto
  solte os tristes».
- **Ganhos e perdas.** Guardei o eco *solutos ... solvat* («soltos ... solte»). *Anxios* virou «tristes»
  (perde-se a ansiedade; «aflitos» não cabia em nenhuma posição do verso sem o 2-5-8, que a tradição não
  usa). *Allevet* («alivie», «erga») ficou no sentido literal de «erguer». A ordem dos versos 2–4 se
  inverteu um pouco (o dia passa ao verso 2, o verbo ao 3), sem mudar o sentido.
- O hino vai entre aspas, depois do «Pois tu és,» de Agostinho, que fica na prosa, como no latim. A página
  do Latin Library não traz a aspa de abertura (ver `original/LEIAME.md`); pus as aspas do português.
- Para o Livro XI (XXVII.35), onde Agostinho volta a *Deus creator omnium* para medir as sílabas: convém
  que o tradutor de lá saiba desta versão, embora ali o verso seja analisado e não citado como hino.

## Variantes O'Donnell × Knöll

Nenhuma variante deste livro obrigou a deixar O'Donnell; segui-o em todas. As que mudariam a tradução
(Knöll segue em quase todas o códice S, o Sessoriano, contra a maioria dos manuscritos):

- **XIII.34** *iam sanato corde ab illo vulnere **in quo poterat redargui carnalis affectus*** (O'D) ×
  *in quo **postea redargui carnales affectus*** (Knöll, com S). Com O'D: «curado já o coração daquela
  ferida, em que se poderia repreender um afeto carnal»; com Knöll: «daquela ferida, na qual depois
  repreendi os afetos carnais». Segui O'Donnell (maioria dos códices): a frase retoma o parágrafo anterior
  («se achar pecado em eu ter chorado minha mãe...»), em que a culpa é possível, não afirmada.
- **XIII.34** *si remota misericordia **discutias** eam* (O'D) × ***discutiam*** (Knöll, com S): «se a
  examinares», não «se eu a examinar». Segui O'Donnell: a frase seguinte (*quia vero non exquiris delicta
  vehementer*) fala do exame de Deus. No mesmo lugar, *quia vero* (O'D) × *quia omnino* (Knöll): sem
  efeito.
- **IV.8** Sl 4,2: *cum invocarem, **exaudivit me deus** iustitiae meae* (O'D) × *cum invocarem **te,
  exaudisti me**, deus...* (Knöll, com S e W). Segui O'Donnell: «Quando eu invocava, ouviu-me o Deus da
  minha justiça»; com Knöll seria «Quando eu te invocava, tu me ouviste, Deus da minha justiça».
- **III.5** *amoenitatem sempiterne **virentis** paradisi tui* (O'D) × *sempiternae **virtutis** paradisi
  tui* (Knöll, com S). Segui O'Donnell: «a amenidade do teu paraíso sempre verdejante», que responde ao
  campo de Cassicíaco (*rus*) dado por Verecundo; com Knöll seria «a amenidade da eterna virtude do teu
  paraíso».
- **III.5** *retribues illi, domine, in **resurrectione** iustorum* (O'D, com Lc 14,14) × *in
  **retributione** iustorum* (Knöll, com S). Segui O'Donnell: «na ressurreição dos justos».
- **IV.12** *genua **supplici** affectu fiximus* (O'D) × ***simplici*** (Knöll, com S): «com afeto
  suplicante», não «com afeto simples».
- **VIII.18** *in puerilibus **animis*** (O'D) × *in puerilibus **annis*** (Knöll, com S): «nas almas
  pueris», não «nos anos da infância».
- **VIII.18** *per praepositos homines*: Knöll marca o lugar com a cruz (†) e registra a conjectura de
  Antoine Arnauld, *praeposteros* («homens pervertidos», que caberia à criada da história). O'Donnell
  imprime *praepositos* sem cruz. Segui O'Donnell: «por meio dos homens postos à frente dos outros».
- **VI.14** *multa eius **alias** mirabiliora* (O'D) × *multa eius **alia** mirabiliora* (Knöll):
  «noutras ocasiões, muitas coisas ainda mais admiráveis» × «muitas outras coisas mais admiráveis».
  Diferença mínima; segui O'Donnell.
- **XII.29** *iuvenali voce cordis* (O'D) × *iuvenali voce, voce cordis* (Knöll, com S): «pela voz
  juvenil do coração» × «por uma voz juvenil, a voz do coração». Segui O'Donnell.
- **IV.11** *ad alia **multa** adipiscenda* (O'D, com a maioria) × *ad alia adipiscenda* (Knöll):
  mantive «muitas outras coisas».
- Sem efeito na tradução, ou quase: I.1 *dicant* × *dicent*, *divitiis meis* × *divitiis*; II.2 *a
  convalle* × *in convalle*; II.4 *deponere* × *ponere*; III.5 *benigne sane* × *benigne tamen*, *ea ipsa
  tamen* × *ea tamen ipsa*; III.6 *tuus autem, domine* × *tuus autem*; IV.9 *graviter ac fortiter* × *et
  fortiter*; IV.10 *devorans* × *et devorans*, segundo *ostendet* × *ostendit*, *afferent* (O'D; leia-se
  *afferrent*) × *afferrent*; VI.14 *domitori* × *dominatori*, *dulcedine* × *dulcitudine*, *super
  salutem* × *super salute*; VII.16 *propalata* × *prolata*; VIII.17 *nec liberet* × *non liberet*;
  VIII.18 *tamquam puella sobria* × *puella sobria*; X.24 *ubi pascis* × *unde pascis*, *veritate pabulo*
  (O'D e Knöll, com S) × *veritatis pabulo* (maioria); X.26 *deus meus praestitit* × *deus praestitit*;
  XII.31 *dolebam dolorem* × *dolebam dolorem meum*; XII.32 *evigilavi* × *vigilavi*; XIII.35 *dimitte
  illi et tu* × *dimitte et tu illi*; XIII.36 *condiri aromatis* × *condi aromatis*, *quid obiciat* ×
  *quod obiciat*; XIII.37 *haec legerint* × *hoc legerint*, *in hanc vitam* × *in hac uita*. Em XI.28 o
  OCR dá *nolebat* por *volebat*, sem registro no aparato: erro de OCR.

## Termos e nomes novos

| latim | tradução | onde / observação |
|---|---|---|
| *hostia laudis* | hóstia de louvor | I.1 (Sl 115,17) |
| *nugae* | ninharias | I.1 *suavitatibus nugarum* → «doçuras das ninharias»: as mesmas *nugae nugarum* do Livro VIII (XI.26–27). Harmonizado na revisão de coerência (antes: «frivolidades») |
| *garrire* | tagarelar | I.1: *garriebam tibi*, a conversa de criança com Deus; guardei o verbo, que é de propósito |
| *nundinae loquacitatis* | a feira da tagarelice | II.2 |
| *bella forensia* | guerras do foro | II.2 |
| *vindemiales feriae* | as férias da vindima | II.2, II.3, V.13 |
| *sollemniter* | na data costumada | II.2: sair «na forma regular», no fim do período letivo; «solenemente» enganaria |
| *canticum graduum* | o cântico dos degraus | II.2 (títulos dos Sl 119–133) |
| *cupiditas* | cobiça | II.4: o desejo de ganho e de carreira |
| *militia tua* | a tua milícia | II.4; *militia saecularis* → «a milícia do século» (VIII.17) |
| *cathedra mendacii* | a cátedra da mentira | II.4: a cadeira de retórica |
| *sors* | quinhão | III.5: *ipsam sortem retribuisti ei* → «já lhe deste em retribuição o próprio quinhão» (a parte na herança dos santos; «sorte» seria ambíguo) |
| *rus*, *in re eius* | o campo; a sua propriedade | III.5, VI.14 |
| *villa* | a casa de campo | IV.7, IV.8 |
| *libri disputati* | os livros das discussões | IV.7: os diálogos de Cassicíaco (com os presentes) e os *Solilóquios* (consigo); não acrescentei os títulos |
| *typhus* | o fumo do orgulho | IV.8, como no Livro VI (VI.10) |
| *gens tenebrarum* | a raça das trevas | IV.10: termo maniqueu (o princípio do mal) |
| *vetustas* | vetustez | IV.10: *mactans vetustatem meam*, o «homem velho»; «velhice» enganaria |
| *idipsum* | o Mesmo | IV.11 (Sl 4,9 *in idipsum*), IV.11 (*tu es idipsum valde* → «tu és o Mesmo em sumo grau»), X.24 (*in idipsum* → «para o Mesmo»). Nome de Deus como aquele que não muda (Sl 101,28 *tu autem idem ipse es*); maiúscula por ser nome divino. Proponho fixá-lo para os livros seguintes |
| *nomen dare* | dar o nome | VI.14: inscrever-se para o batismo |
| *de magistro* | _O mestre_ | VI.14: título do diálogo com Adeodato; em itálico e traduzido, como _Sobre o belo e o apto_ no Livro IV |
| *antistes* | prelado | V.13, VII.16, como no Livro VI |
| *agens in rebus* | _agens in rebus_ | VIII.17: corpo de correios e informantes da administração imperial; termo técnico deixado em latim e itálico, como no Livro VIII (VI.15). Harmonizado na revisão de coerência (antes: «agente do imperador») |
| *municipium* | município | VIII.17: Tagaste |
| *Ostia Tiberina*, *Ostia* | Óstia Tiberina, Óstia | VIII.17, X.23, XI.28 |
| *virga Christi tui, regimen unici tui* | a vara do teu Cristo, o governo do teu Unigênito | VIII.17; *unicus tuus* → «teu Unigênito», como nos Livros X, XI e XIII (harmonizado na revisão de coerência; antes: «teu Filho único») |
| *famula decrepita* | uma criada decrépita | VIII.17 |
| *cupa*, *laguncula*, *caliculi*, *merum* | o tonel, a garrafinha, os copinhos, vinho puro | VIII.18 |
| *vinulentia* | o gosto pelo vinho | VIII.18: o Livro VI usou «embriaguez»; aqui trata-se de uma menina que sorve gotas, e o próprio texto nega a *temulenta cupido*; «embriaguez» ficou para *temulenta* |
| *meribibula* | beberrona | VIII.18: diminutivo cunhado sobre *merum* + *bibere* («bebedorazinha de vinho puro»); «beberrona» guarda o insulto, não o *merum* |
| *tabulae matrimoniales* | as tábuas a que chamam matrimoniais | IX.19: o contrato de casamento lido na cerimônia |
| *cubilis iniuriae* | as ofensas ao leito conjugal | IX.19: as infidelidades de Patrício |
| *mancipium* | serva | IX.21: *bono mancipio tuo*; literalmente «propriedade, escrava» |
| *conversatio* | trato; viver | IX.22 (*sanctae conversationis* → «de um santo viver»), XII.33 (*conversationem eius piam* → «o seu trato, piedoso») |
| *dormitio* | dormição | IX.22 |
| *Hierusalem* | Jerusalém | XIII.37 |
| *chirographum* | a cédula | XIII.36 (Cl 2,14): o título de dívida; «cédula», como no Livro VII (XXI.27), na mesma citação. Harmonizado na revisão de coerência (antes: «o quirógrafo») |
| *sacrificium pretii nostri* | o sacrifício do nosso resgate | XII.32: a eucaristia oferecida junto ao túmulo |
| *balanion* | _balanion_ | XII.32: em itálico, como palavra estrangeira; ver abaixo |
| Verecundus | Verecundo | III.5 (já no guia) |
| Evodius | Evódio | VIII.17, XII.31 |
| Iustina, Valentinianus | Justina, Valentiniano | VII.15 (*Valentiniani regis pueri* → «do menino rei Valentiniano») |
| Protasius, Gervasius | Protásio, Gervásio | VII.16 |
| *basilica ambrosiana* | a basílica ambrosiana | VII.16: em minúscula, como adjetivo, como no latim |
| Monnica, Patricius | Mônica, Patrício | XIII.37, IX.19 (já no guia; o latim tem a grafia *Monnica*) |

*Animus* → espírito (I.1, XII.29) e ânimo (II.3, IV.8, VII.16, XI.28, XII.32), conforme o caso;
*anima* → alma; *mens* → mente; *libido* → paixão (*scabiem libidinum*, I.1); *continentia* → continência;
*catechumenus* → catecúmeno; *manichaei* → os maniqueus. Deus por «tu» em todo o livro.

## Passagens difíceis e leitura adotada

- **I.1, *tu autem, domine, bonus et misericors, et dextera tua respiciens ... et exhauriens*.** Frase
  sem verbo finito, com dois particípios. Dei-lhe verbos («és bom ... a tua destra olhava ... e esgotava»)
  para não deixar um fragmento solto em português.
- **I.1, *quas amittere metus fuerat iam dimittere gaudium erat*.** «E as que fora um medo perder, já era
  uma alegria deixar»: guarda o quiasmo; o jogo *amittere / dimittere* virou «perder / deixar».
- **II.3, *ut putaretur et disputaretur de animo meo*.** «Que se opinasse e se disputasse»: o par
  *putare / disputare* passou só em parte.
- **II.4, *propter liberos suos me liberum esse numquam volebant*.** O jogo *liberi* (filhos) / *liber*
  (livre) não passa: «por causa dos seus filhos, nunca queriam que eu fosse livre». Perda.
- **II.4, *vacandi et videndi quoniam tu es dominus*.** Sl 45,11 (*vacate et videte*): «ter vagar e ver».
- **III.5, *nec christianum esse alio modo se velle dicebat quam illo quo non poterat*.** Verecundo só
  queria ser cristão como os amigos, renunciando ao casamento, o que lhe era impossível: «de outro modo
  senão daquele de que não era capaz».
- **III.5, *in monte incaseato*.** Sl 67,16 (Vetus Latina: *mons incaseatus*, «monte coalhado», como
  queijo). Agostinho brinca com *Cassiciacum* e *caseus* (queijo): ao campo de Cassicíaco responde o
  «monte coalhado» de Deus. Traduzi «no monte coalhado»; o jogo com o nome do lugar se perde.
- **III.6, *veritatis filii tui carnem phantasma crederet*.** O docetismo maniqueu. Entendi *veritatis* em
  aposição a *filii tui*: «a carne do teu Filho, a Verdade».
- **III.6, *adoptivus ex liberto filius*.** «Filho adotivo, de liberto que era»: Nebrídio, libertado (do
  pecado), passa de liberto a filho.
- **III.6, *tu, domine, quem potat ille*.** «Tu, Senhor, a quem ele bebe»: Deus é a própria bebida.
- **IV.7, *tamquam in pausatione anhelantibus*.** As letras de Cassicíaco «ainda respiravam, como numa
  pausa ofegante, a escola da soberba»: a imagem é a do corredor que, parado, ainda arqueja.
- **IV.7, *me complanaveris humilitatis montibus et collibus*.** Os dois textos leem *humilitatis* (alguns
  códices, *humiliatis*). «Me aplanaste, abaixando à humildade os montes e as colinas dos meus
  pensamentos» serve às duas leituras (Is 40,4).
- **IV.8, *muliebri habitu, virili fide, anili securitate, materna caritate, christiana pietate*.** Série
  de cinco, guardada: «com hábito de mulher, fé de homem, serenidade de anciã, caridade de mãe, piedade de
  cristã».
- **IV.8, *sacramenta / medicamenta*, *insani / sani*.** Passaram: «sacramentos / medicamentos», «insanos /
  sãos».
- **IV.8, a frase longa sobre o Salmo 4.** *Vellem ut ... audirent voces meas ... quid de me fecerit ille
  psalmus (...) audirent ignorante me*. Repeti «quisera» para retomar o fio depois da citação.
- **IV.9, *clamat "quousque", clamat "scitote", et ego tamdiu nesciens*.** «Sabei / sem saber»: passou.
- **IV.10, *internum aeternum*.** «O eterno interno»: guardei a rima.
- **IV.10, *in cubili*.** «No leito», como o Sl 4,5 (*in cubilibus vestris compungimini*), que está por
  trás.
- **IV.11, *surdis mortuis*.** «Aqueles mortos surdos»: os maniqueus.
- **IV.11, *litteras de melle caeli melleas et de lumine tuo luminosas*.** «As letras melífluas do mel do
  céu e luminosas da tua luz»: guardei a dupla figura etimológica como pude.
- **VI.14, *formare nostra deformia*.** «Dar forma às nossas deformidades».
- **VI.14, *horrori mihi erat illud ingenium*.** «Aquele engenho me causava assombro»: *horror* aqui é o
  espanto sagrado diante do extraordinário.
- **VII.16, *civis civitatique notissimus*; *ut duceret suum ducem rogavit*.** «Um cidadão ... muito
  conhecido na cidade»; «pediu ao seu guia que o guiasse»: os dois jogos passaram.
- **VII.16, *olim suspirans tibi et tandem respirans, quantum patet aura in domo faenea*.** «Suspirava /
  respirava» passou. A *domus faenea* é a carne, que é feno (Is 40,6): «tanto quanto dá lugar ao ar uma
  casa de feno».
- **VIII.17, *parturit / parturivit*.** «Dá à luz / me deu à luz»: passou. *Multa praetereo, quia multum
  festino* → «muito deixo passar, porque tenho muita pressa».
- **VIII.17, *ut iam nec liberet quod non deceret*.** «Que já não lhes aprouvesse o que não lhes
  conviesse»: guarda a rima.
- **VIII.18, *qui modica spernit, paulatim decidit*.** Eclo 19,1: «quem despreza o pouco, pouco a pouco
  cai», com a repetição de *modicum* («àquele pouco outros poucos»).
- **VIII.18, *de alterius animae insania sanasti alteram*.** «Pela insânia de uma alma sanaste a outra»:
  passou.
- **VIII.18, *aut ne forte et ipsa periclitaretur, quod tam sero prodidisset*.** A criada não denunciou a
  menina em público por medo de ser punida por ter calado tanto tempo: «por tê-la denunciado tão tarde».
- **IX.19, *illae arguebant maritorum vitam, haec earum linguam*.** «Elas culpassem a vida dos maridos,
  ela culpava a língua delas»: antítese guardada.
- **IX.21, *male loquendo / bene loquendo*.** «Falando mal / falando bem».
- **IX.22, *quia ex munere tuo sinis loqui*.** Agostinho se desculpa de chamar a si e aos amigos «teus
  servos»: «(pois, por dom teu, nos deixas falar)».
- **X.24, *verbum / verbo tuo*.** «A palavra começa e acaba» × «o teu Verbo»: em latim é a mesma palavra
  (*verbum*); em português o jogo se perde em parte. Perda.
- **X.25, o discurso de Óstia.** Uma só frase condicional, com *sileat* repetido e apódose em *nonne hoc
  est*. Usei o futuro do subjuntivo («se para alguém se calar ..., se calarem ...») e o presente na
  apódose («não é isto»), para guardar a anáfora e o ritmo. Aspas: “...” para o discurso inteiro, ‘...’
  para as duas citações dentro dele.
- **XI.27, *ponitis hic matrem vestram* / *ponite hoc corpus ubicumque*.** *Ponere* é «sepultar»: «Sepultais
  aqui a vossa mãe» / «Sepultai este corpo em qualquer lugar», para guardar o par.
- **XI.28, *ista inanitas plenitudine bonitatis tuae*.** «Esse vazio, pela plenitude da tua bondade»:
  guardei a antítese *inanitas / plenitudo*.
- **XI.28, *coniuncta terra amborum coniugum terra tegeretur*.** «Que a terra unida de ambos os esposos
  fosse coberta de terra»: guardei a repetição de *terra*.
- **XII.29, *nec misere moriebatur nec omnino moriebatur*.** «Nem morria miseravelmente, nem morria de
  todo».
- **XII.31, *alio dolore dolebam dolorem*.** «Doía-me da minha dor com outra dor».
- **XII.32, *imus, redimus*.** Presente seco, como no latim: «vamos, voltamos sem lágrimas».
- **XII.32, *balneis nomen inditum quia graeci balanion dixerint, quod anxietatem pellat ex animo*.**
  Etimologia popular do grego βαλανεῖον («banho»), como se viesse de βάλλειν τὴν ἀνίαν («lançar fora a
  aflição»). Deixei *balanion* em itálico, sem glosa; o leitor entende o sentido pela frase.
- **XIII.36, *quis ei refundet innocentem sanguinem? quis ei restituet pretium*.** O *ei* é o inimigo:
  ninguém pode devolver ao diabo o sangue de Cristo nem o preço do resgate, para que ele reclame a alma.
- **XIII.36, *cui nemo reddet, quod pro nobis non debens reddidit*.** «A quem ninguém pagará o que ele,
  sem nada dever, pagou por nós»: guardei *reddet / reddidit*.
- **XIII.37, *per confessiones*.** Traduzi «por meio das confissões», sem demonstrativo: a palavra é a do
  título, e o leitor reconhece o livro.

## Citações bíblicas que exigiram decisão

Todas traduzidas do latim de Agostinho, sem referência no texto.

- **IV.8–11, o Salmo 4.** Segui o texto que Agostinho cita, versículo a versículo: *in tribulatione
  dilatasti mihi* → «na tribulação me dilataste»; *quousque graves corde?* → «até quando pesados de
  coração?» (sem verbo, como no latim); *magnificavit sanctum suum* → «engrandeceu o seu Santo» (e
  *magnificaveras* → «tinhas engrandecido», para guardar o eco; *clarificatus* de Jo 7,39 → «glorificado»);
  *signatum est in nobis lumen vultus tui* → «está impressa em nós a luz da tua face» (*vultus* de Deus → «face», como nos outros livros; antes «do teu rosto»); *in pace in
  idipsum* → «em paz, no Mesmo»; *singulariter in spe constituisti me* → «de modo singular me firmaste na
  esperança».
- **X.25, 1 Cor 15,51.** *Omnes resurgimus, sed non omnes immutabimur* (a forma latina, que difere do grego): «todos ressurgirmos, mas nem todos seremos transformados».
- **XII.31, Sl 100,1.** *Misericordiam et iudicium cantabo tibi, domine* → «Cantarei a ti, Senhor, a
  misericórdia e o juízo».
- **XIII.35, Tg 2,13.** *Superexultet misericordia iudicio* → «Que a misericórdia exulte acima do juízo».
- **XIII.35, Rm 9,15.** *Qui misereberis cui misertus eris, et misericordiam praestabis cui misericors
  fueris* → «tu que terás compaixão de quem tiveres tido compaixão, e usarás de misericórdia com quem
  tiveres sido misericordioso».
- **XIII.36, Sl 118,108.** *Voluntaria oris mei approba, domine* → «aprova, Senhor, as ofertas
  voluntárias da minha boca».
- **III.6, Sl 26,8.** *Quaesivi vultum tuum; vultum tuum, domine, requiram* → «Busquei a tua face; a tua
  face, Senhor, eu buscarei», como no Livro I (XVIII.28); harmonizado na revisão de coerência (antes: «o teu rosto»).

## Propostas para o guia (não alterei o guia)

- Fixar *idipsum* → «o Mesmo», com maiúscula, para toda a obra.
- Fixar *antistes* → «prelado» e *typhus* → «o fumo do orgulho», já usados nos Livros VI e IX.
