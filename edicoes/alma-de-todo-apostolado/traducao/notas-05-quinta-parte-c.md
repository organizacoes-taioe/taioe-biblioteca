# Notas do tradutor: A alma de todo apostolado, Quinta parte, capítulo 3, IV e V

Arquivo: `traducao/05-quinta-parte-c.txt`. Texto-base: `original/05-quinta-parte-c.txt` (12e édition, 1927,
págs. 245–267 do livro: a Vida litúrgica, seções IV, «Avantages», e V, «Pratique»). Conferido contra o
original, parágrafo a parágrafo, e contra a imagem do scan, página a página
(`ferramentas/cache/alma/rev/262.png` a `284.png`; para as notas em corpo pequeno, `img/i268.png`,
`i278.png` e `i280.png`, de resolução maior).

Conferência por script: 143 blocos no original e 143 na tradução. São 1 cabeçalho, 8 títulos `##`,
4 separações `## * * *` (copiadas iguais), 26 notas `¤ [n]`, 5 parágrafos de continuação de nota `¤`
(1 na nota 14 e 4 na nota 22) e 99 parágrafos de prosa, como no LEIAME (99 parágrafos, 12 títulos
contando as separações, 26 notas). O arquivo não tem marca `[X.n]`, porque continua o capítulo V.3
(LEIAME, «Convenção das marcas»); os títulos `##` servem de âncora, e os oito foram traduzidos com o
prefixo, os números romanos, as letras e o ponto final. As 26 chamadas `[n]` e as 26 notas `¤ [n]`
estão iguais e nos mesmos blocos. Razão de tamanho tradução/original (sem o `[Trad.: …]`): todos os
blocos entre 0,8 e 1,4, salvo o título «c) Cumprimento da função litúrgica.» (0,79, só pela troca de
*Accomplissement* por «Cumprimento»). As linhas `# ` do topo foram copiadas, e só o `# titulo:` foi
traduzido («Quinta parte, capítulo 3, IV e V»). Varreduras de mesóclise: o grep do CONVENCOES e a
varredura em Python com a mesma regex terminada em `(?![A-Za-zÀ-ÿ])` não acharam nada. Três futuros
das «resoluções» que pediam ênclise foram desfeitos de propósito: *je m'appliquerai* → «eu me
aplicarei»; *je m'astreindrai* → «eu me obrigarei»; *je me rappellerai* → «eu me lembrarei»; e *je vous
ferai de moi-même* → «eu vos farei de mim mesmo».

## Decisões gerais

- **Itálico do autor**, conferido nas 23 páginas do scan, como no Prelúdio e na Primeira parte. É
  muito frequente aqui (perto de 150 trechos). Exemplos: a frase de abertura *Quelle difficulté
  j'éprouve … surnaturel!*; *seule*; *faute de vigilance ou de fidélité*; *Ecole de Présence de Dieu*;
  *Dieu en tout, toujours, partout*; *Jamais je ne voudrais scandaliser par ce qui doit édifier*; *A
  tout prix, je veux que cette récitation soit une vraie prière du cœur*; a citação de são Francisco
  de Sales *La précipitation est la mort de la dévotion*; na nota 22, *enlevait* e *même de croire*;
  na nota 24, *ne sait pas ce qu'elle dit* e *du prêtre qui bâcle sa messe*. Quando o itálico cai
  numa palavra que o português desloca, ele acompanha o sentido: *qui seule peut rendre* → «que _só_
  ela pode tornar»; *la première part aille d'abord* → «a _primeira parte_ vá _antes de tudo_»; *une
  demi-heure à ma* **Messe** → «_meia hora à minha_ **Missa**».
