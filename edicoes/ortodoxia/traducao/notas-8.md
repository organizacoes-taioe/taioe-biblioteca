# Ortodoxia — notas do tradutor, capítulo VIII (O romance da ortodoxia)

Parágrafos: 27/27. Grep de mesóclise sem resultado.

## Variantes do texto-fonte (LEIAME)

- § 5: `the discovery of one of them` (Gutenberg) / `the doctrine of one of them` (scan). O LEIAME não marca o
  Gutenberg como errado e a leitura faz sentido («Concluímos o último capítulo com a descoberta de uma delas»,
  isto é, a do pecado original como salvaguarda da democracia). Segui o Gutenberg.
- § 15: `as a divine love` (Gutenberg, marcado como erro) → segui o scan, `as of divine love`: «É tão verdade da
  fraternidade democrática quanto do amor divino».
- § 27: o Gutenberg traz `they only destroy political and common courage sense`, frase truncada (não listada no
  LEIAME; o cache do scan não estava disponível para conferir). Adotei a leitura das edições impressas correntes,
  `political courage and common sense`: «destroem apenas a coragem política e o bom senso» (*common sense* → «bom senso», como nos caps. IV, VI e IX;
  antes «senso comum»).
- § 10: `hectagonal` (Gutenberg) → «hexagonal». A palavra inglesa não existe; o par triangular/hexagonal é o
  sentido evidente. Proposta: acrescentar ao LEIAME.

## A citação de Swinburne (§ 17, parágrafo próprio no original)

*Hertha*, de *Songs before Sunrise*, na versão que Chesterton cita de memória (sem o «But» do primeiro verso e com
«that thou seekest» em vez de «whom thou seekest»). Traduzi o que ele escreveu. Fica num parágrafo só, como no
original, entre aspas, com « / » entre os versos; acrescentei as aspas simples da fala interna (‘...’), que o
Gutenberg perdeu e o poema tem.

Metro do original (estrofe de *Hertha*): quatro versos anapésticos curtos e um longo, rimas ABABB, todas agudas
(*now/thou*, *cry/high/I*). Molde do original: `5: 2-5`, `6: 1-3-6`, `6: 3-6`, `6: 3-6`, `18: 3-6-9-12-15-18`
(o último são seis anapestos, sem pausa que quebre a conta).

Tradução, conferida com o `molde.mjs` (5 exatos, nenhum ✗, nenhum ≠, nenhuma leitura forçada):

| verso | molde | obtido |
|---|---|---|
| Pois, que fazes tu, | `5: (1)-(2)-3-5` | 3-5 |
| a clamar, como um réu, | `6: 3-6 (1)` | 3-6 |
| ‘Eu sou eu, tu és tu, | `6: (1)-(2)-3-(4)-(5)-6` | 1-2-3-4-5-6 |
| eu no pó, tu no céu’? | `6: (1)-3-(4)-6` | 1-3-4-6 |
| Eu sou tu, que procuras a Deus; mas encontra-te só: tu és eu. | `18: (1)-(2)-3-6-9-12-15-(16)-(17)-18` | 1-2-3-6-9-12-15-16-17-18 |

- Rimas ABABB agudas mantidas: *tu/tu* (A) — inevitável, porque o verso 3 tem de ser a fórmula «Eu sou eu, tu és
  tu», que Chesterton retoma na prosa (§ 18) como lema da teologia ocidental; *réu/céu/eu* (B).
- O verso longo é um eneassílabo duplo (3-6-9 + 3-6-9), ternário como o original; o meio cai em palavra aguda
  (*Deus*) e a segunda metade começa por consoante, para não haver fusão na cesura.
- Os monossílabos tônicos em fila («Eu sou eu, tu és tu»; «tu és eu») ficam como tempos facultativos no molde,
  como o manual prevê para monossílabos. O quiasmo do original («I am thou... thou art I») ficou: «Eu sou tu...
  tu és eu».
- O 1.º verso fica 3-5 e não 2-5 como o inglês; o desenho existe no corpus (3,1%).
- **Perdas e cessões:** *now* virou «Pois» (o «e agora?» de quem interpela); *Looking Godward* se perdeu como
  imagem própria, e o «para Deus» passou ao verso 4 («tu no céu») e ao verso 5 («a Deus»); «como um réu» é
  acréscimo de ornamento, para a rima, mas diz a mesma prostração do «I am low»; *I am low, thou art high* →
  «eu no pó, tu no céu»; *to find him* → «a Deus» (o *him* é o deus que o homem procura no alto); *find thou but
  thyself* → «encontra-te só».
