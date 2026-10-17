# Verso livre: cantos XXXIX a XLIII (versos 2822–3184) e o fragmento de Finnsburh (1–48)

Arquivos: `39.txt` (71 versos), `40.txt` (54), `41.txt` (112), `42.txt` (79), `43.txt` (47),
`finnsburh.txt` (48). Mesmo método e mesmas metas de `notas.md` (cantos I–II), que serviram de modelo.

## 1. Método

1. Leitura do original com o glossário de Harrison e Sharp verso a verso (extraído por script, para cada
   número de verso, de todos os verbetes que o citam) e com as notas da edição (vv. 2837–3184 e as notas
   de Finnsburh); para Finnsburh, o glossário próprio do fragmento (fim do arquivo da edição) e Chambers
   (cap. sobre o fragmento). Conferência com Hall (numeração por seção), Gummere (cuja numeração de
   seções, nesta parte, está deslocada: o XXXIX dele é o nosso XLI) e Morris e Wyatt. Nada foi copiado
   dessas versões nem da tradução aliterativa de `../traducao-aliterativa/`, consultada só para nomes e termos.
2. Rascunho verso a verso, com a frase portuguesa dentro do verso; conferência do alinhamento com o
   original lado a lado (`paste`), verso por verso.
3. Ritmo: `verso-livre.mjs` (sobre cópia com as trocas de pronúncia) e `molde.mjs` (molde livre `*` com
   `# troca`), com a visão compacta (esqueleto e intervalos por verso) e um testador de versos avulsos.
   Duas a três passadas por canto (§ 4).
4. Revisão de sentido e crítica (§ 5).

Trocas de pronúncia usadas (além das do modelo): Hygelac ⇒ Híguelac, Wiglaf ⇒ Uíglaf, Weohstan ⇒
Uéostan, Ohthere ⇒ Ócterre, Onela ⇒ Ónela, Hæthcyn ⇒ Hétkin, Hrethel ⇒ Hrétel, Hrethling(s) ⇒
Hrétling(s), Eofor ⇒ Éofor, Wonred ⇒ Uônred, Wulf ⇒ Vulf, Hrefnawudu ⇒ Hrefnavúdu, Hrefnesholt ⇒
Hrefnesrólt (leitura oxítona natural do leitor brasileiro), Earnanæs ⇒ Earnanés, Hronesnæs ⇒ Hronesnés,
Hnæf ⇒ Hnéf, Hengest ⇒ Hênguest, Sigeferth ⇒ Síguefert, Eaha ⇒ Éaha, Ordlaf ⇒ Órdlaf, Guthlaf ⇒ Gútlaf,
Garulf ⇒ Gárulf, Guthere ⇒ Gútere, Finnsburh ⇒ Finsburh.

## 2. Escolhas gerais

- **Fórmulas do guia**: «Wiglaf falou, o filho de Weohstan» (2863, 3077; a edição grafa _Wēohstān_ e
  _Wīhstān_, uma forma só, como manda o § 9); _folces hyrde_ → pastor do povo (2982; Finnsburh 46);
  _rīces hyrde_ → pastor do reino (3081); _mīne gefrǣge_ → pelo que ouvi (2838); _ne gefrægn ic_ → nunca
  ouvi dizer (Finnsburh 37); _heorð-genēatas_ → companheiros da lareira (3181).
- **Deus**: o Soberano (_wealdend_, 2858); o juízo de Deus (_dōm godes_, 2859, guia § 9); Deus (2875,
  3055); o Soberano das vitórias (_sigora waldend_, 2876); o Rei verdadeiro das vitórias (_sigora
  sōð-cyning_, 3056); o Dono (_āgend_, 3076, como em `../traducao-aliterativa/`); o Soberano (_waldend_, 3110).
  Pronome de Deus em minúscula (3056–3058).
- **Termos do guia**: _wyrm_ → serpe; _draca_ → dragão; _āglǣca_ → o temível (2906); _gryre-gæst_ →
  hóspede do horror (3042, § 9); _bǣr_ → esquife (3106); _beorh_ → túmulo (2843, 3098, 3165) e monte
  (3144, o lugar da pira, § 9); _hlǣw_ → túmulo (3159, 3171); _gifeðe_ → fado (3086); _dugoð_ → os
  veteranos (2921, 2946); _ealu-benc_ → banco da cerveja; _gūð-gewǣdu_ → vestes de guerra; _cempa_ →
  campeão; _secg_ → guerreiro, varão; _glēd_ → brasa; _lēg_ → chama; _ǣled_ → fogo.
