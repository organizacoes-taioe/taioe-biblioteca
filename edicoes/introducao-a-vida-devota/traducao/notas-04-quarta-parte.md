# Notas do tradutor: Quarta parte da Introdução

Arquivo: `traducao/04-quarta-parte.txt`. Texto-base: `original/04-quarta-parte.txt` (Boulenger, 1909, texto de 1619, via Wikisource).
Texto de conferência: Annecy, t. III (1893), no OCR de `ferramentas/cache/filoteia/annecy3.txt`, consultado em todas as passagens duvidosas (lista em «Emendas»).

## O que foi conferido

- **Parágrafos.** 89 no francês e 89 na tradução (o sumário da parte e 88 parágrafos de texto), na mesma ordem.
- **Títulos.** Os 15 títulos `## Chapitre N — ...` viraram `## Capítulo N — ...`, com os romanos iguais.
- **Marcas.** As 15 marcas, de `[IV.1]` a `[IV.15]`, iguais, no começo do primeiro parágrafo de cada capítulo.
- **Notas.** O arquivo não tem chamadas `[n]` nem notas `¤`, como diz o LEIAME.
- **Cabeçalho.** Só `# titulo: Quarta parte da Introdução`, como em `00-oracao-e-prefacio.txt`.
- **Itálico.** O único itálico do arquivo (o sumário «_Contenant les avis..._») ficou em itálico.
- **Numeração do autor.** Os «1.», «2.»... de IV.3, IV.13, IV.14 e IV.15 (inclusive a numeração dentro do ponto 4 de IV.13) estão todos, na mesma ordem.
- **Pontuação.** Mesmo número de «?» e «!» em cada parágrafo, salvo onde houve emenda (ver abaixo: IV.12, um «!» espúrio de Boulenger).
- **Tamanho.** Cada parágrafo traduzido tem entre 82% e 112% do tamanho do original. Os três mais curtos (IV.8, primeiro parágrafo de IV.12, ponto 6 de IV.14, de 82% a 85%) foram relidos frase a frase: não falta nada; o francês é que é mais longo (*il nous faut*, *on lui ôtera même ce qu'il n'a pas*...).
- **Mesóclise.** O `grep` do CONVENCOES e a varredura em Python com `(?![A-Za-zÀ-ÿ])` não acharam nada. Também não há *no-la*, *vo-la*, *lho*, *mas* (= *me + as*): ver «Decisões gerais».
- **Versos.** Não há versos neste arquivo (os dois dísticos da obra estão em III.1 e V.18).

## Decisões gerais

- **Tratamento.**
  - Filoteia, por **vós**, com as concordâncias no feminino que o francês faz: «rejeitada por ele» (IV.1), «corajosa», «vencida» (IV.3), «afligida», «humilde e temerosa» (IV.5), «tentada» (IV.6), «inclinada», «sujeita» (IV.10), «apertada», «livrada», «aquietada» (IV.11), «atingida» (IV.12), «privada», «simples e franca» (IV.14). Nas orações postas na boca dela, também: «antes de ser humilhada» (IV.14, 1; o francês tem *humiliée*) e «quando estou entregue a mim mesma» (IV.14, 1; o francês não marca o gênero, mas a oração é de Filoteia).
  - Deus e Jesus, por **vós**, nas orações e jaculatórias.
  - **Tu**, onde o francês tem *tu*: Jesus a santa Catarina (que lhe responde por *vós*, como no original), o inimigo à alma seca («Ah! pobrezinha, onde está o teu Deus?»), são Luís ao filho, Godofredo e o amigo, Pr 25,16 («Achaste mel?»), e o «Para trás, ó Satanás». Em IV.14, 2, a alma fala ao vento frio por *tu* («Retira-te daqui, ó aquilão») e ao vento das consolações por *vós* («vinde... soprai»), como o francês (*Ote-toi* / *venez*).
