# Heródoto, Histórias: convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md` (vale tudo de lá: nunca mesóclise, um bloco traduzido para cada bloco
do original, as marcas `[c.s]` no mesmo lugar). Texto-fonte e correções: `original/LEIAME.md`. Traduz-se o grego
de Godley (Loeb, 1920), que vai ao lado; a tradução inglesa de Godley serve só para conferir o sentido, nunca de base.
A obra cresce por livros (pedido do Gere: «em partes»): os livros I (Clio) e II (Euterpe); os outros vêm em pedidos
seguintes, com estas mesmas convenções. Ao traduzir um livro novo, acrescentar aqui os nomes e termos dele (o livro II
tem a sua seção no fim).

## Princípio e tom

Português do Brasil culto e fluente, de prosa narrativa: Heródoto conta como quem fala, em frases encadeadas por
«e», «então», «depois disso», com retomadas («Assim foi que…», «Isso é o que dizem os persas»). Manter esse
andamento oral, as repetições e as fórmulas de abertura e fecho dos episódios (são a costura do livro), sem
transformá-lo em prosa acadêmica nem em conversa. Nada de acréscimo explicativo (nem «isto é», nem datas, nem nome
que o grego não dá). Sem palavra rara (o Gere não quer «medrou», «hoste», «ledo»): prefira o vocabulário comum.
Heródoto fala de si na 1ª pessoa («eu sei», «a meu ver», «como ouvi», «não sei dizer»): manter, com o mesmo cuidado
dele em distinguir o que viu, o que ouviu e o que pensa (λέγουσι «dizem», λέγεται «conta-se», ὡς ἐγὼ πυνθάνομαι
«pelo que eu soube», δοκέω «penso», οὐκ ἔχω εἰπεῖν «não sei dizer»).

## Formato

- `traducao/<arquivo>.txt` para cada `original/<arquivo>.txt`, com o mesmo número de blocos (parágrafos separados por
  linha em branco), na mesma ordem. Cabeçalho `# titulo: <título da parte>`. Um parágrafo por capítulo; os oráculos
  em verso fazem bloco à parte, como no original.
- O primeiro bloco do primeiro arquivo de cada livro é o nome do livro: `Α · ΚΛΕΙΩ` → `LIVRO I · CLIO`;
  `Β · ΕΥΤΕΡΠΗ` → `LIVRO II · EUTERPE`.
- As marcas `[5.2]` (capítulo.seção, a numeração usual, dentro de cada livro; o livro é o da parte) ficam no mesmo
  lugar, iguais, no começo da frase correspondente (se a ordem da frase mudar, a marca fica antes da frase que começa
  a seção). O proêmio é `[1.0]`: Godley o imprime no começo do capítulo 1, antes da seção 1; os outros livros não
  têm proêmio.
- Falas entre “ ” (com ‘ ’ dentro), como o Perseus as marca. Itálico `_assim_` para título de obra e palavra grega
  ou estrangeira que fica na língua (Heródoto cita palavras persas, citas, egípcias e as explica: a palavra fica em
  itálico, a explicação é dele).
- Colchetes `[ … ]`: o que Godley imprime entre colchetes (trecho que ele, com outros editores, tem por acréscimo de
  copista) vai entre colchetes também na tradução. Lacuna do original: `…`.
- Oráculos e versos citados (`| ` no original): um verso traduzido por linha `| `, no mesmo número de linhas; verso
  livre e claro (são citações curtas; regra das convenções gerais), com registro nas notas. O tom oracular (enigma,
  imagem, vocativo) fica.

## Nomes

Forma portuguesa usual (a dos livros de história em português; acento pela pronúncia latina, como Plutarco):

- **Lídia**: Creso, Candaules (Mírsilo, para os gregos), Giges, Ardis, Sadiates, Aliates, Átis, Adrasto (frígio,
  filho de Górdias, neto de Midas), Pantaleão, Sandanis, Sardes, o Halis, o Hermo, o Pactolo, o Tmolo, Mermnadas,
  Heraclidas, Agron, Nino, Belo, Alceu.
- **Grécia**: Sólon, Telo, Cléobis e Bíton, Árion de Metimna, Periandro, Trasibulo, Pisístrato, Megacles, Licurgo
  (o de Atenas e o de Esparta), Hipócrates, Pítaco, Bias, Tales de Mileto, Leão e Agesicles (reis de Esparta),
  Anaxândrides, Aríston, Licas, Orestes, Quílon, Glauco de Quios, Pactias, Mazares, Tábalo, Hárpago, Dodona,
  Delfos, Abas, Anfiarau, Trofônio, Bránquidas (Dídimo), Amon; Mileto, Foceia, Esmirna, Cólofon, Priene, Éfeso,
  Clazômenas, Teos, Quios, Samos, Lesbos, Cnido, Halicarnasso, Cária, Lícia, Xanto, Cauno, Pânionion (o santuário
  comum dos jônios).