- **Tratamento**: vós nas falas de Wiglaf aos covardes e aos guerreiros; tu na resposta de Sigeferth a
  Garulf (Finnsburh 26–27).
- **Aspas**: falas de Wiglaf (2865–2892; 3078–3110; a ordem 3115–3120, que abre no meio do verso, como na
  edição); a fala do mensageiro (2901–3028) fecha no último verso de `40.txt` e reabre no primeiro de
  `41.txt` (guia, § 6). O fim do canto XXXVIII (`original/38.txt`) fecha a fala de Beowulf dentro do 38, e
  o XXXIX começa em narração: nada atravessa 38→39. Finnsburh: a fala mutilada do v. 1 (“. . . nunca
  ardem.”), a do rei (3–12) e a de Sigeferth (24–27, com o parêntese «(disse ele)» dentro das aspas, como
  no impresso).
- **Lacunas**: 3151–3157 e Finnsburh 1 e 48. Traduzi só as palavras inteiras; os fragmentos de palavra
  (_lat_, _con_, _ede_, _gas_, _hyðo_, _haf mid_; _næs_ em Finnsburh 1) viraram `. . .`, no mesmo lugar do
  verso; `(?)` no lugar da edição (3153, 3157). Nada foi completado com as restaurações de Bugge.

## 3. Passagens revistas (sentido)

