# Verso livre: cantos XXXI a XXXIV (versos 2145–2460)

Mesmo método dos cantos I e II (`notas.md`): do inglês antigo de Harrison e Sharp, um verso português
para cada verso do original, sem tabulação e sem imitar a medida aliterativa. Nomes, termos, fórmulas e
tratamento seguem `../CONVENCOES.md` (§§ 3–9); o § 2 foi posto de lado.

Arquivos: `31.txt` (78 versos), `32.txt` (90), `33.txt` (79), `34.txt` (69).

## 1. Método

1. Leitura do original com o glossário e as notas de Harrison e Sharp. Cada verso foi conferido com Hall
   (seções XXXI–XXXIV), Gummere e Morris e Wyatt. Gummere, nas lacunas de 2215–2231, segue as
   reconstruções de Bugge, e a tradução não as segue.
2. Rascunho verso a verso, e depois o ritmo pelo Versificador. Para medir:
   - as `# troca` de pronúncia foram aplicadas numa cópia com um script de substituição por palavra
     inteira (o `sed` com `\b` falhava no Git Bash);
   - a cópia foi medida com o `verso-livre.mjs`;
   - o `molde.mjs` foi rodado sobre o arquivo verdadeiro, com molde livre (`*`) e as mesmas `# troca`.
3. Revisão de sentido, verso a verso, contra o original e o glossário (§ 5).
4. Crítica de um subagente (Sonnet, esforço médio), depois da revisão de ritmo (§ 6).

**Trocas usadas**, além das do modelo:

| nome | troca |
|---|---|
| Hygelac | Híguelac |
| Wealhtheow | Uéltiou |
| Ecgtheow | Éctiou |
| Heoroweard | Hérouard |
| Hrethel | Hrétel |
| Hygd | Hid |
| Heardred | Hérdred |
| Hereric | Hérerric |
| Ohthere | Ócterre |
| Eadgils | Édguils |
| Herebeald | Hérebald |
| Hæthcyn | Hétquin |

A acentuação inicial segue a do inglês antigo, como nas trocas do modelo (Héorogar, Hélfdene).

**Linha só de pontos.** O verso 2219 é todo lacuna, e o motor do Versificador quebra num verso sem
nenhuma sílaba. Por isso ele foi tirado da cópia medida pelo `verso-livre.mjs`, que mostra 77 versos
para o canto XXXI, e não 78. O `molde.mjs` aceita o verso e o pula.

## 2. Escolhas gerais

- **Aposições** guardadas no lugar:
  - «o filho de Healfdene» (2148);
  - «o sábio senhor» (2157);
  - «o chefe dos Scyldings» (2160);
  - «o amparo dos nobres … — o rei forte na guerra —» (2191–2192). Os travessões vêm da crítica, § 6;
  - «um … um dragão» (2211–2212);
  - «o guardião dos anéis» (2246);
  - «o amparo dos combatentes … o senhor dos nobres» (2338–2339);
  - «o príncipe dos anéis» (2346);
  - «o senhor amigo do povo … o filho de Hrethel» (2358–2359);
  - «o elmo dos Scylfings, / o melhor dos reis do mar, / … o príncipe famoso» (2382–2385);
  - «o senhor dos tesouros, / o senhor amigo dos povos» (2429–2430).
- **Fórmulas**:
  - «Beowulf falou, o filho de Ecgtheow:» (2426);
  - «aquele era um bom rei!» (2391), igual ao I, 11;
  - «Ouvi dizer» (2164, 2173), para _hȳrde ic_;
  - «Assim deve agir um parente» (2167), para _swā sceal_.
- **Tratamento.** Beowulf fala a Hygelac por **tu** (2149–2152, 2156–2163). O último sobrevivente fala
  à terra por **tu**, e o _Hwæt!_ da fala dele virou «Vê!» (2249, guia § 9).
- **Deus**:
  - _god_ → Deus (2183);
  - _waldend_ → o Soberano (2293, 2330);
  - _ēce dryhten_ → o Senhor eterno (2331);
  - _Wyrd_ → o destino (2421, com minúscula, guia § 3).
