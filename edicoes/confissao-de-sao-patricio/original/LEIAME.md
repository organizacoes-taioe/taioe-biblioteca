# Confessio de São Patrício: texto latino (base)

**Base:** Newport J. D. White, *Libri Sancti Patricii* (Londres, SPCK, 1918; Texts for Students, n. 4), p. 5–26:
os 62 parágrafos numerados por ele (`[n]` em `confessio.txt`), 4.650 palavras. Sem aparato, notas, referências
bíblicas nem cabeços; o itálico das citações bíblicas saiu sem marca; æ/œ viraram ae/oe; a hifenização de fim de linha e de
página foi desfeita. Grafia e pontuação de White como impressas: u por v e i por j (`Uillulam`, `uico`),
`inperfectus`, `inpendi`, `adpeto`, `obprobrium`, `cotidie`, `caeteri`, `sepe` (sem ae, duas vezes), espaço antes de `;`
`?` `!` `:`, travessão sem espaços (`prouidere—sed`; só em 43 há um travessão espaçado, `mei — scit`). Os colchetes de `sepe [me]` (§ 35)
são de White (emenda dele sobre Denis); ficam. Os parágrafos tipográficos dentro de um número foram juntos num só bloco.

**Testemunhos:** (1) o exemplar de Toronto da ed. 1918 (`librisanctipatr00patr`, PDF baixado: 44 páginas; a Confessio
está nas p. 11–32 do PDF = p. 5–26 do livro; tem uma anotação manuscrita na margem da p. 5, ignorada); (2) o outro exemplar
(`librisanctipatri0000patr`, OCR pior, só serviu de conferência); (3) a ed. de 1905 (PRIA), que é diplomática (grafia dos
manuscritos, `dilicta`, `missertus`) e só serviu para ler o OCR; (4) o Wikisource latino (Duffy 2000 sobre Bieler), só para
achar erros de leitura: nenhuma leitura dele foi adotada.

**Método:** o OCR de 1918 é bom até a p. 14 e ruim da p. 15 em diante (as p. 19, 21 e 25 têm itálicos borrados). Por
isso o texto foi **lido página por página na imagem** (as 22 páginas, a 150 dpi; as p. 17, 19, 21, 23 e 25 também a 260 dpi), e
depois conferido por script (difflib por palavra) contra os dois OCRs, o de 1905 e o Wikisource. Toda divergência foi
reexaminada; os pontos decididos em recortes de 400–450 dpi (16, ver `patricio-pontos.tsv` no diretório de trabalho do
agente, `~/.cache/claude-pedidos-0511/patricio-cipriano/rascunho/`) são:
`reppuli` (§ 18; as duas OCRs têm dois p, e minha 1ª leitura tinha um só), `inpulsus` (§ 26, em itálico; 1ª leitura: impulsus),
`omne nomen` (§ 4; mancha de tinta sobre o `n`, lido `omne`), `coheredes` (§ 4), `domini cati` (duas palavras, § 13),
`dedi` (§ 1: no exemplar de Toronto o `i` saiu com pingo borrado, parecendo `dedj`; o outro exemplar lê `dedi`),
`sepe [me]` (§ 35), `sepe indulsit` (§ 46), `ipsa Deo proximaret` (§ 42; OCR: ipse), `siue detractare` (§ 49; OCR: sine),
`caream sepulturam` (§ 59; OCR: carearn), `irasceretúr` (§ 46, com o acento agudo impresso) e `obseruare` (§ 40).

**Leituras duvidosas que ficaram:**
- § 40, p. 19: `obseruare` em itálico borrado. A imagem (450 dpi) deixa u/v indecidível; ficou `obseruare` (como todo o resto de White e
  como a variante `seruare` do aparato; o Wikisource tem `observare`).
- § 4, p. 6: `omne` com mancha de tinta (lido `omne`; o Wikisource também).
- § 46, p. 21: `irasceretúr` com acento: mantido como impresso (provável erro do tipógrafo; o sentido é `irasceretur`).
- § 1, p. 5: `dedi` (ver acima).
- Alguns itálicos das p. 19 e 25 são só legíveis a 260 dpi; os que o OCR e o Wikisource confirmam foram dados por certos.

## Diferenças de sentido entre White (1918) e o Wikisource/Duffy (que segue Bieler)