- Na prosa seguinte: *"I am I, thou art thou"* → «Eu sou eu, tu és tu» (igual ao verso); *"found himself"* →
  «“encontrado a si mesmo”» (eco do «encontra-te»).

## Trocadilhos, paradoxos e soluções

- **words of one syllable** (§ 1): «palavras de uma sílaba». As frases de Jones e Brown não ficam monossilábicas em
  português; ficou a oposição entre a frase comprida e oca e a frase curta que obriga a pensar. *Gaol* → «cadeia».
- **damn / degeneration** (§ 1): «“danado”» / «“degeneração”»: *danado* guarda a danação (a sutileza metafísica) e
  o uso de praguejar, e a aliteração em *d*.
- **High / Low / Broad Church** (§ 3): «da Alta Igreja... tudo o que é alto»; «os da Baixa Igreja deveriam gostar da
  missa baixa» (o termo litúrgico existe em português); «os da Igreja Larga deveriam gostar de piadas largas».
  *Broad jokes* são piadas indecentes; *largo* em português também quer dizer «pouco escrupuloso» (consciência
  larga), o que salva a piada, ainda que «piadas largas» não seja expressão feita. **Perda parcial.** No § 6, por
  coerência, *a "broad" or "liberal" clergyman* → «um clérigo “largo” ou “liberal”».
- **liberal / free** (§ 3): «todos os liberais deveriam ser livres-pensadores, porque deveriam amar tudo o que é
  livre»; passa inteiro.
- **notes of the new theology** (§ 5): «as notas da nova teologia», no sentido das *notas da Igreja*.
- **A holiday, like Liberalism... A miracle** (§ 7): «As férias, como o liberalismo, significam apenas a liberdade do
  homem. Um milagre significa apenas a liberdade de Deus.» (*holiday* aqui é a ida das crianças à praia.)
- **love our neighbours / be our neighbours** (§ 14): «ela não nos manda amar o próximo; manda-nos ser o próximo».
- **real selves / unselfish selves / selfish person** (§ 14): «eus reais... eus realmente desprendidos de si... uma
  pessoa enormemente egoísta». O jogo *self/unselfish* não tem par exato; ficou a ideia do eu que sai de si.
- **shut his eyes / keep an eye on Lord Curzon** (§ 18): «fechar os olhos... ficar de olho em lorde Curzon»; passa.
- **Insisting that God is inside man...** (§ 19): mantive o gerúndio solto do original, que faz a simetria: «Insistindo
  em que Deus está dentro do homem, o homem está sempre dentro de si mesmo. Insistindo em que Deus transcende o
  homem, o homem transcendeu a si mesmo.»
- **it is not well for man / for God to be alone** (§ 20): «não é bom que o homem esteja só» / «não é bom que Deus
  esteja só» (Gn 2,18, como Chesterton cita).
- **damned / damnable** (§ 21): «chamar um homem de “condenado”... chamá-lo de condenável»; passa inteiro.
- **an eatable hero** (§ 21): «um herói comestível».
- **patient / IMPATIENT** (§ 23): «“paciente” está na voz passiva; “pecador”, na ativa... não um paciente, mas um
  _impaciente_. Tem de estar pessoalmente impaciente com a falsificação.» Passa inteiro.
- **to be continued in our next** (§ 22): «“continua no próximo número”»; *serial story* → «folhetim».
- **have his back to the wall** (§ 25): «ver-se contra a parede».
- **heaven / Hartlepool** (§ 26): «não pode ir para o céu... não pode ir para Hartlepool»; perdeu-se a aliteração.
- **the book of the Recording Angel / the books of Marshall & Snelgrove** (§ 27): «o livro do Anjo Registrador...
  manter em ordem os livros da Marshall & Snelgrove»; *livros* também é a escrituração comercial, e o jogo passa.
- **secularists... secular things** (§ 27): «Os secularistas... destruíram as coisas seculares».
- **These scraps of puerile pedantry** (§ 12): «Esses retalhos de pedantismo pueril», eco dos «retalhos» do manto
  do lama, frase antes; o eco é do português, não do inglês (*remnants/scraps*).

## Termos e nomes

