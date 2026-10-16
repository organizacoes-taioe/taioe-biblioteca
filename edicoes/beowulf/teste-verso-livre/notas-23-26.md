# Verso livre: cantos XXIII a XXVI (versos 1474–1817)

Mesmo método dos cantos I e II (`notas.md`): do inglês antigo de Harrison e Sharp, um verso português
para cada verso do original, sem tabulação, sem imitar a medida aliterativa. Nomes, termos, fórmulas e
tratamento seguem `../CONVENCOES.md` (§§ 3–6 e 9); onde o guia é omisso, a forma de `../traducao/`.

## 1. Método

1. Leitura do original com o glossário e as notas de Harrison e Sharp. Para não perder nenhum verso, um
   script listou, para cada número de verso de 1474 a 1817, todas as entradas do glossário que o citam,
   com o sentido dado ali; os casos disputados (§ 3) foram decididos por essa lista. Conferência com
   Hall (seções XXIII–XXVI, numeração por seção), Gummere (cuja numeração de seções está deslocada uma
   unidade) e as notas da edição.
2. Rascunho verso a verso.
3. Ritmo: `verso-livre.mjs` (numa cópia com as `# troca`) e `molde.mjs` em molde livre; mais um script
   que acusa esqueletos iguais em versos vizinhos e três vogais iguais seguidas (_dura a agarrou_).
4. Releitura de sentido e de língua (§ 5) e crítica independente (§ 6).

## 2. Escolhas gerais

- **Fórmulas**: «Beowulf falou, o filho de Ecgtheow:» (1474, 1652); _Hrōðgār maðelode, hylt
  scēawode_ (1688) → «Hrothgar falou; examinava o punho,» (a fala só começa em 1700, depois da
  descrição do punho, como no original). _Hwæt!_ nas falas → «Vê!» (1653, 1775: Beowulf e Hrothgar
  falam a um só, tratado por tu).
- **Tratamento**: tu entre Beowulf e Hrothgar; dual _wit_ → «nós dois» (1477, 1707), _unc_ → «nós dois»
  (1784).
- **Deus**: _hālig god_ → o santo Deus, _wītig drihten_ → o Senhor sábio, _rodera rǣdend_ → o regente
  dos céus (1554–1556, como em `traducao/`); _fæder_ → o Pai, _sōð metod_ → o verdadeiro Criador
  (1610–1612); _ylda waldend_ → o Soberano dos homens (1662); _ēce dryhten_ → o Senhor eterno (1693,
  1780); _waldend_ → o Soberano (1694); _mihtig god_ → Deus poderoso (1717, 1726); _wuldres waldend_ →
  o Soberano da glória (1753); _metod_ → o Criador (1779). Pronome de Deus em minúscula («ele guiou»,
  1664; «ele deixa», 1729).
- **Kennings e compostos** (a imagem, sem explicar): _gold-wine gumena_ amigo de ouro dos homens;
  _hond-gesella_ companheiro de mão; _bēaga brytta_ doador de anéis; _brim-wylm_ vaga do mar;
  _brim-wylf_ loba do mar; _grund-wyrgen_ loba do fundo; _mere-wīf_ mulher do lago; _hringa þengel_
  príncipe dos anéis; _leoðo-syrce_ camisa de elos dos membros; _nið-sele_ salão do abismo;
  _hrōf-sele_ teto do salão; _fǣr-gripe flōdes_ súbito aperto da enchente; _beado-lēoma_ luz da
  batalha (guia); _hring-mǣl_ espada de anéis; _gūð-lēoð_ canto de guerra; _wunden-mǣl_ espada
  ondeada; _brēost-net_ rede do peito; _here-net_ rede de guerra; _bān-hringas_ anéis dos ossos;
  _flǣsc-homa_ manto de carne; _rodores candel_ candeia do firmamento; _heorð-genēatas_ companheiros
  da lareira; _hilde-gicel_ sincelo de guerra; _lid-manna helm_ elmo dos navegantes; _wæl-steng_
  lança da matança; _meodo-wongas_ campos do hidromel; _heaðo-swāt_ suor de batalha; _brēost-hord_
  tesouro do peito; _hlēo-burh_ burgo que abriga os homens; _sāwele hyrde_ pastor da alma;
  _flān-boga_ arco de flechas; _niht-helm_ elmo da noite; _heofones wyn_ alegria do céu; _gūð-wine_
  amigo de guerra (a espada); _ecg-hete_ ódio dos gumes (como em 02, v. 84).
