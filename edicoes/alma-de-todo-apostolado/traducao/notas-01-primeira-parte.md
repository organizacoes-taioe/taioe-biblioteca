# Notas do tradutor: A alma de todo apostolado, Primeira parte

Arquivo: `traducao/01-primeira-parte.txt`. Texto-base: `original/01-primeira-parte.txt` (12e édition, 1927,
págs. 4–46 do livro). A tradução foi escrita por um primeiro tradutor, cuja sessão caiu antes da
conferência. Nesta revisão ela foi conferida contra o original, parágrafo a parágrafo, e contra a
imagem do scan, página a página (`ferramentas/cache/alma/rev/019.png` a `061.png`).

Conferência por script: 216 blocos no original e 216 na tradução. São 1 cabeçalho, 9 títulos `##`,
48 notas `¤ [n]`, 2 parágrafos de continuação de nota `¤` (na nota 10), 1 estrofe de 2 versos `| ` e
155 parágrafos de prosa; os 156 «parágrafos» do LEIAME contam a estrofe. As marcas `[I.1]` a `[I.7]`
estão iguais e na mesma ordem (o `[IV.1]` e o `[I.1]` a mais só aparecem, iguais, dentro da linha
`# nota:` do cabeçalho). As 48 chamadas `[n]` e as 48 notas `¤ [n]` estão iguais e nos mesmos
parágrafos. Os 9 títulos foram traduzidos com o prefixo, os números e o ponto final. Nenhum parágrafo
traduzido tem menos de 0,8 do tamanho do original; as notas 1, 18, 22, 26, 28 e 33 quase dobraram por
causa do `[Trad.: …]`. As linhas `# ` do topo foram copiadas, e só o `# titulo:` foi traduzido
(«Primeira parte»). Varreduras de mesóclise, depois da revisão: o grep do CONVENCOES e a varredura em
Python com a mesma regex terminada em `(?![A-Za-zÀ-ÿ])` não acharam nada.

## Correções feitas nesta revisão

A tradução do primeiro tradutor estava completa e, no geral, fiel. A revisão mudou o seguinte.

1. **Itálico do autor**, conferido nas 43 páginas do scan. O texto-fonte não marca o itálico, e a
   primeira versão só tinha posto em itálico o latim e os títulos. Foram acrescentadas cerca de 80
   ênfases do autor, todas visíveis na imagem, como no Prelúdio:
   - I.1: *se répandre*, a frase *C'est par l'homme que l'homme doit connaître le chemin du salut*,
     *clergé*, *volontaires*, « *personnes d'œuvres* », *avant tout, des hommes de vie intérieure*;
   - I.2: *Vie surnaturelle*, *participer*, *communiquer*, *désordre intellectuel*, *négation d'une
     grande partie du Traité de la Grâce*, *Hérésie des Œuvres* (duas vezes);
   - I.3:
     - *vie d'oraison*, *vie contemplative*;
     - a frase *pour le gouvernement intime … absolument certain*;
     - *en moi*, *méritoire exemplaire et finale*, *efficiente*, *événements*, *personnes*, *choses*,
       *état de grâce*, *son Esprit*;
     - a citação *Ce n'est plus moi qui vis…*;
     - *Vie intérieure*, *habituelle*, *actuelle*;
     - a definição inteira *l'état d'activité d'une âme qui RÉAGIT…*;
     - *à chaque moment*, *ma vie*, *chaque*, *Vous-même*, *sollicitez ma coopération…*, *dans la
       mesure même où se développent ces éléments*, *même violentes*, *prolongées*, *s'y oppose*,
       *augmenter*, *crainte de Dieu*, *componction*;
     - na nota 10: *combattues*, *tiédeur de volonté*, *n'est pas combattue*;
     - *garder mon cœur*, *ne soit pas étouffée la voix de Jésus*, a frase *les péchés véniels
       arriveront à pulluler…*;
     - a definição da guarda do coração (*la sollicitude HABITUELLE … ACCOMPLISSEMENT*), *exige*,
       *habitude*, *posséder la joie*;
     - a citação inteira de Isaías (10ª verdade), *rien*, *tout puissants*, e nas notas 16 e 17
       *rien* e *tout*;
   - I.4: *Vivre avec soi, en soi*, *gouverner soi-même*, *servantes de la volonté*, *amour de
     l'action pour l'action*, *vivre en nous-mêmes*, *labeur de la vie intérieure*, *vie avec Jésus,
     en Jésus, par Jésus*, *vie eucharistique*, *sorte de dogme*, *seconde nature*, *répugnance*,
     *s'étourdir*;
   - I.5: *voulait active*, *au prix de quel labeur arrive-t-il à ce résultat!*, *Dieu invisible comme
     s'il le voyait*, *joies spéciales*, *vivre dans le surnaturel*, *vie entière*, *graduellement*,
     *partie négative*, *côté positif*; na nota 29, *difficultés*, *épreuves*, *actifs*;
   - I.6: a frase *Je me sacrifie moi-même pour eux AFIN QU'eux aussi…*, *pour ce monde corrompu*,
     *prie, traite avec la*, *directement*, *mais aussi à la vie intérieure*, *Vie divine*, *banalité
     de notre Vie intérieure*;
   - I.7: *Voulez-vous plaire à Dieu, ayez pitié de votre âme*, *n'entend pas donner à la vie active
     la préférence sur la contemplation*, *jamais plus que nous-mêmes*, *Note de retraite* (título), a
     frase de Lallemant *qui s'applique davantage au gouvernement d'un cœur…*.

   As palavras em versalete no meio de um trecho em itálico ficaram em maiúsculas dentro do itálico
   («_… que REAGE para REGULAR …_»). O latim das notas, que o livro imprime em redondo, está em
   itálico, como manda o guia.
