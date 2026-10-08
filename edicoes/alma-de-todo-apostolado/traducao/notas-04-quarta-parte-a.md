# Notas do tradutor: A alma de todo apostolado, Quarta parte, a) a c)

Arquivo: `traducao/04-quarta-parte-a.txt`. Texto-base: `original/04-quarta-parte-a.txt` (12e édition, 1927,
págs. 109–148 do livro). Conferido contra a imagem do scan, página por página:
`ferramentas/cache/alma/rev/126.png` a `165.png` (40 páginas).

Conferência por script: 186 blocos no original e 186 na tradução: cabeçalho, 6 títulos `##`, 59 notas
`¤ [n]` (nenhuma com parágrafo de continuação) e 120 parágrafos de prosa, os 120 do LEIAME. A marca
`[IV.1]` está no mesmo lugar. As chamadas `[1]` a `[59]` e as notas `¤ [1]` a `¤ [59]` são iguais e
estão nos mesmos blocos. Os seis títulos têm os mesmos números e letras («1.», «a)», «b)», «c)»).

Proporção de tamanho: nenhum parágrafo traduzido ficou abaixo de 0,8 do original. Abaixo disso só
aparecem o título «QUATRIÈME PARTIE» → «QUARTA PARTE» (0,79) e a nota 57 (0,76, «Ninguém dá o que não
tem»), ambos inteiros. Acima de 1,5 ficaram a nota 16, por causa do `[Trad.: …]`, e a nota 45 («S.
AUG.» → «Santo Agostinho.»).

Linhas `# ` do topo: copiadas; só o `# titulo:` foi traduzido («Quarta parte, capítulo único, a) a c)»,
como no exemplo do guia). Aspas: 34 aberturas no original e 34 na tradução (32 «» e 2 “” internas).

Mesóclise: o grep do CONVENCOES e a varredura em Python com a mesma regex terminada em
`(?![A-Za-zÀ-ÿ])` não acharam nada. Não há versos neste arquivo.

## Decisões gerais

