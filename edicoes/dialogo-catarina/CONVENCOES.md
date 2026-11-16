# Diálogo da Divina Providência (Santa Catarina de Sena) — convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md` (regras gerais) e `original/LEIAME.md` (o texto). Este guia prevalece.

## Fluxo
- Original: `original/<tratado>.txt`. Tradução **por capítulo**: `traducao/capitulos/<nnn>.txt` (000 = o
  cabeçalho do códice), com **o mesmo número de blocos, na mesma ordem**: o título `## n. rubrica` traduzido,
  o 1º parágrafo com a marca `[II.26]` igual, um bloco traduzido para cada bloco. Sem cabeçalho `# `.
- `python3 edicoes/dialogo-catarina/trechos.py mostrar 26 30` mostra os blocos do original (leia por aí, um
  trecho por vez; **nunca cole o original na resposta nem em notas**: só o que for preciso, poucas palavras).
- `trechos.py conferir 26 30` confere blocos, marcas, tamanho, mesóclise e aspas; `estado`; `juntar` grava
  `traducao/<tratado>.txt` dos tratados completos.
- Commit e push a cada lote de capítulos fechado (`git add edicoes/dialogo-catarina`).

## Tom
- Italiano do séc. XIV, ditado em êxtase: períodos longos ligados por «e», «e però», «sí che», «cioè», com
  repetições e retomadas. Português do Brasil culto, claro e natural, com o movimento da frase de Catarina; o
  período longo pode ser cortado com ponto e vírgula ou ponto quando ficaria confuso, sem perder as ligações
  lógicas. Sem arcaísmo e sem palavra rara (o Gere recusa palavras como «medrou»). Nunca mesóclise.
- Conectivos recorrentes: «Sí che vedi» → «Vês, pois,» / «Assim vês»; «E però» → «Por isso»; «cioè» → «isto é»;
  «unde» → «por isso, donde»; «anco» → «antes, pelo contrário» (ou «também», conforme o sentido); «pure» →
  «contudo, mesmo assim» (ou «somente»); «veruno, neuno» → «nenhum».

## Tratamento
- Deus Pai fala à alma por **tu** («caríssima filha», «filha minha caríssima», «minha filha»); a alma fala a Deus
  por **tu** («Ó Pai eterno… tu»). Aos homens em geral, ou aos ministros, Deus diz **vós** (o *voi* do texto).
- Pronomes que se referem a Deus em minúscula (eu, me, mim, meu; ele, seu), mesmo onde Fiorilli põe «Io».
  Maiúscula só nos nomes e títulos (Verdade, Verbo, Ponte, Sangue, Pão, Deidade, Bondade quando é nome de Deus).
- Catarina fala de si em 3ª pessoa: «essa alma», «aquela alma», «uma serva de Deus».