| verso | original | leitura adotada | apoio |
|---|---|---|---|
| 2822–2825 | _Þā wæs gegongen guman unfrōdum earfoðlīce … blēate gebǣran_ | «Então coube ao homem ainda jovem, / com grande pesar, ver … em triste desamparo» | glossário: _it had happened to the young man in sorrowful wise_; _blēate_ = _helplessly_ |
| 2837–2839 | _lȳt manna þāh … þēah þe hē … dyrstig wǣre_ | «a poucos homens deu certo … por mais ousados que fossem»: o singular _hē_ passou ao plural, para concordar com «poucos homens» | glossário (_þēon_: _that throve to few_) |
| 2857 | _on þām frum-gāre_ | «no chefe das lanças»: a imagem (_frum-gār_, «primeira lança») | glossário: _primipilus, duke, prince_ |
| 2859 | _wolde dōm godes dǣdum rǣdan gumena gehwylcum_ | «o juízo de Deus queria dispor dos feitos / de cada um dos homens» | glossário: _God's doom would rule over, dispose of, every man in deeds_; guia § 9. Bugge: _dēað ārǣdan_ (Hall, nota) |
| 2861–2862 | _grim andswaru ēð-begēte_ | «uma resposta dura / veio sem custo a quem perdera a coragem» | glossário (_ēð-begēte_) |
| 2873–2875 | _wrāðe forwurpe. Þā hyne wīg beget, nealles …_ | pontuação da edição: ponto depois de _forwurpe_; «Quando a guerra o alcançou» abre a frase seguinte | notas aos vv. 2873–2874 |
| 2881 | _symle wæs þȳ sǣmra_ | «a serpe enfraquecia sempre que eu feria…»: sujeito explícito (o «sempre ficava mais fraco» deixava pensar em Beowulf) | glossário (_sǣmra_: o dragão) |
| 2883 | _wēoll of gewitte_ | «jorrava do peito» | glossário de _gewit_ neste verso: _heart, breast_ |
| 2885–2887 | _sinc-þego … lufen ālicgean_ | «o receber de joias e o dom de espadas, / a alegria da pátria inteira, à vossa raça, / e o sustento hão de faltar» | glossário (_lufen_: _subsistence?_, duvidoso) |
| 2905–2907 | _sweorde ne meahte …_ | «com a espada o rei / não pôde, no temível…»: sujeito explícito | Hall, Gummere |
| 2908 | _ofer Bīowulfe, byre Wīhstānes_ | «Wiglaf está sentado, / o filho de Weohstan, junto de Beowulf»: a aposição vem antes de Beowulf, no mesmo verso, para não parecer que o filho de Weohstan é Beowulf | |
| 2910 | _healdeð hige-mēðum hēafod-wearde_ | «e vela a cabeceira, pelos mortos» | glossário: dat. pl. = _for the dead_. Sievers lê _hige-mēðe_ («triste de ânimo», de Wiglaf), Bugge um abstrato (Hall, nota; a tradução aliterativa seguiu Bugge) |
| 2912 | _underne_ | «às claras» | glossário: _undyrne_, _plain, clear_ |
| 2919–2921 | _nalles frætwe geaf ealdor dugoðe_ | «não deu mais joias / o chefe aos veteranos» | glossário; nota a 2920 (Bugge) |
| 2922 | _Merewīoinga milts_ | «a graça do merovíngio» | guia § 9; nota ao v. 2922 |
| 2927–2928 | _þā … gesōhton Gēata lēode Gūð-scilfingas_ | «quando … marchou … a gente dos geatas contra os Scylfings guerreiros»: o singular coletivo e o «contra» tiram a dúvida sobre quem atacou | Hall, Gummere |
| 2929–2932 | _se frōda fæder … brȳd āhēorde, gomela īo-meowlan_ | «o grisalho pai de Ohthere», e _gomela_ como nominativo (o velho, Ongentheow), passado ao v. 2931: «e o ancião libertou a esposa, / a mulher de outrora, despojada do ouro» | glossário de _gamol_ (2932 entre os nominativos); _āhēoran_ = _to free (?)_ |
| 2937 | _sweorda lāfe_ | «os restos das espadas» | glossário: _those spared by the sword_ |
| 2941 | _gētan wolde, sume on galg-trēowum_ | «os mataria, e alguns nas árvores da forca» (sem a conjectura de Bugge) | nota aos vv. 2940 ss. |
| 2950 | _se gōda_ | «o bom rei» (Ongentheow; Ongentheow é nomeado dois versos depois) | nota ao v. 2950 («bom» = valente); Bugge: _gomela_ |
| 2958–2959 | _Þā wæs ǣht boden Swēona lēodum, segn Higelāce_ | «Então se deu caça / ao povo dos suecos, e o estandarte a Hygelac» | glossário; nota ao v. 2959 (outras leituras: _segn Higelāces_) |
| 2960 | _Freoðo-wong_ | «o campo da paz», em minúscula | glossário |
| 2963–2965 | _on bīd wrecen … Eofores ānne dōm_ | «foi forçado a parar … teve de sujeitar-se / ao poder só de Eofor» | glossário (_bīd_, _þafian_); Hall |
| 2974–2975 | _ac hē him on hēafde helm ǣr gescer, þæt hē …_ | «pois o rei antes lhe partira o elmo … / e Wulf, tinto de sangue, teve de vergar»: sujeitos explícitos | |
| 2978–2981 | _Lēt … brādne mēce … brecan ofer bord-weal_ | «fez … a larga espada … partir o elmo de gigantes / por cima do muro de escudos»; o verbo _brecan_ subiu um verso | glossário (_brecan_); Gummere |
| 2995–2997 | _hund þūsenda … ne þorfte him þā lēan oðwītan mon_ | «cem mil / em terras e anéis trançados; não podia censurar-lhes o prêmio / homem algum … pois tinham ganho a glória lutando» | nota ao v. 2995; Hall (nota 3) registra a dúvida entre _him_ singular (o rei) e plural (os irmãos); o _syððan hīe … geslōgon_ favorece o plural |
| 3006 | _hwate Scylfingas_ | «e, depois da queda dos heróis, os bravos Scylfings», objeto de «guardou» | glossário (_hwæt_: acc. pl.); nota ao v. 3006 (Scyldingas/Scilfingas) |
| 3011–3012 | _Ne scel ānes hwæt meltan_ | «Não há de fundir-se só uma parte» | |
| 3050–3051 | _swā hīe wið eorðan fæðm þūsend wintra þǣr eardodon_ | «pois no abraço da terra / tinham morado ali mil invernos» | glossário (_fæðm_, _eardian_) |
| 3057 | _(hē is manna gehyld)_ | «(ele é o amparo dos homens)» | glossário: _support, protection_; nota ao v. 3057 |
| 3060 | _gehȳdde_ | «escondera» (o dragão) | texto da edição; Bugge: _gehȳðde_, «saqueara» (o ladrão) |
| 3063–3066 | _Wundur hwār, þonne …_ | como pergunta: «Será espanto, então, quando / um nobre … chega ao fim … ?» | glossário de _hwǣr_: _In elliptical question: is it a wonder when…?_ (Müllenhoff). Sievers: pergunta indireta («mistério é onde…»), seguida pela tradução aliterativa |
| 3068 | _searo-nīðas_ | «o combate» | glossário, 2.º sentido neste verso |
| 3070–3074 | _benemdon … hergum geheaðerod … strāde_ | «o amaldiçoaram fundo … encerrado em lugares de ídolos … quem pisasse aquele chão» | glossário (_benemnan_, _herg_, _strādan_); notas a 3073–3074 (H.-So. _strude_) |
| 3075–3076 | _Næs hē gold-hwæt: gearwor hæfde āgendes ēst ǣr gescēawod_ | «Ele não tinha cobiça de ouro: de melhor vontade / teria antes contemplado a graça do Dono» | glossário (_āgend_ = Deus). Sievers: «não tinha antes visto o favor do dono cobiçoso» (nota) |
| 3085–3087 | _Hēoldon hēah gesceap … gifeðe tō swīð_ | «Recebemos uma sorte pesada … foi forte demais o fado» | glossário (_healdan_ 5, _gifeðe_) |
| 3097 | _æfter wines dǣdum_ | «pelos feitos do amigo» (sem _wine dēadum_) | nota ao v. 3097 |
| 3106 | _brād gold_ | «ouro maciço» | glossário: _massive gold_ |
| 3114 | _folc-āgende_ | «os chefes do povo», nominativo plural | glossário; Bugge: dativo, Beowulf (nota) |
| 3116 | _(weaxan wonna lēg)_ | «(e crescer a chama escura)», parênteses do impresso | nota ao v. 3116 (Cosijn: _weaxan_ = devorar) |
| 3120 | _feðer-gearwum fūs flāne full-ēode_ | «pronta com as penas, seguindo a seta» | nota ao v. 3120 (_fūs_ = provido de) |
| 3124 | _eahta sum_ | «e foi, ele com mais sete» | glossário |
| 3127–3130 | _Næs þā on hlytme … or-wearde ǣnigne dǣl … lǣne licgan_ | «Não foi a sorte que decidiu… / quando os homens viram que qualquer parte / ficava sem guarda … a jazer e a perder-se» | glossário |
| 3146–3147 | _sweart ofer swioðole … (wind-blond gelæg)_ | «negro por cima do vapor … (aquietou-se o vento)» | glossário (_sweoðol_: _vapor, smoke_; _ge-licgan_) |
| 3153 | _sǣlde_ | «disse» (leitura _sǣde_, que Bugge, Hall, Gummere e Morris seguem); o glossário só dá _sǣlan_ «atar», que aqui não faz sentido | nota ao v. 3151 ss. |
| 3162 | _bronda betost_ | «o melhor das brasas» (lição do texto; H.-So.: _bronda be lāfe_, «os restos das brasas») | nota ao v. 3162 |
| 3165 | _siglu_ | «sóis de ouro» | glossário: _sun-shaped ornament_ |
| 3179 | _of līc-haman lǣne weorðan_ | «da morada do corpo e entregar-se ao fim» | glossário: _līc-hama_ (_body-home_); _lǣne_ = _given over to death_ |
| 3182 | _woruld-cyning_ | «um rei deste mundo», singular, como na edição | glossário |
| F 1 | _. . . næs byrnað nǣfre_ | «. . . nunca ardem»; _næs_ (fragmento de _[hor]nas?_) dentro da lacuna | nota ao v. 1 |
| F 4 | _hornas_ | «as galhadas» deste salão: as pontas das empenas, como _horn-gēap_ → «de amplas galhadas» no canto II | nota aos vv. 78–83 do poema |
| F 5 | _ac fēr forð berað_ | «mas eles trazem o terror» | glossário de Finnsburh: _fēr_ = _fear, terror_; Bugge supre versos (nota) |
| F 6 | _gylleð grǣg-hama_ | «ressoa o manto cinzento» (a cota de malha; ou o lobo, Brooke) | glossário |
| F 8 | _waðol_ | «cheia» (a lua) | glossário: _the full moon_ [Grein]; Bosworth: _wandering_ |
| F 18–21 | _Þā gīt Gārulf Gūðere styrode_ | «Então ainda a Garulf Guthere tentava conter»: Guthere contém Garulf (o «a» marca o objeto), como em Chambers; «eles» (19) e «a» (21, a vida) como no texto | notas aos vv. 18–21 (Bugge troca os nomes) |
| F 27 | _swæðer_ | «o que tu mesmo, dos dois, vieres buscar de mim» | nota ao v. 27: _either_ (vida ou morte) |
| F 29–30 | _cēlod bord … bān-helm_ | «o escudo côncavo … o elmo de osso» | glossário (_keeled, hollow_; _bone-helmet_ [_shield_, Bosw.]); Bugge: _bār-helm_ |
| F 34 | _Hwearf flacra hrǣw hræfn, wandrode_ | «Rodava o corvo, adejando, sobre os cadáveres, pairava» | glossário (_flacra_ duvidoso; _wandrian_: _hover_) |
| F 40 | _hæg-stealdas_ | «os homens da sua casa» | glossário: _house-carl_ |
| F 45 | _here-sceorpum hrōr_ | «por forte que fosse como armadura» | glossário (Bosworth: _strong [though it was] as armor_); Thorpe/Bugge: _heresceorp unhrōr_ |

