# Regra Pastoral, de São Gregório Magno: texto latino de trabalho

Arquivos: `parte-1.txt` a `parte-4.txt`. UTF-8, cabeçalho `# chave: valor`, blocos separados por linha em branco. Nada foi traduzido.

## Edição e fonte

- **Edição:** J.-P. Migne, *Patrologia Latina* 77 (Paris, 1849), col. 13–128: *Sancti Gregorii Magni, Romani Pontificis, Regulae pastoralis liber, ad Joannem episcopum civitatis Ravennae*. Migne reproduz o texto dos Maurinos (*Sancti Gregorii Papae I cognomento Magni Opera omnia*, Paris, 1705, t. II), com as notas e variantes deles, que aqui não entram. Domínio público.
- **Transcrição usada:** Documenta Catholica Omnia, `http://www.documentacatholicaomnia.eu/04z/z_0590-0604__SS_Gregorius_I_Magnus__Regulae_Pastoralis_Liber__LT.pdf.html` (o PDF fica em `01p/0590-0604,_SS_Gregorius_I_Magnus,_Regulae_Pastoralis_Liber,_LT.pdf`; o site só responde por `http`). O Wikisource latino («Regulae Pastoralis») traz o mesmo texto, copiado do DCO. É uma digitação do texto de Migne, sem colunas, sem as notas e sem os números alternativos dos capítulos.
- **Fac-símile:** Internet Archive, `bim_early-english-books-1641-1700_1849_77` (PL 77, impressão de 1849), folhas 8 a 65. Cada folha tem duas colunas: folha *n* = colunas 13 + 2(*n* − 8) e 14 + 2(*n* − 8). Para comparar, foram usados também os OCR de duas outras impressões do mesmo volume: `patrologiaecur77mign` e `patrologiaecurs06goog` (Garnier, 1879).

## Como foi conferido (2026-10-27)

1. O texto do DCO foi alinhado palavra por palavra com os três OCR do PL 77 (difflib). De 41.176 palavras, 39.384 batem com pelo menos um OCR.
2. Das que não batem, ficaram como suspeitas: a) as que faltam em todo o vocabulário dos três OCR do volume; b) aquelas em que dois OCR concordam numa outra leitura. Uma a uma, as cerca de 150 suspeitas foram olhadas no contexto. A maior parte eram erros do OCR.
3. **Cada correção abaixo foi conferida na imagem da página** (recortes das folhas, localizados pelas caixas de palavras do hOCR do Internet Archive). Também na imagem foram conferidas, por amostragem, a divisão em parágrafos (a do DCO é a de Migne: a lista de III.1 tem um item por parágrafo, e os capítulos da parte I têm um parágrafo cada) e cerca de 40 palavras suspeitas que estavam certas no DCO.
4. Limites: erro do DCO que dê outra palavra latina válida, num trecho em que os três OCR também falham, pode ter escapado. Pontuação e maiúsculas não foram comparadas sistematicamente.

## Correções (DCO → PL 77, todas vistas na imagem)

Erros de digitação do DCO:

| lugar | DCO | PL 77 |
|---|---|---|
| I.prol | pastibus | passibus |
| II.1 | sollicutidine | sollicitudine |
| II.4 | delinguentibus | delinquentibus |
| II.5 (título) | supsensus | suspensus |
| II.6 | qubius | quibus |
| II.6 | descernere | discernere |
| II.6 | mallus | malus |
| II.6 | Curandam | Curandum |
| II.6 | faciedum | faciendum |
| II.10 | pendere | pondere |
| II.10 | discantur | noscantur |
| III.1 | praedicatiore | praedicatione |
| III.2 | banc | hanc |
| III.4 (título) | subdili | subditi |
| III.10 | quatenos | quatenus |
| III.10 | per durant | perdurant (a PL divide «per-durant» na linha) |
| III.10 | intrarit | intravit |
| III.12 | petractando | pertractando |
| III.13 | durerunt | duruerunt |
| III.13 | confuderis | contuderis |
| III.14 | abmonendi | admonendi |
| III.19 | infimitates | infirmitates |
| III.20 | abundatia | abundantia |
| III.23 | benorum | bonorum |
| III.23 | egregins | egregius |
| III.25 | babitaculum | habitaculum |
| III.28 | integritare | integritate |
| III.28 | preadicit | praedicit |
| III.31 | descendant | descendunt |
| II.3 | coccum his tinctum; his tincto | bis tinctum; bis tincto (2.ª conferência) |
| III.14 | Hine | Hinc (2.ª conferência) |
| III.19 | venire (Gen. III, 14) | ventre (2.ª conferência) |
| III.19 | enimDeo | enim Deo (2.ª conferência) |
| III.24 | `.---Quia` | `. — Quia` (a PL tem um travessão; 2.ª conferência) |