Só diferenças de palavra ou de construção (não de grafia). W = White, D = Duffy.
- § 1: W «filium quendam **Potiti** presbyteri» × D «filium quendam **cum** presbyteri» (sem *Potiti*); W «**Deum enim** uerum ignorabam» × D sem *enim*; W «Et **Dominus** induxit» × D «Et **Deus** induxit»; W «uidetur esse» × D «esse videtur».
- § 2: W «delicta mea **et** ut conuerterem» × D sem *et*; W «adulescentiae ignorantiae meae» × D «adoliscentiae **et** ignorantiae meae»; W «consolatus est **me**» × D «**mei**».
- § 4: W «nec umquam fuit **nec** ante nec erit» × D sem o 1º *nec* do trecho; W «ut **dicimus**» × D «ut **didicimus**»; W «et **eius** Filium» × D «et **huius** Filium»; W «**qui** cum Patre» × D «**quem** cum Patre»; W «fuisse **semper** testamur» × D «testamur **semper**»; W «hominem factum, deuicta **morte**» × D «hominem factum, **morte** devicta» (ordem); W «filii Dei **Patris**» × D «filii Dei» (W cita a variante «om. Patris A»).
- § 6: W «opto fratribus **et** cognatis» × D sem *et* (W cita a variante «fratres et cognatos meos CFR»).
- § 7: W «reddent rationem **de eo**» × D «**pro eo** rationem».
- § 8: W «**se** subtrahere» × D «subtrahere se» (ordem).
- § 9: W «ne inciderem in linguam hominum **et** quia non didici» × D «et» antes e outra ordem; W «didici» × D «dedici».
- § 11: W «Quanto magis… epistola Christi… etsi non diserta, sed **ministrata** fortissime, scripta in cordibus» × D «…**rata et fortissima**…»; W «Et iterum Spiritus testatur, Et **rusticatio** ab Altissimo **creata est**» × D «…**rusticationem**… **creatam**».
- § 12: W «prouidere—sed scio **illud** certissime» × D «providere, sed illud scio…» (ordem); «sursum adleuauit» igual.
- § 14: W «donum Dei et consolationem aeternam» × D «**domum** Dei»; W «quos **ego** in Domino baptizaui» × D «quos in Domino ego babtizavi» (ordem).
- § 16: W «ut in die una… **in** siluis» × D sem o *in* do trecho.
- § 17: W «annis **sex**» × D «sex annis» (ordem).
- § 18: W «ut haberem **inde** nauigare» × D «**unde** nauigarem»; W «**gubernatori** displicuit illi» × D «gubernator»; W «et in itinere coepi orare ; **et** antequam» × D sem *et*.
- § 19: W «quare ergo **non potes** pro nobis orare ?» × D «quare ergo (…) non potes?» (pontuação diferente); W «Deus tuus magnus et omnipotens **est**» × D sem *est* no mesmo lugar; W «cui nihil est inpossibile» × D «**quia** nihil est inpossibile»; W «quia ubique abundat illi» × D «**abundabat**»; W «**haec** summas gratias… ex hac die abundanter **cibum** habuerunt» × D «hoc… cibum» (ordem); W «**Hoc** immolaticum est» × D «Immolaticium est».
- § 20: W «nihil membrorum meorum **praualui**» × D «**praevalens**»; W «Sed unde **mihi** uenit **ignarum in spiritum**» × D «me… ignaro in spiritu»; W «**Et in hoc** uidi in caelum solem» × D «**Inter haec**…»; W «dum clamarem **Heliam**» × D «Helia, Helia».
- § 21: W «Duobus **autem** mensibus» × D sem *autem*.
- § 22: W «quarto decimo die» × D «quartodecimo»; W «peruenimus homines» × D «ad homines» (W cita a variante «ad homines C»).
- § 23: W «uidi in **uisu** noctis» × D «in **sinu** noctis» (W cita «in sinu A»); W «et **dum** recitabam» × D «cum»; W «ut uenias et adhuc **ambulas**» × D «**ambules**»; W «**post annos plurimos** praestitit illis Dominus» × D «ualde… plurimos» (ordem).
- § 24: W «Qui dedit pro te **animam suam** ipse est» × D «Qui pro te animam suam dedit…» (ordem); W «sic **expertus** sum» × D «**expergefactus** sum».
- § 25: W «Spiritus adiuuat **infirmitates** orationis» × D «**infirmitatis**».
- § 26: W «et peccata mea contra laboriosum episcopatum meum—utique in illo die» × D «…episcopatum meum **obiecerunt**, utique…».
- § 27: W «**antequod** essem diaconus» × D «**antequam**».
- § 28: W «**haec** potius bene mihi fuit» × D «**hoc**»; W «ut ego **curas** haberem» × D «**curam**».
- § 29: W «quasi ibi se iunxisset» × D «quasi **quod** sibi iunxisset».
- § 31: W «**Testem Deum** habeo» × D «**teste Deo**».
- § 32: W «ante **dissensionem** illam» × D «**defensionem**» (W cita «defensionem Boll. CF»).
- § 34: W «qui mihi **tanta diuinitate cooperasti**» × D «**tantam divinitatem comparuisti**»; W «**ut** quicquid mihi euenerit» × D sem *ut* e outra ordem; W «nec non» × D «necnon».
- § 35: W «de seruitute **sepe [me]** liberauit» × D «saepe»; W «responsum diuinum **creberrime admonuit**» × D «crebre admonere».
- § 39: W «et ab austro et ab aquilone, et recumbent» × D omite todo este trecho; W «Isaac» × D «Issac».
- § 40: W «Eunte… saluus erit… in **uniuerso mundo**» × D «mundi»; W «Praedicabitur… **et tunc ueniet** finis» × D «venit»; W «Dominus per prophetam **praenuntians inquit**» × D «praenunciat»; W «in **nouissimis** diebus» × D «novissimus».
- § 41: W «quomodo nuper **perfecta** est plebs Domini» × D «**facta**» (W cita «facta A; effecta B; fecta CP»).
- § 42: W «multis ex ancillis **suis**» × D «**meis**».
- § 43: W «et **ita** pergens» × D «et **ut** pergens»; W «uenirem **essemque** cum illis» × D «esse me cum illis»; W «timeo **perdere** laborem» × D «**pedere**»; W «qui **me** imperauit» × D «qui **mihi** imperauit».
- § 46: W «insipientiae meae et neglegentiae meae—et de loco non in unoquoque» × D «…et neglegentiae meae» posto depois; W «mihi **per his** nesciebam» × D «mihi **pro** his»; W «mittit in **periculum**» × D «**periculo**»; W «Iste quare se mittit».
- § 47: W «roborandam et confirmandam fidem uestram» × D «roborandum…».
- § 49: W «**ut me in aliquo titulo infideles** caperent» × D «ut non me in aliquo titulo infideli caperet» (diferente).
- § 50: W «ab aliquo illorum **uel** dimidio scriptulae» × D sem *uel*.
- § 54: W «Sufficit enim **mihi** honor» × D sem *mihi*.
- § 55: W «melius conuenit paupertas et calamitas quam **deliciae et diuitiae**» × D «divitiae et diliciae» (ordem invertida); W «et **si** opes uoluero iam non habeo» × D «etsi».
- § 58: W «**Quapropter** non contingat mihi» × D «Qua propter»; W «plebem suam **quam** adquisiuit» × D «**quamquam**»; W «ut reddam illi **testimonium fidele**» × D «**testem fidelem**» (W: «So White; MSS. have testem fidelem»).
- § 59: W «illis proselitis et captiuis… **aut** uolucres caeli comederent» × D «**ut**»; W «conformes **futurae** imaginis» × D «**futuri**».
- § 60: W «Nam sol iste quem uidemus, **Deo** iubente» × D «**ipso** iubente»; W «sed numquam regnabit neque permanebit splendor eius» × D «sed numquam **manet**…» ; W «Christus **manebit** in aeternum» (igual em D).

Diferenças só de forma, não listadas acima (W / D): quatinus/quatenus, pene/paene, adpeterem/adpetere, sermonem/sermone, animas/animus,
gubernatori/gubernator, susceperunt/susciperunt, efficiatus/effitiatus, aliquantis/aliquantos, persecutiones/persecutionis, infideles/infideli,
Domine/Domino (§ 34), orietur/oriebatur, Conuertimini/Convertemini, Uictoricus/Victoricius, genetiua/genitiva, et grafias (inpendi/impendi, cotidie/quotidie,
caeteri/ceteri, Britanniis/Brittaniis, Hiberione/Hiberionem § 28 etc.).
Atenção: as variantes que White dá no aparato (que não entram aqui) mostram onde ele escolheu entre manuscritos; Duffy/Bieler escolhem outras.
