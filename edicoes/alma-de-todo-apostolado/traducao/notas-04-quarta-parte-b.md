# Notas do tradutor: A alma de todo apostolado, Quarta parte, d) a g)

Arquivo: `traducao/04-quarta-parte-b.txt`. Texto-base: `original/04-quarta-parte-b.txt` (12e édition, 1927,
págs. 148–194 do livro, seções d) a g) do capítulo único da 4ª parte). Conferido contra a imagem do scan,
página a página: `ferramentas/cache/alma/rev/165.png` a `211.png` (47 páginas). Um tradutor anterior
caiu antes de gravar; não havia arquivo parcial, e a tradução foi feita inteira nesta sessão.

Conferência por script: 200 blocos no original e 200 na tradução, do mesmo tipo e na mesma ordem: 1
cabeçalho, 16 títulos `##` (d) a g), as nove classes de almas e três `## * * *`, copiados como estão), 20
notas `¤ [n]`, 5 parágrafos de continuação de nota `¤` (um na nota 1, um na nota 8, três na nota 11) e
158 parágrafos de prosa (os 158 do LEIAME). O arquivo não tem marca `[X.n]` (começa no meio do `[IV.1]`;
o `[IV.1]` e o `[I.1]` só aparecem, iguais, dentro da linha `# nota:`). As 21 chamadas (a `[6]` aparece
duas vezes, como no livro: *Declina a malo* e *Fac bonum* remetem à mesma nota, Ps. XXXVI) e as 20 notas
estão iguais e nos mesmos parágrafos. As linhas `# ` do topo foram copiadas; só o `# titulo:` foi
traduzido («Quarta parte, capítulo único, d) a g)»). Razão de tamanho tradução/original: mínimo 0,68,
máximo 2,05. Os dois abaixo de 0,8 são esperados: a nota 5 (a remissão de página foi trocada, ver
abaixo) e «Leur plan à tous deux était celui-ci :» → «O plano de ambos era este:». O máximo é a nota 1,
com o `[Trad.: …]`. Aspas: 40 «» no original, 40 na tradução. Grep de mesóclise do CONVENCOES e varredura
em Python com a mesma regex terminada em `(?![A-Za-zÀ-ÿ])`: nenhum resultado (uma mesóclise escapou no
rascunho, no parágrafo depois das nove classes, e foi reescrita: «Mas poderia alguém desculpar…»). Underscores e `**`
fechados em todos os blocos.

## Decisões gerais

