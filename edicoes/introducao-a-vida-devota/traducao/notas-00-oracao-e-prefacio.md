# Notas do tradutor: Oração dedicatória e Prefácio

Arquivo: `traducao/00-oracao-e-prefacio.txt`. Texto-base: `original/00-oracao-e-prefacio.txt` (Boulenger, 1909, texto de 1619, via Wikisource).
Texto de conferência: Annecy, t. III (1893), no OCR de `ferramentas/cache/filoteia/annecy3.txt`, lido parágrafo a parágrafo (Oração dedicatória e Prefácio inteiros).

## O que foi conferido

- **Parágrafos.** 13 no francês e 13 na tradução, mais o bloco do cabeçalho, na mesma ordem.
- **Títulos.** Os 2 títulos `## ` foram traduzidos: «Oração dedicatória», «Prefácio».
- **Marcas e notas.** O arquivo não tem marcas `[X.n]`, como diz o LEIAME. Também não tem chamadas `[n]` nem notas `¤`.
- **Cabeçalho.** Ficou só `# titulo: Oração dedicatória e Prefácio`, como nas outras obras traduzidas. As outras linhas `# ` são do arquivo-fonte.
- **Itálicos e pontuação.** Os dois itálicos foram mantidos (*Palma Christi*; *o ofício de distribuir serve de mérito para receber*). A pontuação também bate: 1 «!», 2 «?», 19 «;» e 6 «:» de cada lado.
- **Tamanho.** Cada parágrafo traduzido tem entre 91% e 110% do tamanho do original.
- **Mesóclise.** O `grep` do CONVENCOES e a varredura em Python com `(?![A-Za-zÀ-ÿ])` não acharam nada.
- **Versos.** Não há versos neste arquivo.

## Decisões gerais

- **Tratamento.**
  - Na Oração dedicatória, Jesus é tratado por **vós** («Animai», «vivei e reinai»).
  - No Prefácio, o leitor é tratado por **tu** («peço-te», «verás», «digo-te»).
  - Filoteia aparece no Prefácio só em 3.ª pessoa.
- **Maiúsculas.**
  - Ficaram as de reverência: *Majestade*, *Salvador*, *Espírito Santo*.
  - Ficaram também as que o autor põe nos nomes do livro e das suas partes: *Introdução*, *Prefácio*, *Partes*.
  - Ficaram ainda *Apóstolos*, *Padres da Igreja*, *Serafins*, *Epístolas canônicas*.
  - *Lecteur* ficou «leitor», em minúscula, como no exemplo do CONVENCOES.
  - *Religieux* ficou «religioso», e *hommes Apostoliques*, «homens apostólicos». A maiúscula do francês aí é hábito tipográfico da época.
  - *saint*, *sainte* ficaram em minúscula: são Paulo, santa Tecla.
  - «VIVE JÉSUS» está em versalete no livro. Ficou em maiúsculas: «VIVA JESUS».
- **A data final.** «À Annecy, le jour sainte Madeleine, 1609» virou «Em Annecy, no dia de santa Madalena, 1609». A cidade ficou na forma francesa, que é a usual em português.

## Termos

| francês | tradução | observação |
|---|---|---|
| *bouquet*, *bouquetière* | ramalhete, florista | «ramalhete», como em *bouquet spirituel* do guia |
| *agencement* | arranjo | |
| *commerce du monde* | trato do mundo | |
| *retraite* (do mundo) | retiro | aqui não é o *retraite spirituelle* do guia |
| *ès ménages* | nos lares | a vida de família, em oposição ao claustro |
| *entreprise* | empresa | «a empresa da vida devota», «essa digna empresa»; o eco ficou |
| *mémoires par écrit* | apontamentos por escrito | «memórias» seria ambíguo |
| *entresuite* | encadeamento | |
| *avis* | avisos | |
| *avertissements* | advertências | |
| *loisir* | vagar | três vezes: «sem nenhuma espécie de vagar», «mais vagar», «o seu vagar» |
| *remontrances* | admoestações | |
| *protestation* | protestação | ver Dúvidas |
| *entière résolution* | inteira resolução | |
| *conduites*; *conduite particulière* | orientações; direção particular | |
| *peine* / *travail* | canseira / trabalho | |
| *faix* / *fardeau* | carga / fardo | mantém os dois substantivos do francês |
| *amatrice ou amoureuse de Dieu* | amante ou enamorada de Deus | |
| *heureusement* | com felicidade; com mais êxito | «felizmente» se leria como «por sorte» |

**Nomes:**

- Glícera, Páusias.
- *Palma Christi*, em latim e em itálico, como no original. É o rícino.
- Ilhas Quelidônias (as *Chelidoniae insulae* de Plínio, na Lícia).
- Piraustas, o inseto do fogo de Plínio e Aristóteles.
- São Dionísio (o Areopagita).
- Timóteo, Tito, Filêmon, Onésimo, santa Tecla, Ápia.
- São Marcos, santa Petronila.
- Barônio e Galônio (Cesare Baronio; Antonio Gallonio, oratoriano).
- A senhora Electa: ficou como nome próprio, como o autor a entende (2 Jo 1).
- Santo Agostinho, Florentina.
- Alexandre, Campaspe, Apeles, Plínio.
- Rebeca, Isaac.

## Passagens difíceis