Acréscimos do DCO que não estão na PL, retirados:

- III.9 `Totum 44 spiritum`: o «44» é o número de página da edição maurina, impresso em negrito no meio da linha (2.ª conferência).
- III.24 `debriat [inebriat]`, III.25 `debriare [inebriare]`, III.32 `debrietur [inebrietur]`: as glosas entre colchetes são do DCO; a PL traz só *debriat*, *debriare*, *debrietur*.
- II.7 `“πλατος”` → `πλάτος`: a PL não tem aspas e acentua a palavra.

Grafia modernizada pelo DCO, devolvida à da PL (que em todos esses pontos escreve com *n*, junto):

- *numquam* → *nunquam* (9 vezes: II.7, III.11, III.15, III.18, III.19, III.22, III.27, III.28, III.38); *numquid/Numquid* → *nunquid/Nunquid* (III.19, 2 vezes; III.27; III.28); *tamquam* → *tanquam* (III.26); *Quicumque* → *Quicunque* (III.30); *utcumque* → *utcunque* (I.2, III.10, III.18, IV); *nonnumquam/Nonnumquam* → *nonnunquam/Nonnunquam* (III.19, III.29, IV).
- *procul dubio* → *proculdubio* em II.8, II.10, II.11 e III.20, onde a PL junta; ficaram separados II.3 e III.34, como na PL.

Omissão do DCO, reposta (2.ª conferência): **III.33 não tinha o primeiro parágrafo** (de «Aliter admonendi sunt qui, licet minima…» a «…quanto in minimis didicit non timendo peccare», col. 115–116, folha 59): transcrito da imagem e posto antes de «At contra…». O capítulo passou a ter dois parágrafos.

Total: 34 erros de digitação, 5 acréscimos, 1 omissão (um parágrafo) e 26 grafias (22 formas com *m* e 4 *proculdubio*).

## Erros de impressão da PL, mantidos

Estão no fac-símile de 1849 e foram mantidos, porque a regra é corrigir só o erro de digitalização. O tradutor deve ler a forma certa:

- II.4 *costodiae* (= custodiae); II.4 *coneipitur* (= concipitur; o «c» saiu como «e» na impressão de 1849, e as outras impressões trazem *concipitur*);
- III.9 *Pertubatio* (= perturbatio); III.15 *Palbebrae … precedant* (= palpebrae praecedant); III.22 *mores parvorum* (= pravorum); III.24 *apud imperium vulgus* (= imperitum); III.24 *Diriventur* (= deriventur); III.25 *subtrabunt*, uma vez (= subtrahunt); III.26 *eaque in exsilio* (= ea quae); III.27 *solummedo* (= solummodo); III.16 *Nunnunquam*, duas vezes (= nonnunquam); III.16 *aversa asta* (= hasta, como na frase seguinte); III.25 *Redempter* (= Redemptor); III.28 *Amonendi* (= admonendi).

## Segunda conferência (2026-10-27, na revisão da tradução)

Os pontos levantados pelos tradutores foram vistos na imagem (hOCR do mesmo item para achar a folha):