- **Itálico do autor**, conferido nas 47 páginas do scan, como na Primeira parte. Além do latim e dos
  títulos de obras, ficaram em itálico as ênfases visíveis na imagem:
  - d): *porte-grâce* (duas vezes), *source*, *comme ce n'est qu'après avoir prié*, *admire*,
    *savoure*, *vivante*;
  - e): a proposição *Une œuvre ne s'enracine profondément … à la vie intérieure*, *collaborateurs*,
    *seul*, *assez de vie pour produire d'autres foyers de vie féconde*, *Tant qu'une œuvre n'a pu
    produire ce résultat, son existence est éphémère*, *concevoir*, *sine qua non*, *moyens* (ver
    abaixo), os títulos das cantigas, *Ave maris stella* e *Ave Maria*, *d'arriver à la sainteté*,
    *disait*, *onction*;
  - f): « *Œuvre profane dirigée par un curé* », *à quel point*, *Panem et Circenses*, « *Galette et
    Cinéma* », *utiles*, *prédication par l'exemple*, *exempla trahunt* (duas vezes), *l'apostolat sur
    le peuple*, *la formation des élites pour la grande propagande par le Bon Exemple*, a pergunta dos
    pagãos « *Quelle est donc cette religion …?* », *Ligue tacite de l'action par le bon exemple*,
    *l'éclat des vertus évangéliques*, *Aimez-vous les uns les autres*, *indispensable*, a resposta de
    Pio X (*ce qui est présentement* LE PLUS *nécessaire … vraiment apôtres*), *mais surtout par
    l'exemple*, *de statu animarum*, a frase *Si c'est dans la formation des élites … est une faute*;
    na nota 8, *de la ferveur des prêtres*, *sur elles*, *ne ressort pas de la qualité*; *même infime*,
    *le rôle considérable qu'ils attachaient à la direction spirituelle*, *en dirigeant
    individuellement chaque jeune homme*, *confesseur*, *directeur spirituel*, *les orienter*, *la
    direction mensuelle accordée à chaque sujet*, *par la direction spirituelle*, *faut*, *à fortiori*,
    *œuvres*, *toujours à court de temps*, *les patronages, écoles, orphelinats, etc.*, *pères et de
    mères de famille*, *dans l'âme d'un enfant!*, *une direction*, *Que de vocations sacerdotales et
    religieuses auraient pu éclore!*, *une paroisse*, *une mission*, *Petits Séminaires*, *vers la
    perfection*, *Communautés religieuses*, *tenues de tendre à la perfection*, *Que de prêtres aussi
    seraient bien plus fervents*, *plus de saints*, *Pour certaines âmes*, *transformer la société par
    les élites*, *et le prouvent par leur rayonnement de vie intérieure*, *Regimen animarum*, *Ars
    artium*, *Savoir*, *Savoir-faire*, *Que de fausses notions et de préjugés*, a definição *La
    Direction consiste … perfection* (com «(le prêtre surtout)» em redondo, como no livro), *Vis
    unitiva*, *compendium*, *Duc in altum*, *ex communiter contingentibus*;
  - as nove classes: os rótulos *Péché mortel.*, *Péché véniel.*, *Imperfections.*, *Prière.*; depois,
    os nomes das quatro classes, *quantité*, *vraie paix*, *Calme*, *recueillement*, *confiance*, *la
    classer*, *Excelsior*, *fidélité à l'oraison*, *l'examen particulier*, *surhumaine*, a frase
    *Former des élites … sur les autres!*, *intimement incorporées*;
  - g): *foyer de toute activité, de tout dévouement, de tout apostolat*, *parole morte*, *Hic*,
    *Porte-Christ*, *Au degré de vie eucharistique … de son apostolat*, *vie* (três vezes, «la *vie*
    intérieure, la *vie* eucharistique, la *vie* liturgique»), *faute de puiser assez à la source de la
    vie*, *actifs*, *bonne*, *excellente*, *ce rayonnement du bonheur éternel et infini de Dieu*, *facti
    diabolo terribiles*, a citação de são Francisco *L'oraison, c'est la source … de sa bouche*.
  - Nas notas: *Exhort. ad clerum cathol.*, *Ami du Clergé*, *Serm. de S. Joan. Bapt.*, *Prédication*,
    os títulos da nota 9 e da nota 11 e *Lettres*, todos em itálico no livro.
- **Negrito do livro.** O livro imprime em negrito os quatro pontos da direção (*Paix.*, *Idéal.*,
  *Prière.*, *Renoncement.*), o «le plus» no meio da resposta de Pio X (em itálico) e *Porte-Christ!*
  no fim de g) (negrito e itálico). Foram marcados com `**…**`, que o `js/app.js` aceita: «1° **Paz.**»,
  «_o que é presentemente_ **o mais** _necessário…_», «**_Portadores de Cristo_**».
- **Versalete** em maiúsculas, como manda o guia: FONTE POTAVIT, ORBE DIFFUDIT (dentro do latim, em
  redondo no livro, fora do itálico), MULTIPLICAR, PELO EXEMPLO, CLASSIFICAVA (o livro tem
  «CLASSAIT-IL» em maiúsculas cheias; o pronome sujeito posposto não passa ao português), ZELO,
  CAPACIDADE, INDISPENSÁVEL, ESPECIALMENTE, ANTES DE TUDO, MUITAS VEZES, REAL NECESSIDADE, ADESTRAMENTO DA
  VONTADE, NA MEDIDA EM QUE ELE SE DEDICA, CIÊNCIA, DEDICAÇÃO, TENDÊNCIA À SANTIDADE, SOBRETUDO JUNTO DO
  TABERNÁCULO. Os títulos das nove classes, em versalete no livro e em maiúsculas no texto-fonte, ficaram
  em maiúsculas.
