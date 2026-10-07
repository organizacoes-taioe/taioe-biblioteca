# Notas do tradutor: A alma de todo apostolado, Quinta parte, capítulo 3, I a III

Arquivo: `traducao/05-quinta-parte-b.txt`. Texto-base: `original/05-quinta-parte-b.txt` (12e édition, 1927,
págs. 217–245 do livro). Um tradutor anterior caiu antes de gravar; não havia arquivo parcial, e esta
tradução foi feita do começo. Conferida contra a imagem do scan, página a página
(`ferramentas/cache/alma/rev/234.png` a `262.png`; a pág. 245 tem só o fim do arquivo).

Conferência por script: 172 blocos no original e 172 na tradução. São 1 cabeçalho, 13 títulos `##`
(5 títulos de texto e 8 `## * * *`), 46 notas `¤ [n]`, 5 parágrafos de continuação `¤` (dois na nota 6,
um na 9, um na 22, um na 31) e 107 parágrafos de prosa, como no LEIAME. A marca `[V.3]` está no primeiro
parágrafo, como no original (as outras marcas só aparecem, iguais, na linha `# nota:`). As 46 chamadas
`[n]` e as 46 notas `¤ [n]` estão iguais e nos mesmos blocos. Os títulos guardam o prefixo, os números
romanos e o ponto final. Nenhum bloco traduzido tem menos de 0,75 do tamanho do original; o script só
apontou o título «I. Que é a Liturgia?» (0,72, por ser curto) e a nota 31 (porque o `[Trad.: …]` fica no
meio). As linhas `# ` do topo foram copiadas; só o `# titulo:` foi traduzido («Quinta parte, capítulo 3,
I a III»). Itálico e negrito equilibrados em todos os blocos; aspas «» e “” fechadas. Varreduras de
mesóclise: o grep do CONVENCOES e a varredura em Python com a mesma regex terminada em
`(?![A-Za-zÀ-ÿ])` não acharam nada.

## Decisões gerais