- **Média e Pérsia**: Déjoces, Fraortes, Ciaxares, Astíages, Mandane, Cambises, Ciro, Hárpago, Mitradates, Espaco
  (Σπακώ; «Cino» na língua grega: Κυνώ), Artembares, Oibares, Histaspes, Dario, Arsames, Ecbátana, pasárgadas
  (tribo; as tribos em minúscula, como os povos), Aquemênidas, magos, citas (Madies, Protótias), masságetas, Tômiris, Espargapises, Araxes, Gindes.
- **Assíria e Babilônia**: Babilônia, Nínive, Semíramis, Nitócris, Labineto, Zeus Belo (o templo de Belo), Milita,
  Eufrates, Tigre, Opis.
- Povos: lídios, persas, medos, jônios, eólios, dórios, gregos (Ἕλληνες; «helenos» só em 1.56–58, onde Heródoto
  separa a raça helênica da pelasga), bárbaros (βάρβαροι: o termo grego para os não gregos; não trocar), pelasgos,
  assírios, babilônios, cários, lícios, caunianos, cretenses, fenícios, cilícios, masságetas, citas. Φωκαιέες (de
  Foceia, na Jônia) → **foceenses**; Φωκέες (da Fócida, na Grécia) → **fócios**. Habitantes de cidade sem gentílico
  usual em português: «os de Quios», «os de Cime». Κύρνος → Cirno (a Córsega; o nome grego fica, por causa do
  oráculo de 1.167.4).
- Deuses: Zeus, Hera, Apolo (o Loxias, Λοξίης, é nome de Apolo nos oráculos: «Lóxias»), Atena (Pronaia), Ártemis,
  Héracles, Afrodite Urânia, Dioniso; os nomes estrangeiros como Heródoto os dá (Milita, Alilat, Mitra).

## Termos fixos

- ἱστορίη (proêmio) → **investigação** («a exposição da investigação de Heródoto»).
- βασιλεύς → **rei**; ὁ βασιλεύς (o persa) → «o rei»; τύραννος, τυραννίς → **tirano, tirania** (a palavra grega não é
  necessariamente pejorativa; Heródoto a usa para o senhor único de uma cidade grega, e também para Giges).
  δεσπότης → senhor; δοῦλος → escravo; δορυφόροι → **lanceiros** (a guarda do rei).
- χρηστήριον, μαντήιον → **oráculo** (o lugar e a resposta); χρησμός → oráculo, resposta; ἡ Πυθίη → **a Pítia**;
  θεοπρόποι → os **enviados** ao oráculo; χρᾶσθαι → consultar (o oráculo), χρᾶν → responder (o oráculo).
- ἡμίονος (o oráculo de 1.55 e 1.91) → **mulo**; αἱ Μοῖραι → as Moiras.
- ὄλβιος → **feliz**; εὐτυχής → **afortunado** (na conversa de Sólon e Creso, 1.30–33, a diferença é o centro: ver
  `revisao.json`); εὐδαίμων → feliz; τὸ θεῖον → **a divindade**; φθονερός → invejoso; νέμεσις ἐκ θεοῦ → «um castigo
  vindo de deus»; ὁ θεός (sem nome) → «o deus» quando é o de um oráculo, «deus» no geral.
- Medidas: στάδιον → estádio; πλέθρον → pletro; ὀργυιή → braça; πῆχυς → côvado (πῆχυς βασιλήιος → côvado real);
  παλαστή → palmo; δάκτυλος → dedo; τάλαντον → talento; μνέα → mina; στατήρ → estáter; μέδιμνος → medimno;
  ἀρτάβη → artaba; χοῖνιξ → quénice; πλίνθος → tijolo; ἡμιπλίνθιον → meio-tijolo.
- Instituições e guerra: ἐκκλησία → assembleia; βουλή → conselho; δῆμος → povo; στρατός, στρατιή → exército;
  στρατηγός → general; ὁπλῖται → hoplitas; ἱππεῖς → cavaleiros; τριήρης → trirreme; πεντηκόντερος → pentecôntera.
- Persas: οἱ Μάγοι → os magos; σατραπηίη → satrapia; ὕπαρχος → governador; ἀγγαρήιον não aparece no livro I.