- **Termos do guia**: _gist / gæst / sele-gyst_ → hóspede (1522, 1546, 1603, 1801); _ellor-gǣst /
  ellor-gāst_ → espírito estranho (1617, 1622); _āglǣca_ (Beowulf, 1513) → o temível; _lēod_ como
  título (_Weder-Gēata lēod_, _Gūð-Gēata lēod_) → o chefe dos wedergeatas / dos geatas guerreiros
  (como em `traducao/`); _dugoð and geogoð_ → os veteranos e os jovens; _æsc_ → freixo (1773);
  _middan-geard_ → terra-média; _ofer-hygd_ → soberba; _gylp_ → jactância; _sefa_ → coração; _mōd_ →
  ânimo; _cempa_ → campeão; _ides_ → a dama (1650, a rainha); _seax_ → punhal.
- **Fala que atravessa a seção**: o discurso de Hrothgar começa em 1700 (`25.txt`, v. 50) e acaba em
  1784 (`26.txt`, v. 40): as aspas fecham no último verso de `25.txt` e reabrem no primeiro de `26.txt`
  (guia, § 6). As outras falas (1475–1492, 1653–1677) cabem num arquivo. O último verso de `22.txt` é
  narração e o primeiro de `27.txt` abre fala nova: nada depende de outro lote.

## 3. Passagens revistas (sentido)

