# Notas do tradutor: A alma de todo apostolado, Segunda parte

Arquivo: `traducao/02-segunda-parte.txt`. Texto-base: `original/02-segunda-parte.txt` (12e édition, 1927,
págs. 47–69 do livro). Conferido contra a imagem do scan, página a página: `ferramentas/cache/alma/rev/062.png`
a `086.png`. A prancha «Regina Apostolorum», que fica entre as págs. 50 e 51, está em `066.png` e `067.png`;
o LEIAME a levou para o fim de `06-epilogo.txt`.

Conferência por script: 130 blocos no original e 130 na tradução. São 1 cabeçalho, 7 títulos `##`,
40 notas `¤ [n]` e 82 parágrafos de prosa, como no LEIAME. Não há parágrafos de continuação de nota `¤`
nem versos `| `. As marcas `[II.1]` a `[II.5]` estão iguais e na mesma ordem. As 40 chamadas `[n]` e as 40
notas `¤ [n]` estão iguais, bloco a bloco. Os 7 títulos foram traduzidos com o prefixo, os números e o
ponto final. Nenhum parágrafo traduzido tem menos de 0,79 do tamanho do original. O 0,79 é a fala curta
«— Em suma, baseais tudo na vida interior?»: só caíram os espaços franceses. As notas 22, 23, 26, 28 e 29
quase dobraram por causa do `[Trad.: …]`. As linhas `# ` do topo foram copiadas, e só o `# titulo:` foi
traduzido («Segunda parte»). Varreduras de mesóclise: o grep do CONVENCOES e a varredura em Python com a
mesma regex terminada em `(?![A-Za-zÀ-ÿ])` não acharam nada.

## Decisões gerais

- **Itálico do autor**, conferido nas 23 páginas do scan, como no Prelúdio e na Primeira parte. O
  texto-fonte não marca o itálico. Ficaram em itálico:
  - todo o latim do corpo e das notas, inclusive o das notas que o livro imprime em redondo;
  - os títulos de obras nas notas: *Hom. Simile est., hom. neg.*, *de Consid.*, *Doct. christ.*, *Cæl. hier.*,
    *Serm.* … *in Cant.*, *Opusc. de perf. vit. spir.*, *Illus. Eccl.*, *Different.*, *De Relig.*, *Vita S.
    Bern.*, *Esprit de S. François de Sales*, os três livros de Timon-David na nota 25, *op. cit.*;
  - as ênfases e citações em francês, todas visíveis na imagem:
    - II.1: *Avant toutes choses, avant toutes œuvres* (Leão XIII) e a carta de Pio X inteira, do
      *Nous apprenons* ao *envers Dieu*;
    - II.2: *Soyez parfait comme votre Père céleste est parfait*; a citação *Ce qu'ils ont vu … aux
      hommes*; *d'abord s'assimiler*;
    - II.3, na fala de Timon-David: *payer de votre personne*, *accumuler en vous la vie d'oraison*,
      *cette proportion*;
    - II.4: *s'y ajoute et n'en diminue pas la nécessité*, *jouissance de l'union à Dieu*, *blessure qui
      ne se ferme pas au sein même d'une activité débordante*, *compenser par la ferveur*;
    - II.5: *vie en soi la plus parfaite, la vie par excellence*, *source*, *habituellement*, *surplus*
      e a frase do padre Matheo Crawley, *L'apôtre est un calice … sur les âmes*.

  Na carta de Pio X, o versalete *NOUS NE VOULONS ABSOLUMENT PAS* fica em redondo no livro, no meio do
  itálico. Na tradução, ficou em maiúsculas, fora dos sublinhados: «…do tempo._ NÃO QUEREMOS DE MODO
  ALGUM _que essa opinião…». A última frase do parágrafo, *Mais la raison d'être…*, é do autor e está em
  redondo no livro, e assim ficou. Não estão em itálico no livro, e não ficaram em itálico na tradução: as
  palavras de são Bernardo *En elle l'homme vit plus purement…*; a de são Bernardo *Si vous êtes sages…*;
  a pintura de são Bernardo *En lui, la contemplation et l'action…*; o resumo de Saint-Jure.