## Tratamento

Nas falas, tu entre iguais, para o rei e do rei para os súditos, como no grego; vós no plural. «Ó rei» (ὦ βασιλεῦ),
«senhor» (ὦ δέσποτα). Nada de «Vossa Majestade».

## Notas do tradutor

`traducao/notas-<arquivo>.md`: nomes e termos novos, passagens difíceis e a leitura adotada, onde o texto de Godley
pesou (colchetes, lacunas), oráculos e como foram traduzidos. Quem uniformiza no fim lê todas.

## Livro II (Euterpe): nomes e termos

O livro do Egito. Heródoto chama os deuses egípcios pelos nomes gregos (Zeus, Hefesto, Atena, Ártemis, Apolo, Deméter,
Dioniso, Pã, Leto, Tifão) e só às vezes dá o nome egípcio (Amon, Osíris, Ísis, Hórus, Bubástis): traduzir como ele dá,
sem trocar um pelo outro. A identificação é dele («Osíris, que dizem ser Dioniso»), e fica.

- **Reis**: Psamético (Ψαμμήτιχος), Min, Nitócris, Méris (Μοῖρις), Sesóstris, Feros (Φερῶς), Proteu, Rampsinito,
  Quéops, Quéfren, Miquerino, Asíquis, Ânisis, Sabacos, Setos (o sacerdote de Hefesto), Neco, Psâmis, Apríes, Amásis;
  Cambises, Ciro (do livro I). Os doze reis (δυωδεκαρχίη → «os doze reis», «o governo dos doze»).
- **Lugares**: o Egito, o Nilo, o Delta, Mênfis, Heliópolis, Tebas, Sais, Bubástis (a cidade e a deusa), Busíris,
  Buto, Mendes, Naucrátis, Pelúsio (a boca pelusíaca), Canopo (a boca canópica), Elefantina, Siene, Méroe, Tacompso,
  Quêmis (Χέμμις), Papremis, Tônis (o guarda da boca canópica), o lago Méris, o labirinto, a Líbia, a Etiópia e os
  etíopes, a Arábia e os árabes, a Síria Palestina, a Fenícia e Tiro, os colcos, a Cólquida, o mar Vermelho
  (Ἐρυθρὴ θάλασσα), o mar do Norte (ἡ βορηίη θάλασσα: o Mediterrâneo, visto do Egito), o Istro, os nasamões, os
  celtas, os cinetes, Pirene.
- **Gregos e outros**: Hecateu (o historiador), Melampo, Cadmo, Homero e Hesíodo, Helena, Alexandre (Ἀλέξανδρος, o
  filho de Príamo, que nós chamamos Páris: fica Alexandre, como no livro I), Menelau, Príamo, Heitor, Polidamna,
  Telêmaco, Diomedes, os _Cantos cíprios_ (τὰ Κύπρια ἔπεα), Ródopis, Caraxo, Safo, Esopo, Iadmon, Ládice, Polícrates,
  Etearco.
- **Deuses e animais sagrados**: Amon, Osíris, Ísis, Hórus, Bubástis, Ápis (o boi; Ἔπαφος na língua grega →
  Épafo), a fênix, o íbis, o crocodilo (κροκόδειλος; os jônios o chamaram assim, 69.3: a explicação é dele),
  ἵπποι ποτάμιοι → **cavalos do rio** (o nome de Heródoto; ver `revisao.json`), a lontra, o gato (αἰέλουρος), os
  icnêumones (ἰχνεύμων: o mangusto; palavra no vocabulário), o mussaranho, a víbora alada.
- **Termos**: ἱρέες → **sacerdotes**; ἱρόν → **santuário**; νηός → **templo**; ἄγαλμα → **estátua** (a imagem do
  deus); νομός → **distrito** (as divisões do Egito; ver `revisao.json`); νομάρχης não aparece; σχοῖνος → **esqueno**
  (medida egípcia de 60 estádios, 6.3: a explicação é dele); ἄρουρα → **arura** (medida de terra, 168.1); ταριχεύειν,
  ταρίχευσις → **embalsamar, embalsamamento**; πυραμίς → pirâmide; λαβύρινθος → labirinto; ὀβελοί → obeliscos;
  κολοσσοί → colossos; ἀνδρόσφιγγες → esfinges de cabeça humana; βύβλος → papiro; κίκι → óleo de rícino (_kiki_,
  palavra egípcia); οἶνος ἐκ κριθέων → «vinho de cevada»; τὰ γράμματα → as letras (ἱρά → sagradas, δημοτικά →
  populares); οἱ μάχιμοι → **os guerreiros**, com as duas classes, os **calasírios** e os **hermotíbios**; as sete
  classes (γένεα): sacerdotes, guerreiros, vaqueiros, porqueiros, comerciantes (κάπηλοι), intérpretes, pilotos.
  ὁρτή → festa; πανήγυρις → festa (reunião de muita gente); λύχνοκαίη → «a festa das lâmpadas».