- **Itálico do autor**, conferido nas 40 páginas do scan, como no Prelúdio e na Primeira parte. O
  latim do corpo e os títulos de obras ficaram em itálico. Foram acrescentadas todas as ênfases
  francesas visíveis na imagem:
  - IV.1:
    - *action profonde* e *durable*;
    - em são João da Cruz: *beaucoup plus utiles*, *par une seule œuvre*, *par mille autres* e a
      frase *un peu plus que rien, souvent absolument rien, ou même du mal*;
    - *Occupations maudites*.
  - a): *ainsi mon peuple recevra la plénitude de mes biens*; *La moisson est abondante, et rares
    les ouvriers!*; a citação inteira de Pio X (*Pour restaurer toutes choses…*); *la souffrance*.
  - b):
    - *le sel de la terre, la lumière du monde*;
    - o título « *Fabiola* ».
  - c):
    - abertura: a frase *Le surnaturel transpire ainsi aux yeux des fidèles…*; *Manifestation du*
      (seguida de DIVIN em versalete); *irradiation du surnaturel*; « *J'ai vu Dieu dans un homme* »;
      *accumulateur de vie surnaturelle*;
    - caridade e bondade: *deviner dans son semblable un amour brûlant, allumé aux réalités
      invisibles*; *Dieu-Amour*; « *diffusivus* »; as duas citações do padre Faber (*La bonté, c'est le
      débordement…* e *Partout la bonté…*);
    - humildade:
      - *condition que Jésus seul paraisse*; *Divin*; a fala de são Vicente de Paulo; *mais à Dieu
        seul*; *Transparent de Dieu*;
      - *science de la vie*, *science de la prière*; « *petit* » e *croisse* na citação de são Beda;
      - as palavras de Cristo (*Vous le savez… l'esclave de tous*); a frase de Bourdaloue;
      - *le Moi*, *Fin*, *Moyen*, *Prétexte*, *Société purement humaine*, *Société parfaite établie par
        Notre-Seigneur*;
    - firmeza e doçura: *Vie de Saint Bernard*; *Moi*; *Vous ne savez pas … de quel esprit vous
      êtes*;
    - mortificação:
      - a frase *Et tant qu'on n'a pas fait pénétrer … qu'effleurées*; *Passion rendue comme
        sensible*;
      - só a segunda metade de Mt 15,8 (*il ne m'honore que des lèvres, son cœur est loin de moi*);
      - *Si vous ne faites pénitence, vous périrez tous de même*; *un scandale*; *Bluff*;
      - *faisant resplendir à travers les peuples le mystère de la Croix*; *austérité de vie intime du
        prédicateur*.
  - Notas: *Cant. spirit.*, *Pastor*, *De Sp. Sancto*, *Du champ de bataille à la Trappe*, *Conf.
    spirit.*, *Traité de la vie spirituelle*, *Bréviaire*.

  Ficaram em redondo, porque estão em redondo no livro:
  - a máxima de são Boaventura;
  - as palavras de são João da Cruz fora dos trechos grifados;
  - santa Teresa, Leão XIII, a segunda citação de Pio X, são Basílio, Lacordaire, são Vicente Ferrer,
    são Francisco de Sales e santo Tomás.

  Como na Primeira parte, o versalete dentro de um trecho em itálico ficou em maiúsculas dentro do
  itálico (Bourdaloue: «_… se A HUMILDADE SE VAI, a autoridade se torna ONEROSA e INSUPORTÁVEL._»).
- **Versalete** (aqui em maiúsculas), mantido: UN PLUS GRAND BIEN → «UM BEM MAIOR»; DIVIN → «DIVINO»;
  os sete subtítulos de c) (PAR LA VIE INTÉRIEURE L'APOTRE RAYONNE DE FOI; IL RAYONNE D'ESPÉRANCE, DE
  CHARITÉ, DE BONTÉ, D'HUMILITÉ, DE FERMETÉ ET DE DOUCEUR, DE MORTIFICATION); em são Beda, ZÈLE
  PASSIONNÉ POUR L'HUMILITÉ, EN HUMILITÉ, ROYAUME PROMIS A L'HUMILITÉ; em Bourdaloue, L'HUMILITÉ S'EN VA,
  ONÉREUSE, INSUPPORTABLE. No livro, os subtítulos de c) estão em versalete com as iniciais maiores
  («Il rayonne d'Espérance»). O texto-fonte os dá todos em maiúsculas, e assim ficaram.
- **Tratamento.** O autor fala ao leitor por *vous* uma vez em c) (*Aussi voyez*) e em a)
  (*Hommes de zèle, écoutez le Maître*): «vede», «escutai». Nas falas citadas, o *vous* virou **vós**:
  - Cristo aos apóstolos;
  - são Vicente de Paulo aos seus padres: «Crede-me»;
  - são Vicente Ferrer: «Tende um coração de mãe…». O *vous* dele é de um só leitor, e por isso ficou
    «Se quereis ser útil», com o adjetivo no singular;
  - Leão XIII: «lembrai-vos»;
  - o padre de Nova York;
  - Pio X ao leigo («Meu Filho, … não aprovo a vossa linguagem»);
  - o pároco ao bispo.

  Maiúsculas de reverência seguidas palavra a palavra:
  - *Celui* → «Aquele», «Daquele»; *Lui* → «Ele» (com o *avec Lui* de «o trato com Ele»);
  - *qu'Il répande* → «para que Ele derrame»;
  - onde o autor põe minúscula (*il s'écrie*, *tel qu'il se définit*, *comme lui*), ficou minúscula.

  Também seguem o original:
  - *Œuvres*, *Vie intérieure* (nos títulos; no corpo, *vie intérieure* em minúscula, salvo «sem Vida
    interior» em c), como no original);
  - *Autorité*, *Supérieure(s)*, *Religieuses*, *Saints* (em boa parte de c)), *Apôtres*, *Religion*,
    *Christianisme*, *Economie de l'Evangile*, *Sacrements*, *Sacrifice*;
  - *le maître* em minúscula no fim do parágrafo de *Rogate ergo*, contra *le Maître* no começo do
    mesmo parágrafo.
- **Pontuação.** O espaço francês antes de «:», «;», «!», «?» e dentro das aspas foi retirado.
  Quatro frases interrogativas ou exclamativas terminam em ponto no impresso, e assim ficaram:
  - *Procédés arrogants … dans l'infécondité des œuvres.*;
  - *Quel malheur, quand … vraiment intérieures.*;
  - *Combien vivante est la parole … in cælis est.*;
  - a fala do calvinista, *Est-il possible qu'un évêque … de ma modeste demeure.*

  O guia manda seguir o original; ver Dúvidas.