- **Versalete** (aqui em maiúsculas), mantido: *NOUS NE VOULONS ABSOLUMENT PAS*; o princípio *LA VIE
  ACTIVE DOIT PROCÉDER…*; *IL FAUT EN SOUFFRIR, EN GÉMIR…*; *TOUJOURS*; *LA GRACE DU MOMENT PRÉSENT*. Os
  nomes de autor em versalete nas notas (*S. BERN.*, *D. THOM.*) foram padronizados em caixa normal e por
  extenso, como na Primeira parte. Os santos ficaram em minúscula dentro dos parênteses («(são Bernardo,
  …)»), e com maiúscula quando abrem a nota («¤ [20] São Bernardo», «¤ [35] Santo Tomás.»).
- **Tratamento.** Todo *vous* entre pessoas ficou **vós**, como na Primeira parte. São eles: Leão XIII à
  superiora e às suas filhas; a carta de Pio X ao Instituto; Timon-David ao jovem padre, com o adjetivo
  no singular («ficareis espantado», «sereis capaz»); são Bernardo nas notas 14 e 16. Também Jesus a Marta,
  na nota 9 («vós vos inquietais»), e *Soyez parfait* («Sede perfeito», com o singular do francês). Na
  oração final, Deus por **vós** em minúscula, como no original («dai à vossa Igreja»). A *union puissante*
  a quem o autor também diz *vous* ficou «que prodígios de conversão operais». As maiúsculas de reverência
  seguem o original: *Il*, *Lui*, *Lui-même* (Deus, Jesus) → «Ele», «oferecer-Lhe», «em Si mesmo»; *il lui
  plaît* → «lhe agrada»; *Ejus*, *Ipsius* no latim, intactos. Os substantivos também: *Vie intérieure*,
  *Vie active* nos títulos e em II.4 («Essa constância de Vida interior»), *Apostolat*, *Œuvre*, *Critère*,
  *Règle*, *Cercle*, *Patronage*.
- **Latim.** No corpo, todo em itálico e sem tradução, como o autor o deixa (*ad intra*, *Principium
  quod Deus est quæritur*, *sollicitudinis in cogitatu* etc.). Nas notas, foi acrescentado `[Trad.: …]`
  onde o latim vem sem tradução do autor e o corpo só o parafraseia: notas 22 (santo Tomás), 23 (são
  Boaventura), 26 (santo Isidoro), 28 (santo Tomás) e 29 (Godofredo). Ficaram sem `[Trad.]`, pelo
  critério da Primeira parte, as notas cujo latim o próprio autor traduz no corpo: a 5 (Pio X, a carta
  em francês do parágrafo), a 12 (são Bernardo, *En elle l'homme vit…*) e a 27 (Suárez, traduzido quase
  palavra a palavra no parágrafo). O *Exsuperat omnem sensum* (Fl 4,7), dentro da nota 33, em francês,
  ficou sem tradução, como o latim do corpo.
- **Escritura em francês**, traduzida do francês do autor: notas 1–4, 9–11, 15, 24, 30, 39, e no corpo
  *Soyez parfait…* e *Ce qu'ils ont vu…*. Referências no formato do impresso: «Luc», «Matth.», «Joan.», «I
  Joan.», «Cant.», «Sap.» (o *SAP.* em versalete, em caixa normal). *Actes, VI, 4* ficou **«Atos, VI, 4»**:
  é palavra francesa por extenso, e não abreviatura latina como as outras (ver Dúvidas).
- **Diálogo com Timon-David (II.3).** O livro abre cada parágrafo da conversa com «« — » e só fecha as
  aspas no fim da última fala. Ficou igual, com «— colado às aspas: «— Fanfarra, teatro…», e os parágrafos
  sem travessão («Os instrumentos de música…», «Crede-me…», «_Duc in altum_», «Ah! se os padres…») abertos
  só com «.
- **Pontuação.** O espaço francês antes de «:», «;», «!» e «?» foi retirado. Na fala de Timon-David, *à
  toute Œuvre : Paroisse, …, etc., ce que je dis* ficou entre travessões, «a toda Obra — Paróquia, …,
  Círculo militar etc. — o que digo», porque com os dois-pontos a frase não se lia. O fim do capítulo 4
  (*…devront, disons-nous, la fécondité…*) e a exclamação *quels prodiges de conversion vous opérez*
  terminam em ponto no livro, e assim ficaram.