## 4. Ritmo: o que o Versificador mostrou e o que mudou

Primeiros rascunhos: 39 com 6 versos marcados e 22,5% de versos com 4+ átonas; 40 com 3 marcados; 41 com
19 marcados (muitos `ralo`); 42 com 10; 43 com 4 e 21,3% de 4+ átonas; Finnsburh com 3 marcados e 27,1%
de 4+ átonas. Causas principais: palavras longas de pretônicas sem apoio (_companheiros_, _guardião_,
_necessidade_, _generoso_), possessivos átonos («o nosso senhor», «a vossa raça»), e «que lhe pa-» antes
de tônica.

Reescritas principais (antes → depois):

| verso | antes | depois | por quê |
|---|---|---|---|
| 2843–2844 | A Beowulf, a sua parte / dos tesouros senhoriais foi paga com a morte; | Beowulf pagou / com a morte a sua parte dos tesouros nobres; | `vazio` de 6 átonas |
| 2850 | na grande necessidade do seu senhor; | na grande aflição do seu senhor; | `ralo` |
| 2862 | foi fácil de obter para quem perdera a coragem. | veio sem custo a quem perdera a coragem. | vão de 5 |
| 2877 | quando precisou de coragem. | na hora de mostrar coragem. | `ralo`, `vazio` |
| 2886 | toda a alegria da pátria, para a vossa raça, | a alegria da pátria inteira, à vossa raça, | `vazio` e três vogais seguidas (_toda a alegria_) |
| 2899 | quem cavalgou pelo promontório, | quem subiu a cavalo o promontório, | `ralo` |
| 2910 | e guarda, pelos mortos, a vigília da cabeceira | e vela a cabeceira, pelos mortos, | `ralo`; e mais claro |
| 2936 | para Hrefnesholt, sem senhor. | rumo a Hrefnesholt, sem ter mais senhor. | `ralo` |
| 2949 | e como os povos, entre si, despertaram a contenda. | e como um povo e outro acordaram a contenda. | `ralo` |
| 2990 | Este recebeu os adornos e lhes prometeu… | O rei aceitou os adornos e prometeu-lhes… | `ralo`, `vazio`; sujeito explícito |
| 3003–3005 | assim que souberem que o nosso senhor / … / contra os inimigos o tesouro e o reino | assim que souberem que o nosso rei / … / das mãos inimigas o tesouro e o reino | `ralo`, `vazio` |
| 3022 | a festa e a alegria do canto | a festa e o júbilo do canto | quatro vogais seguidas |
| 3027–3028 | como se fartou no repasto, / enquanto, com o lobo, despojava os caídos. | como lhe foi no repasto, / despojando os mortos ao lado do lobo. | `vazio`, `ralo` |
| 3058 | precisamente a quem dos homens lhe parecesse justo. | a quem ele, dentre os homens, achasse justo. | `ralo` |
| 3082 | para que não fosse enfrentar aquele guardião do ouro, | de não atacar aquele guarda do ouro, | `vazio` (_guardião_ sem apoio) e regência |
| 3118–3120 | a tempestade de flechas, disparada com força, … pronta com as suas penas, e acompanhava a seta. | a tormenta das flechas, lançada com força, … pronta com as penas, seguindo a seta. | `ralo`, `vazio` |
| 3175 | exaltaram a sua nobreza e os seus feitos de coragem, | exaltaram-lhe a nobreza e os feitos de coragem, | `ralo`, `vazio` |
| 3183 | o mais generoso com os homens e o mais bondoso, | com os homens o mais pródigo e o mais manso, | `ralo` (os superlativos com «o mais» átono) |
| F 31 | até que, naquele combate, Garulf tombou, | até que Garulf tombou naquele combate, | `vazio` |
| F 42 | dos companheiros, mas guardaram a porta. | dos companheiros, mas eles guardaram a porta. | `ralo` |