- Corrigidos (erro do DCO): os da tabela marcados «2.ª conferência», o «44» de III.9 e o parágrafo que faltava em III.33.
- Confirmados na PL, mantidos no latim; a tradução segue a leitura indicada:
  - I.11 *a bonis actibus funditur exsors vacat*: a PL traz *funditur*; traduzido como *funditus* («de todo»).
  - II.3 *ad sublimia arma operis invitet*: a PL traz *arma* (sem nota dos Maurinos); traduzido como *armo* («com a espádua da obra»), pelo paralelo com *pectore* e com o *armum* do sacrifício na frase anterior.
  - III.28 *ut incessanter praemia suscipiant*: a PL traz *suscipiant*; traduzido de modo que sirva também a *suspiciant* («a ter sem cessar diante de si os prêmios»).
  - III.36 *longe tamen laboriosius est auditores innumeros ac diversis passionibus laborantes, uno eodemque tempore voce unius et tanta arte vox temperanda est*: a PL é assim; a frase é um anacoluto, não falta texto. A nota *d* dos Maurinos registra a variante *innumeris ac diversis* (de dois manuscritos) e mantém a lição vulgata. A tradução supre o *instruere* da frase anterior.
  - III.38 *Tolerandum nunquam est ut…*: a PL traz *nunquam*; a tradução o lê como pergunta retórica (*nunquam* = *numquid*).

## Divisão e marcas

- Quatro partes, um arquivo por parte. As partes II, III e IV têm na PL um subtítulo, que foi para o `# titulo:` do arquivo (o da IV serve também de título do único bloco `## ` dela).
- Formato (desde a revisão de 2026-10-27, para o site dividir as partes em páginas por capítulo): cada capítulo abre com `## n. título` (o título como na PL, sem o ponto final), e o primeiro parágrafo dele começa com a marca `[parte.n]` (`[I.1]`, `[III.12]`), que o site mostra como «I.1». A carta a João de Ravena abre com a saudação da PL num parágrafo em itálico; o prólogo da parte III, com `## Prologus`; a parte IV, que na PL não tem capítulos, com o seu título em `## `. A numeração vem da ordem: o DCO rotula por engano os capítulos III.18 e III.22 como «CAPUT XXIII».
- Parte III: Migne numera as 36 admoestações com «(Admonitio n.)» no começo do primeiro parágrafo de cada uma. Aqui a numeração vai no título: III.2 a III.35 = admoestações 3 a 36. III.1 contém as admoestações 1 e 2: título «(Admonitio 1–2)» e «(Admonitio 1)» e «(Admonitio 2)» no começo dos dois parágrafos, visíveis, como na PL (na tradução, «(Admoestação 1)» e «(Admoestação 2)»). III.36 a III.40 não são admoestações.
- Ficaram de fora, como no DCO: as notas dos Maurinos, as letras de seção (A–D), os números das páginas da edição maurina na margem e a numeração contínua alternativa dos capítulos («[Al. XIV]»). As referências bíblicas entre parênteses são as de Migne.
- Grafia: a da PL na digitação do DCO, com *ae/oe* no lugar de *æ/œ*, *j* consonântico e *u/v* distintos.

## Totais

Palavras contadas por espaços, títulos incluídos; as marcas e o cabeçalho ficam de fora.

| arquivo | unidades | parágrafos | palavras | colunas PL 77 |
|---|---|---:|---:|---|
| parte-1.txt | carta + 11 capítulos | 12 | 4.607 | 13–24 |
| parte-2.txt | 11 capítulos | 23 | 8.545 | 25–48 |
| parte-3.txt | prólogo + 40 capítulos | 145 | 27.959 | 49–124 |
| parte-4.txt | 1 (sem capítulos) | 2 | 699 | 125–128 |
| **total** | 63 capítulos + carta + prólogo = 65 | 182 | **41.810** | 13–128 |

Coluna da PL em que começa cada capítulo, conferida com o índice do volume («Ordo rerum») e com a imagem nos casos duvidosos:

- I: prol 13, 1 14, 2 15, 3 16, 4 17, 5 18, 6 19, 7 20, 8 21, 9 21, 10 23, 11 23.
- II: 1 25, 2 27, 3 28, 4 30, 5 32, 6 34, 7 38, 8 41, 9 44, 10 44, 11 48.
- III: prol 49, 1 50, 2 52, 3 53, 4 54, 5 56, 6 56, 7 57, 8 58, 9 59, 10 62, 11 64, 12 66, 13 70, 14 71, 15 74, 16 75, 17 77, 18 79, 19 81, 20 83, 21 87, 22 89, 23 92, 24 93, 25 96, 26 99, 27 101, 28 104, 29 107, 30 109, 31 112, 32 113, 33 115, 34 117, 35 119, 36 121, 37 122, 38 123, 39 124, 40 124.
- IV: 125.
