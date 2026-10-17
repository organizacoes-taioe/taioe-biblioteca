# Verso livre: cantos XXXV a XXXVIII (versos 2461–2821)

Mesmo método dos cantos I e II (`notas.md`): do inglês antigo de Harrison e Sharp, um verso português
para cada verso do original, sem tabulação, sem imitar a medida aliterativa. Nomes, termos, fórmulas e
tratamento seguem `../CONVENCOES.md` (§§ 3–6 e 9); onde o guia é omisso, a forma de `../traducao-aliterativa/`
(só consultada).

## 1. Método

1. Leitura do original com o glossário e as notas de Harrison e Sharp. Um script listou, para cada
   verso de 2461 a 2821, todas as entradas do glossário que o citam, com o sentido dado ali; as
   passagens disputadas (§ 3) foram decididas por essa lista, pelas notas (linhas 6180–6340 da edição) e
   pela lista de nomes da edição. Conferência com Hall (seções XXXV–XXXVIII), Gummere (seções
   deslocadas: o nosso XXXV é o fim do XXXIII dele) e Morris e Wyatt.
2. Rascunho verso a verso.
3. Ritmo: `verso-livre.mjs` numa cópia com as `# troca`, visão compacta (um verso por linha, com
   esqueleto e intervalos) e `molde.mjs` em molde livre; mais um script que acusa esqueletos iguais em
   versos vizinhos, 2-5-8-11 seguidos, três vogais seguidas, tabulação, mesóclise e aspas.
4. Revisão de sentido verso a verso (§ 3) e crítica independente (§ 6).

## 2. Escolhas gerais

- **Fala que atravessa seções.** A fala de Beowulf começa no canto XXXIV (2426) e termina em 2510: as
  aspas reabrem no primeiro verso do 35 («“Recolhe-se então ao leito») e fecham em 2510; o 34 (outro
  lote) já fecha as aspas no último verso. O 38 termina fora de fala (2818–2821, narração), e o 39 não
  continua nenhuma fala do 38. Nenhuma pendência de aspas com outros lotes.
- **Fórmulas**: «Beowulf falou» (2511, 2725, 2793); «Wiglaf falou, muitas palavras justas,» (2632, a
  fórmula de `traducao-aliterativa/` para _Wīglāf maðelode word-rihta fela_); «ouvi dizer» (_ic gefrægn_: 2485,
  2695, 2753, 2774); «pelo que ouvi» (_mīne gefrǣge_, 2686); «tal deve ser o varão» (_swylc sceolde secg
  wesan_, 2709).
- **Tratamento**: tu entre Wiglaf e Beowulf e de Beowulf a Wiglaf (2664–2669, 2744–2748, 2814); vós aos
  companheiros (2530–2538, 2801–2803); dual _unc_, _uncer twēga_ → «nós dois», «de nós dois» (2527,
  2533); _ūrum … bām_ → «nossos … de ambos» (2660–2661).
- **Deus**: _metod manna gehwæs_ → o Criador de cada homem (2528, aposto a _Wyrd_, como em `traducao-aliterativa/`);
  _god_ → Deus (2651); _waldend fīra_ → o Soberano dos homens (2742); _frēa ealles_ → o Senhor de tudo
  (2795); _wuldur-cyning_ → o Rei da glória (2796); _ēce dryhten_ → o Senhor eterno (2797);
  _metod-sceaft_ → decreto do Criador (2816, guia); _godes lēoht_ → a luz de Deus (2470). _Wyrd_ → o
  destino, minúscula (2527, 2575, 2815); _gifeðe_ → o fado (2492, 2683, 2731; guia § 9).
- **Termos do guia**: _āglǣca_ → o temível, também no plural para Beowulf e o dragão, «os dois temíveis»
  (2521, 2535, 2558, 2593); _wyrm_ → serpe; _draca_ → dragão; _fȳr-draca_ → dragão de fogo;
  _eorð-draca_ → dragão da terra; _beorh_, _hlǣw_ → túmulo (_Bīowulfes biorh_ → o Túmulo de Beowulf,
  2808, como em `traducao-aliterativa/`); _hord-weard_ → o guarda do tesouro; _beorges weard_ → o guarda do túmulo;
  _gryre-gæst_ → o hóspede do horror (2561, § 9); _inwit-gæst_ → hóspede hostil (2671, § 9);
  _gūð-gewǣdu_ → vestes de guerra; _hild-fruma_ → chefe de guerra; _segn_ → estandarte; _byrne_ →
  cota (de malha); _hring-net_ → rede de anéis; _hilde-lēoma_ → luzes de combate; _bān-hūs_ → casa
  dos ossos; _dugoð_ → os veteranos (2659); _beorn_ → guerreiro (2560); _secg_ → varão (2701, 2709);
  _þegn_ → vassalo; _cempa_ → campeão; _ōretta_ → lutador (2539, como em `traducao-aliterativa/`).