| verso | original | leitura adotada | apoio |
|---|---|---|---|
| 1478–1480 | _gif ic æt þearfe þīnre scolde aldre linnan, þæt þū mē ā wǣre forð-gewitenum on fæder stǣle_ | «se eu, quando de mim precisasses, viesse / a perder a vida, tu havias de estar sempre / para mim, depois de morto, em lugar de pai» | glossário (_forð-gewitenum_ = _me defuncto_; _on fæder stǣle_); nota ao v. 1480 |
| 1489–1491 | _lǣt … Unferð … ealde lāfe, wrǣtlīc wǣg-sweord, wīd-cūðne man, heard-ecg habban_ | «deixa que Unferth, o homem de vasta fama, / tenha a velha herança, a espada pesada e lavrada, / a de gume duro» (a aposição sobe um verso) | glossário: _wǣg-sweord_ = _heavy sword_ (não «espada de ondas»; Kl. lê _wæl-sweord_, nota ao v. 1490). O glossário põe «(Bēowulf)» ao lado de _wīd-cūðne man_, mas pela construção (_lǣt_ + acusativo) o homem de vasta fama só pode ser Unferth, como em Hall e Gummere; parece lapso do glossário. |
| 1496 | _Þā wæs hwīl dæges_ | «Passou-se então o espaço de um dia» | glossário: _the space of a day_ |
| 1498–1501 | _Sōna þæt onfunde, sē þe flōda begong … behēold … þæt þǣr gumena sum æl-wihta eard ufan cunnode_ | «Logo o notou aquela que a extensão das águas … guardara …: que um dos homens, lá de cima, / sondava a morada dos monstros» (quem percebe é a mãe de Grendel) | glossário (_on-findan_, _sē_ por _sēo_ em 1498; _æl-wiht_ = _monster_) |
| 1499 | _heoro-gīfre … hund missēra_ | «ávida de assaltos, guardara cem semestres» | glossário: _eager for hostile inroads_; _missēre_ = meio ano (são cinquenta anos; o número fica como no original) |
| 1509 | _(hē þæs mōdig wæs)_ | «(coragem não lhe faltava)» | glossário: _had the courage for it_ |
| 1512 | _hilde-tūxum here-syrcan bræc_ | «investia com presas de guerra contra a camisa de malha» | glossário de _brecan_: a fera _pressed upon the shirt of mail_, sem rompê-la (a malha está intacta em 1549, 1553). Hall e Gummere: _break through_. |
| 1513 | _ēhton āglǣcan_ | «perseguiam o temível» (Beowulf) | glossário (_āglǣca_ 2: herói, com dúvida); guia, § 5 |
| 1514–1517 | _nið-sele nāt-hwylcum … for hrōf-sele_ | «sem saber qual, num salão do abismo … por causa do teto do salão» | glossário (_hall in the deep_); nota ao v. 1514 |
| 1529 | _þæt wæs forma sīð dēorum māðme, þæt his dōm ālæg_ | «foi a primeira vez / para o caro tesouro que a sua glória falhou» | glossário (_dōm_, _ā-licgan_) |
| 1538 | _be eaxle_ | «pelo ombro» | texto da edição; Sweet e outros leem _be feaxe_, «pelos cabelos» (nota) |
| 1543 | _and-lēan_ | «lhe devolveu a paga» | texto da edição (o manuscrito tem _hand-lēan_, nota) |
| 1544 | _oferwearp_ | «tropeçou» (intransitivo; sujeito Beowulf) | glossário: _to stumble_ |
| 1556–1557 | _rodera rǣdend hit on ryht gescēd, ȳðelīce syððan hē eft āstōd_ | «o regente dos céus decidiu com justiça, / e então, sem custo, ele se pôs de pé» | glossário: _ȳðelīce hē eft āstōd_ = _he easily arose afterwards_; nota ao v. 1557 (a pontuação de Heyne-Socin liga _ȳðelīce_ a _gescēd_) |
| 1564 | _fetel-hilt, freca Scildinga_ | «o punho de correntes o audaz guerreiro dos Scyldings» | glossário: _fetel-hilt_ com correntes de ouro; _freca_ (propriamente «lobo») como designação de herói, aqui Beowulf |
| 1567 | _heard grāpode_ | «o duro ferro a colheu pelo pescoço» | glossário: _the sword griped hard at her neck_ |
| 1584 | _ōðer swylc_ | «outros tantos» | nota ao v. 1584 (Heyne; Sweet: «outros quinze») |
| 1585–1587 | _tō þæs þe hē on ræste geseah gūð-wērigne Grendel licgan_ | «o campeão feroz, e assim viu no leito / Grendel deitado ali, exausto da guerra»; o corte da cabeça (1590) leva o nome, «e Beowulf então lhe cortou a cabeça», porque o sujeito anterior é o cadáver | Hall, Gummere |
| 1599 | _þā þæs monige gewearð_ | «pois muitos concordaram nisto» | glossário (impessoal, _to agree_); nota ao v. 1599 (Hall) |
| 1605 | _wiston and ne wēndon_ | «não sabiam, nem esperavam, ver o seu senhor amigo / em pessoa» | glossário (s.v. _nē_: _knew not and weened not_). Cosijn emenda _wīscton_, «desejavam» (nota), que Hall e Gummere seguem: _wished and yet weened not_. |
| 1611 | _wæl-rāpas_ | «os grilhões das águas» | glossário: _flood-fetter, i.e. ice_ |
| 1617 | _brōden mǣl_ | «a lâmina lavrada» | nota ao v. 1607 (espada tauxiada) |
| 1622 | _ēacne eardas_ | «as vastas extensões» | glossário; Bugge lê _eatna eardas_, «as moradas dos gigantes» (nota) |
| 1631 | _lagu drūsade_ | «o lago estava parado» | glossário: _to stagnate_ |
| 1635 | _cyning-balde men_ | «homens de régia coragem» | glossário (_nobly bold_, com dúvida); Bugge: _cyning-holde_, «fiéis ao rei» |
| 1637–1638 | _earfoðlīce heora ǣghwæðrum fela-mōdigra_ | «e a cada um deles custava muito, / por valentes que fossem» | glossário (_earfoð-līce_; _fela-mōdig_ = _very courageous_); Gummere |
| 1650 | _þǣre idese_ | «a dama» (a rainha) | nota ao v. 1650 |
| 1658–1659 | _æt-rihte wæs gūð getwǣfed, nymðe mec god scylde_ | «quase teria a luta / chegado ao fim, se Deus não me guardasse» | glossário: _almost had the struggle been ended_ |
| 1664–1665 | _eald sweord ēacen (oftost wīsode winigea lēasum)_ | «uma velha espada pesada (muitas vezes ele guiou / quem não tinha amigos)» | glossário: _ēacen_ = _great, heavy_; sujeito do inciso: Deus (1662). Bugge propõe _eotenisc … ēste_ (nota). |
| 1666 | _þā mē sǣl āgeald_ | «(quando a hora me foi dada)» | glossário: _when the favorable opportunity offered itself_ |
| 1676–1677 | _on þā healfe, aldor-bealu eorlum_ | «deste lado, / a morte para os nobres» | glossário: _thou needest not fear death for the courtiers_ |
| 1687 | _on Sceden-igge_ | «em Scedeland» | guia, § 4 (Scedeland vale para _Scede-landum_ e _Scedenig_); a tradução aliterativa usou «Scedenig» |
| 1692 | _frēcne gefērdon_ | «tinham-se portado com audácia» | glossário: _had shown themselves daring_ (a tradução aliterativa leu «terrível sorte tiveram») |
| 1695 | _scennum_ | «nas guardas» (da espada) | glossário: _sword-guard?_ |
| 1703–1704 | _þæt þes eorl wǣre geboren betera_ | «que este nobre / nasceu melhor!» | glossário: _that this nobleman is better born_; texto da edição, não a emenda de Bugge (_nǣre_, «que não há nobre mais bem-nascido do que tu», nota) |
| 1709 | _eal lang-twidig_ | «concedido por longo tempo» | glossário: _long-granted, assured_ |
| 1715 | _āna hwearf_ | «partiu sozinho» | nota ao v. 1715 (morreu só) |
| 1720 | _brēost-hord blōd-rēow_ | «um sanguinário tesouro do peito» | glossário: _a bloodthirsty feeling_; guardado o kenning |
| 1721 | _æfter dōme_ | «como era de uso» | glossário: _according to custom_ |
| 1723 | _lēod-bealo longsum_ | «um longo mal do povo» | glossário; Bugge: tormento eterno (nota) |
| 1729 | _on lufan_ | «voltar-se para os bens» | glossário (_lufa_ = _property_), nota ao v. 1729 |
| 1736 | _nō hine wiht dweleð_ | «nada o detém» | glossário: _nor does aught check him_ |
| 1748 | _wom wundor-bebodum_ | «do mal, das estranhas ordens» | glossário (_wam_ substantivo; Kl. lê _wōm_, «tortas») |
| 1750 | _nallas on gylp seleð fǣtte bēagas_ | «não dá, em paga de jactâncias, / anéis lavrados de ouro» | glossário s.v. _gilp_: _gives no chased gold rings for a boastful speech_; a outra glosa do glossário é «como prometera»; Bugge: _on gyld_, «em recompensa» (nota) |
| 1757 | _unmurnlīce_ | «sem pena» | glossário: _without sorrowing_ |
| 1761 | _ēce rǣdas_ | «os ganhos eternos» | glossário: _the eternal gain_ |
| 1784 | _wīgge weorðad_ | «honrado na guerra» | glossário: _wīg-ge-weorðad_ (conjectura de Cosijn, nota) |
| 1795–1798 | _sele-þegn … þegnes þearfe_ | «um camareiro … as precisões do vassalo» (o vassalo é Beowulf) | glossário: _sele-þegn_ = _chamberlain_; _þearf_: _all the thane's needs_ |
| 1799 | _hēaðo-līðende_ | «os homens do mar» | glossário: _sea-farer, sailor_ |
| 1803–1804 | _Þā cōm beorht sunne scacan ofer grundas_ | «Veio então o sol brilhante / deslizando sobre os campos» | texto e glossário; Sievers emenda (nota) |
| 1804 | _scaðan_ | «os guerreiros» | glossário (_sceaða_ 2) |
| 1808–1813 | _Heht þā se hearda Hrunting beran sunu Ecglāfes … sægde him þæs lēanes þanc_ | «Mandou então o valente que levasse Hrunting / o filho de Ecglaf, que tomasse a sua espada, / … agradeceu-lhe o empréstimo» | o glossário dá _sunu_ (1809) como **acusativo** e _lēan_ como _loan_: Beowulf (_se hearda_) manda Unferth levar de volta a espada e agradece o empréstimo. Diverge da tradução aliterativa, que fez de _sunu_ nominativo (Unferth manda). Hall entende ao contrário (Unferth dá a espada de presente); Gummere, como aqui. |
| 1815 | _weorð Denum_ | «caro aos dinamarqueses» | glossário: _the atheling dear to the Danes_ |

