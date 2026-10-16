# Verso livre: cantos III a VII (versos 115–455)

Continuação do teste em verso livre, pelo método de `notas.md` (cantos I e II): um verso português para
cada verso do original (Harrison e Sharp, 4.ª ed.), na mesma ordem, sem tabulação de cesura e sem imitar
a medida aliterativa. Nomes, termos, fórmulas e tratamento seguem `../CONVENCOES.md` (§§ 3–6, 8 e 9); o
§ 2 ficou de lado. Para nomes que o guia não traz, a forma de `../traducao/` (só consulta).

Arquivos: `03.txt` (74 versos, 115–188), `04.txt` (69, 189–257), `05.txt` (62, 258–319), `06.txt`
(51, 320–370), `07.txt` (85, 371–455).

## 1. Método

1. Para cada verso, o original com o glossário de Harrison e Sharp (um script listava, para cada número
   de verso, todos os verbetes do glossário que o citam) e as notas da edição; conferência com Hall
   (seções III–VII, mesma numeração), Gummere e, onde foi preciso, Morris e Wyatt e os dicionários.
   Nada foi copiado dessas versões nem da tradução aliterativa de `../traducao/`.
2. Rascunho verso a verso, canto por canto.
3. Ritmo: `verso-livre.mjs` sobre uma cópia com as `# troca` aplicadas, `molde.mjs` com molde livre
   (`*`) e as mesmas trocas; visão compacta (esqueleto e intervalos por verso); uma busca de três vogais
   iguais seguidas entre palavras (_soava a harpa_). Duas passadas de reescrita (§ 4).
4. Revisão de sentido de todo o lote, verso a verso, contra o original, Hall, Gummere e o glossário.
5. Crítica independente (§ 5) e conferência de cada correção aceita no `verso-livre.mjs`.

Trocas acrescentadas às de `notas.md`: Hygelac => Hígelac, Ecgtheow => Éjtiou, Wulfgar => Vúlfgar,
Hrethel => Hrétel, Weland => Vêland, hrethmen => hrétmen, wederas => véderas.

## 2. Escolhas gerais

- **Verso a verso.** Onde a sintaxe pediu, uma palavra passou ao verso vizinho dentro da mesma frase:
  v. 199–200 (_sēcean wolde_ → «buscaria», no v. 199, depois da crítica); v. 283–284 (_þolað_
  → «sofrerá», no v. 284, como no original); v. 312–313 (_hof mōdigra / torht getǣhte_ → «a corte dos
  bravos, / resplandecente, lhes mostrou»); v. 350–351 («Eu ao amigo / dos dinamarqueses»: o genitivo
  passou ao verso seguinte, ver § 4); v. 379–380 (_þrīttiges_ → «a força / de trinta homens»);
  v. 443–444 (_etan_ → «devorar», no v. 443, para não deixar dúvida de quem come, § 5).
- **Aposições** no lugar: «o filho de Healfdene, / o protetor do povo» (268–269); «junto ao glorioso, /
  ao senhor dos dinamarqueses» (270–271); «a nau recém-calafetada» (295, aposta a «o vosso barco»);
  «a madeira de colo curvo» (298); «ao amigo / dos dinamarqueses, ao senhor dos Scyldings, … / ao doador
  de anéis, … / ao senhor famoso» (350–353); «com o temível» (425); «proteção dos Scyldings» (428);
  «amparo dos guerreiros, / senhor amigo do povo» (429–430); «este bando aguerrido» (432); «broquel
  amarelo» (438); «o meu senhor, de ânimo propício» (436); «o melhor dos trajes» (454).
