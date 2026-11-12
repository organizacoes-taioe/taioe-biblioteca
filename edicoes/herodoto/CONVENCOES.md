# Heródoto, Histórias: convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md` (vale tudo de lá: nunca mesóclise, um bloco traduzido para cada bloco
do original, as marcas `[c.s]` no mesmo lugar). Texto-fonte e correções: `original/LEIAME.md`. Traduz-se o grego
de Godley (Loeb, 1920), que vai ao lado; a tradução inglesa de Godley serve só para conferir o sentido, nunca de base.
A obra cresce por livros (pedido do Gere: «em partes»): agora o livro I (Clio); os outros vêm em pedidos seguintes,
com estas mesmas convenções. Ao traduzir um livro novo, acrescentar aqui os nomes e termos dele.

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
- O primeiro bloco do primeiro arquivo de cada livro é o nome do livro: `Α · ΚΛΕΙΩ` → `LIVRO I · CLIO`.
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
