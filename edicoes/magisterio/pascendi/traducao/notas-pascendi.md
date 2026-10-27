# Notas do tradutor: *Pascendi Dominici Gregis* (São Pio X, 8 de setembro de 1907)

Tradução nova, do latim, para a Biblioteca Taioé. 96 blocos em cada arquivo: 6 de cabeçalho, 58
parágrafos, o fecho, a assinatura e 30 notas; 58 marcas `{§ n}` (a § 13 e a § 58 caem no meio de um
bloco). Nenhum título de seção. `conferir.py pascendi` sem problema; grep de mesóclise vazio.

## 1. O texto de base

- Base: o latim do vatican.va. Referência: *Acta Sanctae Sedis* 40 (1907), p. 593-650. O PDF do
  vatican.va (`ASS-40-1907-ocr.pdf`) **não tem imagem das páginas**: é só o texto do OCR, recomposto
  em fonte Times. A «conferência no PDF» foi, portanto, a comparação palavra a palavra do vatican.va
  com esse OCR (script em `~/.cache/claude-magisterio/tmp-pascendi/scripts/diff.py`). Só se corrigiu
  onde o vatican.va traz forma impossível ou ilógica e o OCR das ASS traz a forma certa; onde os dois
  são plausíveis, ficou o vatican.va (lista no § 1.4).
- O OCR das ASS também tem erros, e o letreiro espaçado (`l a b o r a v e r i t`) parece marcar
  ênfase; não serviu para conferir o itálico.

### 1.1 Mudanças de estrutura (todas pelas ASS)

- **Notas.** O vatican.va traz as referências entre parênteses no corpo do texto («(Act. xx. 30)»);
  nas ASS são notas de rodapé, numeradas por página. Voltaram a ser notas `[n]`, com numeração
  contínua (1-30), no ponto da chamada das ASS. Duas mudaram de lugar em relação ao vatican.va: [25]
  e [26] (§ 47) ficam depois de «dixit:» e «monuit:», como nas ASS, e não depois da citação. O texto
  das notas segue as ASS («Ep. ad Magistros… non. iul.», não «Iun.»), com as datas e números
  normalizados. A referência de Rm I, 21-22 (§ 33) está entre parênteses no corpo também nas ASS, e
  ficou assim.
- **Notas das ASS que não entraram:** a nota do redator ao título (assinada «N. R.»), e duas
  remissões «Cfr. Acta S. Sedis, vol. 29, pag. 359» (§ 49, depois de «decernimus») e «vol. 30, pag.
  39» (§ 51, depois da citação da *Officiorum*), que remetem a volumes das próprias ASS e parecem do
  redator; o vatican.va também não as tem. **Dúvida para o principal** (§ 7).
- **«II.» e «III.»** que o vatican.va põe no começo dos §§ 40 e 44 não estão nas ASS (conferido na
  p. 634 e 639) e saíram; o documento não tem títulos. Os «I.» a «VII.» das medidas práticas (§§ 45-56)
  estão nas ASS, no começo do parágrafo, e ficam no texto (não são títulos `## `).
- **Cabeçalho:** o vatican.va traz «LITTERAE ENCYCLICAE / PASCENDI DOMINICI GREGIS / SUMMI PONTIFICIS
  PIUS PP. X / DE MODERNISTARUM DOCTRINIS / AD PATRIARCHAS…» e não traz a saudação. Seguiu-se o
  modelo da *Mortalium animos* (papa, «Litterae encyclicae», nome, destinatários: tema, saudação),
  com a saudação das ASS («Venerabiles Fratres, salutem et Apostolicam benedictionem»).
- O fecho perdeu o itálico do vatican.va (como no modelo) e «MCMVII.» o ponto; «PIVS» → «PIUS».

### 1.2 Lacuna do vatican.va preenchida

- p. 597 (§ 6): «ex agnosticismo, *qui solum est in ignoratione*, ad atheismum» — a oração falta no
  vatican.va e faz par com «qui contra totus est in inficiatione positus».
- p. 595 (§ 4): «iure *in* vulgus audiunt»; p. 608 (§ 17): «ut *ut* scientiae extranea
  praedicetur»; p. 615 (§ 24): «Ibi *de* obiectis»; p. 648 (§ 55): «Libros *ne* negligant».

### 1.3 Correções (página das ASS; a lista sai do script `paginas3.py`)

### Palavras (116)

