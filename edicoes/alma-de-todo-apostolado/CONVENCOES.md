# A alma de todo apostolado, de Dom Chautard — convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md`, com as regras gerais. Este guia acrescenta o que é próprio desta obra e prevalece onde for mais específico. O modelo é `edicoes/santa-teresinha/CONVENCOES.md`.

## 1. Texto-fonte

- Os arquivos são `original/00-preludio.txt` a `06-epilogo.txt`. É a 12e édition (1927), estabelecida do scan (ver `original/LEIAME.md`).
- As linhas `# ` do topo são do arquivo. Traduza só o `# titulo:`.
- **Títulos:** todos começam com `## ` (partes, capítulos «1.», seções «a)» e «I.», as nove classes de almas, «Video», «Sitio»...). Traduza e mantenha o prefixo, os números e as letras.
  - `## * * *` é separação de trecho: copie como está.
  - «Video», «Sitio», «Volo», «Volo Tecum» ficam em latim.
- **Marcas:** `[I.1]` (parte e capítulo) fica igual, no começo do parágrafo.
- **Notas do autor:**
  - `[n]` no texto é a chamada; fica igual, no ponto correspondente da frase traduzida.
  - `¤ [n] ...` é a nota; `¤ ...` sem número é o parágrafo seguinte da mesma nota. Traduza e mantenha os prefixos no mesmo lugar.