- **Aspas.** As angulares do original. Na história de Pio X, a fala do pároco dentro da fala do Papa
  ficou entre “…”, e o mesmo se fez com o «petit» dentro da citação de são Beda. Os incisos dentro das
  aspas («Deus quis, escrevia Lacordaire, que…»; «O Salvador, diz ele, chama…») ficaram como no
  original. As citações sem aspas no livro ficaram sem aspas: são João da Cruz, são Boaventura, santa
  Teresa, Pio X, Leão XIII, são Basílio, padre Faber, são Vicente Ferrer, são Vicente de Paulo,
  Bourdaloue e santo Tomás.
- **Latim.**
  - No corpo, todo o latim ficou em itálico e sem tradução, como o autor o deixa; as traduções vêm nas
    notas dele, traduzidas do francês.
  - Ficaram sem tradução em parte alguma, como no original, as frases latinas curtas do corpo:
    *Solitudinem cordis circumferens ubique solus erat*, *Verbum docens*, *oportet illas adducere*,
    *Pusillus grex*, *Deo et paci militantibus*, *Inimicos crucis Christi* (traduzida pelo próprio
    autor no mesmo parágrafo), *lux mundi*.
  - A única nota inteiramente em latim é a 16 (são Gregório, *Regra pastoral*). Ganhou `[Trad.: Pois
    quem, pela necessidade do seu posto, é obrigado a dizer as coisas mais altas, por essa mesma
    necessidade é compelido a mostrá-las.]`.
- **Escritura em francês.** Traduzida do francês do autor (notas 1, 3, 4, 5, 8, 9, 11, 12, 14, 15,
  17–25, 30, 31, 33, 35, 37, 39, 42–44, 49–51, 55–59, e as citações francesas do corpo).
  - A nota 39 traduz *In bonitate et alacritate animæ suæ placuit* por «Il a plu à cause de sa foi et
    de sa mansuétude»: não bate com o latim, mas foi traduzida como está («Agradou por causa da sua fé e
    da sua mansidão»).
  - Referências no formato do impresso: «Joan.», «Matth.», «Luc», «Act.», «Rom.», «Tit.», «I Tim.»,
    «II Tim.», «Philipp.», «Phil.», «I Cor.», «II Cor.», «Coloss.», «Gal.», «Eccl.», «Is.», «Ezech.»,
    «I Petr.».
  - Só as duas abreviaturas que são francesas e não latinas foram trocadas: *Jér.* → «Jer.» (nota 3)
    e *Sag.* → «Sab.» (nota 38). Como os títulos dos livros bíblicos em francês, *Sag.* não seria
    entendido; ver Dúvidas.
  - *8 et 11* → «8 e 11».
  - Os erros de referência do impresso ficaram, segundo o LEIAME. Por exemplo:
    - nota 13, «Matth., V, 3» (é V, 13-14);
    - nota 9, «Matth., X, 7» para *Euntes docete* (o *docete* é de Mt 28,19);
    - nota 49, «Gal., II, 19» (na Vulgata, II, 19; nas Bíblias modernas, 2,19-20).
- **Notas bibliográficas.** Abreviaturas de obras como no impresso (*Cant. spirit.*, str.; *De Sp.
  Sancto*, c., n.º; *Pastor*, 2 p. c.; *Conf. spirit.*; Hom., liv., cap.). As de pessoas foram
  desdobradas como manda o guia: *S. GRÉG.* → «são Gregório»; *S. AUG.* → «Santo Agostinho» (sozinha
  na nota, por isso com maiúscula); *V. Bède* → «venerável Beda»; *S. Luc* → «são Lucas». *Encycl. de
  S. S.* → «Encícl. de S. S.» (Sua Santidade, abreviatura também portuguesa). *aux év. d'Italie* (nota
  27) → «aos bispos da Itália», como na nota 10. *IIe p.* → «IIª p.».

## Termos