- Palavras de outras línguas que Heródoto cita e explica (_bekos_, o pão dos frígios, 2.2; _piromis_, 143.4; _Maneros_,
  79): em itálico, com a explicação dele.

## Livro III (Tália): nomes e termos

O livro de Cambises e de Dario: a conquista do Egito, a loucura de Cambises, Polícrates de Samos, o mago, os sete
persas, o debate sobre o governo, as satrapias e os tributos, os confins da terra (Índia, Arábia), Democedes e a
revolta de Babilônia. O título: `Γ · ΘΑΛΕΙΑ` → `LIVRO III · TÁLIA`.

- **Persas**: Cambises, Ciro, Cassandane (Κασσανδάνη), Esmérdis (Σμέρδις: o irmão de Cambises e o mago, que tem o
  mesmo nome), Patizites (Πατιζείθης, o outro mago), Prexaspes, Otanes (filho de Farnaspes), Fedímia (Φαιδυμίη),
  os sete: Otanes, Aspatines, Gobrias, Intafernes, Megabizo, Hidarnes e Dario, filho de Histaspes; Oibares (o
  cavalariço de Dario; a forma do livro I), Atossa, Artistone, Parmis, Oretes, Mitrobates, Bageu (Βαγαῖος),
  Zópiro (filho de Megabizo); Susa, Ecbátana (também a da Síria, 64.4).
- **Egito e África**: Amásis, Psamenito (Ψαμμήνιτος), Nitétis (Νίτητις), Apríes, Fanes de Halicarnasso, Ápis, os
  amônios e Amon, Oásis (a cidade), os ictiófagos (Ἰχθυοφάγοι: «comedores de peixe» só se Heródoto explicar), os
  etíopes de vida longa (Αἰθίοπες μακρόβιοι), a mesa do Sol, os cartagineses (Καρχηδόνιοι), Cirene, Barca.
- **Gregos**: Polícrates, filho de Éaces, Pantagnoto e Silosonte (Συλοσῶν), seus irmãos; Meândrio, Licareto,
  Carilau; Periandro, Licofron, Melissa, Procles de Epidauro; Corinto, Corcira (Κέρκυρα), Samos, Sifnos e os sifnios,
  Egina e os eginetas, Cidônia (Creta), Hidreia, Trezena, Hermíone; Eupalino de Mégara, Reco, Teodoro de Samos;
  Democedes de Crotona, Califonte, Mílon, Gilo de Tarento, Aristofilides; os lacedemônios (Λακεδαιμόνιοι; Esparta
  quando é a cidade); Arquias; Anacreonte; Píndaro (38.4).
- **Ásia e confins**: os árabes e a Arábia, os indianos (Ἰνδοί) e a Índia, os calátias (Καλλατίαι, 38.4), os
  padeus (Παδαῖοι), os arimaspos, o Erídano, as Cassitérides, o Áces (Ἄκης, o rio do vale); incenso, mirra, cássia,
  canela (κινάμωμον), ládano (λήδανον), estoraque (στύραξ).
- **Termos**: ὁ μάγος → **o mago**; τὰ Μαγοφόνια → «a Matança dos Magos» (nome da festa, 79.3); σατραπηίη →
  **satrapia**; ἀρχή (a província) → governo, província; νομός (a divisão dos tributos, 89–97) → **distrito**, como no
  livro II; φόρος → **tributo**; δῶρα → presentes; τάλαντον Βαβυλώνιον / Εὐβοϊκόν → talento babilônico / euboico;
  ψῆγμα → ouro em pó. No debate (80–82): ἰσονομίη → **igualdade perante a lei**; τὸ πλῆθος ἄρχον, πλῆθος → **o povo**,
  **a multidão** (conforme o tom); ὀλιγαρχίη → oligarquia; μουναρχίη, μούναρχος → monarquia, monarca; τύραννος → tirano.
  κάπηλος (89.3, Dario) → comerciante; δεσπότης → senhor. ὁ ἱπποκόμος → o cavalariço; οἱ δορυφόροι → os lanceiros.
