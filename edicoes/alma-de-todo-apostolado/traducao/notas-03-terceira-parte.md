# Notas do tradutor: A alma de todo apostolado, Terceira parte

Arquivo: `traducao/03-terceira-parte.txt`. Texto-base: `original/03-terceira-parte.txt` (12e édition,
1927, págs. 70–108 do livro). Um tradutor anterior caiu antes de gravar e deixou um rascunho parcial
(`p1.txt`, só o cap. 1) na pasta temporária. Esse rascunho não foi aproveitado: a tradução foi feita
de novo, inteira. Ela foi conferida contra o original, parágrafo a parágrafo, e contra a imagem do
scan, página a página (`ferramentas/cache/alma/rev/087.png` a `125.png`).

Conferência por script (`check.py`, na pasta temporária
`C:\Users\geren\AppData\Local\Temp\claude\alma-de-todo-apostolado-03\`):

- **Blocos:** 192 no original e 192 na tradução, do mesmo tipo e na mesma ordem. São:
  - 1 cabeçalho;
  - 11 títulos `##`;
  - 44 notas `¤ [n]`;
  - 12 parágrafos de continuação de nota `¤`: 3 na nota 10 e 9 na nota 42, que traz a oração do general de Sonis;
  - 124 parágrafos de prosa, o mesmo número do LEIAME.
- **Marcas:** `[III.1]`, `[III.2]` e `[III.3]`, iguais e na mesma ordem.
- **Chamadas:** as 44 chamadas `[n]` estão nos mesmos parágrafos que no original.
- **Títulos:** os 11 foram traduzidos com o prefixo, os números e as letras.
- **Tamanho:** nenhum parágrafo traduzido tem menos de 0,78 do tamanho do original. Os três mais curtos (0,78–0,79) são linhas breves: um título, a nota 40 e o versículo de Isaías. As notas 3 e 6 dobraram por causa do `[Trad.: …]`.
- **Cabeçalho:** as linhas `# ` do topo foram copiadas, e só o `# titulo:` foi traduzido («Terceira parte»).
- **Mesóclise:** o grep do CONVENCOES e a varredura em Python com a mesma regex terminada em `(?![A-Za-zÀ-ÿ])` não acharam nada.
- **Itálico:** os `_` estão pareados em todos os blocos.

## Decisões gerais

- **Itálico do autor**, conferido nas 39 páginas do scan, como no Prelúdio e na Primeira parte (instrução
  do coordenador). O latim e os títulos de obras vão sempre em itálico. As ênfases francesas foram
  marcadas só onde o itálico é visível na imagem:
  - **III.1**
    - *se conservent*, *progressent*, *émanant de la volonté divine*, *forcément*;
    - *moyen de sanctification*, *confiance absolue dans son droit rigoureux*;
    - a citação *Pais mes agneaux, pais mes brebis*;
    - as duas citações de Jesus: *Je suis au milieu de vous…* e *Le Fils de l'homme…*;
    - *moyens de progrès*, *instruments de ruine*, *cause*, «*C'est le dévouement qui m'a perdu !*»;
    - a carta inteira de são Bernardo, menos as palavras em versalete;
    - *occupations maudites*, duas vezes.
  - **III.2**
    - a frase *de volonté, c'est faire un pacte … délibéré*, e *enlever à l'âme l'assurance du salut éternel*;
    - na nota 10, os dois textos bíblicos citados em francês;
    - *toute à la satisfaction … cause excellente?*, *Il faudrait se ressaisir*, *Qu'elle est heureuse de se rassurer par tous ces prétextes !*, *Agir était devenu … la fièvre*;
    - *il se lance … ses remords*, *les vertus actives*;
    - os nomes das quatro etapas: *Première étape*, *Deuxième étape*, *Troisième étape*, *Quatrième étape*;
    - *netteté*, *force des convictions*;
    - *Méditation*, na segunda ocorrência; *facilement*; *l'âme s'est mise en état de ne plus voir*;
    - *abandon de l'ORAISON et de tout RÈGLEMENT*, *négligence dans la récitation du BRÉVIAIRE*;
    - o parágrafo inteiro *L'apôtre ainsi déformé…*;
    - a fala de Jesus *Viens à moi, pauvre âme blessée… Je suis venu sauver ce qui périssait*, com o latim que ela intercala; *Jésus ne peut entrer*;
    - *pensées*, *moi*, *imagination*, *affections*, *volonté*, «*Je ne puis pas*»;
    - a resposta ao ímpio, *que ces chutes on les évite … vers le précipice*;
    - na citação de Lallemant, *alors seulement ils ouvrent les yeux*.
  - **III.3**
    - *saint*, *débutant*, *tiède*, *simple fervent*;
    - *l'apôtre vrai les redoute*, *Se rendre compte*, *résister aux tentations*;
    - *pureté d'intention*, *charité*, *discrétion*, *retenue*, *la foi*, *orgueil*, *combattre*, *conquérir*;
    - *pourvu qu'il y ait eu efforts sérieux*, *perpétuels recommencements*;
    - *l'intelligence*, *énergie surnaturelle de volonté*, *intensité de charité*;
    - *celui de la joie*, *grand bonheur ici-bas*, *aliment de joie*;
    - a frase de Bossuet;
    - nas notas, os títulos *Lumière et flamme*, *Le retour continuel à Dieu*, *Apprentissage de la Garde du cœur* e *Vie* (de Sonis).

  Não estão em itálico no livro, e assim ficaram, as citações de Álvarez de Paz, de santa Teresa, de
  são João da Cruz, de Lavigerie, de são Vicente, de Lallemant (salvo o trecho acima), de Combalot, de
  Pio X e de santo Inácio, nem a fala de Jesus em III.3 b) (*Reviens à moi, pauvre cerf haletant…*).
  As palavras em versalete dentro de um trecho em itálico ficaram em maiúsculas fora do sublinhado
  («_vos_ SUBTRAIR A ESSAS OCUPAÇÕES, _ainda que…_»). O latim em versalete (*HÆ OCCUPATIONES
  MALEDICTÆ*) ficou em maiúsculas e em itálico.