- **Pronomes combinados.** Evitei *no-la*, *no-los*, *vo-la*, *lhos*, que soam lusitanos e arcaicos no Brasil (a tradução de 00 fez o mesmo com «deu-lha»): «Deus, que a dá a nós» (IV.13, 4), «é a mão de Deus que os põe em nosso coração», «as põe em nossa boca...», «segundo a intenção Daquele que as dá a nós», «porque Deus as envia a nós»; «se alguma paixão e inquietação a arrebatou de vós» (IV.11); «o coração que os oferece» (IV.14, 5); «o Senhor me privou delas» (IV.14, 4, por *le Seigneur me les a ôtées*; «mas tirou» confundiria com a conjunção); «deixa de nos tentar com elas» (IV.9, *il cesse de nous en faire*).
- **Minúscula depois de «?» e «!».** Onde o francês continua a frase em minúscula depois de «?» ou «!» («Y a-t-il une attention plus chagrine... ? les mondains néanmoins...»), mantive a minúscula, como manda o CONVENCOES («pontuação como no original»). Ocorre em IV.1, IV.4, IV.13, IV.14, IV.15.
- **Maiúsculas.** As do original: *Salvador*, *Majestade*, *Esposo* (o divino Esposo, o Esposo das nossas almas), *Esposa sagrada*, *Consolador*, *Apóstolo*, *Antigos*, *Paixão*, *santa Cruz*, *santa Comunhão* (em IV.1 *communion* está em minúscula e ficou «comunhão»), *Nome*. *Celui* com maiúscula em IV.13, 4 → «Daquele», «Aquele». *Mon cher époux* (IV.12), em minúscula em Boulenger, ficou «meu querido esposo» (Annecy tem *Espoux*).
- **Aspas.** «...», sem espaço interno, como pede o guia; não há aspas internas neste arquivo.

## Termos

| francês | tradução | onde / observação |
|---|---|---|
| *avis* | avisos | sumário; IV.11 («deu este aviso ao filho»); IV.14, 3 («tomai os avisos»), como proposto nas notas de 00 |
| *s'amuser à* | deter-se em; entreter-se com | título de IV.1; IV.6, IV.7, IV.9, IV.13, IV.14 |
| *tentation; délectation; consentement* | tentação; deleite; consentimento | do guia; IV.3 a IV.7 |
| *sentir / consentir* | sentir / consentir | título de IV.3: o jogo passa |
| *se plaire* | comprazer-se | IV.3, IV.6, IV.12; *plaisir* → prazer |
| *protester, protestation* | protestar, protestação | IV.7, IV.13, como em 00 |
| *recherche* (amorosa) | corte | IV.6: «a corte desonesta que lhe é feita», «a corte que se faz ao seu amor» |
| *mugueter, muguetterie* | galantear, galanteio; namorar | IV.6, IV.10; em IV.8, *mugueter le bien d'autrui* → «namorar e cobiçar» o bem alheio (o *namorar* de «olhar com desejo») |
| *cajolerie* | falatório (IV.1); lisonja (IV.8) | em IV.1 é a tagarelice dos mundanos; em IV.8, as palavras de galanteio |
| *inquiétude* | inquietação | IV.11, do guia |
| *empressement, s'empresser* | sofreguidão, agitar-se | IV.11 |
| *tout bellement* | muito mansamente | IV.11 |
| *tristesse* | tristeza | IV.12 |
| *prière, prier* | prece, orar | IV.12 (para distinguir de *oraison* → oração) |
| *tendreté(s)* | ternura(s) | IV.13–IV.15; *attendrissements* → enternecimentos |
| *douceur(s)* | doçura(s) | IV.13–IV.14; em IV.1 *notre douceur* → «a nossa doçura» (a mansidão salesiana) |
| *dragée; grains sucrés* | confeito(s); grãos açucarados | IV.13, IV.14 |
| *pomme d'amour* | maçã de amor | IV.13; segue a «maçã» da criança |
| *avant-goût* | antegosto | IV.13, IV.15 |
| *sécheresses et stérilités* | securas e esterilidades | do guia |
| *soustractions* | subtrações | IV.14, 4 («distrações ou subtrações da devoção sensível»: o jogo de *distractions / soustractions* passa); IV.15 |
| *conducteur; directeur; guide* | condutor; diretor; guia | IV.7, IV.12, IV.13, IV.14; *celui qui conduit votre âme* → «àquele que guia a vossa alma» (IV.11) |
| *abjection* | abjeção | IV.10, IV.14 (termo salesiano, como na Terceira parte) |
| *mouchons* (das abelhas) | crias | IV.2, IV.14; ver Dúvidas |
| *avettes* | abelhinhas | IV.13 |
| *nymphes* | ninfas | IV.2, IV.14 (termo dos apicultores) |
| *épithème* | epítema | IV.5 (remédio aplicado por fora, sobre o coração) |
| *chicotin* | acíbar | IV.14 (o suco amargo do aloés) |
| *herbe scitique* | erva cítica | IV.13; ver Passagens difíceis |
| *chat-huant* | coruja | IV.1 |
| *araignes* | aranhas | IV.1 |
| *aiguille marine* | agulha de marear | IV.13 |
| *liard* | vintém | IV.13 |
| *confitures liquides / sèches* | doces em calda / doces secos | IV.14, 5 |
| *bise* | aquilão | IV.14, 2 (eco de Ct 4,16, *surge aquilo*) |