- **Itálico:** o texto-fonte **não marca o itálico** (ver LEIAME). Na tradução, ponha em itálico (`_..._`):
  - as citações latinas;
  - os títulos de obras;
  - as palavras estrangeiras.

  As ênfases do autor em francês só se marcam quando forem evidentes ou conferidas no scan. As palavras que o autor pôs em VERSALETE (aqui em maiúsculas: *MULTIPLIER*, *PAR L'EXEMPLE*, *AVANT TOUT*) ficam em maiúsculas.
- **Remissões à paginação do livro:**
  - «Voir note, page 17»;
  - «indiqués pag. 60»;
  - «2e partie, chap. II, pag. 56»;
  - «cité page 77».

  Troque o número da página pelo lugar na obra (parte, capítulo, seção) e registre nas notas.

## 2. Registro e tratamento

- **Tom:** francês eclesiástico do começo do século XX, ardente e direto. O livro é feito de:
  - exclamações e perguntas ao leitor;
  - palavras grifadas;
  - exemplos de padres e de obras;
  - nas «résolutions» da 5ª parte, falas em primeira pessoa dirigidas a Jesus.

  Guarde a força e o ritmo das frases curtas. Não amacie o vocabulário militante do autor («citadelle», «armée de Satan»).
- **Tratamento:** siga o original, passagem por passagem.
  - Deus, a Trindade, Jesus e Maria, quando o autor ou a alma lhes fala por *vous* → **vós**.
    - No **Prélude**, o autor escreve *Vous*, *Votre* com maiúscula: na tradução, **Vós**, **Vosso**, **Vos** com maiúscula também. Nas outras partes, pronomes em minúscula, como no original.
    - Exemplo: «O Dieu très grand et très bon, admirables... sont les vérités que la Foi nous découvre sur Votre vie intime» → «Ó Deus grandíssimo e boníssimo, admiráveis... são as verdades que a Fé nos descobre sobre a Vossa vida íntima».
  - Jesus ou a Igreja falando ao padre ou à alma por *tu* → **tu** («Comment, ô mon fils, pourrais-tu supposer...»; «Aie confiance en moi. Ne suis-je pas ta Mère?»).
  - A alma falando a si mesma («mon âme, tu...») → **tu**.
  - O autor ao leitor: em geral *nous* e «l'apôtre», «l'homme d'œuvres»; quando usa *vous* («Votre approbation de la thèse restera presque stérile...»), **vós**.
- **Maiúsculas de reverência** onde o autor as põe: *Lui*, *Il* (Deus, Jesus) → *Ele*; *Elle* (Maria) → *Ela*. Também *Vie intérieure*, *Garde du cœur*, *Œuvres*: siga o original, palavra a palavra.
- **Nunca mesóclise.** Antes de entregar, rode:

  ```
  grep -n -E -o "[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)\b" traducao/*.txt
  ```

  Não pode sair nada. Cuidado com o futuro das «résolutions»: *je me dirai* → «eu me direi»; *je vous offrirai* → «eu vos oferecerei».

## 3. Latim, Escritura e citações

- **Latim no corpo do texto** (Escritura, liturgia, Padres: *Sine me nihil potestis facere*, *Ut sint unum*, *Age quod agis*): fica em latim, em itálico, como o autor deixa. Quando a nota dá a tradução francesa, traduza a nota.
- **Notas inteiramente em latim,** sem tradução do autor (Pio X, De Lugo, Pedro Damião, Tomás de Aquino, Concílio de Trento...): mantenha o latim. Ponha a tradução portuguesa depois, entre colchetes, marcada «[Trad.: ...]», e registre nas notas do tradutor. Assim o leitor não perde o sentido e o texto do autor fica intacto.
- **Escritura em francês:** traduza do francês do autor, não de uma Bíblia portuguesa. As referências vão no formato dele («Matth., XV, 8» → «Mt., XV, 8» ou «Matth.»: escolha uma forma e mantenha), e os erros do impresso ficam (ver LEIAME).
- **Versos:**
  - O dístico citado em I.3: «Je possède en tout temps et je porte en tout lieu / Et le Dieu de mon cœur et le Cœur de mon Dieu». Traduza **em verso, pelo método do Versificador**: leia `C:\Users\geren\OneDrive\Documentos\Onedrive do Gere\Solar\Editora\Versificador\traducao\MANUAL-DE-TRADUCAO.md` e o `estudo\ESTUDO-DO-RITMO.md` (§ 5). Mantenha:
    - a medida: alexandrinos → dodecassílabos;
    - a rima emparelhada;
    - o quiasmo «le Dieu de mon cœur / le Cœur de mon Dieu».

    Confira com `ferramentas\molde.mjs` até não sobrar ✗ nem ≠.
  - Os versos latinos do Prélude (*Ex quo omnia...*) ficam em latim.

## 4. Nomes

| francês | português |
|---|---|
| Dom Chautard; l'abbé de Sept-Fons | Dom Chautard; o abade de Sept-Fons |
| Cîteaux, cisterciens; Trappistes; Clairvaux | Cister, cistercienses; trapistas; Claraval |
| saint Bernard; saint Benoît; saint Ignace; saint François Xavier | são Bernardo; são Bento; santo Inácio; são Francisco Xavier |
| saint Alphonse (de Liguori); saint Vincent de Paul; saint François de Sales | santo Afonso (de Ligório); são Vicente de Paulo; são Francisco de Sales |
| le saint curé d'Ars; le pauvre d'Assise | o santo cura d'Ars; o pobrezinho de Assis |
| sainte Thérèse; la Vénérable Sœur Thérèse de l'Enfant Jésus; sainte Gertrude | santa Teresa; a Venerável Irmã Teresa do Menino Jesus; santa Gertrudes |
| Pie IX, Pie X, Benoît XV, Léon XIII | Pio IX, Pio X, Bento XV, Leão XIII |
| Abailard; Bossuet; Lacordaire; le P. de Ravignan | Abelardo; Bossuet; Lacordaire; o padre de Ravignan |
| le chanoine Timon-David; l'abbé Allemand | o cônego Timon-David; o padre Allemand |
| le P. Desurmont; le P. Faber; le B. Grignion de Montfort | o padre Desurmont; o padre Faber; o bem-aventurado Grignion de Montfort |
| le général de Sonis; Mgr Favier | o general de Sonis; dom Favier |
| Débora; Goliath; Zachée; Hérode | Débora; Golias; Zaqueu; Herodes |
| Marseille; Lyon; Péking; Nagasaki; New-York | Marselha; Lião; Pequim; Nagasaki; Nova York |

«Saint», com nome, vai em minúscula. Sobrenomes ficam em francês. Títulos de livros citados nas notas ficam na língua original, em itálico.

## 5. Vocabulário

| francês | português |
|---|---|
| l'âme de tout apostolat | a alma de todo apostolado |
| vie intérieure; vie active | vida interior; vida ativa |
| œuvres; homme d'œuvres | obras; homem de obras |
| apôtre; apostolat | apóstolo; apostolado |
| ouvrier évangélique; ouvrier apostolique | operário evangélico; operário apostólico |
| zèle; zélateurs | zelo; zeladores |
| hérésie des œuvres; américanisme | heresia das obras; americanismo |
| garde du cœur | guarda do coração |
| oraison (mentale); oraison du matin | oração (mental); oração da manhã |
| oraisons jaculatoires; communion spirituelle | jaculatórias; comunhão espiritual |
| examen particulier; examen général | exame particular; exame geral |
| vie liturgique; esprit liturgique | vida litúrgica; espírito litúrgico |
| Bréviaire; Office; fonctions liturgiques | Breviário; Ofício; funções litúrgicas |
| direction spirituelle; directeur | direção espiritual; diretor |
| élites | elites |
| « béquilles » | «muletas» |
| porte-Christ; porte-grâce | portador de Cristo; portador da graça |
| Recours habituel à Marie | recurso habitual a Maria |
| Notre-Dame; la Très Sainte Vierge; Marie Immaculée | Nossa Senhora; a Santíssima Virgem; Maria Imaculada |
| le Sacré-Cœur; Jésus-Hostie | o Sagrado Coração; Jesus-Hóstia |
| rayonnement; rayonner | irradiação; irradiar |
| fécondité; fécond | fecundidade; fecundo |
| tiédeur, tiède; ferveur | tibieza, tíbio; fervor |
| patronage (obra de juventude) | patronato |
| prêtre; religieux; séminariste; novice | padre; religioso; seminarista; noviço |
| Prélude; Épilogue | Prelúdio; Epílogo |

## 6. Tipografia

- **Aspas:** as angulares do original, «...»; dentro delas, “...”.
- **Grafia das maiúsculas:** o original escreve *Eglise*, *Evangile*, *A* sem acento nas maiúsculas, por uso tipográfico. Em português, acentue normalmente: *Igreja*, *Evangelho*, *À*.
- **Abreviaturas por extenso:** *S.* → *são*/*santo*/*santa*; *Mgr* → *dom*; *P.* → *padre*; *B.* → *bem-aventurado*; *Vén.* → *venerável*. Nas notas bibliográficas, as abreviaturas de obras ficam como estão.

## 7. Formato de saída

- Cada arquivo vai para `traducao/<mesmo nome>.txt`, com `# titulo:` traduzido («Prelúdio», «Primeira parte», «Quarta parte, capítulo único, a) a c)»...).
- Um parágrafo traduzido para cada parágrafo do original, na mesma ordem, com `## `, `[I.1]`, `[n]`, `¤ [n]`, `¤ ` e `| ` no mesmo lugar.
- As notas do tradutor vão em `traducao/notas-<arquivo>.md`.