- **Latim.** No corpo, fica em latim e em itálico, sem tradução quando o autor não a dá (*Supra pectus…*,
  *Quasi unus…*, *Haurietis aquas…*, *cymbalum tinniens*, *velut æs sonans*, *Non potestis portare
  modo*, *Panem et Circenses*, *exempla trahunt*, *Declina a malo*, *Fac bonum*, *de statu animarum*,
  *Ascensiones…*, *Regimen animarum*, *Ars artium*, *Vis unitiva*, *compendium*, *Duc in altum*, *ex
  communiter contingentibus*, *Excelsior*, *Per triennium…*, *Hic*, *facti diabolo terribiles*); as
  notas que dão a tradução francesa foram traduzidas. A única nota inteiramente em latim é a 1 (Pio X,
  *Haerent animo*): latim mantido, com `[Trad.: …]` depois da referência, como na Primeira parte.
- **Tratamento nos diálogos.** Nas falas entre pessoas (Timon-David ao jovem padre; o Religioso e a
  Superiora; o prelado ao médico; a réplica «Pouvez-vous citer un fait» dirigida a um interlocutor), o
  *vous* virou «o senhor» / «a senhora», como se fala no Brasil; o guia não prevê o caso (fala do *vous*
  a Deus e do autor ao leitor). A apóstrofe às obras («Œuvres de ce temps…, pourquoi n'avez-vous pas
  régénéré…») ficou em **vós**, porque é o autor que fala: «por que não regenerastes», «não estais
  suficientemente enxertadas», «que vos dirigem».
- **Títulos de padres.** *l'abbé Allemand*, *l'abbé Timon-David* → «o padre Allemand», «o padre
  Timon-David» (guia); *le chanoine* → «o cônego»; *M. Allemand*, *M. Timon-David*, *M. Olier* → «o Sr.
  Allemand», «o Sr. Timon-David», «o Sr. Olier» (o *Monsieur* que o francês dá ao padre secular; é a
  forma das traduções portuguesas de Olier). *le P.* → «o padre»; *Vén. P.* → «venerável padre»; *PP.* e
  *P. P.* → «padres»; *Mgr Gay* → «Dom Gay» (maiúscula por abrir item da lista); *Ma mère*, *mon Père* →
  «minha Madre», «meu Padre».
- **Santos nas notas** em minúscula, por extenso: *S. Aug.* → «santo Agostinho»; *S. Thom.* → «santo
  Tomás»; na lista da nota 11, «são Gregório Magno», «santa Chantal» etc. (com «São Jerônimo» em
  maiúscula por abrir item depois de travessão). *Serm. de S. Joan. Bapt.* fica como abreviatura de obra.
- **Referências bíblicas** no formato do impresso, com os erros dele: «I Reg., XXVII, 45» (a frase de Davi
  é de I Reg./1 Sm 17,45), «Act., 20, 31» em arábicos, «Ps., XXXVI», «Ps. LXXXIII».