| francês | português | onde / observação |
|---|---|---|
| *fécondité, fécond* | fecundidade, fecundo | passim (guia) |
| *ex opere operato / operantis* | em latim, itálico | IV.1 |
| *orphelinat de jeunes filles* | orfanato de meninas | IV.1 |
| *sérieusement placées* | colocadas em lugares sérios | IV.1: as órfãs, colocadas em emprego ao sair |
| *aumônier* | capelão | IV.1 |
| *Piété … d'entraînement* | piedade … de arrastamento | IV.1: a que vem do embalo dos outros |
| *mièvrerie* | pieguice | IV.1 |
| « *Pieuseté* » | «Beatice» | IV.1: neologismo pejorativo do autor (de *pieux*), entre aspas no original; ver Passagens |
| *des maniérées* | umas afetadas | IV.1 |
| *Pensionnats, Externats* | Internatos, Externatos | IV.1 |
| *Patronages* | Patronatos | guia |
| *Occupations maudites* | _Ocupações malditas_ | remete à 3ª parte (são Bernardo) |
| *source d'eau vive … fontaine mystérieuse* | nascente de água viva … fonte misteriosa | IV.1, para não repetir «fonte» |
| *prière / oraison* | oração; prece | «oração» para os dois, como na Primeira parte; «prece» onde os dois vêm juntos (*La prière, l'esprit d'oraison* → «A prece, o espírito de oração»; *la prière de l'homme d'oraison* → «à prece do homem de oração») |
| *homme d'oraison* | homem de oração | a), c) |
| *infusion* | infusão | a): o jogo do padre Monsabré (chá / infusão da graça) passa inteiro |
| *chaire* | púlpito | a), c) |
| *effluves* | eflúvios | como no Prelúdio |
| *corédempteur* | corredentor | a) |
| *rayonnement, rayonner, irradiation* | irradiação, irradiar | guia; *IL RAYONNE DE FOI* → «ELE IRRADIA FÉ» (sem preposição, que em português não se usa) |
| *porte-Dieu* | portador de Deus | c), por analogia com *porte-Christ* do guia |
| *Transparent de Dieu* | _Transparente de Deus_ | c) |
| *isoloir* | banquinho isolante | c): o tamborete de vidro das experiências de eletricidade estática |
| *commotion* (elétrica) | descarga | c), as duas vezes, para guardar o paralelo da comparação |
| *accumulateur* | acumulador | c) |
| *convers trappiste*; *frère convers* | converso trapista; irmão converso | c); *F. Gabriel* → «O irmão Gabriel» |
| *sous-hôtelier* | ajudante do hospedeiro | c): o hospedeiro é o monge encarregado dos hóspedes |
| *la Trappe* | a Trapa | nota 34; *venir à la Trappe* → «vir para a Trapa» (o autor escreve de Sept-Fons, que é trapista) |
| *convertisseur* | convertedor | c) |
| *Débonnaireté outrée* | bonomia exagerada | c) |
| *le Moi* | _o Eu_ | c), duas vezes |
| « *snobisme* » | «esnobismo» | c) |
| *Bluff* | _Bluff_ | c): palavra inglesa, em itálico e com maiúscula no livro |
| Christ « *au muguet* » | Cristo «de lírio-do-vale» | c); ver Passagens |
| *confrères* | confrades | c), como na Primeira parte |
| *verte semonce* | severa reprimenda | c) |
| *Petite Sœur des Pauvres / de l'Assomption; Fille de la Charité* | Irmãzinha dos Pobres / da Assunção; Filha da Caridade | c) |
| *Commun des Confesseurs Pontifes* | Comum dos Confessores Pontífices | c) |
| *pléiade(s)* | plêiade(s) | c) |

Nomes: são João da Cruz; Bossuet; são Bernardo; o padre Lacordaire; o padre Monsabré; Notre-Dame (a
catedral de Paris: fica em francês, porque é nome de lugar; o guia dá «Nossa Senhora» para a Virgem);
são Boaventura; Pio X; santo Agostinho; o padre Faber, «o célebre oratoriano»; são Gregório; o cardeal
Wiseman, *Fabiola* (título na língua original), «a filha de Fábio» (*Fabius*, como nas traduções
portuguesas do romance); o padre Passerat; o jovem Desurmont; a Congregação do Santíssimo Redentor;
Tito e Timóteo; Leão XIII; santa Teresa; são Basílio; **santo Antão** (*saint Antoine*, o eremita do
Egito, na forma portuguesa usual); são Bento; são Vicente Ferrer; santo Inácio; Xavier; João Batista; o
bem-aventurado Vianney; Ars; o irmão Gabriel; o general de Miribel; Gravelotte; são Francisco de Sales;
Lacordaire; são Vicente de Paulo; são Beda, «venerável Beda»
na nota; Bourdaloue; santo Tomás; Abelardo; o padre Ratisbonne, *Vie de Saint Bernard* (título como o
autor o dá); Claraval; os israelitas; o Chablais; o bispo de Genebra; o duque de Saboia; Zaqueu;
Herodes; Samaria; o pobrezinho de Assis; são Paulo; Nova York; Estados Unidos; Getsêmani; Pretório;
Bento XV; o padre de Ravignan.