## Termos

| francês | português | onde / observação |
|---|---|---|
| *opérations ad intra* | operações _ad intra_ | II.1 |
| *courses apostoliques* | andanças apostólicas | II.1 |
| *Congrégations enseignantes*; *Institut exclusivement enseignant* | Congregações docentes; Instituto exclusivamente docente | II.1, como as *Milices enseignantes* → «Milícias docentes» da Primeira parte |
| *sécularisation* (das religiosas) | secularização | II.1; as leis francesas de 1901–1904: as religiosas largavam o hábito para continuar a ensinar (a nota 5 fala disso) |
| *ouvrières* | operárias | II.1; *ouvriers évangéliques* → «operários evangélicos» (guia), II.5 |
| *s'enfièvre* | se torna febril | II.1, *Vita securior* |
| *bon plaisir divin* | beneplácito divino | II.1, como na Primeira parte |
| *ici-bas* | neste mundo | II.1, II.2, nota 33 (como no Prelúdio) |
| *débordement*; *débordante* | transbordamento; transbordante | título de II.2; II.2 (o oceano que é Jesus); II.4 (*le débordement de sa charité*, *activité débordante*) |
| *trop-plein*; *excédent*; *surplus* | excedente | II.2 (o reservatório), II.4, II.5 (*surplus*, e o *trop plein* do cálice de Crawley) |
| *prodigalité intarissable*; *munificence inépuisable* | inesgotável prodigalidade; inexaurível munificência | II.2, dois adjetivos diferentes, como no francês |
| *Verbe* / *verbe* | Verbo / verbo | II.2: o Verbo divino e «o nosso verbo» (o espírito interior), como no Prelúdio |
| *tige*; *efflorescence* | haste; eflorescência | II.2 |
| *réservoirs*; *canaux* (*concha*, *canalis*) | reservatórios; canais | II.2, são Bernardo |
| *Patronage de jeunes gens*; *Cercles catholiques*; *Cercle militaire* | Patronato de rapazes; Círculos católicos; Círculo militar | II.3 (guia; Primeira parte) |
| *œuvres de jeunesse* | obras de juventude | II.3 |
| *béquilles* | muletas | II.3 (guia); aqui sem aspas, como no livro |
| *Fanfare*; *cuivres* | Fanfarra; instrumentos de metal | II.3 |
| *tambour de ville* | o tambor do pregoeiro | II.3: o tambor que anunciava os avisos públicos na vila |
| *payer de votre personne* | _pagar com a vossa pessoa_ | II.3 |
| *alliage* | liga | II.3, *au lieu d'alliage … de l'or pur* |
| *suppôts* (de Satan) | sequazes | II.3, como na Primeira parte |
| *s'appellent* (mutuellement) | se reclamam | título de II.4 e *s'appellent, se supposent…* → «reclamam-se, supõem-se…» |
| *oraisons jaculatoires*; *communions spirituelles* | jaculatórias; comunhões espirituais | II.4 (guia) |
| *entretien* (com Nosso Senhor) | colóquio | II.4; na nota 25 (conversa com o cônego), «conversa» |
| *sommet de l'âme* | cume da alma | nota 33 |
| *Dieu des œuvres / œuvres de Dieu* | Deus das obras / obras de Deus | II.4, o quiasmo passa |
| *personnes en charge* | pessoas com encargos | II.4 |
| *foyer* (do zelo) | foco | II.5, *dans son but, son foyer et ses moyens* |
| *américanisme* | americanismo | II.5 (guia) |
| *intronisation familiale du Sacré-Cœur* | entronização do Sagrado Coração nas famílias | II.5 |