- **Pontuação.** Retirado o espaço francês antes de «:», «;», «?» e «!». Algumas frases que o francês fecha
  com ponto, mas que são perguntas («Qui ne voit combien…», «doivent-ils, dès lors, s'étonner…»,
  «Serait-on téméraire…», «Mais pourrait-on excuser…», «Le Pénitent n'est-il pas alors exposé…»)
  ganharam ponto de interrogação, como pede o português. Duas exclamações também: «Combien de pères…»
  e «Sainte révolution dans le monde, si…».

## Termos

| francês | português | observação |
|---|---|---|
| *porte-grâce*; *porte-Christ* | portadora da graça; portadores de Cristo | guia; *porte-grâce* concorda com «eloquência», «palavra» |
| *Répons* | Responsório | ofício de são João |
| *éloquence captivante* | eloquência cativante | |
| *zélateurs* | zeladores | guia |
| *patronage(s)* | patronato(s) | guia |
| *œuvres de jeunesse*; *Œuvre de jeunesse pour les Etudiants et Employés* | obras de juventude; Obra de juventude para os Estudantes e Empregados | |
| *œuvres laïques*; *œuvres postscolaires laïques* | obras laicas; obras pós-escolares laicas | *laïque* no sentido francês de leigo-anticlerical; «laico», não «leigo», que fica para os fiéis (*laïcs* → «leigos») |
| *sujet(s)* | elemento(s); membros; almas; cada um | conforme o contexto: «elementos de elite», «elementos reconhecidos incapazes», «muitos membros só vegetam» (comunidades), «tais almas» (os três últimos estados), «a cada um» (a direção mensal) |
| *« Béquilles »* | «Muletas» | guia; maiúscula onde o autor a põe |
| *élites* | elites | guia |
| *direction (spirituelle)*; *directeur*; *dirigés* | direção (espiritual); diretor; dirigidos | |
| *direction mensuelle*; *direction spirituelle suivie* | direção mensal; direção espiritual regular | |
| *oraison*; *prière* | oração; oração mental | *prière* → «oração»; *oraison* → «oração», ou «oração mental» onde as duas palavras se tocam (nas classes, *Prière. — Fidélité … à l'oraison souvent affective* → «_Oração._ — Fidelidade … à oração mental, muitas vezes afetiva»; no 3° ponto, «_fidelidade à oração mental_») |
| *oraisons jaculatoires* | jaculatórias | guia |
| *examen particulier* | exame particular | guia |
| *dévouement* | dedicação | como na Primeira parte; *dévouements obscurs* → «dedicações obscuras» |
| *rayonnement*; *rayonner* | irradiação; irradiar | guia |
| *tiédeur*; *tièdes*; *attiédie*; *attiédissement* | tibieza; tíbias; amornada; amornamento | |
| *ferveur*; *fervents* | fervor; fervorosos | |
| *demi-advertance* | semiadvertência | termo da moral |
| *union transformante*; *mariage spirituel* | união transformante; matrimônio espiritual | |
| *purifications passives*; *oraison infuse*; *oraison de simplicité* | purificações passivas; oração infusa; oração de simplicidade | |
| as nove classes | ENDURECIMENTO, VERNIZ CRISTÃO, PIEDADE MEDÍOCRE, PIEDADE INTERMITENTE, PIEDADE CONSTANTE, FERVOR, PERFEIÇÃO RELATIVA, HEROICIDADE, SANTIDADE CONSUMADA | *soutenue* → «constante» («sustentada» soa decalque; «sólida» chocaria com *solide piété* da definição da direção) |
| *Croupissement* | estagnação | *croupir*: apodrecer parado |
| *rentrées en soi-même* | retornos a si mesmo | |
| *DRESSAGE DE LA VOLONTÉ*; *dresser* | ADESTRAMENTO DA VONTADE; adestrar | |
| *pieuseté* (entre aspas) | «beatice» | neologismo pejorativo do autor (piedade afetada); «beatice» é a palavra portuguesa para isso |
| *dorlatage* | mimos | *dorloter*: mimar |
| *étude de notaire* | cartório de tabelião | |
| *distributeur automatique* | «distribuidor automático» | |
| *confessional* | confessionário | |
| *Petits Séminaires*; *Grands Séminaires* | Seminários Menores; Seminários Maiores | |
| *lévites* | levitas | |
| *ascétisme*; *mystique* | ascética; mística | as disciplinas |
| *Fête-Dieu* (nota 14) | Corpus Christi | uso brasileiro |
| *Tabernacle* / *tabernacle* | Tabernáculo / tabernáculo | maiúscula onde o autor a põe |
| *Jésus-Hostie*; *l'Hôte divin*; *Divin Prisonnier* | Jesus-Hóstia; o Hóspede divino; Divino Prisioneiro | |
| *communions de parade*; *vrais communiants* | comunhões de aparato; verdadeiros comungantes | |
| *la cité phocéenne* | a cidade foceense | Marselha, fundada pelos foceus |
| *aumônier*; *cercle* | capelão; círculo | como «Círculos católicos» da Primeira parte |
| *sous-officier*; *œil d'adjudant* | suboficial; olho de sargento | |
| *trique*; *mirlitons*; *trombone à coulisse*; *grosse caisse*; *bidon de pétrole* | porrete; mirlitões; trombone de vara; bumbo; lata de querosene | |
| *blouse de jeu et espadrilles* | a blusa de jogo e as alpargatas | |
| *jeu de barres* | o jogo da barra | |
| *bureaucrates* | empregados de escritório | |
| *brebis galeuses* | ovelhas sarnentas | |
| *professeur de lycée* | professor de liceu | |
| *gloriole* | vanglória | |

Nomes: Golias, Davi, Israel; Moisés, o Sinai, os israelitas, os hebreus; Getsêmani, Pretório,
Calvário; Normandia, Marselha, Roma, Ars, Mesnil-Saint-Loup, Japão, Nagasaki; J.-J. Rousseau; santo
Ambrósio, santo Agostinho, são Filipe Néri, santo Atanásio, santo Tomás, são Francisco de Assis, são
Francisco Xavier; Fra Angelico; a Venerável Irmã Teresa do Menino Jesus (guia). Na nota 11, os nomes de
autores e editoras ficam como no impresso (*Aquaviva*, *Lallemand*, *Schrijvers*, *Saudreau*), e as
cidades das editoras também, salvo «Bruxelas».

## Passagens difíceis e leitura adotada

- **«pour que les jeux des *moyens* ne traînent pas»** (Timon-David). *moyens* está em itálico no livro:
  não são «os meios», mas «os médios», a turma intermediária dos patronatos franceses (*petits*,
  *moyens*, *grands*), que o próprio cônego chama logo depois «cette petite jeunesse», em contraste com
  «nos grands jeunes gens». Ficou «os jogos dos _médios_ não esmoreçam».
- **«Changement de refrain dès que le chef d'orchestre donnait le signal de l'exemple».** O regente muda
  de cantiga e os outros o seguem: «assim que o regente dava o sinal com o exemplo».
- **«Comment, par exemple, les soldats viendraient au cercle bien plus nombreux…!»** O condicional
  francês de incredulidade: «Então, por exemplo, os soldados viriam ao círculo em número muito maior…!».
- **«Galette et Cinéma».** *Galette* é bolo (o *panem*) e, na gíria, dinheiro (a «soif de l'or» da mesma
  frase). Ficou «_Grana e Cinema_»: guarda o dinheiro e a gíria; perde o pão. Alternativa, se se
  preferir o pão: «_Pão e Cinema_», perdendo a gíria.
- **«Œuvre profane dirigée par un curé».** *curé* → «vigário», o pároco no Brasil, para guardar a ironia
  do pároco à frente de uma obra profana.
- **«Seuls, exempla trahunt.»** Literalmente «Só [os exemplos], *exempla trahunt*». A frase latina, sem a
  explicitação, ficaria ambígua em português; ficou «Só os exemplos arrastam, _exempla trahunt_», com o
  sentido posto em português antes do latim (acréscimo mínimo, sem colchetes).
- **«Il n'a qu'à laisser parler son expérience et son Cœur»** (fim de d)). O livro imprime *Cœur* com
  maiúscula, mas é o coração do apóstolo (o *son* remete a «L'apôtre»); a maiúscula de reverência
  confundiria com o Coração de Jesus da linha seguinte. Ficou «o seu coração», em minúscula. Ver Dúvidas.
- **«elle disait Notre-Seigneur, Sœur X... avait pu développer…».** O livro tem vírgula onde começa outra
  frase; ficou ponto: «ela _dizia_ Nosso Senhor. A Irmã X... tinha conseguido…».
- **«chauffer à blanc ces âmes».** «Aquecer ao rubro essas almas» (a imagem portuguesa corrente do ferro
  em brasa).
- **«En comparant, sans le mettre suffisamment à point, l'avis…».** *mettre au point* = precisar,
  matizar: «sem o pôr suficientemente nos devidos termos».
- **«Un jour … ce vénéré prêtre était obligé … de nous dire»** e o «Tenez, me dit-il» logo depois: o autor
  passa do *nous* de autor ao *me*; mantido («nos dizer», «disse-me ele»).
- **«Boute-en-train extraordinaire»** → «Animador extraordinário».
- **«les rengaines les plus connues : Un canard déployant ses ailes ; As-tu vu la casquette»**. Cantigas
  populares francesas (a segunda é *As-tu vu la casquette du père Bugeaud?*); os títulos ficam em francês,
  em itálico, como títulos de obras.
- **«Excellente paroisse? Peut-on appeler chrétiens ces gens…»** → «Pode-se chamar cristã essa gente…»
  (concordância com «gente»).
- **«en Dieu … les âmes ont surtout vu par nous le législateur austère»**: «através de nós» (pela imagem
  que os padres deram de Deus), não «por nossa causa».
- **«C'est que, dit saint Athanase, « nous sommes faits dieux par la chair du Christ »».** Aspas do autor
  mantidas; sem referência no livro, nenhuma acrescentada.
- **Nota 1, o latim de Pio X.** *quam oves salutariter audiant* → «que as ovelhas escutem para a sua
  salvação»; *strepit enim diffluitque inanis* → «pois ressoa e se dissipa, vazia».
- **Nota 2.** O francês do autor traduz *Est tantum lucere vanum…* livremente; traduzi o francês dele:
  «Só o brilho é vaidade, só o calor é pouca coisa, o brilho com o calor é a perfeição».
- **Nota 3.** *et que désiré-je sinon qu'il embrase* → «e que desejo eu senão que ele abrase» (o francês
  dá *embraser* intransitivo; o português «abrasar» também o admite).
- **Nota 14.** *Fête-Dieu* → «ofício de Corpus Christi».

## Remissões de página trocadas

- **Nota 5**, «2e partie, chap. II, pag. 56» → «2ª parte, cap. III.» A conversa com Timon-David está no
  cap. 3 da 2ª parte (`02-segunda-parte.txt`, «## 3. Base, Fin et Moyens…», que começa justamente na pág. 56
  do livro: `final/073.txt`). O impresso diz «chap. II», mas o próprio corpo do texto, em e), diz «Au chap.
  III de la 2e partie». Pus o capítulo certo; ver Dúvidas.