## Passagens difíceis e leitura adotada

- **IV.1, « *Pieuseté* ».** Palavra forjada pelo autor, entre aspas, para a piedade de exterioridade e
  afetação que ele descreve. Ficou «Beatice», que em português é justamente a devoção afetada,
  exterior. «Carolice» seria igualmente boa e mais brasileira, mas soa mais coloquial.
- **IV.1, *que traduisent la joie sereine, l'entrain…*.** Os sujeitos de *traduisent* são *la joie, l'entrain…*
  (as mudanças que a alegria etc. traduzem). Para não inverter a frase, ficou «e que se exprimem na
  alegria serena, no ânimo…», que diz o mesmo.
- **IV.1, *Que Dieu nous préserve d'une âme comme celle-là*.** São João da Cruz fala da alma do ativo
  orgulhoso; «Deus nos preserve de uma alma assim».
- **IV.1, *ou même du mal*.** «Ou até o mal» («faz-se … o mal»), para não ler «fazer-se mal» como «ser
  malfeito».
- **a), *Les secrets d'un apostolat fécond se puisent*.** «Haurir» é defectivo («se haurem» não se usa);
  ficou «vão-se buscar».
- **a), *Præcessit Christus in capite : Le Christ a souffert, mais comme chef, Sequitur in corpore :
  Maintenant…*.** Mantida a vírgula do autor entre as duas glosas; *chef* = «cabeça» (do Corpo
  místico), também na nota 12 (*dans le chef seulement* → «só na cabeça»).
- **b), *Ab immundo quid mundabitur?* (nota 14).** O francês *que peut-il sortir de pur?* ficou «que
  coisa pura pode sair?» («que pode sair de puro» soava galicismo).
- **b), *l'Hôte trop souvent délaissé du Tabernacle*.** «O Hóspede do Tabernáculo, demasiadas vezes
  abandonado»: em português o adjunto no meio («o Hóspede demasiadas vezes abandonado do Tabernáculo»)
  ficava ambíguo.
- **b), *Prêche un homme de Dieu, il accourt en foule*.** Condicional sem conjunção, do francês; ficou
  «Se prega um homem de Deus, ele acorre em multidão» (o sujeito de *accourt* é o povo).
- **b), presente histórico** (*le jeune Desurmont se décide … qu'il doit illustrer*): mantido, «se
  decide … que há de ilustrar».
- **b), *faisaient dire à Notre-Seigneur*.** O sujeito é *cette assurance et ce zèle*: a mesma segurança
  que fazia Cristo dizer *Quis ex vobis arguet me de peccato?*. Literal.
- **c), a comparação elétrica.** *commotion* → «descarga» nas duas ocorrências, para que a imagem da
  máquina passe ao homem interior; «comoção» seria o decalque, mas não se entende hoje como choque
  elétrico.
- **c), *Jamais on n'a autant prêché, discuté, composé de savants traités*.** O francês junta dois
  verbos intransitivos e um transitivo com o mesmo *autant*. Em português: «Nunca se pregou e se
  discutiu tanto, nunca se compuseram tantos sábios tratados de apologética como nos nossos dias».
- **c), *la réflexion de la lumière divine*.** Sentido físico: «o reflexo da luz divina».
- **c), *Un zèle qui n'est pas charitable … vient d'une charité qui n'est pas véritable*.** Jogo de rima
  de são Francisco de Sales. Para guardá-lo, ficou «Um zelo que não tem caridade … vem de uma caridade
  que não tem verdade», com a rima *caridade / verdade*. «Não tem verdade» diz «não é verdadeira», com
  pequena mudança de construção.
- **c), *L'ardent amour pour Jésus et la vraie direction pour les âmes donne…*.** *direction pour les
  âmes* não é a direção espiritual técnica, mas a reta disposição para com elas; ficou «a verdadeira
  orientação para com as almas». O verbo, singular no francês, foi para o plural («dão»).