2. **Sentido e estilo:**
   - I.2, *elle n'est que trop vraie*: «ela é verdadeira demais» → «ela é por demais verdadeira».
   - I.3, *C'est une vue, par le cœur, des actions présentes*: «uma vista» → «uma visão».
   - I.4, *ne pas se laisser gouverner par le dehors*: «pelo de fora» → «pelo que vem de fora».
   - I.5, *a rendu ce double mouvement … pénible à effectuer*: «tornou penoso de efetuar» → «tornou
     penoso efetuar».
   - I.5, *à rebâtir et à préserver ensuite d'une ruine nouvelle*: «a preservar depois de uma nova
     ruína» (que se lia «depois que houver uma nova ruína») → «a preservar, depois, de uma nova ruína».
   - I.6, *Nous n'irions pas jusqu'à admettre*: «Não iríamos até admitir» → «Não chegaríamos a
     admitir».
   - I.7, nota de retiro de Dupanloup, *cette vue me préoccupe*: «essa vista» → «essa visão».
   - I.7, *Satan, lui, tout au contraire*: «Satanás, ao contrário» → «Satanás, por sua vez, bem ao
     contrário» (o *lui* e o *tout* tinham caído).
3. **Santos nas referências das notas.** Dentro dos parênteses, «São Gregório», «Santo Tomás», «São
   Bernardo», «Santo Efrém» passaram à minúscula, como manda o guia («Saint, com nome, vai em
   minúscula») e como está no Prelúdio («santo Agostinho»). Isso vale para as notas 18, 20, 21, 22,
   26, 45 e 47. Onde o nome abre a nota (notas 23, 41, 42, 48), a maiúscula é de começo de frase e
   ficou.

## Decisões gerais

- **Tratamento.**
  - O autor ao leitor: *nous* («nós», «a nós mesmo», com o singular do *nous* de modéstia: *nous ont
    aidé nous-même*). Quando ele usa *vous* (I.6, *Voyez-les suivre la marche des apôtres*), ficou
    **vós**: «Vede-as».
  - Jesus, na 3ª verdade (I.3): o autor escreve *Vous, ô Jésus, Vous-même, Vous Vous présentez … Vous
    cachez*, com maiúscula, e *votre sagesse*, *votre amour*, *votre vie*, em minúscula. A tradução
    segue palavra a palavra: «Vós, ó Jesus, _Vós mesmo_, Vos apresentais … Vós ocultais … a vossa
    sabedoria». Na 6ª verdade (*vos Plaies, ô Miséricordieux Rédempteur … vos pieds … votre Sang*),
    tudo em minúscula, como no original: «vossas Chagas», «vossos pés», «vosso Sangue».
  - A alma a si mesma: *O mon âme … Oserais-tu* → «Ó minha alma … Ousarias».
  - Falas entre pessoas: também por **vós**, porque o *vous* francês é aí cerimonioso. São elas: o
    bispo ao homem de Estado (I.5), o padre de Ravignan («Perguntais-me…»), são Bernardo a Eugênio
    III, e santa Teresa às religiosas («Referi…, minhas filhas»). A alma tíbia, na nota 10, diz a
    Deus «não quero deixar de vos desagradar».