- **Oração, *le mot que ... je prononce*.** Traduzi «a palavra», que é o lema «Viva Jesus». *Parmi les hasards* → «entre os perigos»: *hasard*, no século XVII, é o risco, o perigo.
- **Oração, *réprouvé*.** Eco de 1 Cor 9,27; Annecy dá a referência na margem. Ficou «reprovado», o termo das Bíblias portuguesas nesse versículo, com o sentido teológico.
- **Oração, *avec eux*.** *eux* são «os outros» a quem o autor mostra o caminho. Daí «com eles», no masculino, e não «com elas» (as almas).
- **Prefácio, P2, *demeura court*.** Ficou «ficou aquém»: Páusias não conseguiu acompanhar a florista.
- **P3, *humeur mondaine*.** «Humor mundano», no sentido antigo de líquido. A imagem continua a das madrepérolas, que não tomam água do mar, e o duplo sentido (líquido e disposição) passa igual em português.
- **P3, *Palma Christi* / *la palme de la piété*.** O jogo de palavras passa: «erva chamada _Palma Christi_» e «a palma da piedade cristã».
- **P3, *mères perles*.** Ficou «madrepérolas»: em português a palavra designa também a ostra perlífera, e guarda a imagem de «mãe».
- **P3, *la presse des affaires*.** «A azáfama dos negócios temporais».
- **P5, *rien d'exact*.** *Exact* tem aqui o sentido de esmerado, trabalhado com apuro, oposto a «sem vagar». Traduzi «nada de acabado», para não sugerir que o livro tem erros.
- **P6, *réduire à l'utilité commune*.** «Fazer servir à utilidade comum», para evitar o galicismo «reduzir a».
- **P8, *Cet âge est fort bizarre*.** *Bizarre* (Annecy: *bigearre*) é, na época, «caprichoso», «difícil de contentar». Ficou «Este tempo é muito caprichoso».
- **P8, *comme saint Marc et sainte Pétronille, de saint Pierre*.** É uma elipse. Pus «o eram», que o português pede: «como são Marcos e santa Petronila o eram de são Pedro».
- **P9, *Combien plus ... bien aimé.*** O francês tem a forma de pergunta exclamativa, mas termina com ponto. O ponto ficou.
- **P9, *comme fait le cinamome, ceux qui le portent*.** «Como faz o cinamomo aos que o levam pela Arábia Feliz»: o cinamomo, como o trabalho, «aviva o coração» de quem o carrega.
- **P10, *la bonne ... la meilleure ... la très bonne*.** Gradação: «a boa maneira ... a melhor ... e a ótima».
- **P11, *en imprima l'amour en son cœur*.** «Imprimiu no seu coração o amor dela»: o amor de Campaspe, no coração de Apeles.
- **P11, *la lui donna en mariage*.** «A deu a ele em casamento». «Deu-lha» soaria lusitano e arcaico.
- **P11, *je me promets de l'immense bonté de mon Dieu*.** «Assim me prometo da imensa bondade do meu Deus»: é o *prometer-se algo de alguém* do português culto, isto é, esperar com confiança.
- **P11, *conduisant ses chères brebis*.** «Conduzindo eu»: o sujeito é o bispo, que dá de beber ao rebanho como Rebeca aos camelos. O «eu» desfaz a ambiguidade com o «ele» (Deus) que vem logo depois.
- **P11, *que je supplie sa Majesté me vouloir octroyer*.** «A qual suplico à sua Majestade que se digne conceder». O antecedente é «a verdadeira devoção».
- **Citações.** São todas do texto do autor e foram traduzidas do francês dele:
  - Agostinho, *Ep.* 266, a Florentina;
  - Plínio, sobre Alexandre e Apeles;
  - Gn 24, Rebeca.

  Não foi acrescentada referência.

## Emendas pela edição de Annecy

Boulenger (no Wikisource) tem três erros de transcrição evidentes. A tradução segue Annecy:

1. **P9, «par a suavité»** → Annecy, «par la suavité»: «pela suavidade».
2. **P11, «en ayant pitiés la lui donna»** → Annecy, «en ayant pitié la luy donna»: «tendo pena dele, a deu». O *s* é erro por vírgula.
3. **P11, «sur less cœurs»** → Annecy, «sur les cœurs»: «nos corações».

E uma emenda de nome:

4. **P11, «Compaspé»** (Boulenger, e as edições antigas) → **«Campaspe»**. Annecy imprime *Campaspé* e explica em nota que *Compaspé* é erro dos impressores: todas as edições de Plínio dão *Campaspe*, assim como Eliano e Luciano. Em português a forma usual é «Campaspe». **Decisão a confirmar**: ver Dúvidas.

Diferenças de Annecy sem efeito na tradução: P8 *leur charge* (Boulenger) × *leurs charges* (Annecy), traduzido «ao seu ofício»; *saint Pierre*, com maiúscula num ponto em Boulenger.

## Remissões de página

Não há.

## Dúvidas para quem coordena

1. **Campaspe × Compaspé.** Adotei «Campaspe», a forma correta e usual, seguindo a nota de Annecy. Se a regra for seguir o texto de 1619 até nos nomes, troca-se por «Compaspe» (duas ocorrências no P11).
2. ***Protestation*.** Usei «protestação» (declaração solene). «Protesto» em português do Brasil soa como objeção. O termo volta na Primeira Parte (I.20, «Protestation authentique...»), por isso convém fixá-lo no CONVENCOES para os outros tradutores. **Proposta: «protestação».**
3. ***Avis*.** Usei «avisos», no sentido antigo de conselhos, como nas velhas traduções portuguesas («avisos espirituais»). O sumário da Primeira Parte («les avis et exercices requis...») pede o mesmo termo. **Proposta para o guia:** *avis* → avisos.
4. ***Loisir*.** Usei «vagar». **Proposta para o guia:** *loisir* → vagar.
5. **Leitor em minúscula.** Segui o exemplo do CONVENCOES («Meu caro leitor»), embora o francês escreva sempre *Lecteur*. Se a casa preferir manter a maiúscula do autor, são cinco ocorrências.