- **Versalete** (aqui em maiúsculas):
  - os subtítulos «a) MEIO DE SANTIDADE.» e «b) PERIGO PARA A SALVAÇÃO.»;
  - QUERIDO, NAS CONDIÇÕES REQUERIDAS, DEVE A SI MESMO, ELE OS DEVE, DÍVIDA DO CORAÇÃO DE DEUS, DEUS QUER;
  - SUBTRAIR A ESSAS OCUPAÇÕES, AO ENDURECIMENTO DO CORAÇÃO, OCUPAÇÕES MALDITAS;
  - INEXPERIÊNCIA, PRESUNÇÃO, VAIDADE, IMPREVIDÊNCIA e COVARDIA;
  - A AUSÊNCIA DE BASE SOBRENATURAL, ORAÇÃO, REGULAMENTO, BREVIÁRIO, SACRAMENTOS;
  - SEGURAMENTE, INFALÍVEL.

  Sobre *La Messe ELLE-MEME*, ver Emendas.
- **Tratamento.**
  - Jesus em oração (fim de III.2) e Deus na fala da alma (III.3 e) e na oração de Sonis: **vós**, em minúscula, como no original. Onde o autor põe maiúscula, ela ficou: são Gregório Nazianzeno, *en Vous seul* → «em Vós só»; Sonis, *détruit par Vous* → «destruído por Vós».
  - Jesus à alma (III.2 e III.3 b), f)): **tu**. As maiúsculas de *avec Moi, par Moi et en Moi* ficaram «Comigo, por Mim e em Mim».
  - O autor ao leitor (*Demandez-lui…*, *N'en cherchez pas…*), são Bernardo ao papa, santa Teresa, o pregador vaidoso (*Que voulez-vous*) e o padre que assiste Combalot: **vós**, como na Primeira parte.
  - A vida ativa interpelada (*O vie active, tu le reconnais*): **tu**.
- **Maiúsculas de reverência e de substantivos**, seguidas palavra a palavra:
  - *Il*, *Lui*, *Lui-même* (Jesus, Deus) → «Ele», «Dele», «Ele mesmo»; onde o autor escreve *il*, *lui* em minúscula, ficou minúscula;
  - *Œuvres* / *œuvres*, *Vie intérieure*, *Sainteté* / *sainteté*, *Apostolat*, *Plan divin*, *Puissance de Dieu*;
  - «bem-aventurado Cura d'Ars» com maiúscula em III.3 d), como no livro, e «cura d'Ars» em minúscula na nota 42.
- **Latim.** No corpo, em itálico e sem tradução, como o autor deixa. Nas notas inteiramente em latim e sem o sentido dado pelo autor, acrescentei `[Trad.: …]`, com o mesmo critério da Primeira parte:
  - nota 3 (Mt 25,40);
  - nota 6 (Is 53,2-3): o corpo só dá uma frase;
  - nota 25, na sentença de Fischer.

  Ficaram sem `[Trad.]` as notas 4, 5 e 9, porque o próprio autor traduz o latim no corpo: *Je suis au milieu de vous…*, *Le Fils de l'homme…* e a carta de são Bernardo.
- **Referências.** As referências bíblicas estão no formato do impresso («Matth.», «Luc», «Joan.», «Ps.», «III Reg.», «Philipp.», «Cant.», «I Petr.», «Eph.», «Math.»), com os erros do impresso (ver Emendas). Nelas, *et* → «e» e *à* → «a» («Is., LIII, 2 e 3»; «Eph., VI, 11 a 17»). O nome por extenso *Jérémie* → «Jeremias». As abreviaturas de autor das notas foram por extenso:
  - «São Boaventura», «Padre Lallemant», «Santo Inácio», «Bem-aventurado cura d'Ars» com maiúscula quando abrem a nota;
  - dentro dos parênteses, em minúscula: «santo Agostinho», «são Bernardo», «santo Tomás» (*D. THOM.*), «cardeal Fischer», como na revisão da Primeira parte.

  Os títulos e as abreviaturas de obras ficaram como estão: *Vit. S. Franc.*, *in Psalm.*, *De Consid.*, *Doct. spirit.*, *Opusc. de Vit. contempl.*, «Tom. III, liv. V.».
- **Aspas** angulares, «…», com “…” dentro (só na fala de são Vicente de Paulo; ver Emendas).
- **Pontuação.** Foi retirado o espaço francês antes de «:», «;», «!» e «?». Duas frases que no livro
  terminam em ponto, sem ser perguntas de fato, ficaram com ponto:
  - *Combien de fois, hélas!… de l'édifice spirituel.*;
  - *Mais qui ne voit que … aux pires malheurs.*

  A pergunta *N'est-ce pas contre un pareil danger…*, que o autor deixa sem fecho, desemboca na carta de são Bernardo e também ficou assim.

## Termos

| francês | português | observação |
|---|---|---|
| *dévouement* | dedicação | como na Primeira parte; «*C'est le dévouement qui m'a perdu*» → «Foi a dedicação que me perdeu» |
| *homme d'œuvres*; *homme d'Œuvre(s)* | homem de obras; homem de Obras | maiúscula do original; o singular *d'Œuvre* de III.2 virou plural |
| *ouvrier évangélique / apostolique* | operário evangélico / apostólico | guia |
| *homme apostolique*; *apôtre vrai*, *vrai apôtre* | homem apostólico; apóstolo verdadeiro, verdadeiro apóstolo | ordem do original |
| *tiède*, *tiédeur (de volonté)* | tíbio, tibieza (de vontade) | guia; nota 10 da Primeira parte |
| *oraison*; *méditation*; *prière* | oração; meditação; oração | *prière* também «oração», como na Primeira parte; o contexto distingue |
| *oraisons jaculatoires*; *garde du cœur* | jaculatórias; guarda do coração | guia |
| *règlement* | regulamento | regra de vida do padre |
| *lâcheté* | covardia | como na Primeira parte |
| *dissipation*; *recueillement* | dissipação; recolhimento | |
| *Frères enseignants*; *Sœurs gardes-malades* | Irmãos professores; Irmãs enfermeiras | |
| *guérisseur* | sanador | «curador» tem sentido jurídico e «curandeiro» é pejorativo |
| *souffre-douleurs* | maltratados de todos | ver Passagens |
| *calorique* | calórico | o fluido do calor da física antiga, imagem do autor |
| *pensum* | tarefa de castigo | o castigo escolar |
| *folle du logis* | louca da casa | a imaginação, expressão consagrada |
| *tête-à-tête avec Jésus* | colóquio a sós com Jesus | como na Primeira parte (I.4) |
| *balancier* | vara de equilíbrio | a vara do equilibrista na corda bamba |
| *oiseleur*; *alouette* | passarinheiro; cotovia | o «espelho de cotovias» |
| *Esprit de Force* | Espírito de Fortaleza | ver Jogos de palavras |
| *retenue* | comedimento | III.3 a) |
| *énerver* | quebrantar | sentido clássico, «tirar a força» |
| *abreuvé d'humiliations* | abeberado de humilhações | |
| *Notre-Dame des Sept-Douleurs* | Nossa Senhora das Sete Dores | |
| *Venator animarum* | _Venator animarum_ | latim entre aspas, como no livro |
| *Apprentissage de la Garde du cœur* | _Aprendizado da Guarda do coração_ | título de V.4, IV (ver Remissões) |

