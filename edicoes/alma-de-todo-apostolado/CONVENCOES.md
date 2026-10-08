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

## 8. Termos fixados na harmonização

Fixados ao harmonizar os onze arquivos (ver `traducao/HARMONIZACAO.md`). Prevalecem sobre as seções anteriores onde estas forem menos precisas.

### Texto e marcação

- **Epígrafe** da página de rosto, antes do `## Prelúdio`, no original e na tradução: «Jesus deve ser **a Vida** das minhas obras. Senão... (Card. Mermillod)».
- **Negrito:** o tipo grosso do livro vai em `**…**` (o `js/app.js` o converte), também dentro de itálico (`**_Dignè_.**`) e nos títulos corridos. Os títulos `## ` não levam marca, embora estejam em negrito no livro. Conferido em todo o scan: nas partes 00 a 04-a o livro só usa negrito nos títulos; o negrito no corpo começa em IV.1 f) e é frequente na Quinta parte.
- **Perguntas e exclamações** que o impresso fecha com ponto ficam com ponto. A inversão francesa de valor condicional («S'agit-il de…, l'amour…») vira condicional em português («Quando se trata de…, o amor…»), não pergunta.
- **`[Trad.: …]`:** nas notas inteiramente em latim cujo sentido o autor não dá no corpo, e ainda, por decisão de quem coordena: nota 1 do Prelúdio (versos *Ex quo omnia*); começo da nota 12 da 2ª parte; as quatro saudações da prancha *Regina Apostolorum*; «Pão e Cinema» (IV.1 f)); as duas remissões trocadas (nota 28 da 3ª parte; Epílogo, «reproduzida no meio deste livro»). No latim do corpo, nada.
- **Remissões** à paginação do livro: no formato «1ª parte, cap. 3», «3ª parte, cap. 1», «5ª parte, cap. 4, IV». Onde o autor dá o capítulo em romanos («chap. III»), fica como ele escreve.
- **Referências bíblicas** como no impresso, com os erros dele (registrados em `ferramentas/cache/alma/revisado/emendas.txt`). Só as abreviaturas francesas viram latinas: *Jér.* → «Jer.», *Sag.* → «Sab.», *Lévit.* → «Levit.». *Actes* → «Atos» e *Jérémie* → «Jeremias» (por extenso) ficam traduzidos.
- **Santos nas referências das notas:** por extenso e em minúscula dentro dos parênteses («(são Bernardo, …)»); com maiúscula quando abrem a nota («¤ [23] Santo Tomás…»).
- **Ordinais:** os numeradores do autor «1°, 2°» ficam com o sinal do livro; os adjetivos ordinais vão com «º», «ª» («1º princípio», «1ª parte», «4º livro», «1ª VERDADE»).
- **Pronomes contraídos** (*no-lo*, *vo-la*, *lho*): evitar; reescrever.

### Tratamento e nomes

- **Falas entre pessoas** por *vous* → **vós** em toda a obra (Leão XIII, Pio X, Timon-David ao jovem padre, o Religioso e a Superiora, o prelado e o médico, são Bernardo a Eugênio III etc.). Não se usa «o senhor».
- **M.** diante de padre secular (Allemand, Timon-David, Olier) → «o padre»; diante de leigo → «o sr.» (o sr. Dupont, o sr. Wuescher-Becchi).
- *Mgr* → «dom» (dom Favier, dom Dupanloup; «Dom Gay» com maiúscula só por abrir item de lista); monges → «Dom» (Dom Sébastien Wyart, Dom Festugière, Dom Guéranger, Dom Vital Lehodey, Dom Gréa).
- Sobrenomes como o autor os escreve: **Suarez**, **Alvarez de Paz** (sem acento); «Grignion de Montfort» (o *Grignon* da pág. 282 é gralha).
- *saint Antoine* (o eremita) → «santo Antão»; *Notre-Dame* (a catedral de Paris) fica em francês.
- *la Sainte Vierge* → «a Santa Virgem»; *la Très Sainte Vierge* → «a Santíssima Virgem».

### Vocabulário

| francês | português | observação |
|---|---|---|
| *suffisance* | suficiência / presunção | «suficiência» quando vem junto de *présomption* (I.2, «tola suficiência» × «louca presunção»; V.3 IV b)) e em *airs de suffisance* («ares de suficiência»); sozinha, «presunção» |
| *présomption*; *présomptueux* | presunção; presunçoso | |
| *entretien* (com Deus, na oração) | colóquio | também *Entretien cordial/simple/pratique* (V.2); *s'entretenir avec Dieu* → «conversar com Deus»; *entretien* entre pessoas → «conversa» |
| *tête-à-tête avec Jésus* | colóquio a sós com Jesus | |
| *oraison*; *prière* | oração; oração | *prière* → «prece» onde o autor junta ou opõe as duas palavras (IV.1 a)) e nas resoluções de V.2 (a prece de súplica) |
| *Interlocuteur*; *Bouquet spirituel* | Interlocutor; Ramalhete espiritual | |
| *fins dernières*; *Saint Sacrement* | novíssimos; Santíssimo Sacramento | |
| *« Pieuseté »* | «Beatice» / «beatice» | maiúscula onde o autor a põe |
| *au muguet* (um Cristo) | «açucarado» | |
| *Galette et Cinéma* | «Pão e Cinema» | com `[Trad.]` que explica a gíria (*galette* = dinheiro) |
| *porte-Christ*; *porte-grâce*; *porte-Dieu* | portador de Cristo; portadora da graça; portador de Deus | concorda com o substantivo a que se refere |
| *porte-Verbe*, *porte-voix* | a porta-Verbo, a porta-voz | Epílogo |
| *Monseigneur* (vocativo) | Senhor Bispo | |
| *rayonner de* | irradiar + objeto direto | «ELE IRRADIA FÉ» |
| *débordement*; *trop-plein*, *surplus*, *excédent* | transbordamento; excedente | |
| *s'appeler mutuellement* | reclamar-se mutuamente | |
| *dévouement*; *guérisseur*; *folle du logis* | dedicação; sanador; louca da casa | |
| *Esprit de Force*; *spirituelle* (de pessoa) | Espírito de Fortaleza; espirituosa | |
| *Apprentissage de la Garde du cœur* | Aprendizado da Guarda do coração | título de V.4, IV, e nota 28 da 3ª parte |
| *honoraires*; *sans-gêne*; *crainte révérentielle* | espórtulas; sem-cerimônia; temor reverencial | |
| *Église militante, souffrante et triomphante* | Igreja militante, padecente e triunfante | |
| *Prêtre* (Cristo; o padre unido a ele) | Sacerdote | *prêtre* (o clero) → padre |
| *sujet(s)* | elemento(s), membro(s) | conforme o contexto |
| *Fête-Dieu* | Corpus Christi | |
| *Exercices spirituels* (santo Inácio) | _Exercices spirituels_ | títulos na língua da obra; exceções, os clássicos que o autor cita em francês no corpo: _Introdução à vida devota_, _Imitação de Jesus Cristo_ / _Imitação_ |

**As nove classes de almas** (IV.1 f)): 1. ENDURECIMENTO; 2. VERNIZ CRISTÃO; 3. PIEDADE MEDÍOCRE; 4. PIEDADE INTERMITENTE; 5. PIEDADE CONSTANTE (*soutenue*); 6. FERVOR; 7. PERFEIÇÃO RELATIVA; 8. HEROICIDADE; 9. SANTIDADE CONSUMADA. Os quatro pontos da direção: **Paz.**, **Ideal.**, **Oração.**, **Renúncia.**