**Nomes:** são Jerônimo; santa Catarina de Sena; a bem-aventurada Ângela de Foligno (o francês tem *Foligny*; o guia dá *Foligno*, e o texto diz *bienheureuse*, «bem-aventurada», não «santa»); são Francisco (de Assis); são Bento; são Luís; são Bernardo; Godofredo de Péronne (*Geoffroy de Péronne*; ver Dúvidas); Saul, Davi, Engadi; Naamã, Eliseu, Jordão; Abraão, Isaac; Jó; Alexandre Magno; Arábia Feliz (como em 00); Calvário, Tabor; o Faraó; as parteiras do Egito.

## Passagens difíceis

- **IV.1, *calomnieront votre changement d'hypocrisie*.** «Tacharão caluniosamente a vossa mudança de hipocrisia»: *calomnier qqch. de* é acusar falsamente de.
- **IV.1, *à son refus*.** «Rejeitada por ele»: o mundo a recusou, e por isso ela recorre a Deus.
- **IV.1, *crie au ventre*.** «Se queixam do estômago».
- **IV.1, *si nous nous démettons*.** Oposto a *si nous nous parons*: deixar os enfeites. «Se nos enfeitamos... se nos desataviamos».
- **IV.1, *leurs avarices, ménages*.** *Ménage* é a boa administração da casa: «as suas avarezas, boa economia».
- **IV.1, *João... e dizeis que é samaritano*.** Em Mt 11,18-19 o Filho do homem é chamado «glutão e bebedor de vinho»; «samaritano» vem de Jo 8,48. O autor junta de memória; Annecy traz a mesma lição. Traduzi como está.
- **IV.1, *nous sommes sacrifiés à Dieu et rangés à la vie dévote*.** Mantive a passiva: «estamos sacrificados a Deus e alistados na vida devota».
- **IV.2, *étonné, étonnement*.** No século XVII, «atordoado», «desnorteado»: «um tanto desconcertados», «um pouco de estranheza».
- **IV.2, *ce dites-vous*.** Torneio de época: «dizeis vós».
- **IV.2, *des plumes comme de colombe*** (Sl 54,7). «Penas como de pomba», com a palavra do autor (*plumes*), e não as «asas» das Bíblias.
- **IV.3, *réduit l'amour de Dieu au petit pied*.** «Reduz a bem pouco o amor de Deus».
- **IV.3, *l'un se jeta dans les épines et l'autre dans la neige*.** Pela ordem da frase, Francisco teria se lançado nos espinhos e Bento na neve; a tradição conta o contrário (Bento nos espinhos, segundo são Gregório; Francisco na neve). Annecy tem a mesma ordem. Mantive o texto do autor, sem correção.
- **IV.4, *étranges accidents*.** «Estranhas comoções» (para não repetir «abalar», que traduz *ébranler* na mesma frase).
- **IV.4, *le tyran, qui se défiait de la vaincre*.** *La* é a alma do jovem: «que desesperava de vencê-la pelas dores».
- **IV.4, *ces tiennes sales cogitations de ton cœur*.** Guardei a redundância da fala: «esses teus imundos pensamentos do teu coração».
- **IV.4, *expugner*.** «Expugnar» (tomar de assalto), que existe em português culto e guarda a imagem militar.
- **IV.5, *ne vous assurant pas de pouvoir vaincre*.** «Não vos assegurando de poder vencer»: não vos dando por segura.
- **IV.6, *quoiqu'elle en fît la délicate*.** «Ainda que se fizesse de melindrosa».
- **IV.6, *toutes fois et quantes que*.** «Todas as vezes que».
- **IV.6, *peu ou prou*.** «Pouco ou muito».
- **IV.6, *chatouillement de délectation*.** «Titilação de deleite».
- **IV.7, *barguigner*.** «Regatear», como *marchander* em IV.6 e IV.14.
- **IV.8, *corrival / corrivale*.** «Rival» nos dois gêneros; o português não tem o par.
- **IV.9, *se morfondrait*.** «Se consumiria».
- **IV.11, *quant et quant*.** «Juntamente».
- **IV.11, *attrempant*.** «Temperando».
- **IV.11, são Luís.** O francês imita o falar antigo do santo rei (*ainsi pourras ton mal légèrement porter*). Traduzi em português correto, com um leve sabor antigo na ordem: «assim poderás levar ligeiramente o teu mal».
- **IV.12, *productions*.** «Efeitos» («conforme os diversos efeitos que produz em nós»), para não carregar a frase com «produções».
- **IV.12, *Mon Bien-aimé à moi, et moi à lui*** (Ct 2,16). «O meu Bem-amado é meu, e eu sou dele».
- **IV.12, *Mes yeux se fondent sur vous*** (Sl 118,82, *defecerunt oculi mei*). «Os meus olhos se consomem por vós».
- **IV.12, *Ô Jésus, soyez-moi Jésus*.** «Ó Jesus, sede para mim Jesus» (isto é, Salvador).
- **IV.12, *en fin finale*.** «Por fim e afinal».
- **IV.13, *continue l'être*.** «Conserva o ser».
- **IV.13, *tendre et prétendre à notre Dieu*.** O jogo passa: «tender e pretender ao nosso Deus».
- **IV.13, *si sommes-nous à Dieu…… ».** Mantive as reticências duplas do original (marcam o salto de Rm 14,8 para Rm 8,35).
- **IV.13, *la condition de cette vie lui apporte*.** *Lui* com antecedente *nos âmes*, no plural: «lhes traz». Annecy tem o mesmo *luy*. A concordância foi feita pelo sentido.
- **IV.13, *pierres*.** As abelhinhas abraçam «pedras», como diz o autor (*pierres*); não pus «pedrinhas».
- **IV.13, *l'herbe scitique*.** A *scythice herba* de Plínio, o alcaçuz, que tira a fome e a sede. «Erva cítica», da Cítia; não pus «alcaçuz», para não acrescentar glosa.
- **IV.13, *amadouer*.** «Agradar» o filho; *mignardise et caresse* → «o mimo e a carícia».
- **IV.13, *il m'est bon d'être avec vous*** (Mt 17,4). Dito no singular pelo autor: «é bom para mim estar convosco» («é-me bom» soaria lusitano).
- **IV.13, *As-tu trouvé le miel ? manges-en ce qui suffit*** (Pr 25,16). «Achaste mel? come dele o que basta».
- **IV.14, *en friche*.** «A terra inculta».
- **IV.14, *buque*.** «Bate» (à porta).
- **IV.14, *nous laisse croupir*.** «Nos deixa estagnar».
- **IV.14, *simple et naïve*.** *Naïf* é, na época, «natural, sem artifício»: «simples e franca».
- **IV.14, 6, *on lui ôtera même ce qu'il n'a pas*.** O paradoxo é do autor e se repete logo depois (a chuva «tira-lhes ainda a vida que não têm»). Mantido.
- **IV.14, 4, *Le Seigneur m'a donné des consolations ; le Seigneur me les a ôtées*** (Jó 1,21, adaptado pelo autor). «O Senhor me deu consolações; o Senhor me privou delas».
- **IV.15, *au voyage duquel il est question*.** O trecho é recortado de uma narrativa maior (a viagem de são Bernardo), e o autor não a apresenta. Ficou literal: «na viagem de que se trata».
- **IV.15, *se ramentevoir*.** «Lembrar-se»; *facultés* → «bens».
- **IV.15, *Je ne serai jamais ennuyé*.** *Ennui* tem aqui o sentido forte da época, aflição, abatimento: «Nunca estarei aflito»; *ennuis intérieurs* → «aflições interiores».
- **IV.15, *ès jours heureux, il se faut ressouvenir du malheur*** (Eclo 11,27). «Nos dias felizes é preciso lembrar-se da desgraça».
- **Citações.** Todas traduzidas do francês do autor, sem referência acrescentada: Jo 15,19; Mt 11,18-19; 1 Cor 13,4-5; Gl 5,17; Rm 7,23; Mt 26,41; Mt 4,10; Sl 118,109; 2 Cor 7,10; Eclo 30,25; Tg 5,13; Ct 2,16; 1,12; Sl 118,82; Rm 8,35; Rm 14,8; Sl 118,103; Ct 1,1; Lm 3,25; Mt 7,17; Mt 17,4; Pr 25,16; Sl 41,4; Sl 118,71.67; Lc 1,53; Mt 25,29; Sl 50,14; Mt 26,39; Ct 4,16; Jó 1,21; Eclo 11,27; Ct 5,2.