- p. 594: «gremioque ecclesiae» → «gremioque Ecclesiae»
- p. 594: «veneratis» → «venenatis»
- p. 594: «ausu sacrilege,» → «ausu sacrilego,»
- p. 594: «mirabitu iure» → «mirabitur iure»
- p. 595: «facerimus» → «fecerimus»
- p. 595: «personates» → «personatos»
- p. 595: «iure vulgus» → «iure in vulgus»
- p. 597: «ex _agnosticismo_, ad _atheismum_» → «ex _agnosticismo_, qui solum est in ignoratione, ad _atheismum_»
- p. 598: «iu _subsconscientia_» → «in _subconscientia_»
- p. 598-599: «religiose sensu,» → «religioso sensu,»
- p. 599: «conscientae» → «conscientiae»
- p. 599: «potestatum,» → «potestatem,»
- p. 599: «Ex hoc autum» → «Ex hoc autem»
- p. 600: «ipsani» → «ipsam»
- p. 601: «amrmetur» → «affirmetur»
- p. 601: «Quae a Vaticana Synodo» → «Quare a Vaticana Synodo»
- p. 601: «dixirit» → «dixerit»
- p. 601: «curas est» → «cuius est»
- p. 601: «sisnificat» → «significat»
- p. 602: «absolute continetur, infinites» → «absoluto continetur, infinitos»
- p. 603: «minim non» → «mirum non»
- p. 603: «doctrina aliae» → «doctrinae aliae»
- p. 604: «experientiam gignendum» → «experientiam gignendam»
- p. 604: «illum fuerit» → «illam fuerit»
- p. 604: «inverit» → «iuverit»
- p. 605: «experientae» → «experientiae»
- p. 605: «_religiosi sensui_» → «_religioso sensui_»
- p. 605: «commaxime» → «cummaxime»
- p. 607: «quovis religiose,» → «quovis religioso,»
- p. 607-608: «fidem contra, ut scientiae» → «fidem contra, ut ut scientiae»
- p. 609: «facia est» → «facta est»
- p. 609: «accommodate obstinatissime» → «accommodare obstinatissime»
- p. 609: «_immanentia_ et _symbolismi._» → «_immanentiae_ et _symbolismi_.»
- p. 610: «sedilia» → «sed illa»
- p. 611: «semiis» → «seminis»
- p. 612: «et origina aliquid» → «et origine aliquid»
- p. 612: «extraordinarium» → «extraordinariarum»
- p. 612: «quapiam religion sunt» → «quapiam religione sunt»
- p. 612: «opinions» → «opiniones»
- p. 613: «inspiratione sacrorum librorum» → «inspirationis sacrorum librorum»
- p. 613: «credente quavis» → «credente quovis»
- p. 614: «Quo modo Ecclesiae e» → «Quo modo Ecclesia e»
- p. 614-615: «commercium ut usus» → «commercium et usus»
- p. 615: «Ibi _obiectis_» → «Ibi de _obiectis_»
- p. 615: «haec ac philosophis» → «haec a philosophis»
- p. 615: «Pius Vl.» → «Pius VI.»
- p. 615: «dirivetur» → «derivetur»
- p. 615: «ab Ecclesiae seiungi» → «ab Ecclesia seiungi»
- p. 616: «potestatis eadem perscribentis» → «potestatis eamdem perscribentis»
- p. 618: «ex perversione» → «ex pervasione»
- p. 618: «sensus religios in» → «sensus religiosi in»
- p. 620: «Institute ergo» → «Instituto ergo»
- p. 620: «et ferentes» → «efferentes»
- p. 620: «ac sacrilegio ausu» → «ac sacrilego ausu»
- p. 620: «veligio» → «religio»
- p. 620: «homimim» → «hominum»
- p. 621: «dogmatum in sensus» → «dogmatum is sensus»
- p. 621: «iam singulorum» → «tam singulorum»
- p. 621: «quaque ab iis» → «quaeque ab iis»
- p. 621-622: «visum est iam consecutiones» → «visum est. Iam consecutiones»
- p. 623: «in ecclesia historia» → «in Ecclesiae historia»
- p. 623: «quae in Ecclesiae, altera» → «quae in Ecclesia, altera»
- p. 624: «tarn» → «tam»
- p. 624: «ea quacumque quae» → «ea quaecumque quae»
- p. 625: «Quia immo» → «Quin immo»
- p. 626: «scilicet magistrum et ducem» → «scilicet magistram et ducem»
- p. 626: «circumstantiis aeris» → «circumstantis aeris»
- p. 627: «nod sunt» → «noti sunt»
- p. 627: «patet her:» → «patet iter:»
- p. 628: «adversaries» → «adversarios»
- p. 628: «adversaries» → «adversarios»
- p. 628: «utrorum causae» → «ut eorum causae»
- p. 629: «Unde nec quod» → «Unde fiet quod»
- p. 629: «de Ecclesia dogmatibus» → «de Ecclesiae dogmatibus»
- p. 629: «Infinite honorem» → «Infinito honorem»
- p. 630: «enim postquam prorsus» → «enim postulari prorsus»
- p. 630: «capacitatem solem» → «capacitatem solum»
- p. 630: «sommatim» → «summatim»
- p. 631: «At catechesim» → «Ad catechesim»
- p. 631: «collecta nimirum contractaque in centum» → «collecta nimium contractaque in centrum»
- p. 631: «passivi anteponi» → «passivis anteponi»
- p. 632: «modernismo et quaestio» → «modernismo est quaestio»
- p. 633: «maximeinterest sic» → «maxime interest sit»
- p. 635: «sibique nimirum praefidens» → «sibique nimium praefidens»
- p. 636: «Germina vero» → «Gemina vero»
- p. 637: «illius monumentum ac pondus» → «illius momentum ac pondus»
- p. 637: «ecclesiasticas traditionis» → «ecclesiasticas traditiones»
- p. 637: «parve aut» → «prave aut»
- p. 639: «auctorum multitudini» → «auctorum multitudine»
- p. 639: «acre hausto» → «aere hausto»
- p. 639: «Sacros Reliquias» → «Sacras Reliquias»
- p. 641: «ancillarum move» → «ancillarum more»
- p. 641: «utiliter ansa» → «utiliter ausa»
- p. 641: «quanta rerum» → «quanto rerum»
- p. 641: «levitetque» → «leviterque»
- p. 642: «vel Institute» → «vel Instituto»
- p. 643: «Universatibus» → «Universitatibus»
- p. 643: «suscipeant» → «suscipiant»
- p. 644: «detulent» → «detulerit»
- p. 644: «aliquarum indicibus» → «aliquorum indicibus»
- p. 644: «nequeunt idea» → «nequeunt ideo»
- p. 646: «scientia de doctrinae» → «scientia et doctrinae»
- p. 646: «Constitutionis Officiorum- in» → «Constitutionis _Officiorum_ in»
- p. 646: «Vivi e clero» → «Viri e clero»
- p. 647: «preponatur» → «proponatur»
- p. 647: «onestum» → «honestum»
- p. 647: «perpetuenter» → «perpetuentur»
- p. 648: «Leonis XVI.» → «Leonis XIII.»
- p. 648: «Libros negligant» → «Libros ne negligant»
- p. 648: «questione sagitari» → «quaestiones agitari»
- p. 649: «ratibus» → «ritibus»
- p. 649: «Hoc qui teneant» → «Hoc qui teneat»
- p. 649: «in veritati nititur» → «in veritate nititur»
- p. 650: «novi aliquod» → «novi aliquid»
- p. 650: «suppetitias» → «suppetias»
- p. 650: «Ecclesiam Christo sincero» → «Ecclesiam Christi sincero»