- **Maiúsculas de reverência e de substantivos**, seguidas palavra a palavra: *Lui*, *Il* (Deus,
  Jesus) → «Ele»; *Elle* (a Causa primeira, I.6) → «Ela»; *Son intimité*, *Sa vie* (10ª verdade) →
  «a Sua intimidade», «a Sua vida». Também *Œuvres*, *Vie intérieure*, *Vie surnaturelle*, *Vie
  intime*, *Garde du cœur* (8ª verdade), *Bon Plaisir*… Onde o autor escreve em minúscula (*vie
  intérieure* em boa parte do texto, *il* para Jesus em I.2), ficou minúscula.
- **Versalete** (aqui em maiúsculas), mantido: *SOURCE UNIQUE*, *LUI SEUL, JÉSUS, EST LA VIE*,
  *HÉRÉSIE DES ŒUVRES*, *CHACUN*, *ACTION VITALE*, as dez *VÉRITÉS*, *LA LAME USE LE FOURREAU*,
  *CREDO*, *AFIN QUE*, *CAUSE PREMIÈRE*, *D'ABORD LA MIENNE*, a frase de são Bernardo *C'EST EN VAIN
  QUE…* etc. O versalete de *1re VÉRITÉ* ficou «1ª VERDADE».
- **Latim.** No corpo, todo em itálico e sem tradução, como o autor deixa; a tradução vem nas notas
  do próprio autor. Nas notas inteiramente em latim e sem tradução do autor, foi acrescentado
  `[Trad.: …]`: na 1 (Leão XIII), na 18 (são Gregório), na 22 (santo Efrém e Hugo de São Vítor), na 26
  (são Gregório), na 28 (Hb 11,27) e na 33 (Rm 7,22-24). Ficaram sem `[Trad.]` as notas 31, 38 e 47,
  porque o próprio autor dá o sentido em francês no corpo. A 31 (santo Tomás) é parafraseada em I.5,
  *l'homme, dit-il, est placé…*. A 38 (Jo 17,19) é a frase *Je me sacrifie moi-même pour eux…* de
  I.6. A 47 (são Bernardo) é a carta a Eugênio III, traduzida no parágrafo.
- **Escritura em francês**: traduzida do francês do autor (Isaías na 10ª verdade, com «Jeová» por
  *Jéhovah*; as notas 2 a 7, 9, 11 etc.). Referências no formato do impresso: «Joan.», «Matth.»,
  «Luc», «Rom.», «Heb.», «Phil.», «Philipp.», «Ephes.», «Prov.», «Is.», «Ps.», «I Cor.», «II Cor.»,
  «I Joan.», e «S. Matth.» na nota 4, como abreviatura bibliográfica.
- **Aspas** angulares do original, «…». A fala do santo cura d'Ars (I.3) e as de Donoso Cortés e de
  santo Agostinho (I.6) vêm sem aspas no livro e assim ficaram.
- **Pontuação.** O espaço francês antes de «:», «;», «!» e «?» foi retirado. Em três lugares o
  original tem vírgula onde o português pede ponto: I.2, *succès, Une chose* (no scan, ponto); I.4,
  *contemporains, Vivre avec soi* (no scan, vírgula); I.6, *saint François-Xavier: Ils semblaient*.
  Ficou ponto. Em I.5, *ne voyons-nous pas le saint roi Louis IX…*, a frase é pergunta e termina em
  ponto no livro; a tradução pôs «?».
- *vice versa* (nota de santo Tomás, I.5), em itálico no livro, ficou «vice-versa», em redondo, porque
  é forma aportuguesada e corrente.

## Termos