## Emendas

Erros evidentes de Boulenger (ou da transcrição do Wikisource), conferidos em Annecy. A tradução segue Annecy:

1. **IV.1, «un peu plus malin qu'à l'ordinaire»** → Annecy, *plus matin*: «um pouco mais cedo que de costume».
2. **IV.1, «nous regardant ainsi de mauvais œil, Jamais nous ne pouvons»**: maiúscula espúria; Annecy, *jamais*.
3. **IV.3, «son malheureux dessein, Premièrement»**: vírgula por ponto. Ficou ponto.
4. **IV.4, «faire souffrir et combattre Tamant»** → Annecy, *l'amant*: «o amante».
5. **IV.11, «elle s'échauffera à la quête des moyens, comme si ce bien s'empressera et dépendait plus d'elle»** → Annecy: *elle s'empressera et s'eschauffera a la queste des moyens, comme si ce bien dependoit plus d'elle*. O verbo *s'empressera* saiu do lugar na transcrição. Traduzi pela lição de Annecy: «ela se agitará e se afogueará na busca dos meios, como se esse bem dependesse mais dela».
6. **IV.11, «Quand donc l'âme sent qu'elle a I quelque mal»**: o «I» é sobra de número de página. Retirado.
7. **IV.11, «car après es petits»** → Annecy, *après les petitz*: «depois dos pequenos». (Annecy tem *treuveroyent*, «achariam»; Boulenger, *trouveront*. Segui Boulenger: «acharão».)
8. **IV.12, «dont il voudrait que chacun fût comme lui, La mauvaise tristesse»**: vírgula por ponto (Annecy tem ponto e abre aí parágrafo novo; mantive a divisão de parágrafos de Boulenger).
9. **IV.12, «Dieu démon cœur ! ... le bien-aimé de ! mon âme !»** → Annecy, *Dieu de mon cœur ... le Bienaymé de mon ame*: «Deus do meu coração! ... o bem-amado da minha alma!». Por isso o parágrafo tem um «!» a menos que o francês.
10. **IV.13, 1, «aucune vraie dévotion, Saül poursuivant»**: vírgula por ponto. Ficou ponto.
11. **IV.13, 4, «Quand nous aurons de ces douleurs et consolations»** → Annecy, *de ces douceurs et consolations*: «dessas doçuras e consolações».
12. **IV.13, 4, «de dire pour ces douceurs : ce Oh ! que je suis bon ! »** → Annecy, sem o *ce*; é a aspa de abertura mal lida: «Oh! como sou bom!».
13. **IV.13, 4, «pour mous rendre doux»** → Annecy, *pour nous rendre doux*: «para nos tornar doces».
14. **IV.14, 3, «il nous inspire de nous remettra à nos exercices»** → Annecy, *nous remettre*: «inspira-nos que voltemos aos nossos exercícios».
15. **Hifenizações de fim de linha** que sobraram no texto («de- vant», «rap- portons», «quoi- qu'il»): lidas como palavra inteira.

**Aspas fechadas.** Em dois lugares Boulenger abre «, mas não fecha:
- IV.1, a fala dos amigos («Vous tomberez, diront-ils...»): fechei depois de «sem tantos mistérios», antes de «e mil outras ninharias assim», que é do autor;
- IV.12, a lista de jaculatórias («O Dieu de miséricorde !...»): fechei depois de «o bem-amado da minha alma!», antes de «e semelhantes» (como faz o autor em IV.12, «Qui me séparera de l'amour de mon Dieu ? » et semblables).

Annecy não tem aspas nesses trechos (imprime as falas sem aspas), por isso a decisão é minha; ver Dúvidas.

Diferenças de Annecy sem efeito na tradução: IV.3 *soutint* (Annecy) × *souffrit* (Boulenger), «sofreram»; IV.2 «Courage ! Philothée quand...» sem vírgula em Boulenger, traduzido «Coragem, Filoteia! Quando...».

## Remissões de página

Não há. As remissões internas do autor («la princesse de laquelle nous avons parlé», IV.6; «comme j'ai dit ci-dessus», IV.15) apontam para capítulos desta mesma parte e ficaram como estão.

## Dúvidas para quem coordena

1. **Aspas fechadas em IV.1 e IV.12.** Boulenger abre e não fecha; fechei onde termina a fala. Se a regra for não tocar nem nisso, basta tirar as duas aspas de fechamento (uma em cada parágrafo).
2. ***Mouchons* → «crias».** Os *mouchons* são as abelhas novas, ainda em formação, que o autor chama logo depois de *nymphes*. Usei «crias» (IV.2: «as pequenas crias das abelhas», «somos ainda pequenas crias na devoção»; IV.14, 5: «mais mel e menos crias»). Alternativas: «abelhinhas» (mas «abelhinhas» já traduz *avettes* em IV.13) ou «filhotes». **Proposta para o guia:** *mouchons* → crias; *avettes* → abelhinhas.
3. ***Geoffroy de Péronne* → «Godofredo de Péronne».** Forma portuguesa usual do nome (como Godofredo de Bulhão). Se a casa preferir manter o nome francês, é «Geoffroy» em quatro lugares de IV.15.
4. ***Douceur* (virtude) → «doçura».** Em IV.1 e IV.11 *douceur* é a virtude da mansidão. Mantive «doçura», que é o termo salesiano consagrado e liga com as *douceurs* (consolações) de IV.13. Se a Terceira parte (cap. VIII–IX, *De la douceur envers le prochain*) usar «mansidão», convém harmonizar.
5. ***Conducteur*** ficou «condutor» (do guia: *conducteur, guide → guia, condutor*); *directeur* → «diretor». Pareceu melhor reservar «guia» para o verbo *conduire* («àquele que guia a vossa alma»). Convém que o guia fixe uma só palavra para *conducteur*.
6. ***Recherche* (amorosa) → «corte»; *mugueter* → «galantear».** Proposta para o guia, se aparecer em outras partes (a Terceira parte, cap. XVII–XXI, trata das amizades e dos galanteios).
7. **Minúscula depois de «?» e «!»** (IV.1, IV.4, IV.13, IV.14, IV.15), mantida como no francês. Se a casa preferir a norma atual, é trocar a inicial em uns dez lugares.