## 4. Ritmo: o que o Versificador mostrou e o que mudou

Primeiro rascunho: 23 com 5 versos marcados; 24 com 6; 25 com 18; 26 com 10. As causas foram quase
sempre as mesmas: palavras longas sem acento secundário reconhecido (_dinamarqueses_, _perseguição_,
_necessidade_, _wedergeatas_), artigo e preposição em fila (_mas o Soberano dos homens me concedeu_),
e o demonstrativo _naquele_, que a leitura natural não acentua.

Reescritas principais (antes → depois):

| verso | antes | depois | por quê |
|---|---|---|---|
| 1478 | que, se na tua necessidade eu viesse | que, se eu, quando de mim precisasses, viesse | `ralo`, `vazio` (3 acentos em 13 sílabas) |
| 1493 | (sem troca) _wedergeatas_ lido como palavra de um acento | `# troca: wedergeatas => wéder-geatas` | o composto tem acento secundário em _we-_; sem a troca o programa via 6 átonas seguidas |
| 1508 | o príncipe dos anéis para a sua morada, | o príncipe dos anéis à morada dela, | `ralo`, `vazio`; e «dela» diz de quem é a morada |
| 1557 | e com facilidade ele se ergueu, então. | e então, sem custo, ele se pôs de pé. | `vazio` |
| 1494–1504 | partiu com coragem… / antes que ele pudesse avistar a planície do fundo / sedenta de assaltos, guardara por cem semestres / … | lançou-se com coragem… / antes que pudesse ver o chão do fundo / ávida de assaltos, guardara cem semestres / … | série de intervalos de 3 (o canto tinha 42% de ternário) |
| 1558 | Viu então entre as armas uma lâmina vitoriosa, | Viu então, entre as armas, a lâmina bendita de vitórias, | `vazio` |
| 1561 | só que era maior do que qualquer outro homem | só que era maior do que outro homem qualquer | `choques` |
| 1572 | tal como do céu, serena, resplandece | tal como brilha, serena, lá do céu | `ralo` |
| 1612 | dos tempos e das estações: esse é o Criador verdadeiro. | das estações e dos tempos: esse é o verdadeiro Criador. | `vazio` |
| 1628 | o valente bando de vassalos, alegraram-se pelo senhor, | a tropa seleta dos vassalos, contentes pelo senhor, | `ralo`, `vazio`; _þrȳðlīc_ = escolhido (glossário) |
| 1662–1663 | mas o Soberano dos homens me concedeu / que eu visse… | mas o Soberano dos homens me deu a graça / de ver… | `ralo`; regência |
| 1671 | a matança dos dinamarqueses, como era devido. | a matança do povo dinamarquês, como era justo. | `ralo`, `vazio` |
| 1682 | obra de ferreiros prodigiosos; e quando deixou este mundo | obra de ferreiros portentosos; quando o mundo deixou | `ralo`, `vazio` |
| 1697 | posto e dito, para quem a espada, | posto e dito, para quem fora a espada, | `vazio` |
| 1707–1709 | a força com a sabedoria do ânimo… / a minha amizade, como dissemos nós dois; tu hás de ser um consolo / por longo tempo seguro para o teu povo, | a força com o saber do ânimo… / a amizade, como já dissemos nós dois; serás um consolo / concedido por longo tempo ao teu povo, | `vazio`, `choques`, `vazio`; e _lang-twidig_ fica mais perto do glossário |
| 1712–1713 | não cresceu para alegria deles, mas para a matança / e para a morte violenta das gentes dinamarquesas; | não cresceu para o bem deles, e sim para a matança / e para a morte cruel das gentes dinamarquesas; | `vazio`, `ralo` |
| 1717, 1726 | embora o poderoso Deus… / como o poderoso Deus… | mesmo que Deus poderoso… / como Deus poderoso… | `ralo`, `vazio` |
| 1732, 1735, 1737 | a fortaleza dos homens / na sua insensatez, imaginar onde ele acaba / nem a mágoa da perfídia | o burgo que abriga os homens / na sua falta de siso, pensar onde acaba / nem mágoa de traição | `ralo`, `vazio`, `ralo` |
| 1757 | que reparte os tesouros sem lamentar, | que distribui sem pena os tesouros, | `ralo` |
| 1777–1778 | o velho inimigo, o meu invasor: / daquela perseguição eu sofri sem cessar | o velho inimigo, o intruso em minha casa: / daqueles ataques eu sofri sem cessar | `ralo`, `vazio` |
| 1798 | as precisões do vassalo, tais como naqueles dias | as precisões do vassalo, tais como, nesse tempo, | `ralo`, `vazio` |
| 1815 | estavam os guerreiros, foi o querido dos dinamarqueses, | estavam os guerreiros, foi, caro aos dinamarqueses, | `vazio` |
| 1567, 1569, 1661, 1783 | dura a agarrou / morte, e ela / embora a arma / goza a alegria | o duro ferro a colheu / morte; ela / ainda que a arma / goza o prazer | três vogais iguais seguidas |