**Resultado final** (`verso-livre.mjs`, com as `# troca`):

| | XXXIX | XL | XLI | XLII | XLIII | Finnsburh | meta |
|---|---|---|---|---|---|---|---|
| versos | 71 | 54 | 112 | 79 | 47 | 48 | = original |
| média de sílabas | 12,3 | 12,1 | 12,5 | 12,6 | 11,5 | 13,3 | |
| sílabas por acento | 2,65 | 2,70 | 2,58 | 2,63 | 2,63 | 2,56 | 2,4–2,8 |
| intervalos 1 / 2 / 3 / 4 / 5+ (%) | 9,7 / 32,9 / 34,9 / 20,2 / 2,3 | 6,9 / 30,9 / 35,6 / 22,3 / 4,3 | 9,6 / 33,1 / 38,9 / 14,7 / 3,7 | 9,3 / 34,3 / 33,7 / 18,7 / 4,0 | 8,2 / 31,0 / 38,6 / 20,3 / 1,9 | 7,5 / 37,0 / 38,0 / 15,0 / 2,5 | ~15 / 30 / 29 / 16 / 5 |
| versos com 4+ átonas seguidas | 8,5% | 14,8% | 14,3% | 15,2% | 6,4% | 10,4% | até ~20% |
| terminam em pontuação | 67,6% | 66,7% | 70,5% | 67,1% | 70,2% | 87,5% | 65–100% |
| âncoras métricas | 17 | 11 | 17 | 16 | 8 | 8 | |
| versos marcados | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