- **Kennings e compostos** (a imagem, sem explicar): _hring-boga_ o enroscado em anel; _gūð-floga_ o
  voador da guerra; _ūht-floga_ voador da alva; _lind-wiga_ guerreiro da tília; _gold-gyfa_ doador de
  ouro; _gold-wine Gēata_ amigo do ouro dos geatas; _hilde-swāt_ suor de batalha; _wæl-fȳr_ fogo da
  matança; _wæl-rēc_ fumo da matança; _wæll-seax_ punhal da matança; _here-grīma_ máscara de guerra;
  _glēd-egesa_ o terror das brasas; _līg-ȳð_ ondas de chama; _fȳr-wylm_ ondas de fogo; _sāwul-drēor_
  sangue da alma; _gūð-wine_ (a espada) amigos da guerra (2736); _feorh-bealu_ mal da vida;
  _lǣn-dagas_ dias emprestados; _brēost-hord_ tesouro do peito; _heaðo-wylm_ ondas hostis;
  _hand-gesteallan_ companheiros de mão; _hilde-grāp_ aperto de guerra; _hioro-serce_ camisa de guerra;
  _beadu-serce_ camisa de guerra; _māððum-sigla_ joias como sóis (glossário: _sun-shaped ornament_);
  _brentingas_ altos barcos; _flōda genipu_ névoas das águas.

## 3. Passagens revistas (sentido)