**Resultado final** (`verso-livre.mjs`, com as `# troca`):

| | canto XXIII | canto XXIV | canto XXV | canto XXVI | meta |
|---|---|---|---|---|---|
| versos | 84 | 94 | 94 | 72 | = original |
| média de sílabas | 13,1 | 12,9 | 12,9 | 12,9 | |
| sílabas por acento | 2,58 | 2,64 | 2,62 | 2,66 | 2,4–2,8 |
| intervalos 1 / 2 / 3 / 4 / 5+ (%) | 6,7 / 39,9 / 38,8 / 11,4 / 3,2 | 7,7 / 33,0 / 37,9 / 16,8 / 4,7 | 8,4 / 38,6 / 32,3 / 16,6 / 4,1 | 9,0 / 33,1 / 36,3 / 18,0 / 3,6 | ~15 / 30 / 29 / 16 / 5 |
| versos com 4+ átonas seguidas | 13,1% | 18,1% | 16,0% | 11,1% | até 22% |
| versos que terminam em pontuação | 71,4% | 73,4% | 70,2% | 70,8% | 65–100% |
| âncoras métricas | 14 | 19 | 12 | 11 | uma ou duas a cada 6–8 versos |
| versos marcados (`ralo`, `vazio`, `choques`) | 0 | 0 | 0 | 0 | 0 |