| francês | português | onde / observação |
|---|---|---|
| *libéral*, *libéralité* | liberal, liberalidade | I.1 |
| *apanage* | apanágio | I.1, I.1 (fim) |
| *Exemplaire* (divin) | Exemplar | I.1 |
| *dispensation de ses bienfaits* | dispensação dos seus benefícios | I.1 |
| *cadre de l'armée du Christ* | os quadros do exército de Cristo | I.1 |
| *Milices enseignantes* | Milícias docentes | I.1 |
| *Patronages*; *Écoles libres*; *Bonne Presse* | Patronatos; Escolas livres; Boa Imprensa | I.1 (guia: *patronage* → patronato) |
| *personnes d'œuvres* | pessoas de obras | I.1, I.4 |
| *Cep* (divin) | Videira (divina) | I.2, parábola de Jo 15 |
| *entés sur l'Homme-Dieu* | enxertados no Homem-Deus | I.2 |
| *suffisance*; *présomption*; *présomptueux* | presunção; presunção; presunçoso | I.2, I.3, I.6; ver Dúvidas |
| *Hérésie des Œuvres* | Heresia das Obras | I.2; «HERESIA DAS OBRAS» no versalete |
| *américanisme* | americanismo | I.4 |
| *homme d'église* | homem de Igreja | I.4 |
| *tête-à-tête intime avec Jésus-Hostie* | colóquio a sós com Jesus-Hóstia | I.4 |
| *grâce du moment présent* | graça do momento presente | I.3 |
| *recueillement* | recolhimento | I.3 |
| *oraisons jaculatoires*; *communions spirituelles* | jaculatórias; comunhões espirituais | I.3 (guia) |
| *oraison du matin*; *examens particulier et général* | oração da manhã; exames particular e geral | I.3 (guia) |
| *Garde du cœur*; *garde du cœur* | Guarda do coração; guarda do coração | I.3, com a maiúscula do original |
| *mobile*; *accomplissement* | motivo; execução | I.3, 8ª verdade |
| *sans contention* | sem tensão | I.3 |
| *Agendo contra* | _Agendo contra_ | I.3, latim de santo Inácio |
| *Règne du Christ* (meditação) | Reino de Cristo | I.3 |
| *tiédeur de volonté* | tibieza de vontade | I.3, nota 10 |
| *bon plaisir divin* | beneplácito divino | I.5 |
| *assujétissant* | exigente | I.5; ver Passagens |
| *dévouement* | dedicação | I.4, I.5 |
| *neurasthénique* | neurastênico | I.4 |
| *cloîtrée* | enclausurada | I.6 |
| *Carmélites, Trappistines, Clarisses*; *Trappistes* | carmelitas, trapistinas, clarissas; trapistas | I.6, em minúscula, como nome de membros de ordem |
| *ménagère* | dona de casa | I.6 |
| *suppôts de Satan* | sequazes de Satanás | I.6 |
| *Chartreux* | cartuxo | I.6 |
| *Docteur angélique* | Doutor angélico | I.7 |

Nomes: Nosso Senhor; são Paulo; são Boaventura; santo Inácio; são Gregório Magno; são Bento, Subiaco;
Leão XIII, o cardeal Gibbons, arcebispo de Baltimore; o cardeal Mermillod; a bem-aventurada
Margarida Maria; Dom Sébastien Wyart (nome do trapista, mantido em francês, como os sobrenomes);
Agostinho, João Crisóstomo, Bernardo, Tomás de Aquino, Vicente de Paulo; o santo rei Luís IX;
Marta, Madalena; Donoso Cortés; Bossuet; os solitários da Tebaida; são Francisco Xavier; santa
Teresa; dom Favier, bispo de Pequim; a Cochinchina, Saigon; o padre Chevrier, Dom Bosco, o padre
Marie-Antoine; a venerável Ana Maria Taigi; são Bento José Labre; o sr. Dupont, «o santo homem de
Tours»; o coronel Paqueron; o general de Sonis; o santo cura d'Ars, o bem-aventurado Vianney; santo
Afonso de Ligório; Godofredo (secretário de são Bernardo); o papa Eugênio III; dom Dupanloup; o padre
Desurmont, C.SS.R.; o padre Faber; Dom Festugière, O.S.B.; o padre Léon, O.M.; o padre Lallemant; o
padre de Ravignan. Títulos de livros na língua do original, em itálico (*Le retour continuel à Dieu*,
*Lumière et flamme*, *Homo apost.*, *Moral.*, *de Consid.*, *Vita S. Bernardi*, *Doct. Spirit.*), salvo
os dois clássicos que o autor cita em francês no corpo, traduzidos: _Introdução à vida devota_ e
_Imitação de Jesus Cristo_.

## Passagens difíceis e leitura adotada

- **I.1, *Seul aussi, il aurait pu en appliquer la vertu*.** «Só ele também poderia aplicar-lhe a
  virtude», com o condicional simples no valor de passado («teria podido»), corrente em português.