`molde.mjs` (molde livre, `*`, com as `# troca`): nenhum ✗, nenhum ≠, nenhuma «leitura natural tem»,
nos seis arquivos. Nenhum par de versos vizinhos com o mesmo esqueleto (conferido por script).

Fora da meta, de propósito (como no modelo): o choque abaixo da média dos mestres e o ternário acima; o
intervalo 4 fica um pouco alto em XXXIX, XL e XLIII (20–22%), por causa dos nomes e das palavras de
três sílabas antes da tônica; nenhum verso chega a ser marcado. Os versos longos (até 18–21 sílabas)
estão onde o original é hipermétrico ou tem enumeração: 2995–2997, 3119, Finnsburh 13, 24, 30.

## 5. Revisão de sentido e crítica

Revisão de sentido: cada verso conferido, no rascunho, com o glossário do próprio verso, as notas da
edição, Hall, Gummere e Morris e Wyatt (§ 3). Depois da passada de ritmo, cada canto foi relido lado a
lado com o original.

**Crítica.** A chamada ao subagente crítico foi interrompida (a ferramenta não chegou a rodar). Fiz então
eu mesmo, depois da revisão de ritmo, uma releitura crítica completa do lote, verso a verso contra o
original e o glossário (o de Finnsburh para o fragmento), com a lista do passo 4: sentido, ambiguidade,
gramática (crase, regência, concordância, colocação), mesóclise, desvio do guia, anglicismo. Aceitei e
corrigi (cada correção medida de novo no `verso-livre.mjs`):

- 2867 «os adornos de guerra em que estais de pé» (podia ler-se «sobre os quais») → «que trazeis aí».
- 2881 sujeito incerto («sempre ficava mais fraco» podia ser Beowulf) → «a serpe enfraquecia sempre…».
- 2887 «hão de acabar … à vossa raça» (regência) → «hão de faltar».
- 2897 «do último dia ou do regresso» → «e do regresso» (_bēga on wēnum_: na espera das duas coisas).
- 2908 «junto de Beowulf, o filho de Weohstan» (parecia aposição de Beowulf) → «o filho de Weohstan,
  junto de Beowulf».
- 2990 «Ele aceitou» (podia ser Eofor) → «O rei aceitou».
- 2998 três vogais (_e a Eofor_) → «e deu então a Eofor».
- 3015–3016 «o fogo … o fogo» (_brond_, _ǣled_) → «a fogueira … o fogo».
- 3031 «não mentiu muito / nos destinos nem nas palavras» (obscuro) → «nem nos fatos nem nas palavras»
  (_wyrda nē worda_: aqui _wyrd_ é o que aconteceu; registro a exceção ao «destino» do guia).