## Termos fixos
| italiano | tradução |
|---|---|
| Veritá (Deus, Cristo): la mia Veritá; Veritá etterna; dolce Veritá; prima (dolce) Veritá; somma Veritá | Verdade (maiúscula): a minha Verdade (o Filho); a Verdade eterna; a doce Verdade; a Primeira (doce) Verdade; a suma Verdade. A verdade comum, minúscula |
| el Verbo; unigenito mio Figliuolo | o Verbo; o meu Filho unigênito |
| ponte (Cristo); scaloni; i piedi, el costato, la bocca | a Ponte; os degraus (os três degraus: os pés, o lado, a boca); «costato» = lado (o lado aberto) |
| fiume; annegare | o rio; afogar-se |
| bottiga (do corpo místico, do lado aberto) | adega — ver `revisao.json` |
| discrezione; discreto; indiscreto | discrição; discreto; indiscreto (é o discernimento que dá a cada um o que lhe é devido) |
| caritá; amore; dilezione | caridade; amor; amor (dileção só se vier junto de «amore») |
| cognoscimento di sé (e di Dio); la cella del cognoscimento di sé | conhecimento de si (e de Deus); a cela do conhecimento de si |
| affecto; desiderio; sancto desiderio; ansietato desiderio | afeto; desejo; santo desejo; desejo ansioso (anima ansietata = alma ansiosa) — ver `revisao.json` |
| sensualitá | sensualidade (a parte sensitiva, o amor sensível) — ver `revisao.json` |
| amore proprio; propria volontá; volontá sensitiva | amor-próprio; vontade própria; vontade sensitiva |
| lume (della fede, de l'intellecto, naturale, sopranaturale); luce | lume (da fé, do intelecto, natural, sobrenatural); luz |
| occhio de l'intellecto | olho do intelecto |
| memoria, intellecto, volontá (le tre potenzie) | memória, intelecto, vontade (as três potências) |
| virtú; vizio; defecto | virtude; vício; defeito |
| colpa; pena | culpa; pena (sofrimento ou castigo, conforme o lugar) |
| proximo | próximo |
| salute (dell'anime) | salvação (das almas), nunca «saúde» |
| onore di Dio | honra de Deus |
| Sangue; Pane; sacramento | o Sangue; o Pão; o sacramento |
| sancta Chiesa; corpo mistico; sposa | santa Igreja; corpo místico; esposa |
| Cristo in terra; vicario; pastore | o Cristo na terra (o papa); vigário; pastor |
| ministri; sacerdoti; prelati | ministros; sacerdotes; prelados |
| religione; religiosi; ordine | ordem religiosa, vida religiosa (conforme o lugar); religiosos; ordem |
| servi mercennari; servi fedeli; amici; figliuoli | servos mercenários; servos fiéis; amigos; filhos |
| timore servile; sancto timore | temor servil; santo temor |
| stato unitivo; stato perfecto, imperfecto | estado unitivo; estado perfeito, imperfeito |
| lagrime (i cinque stati di lagrime) | lágrimas (os cinco estados de lágrimas) |
| dimonio, dimoni; dimonia | demônio, demônios |
| gustare; gusto | saborear, provar; gosto, sabor |
| dilecto; consolazione; diletto spirituale | deleite; consolação; deleite espiritual |
| mezzo; col mezzo di | meio; por meio de |
| Deitá; bontá; providenzia; obedienzia | Deidade; bondade; providência; obediência |
| tribulazione; fadiga; pazienzia; impazienzia | tribulação; fadiga (ou trabalho); paciência; impaciência |
| perseveranzia; fortezza; longanimitá | perseverança; fortaleza; longanimidade |
| mondo; carne; dimonio (os três inimigos) | o mundo, a carne e o demônio |
| arbore (da caridade, de morte) | árvore |
| pietre (as virtudes da Ponte); muro | pedras; muro |
| cuore; cuore aperto | coração; coração aberto |
| fornace (della caritá) | fornalha |
| abisso; pelago; mare pacifico | abismo; pélago; mar pacífico |
| figliuolo (da árvore); mirollo; vite, tralci; lavoratore | rebento; medula; videira, ramos; lavrador (os homens, os ministros e o Pai, pelo jogo com Jo 15) |
| actuale (obras, penitência) | exterior (para a Ponte: «em pessoa») |
| molestie; sicurtá; banditore | aflições (nunca «moléstias»); confiança; arauto |
| murare; calcina; marcia; margine; balia; ancudine | assentar (as pedras); argamassa; pus; cicatriz; ama; bigorna |
| rendere el debito | dar o que é devido / pagar a dívida, conforme a frase |
| pazzo d'amore; impazzare (per le creature) | louco de amor; enlouquecer (pelas tuas criaturas) |

## Escritura e citações
- Catarina cita de memória, em italiano ou em latim: traduza **como ela cita**, sem copiar Bíblia portuguesa e sem
  acrescentar referência. Latim no texto: traduza e deixe o latim só se for fórmula breve conhecida (*Deo gratias*),
  em itálico.
- Aspas «» da edição → “ ”; dentro delas ‘ ’. As falas marcadas com — continuam com travessão (—).
- Nomes na forma usual no Brasil: Pedro, Paulo, Domingos, Francisco, Tomás de Aquino, Gregório, Agostinho,
  Jerônimo, Lázaro, Madalena, Maria Madalena.

## Notas do tradutor
Cada lote grava `traducao/notas-<a>-<b>.md` (capítulos a–b): termos novos e a solução; passagens difíceis e a
leitura adotada; **2 ou 3 candidatas a decisão para o Gere** (termo delicado, frase célebre, passagem de dois
sentidos), cada uma com o italiano (poucas palavras), a tradução adotada e uma ou duas alternativas. Termo novo
que se repete: propor nas notas para entrar na tabela acima.