- **Negrito.** Esta parte do livro usa também o negrito, o que não acontecia nos arquivos já
  traduzidos. Há dois usos:
  - os títulos corridos, no começo do parágrafo: *Humilité parfaite.*, *Charité universelle.*,
    *Esprit de sacrifice.*, e os três advérbios latinos da oração *Aperi*, *Dignè.*, *Attentè.*,
    *Devotè.*;
  - palavras de ênfase forte no meio da frase: *Ecole de la Prière*, *incorporent*, *hostie*,
    *fondue*, *nostalgie du Ciel*, *Esprit de foi*, *sans-gêne*, *Rubriques*, *Psaumes*, *symboles*,
    *une âme de petit enfant*, *apostolat*, *Messe*, *prétextes*, *regard*.

  Marquei-os com `**…**`, que o `js/app.js` já converte em `<strong>` («_itálico_ e **negrito**»).
  Os três advérbios latinos ficaram em negrito e itálico: `**_Dignè_.**`. Ver Dúvidas, 1.
- **Versalete** (aqui em maiúsculas), mantido: na nota 22, *SCANDALE* → «ESCÂNDALO» e *VÉCUE* →
  «VIVIDA». Os nomes de autor em versalete das notas (*S. THOM.*, *P. OLIVAINT*, *Petr. BLESENS.*)
  foram por extenso, em caixa normal, como na Primeira parte.
- **Tratamento.**
  - Jesus, Deus, o «bom Mestre»: **vós**, em minúscula, como no original; com maiúscula só onde o
    autor a põe: *C'est Vous-même* → «Sois Vós mesmo»; *comme à Vous-même … m'unir à Vous* → «como a
    Vós mesmo … unir-me a Vós»; *Identifié à Vous* → «Identificado a Vós»; *uni au Vôtre* → «unido ao
    Vosso»; *me revêtir de Vous* → «revestir-me de Vós»; *ce qui en Vous dominait tout* → «o que em
    Vós tudo dominava».
  - A Igreja (*A votre école, sainte Eglise … vous me communiquez*; *Sainte Eglise du Rédempteur*), a
    Liturgia (*Divine Liturgie … je vous suis redevable*; *Sainte Liturgie, quel baume vous
    apporterez*) e a Vida litúrgica personificada (*Chère Vie liturgique, accroissez*): também
    **vós**, porque o autor lhes fala por *vous*: «aumentai», «trareis».
  - A Igreja à alma (*Chère âme, regarde*) e o autor à própria alma (*ô mon âme, tu forgeras*; *Pour
    toi, mon âme … tu dois*): **tu**.
  - O *nous* de modéstia da nota 22 (*Etant étudiant … nous eûmes*) ficou no plural com o particípio
    no singular («Sendo estudante…, e subtraído…, tivemos»), como *nous-même* na Primeira parte.
- **Maiúsculas de reverência**, palavra a palavra: *Celui qui est l'Adoration* → «Daquele que é a
  Adoração»; *vers Lui* → «Nele»; *avec Lui* → «com Ele»; *qu'Elle ne me voie* (Maria) → «enquanto Ela
  não me vir»; *avec Lequel* (nota 22) → «com o Qual»; *Celui qui est la Joie des Elus* → «Daquele que
  é a _Alegria dos Eleitos_». Onde o autor escreve *il*, *son*, *ses* em minúscula (*il est aussi mon
  Père*, *son cœur*, *dont il est la vie*), ficou minúscula. As maiúsculas de substantivos também
  seguem o original: *Vie liturgique* / *vie intérieure* (as duas grafias), *Oraison* / *oraison*,
  *Foi* / *foi*, *vertu de Religion* / *vertu de religion*, *Rubriques* / *rubriques*, *Fonctions*,
  *Cycle*, *Sacramental*, *Apostolat*, *Ministre de Dieu*.
- **Latim.** No corpo, todo em itálico e sem tradução, como o autor deixa (*os, lingua, mens, sensus,
  vigor*; *Obediente Domino voci hominis*; *inter vestibulum et altare*; *Imitamini quod tractatis*;
  *Scalpri salubris…*; *Agnoscite quod agitis*; *Deus in adjutorium*; *Introibo*; *Omnipotens et
  misericors Deus…*; *dignè, attentè, devotè*; *Aperi*; *Abneget semetipsum*; *Sitio*, que o guia
  manda deixar em latim). Onde o próprio autor dá a tradução na nota (19, 20, 23, 25, 26), traduzi a
  nota. Nas notas inteiramente em latim e sem tradução do autor, foi acrescentado `[Trad.: …]`: notas
  2, 3, 4, 6, 12, 13, 14 (os dois parágrafos) e 18. As notas 5, 7, 8, 9, 10, 11, 15, 16, 17 e 21 só
  dão a referência e ficaram sem `[Trad.]`.