- **Tratamento.**
  - Jesus, nas falas da alma, por **vós**, com a maiúscula do original palavra a palavra. O autor escreve
    ora *Vous* (*C'est Vous, ô Jésus, Vous seul*; *par Vous*; *un autre Vous-même*; *Votre Personne*; *la
    Vôtre*; *à Vous consacrées*; *m'identifie avec Vous*), ora *vous*, *votre* (a maior parte). Ficou
    «Vós», «Vossa», «Convosco» onde ele põe maiúscula, e minúscula no resto.
  - A Igreja, interpelada pela alma (*ô sainte Eglise … vous*), também por **vós**: «sejais», «convosco
    me alegrarei».
  - A Igreja falando à alma (*Aie confiance en moi. Ne suis-je pas ta Mère?*) e Jesus falando ao padre
    (*Comment, ô mon fils, pourrais-tu supposer…*) por **tu**, como manda o guia. A alma a si mesma (*tu
    dois, ô mon âme*) também por tu.
  - Na nota 31, o padre Caussette fala ao padre-leitor por *vous*: «vós» («seríeis vós», «dizem-vos as
    boas almas»). Na nota 18, Bossuet fala aos fiéis por *vous*: «que respondeis vós?».
  - Maiúsculas de reverência seguidas: *en dehors de Lui* → «fora de Si»; *un autre Lui-même* → «um outro
    Ele mesmo»; *C'est Elle qui*, *qu'Elle* (a Igreja) → «Ela».
- **Itálico do autor**, conferido nas 29 páginas do scan, como na Primeira parte. Além do latim e dos
  títulos, foram marcadas todas as ênfases visíveis na imagem. Entre elas:
  - a *Résolution* inteira, em itálico no livro;
  - V.3, I: *Le culte public, social, officiel*; *substantielle et vivante*; *C'est un Dieu qui loue
    Dieu*; *Sacrifice*, *Sacrements*, *entourer*, *continuer*; *Elle prélude ainsi à son occupation
    éternelle*; *se divinise*;
  - II: *strictement*; *vous désirez que ma bonne volonté vous offre davantage*; *profitent*; *nourriture
    aussi saine…*; *Cycle liturgique*; *même ordre d'idées*; *grâce spéciale*; *il saisit mon être tout
    entier*; *événement présent…*; *Vie Eucharistique*; *Vie de l'Eglise et la Vôtre*; *entrer en
    participation active…*; *un sujet d'oraison*, *Visites au Saint Sacrement*, *Lectures privées*;
    *quiétisme*; *ne saurait dispenser de l'Oraison du matin*; *Sentimentalisme*, « *Pieuseté* »; *à leur
    volonté*; *but unique*; *Faire mourir le vieil homme…*; *pénétré d'esprit liturgique*;
  - III: *S'unir*; *part active*; *plus directe*; *Ambassadeur*; *un autre Vous-même*; os três
    princípios (o enunciado inteiro de cada um, em itálico no livro); *Chef et la Vie*; as duas citações
    de são Paulo; *même* (cinco vezes); *grâce*, *prière*, *Sacrements*; *prière liturgique*, *plus
    puissante*; *le droit*; *me députe au culte…*; *de la race choisie…*; *comme chrétien*; as orações do
    Cânon citadas em francês; *œuvre commune de toute l'Eglise*; *Communion des Saints*; *tout se fait-il
    en commun…*; *charité fraternelle*; Jo 13,35; *fondement*; *m'y ramène constamment*; *Quel amour pour
    vous…*; *la perfection de chacun de vos enfants*; *elle est aussi ma prière* e o resto do parágrafo;
    *elle ne fait qu'un*; *Pater*; *consacrée à louer Dieu*; *tous les besoins de mes frères*; *la
    louange*; *charitable, fraternelle et catholique*; *m'initier à la louange divine…*; *comme ayant
    autorité*; *à ma foi*; *Où donc trouveras-tu…*; *C'est avec ma Mère que je prie*; *dédoublement*; *la
    personne même*; *s'ajoute*; *C'est l'Église qui les met sur mes lèvres*; *Par moi l'Eglise s'unit…*;
    *action mystérieuse…*; *médiateur*; *Dieu attend de moi…*; *Dieu exige*; *Quel stimulant…*; *tous les
    membres n'ont pas les mêmes attributions*; *but principal*; *de toute éternité*; *exercer par moi*;
    *plus grande que la création de l'univers*; *identification*; *Mon Corps, Mon Sang*; *je veuille*;
    *votre âme est liée à mon âme*; *se fusionne avec la mienne*; *chaque Messe*; *remettre en relief à
    mes yeux*; *aussi divin que celui de créer*; *Fiat*; a fala de Jesus (*je tolère que … « Contre-Christ
    »*, *prendrait ma place*, *oublier*, *te revêtir de moi*, *seule*, *aussitôt*, *accepter froidement …
    ma colère!*); *interdit*; *alternative de la piété ou de l'imposture*; *m'exprimer*; *ce que tu ne
    penses pas…*; *résolu*; *hypocrisie*; *vain simulacre*; *m'invitent à scruter mon cœur…*; *vous
    imiter par la Vie intérieure*; *me revêtir de Jésus-Christ*; *Jésus crucifié*; *piété commode*;
    *vertus bourgeoises*; *certains moyens*; *la même fin*; *coupable*; *enseignement de l'Eglise et de
    ses Saints*; *chacune*; *grâce actuelle*; *C'est l'Eglise qui sollicite cette grâce*; *Et lorsque,
    résolus…*; *je veux profiter de ces grâces*; *chacun*; *ouvrirai largement…*; *identifier avec les
    vôtres…*; *m'unis comme simple chrétien*; *Ambassadeur*; *par la Prière officielle*; *Apostolat de
    l'exemple*;
  - nas notas: *a fortiori* (notas 6 e 31); na nota 9, *telle grâce*, *geste individuel*, *geste de
    l'Eglise*, *de quelque manière*.
  - Onde o português desloca a palavra grifada, o itálico vai com ela: *Apelais _para a minha fé_*;
    *quando _só_ a fragilidade humana está em jogo* (*seule*).
- **Negrito.** Este trecho, diferente da Primeira parte, usa **negrito** (tipo grosso) como ênfase,
  muitas vezes dentro de frases em itálico: *Membre*, *Ambassadeur*, *Ministre* (na *Résolution*); a
  definição *L'ensemble des moyens … âmes*; *Eternelle Liturgie*; *trait d'union*; *Amour personnifié*,
  *Souffrance personnifiée*; *source première et indispensable*; *Contrefaçons de la Vie liturgique*; a
  enumeração *crainte, espérance … la vertu*; *j'utiliserai Messe … des fidèles*; os rótulos *1er / 2e /
  3e Principe*, com *Membre de l'Eglise*, *comme chrétien*, *Représentant de l'Eglise*, *mandat
  officiel*, *Prêtre*, *Ministre de Jésus-Christ*; *incorporation au Christ*; *d'abord*; *Eglise tout
  entière*; *Erreur profonde*; *à beaucoup plus de titres*; *exigences*; *Cum Ecclesiâ*, *Ecclesia*,
  *Christus*; e, na nota 9, *per se efficacissima*. Marquei com `**…**`, que o `js/app.js` já converte em
  `<strong>`. Ver Dúvidas, 1.
- **Inversão do itálico.** No 3º princípio, *Alter Christus* vem em redondo dentro do enunciado em
  itálico (inversão tipográfica). Ficou assim: «_portanto_ Alter Christus; _e ter por certo…_». Em todos os
  outros lugares, *Alter Christus* e o latim do corpo estão em itálico.
- **Versalete**, mantido em maiúsculas: *GRAND SACRAMENTAL* (nota 9) → «GRANDE SACRAMENTAL». Os nomes de
  autor em versalete nas notas (*BOSSUET*, *S. PET. DAM.*, *DE LUGO*…) foram padronizados em caixa normal,
  como sugere o LEIAME.
- **Latim.**
  - No corpo, em itálico e sem tradução, como o autor deixa (*Sicut erat in principio*, *Cœli enarrant*,
    *Orate fratres*, *persona publica totius Ecclesiæ os*, *in mensuram ætatis plenitudinis Christi*,
    *gaudeamus … diligam*, *Absit*, *Complevit Dominus…*, *Imitamini quod tractatis* etc., *Impone,
    Domine…*). Ver Dúvidas, 2.
  - Nas notas: `[Trad.: …]` nas citações latinas que o autor não traduz nem parafraseia no corpo. São 16:
    notas 12, 17, 22, 27, 28, 29, 31 (duas: santo Agostinho na nota e na continuação), 35, 36, 37, 38,
    39, 40, 41 e 43.
  - Ficaram sem `[Trad.]` as notas cujo latim o próprio autor dá em francês no corpo: 10 e 11 (são Paulo,
    «Assim como, diz ele…»), 15 (Billot, *me députe au culte de Dieu…*), 16 (1 Pd 2,9, *de la race
    choisie…*), 18 (as orações do Cânon, traduzidas no corpo), 24 (*comme ayant autorité*) e 33 (*tous
    les membres n'ont pas les mêmes attributions*). Também as expressões latinas soltas nas notas em
    francês (*per se efficacissima*, *Opus operantis*, *Dominus vobiscum*, *a fortiori*).
  - Nas notas que misturam latim e francês (31), o `[Trad.]` vem logo depois da citação latina e da
    referência dela, e não no fim da nota, para não separar a tradução do texto traduzido.
- **Referências.** Bíblicas no formato do impresso: «Eccli.», «Rom.», «I Cor.», «I Pet.», «Joan.»,
  «Eph.», «Matth.», «Thren.», «Is.», «Lévit.», «I Tim.». Os nomes de santos nas notas, por extenso e em
  minúscula dentro dos parênteses, como na Primeira parte: *S. Pet. Dam.* → «são Pedro Damião»; *S.
  Ambr.* → «santo Ambrósio»; *S. Aug.* → «santo Agostinho»; *S. Joan. Chrysost.* → «são João Crisóstomo»;
  *S. Bern.* → «são Bernardo»; *S. Th.* → «santo Tomás»; *S. Dion. Areop.*, *S. Dionys.* → «são Dionísio
  Areopagita», «são Dionísio»; *S. Greg. Naz.* → «são Gregório Nazianzeno»; *S. Ignat.*, *S. Ignace* →
  «santo Inácio». Também *Card. Billot* → «cardeal Billot»; *D. Gréa* → «Dom Gréa»; *Vén. P. Eymard* →
  «venerável padre Eymard»; *P. Caussette* → «padre Caussette»; *Petr. Bles.* → «Pedro de Blois»;
  *Gulielm. Paris.* → «Guilherme de Paris». Os títulos de obras ficaram na língua do original e em
  itálico (*Orais. fun. de Marie-Thérèse d'Aut.*, *Perf. chrét.*, *Exordium magnum Ord. Cisterc.*, *La
  Sainte Liturgie*, *Méditations sur l'Évangile — Cène*, *Manrèze du Prêtre*, *Opusc.*, *Patr. lat.*,
  *In Lucam*, *De civit. Dei*, *De Euchar.*, *De Sacramentis*…). As abreviaturas bibliográficas latinas
  ficaram (*loc. cit.*, *et seq.*, *Inter dubia opp.*, *Conc. Trid.*, *Cat. Roman.*). As indicações em
  francês foram traduzidas: *1re part., 5e traité, ch. XIX* → «1ª parte, 5º tratado, cap. XIX»; *1re
  partie, LXIIIe jour* → «1ª parte, 63º dia»; *1er jour, 2e discours* → «1º dia, 2º discurso»; *Canon de
  la Messe* → «Cânon da Missa»; *Office de Noël* → «Ofício de Natal»; *Pontifical romain* → «Pontifical
  romano».
- **Aspas.** Angulares do original; dentro da citação de Bossuet (nota 18), que no livro usa « » dentro
  de « », ficaram “ ”, como manda o guia.
- **Pontuação.** O espaço francês antes de «:», «;», «!» e «?» foi retirado. Mantidas as frases sem verbo
  do autor («Abismo entre as tuas funções…»; «Hino imperfeito…») e o ponto final da última frase do
  arquivo, que é pergunta retórica sem «?» no livro.

## Termos

| francês | português | observação |
|---|---|---|
| *Vie liturgique*; *esprit liturgique* | Vida litúrgica; espírito litúrgico | guia; maiúscula como no original |
| *Fonctions liturgiques*; *fonction* | Funções litúrgicas; função | |
| *Membre*; *Ambassadeur*; *Représentant*; *Ministre* | Membro; Embaixador; Representante; Ministro | |
| *Ambassadeur attitré* | Embaixador credenciado | |
| *délégué*; *député*; *mandat officiel* | delegado; deputado; mandato oficial | |
| *dédoublement* | desdobramento | a imagem do embaixador |
| *Cycle liturgique* | Ciclo litúrgico | |
| *Office divin*; *offices* | Ofício divino; ofícios | guia |
| *collectes, épîtres, évangiles* | coletas, epístolas, evangelhos | |
| *oraisons* (da liturgia) | orações | *vos admirables oraisons*: as coletas |
| *oraison du Bréviaire* (nota 14) | oração do Breviário | |
| *Oraison du matin*; *sujet d'oraison* | Oração da manhã; assunto de oração | guia |
| *oraison avancée* (nota 6) | oração adiantada | |
| *pensée mère* | ideia-mãe | duas vezes |
| *trait d'union* | traço de união | |
| *Foyer d'amour infini* | Foco de amor infinito | |
| *Chef* (de Corpo místico) | Cabeça | também *mon divin Chef Jésus-Christ* → «minha divina Cabeça, Jesus Cristo», como no Prelúdio |
| *Bercail* | Redil | |
| *Eglise militante, souffrante et triomphante* | Igreja militante, padecente e triunfante | forma usual em português |
| *Vie cachée, publique, souffrante et glorieuse* | Vida oculta, pública, dolorosa e gloriosa | |
| *Contrefaçons de la Vie liturgique* | Contrafações da Vida litúrgica | |
| *Sentimentalisme*; « *Pieuseté* » | Sentimentalismo; «Beatice» | ver Passagens |
| *grand'messe solennelle* | missa cantada solene | |
| *inhumation* | sepultamento | |
| *Communion des Saints*; *Symbole des Apôtres* | Comunhão dos Santos; Símbolo dos Apóstolos | |
| *puissance d'impétration* | poder de impetração | nota 9 |
| *Frère Convers*; *Salutation Angélique*; *Matines* | Irmão converso; Saudação Angélica; Matinas | nota 6 |
| *bête de somme* | besta de carga | nota 6 |
| *servants de messe* | os que servem à missa | nota 25; «acólitos» seria a ordem menor, que eles não têm |
| *parlementaire* | parlamentário | nota 31: o enviado que negocia com o adversário |
| *ornements sacrés*; *vêtements liturgiques* | paramentos sagrados; vestes litúrgicas | |
| *linges* (sacrés) | linhos | corporais, sanguinhos etc. |
| *fonts baptismaux* | pia batismal | |
| *redoutables mystères* | tremendos mistérios | eco do *tremenda mysteria* |
| *Souverain Prêtre*; *Prêtre éternel*; *Prêtre unique* | Sumo Sacerdote; Sacerdote eterno; Sacerdote único | Cristo |
| *prêtre*; *mes actes de Prêtre* | padre; meus atos de Padre | o leitor (guia: *prêtre* → padre) |
| *prêtres de l'ancienne Loi* | sacerdotes da antiga Lei | |
| *Sacerdoce* | Sacerdócio | |
| *« Sans Christ »*, *« Contre-Christ »*; *Antéchrist* | «Sem Cristo», «Contra-Cristo»; Anticristo | |
| *parti-pris d'infidélités* | propósito deliberado de infidelidades | |
| *vertus bourgeoises*; *piété commode* | virtudes burguesas; piedade cômoda | |
| *lâcheté* | covardia | |
| *Jéhovah* | Jeová | como na Primeira parte |
| *Melchisédech*; *Gethsémani*; *Lac de Tibériade* | Melquisedeque; Getsêmani; Lago de Tiberíades | |
| *saint Bernardin de Sienne*; *saint Pierre Damien* | são Bernardino de Sena; são Pedro Damião | |

## Passagens difíceis e leitura adotada

- **«Elle prélude ainsi à son occupation éternelle».** «Ela preludia assim a sua ocupação eterna», com
  *preludiar* transitivo, que guarda o eco do *Prelúdio* do livro.
- **«Hymne imparfaite … l'hymne parfaite».** *Hymne*, feminino no francês litúrgico, é masculino em
  português: «Hino imperfeito», «o hino perfeito». O *la* de *la chantent* remete ao hino: «o cantam».
- **«en nous le montrant visible en Vous».** «Ao mostrá-lo a nós visível em Vós» (o *le* é Deus).
- **« Pieuseté ».** Palavra pejorativa, entre aspas no livro, para a piedade adocicada e afetada.
  «Beatice» dá em português o mesmo desdém, sem neologismo; «piedosidade» seria decalque sem curso.
- **«ne saurait dispenser de l'Oraison du matin».** «Não pode dispensar da Oração da manhã» (o
  condicional de *savoir* negado vale presente).
- **«Prendre une part active, ce sont les propres paroles de Pie X, et coopérer…».** Mantidas as
  vírgulas do autor, que intercala o inciso no meio da citação do *Motu proprio*.
- **Nota 8, «Le prêtre, le pontife lui-même ne relève comme le simple fidèle que de son caractère de
  chrétien».** *Relever de* = estar sob, agir a título de: «só agem em virtude do seu caráter de cristão».
- **«Ce lien … se resserre d'autant plus que…».** «Estreita-se tanto mais quanto mais…».
- **«je suis le membre du Christ».** O artigo francês não tem valor enfático claro; ficou «sou membro de
  Cristo».
- **«et plus belle, et plus sainte, et plus nombreuse».** Guardado o polissíndeto a partir do segundo
  termo: «mais bela, e mais santa, e mais numerosa».
- **«utilitaire, besogneuse et intéressée».** «Utilitária, necessitada e interessada»: *besogneuse* é a
  piedade que pede; «interessada» sem o tom pejorativo de «interesseira», que o contexto não quer.
- **«C'est donc que vous avez reçu».** «Quer dizer, pois, que recebestes».
- **Nota 31, «laudate de vobis».** «Louvai-o com o que vós sois», porque o próprio Agostinho explica *de
  vobis* pela consciência, a vida e as obras.
- **«N'y a-t-il pas, en effet, identification entre Vous et moi…?»** Mantida a pergunta negativa: «Não
  há, com efeito, identificação entre Vós e mim…?».
- **«C'est tellement Vous qui agissez par moi que…».** «A tal ponto sois Vós que agis por mim, que…».
- **«produire un Enfant de Dieu».** «Um Filho de Deus», com a maiúscula do original; o artigo indefinido
  afasta a confusão com o Filho.
- **«Quoi !»** «Pois quê!».
- **«Abîme entre tes fonctions et celles des prêtres de l'ancienne Loi.»** Frase nominal, guardada:
  «Abismo entre as tuas funções e as dos sacerdotes da antiga Lei.».
- **«m'embusquer dans une piété commode».** *S'embusquer* é a gíria da guerra de 1914 para quem se abriga
  num posto seguro, longe da frente. «Emboscar-se» em português quer dizer outra coisa (armar
  emboscada); ficou «refugiar-me numa piedade cômoda». O matiz militar se perde.
- **«Non seulement Ambassadeur …, mais encore un autre Lui-même, je prétendrais…!»** A aposição pede um
  sujeito expresso em português: «Eu, não somente Embaixador de Jesus crucificado, mas ainda um outro Ele
  mesmo, pretenderia…!».
- **«Arrière les subterfuges, ô mon âme, qui me feraient…».** «Fora com os subterfúgios, ó minha alma,
  que me levariam a considerar…». O autor passa de «mon âme» (vocativo) a «me» (eu) na mesma frase; a
  tradução guarda a passagem.
- **«Je serais d'autant moins excusable de fermer l'oreille…».** «Eu seria tanto menos desculpável, se
  fechasse os ouvidos…, quanto…».
- **«jaloux de répondre à votre attente».** «Zeloso de corresponder à vossa expectativa».
- **Nota 12.** *dum* com valor causal-explicativo: «pois, salvo o mistério da unidade oculta, um só homem
  recebe também todos os Sacramentos».
- **Nota 43, *in quo salietur?*** «Com que se há de salgar?», para evitar a mesóclise.

## Remissões de página

Nenhuma neste arquivo. A frase «La méditation que je ferai plus tard sur les avantages de la Vie
liturgique» remete à seção IV (no arquivo `05-quinta-parte-c.txt`), sem número de página.

## Emendas

Nenhuma. O texto-base confere com a imagem nas 29 páginas. Ficaram como no impresso, segundo o LEIAME:
- nota 43, «I Tim., V, 12» (é 1 Tm 4,12);
- nota 45, «Is., LII, 12» (é Is 52,11);
- nota 43, «S. Th. 22, q. 184» (= 2ª 2ae, q. 184);
- nota 30, «I. Dom. vob.» (provavelmente *l.* [*liber*] *Dominus vobiscum*, o opúsculo XI de são Pedro
  Damião).

## Dúvidas para quem coordena

1. **Negrito.** As págs. 217–245 têm muitas palavras em tipo grosso (lista em Decisões gerais). O guia só
   fala de itálico e de versalete. Marquei `**…**`, que o site já mostra. A tradução da Primeira parte
   não usa negrito (não conferi se o livro o usa ali), e por isso não há precedente. Se se preferir não usar negrito,
   basta tirar os `**` (o texto fica correto). Também se pode passá-lo a itálico, mas em vários lugares o
   negrito está dentro de frases já em itálico e se perderia. **Proposta para o guia (não alterado):**
   «o tipo grosso do autor vai em `**…**`».
2. **Latim do corpo sem tradução.** Várias citações latinas do corpo não têm tradução nem nota do autor:
   *persona publica totius Ecclesiæ os*, *in mensuram ætatis plenitudinis Christi*, *Divisiones gratiarum
   sunt*, *Complevit Dominus…*, *Imitamini quod tractatis…*, *Impone, Domine…*. Segui o guia e as deixei
   sem `[Trad.]`. Se se quiser dar o sentido ao leitor, a proposta é pôr o `[Trad.: …]` logo depois da
   citação, como nas notas.
3. **«Beatice» por « Pieuseté ».** Ver Passagens; a alternativa mais literal seria «Piedadezinha».