Nomes: Nosso Senhor; Marta, Maria; Leão XIII; Pio X; o Doutor angélico; são Boaventura; Ricardo de São
Vítor; são Bernardo, o abade de Claraval; são Gregório; santo Agostinho; o Pseudo-Dionísio; santo
Tomás; o padre Allemand e o cônego Timon-David (guia); o Val-des-Bois (mantido); Marselha; santo
Isidoro; Suárez (ver Dúvidas); Godofredo (*GOD.*, o secretário de são Bernardo, como na Primeira parte);
o padre Saint-Jure; são Francisco de Sales; santa Joana de Chantal; Moulins (mantido); santo Ambrósio; o
padre Léon; o reverendo padre Matheo Crawley (*R. P.* por extenso; prenome como no impresso); são
Dionísio, são Martinho, são Domingos, são Francisco de Assis, são Francisco Xavier, são Filipe Néri,
santo Afonso. *S. S. PIE X* (nota 5) → «Sua Santidade Pio X». O Aveyron ficou em francês.

## Passagens difíceis e leitura adotada

- **II.1, *les théologiens affirment la vie intérieure supérieure en soi à la vie active*.** Predicativo
  à francesa; ficou «afirmam que a vida interior é, em si, superior à vida ativa».
- **II.1, Leão XIII, *si vous ne pouvez conserver et cela et les œuvres*.** «Se não puderdes conservar ao
  mesmo tempo isso e as obras» (*et … et* = «ao mesmo tempo»; *cela* = a vida religiosa).
- **II.1, Pio X, *Nous apprenons qu'une opinion*.** O latim da nota 5 diz *quam pervulgari audimus*:
  «Chega-nos a notícia de que…». *Tant soit peu de crédit* → «o menor crédito»; *l'emporte de beaucoup sur*
  → «está muito acima da».
- **Nota 7.** O francês inverte a ordem do latim (*securior, opulentior* → *plus riche, plus sûre*). A
  tradução segue o francês do autor: «mais rica, mais segura».
- **Nota 8, *de rares travaux*.** Traduz o *circa aliqua* do latim: «a uns poucos trabalhos».
- **II.1, *Vita securior*, o tríplice defeito.** Os glosemas latinos (*sollicitudinis in cogitatu* etc.)
  ficaram em itálico, depois da glosa francesa traduzida, na mesma ordem.
- **II.1, *meurt plus rassuré*.** «Morre mais confiante», que é o *moritur fiducius* da nota; «tranquilo»
  já servira para *repose plus tranquille*.
- **II.2, *Ainsi devons-nous être, en quelque façon, hommes apostoliques qui assumons…*.** O verbo na 1ª
  pessoa (*assumons*) mostra que *hommes apostoliques* é aposto de *nous*: «Assim devemos ser, de algum
  modo, nós, homens apostólicos que assumimos…».
- **II.2, *notre verbe à nous*.** «O nosso verbo, o nosso», para guardar a insistência do *à nous*.
- **Nota 16, *qu'elle s'éloigne de vous sans en sortir*.** O francês do autor traduz livremente o *quæ si
  procedit, non recedat*. A tradução segue o francês: «que ela se afaste de vós sem de vós sair».
- **Nota 14, *le souverain Maître de toutes choses*.** «O soberano Senhor de todas as coisas» (*Maître*,
  como dono e senhor; o latim diz *Parente*).
- **II.2, *il lui sera permis d'en faire part aux autres*.** «Lhe será permitido reparti-las com os
  outros», sem a mesóclise que a construção puxaria.
- **II.3, *Sortes d'entreprises…*.** A frase sem verbo principal do autor ficou sem verbo: «Espécies de
  empresas organizadas…».
- **II.3, *ces hommes mariés même que comptera le Cercle projeté*.** «E até para os homens casados com que
  contará o Círculo projetado».
- **II.3, *si l'ensemble des prêtres … connaissaient*.** O francês faz a concordância pelo sentido, no
  plural. Ficou «se os padres, os religiosos, e até as pessoas de obras, no seu conjunto, conhecessem…».
- **II.3, *le bruit fait peu de bien, et le bien peu de bruit*.** «O barulho faz pouco bem, e o bem pouco
  barulho»: o quiasmo passa.
- **II.4, *Pressé par cette soif … elle revient*.** No livro, *Pressé* está no masculino e o sujeito é
  *elle* (a alma); conferido no scan (pág. 65). A tradução concorda com a alma: «Impelida».