| inglês | tradução |
|---|---|
| liberal, liberality, illiberal | liberal, liberalidade, iliberal |
| liberalisers of theology; "liberalising" | liberalizadores da teologia; “liberalização” |
| Liberals and Tories | liberais e tories |
| the New Theology; the modernist church | a Nova Teologia; a igreja modernista |
| immanence, immanentism, immanent | imanência, imanentismo, imanente |
| transcendence, transcendent | transcendência, transcendente |
| High Church, Low Church, Broad Church; Low Mass | Alta Igreja, Baixa Igreja, Igreja Larga; missa baixa |
| Unitarians, Trinitarians | unitaristas, trinitários |
| the Athanasian Creed | o Credo Atanasiano |
| Mahommedanism, Mahommedan; Mahomet | maometismo, maometano; Maomé |
| Thugs | tugues |
| Swedenborgian | swedenborguiano |
| Theosophist, theosophical | teósofo, teosófico |
| world-soul | alma do mundo |
| aeon(s) | éon, éons |
| melting-pot | cadinho |
| serial story | folhetim |
| profligate | devasso |
| sweater (o patrão de oficina de suor) | explorador de operários (harmonizado com o cap. VII; antes «patrão explorador») |
| the Recording Angel | o Anjo Registrador |
| Bible-smasher | demolidor de Bíblias |
| indeterminate sentence | pena indeterminada |
| parish priest / clergyman (anglicanos, § 6) | vigário / clérigo |
| Mrs. Besant; Lord Curzon; King Bomba; King Leopold | a sra. Besant; lorde Curzon (minúscula, como «lorde Hugh Cecil» no cap. VII); o rei Bomba; o rei Leopoldo |
| the CHURCH TIMES, the FREETHINKER | o _Church Times_, o _Freethinker_ (títulos, não ênfase) |
| "Songs before Sunrise" | “_Songs before Sunrise_” (título sem traduzir: aspas do original e itálico de língua estrangeira, como “_Vie de Jésus_” no cap. III) |
| the Serpentine; Surbiton, Wimbledon, Hartlepool; Marshall & Snelgrove | ficam como estão, sem explicar |

## Outras decisões

- Ênfases em maiúsculas → itálico: _Alega-se_ (ALLEGED), _vigiar_ (WATCH), _coração_ (HEART), _história_ (STORY),
  _possa_ (MIGHT), _perigo_ (DANGER), _impaciente_ (IMPATIENT), _fazê-las_ (MAKE). CHURCH TIMES e FREETHINKER são
  títulos de jornal e ficam em itálico de título.
- *the church* em minúscula no Gutenberg: na harmonização, quando é a instituição, ficou «a Igreja», como manda o
  glossário e como o cap. IX já fazia («trazer a liberdade para a Igreja», «libertar a Igreja», «atear fogo à
  Igreja»); fica minúscula só «a igreja modernista» (o movimento) e «as igrejas católicas» (os edifícios).
  *The Church* maiúscula fica «a Igreja».
- § 14: *as one likes a looking-glass, because it is one's self* → «como se gosta de um espelho, porque é a própria
  pessoa» (na harmonização, o impessoal no lugar de «a gente mesma»).
- § 15: *sham love ends in compromise* → «o amor fingido acaba em meio-termo» (*compromise* → «meio-termo», como nos
  caps. V e VI; antes «acomodação»).
- § 6: «"miracles do not happen," as in the dogma which Matthew Arnold recited» → «“os milagres não acontecem”» (é a
  frase de *Literature and Dogma*, citada em prosa).
- § 6: Tennyson («there lives more faith in honest doubt», *In Memoriam*) vem parafraseado em prosa; traduzi como
  prosa: «havia fé na dúvida honesta deles».
- § 11: *imposing its morality only upon the refreshment of the lower classes* (a abstinência de álcool) → «impor a
  sua moral apenas às bebidas das classes baixas».
- § 15: *It is her instinct* (o cristianismo no feminino, em inglês) → «É instinto seu», sem marcar gênero.
- § 16: *cut off from the world* → «cortado do mundo», para guardar o eco da espada do parágrafo anterior.
- § 25: «Thou shalt not tempt the Lord thy God» → «Não tentarás o Senhor teu Deus», com *Si mesmo* em maiúscula
  como o *Himself* do original.


## Conferência com o scan de 1908 (acrescentada depois)

- § 5: o scan traz «with the doctrine of one of them»; a tradução passou a «com a doutrina de uma delas».
- § 27: o scan confirma «political courage and common sense».
- § 10: o scan também traz «hectagonal»; ficou «hexagonal».