- 3053 concordância: «aquela herança … fora envolta».
- 3074 «aquele que pisasse aquele chão» → «quem pisasse aquele chão».
- 3082 «conselho algum / que não fosse atacar» (regência) → «de não atacar».
- 3113 «dar ordem … que a lenha…» → dois-pontos: «donos de casas: que a lenha da pira / trouxessem…».
- 3127 «quem saqueava» → «quem saquearia».
- 3128 «viram que parte alguma / ficava sem guarda» (dizia o contrário) → «que qualquer parte».
- 3142–3143 «o ilustre senhor / … o senhor amado» → «o ilustre rei / … o senhor amado».

Mantive, conferido com o glossário:

- 2910 «pelos mortos» (glossário) contra a leitura de Bugge adotada na tradução aliterativa.
- 3063–3066 como pergunta (glossário de _hwǣr_), contra Sievers.
- 2950 «o bom rei» para Ongentheow logo depois de «o bom rei» Hygelac (2945): é a mesma palavra no
  original (_se gōda_), e o nome de Ongentheow vem dois versos depois.
- 2980 «a velha espada dos gigantes … o elmo de gigantes» (_eotonisc_, _entisc_): a repetição é perda
  (o português não tem dois adjetivos para «de gigante»), como já notava a tradução aliterativa.
- 3029 o jogo _secg … secgende_ («o bravo varão ia contando») não passa.

## 6. Nomes e termos novos (não estão no guia)

- **Nomes**: os de Finnsburh seguem o § 9 (Sigeferth, Eaha, Ordlaf, Garulf, Guthere; _Secgan_ →
  secgas); Guthlaf, Hnæf, Hengest, Finnsburh, Wulf, Wonred, Eofor, Hrefnawudu, Hrefnesholt, Earnanæs,
  Hronesnæs, hugos, hetwaros, frísios, francos, merovíngio, wederas, Scylfings, Hrethlings pelo guia.
  _Wulf Wonrēding_ → «Wulf, filho de Wonred»; _Jofor_ → Eofor; _Gūð-scilfingas_ → «Scylfings guerreiros»
  e _Hæðcyn Hrēðling_ → «Hæthcyn, o Hrethling» (como em `../traducao-aliterativa/`).
- **Deus**: _āgend_ → o Dono; _sigora sōð-cyning_ → o Rei verdadeiro das vitórias (como em `../traducao-aliterativa/`).
- **Compostos e kennings**: _wīd-floga_ → voador das distâncias; _homera lāfe_ → herança dos martelos;
  _attor-sceaða_ → inimigo venenoso; _hild-latan_ → lerdos de batalha; _trēow-logan_ → traidores da fé;
  _fēðe-cempa_ → campeão a pé; _frum-gār_ → chefe das lanças; _ēored-geatwe_ → adornos de guerra;
  _līf-wraðu_ → amparo de vida; _ferhð-genīðla_ → inimigo mortal; _sinc-þego / swyrd-gifu_ → o receber
  de joias / o dom de espadas; _ēðel-wyn_ → alegria da pátria; _edwīt-līf_ → vida de opróbrio;
  _heaðo-weorc_ → obra da guerra; _haga_ → cercado; _ēg-clif_ → penhasco do mar; _bord-hæbbende_ →
  portadores de escudos; _wil-geofa_ → doador de graças; _dēað-bed_ → leito da morte; _wæl-rest_ →
  leito da matança; _ealdor-gewinna_ → inimigo da sua vida; _hēafod-weard_ → (velar a) cabeceira;
  _byrn-wiga_ → guerreiro de malha; _brim-wīsa_ → chefe do mar; _sweorda lāf_ → restos das espadas;
  _hēaðo-līðend_ → marujos de guerra; _freoðo-wong_ → campo da paz; _eorð-weall_ → muro de terra;
  _bord-weal_, _scild-weall_ → muro de escudos; _here-wīsa_ → chefe da hoste; _glēo-drēam_ → júbilo do
  canto; _hlim-bed_ → leito do repouso; _wundor-dēað_ → morte assombrosa; _lēg-draca_ → dragão de
  chamas; _eorð-scræf_ → grutas da terra; _searo-geþræc_ → monte de obras de arte; _īsern-scūr_ → chuva
  de ferro; _inwit-hrōf_ → teto hostil; _ǣled-lēoma_ → luz de fogo; _weall-clif_ → falésia; _frætwa
  hyrde_ → pastor dos adornos; _bǣl-fȳr_ → fogos fúnebres; _wudu-rēc_ → fumo da lenha; _giōmor-gyd_ →
  canto de luto; _word-gyd_ → canção de palavras; _wine-dryhten_ → senhor amigo; _woruld-cyning_ → rei
  deste mundo; _siglu_ → sóis de ouro.