- **Escritura em francês** (notas 19, 20, 25, 26): traduzida do francês do autor. A nota 19 (*préparez
  votre âme*) ficou «preparai a vossa alma», e a 20 (*Je vous chanterai*), «Eu vos cantarei», com o
  *vous* do francês.
- **Referências** no formato do impresso: «Hebr.», «Joan.», «Philip.» e «Philipp.» (as duas grafias do
  livro), «Luc», «Coloss.», «Joel», «Josué», «Eccli.», «Ps.», «Jér.», «Matth.»; *lib.*, *cap.*, *liv.*,
  *c.* como estão. Abreviaturas de autores por extenso (guia, § 6): *S. Aug.* → «santo Agostinho»;
  *S. Greg.* → «são Gregório»; *S. Thom.* → «santo Tomás»; *Petr. Blesens.* → «Pedro de Blois»; *P.
  Olivaint* → «padre Olivaint»; *Règle de S. Benoît* → «Regra de são Bento». Títulos de obras em
  itálico, como no livro: _De Civit. Dei_, _Epist._, _Dialogor._, e _in I Cor._ (o comentário de santo
  Tomás à primeira carta aos Coríntios).
- **Pontuação.** O espaço francês antes de «:», «;», «!» e «?» foi retirado; as aspas angulares, sem
  os espaços internos. Duas frases interrogativas que o livro fecha com ponto receberam «?», como se
  fez na Primeira parte: *n'est-ce pas là, ô mon Sauveur, le but … l'Esprit de sacrifice.* e *Serait-il
  possible que toutes ces fêtes … gage de prédestination.* As exclamativas fechadas com ponto
  (*comme il m'est facile…*; *Quelles armes tu forgeras…*; *Sainte Liturgie, quel baume…*) ficaram
  com ponto, como no impresso. Em *Qu'importe que je n'éprouve aucun attrait naturel pour ce labeur, il
  me suffit…* a vírgula virou ponto de interrogação, porque em português a pergunta pede fecho.

## Termos

| francês | português | onde / observação |
|---|---|---|
| *Vie liturgique*; *esprit liturgique*; *âmes liturgiques* | Vida litúrgica; espírito litúrgico; almas litúrgicas | passim (guia) |
| *Oraison* (mental) / *prière* | Oração / oração | o português tem uma palavra só para as duas; *L'Oraison et la Vie liturgique sont deux sœurs* → «A Oração e a Vida litúrgica»; *Ecole de la Prière* → «Escola da Oração»; *la prière Aperi* → «a oração _Aperi_» |
| *collectes*; *oraison* (da missa) | coletas; oração | IV a), IV c) |
| *office*; *Bréviaire*; *Missel, Rituel* | ofício; Breviário; Missal, Ritual | guia |
| *fonctions liturgiques*; *fonction* | funções litúrgicas; função | guia; *les diverses « fonctions »* → «as diversas «funções»» |
| *Rubriques*; *Sacramentaux*; *grand Sacramental* | Rubricas; Sacramentais; grande Sacramental | |
| *vertu de Religion* | virtude de Religião | IV a), com a maiúscula do original |
| *mise en acte* | o pôr em ato | IV a) |
| *amour de complaisance, de bienveillance* | amor de complacência, de benevolência | termos clássicos da teologia do amor |
| *Cycle des fêtes*; *Cycle liturgique* | Ciclo das festas; Ciclo litúrgico | |
| *leçons* (do ofício) | lições | IV a); *par ces leçons l'Eglise me crie* → «por essas lições» |
| *Emmanuel* | _Emanuel_ | grifado no livro |
| *naturalisme qui tend à m'enliser* | naturalismo que tende a atolar-me | *enliser*: afundar na areia movediça |
| *Eglise militante et souffrante* | Igreja militante e padecente | termo usual em português |
| *corédempteurs* | corredentores | IV b) |
| *Prêtre avec vous* (o padre unido a Cristo Sacerdote) | Sacerdote convosco | o guia dá *prêtre* → padre; aqui, com maiúscula e dito de Cristo e do padre que se une a ele, «Sacerdote» |
| *prêtre*, *prêtres* (o clero) | padre, padres | guia; *vous obéissez à vos prêtres* → «obedeceis aos vossos padres» |
| *curé* (nota 22) | pároco | |
| *honoraires* (de missa) | espórtulas | V a); o termo eclesiástico brasileiro para o estipêndio da missa |
| *corvée* | tarefa penosa | V a); «corveia» é arcaico |
| *sans-gêne* | sem-cerimônia | V a), V c), nota 22 |
| *crainte révérentielle* | temor reverencial | V b), nota 22 |
| *ingénuité*; *naïf*, *naïve*; *ingénument* | candura; ingênuo, ingênua; com candura | V b); para não dizer «ingenuidade ingênua» (*ingénuité naïve* → «candura ingênua») |
| *langage aussi naïf que grandiose* | linguagem tão singela quanto grandiosa | V a); «ingênua» soaria pejorativo ao lado de «grandiosa» |
| *âme de petit enfant*; *âme d'enfant* | alma de criancinha; alma de criança | V b) |
| *rajeunissement d'âme* | rejuvenescimento de alma | V b) |
| *tenue*; *maintien* | compostura; porte | V c), nota 22 |
| *butiner* | libar | V c); a imagem da abelha continua no parágrafo seguinte («o mel da devoção numa outra flor») |
| *pourvoyeuse* | provedora | V c) |
| *posément*; *très posément* | pausadamente; muito pausadamente | V b), V c) |
| *Tantôt … tantôt*; *D'autres fois* | Umas vezes … Outras vezes; Em outras ocasiões | V c); «ora … ora» confundiria com a conjunção «ora» no começo do parágrafo |
| *enlevait sa messe* (nota 22); *bâcle sa messe* (nota 24) | despachava a sua missa; despacha a sua missa | a mesma ideia de pressa e descaso |
| *diversion reposante* | pausa repousante | V, fim; «diversão» em português é divertimento, e «distração» chocaria com as «distrações» de V c) |
| *semer les gerbes* | semear os feixes | V, fim; a imagem do autor (semear feixes) ficou como está |
| *Jean le bien-aimé* | João, o bem-amado | IV c) |
| *la Sainte Vierge*; *la très sainte Trinité* | a Santíssima Virgem; a santíssima Trindade | IV c); o guia dá «a Santíssima Virgem»; *très sainte* em minúscula, como no livro |
| *le Bienheureux Père Perboyre* | o bem-aventurado padre Perboyre | V; são João Gabriel Perboyre, lazarista, beatificado em 1889 (o guia: *B.* → bem-aventurado, *P.* → padre) |
| *Pontifical romain*; *Canon de la Messe*; *Hymne de la Dédicace* | Pontifical romano; Cânon da Missa; Hino da Dedicação | notas 9, 11, 15 |
| *Oraison du 12e Dim. après la Pent.* | Oração do 12º dom. depois de Pent. | nota 21, com as abreviaturas do livro |