`molde.mjs` (molde livre, `*`, com as `# troca`): nenhum ✗, nenhum ≠, nenhuma «leitura natural tem»
nos quatro cantos.

Fica fora das metas, de propósito ou por limite: o choque (intervalo 1) baixo, como nos cantos I e II
(o tom é narrativo e solene); o ternário perto de 38% em 23 e 24, pelas mesmas paroxítonas de
três sílabas que os cantos I e II já mostravam (37–39%); o intervalo 4 em 26 no limite (18%), pelos
versos longos do sermão. Os versos 1765–1766 (_oððe fȳres feng oððe flōdes wylm, / oððe gripe mēces
oððe gāres fliht_) têm o mesmo esqueleto (3-6-9-12) de propósito: é a enumeração anafórica do
original («ou o aperto do fogo, ou a fúria da enchente, / ou o golpe da espada, ou o voo da lança»).

## 5. Revisão de sentido e língua (antes da crítica)

- 1572: «sereno» não concordava com «a candeia» → «serena».
- 1586–1587: «viu no leito, estendido, / Grendel deitado ali» repetia a ideia → «e assim viu no leito».
- 1605: «se ao seu senhor amigo / em pessoa veriam» (objeto preposicionado) → «se o seu senhor amigo».
- 1629: volta a «vê-lo são e salvo», como no original (_gesēon_).
- 1720: «um tesouro do peito sanguinário» deixava «sanguinário» no peito → «um sanguinário tesouro do
  peito».