- **I.1, *rentrer découragés sous la tente*.** Imagem de Aquiles que se retira para a tenda: «recolher-se,
  desanimados, à sua tenda».
- **I.2, *une folle présomption injurieuse pour Jésus-Christ, ne comptait guère que sur ses propres
  forces*.** «quase só contasse com as próprias forças»: *ne … guère que* é «quase só».
- **I.3, *Je puis donc la définir l'état d'activité…*.** «Posso, pois, defini-la: o estado de
  atividade…», com dois-pontos, porque a definição inteira vem em itálico no livro.
- **I.3, *Ma vie intérieure sera ce qu'est ma Garde du cœur*.** «Será o que for a minha Guarda do
  coração»: o futuro do subjuntivo dá a correspondência que o francês faz com o presente.
- **I.3, 7ª verdade, *Or je cesse forcément*.** O francês subentende o complemento («deixo de
  aumentá-la»), que a tradução explicita para a frase não ficar ambígua.
- **I.3, 10ª verdade, *au cours de ses progrès*.** O possessivo remete à vida interior: «à medida que
  essa vida progredir».
- **I.4, *Pour eux, l'église n'est pas encore un temple protestant*.** *église* em minúscula, o
  edifício: «a igreja».
- **I.5, *c'est le plus assujétissant*.** O trabalho que mais sujeita, que não deixa folga. Ficou «o
  mais exigente»; «sujeitante» não existe, e «o que mais escraviza» exageraria.
- **I.5, *pour n'aspirer que Jésus et sa vie*.** Sem *à*, *aspirer* é transitivo («respirar»); mas o
  contexto (*son cœur à tout oublier pour…*) pede o sentido de desejo. Ficou «para só aspirar a Jesus
  e à sua vida», que em português guarda o duplo valor.
- **I.5, Dom Sébastien, *Allons donc!*** Interjeição de protesto: «Ora essa!».
- **I.4, *Il la dédaigne d'autant plus, que dis-je? il a pour elle d'autant plus de répugnance que…*.**
  A correção retórica do autor ficou: «Ele a desdenha tanto mais, que digo? tem por ela tanto mais
  _repugnância_, quanto…».
- **I.6, *Le doigt sur le clavier des pardons divins*.** «Com o dedo no teclado dos perdões divinos»,
  imagem do órgão, literal.
- **I.6, *engendrer les âmes à la ferveur* (I.2) e *engendrer que des âmes d'une piété de surface*
  (I.6).** «Gerar»; *frapper sur des caractères trempés l'empreinte de Jésus-Christ* → «cunhar em
  caracteres bem temperados a efígie de Jesus Cristo» (imagem da moeda e do aço).
- **I.7, *Tuus esto ubique* … *Il n'est pas sage celui qui n'est pas à lui-même*.** «Sê de ti mesmo»
  (nota 45) e «não é sábio aquele que não é de si mesmo», para guardar o *à soi* que o autor repete
  depois (*Totus primum sibi* → «Todo de si mesmo primeiro»; *soyez donc aussi à vous-même* → «sede,
  pois, também de vós mesmo»).
- **I.7, *Prima sibi charitas*.** O autor traduz na nota 44, *Charité d'abord pour soi-même*:
  «Caridade primeiro para consigo mesmo».

## O dístico de I.3, em verso

*Je possède en tout temps et je porte en tout lieu / Et le Dieu de mon cœur et le Cœur de mon Dieu*,
atribuído pelo autor a santa Margarida Maria. São dois alexandrinos franceses de rima emparelhada
aguda (*lieu / Dieu*). Os dois têm desenho ternário 3-6-9-12 e fazem quiasmo no segundo verso. Foi
conferido pelo método do Versificador (`MANUAL-DE-TRADUCAO.md`; `ESTUDO-DO-RITMO.md`, § 5). Metro de
chegada: o alexandrino clássico com lei do hemistíquio, que é o que a tabela do manual dá para o
alexandrino francês.

| Je possède en tout temps et je porte en tout lieu | Possuo e levo sempre e sob todos os céus |
|---|---|
| Et le Dieu de mon cœur et le Cœur de mon Dieu. | O Deus do coração e o Coração de Deus. |