- **c), a história de Pio X.**
  - *Monseigneur* (o pároco ao bispo) → «Senhor Bispo». «Monsenhor», no Brasil, é título de um
    prelado menor, e «Excelência» pediria a terceira pessoa. «Senhor Bispo» casa com o *vós* da fala.
  - *Grand émoi chez ses confrères qui se plaignent* (presente histórico no meio do passado): mantido.
- **c), *Procédés arrogants, airs de suffisance, n'entrent-ils pas souvent pour une part…*.** «Não entram
  eles muitas vezes com a sua parte na infecundidade das obras», com o ponto final do impresso.
- **c), *Débonnaireté outrée, mais le plus souvent tendance au despotisme*.** «Bonomia exagerada, mas,
  as mais das vezes, tendência ao despotismo»: os dois excessos do parágrafo seguinte (pusilanimidade e
  orgulho).
- **c), Bourdaloue, *si L'HUMILITÉ s'EN VA*.** No texto-fonte, *s'EN VA* com *s* minúsculo, resto do
  versalete. Ficou «se A HUMILDADE SE VAI».
- **c), *l'évêque de Genève*.** No tempo da missão do Chablais (1594), Francisco de Sales ainda não era
  bispo; o autor o chama pelo título que teve depois. Mantido.
- **c), *la guerre qui sévit en ce moment*.** A guerra de 1914–1918 (o LEIAME a cita como sinal das
  ampliações). Literal: «a guerra que se trava neste momento».
- **c), *L'industriel qui occupe cet employé*.** «O industrial de quem esse homem é empregado», para não
  repetir «emprega esse empregado».
- **c), *que par d'interminables et vives discussions*.** «do que por meio de intermináveis e vivas
  discussões».
- **c), *en vain l'apôtre immortifié emprunterait-il à Bossuet ses grands accents sur le Calvaire*.**
  «Em vão o apóstolo imortificado pediria emprestados a Bossuet os seus grandes acentos».
- **c), *c'est trop peu des arguments communs, voire même des aperçus grandioses*.** «São muito pouco os
  argumentos comuns, e até as perspectivas grandiosas».
- **c), un Christ « *au muguet* ».** O *muguet* é o lírio-do-vale, flor de perfume doce. No francês
  antigo, *muguet* era também o janota perfumado. O autor fala de um Cristo adocicado, de enfeite,
  oposto ao do Getsêmani e do Calvário. Ficou «um Cristo “de lírio-do-vale”», entre aspas como no
  original, com perda do segundo sentido.
- **c), nota 59.** *qui fît une cloison* (lat. *sepem*) → «que levantasse uma cerca».

## Remissões de página

Nenhuma com número de página. A única remissão interna é *l'expression Occupations maudites citée plus
haut de saint Bernard* (IV.1), que remete a III.1 (3ª parte). Ficou «citada acima», sem número, como no
original.

## Emendas

Nenhuma. O texto-base confere com a imagem nas 40 páginas, salvo o itálico, que foi marcado.

## Dúvidas para quem coordena

1. **Abreviaturas bíblicas francesas.** Troquei *Jér.* por «Jer.» e *Sag.* por «Sab.» e deixei as
   latinas como no impresso (*Matth.*, *Joan.*, *Eccl.* etc.). Se se preferir guardar tudo como no
   livro, basta desfazer as duas.
2. **«Notre-Dame»** (a catedral de Paris, onde pregava Monsabré): ficou em francês, por ser nome de
   lugar, apesar da tabela do guia («Notre-Dame» → «Nossa Senhora», que vale para a Virgem). Proposta
   para o guia: registrar a distinção.
3. **Perguntas e exclamações terminadas em ponto** no impresso (ver Decisões gerais, Pontuação).
   Mantive o ponto, como o guia manda. A Primeira parte, em I.5, pôs «?» num caso igual. Convém decidir
   uma regra única para a obra.
4. **«Beatice»** para « *Pieuseté* » e **«de lírio-do-vale»** para « *au muguet* ». Os dois pedem
   decisão de estilo; as alternativas são «carolice» e «açucarado».
5. **Proposta para o guia (não alterado):**
   - *rayonner de* → «irradiar» + objeto direto («ELE IRRADIA FÉ»);
   - *porte-Dieu* → «portador de Deus»;
   - *saint Antoine* (o eremita) → «santo Antão»;
   - *Monseigneur* em vocativo → «Senhor Bispo»;
   - *prière / oraison* juntos → «prece / oração».
