# Introdução à vida devota (Filoteia), de São Francisco de Sales: texto francês de trabalho

Arquivos: `00-oracao-e-prefacio.txt` a `05-quinta-parte.txt`. São 8 arquivos em UTF-8, com cabeçalho `# chave: valor` e parágrafos separados por uma linha em branco. Nada foi traduzido.

## Fonte e edição

- **Texto pedido: o de 1619.** É a «dernière édition, revue, corrigée et augmentée par l'Autheur» (Paris, Joseph Gottereau, 1619), a última revista pelo santo. A primeira edição saiu em Lyon no fim de 1608, com data de 1609. O texto foi muito ampliado em 1609–1610 e retocado até 1619.
- **Edição de base:** *Introduction à la vie dévote*, texte intégral publié d'après l'édition de 1619, par l'abbé Fernand Boulenger (Paris, Vve Ch. Poussielgue, 1909).
  - Boulenger reproduz o texto de 1619 com a **ortografia modernizada**. Mantém o vocabulário e a sintaxe do século XVII: *ès*, *icelui*, *meshui*, *ains*, *voirement*.
- **Fonte digital:** Wikisource em francês, «Introduction à la vie dévote (Boulenger)», página «Texte entier», https://fr.wikisource.org/wiki/Introduction_%C3%A0_la_vie_d%C3%A9vote_(Boulenger)/Texte_entier.
  - É uma transcrição feita sobre o fac-símile da edição de 1909, o arquivo «De Sales - Introduction à la vie dévote, 1619, édition Boulenger, 1909.pdf».
  - A página bruta está em `ferramentas/cache/filoteia/entier.html`.