Nomes: são Paulo, santo Tomás, são Gregório, são Francisco de Sales, são Bento, santo Agostinho,
Pedro de Blois, o padre Olivaint, o bem-aventurado padre Perboyre, a Rainha dos Anjos.

## Passagens difíceis e leitura adotada

- **IV a), *Ecole de Présence de Dieu que la Liturgie*.** Construção exclamativa francesa («que escola
  é a Liturgia»): «_Escola de Presença de Deus_ é a Liturgia, e de Presença do nosso Deus tal como o
  manifestou a Encarnação!».
- **IV a), *Croire que Jésus vit en moi … quel levier de vie surnaturelle me donne l'oraison*.** O
  infinitivo grifado abre a frase como tema; a vírgula do francês virou dois-pontos: «_Crer que Jesus
  vive em mim e que quer agir em mim, se eu não lhe puser obstáculo_: que alavanca…». *y agir* → «agir
  em mim».
- **IV a), *combien combat spirituel, vertu, épreuve perdront*.** Mantida a enumeração sem artigos, que
  é do estilo do autor.
- **IV a), *garder l'âme dans la direction de ses actions vers Dieu*.** «Manter a alma na orientação
  das suas ações para Deus».
- **IV b), *la présomption, la suffisance*.** Aqui as duas palavras vêm juntas, e por isso não podiam
  dar ambas «presunção», como na Primeira parte (ver as Dúvidas daquele arquivo): ficou «a presunção,
  a suficiência», com *suffisance* no sentido de quem se basta a si mesmo. Ver Dúvidas, 3.