### Espaços (palavras juntas ou partidas) (55)

- p. 594-595: «adradicem» → «ad radicem»
- p. 595: «tamen,Venerabiles» → «tamen, Venerabiles»
- p. 597-598: «devita» → «de vita»
- p. 598: «quiest» → «qui est»
- p. 599: «deDeo» → «de Deo»
- p. 599: «quae libet» → «quaelibet»
- p. 599: «dequo» → «de quo»
- p. 599: «quaereapse» → «quae reapse»
- p. 600: «deveteri» → «de veteri»
- p. 601: «exsurgentiain» → «exsurgentia in»
- p. 602: «quammodum» → «quam modum»
- p. 602: «obiectinotae» → «obiecti notae»
- p. 603: «tantoesse» → «tanto esse»
- p. 605: «quotandem» → «quo tandem»
- p. 605-606: «ineo qui» → «in eo qui»
- p. 609: «quid quid verum» → «quidquid verum»
- p. 609: «omni modis» → «omnimodis»
- p. 610: «quamformula» → «quam formula»
- p. 610: «acredente» → «a credente»
- p. 611-612: «cetero qui» → «ceteroqui»
- p. 612: «adnotiones» → «ad notiones»
- p. 617: «impensumin» → «impensum in»
- p. 617: «libri,quos» → «libri, quos»
- p. 617: «inter mortua» → «intermortua»
- p. 618: «quamquae» → «quam quae»
- p. 618: «praese tulerunt» → «prae se tulerunt»
- p. 619: «eoquod» → «eo quod»
- p. 623: «fidei,quod» → «fidei, quod»
- p. 623: «alterqui» → «alter qui»
- p. 623: «atque omniae dicit,» → «atque omnia edicit,»
- p. 624: «alteraquae» → «altera quae»
- p. 625: «praestituis se» → «praestituisse»
- p. 631: «a mandata» → «amandata»
- p. 632: «animis ensus» → «animi sensus»
- p. 633: «a mentis» → «amentis»
- p. 634: «homineut» → «homine ut»
- p. 634: «credentiaeque ac philosopho» → «credenti aeque ac philosopho»
- p. 634: «siqua habebitur» → «si qua habebitur»
- p. 636: «fortissimea» → «fortissime a»
- p. 636: «tollendamet» → «tollendam et»
- p. 636: «estindicium» → «est indicium»
- p. 636-637: «favereincipiat» → «favere incipiat»
- p. 639: «etiamde» → «etiam de»
- p. 640: «quidcum» → «quid cum»
- p. 641: «ante hac» → «antehac»
- p. 643: «nelegantur» → «ne legantur»
- p. 643: «quamquae» → «quam quae»
- p. 643: «cetero qui» → «ceteroqui»
- p. 643: «acrecentiori» → «ac recentiori»
- p. 644: «libriqui» → «libri qui»
- p. 645: «indoctrinis» → «in doctrinis»
- p. 647: «eiusmodi,quos» → «eiusmodi, quos»
- p. 647: «excidant,quae» → «excidant, quae»
- p. 647: «enim,Venerabiles» → «enim, Venerabiles»
- p. 648: «idgenus» → «id genus»