- **Kennings e compostos** (a imagem, não a explicação): _ȳð-lida_ → viajante das ondas (198); _swan-rād_
  → caminho do cisne (200); _sund-wudu_ → madeira das águas (208); _sǣ-wudu_ → madeira do mar (226);
  _wunden-stefna_ → a proa recurva (220, sem acrescentar «navio»); _fāmig-heals_ → de colo de espuma
  (218); _wunden-hals_ → de colo curvo (298); _lagu-strǣt_ → estrada das águas (239); _mægen-wudu_ →
  madeira da força (236); _lind-hæbbende_ → os que portam a tília (245); _word-hord_ → tesouro de
  palavras (259); _cear-wylmas_ → ondas da angústia (282); _hilde-rǣs_ → tormenta da batalha (300);
  _ān-genga_ → «que anda sozinho» (165 e 449, a mesma imagem nos dois lugares); _gāst-bona_ → matador
  de almas (177); _dēað-scūa_ → sombra da morte (160); _hel-rūnan_ → feiticeiros do inferno (163, o
  glossário: _sorcerer_); _gif-stōl_ → trono das dádivas (168); _here-grīma_ → máscaras de batalha
  (396); _grīm-helmas_ → elmos de viseira (334); _searo-net_ → rede de arnês (406); _īren-þrēat_ → tropa
  de ferro (330); _æsc-holt_ → hastes de freixo (330); _wæl-sceaft_ → hastes de morte (398); _mōr-hopu_
  → refúgios do pântano (450).
- **_-geatwe_** (equipamento) → «aprestos»: _gryre-geatwe_ → aprestos de terror (324); _wīg-geatwe_,
  _gūð-geatwe_ → aprestos de guerra (368, 395). _searo_ fica «arnês» (guia), _byrne_ «cota» ou «cota de
  malha», _rand_ «broquel» (231, 326, 438), _bord_, _scyld_ «escudo».
- **Nomes de Deus**: o Criador (_metod_, 169 e 180, isolado), o juiz dos feitos (181), o Senhor Deus (181),
  o elmo dos céus (182), o Soberano da glória (183), o Senhor (187, 441), o Pai (188), Deus (227), o
  santo Deus (381), o Pai, Soberano de tudo (_fæder alwalda_, 316, como em `../traducao/`). Pronome em
  minúscula («cujo amor», 169).
- **Fórmulas do guia**: «O vigia falou» (286); «Wulfgar falou» (348, 360); «Hrothgar falou, o elmo dos
  Scyldings» (371); «Beowulf falou» (405); «rijo sob o elmo» (_heard under helme_, 342 e 404, como em
  `../traducao/`); «o amigo dos Scyldings» (148, 170); «o vassalo de Hygelac» (194); «proteção dos
  Scyldings» (428); «senhor amigo do povo» (430); «a melhor das casas» (_hūsa sēlest_, 146 e 285, sempre
  igual); a fórmula _wæs þæt gewin tō strang/swȳð, lāð and longsum_ (133–134 e 191–192) → «era dura /
  forte demais a aflição, / odiosa e longa», igual nos dois lugares.
- **Tratamento**: o vigia trata os geatas por vós; Beowulf trata o vigia e Hrothgar por tu; Wulfgar trata
  Beowulf e Hrothgar por tu, os geatas por vós.
- **Falas**: nenhuma atravessa os limites do lote (o v. 114, último de `02.txt`, é narração; o v. 456,
  primeiro de `08.txt`, abre uma fala nova de Hrothgar). Falas: 237–257 (o vigia), 260–285 (Beowulf),
  287–300 (o vigia, abre no meio do verso), 316–319 (o vigia), 333–339 (Wulfgar), 342–347 (Beowulf,
  abre no meio do verso), 350–355 (Wulfgar), 361–370 (Wulfgar a Hrothgar), 372–389 (Hrothgar, fecha no
  meio do verso), 391–398 (Wulfgar), 407–455 (Beowulf).

## 3. Passagens revistas (sentido)