- 1780: «por ter vivido para ver / que … eu a contemple» misturava os tempos → «por ter alcançado em
  vida / que …».

## 6. Crítica

Um crítico (Sonnet, esforço médio) conferiu os 344 versos com o original, Hall, Gummere, o guia e o
glossário (com a lista, dada a ele, das decisões já tomadas pelo glossário). Apontou 15 itens; nenhuma
mesóclise, nenhum desvio de nomes, fórmulas ou aspas. Aceitos, cada um conferido de novo no
`verso-livre.mjs` e no `molde.mjs`:

- 1498–1500: «Logo percebeu aquela que…» deixava dúvida sobre quem percebe (é a mãe de Grendel, _sē þe
  flōda begong … behēold_; quem sonda de cima é Beowulf) → «Logo o notou aquela que a extensão das
  águas, / … / cruel e voraz: que um dos homens, lá de cima, / sondava…».
- 1489–1490: «o homem de vasta fama» ficava colado à espada → «E tu deixa que Unferth, o homem de vasta
  fama, / tenha a velha herança, a espada pesada e lavrada,» (a aposição sobe um verso, dentro da
  frase).
- 1538–1539 e 1564: sujeito e objeto justapostos → «Então o chefe dos geatas guerreiros (a contenda
  não o assustava) / agarrou pelo ombro a mãe de Grendel;» e «O audaz guerreiro dos Scyldings pegou
  então o punho de correntes,».
- 1555: tempo verbal → «não tivesse regido a vitória».
- 1591: «e ele então lhe cortou a cabeça» (o sujeito anterior é o cadáver) → «e Beowulf então…».
- 1599: «o seu senhor famoso» sugeria Hygelac (é Hrothgar, _mǣrne þēoden_) → «o senhor famoso».
- 1605–1606: regência («esperavam se») → «não sabiam, nem esperavam, ver o seu senhor amigo / em
  pessoa.».
- 1637–1638: «para cada um» soava como beneficiário → «e a cada um deles custava muito, / por valentes
  que fossem» (_heora ǣghwæðrum fela-mōdigra_; a concessiva interpreta o genitivo, como Gummere).