- **IV b), *faire en tout plaisir à votre Père*.** «De agradar em tudo ao vosso Pai» (eco de Jo 8,29,
  citado na nota 3).
- **IV b), *obéissant jusqu'à la mort et jusqu'à la mort de la Croix*.** O autor repete *jusqu'à*;
  ficou «obediente até a morte e até a morte da Cruz», sem passar para a forma da nota latina («e morte
  de cruz»), que vai no `[Trad.]` da nota 4.
- **IV b), *assouplir mon jugement et ma volonté*.** «Tornar flexíveis o meu juízo e a minha
  vontade».
- **IV b), *Mais vous entendez que la première part aille d'abord à l'ensemble des âmes dont vous avez
  la sollicitude*.** *entendre* = «querer»; «das almas confiadas à vossa solicitude».
- **IV b), *Je vous rendrai donc hostie pour hostie*.** *rendre* = dar em troca: «Eu vos retribuirei,
  pois, _hóstia por hóstia_».
- **IV b), *compléter pour votre Corps qui est l'Eglise ce qui manque à votre Passion*.** Paráfrase de
  Cl 1,24 (nota 12): «completar, em favor do vosso Corpo, que é a Igreja, o que falta à vossa Paixão».
- **IV b), nota 13.** O latim de santo Agostinho, tal como o autor o cita, traz *qui etiam obtulit in
  Passione*, sem o *se ipsum* do texto da _Cidade de Deus_. O latim ficou como no livro; o `[Trad.]`
  diz «que também se ofereceu», que é o sentido.
- **IV b), nota 14.** *Tunc ergo verè pro nobis Hostia erit Deo*: o sujeito subentendido é a Hóstia
  do altar: «ela será verdadeiramente hóstia por nós diante de Deus».
- **IV c), *une Mère toute bonne et toute-puissante*.** «Uma Mãe toda bondosa e toda-poderosa» (a
  «onipotência suplicante» de Maria).
- **V a), *Ce mot résume toute méthode*.** «Esta palavra resume todo método» (qualquer método, não «o
  método todo»).
- **V a), *ils se retrouvent dans un grand nombre des compositions prophétiques*.** O autor retoma o
  sujeito com *ils*; guardei a retomada («essa palavra íntima, esses _sentimentos_ …, eles se
  encontram…»), como a Primeira parte guarda as deslocações do autor.
- **V b), *Lorsque tu parvins à l'âge de raison, tu acceptais … tout ce que ma mère te disait*.** O
  autor fala à própria alma e lembra a sua mãe; ficou literal: «tudo o que minha mãe te dizia».
- **V b), *alors même qu'obscurité et sécheresse seraient son lot*.** O possessivo remete à alma (ou à
  vontade, no fim da frase anterior); «o seu quinhão» guarda a mesma ambiguidade.