- **Termos do guia**:
  - _gæst_ (o dragão, 2313; o ladrão, _gyste_, 2229) → hóspede;
  - _lyft-floga_ → voador do ar;
  - _wyrm_ → serpe;
  - _draca_ → dragão;
  - _beorh, hlǣw_ → túmulo;
  - _heorð-genēatas_ → companheiros da lareira;
  - _medo-benc_ → banco de hidromel;
  - _frēawine folca_ → senhor amigo do povo / dos povos;
  - _eorla hlēo_ → o amparo dos nobres;
  - _wīgendra hlēo_ → o amparo dos combatentes;
  - _sefa_ → coração;
  - _mōd_ → ânimo;
  - _dugoð_ → os veteranos;
  - _bill_ → lâmina;
  - _byrne_ → cota de malha;
  - _lind_ → tília;
  - _wergild_ (implícito em _feoh-lēas_) → «sem preço de sangue»;
  - _on burgum_ → nas cidadelas (como no II, 53).
- **Kennings e compostos**:

  | inglês antigo | tradução | verso |
  |---|---|---|
  | _hilde-sceorp_ | veste de batalha | 2156 |
  | _brēost-gewǣdu_ | veste do peito | 2163 |
  | _inwit-net_ | rede da malícia | 2168 |
  | _hond-gestealla_ | companheiro de mão | 2170 |
  | _hilde-hlæmm / hilde-hlemm_ | fragor (fragores) | 2202, 2352 |
  | _bord-hrēoða_ | abrigo dos escudos | 2204 |
  | _ūht-sceaða_ | o velho inimigo da madrugada | 2272 |
  | _nīð-draca_ | dragão de guerra | 2274; glossário: _battle-dragon_ |
  | _hord-wynn_ | a delícia do tesouro | 2271 |
  | _glēo-bēam_ | lenho do canto | 2264 |
  | _hioro-drync_ | tragos de espada | 2359 |
  | _sioleða bigong_ | o reino das baías | 2368; glossário: _realm of bights_ |
  | _gif-stōl_ | trono das dádivas | 2328 |
  | _lǣn-dagas_ | dias emprestados | 2342 |
  | _wīd-floga_ | aquele que voa longe | 2347 |
  | _hond-gemōt_ | encontros de mãos | 2356 |
  | _sāwle hord_ | o tesouro da alma | 2423 |
  | _horn-boga_ | arco de chifre | 2438 |
  | _wīn-sele_ | salão do vinho | 2457 |
  | _wind-gerest_ | pouso do vento | 2457 |
  | _gold-wine Gēata_ | o amigo do ouro dos geatas | 2420 |
- **Lacunas** no mesmo lugar do verso, sem completar. Só as palavras legíveis foram traduzidas:
  - 2217 _hond … hwylc_ → «a mão . . . qual»;
  - 2218 _since fāhne_ → «ornado de joias». Vai no masculino para não se ligar a «a mão»;
  - 2219, só pontos;
  - 2221 _þæt sie …_ → «que . . .»;
  - 2222 _folc-beorn_ → «o homem do povo»;
  - 2223 _wyrm-horda . . . cræft_ → «dos tesouros da serpe . . . o acervo»;
  - 2229 _þām gyste … stōd_ → «ao hóspede . . . se erguia»;
  - 2230 _earm-sceapen_ → «o mísero»;
  - 2231 _se fǣs begeat_ → «o perigo o tomou». Glossário: _fǣr_, ataque súbito, v. 2231;
  - 2362 _... XXX_ → «. . . trinta». Grein insere _āna_; não se completou.
- **Falas que atravessam seções.** O relato de Beowulf a Hygelac vem de `30.txt`: as aspas reabrem
  em 2145 e fecham em 2152, onde ele acaba. A fala de Beowulf que começa em 2427 continua em
  `35.txt`, e as aspas fecham no último verso de `34.txt` (2460). Os dois vizinhos, feitos por outros
  tradutores, já estão assim: `30.txt` fecha as aspas no fim e `35.txt` as reabre no começo.

## 3. Passagens revistas (sentido)