- **Nota 11**, «Traités divers de M. Timon-David, indiqués pag. 60» → «indicados na 2ª parte, cap. III
  (nota)». A lista dos tratados (*Méthode de direction des œuvres de jeunesse* etc.) está na nota da pág.
  60, que é a nota `[25]` de `02-segunda-parte.txt`, no cap. 3.
- Ficou como está a remissão externa da nota 1, «(Voir Ami du Clergé, année 1908, page 787)», que é a
  página da revista, não do livro.

## Emendas

- **«ORBE DIFFU-DIT»** (texto-fonte, parágrafo do Responsório): hífen de fim de linha que ficou no meio
  do versalete (no livro, «DIFFU-» no fim da linha, «DIT.» na seguinte). Na tradução, «ORBE DIFFUDIT».
  Convém corrigir também o texto-fonte.
- **«Déclina a malo»** (texto-fonte) → *Declina a malo*: a imagem da pág. 168 mostra «Declina», sem
  acento, como no latim do Salmo. Convém corrigir também o texto-fonte.
- **Vírgula por ponto** em «elle disait Notre-Seigneur, Sœur X...» (ver acima).

## Dúvidas para quem coordena

1. **Nota 5, capítulo da remissão.** O impresso diz «chap. II», o lugar certo é o cap. III (pág. 56, e o
   próprio texto, em e), diz «chap. III»). Pus «2ª parte, cap. III». Se se preferir seguir o impresso à
   letra, ficaria «2ª parte, cap. II», que leva o leitor ao lugar errado.
2. **«son Cœur»** do apóstolo, com maiúscula no livro (fim de d)). Pus minúscula. Se se quiser a maiúscula
   do impresso, basta trocar «o seu coração» por «o seu Coração».
3. **«Galette et Cinéma» → «Grana e Cinema».** Proposta alternativa: «Pão e Cinema» (ver acima).
4. **«M.» → «o Sr.»** para padres seculares (Allemand, Timon-David, Olier). Se o guia preferir outra
   forma («o padre»), é troca simples; convém fixá-la no CONVENCOES, porque Olier e outros voltam na 5ª
   parte.
5. **Correções do texto-fonte** (fora do meu escopo; não toquei no original): «DIFFU-DIT» → «DIFFUDIT» e
   «Déclina» → «Declina».
6. **Propostas para o guia (não alterado):** registrar *vous* entre personagens → «o senhor» / «a
   senhora»; *sujet(s)* → «elemento(s)» / «membro(s)»; *pieuseté* → «beatice»; os nomes das nove classes
   de almas (para a 5ª parte, que volta a eles); *Fête-Dieu* → «Corpus Christi»; o negrito do livro
   marcado com `**…**`.