| verso | original | leitura adotada | apoio |
|---|---|---|---|
| 2461–2462 | _Gewīteð þonne on sealman … ān æfter ānum_ | «Recolhe-se então ao leito … um pelo outro»: continua o pai da comparação do canto XXXIV | glossário (_sealma_; _ān æfter ānum_, _one for the other_); Hall, nota à seção XXXIV |
| 2466 | _on þām feorh-bonan fǣhðe gebētan_ | «vingar no matador aquela morte» | glossário (_gebētan_ 2: _could in no way avenge the death upon the slayer_) |
| 2467–2468 | _hatian … lāðum dǣdum_ | «perseguir o guerreiro / com atos de ódio» | glossário (_could not do him any harm_) |
| 2476 | _oððe_ | «e» | nota ao v. 2477 (_oþþe = and_) |
| 2485–2486 | _mǣg ōðerne billes ecgum on bonan stǣlan_ | «um parente pelo outro / com os gumes da lâmina vingou no matador» (Hygelac vinga Hæthcyn) | glossário s.v. _stǣlan_ (dá as duas leituras; a segunda é a dos vv. 2962 ss.) |
| 2489 | _heoro-blāc_ | «pálido da espada» | glossário; Bugge propõe _hrēa-blāc_ (nota) |
| 2502 | _for dugeðum_ | «por bravura» | glossário (_in ability_?) e nota (Ettmüller: _of my prowess_); `traducao-aliterativa/` preferiu «ante os veteranos» |
| 2508–2509 | _hilde-grāp heortan wylmas, bān-hūs gebræc_ | «foi meu aperto de guerra que as ondas do coração, / a casa dos ossos, lhe quebrou»: o aperto é o de Beowulf (o «meu» tira a dúvida) | glossário |
| 2520–2522 | _gif ic wiste hū wið þām āglǣcean elles meahte gylpe wiðgrīpan_ | «se soubesse como / de outro modo poderia, contra o temível, / cumprir a jactância» | glossário s.v. _wiðgrīpan_ (_maintain my boast of battle_); Grein, «combater a jactância do monstro», fica registrado |
| 2524 | _rēðes and-hāttres_ | «calor feroz e hostil» (o calor que vem contra o homem) | glossário (_heat coming against one_); a nota dá a palavra como conjectura de Heyne (Grein: _oreðes and attres_, «bafo e veneno») |
| 2529 | _þæt ic wið þone gūð-flogan gylp ofersitte_ | «tanto que dispenso a jactância contra o voador da guerra» | glossário (_ofersittan_: _refrain from_) |
| 2545 | _hilde-hlemma_ | «o que ruge na guerra»: aposição a Beowulf, não «estrondo» | glossário (_one raging in battle, warrior_, nom. sg.) |
| 2546 | _(stōd on stān-bogan)_ | parênteses mantidos, sem sujeito: «(estava num arco de pedra)» | texto da edição; Grein e Heyne-Socin leem _standan stān-bogan_ (nota) |
| 2548–2550 | _ne meahte horde nēah unbyrnende … dēop gedȳgan_ | «perto do tesouro / não podia ele, sem se queimar …, / aguentar no abismo» | glossário s.v. _dēop_; a emenda _dēor_ (nota) não foi seguida |
| 2565 | _ecgum unglēaw_ | «de gumes afiados», qualificando a espada | glossário (_un-glēaw_, _of a sharp-edged sword_); Bugge: _unslāw_ |
| 2570–2571 | _gebogen … gescīfe scyndan_ | «enroscada, deslizando, / avançando ligeira» | glossário (_gescīfe_: _advancing_); nota aos vv. 2570–2571 |
| 2574–2576 | _þǣr hē þȳ fyrste forman dōgore wealdan mōste, swā him Wyrd ne gescrāf hrēð æt hilde_ | «ali onde ele, naquela hora, pela primeira vez, / teve de impor-se; o destino não lhe deu / glória na guerra» | glossário s.v. _wealdan_ e _mōtan_ (_if he must for the first time that day be victorious, as Fate had denied him victory_) |
| 2578 | _incge lāfe_ | «com a preciosa herança» | glossário (_costly_? _mighty_?) |
| 2589 | _grund-wong þone_ | «aquele chão» (o fundo da caverna ou a terra: o português guarda as duas) | nota ao v. 2589; glossário |
| 2590 | _wyrmes willan_ | «por causa da serpe» | glossário s.v. _willa_ (instr., _for the sake of_) |
| 2604 | _lēod Scylfinga_ | «príncipe dos Scylfings» | glossário (_lēod_, _prince_); nota ao v. 2604 |
| 2607 | _āre_ | «o favor» | glossário; a nota (Kluge) dá «posse»; o verso seguinte diz qual era |
| 2613–2615 | _þām æt sæcce wearð wracu wine-lēasum Wēohstānes bana_ | «para ele, em combate, / sem amigos, a vingança de Weohstan foi o matador» | glossário s.v. _bana_ (figurado, _wracu … bana_); lista de nomes (Eanmund); Heyne-Socin e Grein: _wrǣccan … Wēohstān bana_ (nota) |
| 2619–2620 | _nō ymbe þā fǣhðe spræc, þēah þe hē his brōðor bearn ābredwade_ | «Weohstan não falou da contenda, / embora tivesse abatido o filho do irmão de Onela» | lista de nomes da edição (Ēanmund: _Wēohstān does not speak willingly of this fight, although he has slain Onela's brother's son_). Gummere faz de Onela o sujeito de _spræc_; fica registrado. Os nomes foram postos por extenso para tirar a dúvida dos pronomes. |
| 2650–2651 | _þenden hyt sȳ, glēd-egesa grim_ | «enquanto dura o calor, / o terror das brasas, feroz!» | glossário (_hit_, st. f., _heat_; _whilst the heat lasts_) |
| 2656 | _fāne gefyllan_ | «abater o inimigo» | glossário (_fāh_ 1, o dragão); nota |
| 2658–2659 | _þæt nǣron eald-gewyrht, þæt hē āna scyle Gēata duguðe gnorn þrowian_ | «que os seus antigos méritos não pedem que ele, sozinho / entre os veteranos dos geatas, sofra a aflição» | glossário s.v. _eald-gewyrht_ e _ān_ (_alone of the warriors of the Gēatas_) |
| 2660–2661 | _sceal ūrum þæt sweord and helm, byrne and byrdu-scrūd bām gemǣne_ | «a espada e o elmo hão de ser nossos, / a cota e o adorno do escudo, de ambos em comum» | glossário (_ūrum … bām_; _byrdu-scrūd_, _shield-ornament_?); a leitura _beadu-scrūd_ (nota) não foi adotada |
| 2667–2669 | _scealt nū … feorh ealgian_ | «hás de» passou ao v. 2669, junto do infinitivo | sintaxe portuguesa |
| 2677 | _elne geēode_ | «com toda a pressa» | glossário s.v. _ge-gān_ (_went quickly under his kinsman's shield_) |
| 2686–2688 | _sē þe mēca gehwane … swenge ofersōhte_ | «a mão / que toda espada … / vencia com o golpe» (a mão forte demais inutilizava a espada) | glossário s.v. _ofer-sēcan_; a emenda _þone_ de Bugge (nota) não foi seguida |
| 2694 | _sāwul-drīore; swāt ȳðum wēoll_ | «com o sangue da alma; o cruor fervia em ondas»: «cruor» para não repetir «sangue» | glossário (_swāt_: _wound-blood_) |
| 2696 | _and-longne eorl_ | «o nobre, erguido» | glossário (_at whole length, raised up high_) |
| 2698 | _ne hēdde hē þæs heafolan_ | «não protegeu a cabeça» (a sua: Wiglaf se expôs) | glossário s.v. _hēdan_ (_did not protect his head_); Bugge, «não visou a cabeça do dragão» (nota), fica registrado |
| 2700 | _nīð-gæst_ | «o hóspede maligno» | glossário (_hostile alien, fell demon_); «maligno» para distinguir de _inwit-gæst_ (2671), «hóspede hostil» |
| 2703–2704 | _Þā gēn sylf cyning gewēold his gewitte_ | «Então o próprio rei de novo / dominou os sentidos» | glossário (_possessed his senses_; _þā gēn_, _then again_) |
| 2707 | _(ferh ellen wræc)_ | «(a vida expulsou a força)», parênteses da edição | glossário (_with the departing life his strength left him_); Klüge e Sievers (nota) propõem emendas |
| 2721–2724 | _Hyne … heoro-drēorigne, þēoden mǣrne, þegn ungemete till, wine-dryhten his wætere gelafede, hilde-sædne_ | objeto direto com «a» («ao ensanguentado …, / ao famoso rei, o vassalo …, / ao seu senhor e amigo, refrescou com água, / ao farto de luta»): fica claro quem banha e quem é banhado, sem mudar a ordem | glossário (_gelafian_, _refresh, lave_) |
| 2725 | _hē ofer benne spræc_ | «falou sobre a ferida» | glossário s.v. _ofer_ (_about, concerning_) |
| 2736 | _þē mec gūð-winum grētan dorste_ | «que me ousasse saudar com os amigos da guerra» (as espadas; a ironia de _grētan_ fica) | glossário s.v. _gūð-wine_ (_designation of the sword_; _attack me with his war-friends_) |
| 2739–2740 | _nē mē swōr fela āða on unriht_ | «e não jurei / muitos juramentos em falso» (a litotes do original) | glossário |
| 2750 | _swegle searo-gimmas_ | «as gemas lavradas, brilhantes como o céu» | glossário (_swegle_, _bright, etherlike_; _searo-gim_, _cunningly set gem_) |
| 2757 | _bī sesse_ | «junto ao assento» (diante da toca) | glossário s.v. _sess_ |
| 2762 | _feormend-lēase_ | «sem mão que as limpasse» | glossário (_wanting the cleanser_) |
| 2765–2767 | _Sinc ēaðe mæg … gehwone ofer-hīgian, hȳde sē þe wylle!_ | «O tesouro bem pode, / o ouro no chão, a qualquer um da raça / dos homens vencer: esconda-se quem quiser!» | glossário (_ofer-hīgian_, _to exceed_; _hȳde [hine, himself]_). `traducao-aliterativa/` preferiu «esconda-o»; Hall e Gummere leem «tornar soberbo» (Kluge, nota) |
| 2770 | _gelocen leoðo-cræftum_ | «tecido em malhas com arte» | glossário (_a banner all hand-wrought of interlaced gold_); as outras leituras (encantado; feito à mão) na nota |
| 2778–2780 | _bill ǣr-gescōd (ecg wæs īren) eald-hlāfordes þām þāra māðma mund-bora wæs_ | «antes ferira a lâmina / (o gume era de ferro) do velho senhor / aquele que era o guardião daqueles tesouros»: a espada de Beowulf matou o dragão | glossário s.v. _ge-sceaðan_ e _eald-hlāford_ (_of the old Bēowulf_?); nota ao v. 2778 (Müllenhoff: o antigo dono do tesouro; Wülker: _ǣrgescōd_ «calçado de bronze») |
| 2782 | _hioro-weallende_ | «rolando em fúria» | glossário (_rolling around fighting_) |
| 2784 | _Ār_ | «O mensageiro» (Wiglaf) | glossário (_ār_, _messenger_) |
| 2786 | _collen-ferð_ | «ele, de alma altiva»: Wiglaf | glossário (_of Wīglāf_) |
| 2792–2793 | _wæteres weorpan, oð þæt wordes ord brēost-hord þurhbræc_ | «a lançar-lhe água, até que a ponta da palavra / rompeu o tesouro do peito» | glossário (_wæteres_, gen. instr.; _the word's point broke through his closed breast_) |
| 2800–2801 | _on māðma hord mīne bebohte frōde feorh-lege_ | «vendi pelo tesouro de joias / a minha velha vida» | glossário (_for the treasure-hoard I sold my old life_) |
| 2804 | _æt brimes nosan_ | «no promontório do mar» | glossário (_at the sea's promontory_) |
| 2814 | _ende-lāf_ | «o último que resta» (o jogo com _Wīg-lāf_, da nota, não passa) | glossário; nota ao v. 2815 |
| 2819 | _ǣr hē bǣl cure_ | «antes que escolhesse a pira» | glossário (_before he sought his funeral-pile_) |
| 2821 | _sōð-fæstra dōm_ | «a glória dos justos» | glossário (_glory, realm, of the saints_) |

## 4. Ritmo: o que o Versificador mostrou e o que mudou

Primeiro rascunho: canto 35 com 10 versos marcados e 24 com 4 átonas seguidas (16,9%); canto 36 com 10
marcados (quase todos por possessivos átonos: «ao nosso senhor», «por sua própria vontade», «na tua
juventude»); canto 37 com 1 marcado e 20,7% de versos com 4 átonas; canto 38 com 10 marcados.

Reescritas principais (antes → depois):

| verso | antes | depois | por quê |
|---|---|---|---|
| 2482 | embora um deles o pagasse com a vida, | embora um deles a tenha pago com a vida, | `ralo` |
| 2485–2486 | um parente vingou o outro / com os gumes da lâmina no matador, | um parente pelo outro / com os gumes da lâmina vingou no matador, | `ralo`, `vazio`; e «vingou o outro» dava três vogais |
| 2495–2497 | de ir aos gépidas, aos dinamarqueses da lança / ou ao reino dos suecos procurar | de ir aos gépidas, ir aos dinamarqueses da lança / ou ao reino dos suecos à procura / de um guerreiro pior, … | `vazio` em «aos dinamarqueses» |
| 2502 | desde que, por bravura, me tornei de Dæghrefn | desde que eu, por bravura, … | `ralo`, `vazio` |
| 2516 | sair do salão sob a terra para me buscar! | sair à minha procura do salão sob a terra! | `vazio` |
| 2537–2538 | ou a guerra há de levar, / morte terrível, o vosso senhor! | ou a guerra, o terrível / mal da vida, há de levar o vosso senhor! | `vazio` («o vosso senhor» sem apoio) |
| 2542 | não é essa a empresa do covarde. | tal caminho não é de covarde. | `choques` |
| 2545 | o furioso na luta, | o que ruge na luta, | `ralo` |
| 2531–2533 | qual de nós dois / … sobrevive melhor / às feridas. Não é esta a vossa empresa, | qual pode melhor / … resistir às feridas, / de nós dois. Não vos cabe esta empresa, | cada palavra volta ao seu verso; `choques` em «Não é esta» |
| 2574–2575 | teve de lutar sem que o destino lhe desse | teve de impor-se; o destino não lhe deu | `vazio`; e o sentido de _wealdan_ |
| 2470, 2564, 2570, 2575, 2595 | deixou a alegria / a antiga herança / então a arder / impor-se, e o destino / sofreu o aperto | deixou o júbilo / a velha herança / então, ardendo / impor-se; o destino / sofreu angústia | três vogais seguidas |
| 2613 | filho de Ohthere; a quem na peleja, | filho de Ohthere: para ele, em combate, | `vazio` |
| 2635 | quando prometemos ao nosso senhor | quando ao senhor demos nossa palavra | `ralo`, `vazio` |
| 2637–2638 | que lhe pagaríamos estas armas … / se lhe chegasse uma precisão como esta, | que havíamos de pagar-lhe as armas … / se lhe viesse alguma precisão assim, | `ralo` |
| 2640 | por sua própria vontade, | por vontade dele mesmo, | `ralo` |
| 2648 | em que o nosso senhor precisa da força | em que o senhor dos homens precisa da força | `ralo`, `vazio`; e é a imagem de _man-dryhten_ |
| 2665–2666 | na tua juventude, / que não deixarias, enquanto vivesses, | quando eras jovem, / que nunca, enquanto vivo, deixarias | `ralo`, `vazio` |
| 2676–2677 | mas o moço, sob o escudo do parente, / entrou com coragem, | mas o moço se abrigou sob o escudo do parente, / com toda a pressa, | `ralo`; e o sentido de _elne_ (glossário) |
| 2710 | um vassalo na precisão. Aquela foi para o rei | um vassalo quando é preciso. Aquela foi, para o rei, | `ralo` |
| 2762 | sem quem as polisse, | sem mão que as limpasse, | `vazio` |
| 2785 | instigado pelos tesouros: atormentava-o a dúvida | movido pelas joias: roía-o a curiosidade, | `ralo`; e _fyrwet_ é curiosidade |
| 2795–2796 | Por estas riquezas ao Senhor de tudo / dou graças com palavras, | Por estas riquezas eu agradeço ao Senhor de tudo, / digo-o com palavras, | `ralo` |
| 2805–2806 | ele há de, em memória, para o meu povo, / erguer-se alto | ele há de servir de lembrança ao meu povo, / erguendo-se alto | `vazio` |
| 2807 | para que os marinheiros o chamem depois | para que depois os homens do mar o chamem | `ralo`, `vazio` |
| 2814 | Tu és o último resto da nossa linhagem, | Tu és o último que resta da nossa raça, | `vazio` |
| 2816–2817 | os meus parentes para o decreto … / nobres na sua coragem | os parentes que eu tinha, ao decreto … / nobres em plena coragem | `ralo`, `vazio` |

Lição repetida do lote: o `verso-livre.mjs` não acentua os possessivos (_nosso, sua, tua, vosso_);
«ao nosso senhor» no fim do verso abre um vão de cinco átonas. Onde o possessivo não fazia falta, saiu;
onde fazia, pôs-se uma palavra plena antes dele.

**Resultado final** (`verso-livre.mjs`, com a pronúncia dos nomes dada por `# troca`):

| | canto XXXV | canto XXXVI | canto XXXVII | canto XXXVIII | meta |
|---|---|---|---|---|---|
| versos | 142 | 92 | 58 | 69 | = original |
| média de sílabas | 12,8 | 12,9 | 13,0 | 12,7 | |
| sílabas por acento | 2,60 | 2,69 | 2,71 | 2,60 | 2,4–2,8 |
| intervalos 1 / 2 / 3 / 4 / 5+ (%) | 9,5 / 35,0 / 32,3 / 19,6 / 3,6 | 6,6 / 32,7 / 38,1 / 19,5 / 3,2 | 5,9 / 32,6 / 36,2 / 21,7 / 3,6 | 9,4 / 34,5 / 36,0 / 16,9 / 3,4 | ~15 / 30 / 29 / 16 / 5 |
| versos com 4+ átonas seguidas | 13,4% | 12,0% | 13,8% | 13,0% | até ~20% |
| versos que terminam em pontuação | 62,0% | 63,0% | 70,7% | 65,2% | 65–100% |
| âncoras métricas | 21 | 12 | 4 | 12 | |
| versos marcados (`ralo`, `vazio`, `choques`) | 0 | 0 | 0 | 0 | 0 |

`molde.mjs` (molde livre, `*`, com as `# troca`): nenhum ✗, nenhum ≠, nenhuma «leitura natural tem», nos
quatro cantos.

Fora da meta, de propósito: o choque (intervalo 1) fica entre 6% e 10%, abaixo dos mestres, e o
ternário acima, como nos cantos I e II (relato solene; paroxítonas de três sílabas). Versos que
terminam em pontuação: 62–71% (o original encadeia muito nos discursos e nas descrições de 2543–2550 e
2757–2783; não se quebrou frase para acertar o número).

## 5. Trocas de pronúncia usadas na medição

Além das de `PROMPT-CONTINUACAO.md`: Herebeald => Hérebald; Hrethel => Hrétel; Hæthcyn => Hétkin;
Hreosnabeorh => Hréosnabeor; Eofor => Êofor; Dæghrefn => Dégrefen; Ecgtheow => Éctiou; Wiglaf =>
Uíglaf; Weohstan => Uéostan; Ælfhere => Élfere; Wægmunding => Uégmunding; Eanmund => Éanmund; Ohthere
=> Ótere; Onela => Ônela; Nægling => Négling; Hronesnæs => Rônesnés; wedergeatas => wéder guéatas (o
composto tem dois apoios na fala; sem a troca o programa lê um vão de sete átonas).

## 6. Crítica

Foi chamado um crítico independente (Sonnet, esforço médio), com o original, a tradução, o guia, Hall,
Gummere, Morris e Wyatt e o extrato do glossário por verso, instruído a apontar até 15 problemas de
sentido, ambiguidade, gramática, guia e anglicismo, sem comentar o ritmo. **O resultado dele não chegou
antes da entrega deste lote**: os pontos que ele apontar ficam para o coordenador conferir (aceitar só o
que o glossário não contradiz e medir cada mudança com o `verso-livre.mjs`).

Antes disso, a revisão de sentido (§ 3) foi feita verso a verso contra o original e o extrato do
glossário, e já mudou: 2464–2465 (sem o acréscimo «no peito»), 2492 (_gifeðe_ → «como quis o fado»,
guia § 9), 2531–2533 (palavras de volta ao seu verso), 2560 (_biorn_ → guerreiro, guia), 2574–2575
(_wealdan_ → «impor-se»), 2619–2621 (sujeito Weohstan, pela lista de nomes da edição), 2660–2661
(_byrdu-scrūd_ → «adorno do escudo», glossário), 2676–2677 (_elne_ → «com toda a pressa», glossário),
2703–2704 («de novo … voltou a» redundante), 2749 («tesouro» repetido), 2789 e 2798 (regência).

## 7. Nomes e termos novos (para o guia)

- Nenhum nome próprio fora do guia. Weohstan numa forma só (a edição tem _Wēoxstān_ 2603,
  _Wēohstān_ 2614, _Wīhstān_ 2753). Hreosnabeorh, Hronesnæs, Nægling como em `traducao-aliterativa/`.
- _ōretta_ → lutador; _lind-wiga_ → guerreiro da tília; _nīð-gæst_ → hóspede maligno (proposta:
  distinguir de _inwit-gæst_, «hóspede hostil»); _hilde-hlemma_ → o que ruge na guerra (aposição de
  pessoa, glossário); _gūð-wine_ (a espada) → amigos da guerra; _ār_ (mensageiro) → o mensageiro;
  _māððum-sigla_ → joias como sóis; _sāwul-drēor_ → sangue da alma, _swāt_ → cruor (2694).
- _gold-wine Gēata_ → «amigo do ouro dos geatas» (2585), como em `traducao-aliterativa/`. Os cantos XXIII–XXVI
  deste teste usam «amigo de ouro dos homens»: o coordenador escolhe uma forma.
- _æt þearfe_ → «na precisão» (2695) e «quando é preciso» (2710): a fórmula variou por ritmo.
- Proposta para o guia (§ 9): _sōð-fæstra dōm_ → «a glória dos justos»; _Bīowulfes biorh_ → o Túmulo
  de Beowulf.

## 8. Conferência

- Versos: 142 (2461–2602), 92 (2603–2694), 58 (2695–2752), 69 (2753–2821), como o original.
- Tabulação: nenhuma. Grep de mesóclise: nada.
- Aspas: 35 reabre no v. 2461 e fecha em 2510; abre 2512–2516, 2519–2538; 36: 2634–2661, 2664–2669;
  37: 2730–2752; 38: 2795–2809, 2814–2817.
- Cabeçalho igual ao de `traducao-aliterativa/` (`# canto`, `# titulo`, título do § 8 do guia).