- 1680–1681 e 1685–1687: inciso que partia a frase → «passou a pertencer, / depois da queda dos
  demônios, ao senhor dos dinamarqueses,» e «passou ao poder, dos reis do mundo, / do mais excelente
  entre os dois mares, / dos que davam riquezas em Scedeland.».
- 1690–1691: a aposição «o mar que jorrava» entre verbo e objeto → «quando o dilúvio, / o mar que
  jorrava, matou a raça dos gigantes».
- 1702–1704: «lembra tudo o que vai longe» → «recorda tudo desde longe»; «nasceu de estirpe mais alta»
  acrescentava «estirpe» → «nasceu melhor!» (_geboren betera_, como o original, sem segundo termo).
- 1795–1798: «vassalo» designava o camareiro e o hóspede → _sele-þegn_ «camareiro» (glossário:
  _chamberlain_), e «as precisões do vassalo» fica para Beowulf.
- 1585–1587 e 1780–1782: já corrigidos na revisão do § 5 quando a crítica chegou.

Recusados:

- 1708–1709, «concedido por longo tempo»: o crítico o tomou por acréscimo, mas é o sentido que o
  glossário dá a _lang-twidig_ (_long-granted, assured_).
- «Precisões» (1526, 1798) como anglicismo: _precisão_ = necessidade é português antigo e literário (a
  tradução aliterativa usa a mesma palavra); ficou.

## 7. Nomes e termos novos (fora do guia)

- **Nomes**, na forma do guia ou de `traducao/`: Hrethel (_sunu Hrēðles_, 1486), Hrunting, Unferth,
  Ecglaf, Heremod, Ecgwela; _Ār-Scyldingas_ → **os honrados Scyldings** (1711, como em `traducao/`);
  _West-Dene_ → dinamarqueses do oeste (guia); _Hring-Dene_ → dinamarqueses dos anéis (guia);
  _Sceden-ig_ → Scedeland (guia).
- **Pronúncia** (`# troca` acrescentadas ao molde): Hygelac => Hígelac; Ecgtheow => Éctiou; Hrethel =>
  Hrétel; Unferth => Únfert; Hrunting => Hrúnting; Heremod => Héremod; Ecgwela => Écuela; Ecglaf =>
  Éclaf; Scylding => Scílding; wedergeatas => wéder-geatas (acento secundário do composto).
- **Termos**: _missēre_ → semestre (_hund missēra_ → cem semestres, 1499 e 1770, como em `26` da
  tradução aliterativa; em `23` ela usou «meios-anos»: proponho «semestres» nos dois lugares);
  _wǣg-sweord_ → espada pesada (glossário; a tradução aliterativa tem «espada de ondas»); _wunden-mǣl_
  → espada ondeada; _hilde-rinc_ → guerreiro (da batalha); _nōn dæges_ → a hora nona; _sceattas_ →
  riquezas; _sele-þegn_ → camareiro; _rand-wiga_ → guerreiro de escudo; _cuma_ → visitante;
  _yppe_ → estrado.

## 8. Proposta para o guia

- § 4: registrar que **Scedeland** vale também para _Sceden-ig_ (1686), para que os lotes não
  divirjam (a tradução aliterativa tem «Scedenig» em `25.txt`).
- § 5 ou § 9: _wǣg-sweord_ (1490) → «espada pesada», como manda o glossário.
- § 9: XXVI, 1808–1810: decidir uma leitura só (a do glossário: Beowulf devolve Hrunting e agradece o
  empréstimo), porque a tradução aliterativa seguiu a outra.

## 9. Conferência

- Versos: 84 (1474–1557), 94 (1558–1651), 94 (1652–1745), 72 (1746–1817), iguais ao original; sem
  tabulação.
- Grep de mesóclise: nada.
- Aspas: 1475–1492; 1653–1677; 1701–1745 (fecha no fim de `25.txt`) e 1746–1785 (reabre no começo de
  `26.txt`).
- Cabeçalhos com os títulos do guia, § 8.