Nomes: são Paulo, Tito, Timóteo; os Bernardos e os Franciscos Xavier; Álvarez de Paz (com acento, forma
espanhola do jesuíta Diego Álvarez de Paz); santa Teresa; são João da Cruz; são Gregório; são Francisco
de Assis; são Boaventura; Isaías; o padre Léon, O.F.M. Cap.; o papa Eugênio III; são Bernardo; santo
Tomás; santo Afonso; o padre Desurmont; o cardeal Lavigerie; são Vicente de Paulo; o padre Lallemant; o
padre Combalot (*l'abbé*); o cardeal du Perron; Elias; são Gregório Nazianzeno; são Jerônimo; o Doutor
seráfico (são Boaventura); Pio X; são Francisco de Sales; o bem-aventurado Cura d'Ars; santo Inácio; o
general de Sonis; Bossuet; o cardeal Fischer (assim no livro; é são João Fisher).

## Passagens difíceis e leitura adotada

- **III.1, *la si judicieuse et si spirituelle sainte Thérèse*.** *Spirituelle* aplicada a uma pessoa
  é, em francês, quase sempre «espirituosa», «de espírito vivo», e combina com o *mot paradoxal* que
  vem em seguida. Ficou «tão espirituosa». Se se preferir o outro sentido, troque por «tão
  espiritual».
- **III.1, *n'a pas en soi, comme effet, d'altérer*.** «não tem em si mesmo por efeito alterar».
- **III.1, *l'acquisition des vertus poursuivies jusqu'à la sainteté*.** «a aquisição das virtudes
  levadas até a santidade».
- **III.1, *dans les plus chétifs des souffre-douleurs*.** *Souffre-douleur* é aquele em quem todos
  descarregam os maus-tratos. Ficou «nos mais desvalidos dentre os maltratados de todos». O «de
  todos» se repete logo depois (*méprisé de tous* → «desprezado de todos»), e isso faz eco à imagem
  do Servo.
- **III.1, *une moisson de grâces qui lèvent*.** *Moisson* semeada que «brota»: «uma seara de graças
  que germinam», para a imagem não se partir entre colheita e semeadura.
- **III.1, *accable de ses coups* / *un ver qu'on écrase*.** Os verbos são diferentes no francês:
  «acabrunha com os seus golpes» / «um verme que se esmaga».
- **III.1, *Aussi, nous l'avons regardé*.** «E assim nós o olhamos»: *aussi* em começo de frase é
  consecutivo («por isso»), não aditivo.
- **III.1 b), *Satan a tout su mettre en œuvre*.** «Satanás soube lançar mão de tudo», para não
  repetir «ação» (*le délire de l'action* vem logo depois).
- **III.1 b), *Du même coup*.** «Com isso mesmo», e não «do mesmo golpe», que é galicismo.
  O mesmo vale em III.2 e III.3 d).
