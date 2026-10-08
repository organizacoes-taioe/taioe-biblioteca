# Notas do tradutor: Segunda parte (cap. I–XXI)

Arquivo: `traducao/02-segunda-parte.txt`. Texto-base: `original/02-segunda-parte.txt` (Boulenger, 1909, texto de 1619, via Wikisource).
Texto de conferência: Annecy, t. III (1893), no OCR de `ferramentas/cache/filoteia/annecy3.txt`. Além da consulta pontual, rodei uma colação palavra a palavra só desta Parte (as funções de `colacao.py`, com limiar de 1 a 3 palavras, temporários em `C:\Users\geren\AppData\Local\Temp\claude\introducao-a-vida-devota-02\`). Ela achou quatro lacunas de Boulenger que a colação geral do LEIAME não registrou (ver «Emendas»).

## O que foi conferido

- **Parágrafos.** 127 blocos no francês e 127 na tradução, contando o cabeçalho, o sumário e os 21 títulos (105 parágrafos de texto, como no LEIAME), na mesma ordem.
- **Títulos.** Os 21 `## Chapitre N — ...` viraram `## Capítulo N — ...`, com os números romanos como estão.
- **Marcas.** As 21 marcas, de `[II.1]` a `[II.21]`, iguais e na mesma ordem, no começo do primeiro parágrafo de cada capítulo.
- **Chamadas e notas.** Não há `[n]` nem `¤`, como diz o LEIAME.
- **Itálicos.** Os 15 do original, nos mesmos lugares: o sumário, *Pater*, *Ave Maria*, *Credo*, *Pater noster*, e os títulos *Tratado da oração*, *Combate espiritual*, *Confissões*, *Crônicas de são Francisco*.
- **Numeração** «1.», «2.»... dos conselhos (II.1, II.10, II.11, II.14): a mesma, parágrafo a parágrafo; também a numeração interna de II.14, ponto 5 (as seis partes da missa).
- **Pontuação.** «!» bate (16 × 16). «?»: 11 × 9, porque dois «?» de Boulenger são erro por vírgula (ver «Emendas»). Os «;» e «:» são um pouco mais numerosos na tradução (175 × 165; 79 × 77) por desdobramento de frases. Aspas «» iguais parágrafo a parágrafo, salvo um «»» solto de Boulenger em II.7, retirado.
- **Tamanho.** Todos os 105 parágrafos ficaram entre 80% e 106% do original (em caracteres). Nenhum abaixo da metade.
- **Mesóclise.** O `grep` do CONVENCOES e a varredura em Python com `(?![A-Za-zÀ-ÿ])` não acharam nada. Futuros com pronome resolvidos com próclise ou outra construção: «vós lhe pedireis perdão» (II.10), «há de se considerar» (II.11, *on considérera*), «teríeis muita sonolência» (II.1.9, em vez do futuro do pretérito com pronome), «Às vezes vos acontecerá» (II.8), «haveis de tornar-vos toda bela» (II.21).
- **Versos.** Não há versos neste arquivo.

## Decisões gerais

- **Tratamento.**
  - Filoteia por **vós** em todo o arquivo, com o feminino que o francês marca: *obligée*, *consolée*, *instruite*, *prosternée*, *séparée*, *présente*, *jointe et unie*, *disposée*, *trompée*, *tourmentée* («obrigada», «consolada», «instruída», «prostrada», «separada», «presente», «junta e unida», «disposta», «enganada», «atormentada»), e «vós mesma» (II.9, II.10).
  - Deus e Jesus, nas orações e nas citações dos salmos, por **vós** («Não me rejeiteis», «Ó Senhor, eis aqui este pobre e miserável coração»).
  - **Falas citadas**, como no original: santo Anselmo aos da comitiva, por *vous* → «vós rides»; Constantino aos monges → «Como vos admirais»; são Francisco ao companheiro → «Olhai», e ao cordeirinho por *tu* → «como representas»; Elzeário a Delfina → «se me quiserdes ver, procurai-me»; santa Catarina aos que a censuravam → «peço-vos que também vós não o vitupereis»; o Juiz aos condenados → «Miseráveis, por que morrestes».
  - **A própria alma** (II.12, «Où sommes-nous, ô mon âme?») só aparece em vocativo, sem verbo: «Onde estamos, ó minha alma?».
  - **O «on» do exame de consciência** (II.11) ficou impessoal com «se»: «Agradece-se a Deus», «Examina-se como se procedeu».
- **Maiúsculas.** As de reverência, onde o texto as põe: *Majestade*, *Salvador*, *Divindade*, *Esposo*, *Esposa* (a do Cântico, em II.18), *Rei celeste*, *Juiz*, *Corpo*, *Sacramento*, *Paixão*, *Natividade*, *Ascensão*, *Sol de justiça*, *Providência*, *Anjos* (só na citação do salmo em II.16, onde Boulenger a põe). *Saint* com nome, em minúscula. *Partie* → «Parte» (II.19), como na nota 01.
- **«missa» em minúscula.** O guia, na tabela, escreve «a santa Missa»; Boulenger escreve sempre *messe* em minúscula, e as traduções da Primeira e da Quinta Parte puseram «santa missa». Segui o original e as outras Partes (ver «Dúvidas»).
- **Nomes de autores** (II.1, II.6, II.17): deixados como o autor os escreve, pelo sobrenome, na forma portuguesa quando há uma usual: Bellintani (Mattia Bellintani), Bruno (Vincenzo Bruno), Capilia (dom André Capilla), Granada (Luís de Granada), Du Pont (Luis de la Puente: mantive a forma francesa do autor), Arias (Francisco Arias), Gerson, Dionísio Cartuxo, Luís Blósio, Stella (Diego de Estella), Pinelli (Luca Pinelli), Ávila (são João de Ávila).
- **Citações da Escritura.** Traduzidas do francês do autor, sem referência acrescentada: Sl 138 («Se eu subo ao céu»), Gn 28 (Jacó: «terrível», como *terribilis* da Vulgata), At 17,28, Ct 2,9 (as grades), Sl 50 e 118 (II.3, «a vossa serva», no feminino, como o francês para Filoteia), Gn 32 (Jacó), Mt 15 (a cananeia), Sl 30 e 90, com eco de Is 25,4 (II.12, o refúgio), Sl 72, 15, 122 e 24 (II.12), Sl 72,26 («Deus do seu coração», II.2), Sl 101 (o pelicano, a coruja, o pardal), Sl 68 (II.13), Sl 137 (II.16), Lc 2 (II.17), Ap 3,20 e o Cântico (II.18), Sl 94 (os quarenta anos), Ct 5 (II.18), Jo 6 (II.20), Mt 8 (II.21, «Senhor, eu não sou digno», no masculino, como na fórmula litúrgica).

## Termos

| francês | tradução | onde / observação |
|---|---|---|
| *oraison* | oração | passim; *oraison mentale / vocale* → «oração mental / vocal», como no guia |
| *prière*, *prier* | prece, oração; rezar, rogar | II.8 «a prece» (ao lado de «ação de graças, oferecimento»); «rezar» no sentido comum |
| *avis* | avisos | sumário, título de II.8 (como nas notas 00 e 01) |
| *élancements* | impulsos | II.11, II.13, II.21; «estes impulsos de Davi» (II.13). Na Quinta Parte, «impulsos» também |
| *saillies* | arroubos | II.13 |
| *traits d'amour* | dardos de amor | II.13 (*trait* = flecha, eco de «jaculatória») |
| *retraite spirituelle*; *faire leur retraite* | retiro espiritual; fazer o seu retiro | II.12, II.13, II.17, II.18, como no guia; das aves, «para se recolherem» |
| *bouquet* | ramalhete | II.7, II.13 |
| *colloque* | colóquio | II.8 |
| *fabrication du lieu*; *leçon intérieure* | fabricação do lugar; lição interior | II.4. É a «composição de lugar» inaciana; guardei a palavra do autor |
| *loisir* | vagar | II.11, II.12 (como nas notas 00, 01, 05) |
| *dîner*; *souper*; *collation* | almoço; ceia; colação | II.1.3, II.1.9, II.11. *Dîner* é a refeição do meio-dia (II.1 a põe depois da manhã); ver «Dúvidas» |
| *chapelet* | terço | II.1.7 |
| *Manuels et Heures* | Manuais e Horas | II.1.7 (os livros de horas) |
| *père spirituel*; *guide*; *conducteur*; *directeur* | pai espiritual; guia; condutor; diretor | segui a palavra do autor em cada lugar; «condutor» em II.18 e II.20, como na Quinta Parte (a Primeira usou «guia»; ver «Dúvidas») |
| *contenances* | modos; postura | II.1 «aprendereis os seus modos»; II.9 «postura devota» |
| *viande(s)* | alimento(s) | II.1, II.20, II.21 («alimento celeste», «alimento de suavidade», «alimentos sólidos») |
| *agencements et surgeons* | ramificações e rebentos | II.10 (as orações curtas que brotam da grande) |
| *par manière d'agencement* | como por enfeite | II.19 (confissão feita por forma, para compor) |
| *forts* (dos cervos) / *fort* | esconderijos / fortaleza | II.12; o jogo de *forts* / *fort* não passa |
| *masures* | ruínas | II.12, Sl 101 |
| *chat-huant ou hibou*; *hibou* | a coruja ou o mocho; o mocho | II.12 |
| *établerie* | estábulo | II.12 |
| *tracas* | lida; azáfama | II.8 «a lida da sua casa»; II.12 «a azáfama dos negócios» (como «azáfama» no Prefácio) |
| *hantise, privauté et familiarité* | convivência, intimidade e familiaridade | II.13 |
| *divertissements* | desvios | II.13 (as breves pausas de atenção) |
| *dilection* | dileção | II.13 |
| *cogitations* | cogitações | II.13 |
| *tourne-soleil* | girassol | II.13 |
| *levraut* | filhote de lebre | II.13 |
| *train* | comitiva | II.13 |
| *détroit de la mort* | estreito da morte | II.13 |
| *force forcée* | força maior | II.14; a redundância do francês não passa |
| *officier* (o padre na missa) | ministro | II.14 |
| *protestez de vouloir* | protestai que quereis | II.14 (do verbo; como *protestation* → «protestação» nas outras Partes) |
| *communion* (= o que é comum) | o que é comum | II.15: *que la communion soit préférée à toute sorte de particularité* → «que o que é comum seja preferido a toda sorte de particularidade»; «comunhão» se leria como a Eucaristia |
| *commandées / recommandées* | mandadas / recomendadas | II.15: o jogo passa |
| *inspirations / aspirations* | inspirações / aspirações | II.16: passa |
| *trépassés* | defuntos | II.16 |
| *damoiselle* | senhora; donzela | II.16 «uma senhora, então jovem»; II.18 «a donzela que se quer casar» |
| *gentilhomme* | fidalgo | II.18 |
| *agréer* | acolher | II.18 (o segundo dos três atos, o noivado e a inspiração) |
| *délectation* | deleite | II.18, como no guia |
| *méconnaissants* | ingratos | II.18 |
| *accostée*, *accointance* | que se juntou; trato | II.19 (a leoa e o leopardo) |
| *naïvement* | com singeleza | II.19 (sem a nuance de «ingênuo») |
| *chérir le prochain* | querer bem ao próximo | II.19 |
| *conversation* | companhia | II.19 «o prazer da companhia» (no jogo) |
| *chagrin* | mau humor | II.19 (ao lado da tristeza); a Quinta Parte usou «despeito», ao lado da ira |
| *mithridat* | mitridato | II.20 |
| *imbéciles* | débeis | II.20 |
| *exquise* | apurada | II.20 (a disposição para a comunhão diária) |
| *bizarres*; *coquilleux* | caprichosos; melindroso | II.20 (como «caprichoso» na nota 00) |
| *à l'aventure* | porventura | II.20 |
| *Saint Sacrement* | Santo Sacramento | II.21 |

**Nomes:** Jacó, Davi, santo Estêvão, a Madalena, são João, o bom ladrão; santa Catarina de Sena; o bem-aventurado Elzeário, conde de Ariano, e Delfina; santo Agostinho e a senhora Proba; santo Antão; são Gregório, bispo de Nazianzo (II.13) e são Gregório Nazianzeno (II.13, fim), como o autor varia; Máximo; são Fulgêncio, bispo de Ruspe; Teodorico, rei dos godos; santo Anselmo, arcebispo de Cantuária; Constantino, o Grande; são Francisco (de Assis); Francisco de Borja, duque de Gandia; são Basílio; santa Francisca (Romana); são Jerônimo e santa Paula; são João Crisóstomo; Pedro Fabro, Inácio, a aldeia de Villaret; são Paulo, primeiro eremita; madre Teresa; são Carlos Borromeu; são Luís; são Bernardo; santa Maria Egipcíaca; são Simeão Estilita; santa Catarina de Gênova; santa Ângela (de Foligno); Mitridates, rei do Ponto.

## Passagens difíceis

- **II.1.2, *la mentale et cordiale*.** O substantivo fica subentendido, como no francês: «a mental e cordial» (a oração).
- **II.1.2, *l'arbre de désir*.** «A árvore do desejo»: eco de Ct 2,3 (*sub umbra illius quem desideraveram sedi*). Literal.
- **II.1.4, *ne pourra vous bonnement empêcher*.** *Bonnement* = de boa-fé, com razão: «poderá de boa-fé impedir-vos».
- **II.1.9, *ce faisant sur icelui*.** «Se o fizésseis logo em cima dela» (da refeição). Reescrevi a oração para evitar o futuro do pretérito com pronome.
- **II.1.9, *vous remettre en train*.** «Retomar o costume».
- **II.2, *en attendant que ... vous en puissiez être plus amplement instruite*.** «Enquanto ... não vierdes a ser mais amplamente instruída».
- **II.3, *la bien servir*.** O *la* é a Majestade: «a graça de bem a servir e adorar».
- **II.4, *l'épervier à ses longes*.** «Como se prende o gavião pelas suas correias, para que fique pousado no punho» (as *longes* são as correias da falcoaria).
- **II.6, *la crainte de la disgrâce de Dieu, du jugement et de l'enfer*.** *Disgrâce* = perda do favor: «o temor do desfavor de Deus, do juízo e do inferno», que guarda a série de genitivos.
- **II.6, a resolução.** *Or sus donc, je ne me piquerai plus* → «Pois bem, já não me ofenderei»: *se piquer* = ofender-se.
- **II.7, *j'ai remarqué qu'il fallait dire*.** *Remarquer* aqui é «indicar» (nas meditações da Primeira Parte): «indiquei que se devia dizer». O mesmo em II.12 e II.18 (*que je vous ai remarquées*, *que j'ai marquées*).
- **II.8, *nous étant bien avis*.** «Parecendo-nos bem».
- **II.8, *plaidoirie*; *trafic*.** «As defesas no tribunal»; «o seu comércio» (*trafic* = negócio, sem a nuance moderna).
- **II.9, *Si ne vous laisserai-je point. Seigneur, que...*.** O ponto de Boulenger depois de *point* quebra a frase de Gn 32,26; Annecy a lê inteira. Traduzi «Não vos deixarei, Senhor, enquanto não me tiverdes dado a vossa bênção».
- **II.9, *Combien de courtisans ... rendre leur devoir.*** Pergunta exclamativa terminada com ponto, como no Prefácio (nota 00, P9): o ponto ficou. *Rendre leur devoir* → «cumprirem o seu dever», repetido na frase seguinte, como no francês.
- **II.9, *que ce nous est un honneur trop plus grand*.** «Com saber que já é para nós uma honra grande demais»: *trop plus* = muito mais (do que merecemos).
- **II.11, *une douzaine de vives aspirations ... que vous ferez sur ce divin Sauveur*.** «Que lançareis para esse divino Salvador».
- **II.12, *Bienheureuse sera l’âme ...*.** Eco dos Sl 30 e 90 e de Is 25,4; «a minha casa de refúgio, a minha muralha segura» (*rempart*).
- **II.12, *Nativité*.** «Natividade», com maiúscula, como o texto.
- **II.12, *Elzéar, comte d'Arian en Provence*.** Elzéar de Sabran, conde de Ariano (o feudo é no reino de Nápoles; a família, provençal). Traduzi como o autor: «conde de Ariano, na Provença».
- **II.13, *et si, cet exercice n'est point malaisé*.** *Et si* = e além disso (ou: e contudo). Ficou «e, além disso, este exercício não é difícil».
- **II.13, *comme dit saint Augustin après saint Antoine*.** É o santo Antão do deserto (o «livro da natureza»), o mesmo do episódio de Constantino logo abaixo.
- **II.13, *il fit cette belle pensée*.** «Formou ele este belo pensamento».
- **II.13, *la pauvre bête*.** «O pobre bicho» (o filhote de lebre).
- **II.13, *Comme admirez-vous ... Admirez plutôt de quoi Dieu éternel a écrit*.** *Comme* = por que, como; *de quoi* = de que: «Como vos admirais de que um rei escreva a um homem? Admirai-vos antes de que o Deus eterno tenha escrito a sua lei aos mortais, e mais ainda, lhes tenha falado...». Annecy dá a mesma lição.
- **II.13, *pensées de jardin ... telles sont mes cogitations*.** O autor joga com *pensée*, a flor e o pensamento. Em português a flor é o «amor-perfeito», mas também se chama «pensamento» (Houaiss); traduzi «uns pensamentos de jardim», com «de jardim» desfazendo a ambiguidade como no francês, e «cogitações» para *cogitations*. O jogo passa em parte.
- **II.13, *détournent ... contourner ... contournent*.** «Desviam as criaturas do seu Criador para as volver ao pecado; ... volvem as criaturas para a glória»: a repetição *contourner / contournent* passa com «volver».
- **II.13, último parágrafo, *Or, cet exercice ... gît la grande œuvre*.** Frase sem preposição em Boulenger; ver «Emendas».
- **II.14.4, *d'une présence réelle*.** «Com uma presença real», em oposição a «presença espiritual».
- **II.15, *Confessions*.** Sem itálico aqui, como no original (em II.17 o título está em itálico, e ficou).
- **II.16, *mère de notre souverain Père, et par conséquent notre grand'mère*.** Literal: «mãe do nosso soberano Pai, e por consequência nossa avó»; *petits-enfants* → «netinhos», que guarda a imagem.
- **II.16, *avec tant de recommandation*.** «Com tanto encarecimento».
- **II.17, *son Enfant*.** «O seu Menino», com maiúscula, como o texto.
- **II.17, *selon votre vacation, Car bien que*.** Boulenger abre aí, depois de vírgula, um *Car* maiúsculo; fiz frase nova («Porque, embora...»).
- **II.18, *premièrement, il nous la propose*.** «Primeiramente nos propõe essa ação», para evitar «no-la propõe».
- **II.18, *désobligé*.** «Ficaria bem magoado».
- **II.19, *vous vous accusez de n'avoir pas chéri*.** Indicativo, não imperativo: «Por exemplo, vós vos acusais de não ter querido bem ao próximo».
- **II.19, *qui ne fait ni froid ni chaud*.** «Que não faz nem frio nem calor», expressão viva no português do Brasil.
- **II.19, *me dira quelque légère parole*.** O futuro hipotético do francês ficou no presente («me diz ... eu a tomo a mal»), mais natural em português.
- **II.19, *contre une personne, ayant pris de lui ... celui-là*.** O francês passa de *personne* a *lui*; ficou «contra uma pessoa, tendo tomado a mal alguma coisa que ele me disse, ... mas porque aquele homem me era desagradável».
- **II.20, *le tort qu'ils ont eu*.** «O erro que cometeram em morrer espiritualmente».
- **II.20, Agostinho.** *je le suade* → «a isso persuado» (*suadeo*). *Vitupérer* → «vituperar», que guarda a repetição de santa Catarina.
- **II.20, *l'affection de pécher / l'affection du péché*.** «A afeição de pecar» (a vontade de cometê-lo) e «a afeição ao pecado» (o apego a ele): a distinção é do autor (ver «Emendas», 3).
- **II.20, *Dieu trouvait mauvais en l'ancienne Loi*.** Dt 15; «exigissem o que se lhes devia nos dias de festa».
- **II.21, *Celui lequel, auquel, par lequel et pour lequel vous croyez, espérez et aimez*.** «Aquele em quem, a quem, por quem e para quem credes, esperais e amais»: as quatro preposições ficaram.
- **II.21, *communiquer avec votre perfection*.** O autor joga com *communier / communiquer*: «comunicar com a vossa perfeição» guarda o eco com «comungar».
- **II.21, *se réduit en viande*.** «Se reduz a alimento».

## Remissões

Não há remissões de página. As remissões internas ficaram como estão: «as meditações que vos dei» (II.5), «as quatro maneiras que vos indiquei» (II.12), «os capítulos XXVII, XXVIII, XXIX, XXXV e XXXVI da terceira Parte e o capítulo VIII da quarta Parte» (II.19; ver «Dúvidas»).

## Emendas

Erros de transcrição de Boulenger/Wikisource, corrigidos sem efeito no sentido:

1. **II.1, *ceux que je vous conseille son saint Bonaventure ... Grenade Du Pont*** → *sont* e *Grenade, Du Pont* (Annecy).
2. **II.1.6, *_Ave Maria_et le_Credo_en latin*, *seul_Pater_*** → espaços restituídos.
3. **II.4, *d user*; II.12, *d\*y demeurer*; II.13, *dé penser*, *la (grève*, *repreliait*, *fort| étonnés*, *nangé*; II.14, *la| sainte messe*, *de de Notre Seigneur*; II.19, *Phi- lothée*, *les même choses*, *il veulent*; II.20, *tnithridat*, *aisé- ment*, *excercice*; II.21, *reçu,excitez*, *réellementà*, *comiinuniez*** → sobras de OCR e erros de letra, corrigidos.
4. **II.6, *André Capilia, | et voyez*** → o «|» solto foi retirado (não é verso).
5. **II.7, *celle de la supplication » par laquelle*** → vírgula (Annecy). O «»» solto foi retirado.
6. **II.13, primeiro parágrafo, *l'une l'autre. et toutes deux*** → vírgula.
7. **II.13, *ne s'arrêtent que pour mieux aller*** → *ne s'arrêtant* (Annecy): «não parando senão para andar melhor».
8. **II.13, último parágrafo, *Or, cet exercice ... gît*** → *Or, en cet exercice ... gît* (Annecy): «Ora, neste exercício ... está a grande obra da devoção».
9. **II.14.1, *âme de la piété ? mystère ineffable*** → vírgula (Annecy). **II.16, *imiter ? et en l'intercession*** → vírgula (Annecy).
10. **II.16, *égales et pareilles aux anges et, font*** → *aux Anges, font* (Annecy).
11. **II.19, *vous deviez; ... et dites:ayant vu ... comme vous devez;*** → espaços e pontuação normais.

Lacunas de Boulenger (as quatro já estão no Wikisource, não vêm da preparação do arquivo), preenchidas por Annecy:

12. **II.4, depois de *si vous voulez méditer Notre Seigneur*.** Boulenger salta do primeiro *Notre Seigneur* ao segundo (salto do mesmo ao mesmo) e a frase fica sem sentido («Par exemple, si vous voulez méditer Notre Seigneur, en la façon que les Évangélistes le décrivent.»). Annecy: *en croix, vous vous imaginerez d'estre au mont de Calvaire et que vous voyes tout ce qui se fit et se dit au jour de la Passion; ou, si vous voules, car c'est tout un, vous vous imaginerez qu'au lieu mesme ou vous estes se fait le crucifiement de Nostre Seigneur*. Traduzi o trecho de Annecy: «Por exemplo, se quiserdes meditar Nosso Senhor na cruz, imaginareis estar no monte Calvário e ver tudo o que se fez e se disse no dia da Paixão; ou, se quiserdes, porque é tudo um, imaginareis que no mesmo lugar onde estais se faz a crucifixão de Nosso Senhor, da maneira como os Evangelistas a descrevem.» São 37 palavras. A colação geral (`colacao.out`, posição 20504) já tinha o trecho, mas ele ficou entre as sobras atribuídas ao aparato.
13. **II.19, *expliquez si ç'a été pour le plaisir de la conversation*.** Annecy: *si ç'a esté pour le désir du gain, ou pour le playsir de la conversation*. Traduzi «explicai se foi pelo desejo do ganho ou pelo prazer da companhia».
14. **II.20, *parce que non seulement vous n'avez pas même l'affection du péché*.** Frase sem sentido em Boulenger (outro salto). Annecy: *parce que non seulement vous n'aves pas l'affection de pécher, mais vous n'aves pas mesme l'affection du péché*. Traduzi «porque não só não tendes a afeição de pecar, mas nem sequer tendes a afeição ao pecado».
15. **II.21, *pour vous purifier de vos imperfections, pour vous consoler*.** Annecy: *pour vous purifier de vos imperfections, pour vous délivrer de vos misères, pour vous consoler*. Traduzi «para vos livrardes das vossas misérias».

Diferenças de Annecy não seguidas (sem efeito, ou duvidosas):

- **II.13, *car il vous en fournit*** (Boulenger) × *fournira* (Annecy). Segui Boulenger: «porque ele vos fornece».
- **II.13, *ne trouve point d'arbre*** (Boulenger) × *trouvent* (Annecy). Concordância no plural em português, como pede o sujeito: «não encontram árvore».
- **II.19, *lisez attentivement les chapitres XXVII...*** (Boulenger) × *lisez diligemment les chapitres VI, XXVII...* (Annecy, que acrescenta o capítulo VI). Segui Boulenger; ver «Dúvidas».
- **II.20, *Quant aux maladies corporelles...*.** Annecy faz parágrafo à parte; Boulenger o une ao anterior. Segui Boulenger, para manter a contagem de parágrafos.

## Dúvidas para quem coordena

1. **As quatro lacunas de Boulenger** (Emendas 12 a 15). Preenchi-as por Annecy, porque sem elas duas frases não têm sentido (II.4, II.20) e as outras duas perdem um membro da enumeração. O LEIAME diz que «não há omissões»; convém corrigir o LEIAME e, se a casa quiser, acrescentar o trecho também a `original/02-segunda-parte.txt` (não toquei no original). As outras Partes podem ter lacunas semelhantes que a colação geral escondeu entre as sobras de aparato: a de II.4 estava em `colacao.out` e foi tomada por variante.
2. **II.19, capítulo VI da terceira Parte.** Annecy, no texto de 1619, manda ler também o capítulo VI da Terceira Parte e diz *diligemment*; Boulenger não tem o VI. Segui Boulenger. Se o fac-símile de 1619 der o VI, acrescenta-se «VI,» na lista.
3. ***Dîner* / *souper*.** Usei «almoço» e «ceia» (e «colação» para *collation*), porque *dîner* é aqui a refeição do meio-dia e *souper* a da noite. Outra Parte usou «jantar» para *dîner* («antes do jantar»), que no Brasil se lê como a refeição da noite. **Proposta para o CONVENCOES:** *dîner* → almoço; *souper* → ceia.
4. ***Conducteur*.** A Primeira Parte usou «guia»; a Quinta, «condutor»; eu segui a palavra do autor («guia» para *guide*, «condutor» para *conducteur*, «diretor» para *directeur*). Convém fixar no guia.
5. **«missa» × «Missa».** O guia escreve «a santa Missa»; o original e as outras Partes, minúscula. Segui a minúscula (7 ocorrências). Se a casa preferir a maiúscula, é uma troca simples em todos os arquivos.
6. ***Élancements* → «impulsos».** Termo frequente nesta Parte (aspirações e orações jaculatórias). **Proposta para o guia**, ao lado de *aspirations* → aspirações.
7. ***Du Pont*.** Deixei o nome como o autor o escreve (é Luis de la Puente). Se a casa preferir a forma espanhola, são duas ocorrências (II.1, II.17).