| verso | original | leitura adotada | apoio |
|---|---|---|---|
| 117 | _gebūn hæfdon_ | «a tinham ocupado» (feito ali as suas camas) | glossário (_gebūan_) |
| 120 | _Wiht unhǣlo_ | «O ser da ruína» | glossário: _the demon of destruction_ |
| 128 | _æfter wiste_ | «depois daquela ceia»: a refeição de Grendel (os trinta vassalos) | glossário (_wist_, 2); Gummere entende «depois do banquete» dos dinamarqueses |
| 131 | _þolode þrȳð-swȳð_ | «sofria dor imensa»: _þrȳð-swȳð_ substantivo, objeto de _þolode_ | glossário: _great pain_ (?); a outra leitura do glossário (adjetivo, «o muito poderoso») é a de `../traducao/` e de Hall |
| 136 | _nō mearn fore_ | «e não recuou / diante da vingança e do crime» | glossário (_murnan_ 1: _to shrink from_) |
| 142 | _heal-þegnes hete_ | «o ódio do vassalo do salão» (Grendel, que ocupa o salão) | glossário; B. lê _hel-þegnes_ (nota ao v. 142) |
| 147 | _torn_ | «o tormento» | glossário: _distress_ |
| 154–156 | _sibbe ne wolde … feorh-bealo feorran, fēo þingian_ | «não quis, por amizade, / livrar nenhum dos homens … / do mal mortal, nem compensá-lo com bens» | glossário (_sib_: instr., _in peace_?; _feorran_: _would not from friendship free_); B. toma _sibbe_ como objeto («não quis paz», nota ao v. 154) |
| 158 | _beorhtre bōte_ | «compensação brilhante» | glossário (_bōt_ 2: satisfação, tributo; _beorht_ 2: notável) |
| 161 | _seomade and syrede_ | «prendia em laços, armava ciladas» | glossário: _entrap_ |
| 168–169 | _nō hē þone gif-stōl grētan mōste, māððum for metode, nē his myne wisse_ | «não podia ele tocar o trono das dádivas, / a joia, por causa do Criador, cujo amor não conhecia» | glossário (_myne_: _whose [God's] love he knew not_); Wülker (nota): «nem tinha desejo disso». Passagem disputada; o «cujo» deixa claro que o amor é o do Criador, como no glossário |
| 171–172 | _Monig-oft gesæt rīce tō rūne_ | «Muitas vezes se sentava / o rei com o conselho» | glossário (_rīce_ 2: _the king with his chosen advisers_; _gesittan_) |
| 175–176 | _hærg-trafum_, _wīg-weorðunga_ | «nas tendas dos deuses», «sacrifícios aos ídolos» | glossário |
| 184 | _þurh slīðne nīð_ | «por cruel hostilidade» | glossário (_through fierce hostility, heathenism_) |
| 186 | _wihte gewendan_ | «nem mudança alguma» (a sorte não muda) | glossário |
| 189 | _mǣl-ceare_ | «na aflição sem fim» (instrumental) | nota ao v. 189: H.-So. o toma como acusativo, outros como instrumental; a frase portuguesa pede o instrumental |
| 194 | _fram hām_ | «em casa» | glossário e nota ao v. 194 |
| 204 | _hǣl scēawedon_ | «viram presságios favoráveis» | glossário: _observed favorable signs_ |
| 207 | _fīftȳna sum_ | «ele, um de quinze» (com mais catorze) | glossário |
| 210 | _Fyrst forð gewāt_ | «Passou o tempo» (o da ida ao porto) | glossário |
| 219 | _ymb ān-tīd ōðres dōgores_ | «no dia seguinte, à mesma hora» | glossário e nota ao v. 219 |
| 223–224 | _þā wæs sund liden, eoletes æt ende_ | «estava cruzado o mar, / no termo das águas» | glossário (_eolet_: _sea_?) e nota ao v. 224 (_sea_ ou _fjord_); a outra leitura, «viagem», daria «chegara ao fim a travessia» |
| 229 | _of wealle_ | «do alto da costa» | glossário (_weal_ 2: _elevated sea-shore_) |
| 238 | _brontne cēol_ | «a quilha espumante» | glossário (_brant_: _foaming, going-high_) |
| 240 | _helmas bǣron_ | «e trouxestes os elmos?» | texto da edição (conjectura de H.-So.); W. lê _hringed-stefnan_ (nota ao v. 240) |
| 241 | _Ic wæs ende-sǣta, ǣg-wearde hēold_ | «Tenho sido o guarda da fronteira, vigiei a costa» | glossário (_I have hitherto kept watch on the sea_) |
| 244 | _cūðlīcor_ | «mais às claras» | glossário: _more openly_ (o vigia pensa nos desembarques às escondidas) |
| 249 | _seld-guma_ | «homem comum» | glossário (_common man?_); nota ao v. 249 |
| 253 | _lēase scēaweras_ | «falsos espiões» | glossário (_lēas_: _false_); a nota dá «soltos, errantes» |
| 258 | _se yldesta_ | «o mais honrado de todos» | glossário e nota ao v. 258 (_the most respected_, não «o mais velho») |
| 263 | _ord-fruma_ | «alto príncipe» | glossário: _head lord, high prince_ (não «da vanguarda») |
| 269 | _wes þū ūs lārena gōd_ | «sê bom para nós com teu conselho» | glossário |
| 275 | _dǣd-hata_ | «um perseguidor» | glossário e nota ao v. 275 |
| 278 | _þurh rūmne sefan_ | «de ânimo generoso» | glossário (_rūm_ 2: _magnanimous_) |
| 280–281 | _gyf him ed-wendan ǣfre scolde bealuwa bisigu_ | «se algum dia tiver de cessar para ele / o tormento dos males» | glossário (_edwendan_ verbo); B. o toma como substantivo (nota ao v. 280), sem mudar o sentido |
| 299–300 | _Gūð-fremmendra swylcum gifeðe bið …_ | «A um tal guerreiro há de ser dado pelo fado / sair ileso da tormenta da batalha» | glossário; guia, § 9 (_gifeðe_ → fado) |
| 303–305 | _eofor-līc … ferh wearde hēold_ | «figuras de javali … o varrão fazia a guarda» | glossário (_ferh_: _hog, boar_); B. e t. Br. leem _ferh-wearde_ (nota ao v. 305) |
| 306 | _Gūðmōde grummon_ | «Ansiosos de combate, apressaram-se» | glossário (_grimman_: _to hasten_) |
| 312–313 | _hof mōdigra torht_ | «a corte dos bravos, / resplandecente» (a morada dos dinamarqueses) | glossário |
| 320 | _stān-fāh_ | «de pedras de cores» | glossário: _paved with stones of different colors_ |
| 322–323 | _hring-īren scīr song in searwum_ | «o ferro dos anéis, luzente, / cantava na armadura» | texto da edição; S. faz de _hring-īren_ aposto de _gūð-byrne_ (nota ao v. 322) |
| 327 | _bugon þā tō bence_ | «e foram sentar-se no banco» | glossário (_būgan_) |
| 332 | _æfter æðelum frægn_ | «indagou … a nobre linhagem» | glossário (_æðelu_: _noble lineage_; o manuscrito traz _hǣleþum_) |
| 336 | _ār and ombiht_ | «mensageiro e servidor» | glossário |
| 348 | _Wendla lēod_ | «um príncipe dos vândalos» | glossário (_lēod_: _prince_); guia, § 4 |
| 353 | _ymb þīnne sīð_ | «acerca da tua vinda» | nota ao v. 353 (_arrival_) |
| 357 | _unhār_ | «muito grisalho» | glossário; Grein: «calvo» (nota ao v. 357) |
| 359 | _cūðe hē duguðe þēaw_ | «sabia o uso da nobreza» | glossário (_the custom of the distinguished courtiers_) |
| 367 | _glædnian_ | «o prazer das tuas respostas» | texto da edição (Thorkelin); o manuscrito e H.-So. leem _glædman_ (nota ao v. 367) |
| 373 | _eald-fæder_ | «O seu velho pai» | o glossário dá «avô, antepassado», mas a nota ao v. 373 mostra que é o pai, com _eald_ honorífico |
| 378–379 | _gif-sceattas Gēata … þyder tō þance_ | «presentes para os geatas / até lá, em sinal de amizade» | glossário (_tribute for the G[eats]_; _þanc_ 3: _favor_); Th. e B. emendam para _Gēatum_ (nota ao v. 378), com o mesmo sentido |
| 386–387 | _hāt hig in gān, sēon sibbe-gedriht_ | «manda-os entrar, / ver a tropa de parentes, toda reunida» | glossário (_sibbe-gedriht_: os dinamarqueses); a nota ao v. 387 o faz sujeito de _sēon_; o português guarda a ambiguidade |
| 390 | _word inne ābēad_ | «e de dentro deu o recado» | glossário: falou de dentro, à porta do salão |
| 399 | _se rīca_ | «o poderoso» (Beowulf) | glossário |
| 404 | _on heoðe_ | «no interior» | glossário |
| 414 | _under heofenes hādor_ | «sob o brilho do céu» | glossário; Grein: _receptaculum_ (nota ao v. 414) |
| 419–420 | _þā ic of searwum cwōm, fāh from fēondum, þǣr ic fīfe geband_ | «quando eu vim dos combates, / tinto de sangue inimigo, onde amarrei cinco» | glossário (_searo_ 2; _fīfe_ (?)); B. lê _fīfelgeban_ (nota aos vv. 420–421) |
| 423 | _wræc Wedera nīð (wēan āhsodon)_ | «vinguei a afronta aos wederas (tinham sofrido males)» | glossário (_enmity against the W._) |
| 425–426 | _āna gehegan þing wið þyrse_ | «devo sozinho decidir / a questão contra o ogro» | glossário (_þing gehegan_: abrir o tribunal; a luta como assembleia) |
| 433 | _geāhsod_ | «Soube também, perguntando» | glossário: _to find out by inquiring_ |
| 444 | _etan unforhte_ | «devorar … / sem medo» (advérbio) | nota ao v. 444 (B., Gr., Ha.); Kl. lê _anforhte_ |
| 445 | _mægen Hrēðmanna_ | «a flor dos hrethmen» | glossário (_mægen_ 2: _prime, flower_) |
| 446 | _hafalan hȳdan_ | «cobrir-me a cabeça» (sepultar) | nota ao v. 446 (Th.); H.-So. pensa numa guarda de honra |
| 448 | _byrgean þenceð_ | «pensa no banquete» | glossário (_byrgan_: _to feast_) |
| 450 | _mearcað mōr-hopu_ | «mancha os refúgios do pântano» (com o sangue) | glossário |
| 451 | _līces feorme_ | «o sustento do meu corpo» | glossário e nota ao v. 451 |
| 452 | _gif mec hild nime_ | «se a batalha me levar» (sem personificar) | nota ao v. 452 (Rönning personifica _Hild_) |
| 455 | _Gǣð ā Wyrd swā hīo scel!_ | «Vai sempre o destino como tem de ir!» | guia, §§ 3 e 9 (_wyrd_ → o destino, minúscula) |

## 4. Ritmo: o que o Versificador mostrou e o que mudou

Metas de `notas.md`, § 4: 2,4–2,8 sílabas por acento; nenhum verso marcado; no máximo uns 20% de versos
com 4 átonas seguidas; nada de três vogais iguais seguidas; não repetir o mesmo esqueleto em versos
vizinhos.

**Primeiro rascunho**: 36 versos marcados no lote (III 6, IV 7, V 7, VI 7, VII 9), quase todos `ralo`
ou `vazio`; 4+ átonas seguidas em até 23% dos versos (III) e 22% (VII); ternário de 40% a 42%. (Essas
primeiras medidas saíram sem as `# troca`, por um erro no script que as aplicava à cópia; corrigido o
script, tudo foi medido de novo com elas, e os números do fim são esses.)

O caso que mais se repetiu foi o de **«dinamarqueses»**: depois de uma paroxítona, «… dos
dinamarqueses» dá cinco átonas seguidas (_a-mi-go-dos-di-na-mar-QUE-ses_), e o verso sai `vazio`.
Soluções, sem mudar o termo do guia: o adjetivo «dinamarquesa/dinamarquês», que deixa só quatro (242,
253, 389); uma oxítona antes («senhor dos dinamarqueses», 271, 359, 427); ou passar o genitivo ao
verso seguinte dentro da frase (350–351).

Reescritas principais (antes → depois):

| verso | antes | depois | por quê |
|---|---|---|---|
| 116 | a ver como os dinamarqueses dos anéis | a ver de que modo os dinamarqueses dos anéis | `vazio` (6 átonas: «como» fica átono) |
| 120 | a desventura dos homens. A criatura da perdição, | a desgraça dos homens. O ser da ruína, | `ralo` (4 acentos em 16 sílabas); o glossário dá _demon of destruction_ |
| 125 | com aquela fartura de mortos, a buscar a morada. | levando a fartura de mortos, rumo à morada. | `ralo`, `vazio` (5 átonas no começo) |
| 129 | um grande clamor da manhã. O senhor glorioso, | grande clamor da manhã. O ilustre senhor, | 3-3-3-3 seguido |
| 139 | um repouso mais afastado, | fosse buscar repouso mais folgado, | `ralo` (2 acentos em 8 sílabas) |
| 143 | mais longe e mais seguro quem escapou ao inimigo. | mais longe e mais firme quem fugiu do inimigo. | `ralo` |
| 147 | doze invernos inteiros sofreu o tormento | durante doze invernos sofreu o tormento | 3-3-3-3 |
| 164 | o inimigo da humanidade | o inimigo do gênero humano | vão de 5 átonas |
| 176 | sacrifícios aos ídolos, e pediam com palavras | sacrifícios aos ídolos, e em palavras pediam | `ralo` |
| 197 | naqueles dias desta vida, | nos dias de então, nesta vida, | `ralo` (2 acentos em 8 sílabas) |
| 238–239 | protegidos por cotas de malha … / pela estrada das águas viestes assim conduzindo | vestidos de malha, que assim a quilha espumante / viestes guiando pela estrada das águas | o mesmo esqueleto 3-6-9-12-15 em dois versos seguidos |
| 242 | para que na terra dos dinamarqueses nenhum inimigo | a fim de que nenhum inimigo, em terra dinamarquesa, | `ralo`, `vazio` |
| 247 | nem o consentimento dos parentes. | nem a aprovação dos parentes. | `vazio` |
| 261 | e companheiros da lareira de Hygelac. | e de Hygelac somos companheiros da lareira. | `ralo` |
| 263 | príncipe nobre e eminente | alto príncipe nobre | três vogais iguais (_nobre e eminente_); e o glossário dá _high prince_ |
| 265–266 | velho, da sua morada; dele se lembram bem / todos os sábios | velho, dos seus lares; bem se lembra dele / cada um dos sábios | `vazio`; e o singular de _wēl-hwylc_ |
| 270 | Temos para o glorioso uma grande missão, | Temos grande missão junto ao glorioso, | `vazio` |
| 309 | era, para os habitantes da terra, o mais famoso | era o mais famoso entre os que vivem na terra, | `vazio` |
| 313 | resplandecente, lhes mostrou, para que pudessem | radiante, lhes mostrou, de modo que pudessem | `ralo` |
| 319 | para vigiar contra a tropa inimiga. | e montar guarda contra a hoste inimiga. | `ralo` |
| 332 | perguntou aos guerreiros pela sua linhagem: | indagou dos guerreiros a nobre linhagem: | `ralo`, `vazio`; «nobre» devolve _æðelum_ |
| 347 | que o possamos saudar, a ele que é tão bom. | que possamos saudar quem é tão bom. | `choques` |
| 350–351 | Eu ao amigo dos dinamarqueses, / ao senhor dos Scyldings, vou perguntar, | Eu ao amigo / dos dinamarqueses, ao senhor dos Scyldings, vou perguntar, | `vazio` |
| 359 | conhecia o costume dos veteranos. | sabia o uso da nobreza. | `ralo`; e o glossário (_duguðe þēaw_) |
| 367 | alegrá-los com as tuas respostas, Hrothgar! | Hrothgar, o prazer das tuas respostas! | `ralo`, `vazio` |
| 382 | para nos socorrer nos enviou, | nos mandou, para nos dar socorro, | `ralo`, `vazio` |
| 385 | pela sua ousadia hei de oferecer tesouros. | pelo seu ânimo ousado hei de dar tesouros. | `vazio` |
| 411 | dizem os navegantes que este salão fica, | contam os homens do mar que este salão fica, | `vazio` |
| 418 | porque conheciam a força do meu vigor: | porque sabiam quanto podia a minha força: | `ralo` |
| 434 | na sua temeridade não faz caso das armas; | por ser temerário, das armas não faz caso; | `vazio` |
| 448–450 | levará … pensará em comê-lo, / o solitário o devorará sem piedade, / manchará … | leva … pensa no banquete, / come-o sem pena aquele que anda sozinho, / mancha … | `ralo`; o presente do original (_byreð, þenceð, eteð, mearcað_); a imagem de _ān-genga_ |
| 455 | Vai sempre o destino como deve ir! | Vai sempre o destino como tem de ir! | `choques` |

Segunda passada (canto VII): 4+ átonas seguidas em 20% dos versos, no limite. Encurtei os vãos em
palavras curtas, sem tocar no sentido: «no aperto da mão» (380), «Podeis agora entrar, nos aprestos de
guerra» (395), «conforme o bravo ordenou» (401), «quando eu vim dos combates» (419), «tinto de sangue
inimigo» (420), «amparo dos guerreiros» (429), «com a tropa dos meus nobres» (431), «purgar Heorot»
(432), «Soube também, perguntando» (433), «hostil contra hostil» (440), «cobrir-me a cabeça» (446),
«que o peito me guarda» (453). Resultado: 7%.

Outras: «o mar contra o areal» (213; _contra a areia_ dava três _a_); «o guerreiro os guiava» (402;
_enquanto o homem_ dava três _o_); «sozinho contra todos» (145) e «Exaustos do mar, puseram os escudos
largos» (325), «Deu-lhe resposta então» (340), para quebrar séries ternárias.

**Resultado final** (`verso-livre.mjs`, com as `# troca`):

| | III | IV | V | VI | VII | lote | meta |
|---|---|---|---|---|---|---|---|
| versos | 74 | 69 | 62 | 51 | 85 | 341 | = original |
| média de sílabas | 12,9 | 12,8 | 12,5 | 12,5 | 12,6 | 12,7 | |
| sílabas por acento | 2,63 | 2,64 | 2,62 | 2,65 | 2,61 | 2,63 | 2,4–2,8 |
| intervalos 1 / 2 / 3 / 4 / 5+ (%) | 9,0 / 30,7 / 40,0 / 19,0 / 1,4 | 5,3 / 36,1 / 41,0 / 15,0 / 2,6 | 12,4 / 32,1 / 34,2 / 17,9 / 3,4 | 9,0 / 30,2 / 40,7 / 17,5 / 2,6 | 10,2 / 31,2 / 37,7 / 18,8 / 2,2 | 9,1 / 32,1 / 38,7 / 17,7 / 2,4 | ~15 / 30 / 29 / 16 / 5 |
| versos com 4+ átonas seguidas | 5,4% | 10,1% | 12,9% | 9,8% | 7,1% | 8,8% | até ~20% |
| versos que terminam em pontuação | 70,3% | 71,0% | 72,6% | 72,5% | 74,1% | 72,1% | 65–100% |
| âncoras métricas | 10 | 9 | 19 | 11 | 15 | 64 | uma ou duas a cada 6–8 versos |
| versos marcados (`ralo`, `vazio`, `choques`) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

`molde.mjs` (molde livre, `*`, com as `# troca`), nos cinco cantos: nenhum ✗, nenhum ≠, nenhuma
«leitura natural tem». Nenhum par de versos vizinhos com o mesmo esqueleto.

O que fica fora da meta, de propósito: como nos cantos I e II, o ternário passa um pouco dos 38% em
III, IV e VI (paroxítonas de três sílabas com artigo: _o vassalo_, _a madeira_, _os guerreiros_), e o
choque fica abaixo da média dos mestres; num relato solene ele ficou onde a fala o pede (_muitas
vezes_, _bom rei_, _Vai sempre_).

## 5. Crítica

Um crítico (Sonnet, esforço médio, num subagente) conferiu os 341 versos com o original, Hall, Gummere,
o guia e o glossário de Harrison e Sharp, sem comentar o ritmo e sem editar. Confirmou, pelo glossário,
leituras que pareciam suspeitas (_ellen-rōf_, _ferh_, _brontne_, _hǣl_, _āhsodon_, _þrȳðlīc_, _heoðe_,
_hel-rūnan_, _myne_, _tō þance_). Apontou 11 itens; aceitos 10 (dois só em parte), cada um conferido
de novo no `verso-livre.mjs` (nenhum verso marcado depois):

- 443–444, ambiguidade de quem come quem («a gente dos geatas / comer sem medo») → «no salão da guerra
  devorar a gente dos geatas / sem medo, como fez muitas vezes» (_etan_ volta ao v. 443; aceito, pois a
  ordem do original ali enganava em português).
- 399, «o poderoso» podia ser lido como Hrothgar → «o poderoso geata» (o crítico propunha o nome; o
  glossário dá _se rīca_ = Beowulf, e «geata» basta, sem acrescentar o nome).
- 156, «pagar por ele um tributo» (referente incerto) → «nem compensá-lo com bens» (glossário: _compound
  the life-bale for money_). Recusei «preço de sangue»: o original não tem _wergild_ aqui.
- 143, «mais firme» → «mais a salvo» (glossário: _more secure_).
- 184–185, regência → «empurrar a alma / para o abraço do fogo».
- 199–201, «o rei da guerra / ele iria buscar» (o «ele» podia ser o rei) → «disse que buscaria o rei da
  guerra / pelo caminho do cisne, o senhor glorioso, / que tinha falta de homens» (_sēcean_ sobe ao
  v. 199; o v. 199 ficou com 18 sílabas).
- 169, «o amor dele» (podia ser o de Grendel) → «cujo amor não conhecia». Recusado «d'Ele»: o guia manda
  o pronome de Deus em minúscula.
- 137, «preso demais a eles» → «a isso».
- 435, «pois» → «então» (_þonne_). Recusada a troca de «assim me seja Hygelac … propício»: é a fórmula
  optativa portuguesa (como «assim Deus me ajude») e traduz _swā mē Higelāc sīe … mōdes blīðe_ ao pé da
  letra.
- 387, «ver» solto → «e ver a tropa de parentes».
- 426, «Por isso» (causa acrescentada) → «Agora, pois, a ti» (_nū þā_).

## 6. Nomes e termos novos (fora do guia)

- **Weland** (_Wēlandes_, 455), o ferreiro lendário; **hrethmen** (_Hrēðmanna_, 445), os dinamarqueses,
  em minúscula como povo: as formas de `../traducao/`.
- **Hrethel** para _Hrēðel_ (374) e _Hrēðlan_ (454), uma forma só.
- _Weder-mearc_ (298) → «a marca dos wederas»; _Wendla lēod_ (348) → «um príncipe dos vândalos».
- _ombeht_ (o vigia, 287) e _ombiht_ (Wulfgar, 336) → «servidor»; _ār_ (336) → «mensageiro».
- _ān-genga_ (165, 449) → «que anda sozinho» (a imagem; `../traducao/` tem «solitário»).
- _-geatwe_ → «aprestos» (_gryre-, wīg-, gūð-geatwe_); _here-grīma_ → «máscaras de batalha»;
  _grīm-helm_ → «elmos de viseira»; _ferh_ (o javali do elmo) → «varrão», para distinguir de _eofor-līc_
  → «figuras de javali».
- _hel-rūnan_ → «feiticeiros do inferno»; _gāst-bona_ → «matador de almas»; _heal-þegn_ → «vassalo do
  salão».
- _sund-wudu_ → «madeira das águas», _sǣ-wudu_ → «madeira do mar» (o guia só traz o segundo).

## 7. Propostas para o guia

1. § 4 ou § 5: dizer que «dos dinamarqueses» pode virar «dinamarquês/dinamarquesa» (_on land Dena_ → «em
   terra dinamarquesa») quando o verso livre sai com cinco átonas seguidas; e que o genitivo pode passar
   ao verso seguinte dentro da mesma frase (350–351).
2. § 5: _-geatwe_ → «aprestos»; _rand_ → «broquel»; _ān-genga_ → «o que anda sozinho».
3. § 3 (fórmulas): _heard under helme_ → «rijo sob o elmo»; _hūsa sēlest_ → «a melhor das casas».

## 8. Conferência

- Versos: 74, 69, 62, 51 e 85, como o original; sem tabulação; sem linha em branco no meio.
- Grep de mesóclise: nada.
- Aspas: conferidas fala por fala (§ 2).
- Cabeçalho igual ao de `../traducao/` (`# canto`, `# titulo`, títulos do § 8 do guia).