- **V c), *Ma volonté a jeté mon cœur et le maintient devant la Majesté de Dieu*.** O complemento de
  lugar serve aos dois verbos: «A minha vontade lançou o meu coração e o mantém diante da Majestade de
  Deus».
- **V c), *paralyse le grand Sacramental qu'est la Liturgie, et l'empêche d'entretenir*.** O *l'*
  retoma *le grand Sacramental*: «e o impede de manter».
- **V c), nota 22, último parágrafo.** As aspas abrem antes de *Au contraire* e fecham no fim, com o
  inciso *nous avouait dernièrement une âme loyale* dentro delas; ficou igual. *une sorte de dégoût
  causée* (concordância errada do impresso) → «causado».
- **V c), nota 24.** O «literato do século passado» não é nomeado pelo autor; não acrescentei o nome.
- **V, fim, *parce que vraie respiration de mon âme*.** Elipse do verbo, guardada: «porque verdadeira
  respiração da minha alma».

## Remissões de página

Nenhuma neste arquivo.

## Emendas

Lições do texto-base que divergem da imagem do scan. A tradução segue o scan:

| parágrafo | texto-base | scan / lição traduzida |
|---|---|---|
| IV b), *Certes, j'ai une part de choix…* | *In primis quae tibi* | *In primis quæ tibi* (com ligadura, como o resto do latim do livro) |
| V a), *L'Eglise les emploie…* | *m'at-elle dit* | *m'a-t-elle dit* (no livro, *m'a-* / *t-elle* na virada de linha; a junção apagou um hífen): «disse-me ela» |
| V c), *Mais son rôle restera secondaire…* | *se maintenir en adoration ou revenir à cette attitude* | *… ou à revenir à cette attitude* (pág. 265): «a manter-se em adoração ou a voltar a essa atitude» |

Divergência em referência bíblica, sem efeito na tradução (ver Dúvidas, 2): na nota 4, o texto-base
traz *Philip., II, 8*, que é o versículo certo; no scan (pág. 251) lê-se *II, 5*. Mantive «II, 8», como
no texto-base.

## Dúvidas para quem coordena

1. **Negrito.** Esta é a primeira parte traduzida com negrito no livro. Marquei-o com `**…**`, que o
   leitor do site já sabe exibir. Se se preferir não usar negrito na edição, há duas saídas:
   - tirar os `**` e deixar só o itálico;
   - nos títulos corridos («**Humildade perfeita.**», «**_Dignè_.**»…), trocar o negrito por itálico.

   Convém que o tradutor de `05-quinta-parte-b.txt` (V.3, I–III, com os títulos corridos *Christus.*
   e afins) e o de `05-quinta-parte-d.txt` sigam a mesma regra.
2. **Nota 4, *Philip., II, 8*.** O scan de 1927 parece trazer *II, 5* (gralha do impresso, porque o
   versículo é Fl 2,8). O texto-base já está com 8, sem registro em `emendas.txt`. Pelo LEIAME, as
   referências ficam como no impresso; se se quiser seguir isso à risca, a nota deve dizer «II, 5».
3. ***suffisance*.** Em IV b) usei «suficiência», porque *présomption* e *suffisance* vêm lado a lado.
   Na Primeira parte, as duas palavras deram «presunção». Se se adotar «suficiência» também lá (é a
   dúvida 2 das notas da Primeira parte), a obra fica coerente.
4. **Gralhas no `original/05-quinta-parte-c.txt`.** As três lições da tabela de emendas convém
   corrigir no próprio texto-base, que vai ao lado da tradução. Não mexi nele, porque a tarefa só
   permite gravar a tradução e estas notas.
5. **Proposta para o guia (não alterado).**
   - Registrar a regra do negrito (ver 1).
   - Acrescentar ao vocabulário: *honoraires* → espórtulas; *sans-gêne* → sem-cerimônia; *crainte
     révérentielle* → temor reverencial; *Eglise souffrante* → Igreja padecente; *Prêtre* (Cristo, e o
     padre unido a ele como Sacerdote) → Sacerdote.