### Itálico mal posto (9)

- p. 596: «_externa revelation_e» → «_externa revelatione_»
- p. 602: «_formulasreligiosas_» → «_formulas religiosas_»
- p. 602: «_symbola,_» → «_symbola_,»
- p. 604: «_experientia._» → «_experientia_.»
- p. 604: «_sensu religios_o» → «_sensu religioso_»
- p. 605: «_sensus religiosi,_» → «_sensus religiosi_,»
- p. 611: «circa illam_, secundariae_» → «circa illam, _secundariae_»
- p. 613-614: «quaevi _permanentiaevitalis_,» → «quae, vi _permanentiae vitalis_,»
- p. 621: «_agnosticismus,_» → «_agnosticismus_,»

### Pontuação (4)

- p. 601: «ac secernatur, Id» → «ac secernatur. Id»
- p. 626: «ignorantiae accusent qui amplectitur» → «ignorantiae accusent; qui amplectitur»
- p. 628-629: «ob quem vivitur, Demum» → «ob quem vivitur. Demum»
- p. 645: «Ea si faverit. Episcopus» → «Ea si faverit, Episcopus»

Nas notas, além disso: «damn, a Leone X» → «damn. a Leone X», «facia est» → «facta est», «quid quid»
→ «quidquid» (nota 11, p. 610); «dirivetur» → «derivetur» (nota 13, p. 616); «Cone. Vat.» → «Conc.
Vat.» (nota 18); «kal. lul.» → «kal. iul.» (nota 20); «Tit. n.» → «Tit. II» (nota 28).

### 1.4 Leituras do vatican.va mantidas (o OCR das ASS diverge, mas as duas formas são possíveis)

«fibras altissimas» (ASS «altissimae», sem o ponto seguinte: erro do OCR); «damnarit»; «Exemplo res
illustrabitur»; «canonis… deducti»; «Mira quidem»; «advertisse»; «penitus» (ASS «penitius»); «nosse
qui velit»; «in priva… experientia» (ASS «privata»); «vindicabunt»; «patrarit»; «in se ipso»;
«effatum»; «iudicarit»; «vivat»; «a modernistis»; «qualecumque»; «criticem»; «ex philosophis»;
«conflata»; «reformator»; «ab orthodoxorum»; «dignissimos»; «ephemerides»; «elaboraverit» (ASS
«laboraverit»); «malorum clamoribus» (ASS «maiorum»: confusão l/i do OCR); «ab quibuscumque»;
«probarit»; «quidquid omne genus»; as grafias «numquam/nunquam», «quanquam», «enunciatio».
Também as ASS trazem «secundum circumstantia» (§ 21; deve ser «circumstantias»): ficou, e se
traduziu «segundo as circunstâncias».

### 1.5 Ano da carta de Gregório IX (nota 10)

Vatican.va e ASS dizem «1223»; Gregório IX foi eleito em 1227, e a carta aos mestres de Paris é de 7 de
julho de 1228. Não se corrigiu (não dá para ver se é erro do impresso ou do OCR); a tradução também
diz 1223. **Dúvida para o principal.** O mês foi corrigido pelas ASS: «non. iul.» = 7 de julho.

## 2. Termos novos (para a tabela do § 3 das convenções)