- **Conferência:** *Œuvres de saint François de Sales*, Édition complète (dita «d'Annecy»), t. III, *Introduction à la vie dévote* (Annecy, 1893), no Internet Archive: https://archive.org/details/oeuvresdesaintfr03fran.
  - Usamos o OCR (`annecy3.txt`) só para conferir. O aparato crítico de Annecy não foi usado nem copiado.
  - Annecy dá o texto de 1619 com a grafia original.

### Conferência com Annecy (1893)

**A primeira conferência estava errada.** Ela dizia que não havia omissões. Os tradutores acharam frases inteiras faltando, e uma segunda colação, palavra a palavra e da obra inteira, confirmou: a transcrição do Wikisource **pulava linhas**. Quase sempre é salto do mesmo ao mesmo: o olho passa de uma palavra para a mesma palavra uma linha abaixo («l'Église... l'Église», «entièrement... entièrement»).

A primeira conferência falhou por dois motivos:

- só procurava trechos de 8 palavras ou mais, e a maior parte das lacunas tem de 4 a 9 palavras;
- tirava o aparato de Annecy por blocos, e a maior lacuna (II.4, 49 palavras) foi tomada por aparato.

#### Método da segunda colação

Os scripts estão em `ferramentas/cache/filoteia/`.

1. **`colacao2.py`: trechos de 3 palavras ou mais.**
   - Os dois lados são normalizados do mesmo jeito: sem acentos nem consoantes dobradas, *oi*/*ai*, *y*/*i*, *u*/*v* reduzidos, terminações cortadas.
   - Annecy entra inteiro, sem filtro que possa engolir texto. Cada palavra leva uma classe: texto corrido, aparato ou título.
     - Aparato é tudo o que vai do primeiro bloco aberto por «(a)», «(1)»... até o cabeçalho da página seguinte.
     - Títulos são os blocos logo depois de «CHAPITRE N».
   - A comparação lista toda diferença em que Boulenger tem 3 palavras ou mais sem par, ou Annecy tem 3 palavras seguidas de texto corrido sem par.
   - Ficam de fora só as trocas em que os dois lados se parecem letra a letra, que são grafia e OCR. As referências da margem («Ps. xv», «Matt. xi») vão para uma lista à parte.
   - O resultado é `colacao2-antes.out`: 212 candidatos e 150 referências de margem.
2. **`colacao3.py`: palavra isolada.**
   - Lista as trocas de uma palavra por outra e as palavras a mais ou a menos.
   - Só entram as diferenças em que a palavra de Annecy é palavra de verdade, isto é, aparece em algum lugar de Boulenger.
   - Saem os pares que se repetem 3 vezes ou mais, porque são modernização sistemática ou vício do OCR.
   - O resultado é `colacao3-antes.out`: 219 candidatos.
3. **Números de ponto.** A sequência «1.», «2.»... foi comparada capítulo por capítulo.
4. **Artefatos do Wikisource.** Varredura de não-palavras, letras soltas, maiúsculas no meio da palavra, apóstrofos perdidos e hífens de quebra de página.

Cada candidato foi lido no contexto, no OCR de Annecy (`annecy3n.txt`, número da linha na saída) e no aparato da página. Nada foi aplicado às cegas. Depois das emendas, as duas colações foram rodadas de novo: `colacao2.out` e `colacao3.out`.

#### O que se achou

- **Do lado de Boulenger, não há texto a mais.** Os trechos sem par em Annecy são falhas do OCR de Annecy: linha perdida na virada de página, palavras embaralhadas pelas referências da margem.
- **Do lado de Annecy, quase tudo o que sobra é aparato:**
  - variantes dos manuscritos e das edições de 1609, 1610 e 1616;
  - os rascunhos longos do manuscrito, como os de III.4, III.7, III.12, III.18, III.38, III.40 e IV.13, que não levam «(a)» no começo de cada página;
  - notas, referências e títulos.
- **O resto é lacuna ou erro de Boulenger/Wikisource.** Está listado abaixo.

#### Critério das emendas

- **Annecy dá o texto de 1619**, e Boulenger diz reproduzir o mesmo texto mudando só a grafia. Onde as palavras diferem, vale a lição de Annecy, posta na ortografia modernizada de Boulenger.
- **Fica Boulenger nestes casos:**
  - diferença de grafia, ou modernização que ele faz sempre:
    - gênero das palavras: «mon guide», «toutes les affaires», «sainte aise», «simple et naïve» dito de Philothée;
    - concordância: «Restent les conversations»;
    - formas verbais: «manges-en», «vous pourrez» por «vous pourras»;
  - a lição de Boulenger é variante das edições anteriores, registrada no aparato de Annecy. Boulenger a preferiu:
    - I.4: «la confiance d'un fils *envers* sa mère», onde Annecy tem «avec» e o aparato dá «envers (Ms.-A-B-C)»;
    - I.4: «ne *le* considérez pas» (Ms.-A);
    - III.3: «comme je *désirais*» (Ms.-A-B-C; 1619: «desirerois»);
  - é Annecy quem emenda 1619. Em III.3, «mes travaux sont des consolations et mes *peines* des roses»: Annecy imprime «espines», do manuscrito e de 1609–1610, e diz em nota que «peines» é a lição das edições seguintes, a de 1619 inclusive.
- Emendas ficam dentro dos parágrafos. Nenhuma muda as marcas `[P.C]`, os títulos `##` ou o número de parágrafos de qualquer arquivo; isso foi conferido arquivo por arquivo contra a versão anterior.

#### Emendas aplicadas

São 233 pontos alterados nos 8 arquivos (00: 3; 01: 34; 02: 50; 03-a: 33; 03-b: 45; 03-c: 26; 04: 23; 05: 19). Ficam na lista `CORRECOES` de `preparar.py`, com o local de cada uma, e em duas regras gerais de `limpa()`. Em cada item vem primeiro o texto de Boulenger/Wikisource, depois o texto emendado.

Vêm de duas fontes:

- **Primeiro lote:** a colação descrita acima.
- **Segundo lote:** erros que os tradutores anotaram em `traducao/notas-*.md`. Cada um foi conferido no OCR de Annecy antes de entrar.
  - A colação não os pegava: são pontuação, letras trocadas dentro da palavra e sobras de OCR do próprio Wikisource («]’ai», «la| sainte», «l(ordinaire»).

**Lacunas de linha inteira:**

| local | Boulenger/Wikisource | emendado (Annecy) |
|---|---|---|
| I.20 | à la vue de l'Église militante ma Mère | à la vue de l'Église **triomphante, et en la face de l'Église** militante ma Mère |
| II.4 | si vous voulez méditer Notre Seigneur, en la façon que les Évangélistes le décrivent | ... méditer Notre Seigneur **en croix, vous vous imaginerez d'être au mont de Calvaire, et que vous voyez tout ce qui se fit et se dit au jour de la Passion ; ou, si vous voulez, car c'est tout un, vous vous imaginerez qu'au lieu même où vous êtes se fait le crucifiement de Notre Seigneur,** en la façon que... |
| II.19 | expliquez si ç'a été pour le plaisir de la conversation | ... ç'a été pour **le désir du gain, ou pour** le plaisir... |
| II.20 | non seulement vous n'avez pas même l'affection du péché | non seulement vous n'avez pas **l'affection de pécher, mais vous n'avez pas** même l'affection du péché |
| II.21 | pour vous purifier de vos imperfections, pour vous consoler | ... imperfections, **pour vous délivrer de vos misères,** pour vous consoler |
| III.3 | Or il sera entièrement formé en votre cœur | Or il sera entièrement **enfanté pour vous lorsque vous l'aurez entièrement** formé en votre cœur |
| III.38 | plusieurs ont cette véritable famille que celle des maris | plusieurs ont cette véritable **opinion, que leur dévotion est plus fructueuse à la** famille que celle des maris |

**Palavras que mudam o sentido:**

| local | Boulenger/Wikisource | emendado (Annecy) |
|---|---|---|
| I.14 | ains qu'aucune des choses | sans qu'aucune des choses |
| I.22 | ces lares et déchets | ces tares et déchets |
| II.19 | lisez attentivement les chapitres XXVII... | lisez diligemment les chapitres VI, XXVII... |
| III.7 | leur réputation, la gâtent entièrement | ... la perdent entièrement |
| III.7 | où la venu loge | où la vertu loge |
| III.12 | l'infirmité de ceux qui en jouissent passent aisément | ... passe aisément (o sujeito é «l'infirmité») |
| III.17 | La communion des voluptés charnelles | La communication des voluptés charnelles |
| III.28 | ne pouvant excuser du moins tout le péché | ne pouvant excuser du tout le péché |
| III.39 | n'en ayant point qui rend tellement les consolations | ... qui prend tellement les consolations |
| IV.1 | un peu plus malin qu'à l'ordinaire | un peu plus matin qu'à l'ordinaire |
| IV.6 | de longue et de petite durée | de longue ou de petite durée |
| IV.8 | il nous faut bien et dignement défendre | ... bien et diligemment défendre |
| IV.11 | elle s'échauffera à la quête des moyens, comme si ce bien s'empressera et dépendait | elle s'empressera et s'échauffera à la quête des moyens, comme si ce bien dépendait |
| IV.13 | Quand nous aurons de ces douleurs et consolations | ... de ces douceurs et consolations |

**Números de ponto:**

- V.2: falta «6.» antes de «Considérez les effets de cette vocation».
- V.4: «4,» passa a «4.», e falta «10.» antes de «Sauriez-vous remarquer».
- V.5: falta «6.» antes de «Quant aux œuvres».

**Palavras omitidas, com sentido igual ou quase:**

- I.14: Pesez ces paroles **si** pesantes
- II.9: un plaisir **très** délicieux
- II.13: ce qui se présente en **la** variété
- II.19: lequel vous pouviez **aisément** secourir
- III.3: c'est là où il y **va** du bon
- III.5: rien ne **nous** peut tant humilier
- III.9: d'une grosse faute **commise** contre la chasteté
- III.16: c'est une **trop** grande ambition
- III.18: Vous **vous** voulez jouer avec lui
- III.34: tels jeux sont **beaucoup** plus blâmables

**Palavra a mais:**

- III.34: «étant battus ~~par~~ des vagues»

**Trocas sem mudança de sentido:**

| local | Boulenger/Wikisource | emendado (Annecy) |
|---|---|---|
| I.5 | ce n'est point leur consentir | ce n'est pas leur consentir |
| I.5 | humilité, quelquefois nous soyons blessés | humilité, nous soyons quelquefois blessés |
| I.10 | à cette fin qu'elle | à celle fin qu'elle |
| I.14 | comparaîtront à la vallée | comparaîtront en la vallée |
| I.15 | o Dieu ! que regret | o Dieu ! quel regret |
| II.8 | la considération doive précéder | la considération doit précéder |
| II.13 | ne s'arrêtent que pour mieux aller | ne s'arrêtant que pour mieux aller |
| II.13 | et ne trouve point d'arbre | et ne trouvent point d'arbre |
| II.20 | confits au sucre et au miel | confits au sucre ou au miel |
| III.9 | que non par les colères | que non pas les colères |
| III.13 | je vous présente le mot | je vous représente le mot |
| III.20 | pour ne pas ouïr | pour ne point ouïr |
| III.21 | sous quelque prétexte que ce soit | sous quel prétexte que ce soit |
| III.23 | les jours auxquels | les jours esquels |
| III.28 | aussi les cogitations | ainsi les cogitations |
| III.35 | Or, en toutes les parties | Or, entre toutes les parties |

**Erros de digitação evidentes:**

| local | Boulenger/Wikisource | emendado |
|---|---|---|
| Préface | par a suavité | par la suavité |
| I.15 | O jmon âme | O mon âme |
| I.24 | couRut | courut |
| II.11 | l'Eglise | l'Église |
| II.13 | cesser dé penser | cesser de penser |
| II.14 | la vie de de Notre Seigneur | la vie de Notre Seigneur |
| II.21 | comiinuniez | communiez |
| III.1 | Gassien | Cassien |
| III.3 | que de possède son âme | que de posséder son âme |
| III.12 | quand à ceux | quant à ceux |
| III.12 | Ghrysostôme | Chrysostôme |
| III.14 | îcar | car |
| III.15 | omme dit | comme dit |
| III.21 | nulle sorte I de propositions | nulle sorte de propositions |
| III.21 | Philothëe | Philothée |
| III.29 | la I médisance | la médisance |
| III.37 | puisqu'on ce temps-là | puisqu'en ce temps-là |
| IV.11 | elle a I quelque mal | elle a quelque mal |
| IV.13 | pour mous rendre | pour nous rendre |
| V.7 | qu'on i fait | qu'on y fait |
| V.13 | 0 résolution (zero) | O résolution |

**Duas regras gerais em `limpa()`, para artefatos do Wikisource:**

- **Hífen de corte na virada de página** (11 casos): «Phi- lothée», «aisé- ment», «popu- laire», «cour- tois», «bien- séance», «con- solations», «de- vant», «rap- portons», «quoi- qu'il», «résolu- tions», «dé- lices».
- **Apóstrofo perdido** depois de *d*/*m* isolados (8 casos): «d user», «d abeilles», «d affection», «d autant», «m as», «d autrui», «d avoir», «d en».

**Segundo lote (notas dos tradutores, conferidas com Annecy):**

- **Mudam o sentido:**
  - I.14: «étant devant soi sa croix» → «ayant devant soi sa croix».
  - II.13: «car il vous en fournit» → «fournira».
  - III.19: «de peur que en particulier» → «de peur que **cherchant** en particulier».
  - III.28: «elle en détourne sa face elle dissimule» → «... sa face **et le** dissimule».
  - III.28: «où qu’il eût vu Rébecca» → «**ou** qu’il eût vu».
  - III.29: «je ne dirai rien de cela» → «je ne dirai rien **que** cela».
  - III.39: «capricieuses prétentions vertu» → «prétentions **de** vertu».
  - IV.3: «tentations que souffrit saint François» → «que **soutint**».
  - IV.11: «plus importants trouveront» → «trouveraient».
  - V.3: «qui demandant lumière» → «**lui** demandant lumière».
  - V.18: «La mère de Symphorien» → «La mère de **saint** Symphorien».
- **Palavras e formas, sem mudança de sentido:**
  - I.14: «les bons de mauvais» → «des mauvais».
  - I.17: «tes belles et sacrées, maisons, et en les saints» → «tes belles et sacrées maisons, et en tes saints».
  - I.18: «qui les console, y et que» → «qui les console, et que».
  - II.1: «conseille son saint Bonaventure» → «sont»; «Grenade Du Pont» → «Grenade, Du Pont».
  - II.13: «Or, cet exercice» → «Or, en cet exercice».
  - II.16: «aux anges et, font» → «aux anges, font».
  - III.1: «alléguant ahab» → «Rahab».
  - III.3: «blasphème» → «blasphémé».
  - III.5: «d’obéir de suivre» → «d’obéir et suivre»; «des motif» → «des motifs».
  - III.6: «plusieurs l’accommodent» → «s’accommodent»; «chacun rappellera» → «appellera».
  - III.14: «le royaume des deux» → «des cieux»; «Celui lest riche» → «Celui est riche».
  - III.15: «eut su faire» → «eût su faire»; «avec douceurs ces diminutlions» → «avec douceur ces diminutions»; «ne vous contentez-pas» → «ne vous contentez pas».
  - III.18: «Il se passera» → «Ils se passeront».
  - III.21: «ce serait donc sacrilège» → «un sacrilège».
  - III.22: «celui qui nait» → «qui n’ait».
  - III.23: «ès jeunes, disciplines» → «ès jeûnes»; «je n’aurais pas» → «je n’aurai pas».
  - III.24: «s’en faut détourner» → «il s’en faut détourner».
  - III.26: «les vraies indices» → «les vrais indices».
  - III.27: «qu’elle ne lésait fait mourir» → «ne les ait»; «si nous n’y pensons pas» → «pensions».
  - III.34: «auvent» → «au vent».
  - III.37: «quand elle arriveront» → «quand elles».
  - III.38: «lamitié», «parla bouche» → «l’amitié», «par la bouche».
  - III.39: «son emmiellées» → «sont».
  - IV.4: «Tamant» → «l’amant».
  - IV.11: «après es petits» → «les petits».
  - IV.12: «Dieu démon cœur», «le bien-aimé de ! mon âme» → «Dieu de mon cœur», «le bien-aimé de mon âme».
  - IV.14: «nous remettra» → «nous remettre».
  - V.2: «mon cœur Ta dit» → «l’a dit».
  - V.3: «que tout se fasse» → «que le tout se fasse».
  - V.7: «qu’on i fait» → «qu’on a fait».
  - V.7: «pour es confessions» → «pour les».
- **Letras e grafia:**
  - Prefácio: «pitiés» → «pitié»; «less cœurs» → «les cœurs».
  - I.1: «actions extérieure» → «extérieures»; «encore quelles» → «encore qu’elles».
  - I.5: «purge» → «purgé».
  - I.9: «teétais» → «tu étais».
  - I.12: «Je tels et de tels» → «de tels et de tels».
  - I.21: «affecions» → «affections».
  - I.22: «n’avoiraucune» → «n’avoir aucune».
  - I.24: «défauts Et» → «défauts et».
  - II.13: «repreliait» → «reprenait»; «nangé» → «mangé».
  - II.19: «les même choses» → «les mêmes»; «il veulent» → «ils veulent».
  - II.20: «tnithridat» → «mithridat»; «excercice» → «exercice».
  - II.21: «réellementà» → «réellement à».
  - III.2: «des. autres» → «des autres».
  - III.5: «Qu’gavons-nous» → «Qu’avons-nous».
  - III.9: «jet marris» → «et marris».
  - III.10: «pourvoir» → «pour voir».
  - III.11: «suivez il encore» → «suivez encore».
  - III.15: «fît» → «fit».
  - III.20: «feles femelles» → «les femelles».
  - III.29: «maindu» → «main du».
  - V.13: «occurences» → «occurrences».
- **Sobras de OCR do Wikisource:**
  - I.20: «]’ai» → «j’ai»; «[leurs», «|et», «[irrévocablement» → sem o sinal.
  - II.6: «Capilia, | et» → sem a barra.
  - II.12: «d*y» → «d’y».
  - II.13: «la (grève», «fort| étonnés» → sem o sinal.
  - II.14: «la| sainte messe» → sem a barra.
  - III.7: «; (car» → parêntese que nunca fecha, tirado.
  - III.9: «[que de passion» → sem o colchete.
  - III.12: «On [appelle» → sem o colchete.
  - III.24: «présomption.il faut pour l(ordinaire qu’une joie modérée ! prédomine» → «présomption. Il faut pour l’ordinaire qu’une joie modérée prédomine»; «modestie ! paraisse» → sem o «!»; «[l’exemple» → sem o colchete.
  - III.25: «extérieure | représente» → sem a barra.
  - I.12: «vous ! avez» → sem o «!».
- **Espaços e itálico:**
  - II.1: «_Ave Maria_et le_Credo_en latin», «un seul_Pater_» → espaços restituídos.
  - II.7: «_Pater noster_et_Ave Maria_» → espaços restituídos.
  - II.14: «_Credo_jusques au_Pater noster_» → espaços restituídos.
  - II.19: «deviez;», «devez;», «dites:ayant» → espaços restituídos.
  - II.21: «reçu,excitez» → espaço restituído.
- **Pontuação:**
  - **Ponto no lugar da vírgula, antes de maiúscula:**
    - I.4: «Dialogues. La dévote»;
    - I.16: «innumérable. Oh !»;
    - II.17: «vacation. Car»;
    - III.15: «blanchisseuse. O ma»;
    - III.16: «supporter. Si vous»;
    - III.19: «personnes. La perfection»;
    - III.28: «jugés ». Mais»;
    - III.30: «simplicité. Les»;
    - IV.3: «dessein. Premièrement»;
    - IV.12: «comme lui. La mauvaise»;
    - IV.13: «dévotion. Saül».
  - **Vírgula no lugar do ponto:** II.13 «l’une l’autre, et toutes»; III.1 «arrivé, comme dit»; III.3 «le mal, vous».
  - **Vírgula no lugar de «?»:** II.14 «piété, mystère»; II.16 «imiter, et en».
  - **Ponto no lugar de vírgula e aspa:** III.3 «par ma faute ». L’autre».
  - **Interrogação:** I.13 «père spirituel ?»; I.22 «lui être ennuyeux ?»; V.4 «péchés véniels ? On».
  - **Pontuação tirada ou trocada:**
    - II.7: «supplication » par» → «supplication, par»;
    - III.16: «extrêmement, pure» → sem vírgula;
    - III.18: «avons besoin ?» → «besoin ;»;
    - III.29: «au ; prochain» → sem o «;»;
    - III.31: «il passait ; le temps» → sem o «;»;
    - IV.1: «œil, Jamais» → «jamais»;
    - V.5: «en parlant ; de vous» → sem o «;»;
    - V.18: «regardez, le ciel» → sem vírgula; no dístico, «j’attends.» → «j’attends,».
  - **Aspas:**
    - III.39: «» C’est le grand mal» → «« C’est...», aspa de fechar no lugar da de abrir;
    - IV.13: «: ce Oh ! que je suis bon ! »» → «: « Oh !...», aspa de abrir mal lida como «ce».

**Não emendado, de propósito:**

- **Nomes que Annecy corrige contra todas as edições antigas.** Fica a lição de 1619:
  - Prefácio: «Compaspé»; Annecy põe «Campaspé».
  - I.4: «Catherine de Cordoue»; Annecy põe «Cardone».
  - I.15: «les paroles de Job». Annecy põe «d’Isaïe» e explica em nota: as edições anteriores à de 1652 atribuem a Jó essas palavras de Isaías, e os editores quiseram retificar o engano.
  - III.40: «Salvia», como em Annecy. A destinatária da carta 79 de são Jerônimo é Salvina.
  - A tradução segue a correção nesses quatro nomes (Campaspe, Catarina de Cardona, Isaías, Salvina), e a apresentação da edição o registra (ver `CONVENCOES.md`, § 7).
- **Aspas que abrem e não fecham**, ou o contrário. Ficam como em Boulenger, porque Annecy quase não usa aspas e não serve de modelo. Os casos estão em I.4, I.14, I.15, I.17, III.14, III.18, III.21, III.27, IV.1, IV.12, V.2 e V.4. Na tradução, as aspas se fecham onde a fala termina.
- **Divisão de parágrafos**, que em Annecy é às vezes outra: em II.20, V.1, V.3, V.7, V.15 e no texto corrido de V.3 e IV.15. Fica a de Boulenger.
- **Pontuação** não foi colada sistematicamente. Ficam também as diferenças miúdas que não são erro, como I.20 «Dieu de mon cœur. Dieu de mon âme», onde o OCR de Annecy também tem ponto.

**Pontuação:** duas lições de Boulenger encerravam com vírgula um parágrafo terminado em ponto. Foram corrigidas por Annecy (`CORRECOES_FIM`):

- «comme vaines et superflues.»
- «car Dieu n'en est point offensé.»

#### O que a colação não pega

- **Pontuação:** não foi colada sistematicamente. Corrigiram-se os casos achados pelos tradutores e pelas varreduras: maiúscula depois de vírgula, sinais soltos, espaço faltando.
- **Erros de uma letra:** a normalização apaga os que formam outra palavra com a mesma forma normalizada, como um acento trocado. A varredura de vocabulário só pega os que não existem como palavra («dé penser», «Philothëe»).
- **Margem de erro:** podem sobrar erros miúdos desse tipo.

## O que foi limpo

O script é `ferramentas/cache/filoteia/preparar.py`. Para reproduzir:

```
python preparar.py
```

- **Retirados:**
  - as notas de rodapé de Boulenger, que são glosas de vocabulário («meshui : désormais» etc.) e não do autor;
  - o léxico do fim do volume e o estudo introdutório de Boulenger;
  - as chamadas de nota e os números de página do Wikisource;
  - os filetes («______») e o «FIN».
- **Itálico** do Wikisource conservado como `_..._`. Isso inclui os subtítulos internos das meditações (*Préparation*, *Considérations*, *Affections et résolutions*, *Conclusion*, *Faites un bouquet...*), que ficaram como parágrafos próprios, em itálico, como no livro.
- **Sumários das partes:** o sumário de cada parte («_Contenant les avis et exercices..._») abre o arquivo da parte, como parágrafo em itálico.
- **Versalete** convertido em maiúsculas («VIVE JÉSUS»).
- **Versos** citados com `| `, um por linha. São dois dísticos:
  - «En son beau vêtement de drap d'or recamé...», em III.1;
  - «A cause des biens que j'attends...», em V.18.

  Na tradução, vão em verso pelo método do Versificador.
- **Títulos de capítulo** no formato `## Chapitre N — Título`, com o título por extenso tirado do índice do livro.
  - Os números de parágrafo das meditações («1.», «2.» ...) são do autor e ficaram.
- **Apóstrofo:** o apóstrofo reto que sobrava em 22 lugares virou tipográfico (’), como no resto do texto.
- Nada foi modernizado além do que Boulenger já modernizara.
- O texto do Wikisource foi emendado por Annecy onde a colação achou lacunas e erros (ver «Conferência com Annecy»).

## Convenção das marcas

`[I.1]` = parte (romano) e capítulo (arábico), na numeração do autor. Fica no começo do primeiro parágrafo de cada capítulo.

| Parte | Capítulos | Marcas |
|---|---:|---|
| Primeira | 24 | `[I.1]`…`[I.24]` |
| Segunda | 21 | `[II.1]`…`[II.21]` |
| Terceira | 41 | `[III.1]`…`[III.41]` |
| Quarta | 15 | `[IV.1]`…`[IV.15]` |
| Quinta | 18 | `[V.1]`…`[V.18]` |

A Oraison dédicatoire e a Préface não têm marca.

Não há notas do autor nesta edição; por isso o arquivo não tem `[n]` nem `¤`.

## Contagens

Palavras contadas por espaços, sem cabeçalho, marcas e prefixos. As contagens são as de depois das emendas da colação; parágrafos, títulos e marcas não mudaram.

| arquivo | conteúdo | parágrafos | títulos `##` | marcas | palavras |
|---|---|---:|---:|---:|---:|
| 00-oracao-e-prefacio.txt | Oraison dédicatoire; Préface | 13 | 2 | 0 | 1.990 |
| 01-primeira-parte.txt | 1ª parte, cap. I–XXIV | 208 | 24 | 24 | 13.714 |
| 02-segunda-parte.txt | 2ª parte, cap. I–XXI | 105 | 21 | 21 | 14.186 |
| 03-terceira-parte-a.txt | 3ª parte, cap. I–XIII | 90 | 13 | 13 | 15.461 |
| 03-terceira-parte-b.txt | 3ª parte, cap. XIV–XXVII | 89 | 14 | 14 | 13.154 |
| 03-terceira-parte-c.txt | 3ª parte, cap. XXVIII–XLI | 101 | 14 | 14 | 14.490 |
| 04-quarta-parte.txt | 4ª parte, cap. I–XV | 89 | 15 | 15 | 13.468 |
| 05-quinta-parte.txt | 5ª parte, cap. I–XVIII | 81 | 18 | 18 | 7.019 |
| **total** | | **776** | **121** | **119** | **93.482** |

## O texto pode ir ao lado da tradução?

Sim (`original_ao_lado = True`). É uma transcrição do Wikisource sobre fac-símile, conferida com Annecy.

## Problemas e dúvidas

1. **Ortografia de Boulenger.** A ortografia modernizada é obra do editor, o abade Fernand Boulenger. Não verificamos a data da morte dele. Uma simples atualização de grafia de um texto em domínio público dificilmente gera direito autoral, mas, se o Gere preferir eliminar o risco, o caminho é Annecy (1893), com a grafia de 1619. Nesse caso, o texto teria de ser preparado de novo a partir do OCR de Annecy, com bem mais trabalho. Não usamos nada mais de Boulenger: nem estudo, nem notas, nem léxico.
2. **Wikisource:** a transcrição tinha lacunas de linha inteira e erros de palavra, agora emendados por Annecy (ver «Conferência com Annecy»). Podem sobrar erros de uma letra que formam outra palavra válida, e a pontuação não foi colada.
3. **Arquivos longos:** os arquivos da 3ª parte têm entre 13 e 15,5 mil palavras. Convém dividir a tradução por capítulos, se preciso.