- **III.2, *fatalement il va le devenir*.** «fatalmente vai tornar-se tal».
- **III.2, *Il faudrait se ressaisir*.** «Seria preciso recobrar o domínio de si».
- **III.2, *Agir était devenu pour sa victime une passion, il lui en donne la fièvre*.** «Agir
  tornara-se para a sua vítima uma paixão; ele a transforma em febre». O literal («dá-lhe a febre
  dela») ficava obscuro.
- **III.2, *et pour cause*.** Ironia: «e não sem motivo».
- **III.2, nota 10, terceiro parágrafo.** A frase do autor não tem verbo principal (*Or, sans une vie
  intérieure sérieuse, nombreux péchés véniels non combattus…*). Ficou elíptica também em
  português, como no impresso.
- **III.2, *il ne pouvait croire à la fidélité à leurs vœux et obligations chez certaines âmes*.**
  A construção foi refeita, sem mudança de sentido: «não podia crer que certas almas, misturadas
  pelas suas obras à vida do século, fossem fiéis aos seus votos e obrigações».
- **III.2, *Jésus cessera-t-il de parler*.** Com «talvez» anteposto, o português pede subjuntivo:
  «Talvez até… Jesus deixe de falar».
- **III.2, *que vous ne voudrez connaître nos travaux que s'ils sont animés … et plongent*.** «que não
  querereis conhecer os nossos trabalhos senão se forem animados … e mergulharem».