| original | tradução |
|---|---|
| modernismus; modernistae; modernista ut philosophus, credens… | modernismo; modernistas; o modernista como filósofo, crente… |
| sensus (religiosus) | sentimento (religioso) — nunca «senso» |
| immanentia vitalis; immanentia religiosa / theologica | imanência vital; imanência religiosa / teológica |
| permanentia divina / vitalis | permanência divina / vital |
| subconscientia; conscientia (religiosa, collectiva) | subconsciência; consciência (religiosa, coletiva) |
| agnosticismus; symbolismus; apriorismus; fideismus; intellectualismus | agnosticismo; simbolismo; apriorismo; fideísmo; intelectualismo |
| experientia (religiosa, originalis) | experiência (religiosa, original) |
| transfiguratio; defiguratio | transfiguração; desfiguração |
| incognoscibile | incognoscível |
| indigentiae, necessitates (*dei bisogni*) | exigências, necessidades |
| realitas (divina, historica) | realidade |
| critice; apologesis; apologeta | crítica; apologética; apologista |
| integralistae; americanistae; protestantes liberales | integralistas; americanistas; protestantes liberais |
| Vaticana Synodus; Tridentina Synodus | Concílio do Vaticano; Concílio de Trento |
| Pontifex Maximus; Antistites (sacrorum) | Sumo Pontífice; Prelados |
| Sacrum Consilium (Episcoporum et Religiosorum…; legitimis ritibus tuendis) | Sagrada Congregação (dos Bispos e Regulares; dos Ritos) |
| S. Officium; Index | Santo Ofício; Índice |
| Consilium a vigilantia | Conselho de vigilância |
| censores ex officio | censores de ofício |
| Magister sacri Palatii apostolici; Cardinalis in Urbe Pontificis Vicarius | Mestre do Sagrado Palácio Apostólico; Cardeal Vigário do Pontífice na Urbe |
| Decessor Noster fel. rec. | Nosso Predecessor, de feliz memória |
| Syllabus (Syll.) | Syllabus |

## 3. Passagens difíceis e leitura adotada

- § 1 «Pascendi dominici gregis mandatum Nobis divinitus officium»: «O ofício de apascentar o rebanho
  do Senhor, que Nos foi confiado do alto». As alusões a Jd 3 e 1Tm VI, 20 ficaram sem referência
  (o documento não as dá).
- § 3 «ut personatos male homines… demonstremus»: «homens que se disfarçam mal».
- § 7 e seguintes, *sensus*: «sentimento» (é o *sentiment* dos autores visados), não «sentido».
- § 13 «utpote quod absoluto continetur»: com a correção das ASS, «como está contido no absoluto».
- § 17 (Gregório IX) «rationalium»: «dos racionais» (os filósofos da natureza do séc. XIII), não
  «racionalistas», que seria anacronismo.
- § 22 «Est Deus in nobis, agitante calescimus illo» (Ovídio, *Fastos* VI, 5, sem referência no
  documento): traduzido em prosa, sem aspas, como está no latim.
- § 34 «quibus modernistae!» — o ponto de exclamação está também nas ASS: mantido («com os mesmos
  auxílios que os modernistas!»).
- § 36 «mendacium utilitatis seu officiosum»: «mentira de utilidade ou oficiosa».
- § 39 «omnium haereseon conlectum»: «o compêndio de todas as heresias».
- § 40 «nullaque est apud ipsos gradus… reverentia»: «nenhum respeito à hierarquia».
- § 42 «eodem tempore nulloque modo adhibito»: «ao mesmo tempo, e sem nenhuma medida».
- § 55 «quod a vigilantia dici placet»: «a que nos apraz chamar de vigilância».
- Citações de concílios, papas e Agostinho: traduzidas do latim do próprio documento. Períodos longos
  divididos em duas ou três frases onde, inteiros, ficariam confusos (§§ 2, 3, 6, 17, 34, 39).

## 4. Para `obras.py` (CORRECOES)

Sugestão: «O texto latino do vatican.va foi conferido palavra a palavra com o das *Acta Sanctae
Sedis*; corrigiram-se 184 erros de digitalização, completou-se uma oração que faltava (§ 6), e as
referências, que o vatican.va põe entre parênteses no texto, voltaram a ser notas, como nas *Acta*.»

## 5. Dúvidas para o principal

1. As duas remissões «Cfr. Acta S. Sedis…» das ASS ficaram de fora (§ 1.1): confirmar.
2. «1223» na nota 10 (§ 1.5): manter como no impresso ou pôr nota?
3. Cabeçalho reorganizado pelo modelo da *Mortalium animos* (§ 1.1): confirmar.