- **II.4, *il lui donne de compenser par la ferveur*.** «Lhe concede _compensar com o fervor_».
- **II.4, *Sustinet, d'être privée*.** O latim vem no meio da frase francesa como glosa: «É … um
  sofrimento para a alma: _Sustinet_, ser privada…».
- **Nota 29, *Deo vocabat*.** O livro imprime *vocabat* (conferido no scan, pág. 62). A frase de Godofredo
  tem *vacabat* («estava livre para Deus», «dava-se a Deus»), que é o que o sentido pede. O latim ficou
  como no impresso, e o `[Trad.]` traduz *vacabat*: «se entregava a Deus».
- **Nota 33, *donc : Exsuperat omnem sensum*.** A doçura está no cume da alma e não suprime as aridezes:
  por isso «ultrapassa todo sentido». Ficou «portanto: _Exsuperat omnem sensum_».
- **II.5, *Contempler la vérité, c'est bien. La communiquer aux autres, c'est mieux encore*.** «É bom … é
  ainda melhor». *Luire sous le boisseau* → «luzir debaixo do alqueire» (Mt 5,15).
- **II.5, *dévorés du désir de se donner*.** Ficou entre vírgulas, ligado aos corações: «reavivai nos
  seus corações, devorados pelo desejo de se darem, uma sede ardente…».

## Remissões de página

Nenhuma neste arquivo. Em II.5, *les paroles du même saint Docteur citées à la fin du chapitre précédent*
remete a II.4 sem dar página: «citadas no fim do capítulo precedente».

## Emendas

O texto-base confere com a imagem nas 23 páginas; nenhuma gralha de OCR. Ficaram como no impresso, e só se
anotam aqui:

- nota 5, *idque ætatis hujus et ingenio necessitatibus postulari*: falta um *et* antes de
  *necessitatibus* (assim no scan); o sentido está no corpo, *l'esprit et les besoins du temps*;
- nota 29, *vocabat* por *vacabat* (ver acima);
- nota 32, *2a 2æ q. 18, a. 2*: o texto citado é da II-II, q. 182, a. 2, mas o livro imprime *q. 18*;
- nota 28, *substractionis* (por *subtractionis*), grafia do impresso;
- II.4, *Pressé* no masculino (ver acima).

## Dúvidas para quem coordena

1. **Nota 33, um parágrafo a mais no livro?** Na pág. 66 do scan, a frase *Sur son lit de mort, à
   Moulins, sainte Jeanne de Chantal…* começa linha nova, recuada, como parágrafo seguinte da nota. O
   texto-base a juntou à nota `¤ [33]`. Mantive um só bloco, para não mudar a contagem; se se quiser
   seguir o livro, basta partir a nota em `¤ [33] Doçura que…` e `¤ No seu leito de morte…`, nos dois
   arquivos.
2. **`[Trad.]` nas notas 5, 12 e 27.** Seguindo a Primeira parte, ficaram sem tradução porque o autor
   as traduz no corpo. A da nota 12 deixa sem tradução o começo, *Hæc (vita) sancta, pura et immaculata*
   («Esta vida santa, pura e imaculada»). Se se preferir dar o `[Trad.]` a toda nota em latim, é fácil
   acrescentar.
3. ***Actes* → «Atos».** As outras referências ficaram como no impresso («Luc», «Matth.», «Sap.»).
   *Actes* é a palavra francesa por extenso e foi traduzida. Se se quiser manter o impresso à letra, é
   trocar por «Actes».
4. **Suárez.** O livro escreve *Suarez*, sem acento, à francesa. O guia manda manter os sobrenomes em
   francês, mas o nome é espanhol e em português corre «Suárez». Fiquei com «Suárez».
5. **Nota 25, endereço.** *L'Œuvre de la Jeunesse Timon-David* virou «Obra da Juventude Timon-David»;
   *Mignard frères* e os endereços (*30, rue du Camas*; *26, rue Saint-Sulpice*) ficaram em francês.
6. **Proposta para o guia (não alterado):** registrar *débordement* → «transbordamento» e *trop-plein*,
   *surplus* → «excedente» (a imagem do reservatório e do cálice volta no livro), e *s'appeler
   mutuellement* → «reclamar-se mutuamente».