- **Finnsburh**: _heaðo-geong_ → jovem na guerra; _grǣg-hama_ → manto cinzento; _gūð-wudu_ → madeira
  da guerra; _wēa-dǣda_ → feitos de desgraça; _gold-hladen_ → carregado de ouro; _wæl-sliht_ →
  matança; _bān-helm_ → elmo de osso; _buruh-þelu_ → chão do castelo; _eorð-būend_ → habitante da terra;
  _swurd-lēoma_ → luz das espadas; _sige-beorn_ → guerreiro de vitória; _hæg-steald_ → homem da casa;
  _driht-gesīð_ → companheiro; _here-sceorp_ → armadura; _hornas_ → galhadas.

## 7. Propostas para o guia

1. § 3 (Deus): _āgend_ → «o Dono» (3076) e _sōð-cyning_ → «o Rei verdadeiro» (3056).
2. § 5: _hlǣw_ → túmulo; _beorh_ → túmulo, e monte quando é o lugar da pira (já no § 9, falta na tabela).
3. § 9: _wyrd_ no plural com _word_ (_wyrda nē worda_, 3031) → «fatos», exceção ao «destino».
4. § 9: _hornas_ do salão (Finnsburh 4) → «galhadas», pelo modelo de _horn-gēap_ (canto II).

## 8. Conferência

- Versos: 71, 54, 112, 79, 47 e 48, iguais aos do original; nenhuma tabulação.
- Grep de mesóclise nos seis arquivos: nada.
- Aspas: abertas e fechadas nos versos de cada fala (contagem de “ e ” igual em cada arquivo); nenhuma
  aspa reta.
- Cabeçalhos iguais aos de `../traducao-aliterativa/` (o de Finnsburh: `# canto: Apêndice`, `# titulo: O combate em
  Finnsburh (fragmento)`).
- Temporários em `C:\Users\geren\AppData\Local\Temp\claude\beowulf-verso-livre-39-43\`. Nenhum commit.

## Crítica independente (feita depois, pelo coordenador)

Um crítico (Sonnet, esforço médio) conferiu o lote depois da entrega e apontou 15 itens; aceitos 14,
cada verso mudado medido de novo no `verso-livre.mjs` (nenhum marcado):

- 2859 «dispor dos feitos» → «reger os feitos» (glossário: _rule over_).
- 2881–2882 a serpe, sujeito e objeto: «sempre que eu a feria com a espada, / a inimiga mortal».
- 2885–2887 «à vossa raça» passa para depois do verbo («hão de faltar à vossa raça»).
- 2960–2961 _syððan_ → «depois que»; 2962 «Ongentheow foi ali» (dois «foi») → «Ali, pelos gumes das
  espadas, Ongentheow».
- 2978–2980 _lēt … brecan_: «fez … a larga espada» lia-se «fabricou» → «brandiu … e partiu o elmo».
- 3006–3007 os Scylfings como objeto de _gehēold_ (nota ao v. 3006: Beowulf os tinha submetido) →
  «também os bravos Scylfings; / ele fez o bem do povo».
- 3070 o _hit_ é o tesouro amaldiçoado, não Beowulf → «pois assim o tesouro amaldiçoaram».
- 3075 «Beowulf não tinha cobiça de ouro» (glossário, s.v. _gold-hwæt_: _he_ (Bēowulf)).
- 3142–3143 sujeito antes do objeto: «puseram então no meio, em pranto, os heróis / o ilustre rei».
- Finnsburh 13 «muito vassalo» (calco) → «mais de um vassalo»; 19–20 ordem; 22 «ele» → «Garulf»
  (quem pergunta; Sigeferth responde); 27 _swæðer_ → «a vida ou a morte» (nota da edição).

Recusado: 2947–2948 «o rastro … , o assalto mortal dos homens, foi visto»: verbo no singular com
aposição, correto.