Conferência: `node ferramentas/molde.mjs versos.txt molde.txt`, molde `12: 6-12` nos dois versos
(temporários em `C:\Users\geren\AppData\Local\Temp\claude\alma-de-todo-apostolado-01-primeira-parte\`).
Resultado: **2 exatos, nenhum ~, nenhum ✗, nenhum ≠, forçamento 0.**

- Verso 1: `2-4-6-9-12`, hemistíquio grave com elisão (*sem/pre‿e*), 1,77% do corpus. *Todos os* conta
  três sílabas, porque o *s* de *dos* impede a fusão.
- Verso 2: `2-6-10-12`, hemistíquio agudo (*coração*), 2,4% do corpus.
- A rima é aguda, como no original: *céus / Deus*, rima tradicional da língua.
- O quiasmo passa inteiro: «o Deus do coração / o Coração de Deus», com a maiúscula de *Cœur*.
- O que cedeu:
  - os dois *mon* (*de mon cœur*, *de mon Dieu*): com «meu», o verso dá 14 sílabas;
  - *en tout lieu*, que virou «sob todos os céus», imagem de lugar que dá a rima;
  - o desenho ternário do original, porque os dois versos saem binários no primeiro hemistíquio.

A primeira versão já era esta. A revisão só a conferiu.

## Remissões de página

Nenhuma neste arquivo. A nota 34 diz *Dans un autre chapitre*, sem página: «Num outro capítulo».

## Emendas

O texto-base deste arquivo traz algumas gralhas de OCR que escaparam à revisão. O LEIAME diz que as
gralhas anteriores à pág. 168 foram corrigidas sem registro. Todas foram conferidas na imagem, e a
tradução segue a lição do scan:

| parágrafo | texto-base | scan / lição traduzida |
|---|---|---|
| I.1, fim (*Quid prodest…*) | *detri-' mentum* | *detrimentum* (o apóstrofo é sujeira da composição) |
| I.2, 1º | *succès, Une chose* | *succès. Une chose* |
| I.2, 2º | *dés qu'il s'agit* | *dès qu'il s'agit* |
| I.3, *Elle répond à la fin de l'Incarnation* | *unigenittun* | *unigenitum* |
| I.4, *Et si on n'ose…* | *au fond du cour* | *au fond du cœur* |
| I.5, *Arracher constamment…* | *sur les points et) il est* | *sur les points où il est* |
| I.6, santa Teresa | *dont lame de feu*; *ditelle* | *dont l'âme de feu*; *dit-elle* |
| I.6, Bossuet | *Thébaide* | *Thébaïde* |

Gralha do próprio impresso, corrigida só na tradução: I.3, 11ª verdade, *Loin d'engendre en moi*
(assim no scan) por *engendrer*: «Longe de gerar em mim». Referências bíblicas erradas no impresso
ficaram como estão, conforme o LEIAME. Na nota 4, *S. Matth., XVI, 25* corresponde a Mt 16,26. Na
nota 37, *Matth., XXIV, 8* corresponde a Mt 26,8.

## Dúvidas para quem coordena

1. **Gralhas no `original/01-primeira-parte.txt`.** As oito lições da tabela acima convém corrigir
   no próprio texto-base, que vai ao lado da tradução. Não mexi nele, porque a tarefa só permite
   gravar a tradução e estas notas.
2. ***suffisance* e *présomption* → «presunção».** O autor alterna as duas palavras: *sotte
   suffisance*, *folle présomption*, *orgueilleuse suffisance*, *apôtre plein de suffisance*. A
   tradução usa «presunção» para ambas. Se se quiser marcar a diferença, *suffisance* pode ir para
   «suficiência» («tola suficiência», «orgulhosa suficiência», «cheio de suficiência»), palavra que
   existe com esse sentido, mas soa menos corrente.
3. **O dístico.** Passa no molde, mas perde os dois *mon* e o ritmo ternário. Uma versão 3-6-9-12 com
   «meu» não coube em doze sílabas sem enchimento. Se se preferir guardar o possessivo à custa da
   imagem, a alternativa a estudar é deslocar *sempre* e *sob todos os céus* para um só hemistíquio.
4. **Proposta para o guia (não alterado).**
   - Registrar que os santos nas referências das notas vão em minúscula dentro dos parênteses
     («(são Gregório)»), mas com maiúscula quando abrem a nota («¤ [23] Santo Tomás…»).
   - Registrar que o itálico do autor, conferido no scan, se marca também nesta parte, como no
     Prelúdio. Ele é frequente: cerca de 80 ocorrências em 43 páginas.