- **III.3 b), *le foyer de mon amour tu retremperas l'acier*.** *Foyer* da forja: «na fornalha do meu
  amor retemperarás o aço».
- **III.3 c), *L'amour est fort contre la mort* (nota 32).** O autor traduz assim *Fortis ut mors
  dilectio*, em vez do usual *fort comme la mort*. A tradução segue o francês dele: «forte contra a
  morte».
- **III.3 c), *La quatrième*.** O impresso tem o feminino só nesse item da série (*le premier, le
  second, le troisième, la quatrième, le cinquième*). Na tradução ficou «O quarto».
- **III.3 e), *entretient-il d'autant plus … qu'il fonde*.** «mantém na alma o horror …, e tanto mais
  quanto põe na persuasão da sua própria impotência … a expectativa dos seus êxitos».
- **III.3 f), oração de Sonis, *Vous êtes mon Maître, et je suis votre propriété*.** *Maître* em
  oposição a *propriété* é o dono, não o mestre que ensina: «Vós sois o meu Senhor».

## Jogos de palavras e perdas

- **III.3 c), *Force*.** Toda a seção joga com *force*: *une force*, *la Force par essence*, *la Force
  du Père*, *l'Esprit de Force*. Para o dom do Espírito Santo, o uso católico em português é
  «fortaleza». Ficou «o Espírito de Fortaleza», e a cadeia «Força… Força… Fortaleza» perde um
  pouco da repetição. Se se preferir guardá-la inteira, «o Espírito de Força» também se entende.
- **III.1, *DETTE DU CŒUR DE DIEU* / *hypothèque*.** A metáfora jurídica passa: «dívida», «hipoteca».
- **III.2, *vertus actives*.** O autor alude ao americanismo, como na Primeira parte. Ficou «virtudes
  ativas», em itálico, como no livro.

## Remissões de página