| verso | original | leitura adotada | apoio |
|---|---|---|---|
| 2148 | _on sīnne sylfes dōm_ | «por escolha dele mesmo» (de Hrothgar) | Glossário (_dōm_ 4: _according to his own choice_). Hall, Gummere e Morris, e a tradução aliterativa, entendem a escolha de Beowulf. O texto diz _sīnne_ (dele); Klaeber emenda para _mīnne_. |
| 2150–2151 | _Gēn is eall æt þē lissa gelong_ | «É ainda de ti / que depende todo favor» | Glossário (_gelong_: _all of favor is still on thee dependent_). Bugge: «sirvo agora só a ti». |
| 2153 | _eafor, hēafod-segn_ | «o javali, o estandarte»: duas coisas em aposição, como no texto | Glossário (_eafor_: a imagem do javali como estandarte). Wülker lê o composto _eafor-hēafodsegn_ (elmo); Kluge lê _ealdor_. |
| 2158 | _his ǣrest_ | «de onde ela vinha» | Nota ao v. 2158 (_ǣrest_ = origem) e glossário. |
| 2162 | _þēah hē him hold wǣre_ | «ainda que lhe quisesse bem»: o pai estimava o filho | Glossário (_hold_: _gracious, dear_); Hall e Gummere. A outra leitura é o filho leal ao pai. |
| 2165–2166 | _lungre gelīce … æppel-fealuwe_ | «iguais em tudo … fulvos como maçãs» | Glossário (_lungre_ 2: _quite_; _æppel-fealu_). |
| 2166 | _hē him ēst getēah_ | «e ao rei ele fez a dádiva» | «ao rei» deixa claro quem recebe (Hygelac). |
| 2175 | _þēodnes dōhtor_ | «a filha de um príncipe» | «a filha do senhor» podia passar por filha de Hrothgar. |
| 2180 | _nealles druncne slōg heorð-genēatas_ | «nunca matou os que bebiam com ele, / os companheiros da lareira» | Glossário (_druncne_: _who had drunk with him_). |
| 2183 | _gin-fæstan gife_ | «o dom abundante» | Glossário (_gin-fæst_: _extensive, rich_). |
| 2186–2187 | _micles wyrðne … gedōn wolde_ | «nem quis, no banco de hidromel, dar-lhe grande honra / o senhor das hostes» | Sujeito no fim, como no original. _drihten wereda_ é um senhor humano (Hygelac ou Hrethel), com minúscula. |
| 2196 | _seofan þūsendo_ | «sete mil», sem dizer de quê | Nota ao v. 2196 (talvez _hides_ de terra). |
| 2198–2200 | _lond gecynde … ōðrum swīðor sīde rīce, þām þǣr sēlra wæs_ | «pertencia na nação, por herança, a terra, / … e ao outro, mais ainda, / o vasto reino, àquele que ali era superior» | Glossário (_gecynde_: _natural, innate_). |
| 2205 | _on sige-þēode_ | «entre a tropa vencedora» | Glossário (_victorious warrior troop_). |
| 2206 | _Heaðo-Scilfingas_ | «os guerreiros Scylfings» | Como no II, 63 do modelo («o guerreiro Scylfing»). A tradução aliterativa diz «Scylfings da batalha». |
| 2213 | _on hēare hǣðe_ | «numa charneca cinzenta» | Glossário de _hār_ (cinzento) cita este verso; Hall: _grayish_. A tradução aliterativa diz «alta». |
| 2216 | _nēode_ | «com avidez» | Nota ao v. 2216 (H.-So.: _with desire, greedily_). |
| 2220 | _fyrena hyrde_ | «o guardião do mal» | Glossário: _the guardian of mischief, wicked one_. |
| 2223–2224 | _Nealles mid geweoldum … sōhte sylfes willum_ | «Nem por querer … / nem por vontade própria buscou quem tanto mal lhe fez» | O par «nem … nem» guarda as duas expressões do original (crítica, § 6). |
| 2228 | _syn-bysig_ | «acossado pela culpa» | Glossário: _guilt-haunted?_ |
| 2237 | _Ealle hīe dēað fornam_ | «A morte levara aquela gente toda» | Explicita que _hīe_ é a linhagem, não os tesouros. |
| 2240 | _wīscte þæs yldan_ | «quis um adiamento: / que por pouco tempo … pudesse desfrutar» | Glossário de _yldan_. |
| 2244 | _nearo-cræftum fæst_ | «de acesso vedado por artes» | Glossário: _art of rendering difficult of access_. |
| 2246 | _hard-fyrdne dǣl_ | «uma porção pesada» | Glossário: _hard to take away, heavy_. Bugge propõe _hard-fyndne_ (difícil de achar). |
| 2250 | _hit ǣr on þē gōde begeāton_ | «Foi de ti, outrora, / que os bons o tiraram» | Glossário de _begitan_: _received it formerly from thee_. |
| 2253 | _gesāwon sele-drēam_ | «tinham visto a festa do salão» | _drēam_ → festa, como no II, 88. |
| 2254 | _fetige_ | «traga» | Glossário (_fetian_: _to bring_). Outros leem _feormie_ (polir). |
| 2256–2257 | _Sceal se hearda helm … fǣtum befeallen_ | «O elmo duro, enfeitado de ouro, / há de perder as placas» | _Sceal_ passou ao verso seguinte, junto do particípio. |
| 2261–2262 | _brosnað æfter beorne … æfter wīg-fruman_ | «se desfaz depois do guerreiro … depois do chefe de guerra» | Repete «depois» como o original repete _æfter_. Glossário de _brosnian_: _after (the death of) the hero_. |
| 2263 | _næs hearpan wyn_ | «acabou-se o júbilo da harpa» | O pretérito do texto (_næs_), sem a emenda _nis_ de Koeppel, com sentido de presente. |
| 2266 | _bealo-cwealm_ | «a morte violenta» | Glossário. |
| 2276 | _wīde gesāwon_ | «por toda parte o viram» | Texto da edição. Gummere segue outra lição («dread him sore»). |
| 2276 | _gēwunian sceall_ | «A ele cabe habitar» | Glossário: _ge-wunian_, _to inhabit_. |
| 2277 | _hlāw under hrūsan_ | «o túmulo sob a terra» | Glossário de _hlāw_ (a câmara do túmulo); guia § 9. |
| 2281 | _ēacen-cræftig_ | «imensamente rica» | Glossário: _immense (of riches)_. |
| 2285 | _onboren bēaga hord_ | «saqueado o tesouro dos anéis» | Glossário (_on-beran_: _carried off_). A nota dá _inminutus_ (diminuído). |
| 2287 | _fīra fyrn-geweorc_ | «a obra antiga dos homens» (a taça) | Glossário. |
| 2292 | _unfǣge_ | «o não fadado à morte» | Glossário. |
| 2299 | _Hwæðre hilde gefeh_ | «Mas a serpe exultava na luta» | Texto defendido por H.-So. (nota ao v. 2299). «a serpe» explicita o sujeito: depois de «nenhum homem», o pronome deixaria dúvida. A emenda de Bugge faria do homem o sujeito. |
| 2302 | _goldes gefandod_ | «tinha mexido no ouro» | Glossário: _discovered the gold_. Ver § 4, três vogais. |
| 2304 | _earfoðlīce_ | «a custo» | Glossário: _could scarcely delay till it was evening_. Hall: «Not fain did the hoard-ward / wait». |
| 2306 | _līge forgyldan … drinc-fæt_ | «queria vingar com chamas / a querida taça» | |
| 2310–2312 | _Wæs se fruma egeslīc … sāre geendod_ | «Foi terrível o começo / … assim como logo / havia de acabar, com dor, no seu doador de joias» | Glossário de _fruma_ (o fim doloroso é a morte de Beowulf). |
| 2320 | _hord eft gescēat_ | «disparou de volta ao tesouro» | Glossário: _darted again back_. |
| 2326 | _þæt his sylfes him bolda sēlest_ | «que a sua própria casa, / a melhor das moradas» | «casa» deixa claro o sentido. O texto diz _him_; Bugge e ten Brink leem _hām_ (nota ao v. 2326). |
| 2335 | _ēa-lond ūtan, eorð-weard þone_ | «a terra cercada de água, por fora, e aquele domínio» | Glossário (_ēa-land_: _land surrounded by water_; _eorð-weard_: _land-property_). |
| 2343 | _ǣr-gōd_ | «bom desde outrora» | Glossário. |
| 2354 | _forgrāp_ | «esmagara» | Glossário: _to kill by the grasp_. |
| 2362–2363 | _hæfde him on earme ... XXX hilde-geatwa_ | «levava no braço . . . trinta / armaduras de guerra» | Nota ao v. 2362. |
| 2364–2365 | _hrēmge þorfton fēðe-wīges_ | «não tiveram razão de se gabar / da luta a pé» | Glossário de _hrēmig_. |
| 2379–2380 | _oð þæt hē yldra wearð … Hyne wræc-mæcgas_ | «até que Heardred cresceu / e foi o rei dos wedergeatas. A ele, os banidos» | Nota ao v. 2380 (_hyne_ = Heardred). O nome explícito tira a dúvida entre Heardred e Beowulf. |
| 2385 | _Him þæt tō mearce wearð_ | «Isso lhe marcou o fim» | Glossário: _mearc_, _the end of life_. |
| 2386 | _orfeorme_ | «ali, no banquete, recebeu ferida mortal» | O glossário dá _feorm_ 2, _banquet_, neste verso (leitura de Grein, _on feorme_). Outras leituras: «por hospedá-los» (tradução aliterativa); «sem sustento» (Wyatt). |
| 2393–2397 | _Ēadgilse wearð fēa-sceaftum fēond … hē gewræc syððan cealdum cear-sīðum, cyning ealdre binēat_ | «de Eadgils se tornou, / do desvalido, inimigo … e Beowulf se vingou depois / em frias jornadas de pesar, e tirou a vida ao rei» | Texto (_fēond_, emenda de Leo) e glossário (_cear-sīð_: _of Bēowulf's expeditions against Ēadgils_; _ge-steppan_: Eadgils atravessou o mar com guerreiros). O nome «Beowulf» em 2396 explicita o _hē_. A outra leitura (manuscrito _freond_; Bugge, Grein, Müllenhoff, Gummere, «friend to the friendless») faz de Beowulf aliado de Eadgils, que mata Onela. Ver § 8. |
| 2402 | _twelfa sum torne gebolgen_ | «um de doze, inchado de raiva» | Glossário de _gebelgan_ (sentido original: inchar). |
| 2414 | _wrǣtta and wīra_ | «de joias e filigranas» | Glossário: _wrǣt_, _ornament, jewel_; _wīr_, fio (de metal lavrado). |
| 2416–2417 | _næs þæt ȳðe cēap, tō gegangenne_ | «não era compra fácil, / de alcançar» | Glossário de _cēap_. |
| 2419 | _hǣlo ābēad_ | «saudava» | Glossário: _wished him health (greeted him)_. |
| 2422 | _grētan_ | «alcançar» | Glossário de _grētan_ 2: _to take hold of_. |
| 2437 | _morðor-bed strēd_ | «foi estendido o leito da morte» | Texto, não a emenda _stȳred_. |
| 2439 | _his frēa-wine_ | «ao seu senhor e amigo» | Texto, não _frēo-wine_ de Bugge. |
| 2441 | _blōdigan gāre_ | «com lança sangrenta» | Guia (_gār_ → lança). O glossário dá também _missile_; ver § 8. |
| 2442 | _feoh-lēas gefeoht, fyrenum gesyngad_ | «luta sem preço de sangue, de pecado perverso» | Nota ao v. 2442 (homicídio que nenhum pagamento resgata). |
| 2445–2450 | o pai cujo filho pende da forca | «um homem velho … quando o velho entoa a canção» | Hall, nota: um velho hipotético, não Hrethel. «o velho» deixa claro que é o pai quem canta. |
| 2450 | _in-frōd_ | «alquebrado» | Glossário: _very aged_. |
| 2454–2455 | _þonne se ān hafað þurh dēaðes nȳd dǣda gefondad_ | «já que o único / pela força da morte provou os feitos» | Texto, não as emendas de Müllenhoff e Bugge; glossário de _gefandian_. |
| 2456 | _Gesyhð_ | «Ele vê» | Sujeito explícito, para «Vê» não passar por imperativo. |
| 2458 | _rēote berofene_ | «privado do rumor» | Glossário: _rēot_, _noise, tumult?_; Bugge entende repouso. |
| 2459 | _in hoðman_ | «na cova» | Glossário: _place of concealment, cave; the grave_. |

## 4. Ritmo: o que o Versificador mostrou e o que mudou

**Primeiro rascunho**, sem as trocas aplicadas (o primeiro `sed` falhou; ver § 1):

| | marcados | pontuação final | sílabas por acento |
|---|---|---|---|
| XXXI | 4 | | |
| XXXII | 5 | 58,9% | |
| XXXIII | 6 | | 2,81, acima da meta |
| XXXIV | 4 | | 2,63, com 21,7% de versos com 4+ átonas |

Reescritas principais (antes → depois):

| verso | antes | depois | por quê |
|---|---|---|---|
| 2152 | parentes próximos, a não ser tu, Hygelac!” | parentes próximos, Hygelac, a não ser tu!” | choques (tu-Hí-) |
| 2162 | ao valente Heoroweard, embora o filho lhe fosse leal, | ao valente Heoroweard, ainda que lhe quisesse bem, | `ralo`; e a leitura de _hold_ (§ 3) |
| 2198 | pertencia naquela nação, por nascença, a terra, | pertencia na nação, por herança, a terra, | `vazio` |
| 2205 | quando o buscaram entre a tropa vitoriosa | quando foram buscá-lo, entre a tropa vencedora, | `ralo` |
| 2166–2167 | de um fulvo de maçã; e ele lhe fez a dádiva / dos cavalos e dos tesouros. Assim deve fazer o parente, | fulvos como maçãs; e ao rei ele fez a dádiva / dos cavalos e das joias. Assim deve agir um parente, | verso de 18 sílabas; sujeito incerto |
| 2208–2209 | Depois o vasto reino veio a Beowulf / às mãos | Depois, a Beowulf, o vasto reino / passou às mãos | regência e corte do verso |
| 2223 | Não foi de propósito que dos tesouros da serpe . . . | Nem por querer, dos tesouros da serpe . . . | `vazio`; depois, a crítica |
| 2230 | mas o desgraçado . . . | porém, o mísero . . . | `ralo` |
| 2255 | o vaso precioso de beber: os veteranos se foram para longe. | o caro vaso de beber: os veteranos se foram. | 21 sílabas |
| 2256–2257 | … enfeitado de ouro, há de perder / as suas placas: … | … enfeitado de ouro, / há de perder as placas: … | `ralo`; o verbo fica junto do particípio, como no original |
| 2261–2262 | se desfaz atrás do guerreiro. Os anéis da cota não podem / seguir o chefe de guerra para longe, | se desfaz depois do guerreiro. E os anéis da cota, / depois do chefe de guerra, não podem ir longe, | pontuação final baixa; repete o _æfter_ do original |
| 2271–2272 | A delícia do tesouro achou / o velho inimigo da madrugada, ali, aberta, | A delícia do tesouro, / o velho inimigo da madrugada achou aberta, | pontuação final |
| 2293–2294 | aquele que do Soberano / conserva a graça. | aquele que conserva / a graça do Soberano. | `ralo`, `vazio` |
| 2308 | como a serpe queria; não quis mais, junto à muralha, | como a serpe queria; e junto à muralha não quis mais | choques |
| 2324 | na sua guerra e na muralha: a esperança o enganou. | na guerra e na muralha: mentiu-lhe a esperança. | `ralo`; a imagem de _gelēah_ (mentir) |
| 2352–2353 | dos fragores da batalha, desde que de Hrothgar, / o varão vitorioso, purificara o salão, | dos fragores da guerra, desde que ele, de Hrothgar, / o varão vitorioso, limpara o salão, | `ralo`, `vazio` |
| 2363 | quando se lançou ao mar. | quando entrou no mar. | `vazio` |
| 2374 | Nem por isso os desvalidos conseguiram | Nem por isso os desvalidos puderam obter | `ralo` |
| 2380 | e reinou sobre os wedergeatas. | e foi o rei dos wedergeatas. | `ralo`, `vazio` («wedergeatas» tem uma tônica só) |
| 2394 | Com uma tropa cruzou | Com a tropa, passou | `ralo` |
| 2401 | em que contra a serpe tinha de lutar. | em que devia lutar contra a serpe. | `ralo` |
| 2419 | enquanto saudava os companheiros da lareira, | enquanto ali saudava os companheiros da lareira, | `ralo` |
| 2453 | de esperar dentro das suas cidadelas | de ver chegar, dentro das cidadelas, | `ralo`, `vazio`; e _gebīdan_ é «viver para ver» |
| 2444, 2448, 2458 | — | — | vãos de 4 átonas; em 2448, «doloroso» repetia o 2445 |

- **Pontuação final no canto XXXII** (58,9% no rascunho): o canto é muito encadeado, como o original.
  Uma vírgula onde a frase pedia pausa (2228, 2232, 2237, 2251, 2262) e as reescritas de 2261–2262 e
  2271–2272 levaram a 65,6%.
- **Três vogais seguidas.** Corrigidas:
  - _para o outro_ → «para ninguém» (2168);
  - _guardava, o audaz_ → «guardava, audaz» (2184);
  - _acabou-se a alegria_ → «acabou-se o júbilo» (2263);
  - _guarda o ouro_ → «guarda ouro» (2277);
  - _descoberto o ouro_ → «mexido no ouro» (2302);
  - _queria o odioso_ → «o odioso queria» (2306);
  - _luta o alegrava_ → «a serpe exultava na luta» (2299);
  - _contra a antiga_ → «contra a lei antiga» (2331);
  - _doloroso a um_ → recusada (2445).

  Ficaram as fusões comuns da fala (_e o único_, _sobre o estrondo_, _que a onda_).

**Resultado final** (`verso-livre.mjs`, com as trocas):

| | XXXI | XXXII | XXXIII | XXXIV | meta |
|---|---|---|---|---|---|
| versos | 78 (77 medidos) | 90 | 79 | 69 | = original |
| média de sílabas | 12,3 | 13,0 | 13,1 | 12,5 | |
| sílabas por acento | 2,52 | 2,64 | 2,76 | 2,60 | 2,4–2,8 |
| intervalos 1 (%) | 12,0 | 7,6 | 5,1 | 10,2 | ~15 |
| intervalos 2 (%) | 37,5 | 36,3 | 32,7 | 32,6 | ~30 |
| intervalos 3 (%) | 34,8 | 35,8 | 38,7 | 38,3 | ~29 |
| intervalos 4 (%) | 13,0 | 17,7 | 19,9 | 15,2 | ~16 |
| intervalos 5+ (%) | 2,7 | 2,5 | 3,7 | 3,8 | ~5 |
| versos com 4+ átonas seguidas | 10,4% | 10,0% | 13,9% | 14,5% | até 20–22% |
| terminam em pontuação | 77,9% | 65,6% | 75,9% | 76,8% | 65–100% |
| âncoras métricas | 12 | 5 | 15 | 7 | |
| versos marcados | 0 | 0 | 0 | 0 | 0 |

`molde.mjs` (molde livre, com as `# troca`): nenhum ✗, nenhum ≠, nenhuma «leitura natural tem», nos
quatro cantos.

**Fora da meta, de propósito.** O ternário passa um pouco do teto em XXXIII e XXXIV (38,7% e 38,3%).
O intervalo 4 também passa em XXXIII (19,9%), pelo vocabulário: _companheiros_, _cidadelas_,
_wedergeatas_, _desvalidos_. Como nos cantos I e II, o choque ficou abaixo da média dos mestres:
aparece só onde a fala o pede («bom rei», «não sei qual», «não quis mais»).

## 5. Revisão de sentido (antes da crítica)

Releitura verso a verso contra o original e o glossário. Mudou:

- **2175**, «a filha do senhor» → «a filha de um príncipe, e mais três cavalos». Antes, «com ele»
  deixava dúvida entre o colar e Beowulf.
- **2218**, «ornada» → «ornado». Concorda com o objeto perdido, e não com «a mão».
- **2224**, o sujeito ficou explícito.
- **2237**, «a todos eles» → «aquela gente toda».
- **2306**, «pagar com chamas a taça» → «vingar com chamas a taça».
- **2319**, «ao povo» → «o povo». A crítica fez voltar «ao povo» (§ 6).
- **2367**, «daquele guerreiro feroz» → «fugindo ao guerreiro feroz».
- **2379–2380**, «até que ele cresceu» → «até que Heardred cresceu», e então «A ele, os banidos».
- **2407**, «Era ele» → «Esse era». O ladrão, e não Beowulf.
- **2447**, «quando ele entoa» → «quando o velho entoa».
- **2456**, «Vê» → «Ele vê».

## 6. Crítica

**Como foi feita.** Um subagente crítico (Sonnet, esforço médio) recebeu:

- o original, a tradução, o guia, Hall, Gummere, Morris e Wyatt, e as notas e o glossário de Harrison
  e Sharp;
- a ordem de apontar até 15 problemas reais (sentido, ambiguidade, gramática, desvio do guia,
  anglicismo), sem comentar ritmo e sem editar nada.

Apontou 7. Todas as sugestões aceitas foram conferidas de novo no `verso-livre.mjs` e no `molde.mjs`.

Aceitos:

1. **2191–2192.** Em «Mandou … o amparo dos nobres trazer para dentro, / o rei forte na guerra, o legado
   de Hrethel», o rei parecia ser o objeto trazido. Ficou «— o rei forte na guerra — o legado de
   Hrethel»: os travessões fecham a aposição ao sujeito.
2. **2223–2224.** «Não foi por querer que … / buscou por vontade própria» parecia afirmar a vontade.
   Ficou «Nem por querer, … / nem por vontade própria buscou quem tanto mal lhe fez», que guarda as
   duas expressões do original (_mid geweoldum_, _sylfes willum_).
3. **2319.** «o destruidor de guerra o povo dos geatas / odiava» lê-se com o povo como sujeito. Voltou
   «ao povo dos geatas», com objeto direto preposicionado, de uso literário.
4. **2339–2340.** «todo de ferro» parecia descrever o rei. Ficou «o senhor dos nobres, um escudo todo
   de ferro, / de guerra, admirável».
5. **2211–2212.** «até que um começou, / nas noites escuras, um dragão, a reinar» tinha o «um» solto
   demais. Aceito em parte: a aposição _ān … draca_ ficou, como pede o guia, mas «um dragão» passou a
   abrir o v. 2212, colado ao «um» («até que um começou, / um dragão, a reinar nas noites escuras»).
   O crítico propunha fundir os dois numa palavra só.
6. **2334–2336.** «O dragão de fogo tinha a fortaleza do povo … / com brasas arrasado» lia-se como
   posse. Ficou «arrasara a fortaleza do povo, … / com as brasas.»
7. **2196.** «sete milhares» → «sete mil».

Recusado: nada. O crítico conferiu com o glossário os pontos disputados (2148, 2213, 2304, 2386,
2393–2397) e não os contestou.

## 7. Nomes e termos novos (fora do guia)

- **Nomes**: Heoroweard (2162) e Hereric (2207), na forma da tradução aliterativa. Os outros nomes do
  lote estão no guia: Hygd, Wealhtheow, Heardred, Ohthere, Eadgils, Herebeald, Hæthcyn, Hrethel,
  Ongentheow.
- **Povos**:
  - _Heaðo-Scilfingas_ → «os guerreiros Scylfings», como _Heaðo-Scilfing_ no II, 63. A tradução
    aliterativa diz «Scylfings da batalha»; convém fixar uma forma;
  - _Weder-Gēatas_ → wedergeatas (guia);
  - _Wederas_ → wederas;
  - _Hetware_ → hetwaros;
  - _Swīo-rīce_ → o reino dos suecos;
  - _Frēslondum_ → nas terras da Frísia.
- **Termos**:
  - _næs_ → cabo (2244, 2418), como nas notas da tradução aliterativa (29–32);
  - _melda_ → delator;
  - _hǣlo ābēodan_ → saudar;
  - _wræc-mæcgas_ → os banidos;
  - _ceorl_ → homem;
  - _hoðma_ → cova;
  - _fǣtt gold_ → ouro batido;
  - _fǣted wǣge_ → a taça adornada de ouro;
  - _drync-fæt_ → vaso de beber;
  - _sinc-fæt_ → taça (2232, 2301);
  - _māððum-fæt_ → vaso de joias;
  - _hord-weard_ → o guarda do tesouro;
  - _beorges hyrde_ → o guardião do túmulo;
  - _weard unhīore_ → um guarda sinistro;
  - _sinc-gifa_ → doador de joias;
  - _brego-stōl_ → trono de príncipe (2197, 2371, 2390);
  - _sibb_ → parentesco;
  - _lēod_ (título, 2160) → o chefe dos Scyldings;
  - _nīð-heard, nīða heard_ → duro nas pelejas;
  - _hilde-dēor_ → audaz na guerra;
  - _drihten wereda_ (senhor humano, 2187) → o senhor das hostes, com minúscula.

## 8. Dúvidas para o coordenador

1. **2393–2397.** Seguiu-se o texto e o glossário: Beowulf vira inimigo de Eadgils e o mata. O nome
   «Beowulf», em 2396, explicita o _hē_. A leitura do manuscrito e da maioria (Beowulf ajuda Eadgils
   contra Onela) mudaria «inimigo» para «amigo», e «Beowulf se vingou» para «ele se vingou». Se o canto
   35 de outro tradutor (2391–2396 são lembrados lá) seguir a outra leitura, convém harmonizar.
2. **2441, _gār_ → «lança».** Mantido o guia, mas é a flecha de Hæthcyn. O glossário dá também
   _missile_. «dardo» resolveria a estranheza sem trair a palavra: proposta para o guia (§ 9).
3. **_Heaðo-Scilfingas_**: «os guerreiros Scylfings» (modelo II, 63) ou «Scylfings da batalha»
   (tradução aliterativa).

## 9. Conferência

- Versos:

  | arquivo | traduzido | original |
  |---|---|---|
  | 31 | 78 | 78 |
  | 32 | 90 | 90 |
  | 33 | 79 | 79 |
  | 34 | 69 | 69 |

- Tabulação: 0 em cada arquivo.
- Grep de mesóclise: nada.
- Aspas:
  - 31: abrem em 2145 e fecham em 2152; abrem em 2156 e fecham em 2163;
  - 32: abrem em 2248 e fecham em 2267;
  - 34: abrem em 2427 e fecham em 2460 (a fala continua em 35).
- Cabeçalho `# canto` / `# titulo` com os títulos do § 8 do guia.
- Leitura do lote inteiro, de uma vez, depois da crítica.
