# Notas do tradutor: A alma de todo apostolado, Quinta parte, capítulos 1 e 2

Arquivo: `traducao/05-quinta-parte-a.txt`. Texto-base: `original/05-quinta-parte-a.txt` (12e édition, 1927,
págs. 195–216 do livro). Conferido contra a imagem do scan, página a página
(`ferramentas/cache/alma/rev/212.png` a `233.png`).

Conferência por script: 178 blocos no original e 178 na tradução. São 1 cabeçalho, 20 títulos `##`
(com os dois `## * * *`, copiados como estão), 20 notas `¤ [n]`, 41 parágrafos de continuação de nota
`¤` (3 na nota 3, 2 na nota 10, 36 na nota 20, que traz as «dez maneiras» de Rigoleuc) e 96
parágrafos de prosa, o mesmo número do LEIAME. As marcas `[V.1]` e
`[V.2]` estão iguais e no mesmo lugar. As 20 chamadas `[n]` e as 20 notas `¤ [n]` estão iguais e nos
mesmos parágrafos, e os prefixos (`## `, `¤ [n] `, `¤ `, `[V.n] `) batem bloco a bloco. Nenhum bloco
traduzido tem menos de 0,76 do tamanho do original; os mais curtos são títulos e frases breves
(«## QUINTA PARTE», «## III. Como farei Oração?», «Ai de quem se recusa…»), sem omissão. As linhas
`# ` do topo foram copiadas; só o `# titulo:` foi traduzido («Quinta parte, capítulos 1 e 2»).
Varreduras de mesóclise: o grep do CONVENCOES e a varredura em Python com a mesma regex terminada em
`(?![A-Za-zÀ-ÿ])` não acharam nada. Conferido também que nenhum bloco ficou com `_` ou `**` ímpar.

## Decisões gerais

- **Itálico e negrito do autor**, conferidos nas 22 páginas do scan (instrução de quem coordena; como
  na Primeira parte).
  - **Itálico**: todas as ênfases visíveis na imagem foram marcadas `_…_`. Entre elas: as frases
    inteiras *Je veux VIVRE davantage cette thèse* e *Votre approbation de la thèse restera presque
    stérile…*; *requises*; *activité naturelle*, *sa volonté*, *état incompatible avec les exercices
    essentiels de la vie intérieure*; *règlement*, *Plus on est occupé*, *pratiques essentielles*,
    *recueillement*, *dépendance*, *insuffisant*, *coup d'œil*, *sûr, juste, pénétrant*; nos avisos,
    *Règlement*, *volonté ferme*, *oraison*, *Messe, Communion*, *bréviaire*, *liturgiques*, *Examen
    particulier*, *examen général*, *Garde du cœur*, *présence de la Très Sainte Trinité*,
    *communions spirituelles*, *oraisons jaculatoires*, *moment présent*, *étude de l'Ecriture
    Sainte*, *lecture spirituelle*, *la confession hebdomadaire*, *sûrement*, *retraite annuelle*,
    *retraite du mois*; em V.2, *se fixe*, *précise, chaude*, *pratique*, *Moyen de vivre*,
    *Nécessité*, *Oraison ou très grand risque de damnation*, *désirée et poursuivie*, *résultats*,
    *distincte*, *efficacement*, *Salut est moralement assuré*, *dénaturent*, *Pas glissant vers
    l'Abîme*, *j'ai manqué ma Retraite*, *Messe*, *sans fruits*, *péché*, *Bréviaire*, *vigilance*,
    *lectures spirituelles*, *examen*, *Brèches*, *Ruines*; a frase de santo Tomás e a de santa Teresa
    (só as palavras citadas, sem o «diz»), *Se détacher*, *Fixé en Dieu*, *Langage de ma Foi, de mon
    Espérance et de ma Charité*, *malléable*, *souple*, *hausser mon âme jusqu'à la sainteté de
    Jésus*, *logique*, *m'enseignant*, *ma soif*, *déciderai*, *instances*, *Lecture spirituelle*,
    *oraison le lendemain*, *sommairement*, *nette*, *forte*, *saisir*, *INTERLOCUTEUR*, *s'impose*,
    *Présence vivante*, *très nombreuses*, *veux*, *dévorer*, *Vérité*, *un ou plusieurs*, *maintes
    fois*, *sensibilité*, *toujours en mon pouvoir*, *effort*, os quatro *veux* do Sitio, *ma vie*,
    *harmonie*, *recherche*, *contradiction*, *quels points*, *obstacles*, *causes*, *occasions*, os
    *Je veux* e *Je crois, j'aime…* do Volo, *générale*, *appliquer*, *de la journée*, *moyens*, a
    frase de santo Agostinho *Obliger un boiteux…*, *le plus important*, *Ma nourriture est de faire
    la volonté de mon Père*, *Bouquet spirituel*, *obligatoires*, *Garde du cœur*, *plus
    directement*, *tel défaut*, *telle vertu*, *principale*, *un point bien choisi*. Nas notas:
    *Ma résolution d'Oraison…* e *Ma résolution de vie liturgique* (títulos), *persuade fortement*,
    *excellente Oraison*, *Clauso ostio*, *Ego sum resurrectio et vita*, *Voici ce Cœur qui a tant
    aimé les hommes*, *Video*, *Sitio*, *Volo*, *Volo Tecum* (nota 9), *Sitio* (nota 16), *Les Voies de
    l'oraison mentale*, *arrivées*, *Œuvres spirituelles*, *après essai sérieux*, *Nouveau Testament*,
    *Imitation*, *Pater, Ave, Credo*, *décharner*.
  - **Parágrafos inteiros em itálico** no livro, e assim na tradução: o último do Video (*Si
    cependant…*), o último do Sitio antes do exame (*Bien que mon effort…*), o segundo do Volo (*Si
    parfois ce Volo…*) e o primeiro depois do `* * *` (*Quand j'arriverai…*). Neste último, o livro
    imprime *Video*, *Sitio* e *Volo* em redondo dentro do itálico; a tradução faz o mesmo, fechando e
    reabrindo o itálico («_…do_ Video _será…_»).
  - **Negrito**: esta parte, diferente da Primeira, usa muito o negrito (as «résolutions» são impressas
    como roteiro de meditação). Ele foi marcado `**…**`, que o `js/app.js` reconhece: *vraiment* (5°
    princípio), *l'heure du lever*, *ne peut pas*, *aucun résultat*, os dois *Prêtre*, *ma vie avec
    Jésus*, *Lumière*, *Amour*, *Force*, *Aliment*, *assurée par ma fidélité à l'oraison*,
    *impossible*, *Efficace*, *invulnérable*, *sûrement*, *meditatio* e *periissem* (dentro do latim
    do Salmo), *très rare*, *renvoient*, *Confessions routinières, parfois douteuses...*,
    *Sacrilège*, *Ascensio mentis in Deum* (negrito e itálico), *Vrai travail*, *élan*, *Entretien
    cordial / simple / pratique*, *spéciale*, *formans* e *pertractans* (dentro do latim), *Video*,
    *Sitio*, *Volo*, *Volo Tecum* (no parágrafo do viajante), *Avant mon repos*, *L'heure de
    l'oraison est arrivée*, *jeter en présence*, *Vivant*, *Adorable et Aimable*, *Saisi*, *Langage
    de la Foi*, *Je le crois*, *Langage de la Charité Affective*, *Affections*, *Vouloir*, *Langage de
    la Charité Effective*, *Volo* (dentro do parágrafo em itálico), *la résolution*, *la
    Supplication*, *Langage de l'Espérance*, *habitude*, *Vivre de Foi*, *Soif habituelle de Dieu*,
    *recours fréquent*, *habituel*, *Examen particulier* e *de la garde du cœur*. Ver Dúvidas.
  - Os títulos `##` (versalete, negrito ou itálico no livro: *Convictions*, *Résolution d'Oraison*,
    *Je veux être fidèle…*, *Video*…) ficaram sem marca, porque o `## ` já os destaca.
- **Versalete**, mantido em maiúsculas: *VIVRE*, *LEX TUA* (no latim do Salmo), *INTERLOCUTEUR*,
  *OBSÉDÉE PAR LES DISTRACTIONS* (nota 14), *1re MANIÈRE* etc. («1ª MANEIRA»). O título *RÉSOLUTION
  D'ORAISON* vem em maiúsculas no arquivo-fonte e assim ficou («RESOLUÇÃO DE ORAÇÃO»). Na nota 1,
  *P. DESURMONT* (versalete de nome de autor) ficou em caixa normal, «Padre Desurmont», como pede o
  LEIAME (padronizar).
- **Tratamento.**
  - Nas «résolutions», a alma fala a Jesus (e uma vez ao Pai) por *vous* → **vós**. O autor escreve
    ora *Vous* com maiúscula (*C'est Vous qui me parlez*, *Vous me présentez*, *devant Vous*, *Vous
    fatiguer*, *Vous demande*, *avec Vous*), ora *vous* em minúscula (*Je vous exposerais*, *vous
    prierais*, *Je vous dirai*, *vous répéter*, *vers vous*), e quase sempre *votre*, *vos* em
    minúscula (mas *Votre Bonté*, em começo de frase). A tradução segue palavra a palavra, como manda o
    guia para as maiúsculas de reverência: «Sois Vós que me falais», «Eu vos exporia», «a vossa
    Veracidade». Os oblíquos que o português acrescenta seguem o pronome francês correspondente: *Vous
    les exprime … Vous les répète* → «exprime-os a Vós … repete-os a Vós»; *Vous disant que je Vous
    aime* → «dizendo-Vos que Vos amo».
  - A alma a si mesma: *Et toi, mon âme, ne cesse pas…* → «E tu, minha alma, não cesses…».
  - O autor ao leitor, no começo de V.1: *Votre approbation … votre vie intérieure* → «A vossa
    aprovação … a vossa vida interior» (vós).
  - Terceira pessoa com maiúscula, mantida: *Il*, *Lui* (Jesus, Deus) → «Ele», «com Ele», «abrir-Lhe»;
    *le Sien* → «o Seu»; *Celui* → «Aquele», «Daquele»; *Elle* (a Igreja, no último parágrafo de V.2)
    → «Ela». No resumo de Rigoleuc (nota 20), o autor escreve *lui*, *il* em minúscula, e assim ficou.
- **Maiúsculas de substantivos**, seguidas palavra a palavra: *Vie intérieure* / *vie intérieure*,
  *Oraison* / *oraison*, *Garde du cœur* / *garde du cœur* (e *garde du Cœur* na nota 20), *Prêtre* /
  *prêtre*, *Retraite*, *Salut*, *Entretien*, *Langage*, *Interlocuteur*, *Idéal*, *Exemplaire*,
  *Supplication*, *Appendice*, *Economie du Plan divin*, *Abîme*, *Sacrilège* etc.
- **Latim.** No corpo, em itálico e sem tradução, como o autor deixa (*Erue eum…*, *Vigilate*,
  *Orate*, *Sacerdos alter Christus*, *Jam non dicam…*, *Nisi quod lex tua…*, *a fortiori*, *Ascensio
  mentis in Deum*, *Tu, Domine Jesu…*, *Volo placere Deo…*, *Omnia possum*, *In eo qui me confortat*,
  *Exaudi me…*, *A fructibus cognoscetis*); a tradução, quando há, vem nas notas do próprio autor
  (2, 4, 5, 6, 8, 16, 18, 19). Nenhuma nota é inteiramente em latim, e por isso não houve `[Trad.: …]`.
  Ficam sem tradução do autor *Vigilate / Orate*, *Sacerdos alter Christus*, *Clauso ostio*, *Ego sum
  resurrectio et vita* e *A fructibus cognoscetis* (ver Dúvidas).
- **Escritura em francês**: traduzida do francês do autor (notas 2, 4, 5, 18, 19; *Ma nourriture est
  de faire la volonté de mon Père*). Referências no formato do impresso: «Matth.», «Joan.», «Ps.»,
  «Phil.»; «Ps., LXXXV», sem versículo, como está.
- **Números e ordinais.** *1er principe*, *2e principe* → «1° princípio», «2° princípio»; os *1°*,
  *2°* dos avisos e das categorias, iguais (com o sinal de grau, como na Primeira parte); *1re
  MANIÈRE* → «1ª MANEIRA».
- **Pontuação.** O espaço francês antes de «:», «;», «!» e «?» foi retirado. Depois de dois-pontos, a
  maiúscula do francês passou a minúscula onde o que segue é continuação da frase (*cette marche
  logique : Je mettrai* → «marcha _lógica_: porei»; *Video : J'aperçois* → «**Video**: avisto»);
  ficou maiúscula nas falas e listas (*Mon Dieu, je veux…*; *Adoration, reconnaissance…*;
  *Confusion, douleur…*). A frase *ne trouveriez-vous pas que ma conduite en est la contradiction.*
  termina em ponto no livro; como é pergunta, a tradução pôs «?». Mantidos como no livro: o ponto
  final de *Qu'il est beau, ô Jésus, l'Idéal que j'aperçois en Vous.* e o *? sinon parce que…* em
  minúscula (Volo Tecum).
- **«Oraison» e «prière».** *oraison* → «oração» (termo do guia); *prière* → «prece», para guardar a
  distinção que o autor faz (*prière humble et confiante*, *ma prière*, *parfum de prière*, *unir sa
  prière à l'Agonie*), salvo o termo técnico *prière vocale* → «oração vocal».

## Termos

| francês | português | onde / observação |
|---|---|---|
| *Principes et Avis* | Princípios e Avisos | título da 5ª parte |
| *Convictions*; *Principes*; *Avis pratiques* | Convicções; Princípios; Avisos práticos | V.1 |
| *Malheur à qui…* | Ai de quem… | V.1 |
| *s'ingère dans les œuvres* | se intromete nas obras | V.1 |
| *chloroformer les âmes* | cloroformizar as almas | V.1, 4° princípio |
| *point de contention* | nada de tensão | V.1, 6° princípio; como *sans contention* → «sem tensão» na Primeira parte |
| *coup d'œil* | olhar | V.1, 6° princípio |
| *se bien buriner dans l'esprit* | gravar bem a buril no espírito | V.1, 1° aviso |
| *l'heure du lever* | a hora de levantar | V.1 |
| *retraite du mois* | retiro mensal | V.1, 8° aviso |
| *confession hebdomadaire* | confissão semanal | V.1, 7° aviso |
| *préparation éloignée* | preparação remota | V.1, 7° aviso |
| *retraitant(s)* | quem faz o retiro; os que fazem retiro | V.1, nota 3 (como no Prelúdio, sem «retirante» nem «exercitante») |
| *franco* | porte pago | nota 3 |
| *retraite d'Ordination* | retiro de Ordenação | V.2 |
| *Entretien* (cordial, simple, pratique); *entretien* | Colóquio; colóquio | V.2; termo tradicional dos métodos de oração; o mesmo na frase de santa Teresa (*Entretien d'amitié* → «Colóquio de amizade») |
| *s'entretenir avec Dieu*; *entretien agréable* | conversar com Deus; conversa agradável | nota 20 (Rigoleuc); «entreter-se» em português soa a «distrair-se» |
| *Interlocuteur* | Interlocutor | V.2 |
| *Langage de la Foi / de la Charité Affective / Effective / de l'Espérance* | Linguagem da Fé / da Caridade Afetiva / Efetiva / da Esperança | V.2 |
| *Video, Sitio, Volo, Volo Tecum* | iguais, em latim (guia) | títulos e corpo; nota 9: *je veux avec Vous* → «quero com Vós» |
| *Bouquet spirituel* | Ramalhete espiritual | V.2, termo devocional corrente |
| *sujet d'oraison*; *point d'oraison* | assunto de oração; ponto de oração | V.2, nota 10 |
| *fins dernières* | novíssimos | nota 10, nota 20 (7ª maneira) |
| *devoirs d'état* | deveres de estado | nota 10 |
| *idée mère* | ideia-mãe | nota 10 |
| *protestation (de dépendance)*; *protester devant Dieu* | protestação; protestar diante de Deus | V.2; nota 20 |
| *élan* | impulso | V.2 (duas vezes, *nouvel élan*, *élan pris le matin*) |
| *Exemplaire parfait* | Exemplar perfeito | V.2, como *Exemplaire divin* na Primeira parte |
| *mobiles secrets* | motivos secretos | V.2; *mobile* → «motivo» na Primeira parte |
| *tête-à-tête du jugement particulier* | face a face do juízo particular | V.2 |
| *défaillances* | fraquezas | V.2 |
| *stratégiste* | estrategista | V.2 |
| *chutes de surprise* | quedas de surpresa | V.2 |
| *la Chananéenne* | a Cananeia | V.2 |
| *Saint Sacrifice* | Santo Sacrifício | V.2 |
| *Saint Sacrement*; *Très Saint Sacrement* | Santíssimo Sacramento (os dois) | nota 20, último parágrafo; «Santo Sacramento» não é uso português |
| *Très Sainte Trinité* | Santíssima Trindade | V.1 |
| *Cœur sacré* | Coração sagrado | nota 12, com a minúscula do original |
| *Clauso ostio* | _Clauso ostio_ | nota 11 (Mt 6,6) |
| *sécheresses* | securas | nota 20, 5ª maneira |
| *le Jardin* | o Horto | nota 20, 5ª maneira |
| *grains de chapelet*; *chapelet*; *Rosaire* | contas do terço; terço; Rosário | nota 20, V.2 |
| *Revue de son intérieur* | Revista do próprio interior | nota 20, 6ª maneira |
| *l'embarras de l'action* | o tumulto da ação | nota 20, 6ª maneira |
| *décharner* | descarnar | nota 20, 7ª maneira |
| *transport* (dos méritos) | cessão | nota 20, 9ª maneira; termo jurídico, em eco de *qu'il nous a cédé* → «nos cedeu» |
| *coursiers*; *char*; *attelage*; *conducteur* | corcéis; carro; atrelagem; condutor | fim de V.2 |

Nomes: o padre Desurmont, C. SS. R.; santa Teresa; o cardeal Lavigerie; santo Tomás; Bossuet;
Alvarez de Paz e Suarez (sobrenomes como no impresso); santo Agostinho (*S. Aug.*, por extenso, em
minúscula, como corrigido na Primeira parte); Belém, Tabor, Calvário; Dom Vital Lehodey (editora
Lecoffre); o padre Rigoleuc, S. J.; Cassiano; santo Inácio, são Francisco de Sales, são Vicente de
Paulo; Abadia de Sept-Fons, Dompierre-sur-Besbre (Allier). Títulos de livros na língua original, em
itálico: *Ma résolution d'Oraison et de Garde du Cœur*, *Ma résolution de vie liturgique*, *Les Voies
de l'oraison mentale*, *Œuvres spirituelles*; a *Imitation* (citada como livro de leitura, nota 20)
ficou «_Imitação_», como a Primeira parte fez com os clássicos citados em francês.

## Passagens difíceis e leitura adotada

- **V.1, *Amener le cher lecteur à admettre comme frappante la thèse*.** «Levar o caro leitor a
  admitir como impressionante a tese…»; *frappante* aqui é «que impressiona, que salta aos olhos».
- **5° princípio, *A-t-elle véritablement soif …, saisit-elle toutes les occasions …, elle peut être
  en paix*.** A inversão francesa vale por condicional; em português, com perguntas, ficaria truncado.
  Ficou «Se tem verdadeiramente sede…, se com toda a sua boa vontade aproveita…, pode ficar em paz».
  *Dieu les lui réserve* → «Deus as reserva para ela» (evitando «lhas»).
- **6° aviso, *Pieuse étude de l'Ecriture Sainte … doivent trouver place*.** O verbo está no plural
  com sujeito singular (descuido do autor, que talvez pensasse em «Escritura e Novo Testamento»).
  Em português, «deve ter lugar».
- **V.2, *Prêtre, j'ai entendu … Prêtre, je dois vivre*.** «Padre, ouvi…» se leria como vocativo
  («ó Padre»). O *Prêtre* do autor, em negrito, é aposto ao «eu»: ficou «**Padre** que sou, ouvi…» e
  «**Padre** que sou, devo viver…», mantendo a repetição.
- **V.2, *ma vie avec Jésus Principe, Moyen et Fin*.** Vírgulas acrescentadas para o aposto: «a
  minha vida com Jesus, Princípio, Meio e Fim, se desenvolve…».
- **V.2, *Oraison ou très grand risque de damnation*.** «Oração ou grandíssimo risco de condenação»
  (*damnation*, no sentido teológico).
- **V.2, *Pas glissant vers l'Abîme*.** «Passo escorregadio rumo ao Abismo».
- **V.2, *j'ai manqué ma Retraite*.** «perdi o meu Retiro» (o retiro não deu fruto).
- **V.2, *Plus, hélas ! de lectures spirituelles*.** «Acabaram-se, ai!, as leituras espirituais».
  *en attendant le Sacrilège* → «à espera do Sacrilégio».
- **II, *Vrai travail donc que l'Oraison mentale*.** Frase nominal francesa; ficou «Verdadeiro
  trabalho é, pois, a Oração mental».
- **Entretien cordial, *Dieu qui me donne le besoin … de cet entretien, bien plus me l'impose, ne veut
  pas me le faciliter*.** «Deus, que me dá a necessidade … deste colóquio, e mais ainda o impõe a mim,
  não queira facilitá-lo para mim». *à l'entretenir filialement* → «a conversar filialmente com Ele».
- **Nota 8 (santo Agostinho).** O francês do autor diz *très douce … très miséricordieuse … très
  forte*, e não superlativos; a tradução seguiu o francês («muito suave e muito misericordiosa, mas
  contudo muito forte»), não o latim (*mitissima*).
- **Volo, *je regrette*.** Entre *Je crois, j'aime, … je déteste*, ficou «arrependo-me», que é o ato
  da contrição (e não o «lamento» corrente).
- **Volo Tecum, *ma confiance illimitée, folle, dirai-je*.** «louca, ousarei dizer»; *ma soif d'être à
  Vous* → «a minha sede de pertencer a Vós»; *je prie par Vous* → «oro por meio de Vós» (para não
  ler «oro em vosso favor»).
- **Nota 20, 9ª maneira, *ses souffrances dont la seule récompense nous appartient par le transport
  qu'il nous en a fait*.** Os sofrimentos são de Cristo; só a recompensa deles é nossa: «cuja
  recompensa — só ela — nos pertence pela cessão que ele dela nos fez».
- **Nota 20, *(Avignon, 1843, page 17 et suiv.)*.** Página da edição de Rigoleuc, não deste livro:
  ficou «pág. 17 e seg.», sem troca.
- **Fim de V.2, *Nous retenons notre cœur … Nous craindrions*.** «Refreamos o nosso coração…
  Recearíamos alongar…». *persuadé* (singular, *nous* de modéstia) → «persuadido», no singular.

## Remissões de página

- **Nota 2**, *Voir le passage de saint Bernard cité page 77* → «Ver a passagem de são Bernardo citada
  na 3ª parte, cap. 1». Conferido em `ferramentas/cache/alma/final/094.txt` (pág. 77 do livro): é a
  carta a Eugênio III (*Je crains qu'au milieu de vos occupations…*, *Hæ occupationes maledictæ*), em
  `original/03-terceira-parte.txt`, capítulo 1 («Les Œuvres, Moyen de sainteté…»), no trecho «b)
  Danger pour le salut». A Primeira parte também cita essa carta (nota 47), mas a pág. 77 é a da
  Terceira.

## Emendas

- **Video, 2° parágrafo**: o arquivo-fonte traz *C'est Vous qui me parlez et m'enseignez cette
  vérité, Jésus.*; a imagem (pág. 207 do livro, `rev/224.png`) tem ***ô** Jésus*. A tradução segue a
  imagem: «ó Jesus». Convém corrigir o original.
- **Nota 5**: o livro (e também a 15e) imprime *Si votre **foi** n'était l'objet de ma méditation*,
  mas o latim é *lex tua*, e a frase seguinte do corpo diz *Or cette loi va jusqu'à…*. É quase certo
  um erro de composição (*foi* por *loi*). A tradução pôs «Se a vossa **lei** não fosse o objeto da
  minha meditação». Ver Dúvidas.

## Dúvidas para quem coordena

1. **Negrito.** Esta parte usa o negrito como ênfase forte (dezenas de vezes nas «résolutions»), e ele
   foi marcado `**…**`, que o leitor da Biblioteca já reconhece. A Primeira parte não tem `**`. Se se
   preferir não usar negrito na obra, a alternativa é trocar todos os `**…**` por `_…_` (ou retirá-los),
   com perda da hierarquia do autor entre itálico e negrito. Convém registrar a decisão no guia.
2. **Nota 5, *foi* × *loi*.** Adotei «lei». Se se preferir manter o erro do impresso, fica «Se a vossa
   fé não fosse…», com uma nota `[Trad.: …]` ou registro.
3. **Latim do corpo sem tradução do autor** (*Vigilate / Orate*, *Sacerdos alter Christus*, *Clauso
   ostio*, *Ego sum resurrectio et vita*, *A fructibus cognoscetis*). O guia manda deixá-los sem
   tradução, e assim ficaram. Se se quiser dar o sentido: «Vigiai / Orai» (Mt 26,41), «O padre é outro
   Cristo», «Fechada a porta» (Mt 6,6), «Eu sou a ressurreição e a vida» (Jo 11,25), «Pelos frutos os
   conhecereis» (Mt 7,16).
4. **«Colóquio» por *Entretien*.** Escolhi o termo tradicional da oração mental, o mesmo da Primeira
   parte (*tête-à-tête intime avec Jésus-Hostie* → «colóquio a sós»). Os capítulos seguintes (V.3,
   V.4, que são as outras duas «résolutions») devem usar o mesmo termo. Proposta para o guia (§ 5):
   *entretien* → colóquio; *Interlocuteur* → Interlocutor; *Bouquet spirituel* → Ramalhete espiritual;
   *Saint Sacrement* → Santíssimo Sacramento; *fins dernières* → novíssimos.
5. **Remissão da nota 2.** Escrevi «3ª parte, cap. 1», no formato do próprio autor («2e partie, chap.
   II»). Se a obra adotar outro formato para essas remissões, basta trocar.