1. **Nota 11, *Voir note, page 17*.** A pág. 17 do livro é a 6ª verdade de I.3, com a nota sobre a
   tibieza de vontade (nota 10 de `01-primeira-parte.txt`), que cita o padre Desurmont, *Le retour
   continuel à Dieu*. A remissão ficou «Ver a nota da primeira parte, cap. 3 (6ª verdade)».
2. **Nota 10, quarto parágrafo, *« Occupations maudites » de la page précédente*.** A expressão está
   no fim de III.1 b). Ficou «do fim do capítulo anterior».
3. **Nota 28, *page 253, sur l'Apprentissage de la Garde du cœur*.** Nesta edição, a pág. 253 cai em
   V.3, sobre a vida litúrgica (`final/270.txt`). A seção *IV. Apprentissage de la Garde du cœur* está
   em V.4, págs. 277–278 (`05-quinta-parte-d.txt`, linha 122). A remissão é, ao que parece, resto da
   paginação de uma edição anterior. Ficou «na quinta parte, cap. 4, IV, sobre o _Aprendizado da
   Guarda do coração_». Convém que o tradutor de `05-quinta-parte-d.txt` use o mesmo termo no
   título, ou que se acerte aqui o que ele escolher.

O texto «Nous avons parlé de ce danger au chapitre précédent» (III.3 a)) não traz página: «Falamos
desse perigo no capítulo precedente».

## Emendas

| lugar | texto-base | scan / lição traduzida |
|---|---|---|
| III.1 b), carta de são Bernardo | *peu à peu elles vous minent infailliblement là où vous ne voulez point aller* | *elles vous mènent* (pág. 77, nítido): «vos levem infalivelmente aonde não quereis ir» |
| III.2, quarta etapa | *La Messe ELLE-MEME* | no scan, a palavra *Messe* também está em versalete (*LA MESSE ELLE-MÊME*): «A PRÓPRIA MISSA» |
| III.2, são Vicente de Paulo | *: « c'est la vie animale toute pure. »* (as aspas de dentro abrem e não fecham) | assim também no scan; na tradução, aspas internas fechadas: «…: “é a vida animal pura e simples.”» |

Referências erradas no impresso ficaram como estão, conforme o LEIAME:

- nota 4, *Luc, XXIII, 27*, por Lc 22,27;
- nota 13, *Ps., CXXXII, 2*, por Sl 137,1 (Vulgata);
- nota 20, *Jérémie, IV, 5*: o versículo é de Lamentações 4,5, atribuídas a Jeremias;
- nota 23, *Cor., XV, 28*, sem o «I»;
- nota 29, *Tim., II, 1*, por II Tim;
- nota 28, *Math.*, grafia do impresso.

## Dúvidas para quem coordena

1. **Gralha no `original/03-terceira-parte.txt`.** Convém corrigir *minent* → *mènent* (carta de são
   Bernardo, III.1 b)) no próprio texto-base, que vai ao lado da tradução. Não mexi nele.
2. **Nota 28.** A remissão do autor (*page 253*) aponta para o lugar errado nesta edição. Troquei pela
   seção certa (V.4, IV), mas sem marcar a troca no texto. Se se preferir registrá-la no próprio
   texto, pode-se acrescentar «[Trad.: no original, «página 253»]».
3. ***Spirituelle* (santa Teresa) e *Esprit de Force*.** Ver Passagens e Jogos de palavras: são duas
   escolhas de sentido que podem ser revistas sem mexer no resto.
4. **Termo para *Apprentissage*.** «Aprendizado» (aqui) ou «aprendizagem»: convém fixar no guia,
   para que a nota 28 e o título de V.4, IV coincidam.
5. **Proposta para o guia (não alterado):** registrar *dévouement* → dedicação; *guérisseur* →
   sanador; *folle du logis* → louca da casa; *Esprit de Force* → Espírito de Fortaleza; e o critério
   do `[Trad.]` (só nas notas latinas cujo sentido o autor não dá no corpo).
