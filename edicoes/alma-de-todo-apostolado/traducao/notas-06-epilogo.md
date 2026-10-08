# Notas do tradutor: A alma de todo apostolado, Epílogo e prancha «Regina Apostolorum»

Arquivo: `traducao/06-epilogo.txt`. Texto-base: `original/06-epilogo.txt` (12e édition, 1927). O Épilogue
ocupa as págs. 291–292 do livro. A prancha «Regina Apostolorum» fica fora da paginação, entre as págs. 50
e 51; o LEIAME a levou para o fim deste arquivo. Os dois foram conferidos contra a imagem do scan:
`ferramentas/cache/alma/rev/308.png` e `309.png` (Épilogue) e `066.png` e `067.png` (prancha).

Conferência por script: 18 blocos no original e 18 na tradução. São 1 cabeçalho, 2 títulos `##` e 15
parágrafos, como no LEIAME. Não há marcas `[X.n]` (o Épilogue e a prancha não as têm), nem chamadas
`[n]`, nem notas `¤`, nem versos `| `. As linhas `# ` do topo foram copiadas, e só o `# titulo:` foi
traduzido («Epílogo; Regina Apostolorum (prancha)»). Nenhum parágrafo traduzido tem menos de 0,88 do
tamanho do original; o 0,88 é o primeiro parágrafo da nota da prancha, mais curto em português
(*constituant un des monuments* → «um dos monumentos»). Varreduras de mesóclise: o grep do CONVENCOES e
a varredura em Python com a mesma regex terminada em `(?![A-Za-zÀ-ÿ])` não acharam nada. O espaço
francês antes de «:» e «;» foi retirado, também no latim.

## Decisões gerais

- **Itálico**, conferido nas quatro imagens.
  - **Épilogue:** o livro não tem nenhum itálico nas duas páginas (ampliei a imagem para conferir *image
    de la vie intérieure*, *image de la vie active*, *porte-Verbe*, a citação de Rohault de Fleury). Não
    há latim nem título de obra. Na tradução, nada ficou em itálico.
  - **Prancha:** as quatro saudações latinas estão em itálico no livro e assim ficaram. A nota sobre a
    imagem (*On pouvait admirer… Michel Ducas et autres*) também está inteira em itálico no livro. É
    extrato das atas do Congresso Mariano, quer dizer, citação. Ficou em itálico, como a carta de Pio X
    em II.1. Ficaram fora do itálico, como estão em redondo no livro:
    - as palavras em versalete, que ficam em maiúsculas: PANAGHIA PARTHENOS, PARTHENOS, NICOPOTAS, e a
      fonte (EXTRATO DAS ATAS DO CONGRESSO MARIANO), com os seus parênteses;
    - a última linha, «(Ver o Epílogo no fim deste volume)», que é do editor do livro.

    As datas entre parênteses, (1904-1905) e (450-453), saem em algarismos redondos no meio do itálico,
    como é costume tipográfico. Ficaram dentro do sublinhado, para o itálico não se partir em pedaços.
- **Título.** *ÉPILOGUE* em maiúsculas no original → «EPÍLOGO», como «PRIMEIRA PARTE». *Regina
  Apostolorum* fica em latim, sem sublinhado, como os outros títulos latinos que o guia manda manter
  («Video», «Sitio»). No livro, ele vem em letra de fantasia, sem itálico.
- **Latim sem `[Trad.: …]`.** As quatro saudações são corpo do texto (legenda da gravura), não nota.
  Segui o guia (§ 3: «Latim no corpo do texto… fica em latim») e a decisão do Prelúdio para os versos
  *Ex quo omnia…*, que ficaram sem tradução. A tradução vai aqui, para o caso de se querer acrescentá-la
  (ver Dúvidas):
  1. *Salve, Virgo Parens…* → «Salve, Virgem Mãe, Colmeia que destila mel; em ti pôs o seu tabernáculo
     o Verbo, que com a palavra ilumina o mundo: levemos contigo, no íntimo, o Verbo do Pai.»
  2. *Salve, clarum Solis justitiæ Speculum…* → «Salve, claro Espelho do Sol de justiça; tanto mais
     fervorosamente manifestemos Jesus pela ação, quanto mais vivermos de Jesus pela contemplação.»
  3. *Salve, Cordis Jesu vivum Receptaculum…* → «Salve, vivo Receptáculo do Coração de Jesus; desta fonte
     divina hauramos por ti o espírito de sacrifício e de oração.»
  4. *Salve, stans juxta Crucem consors sacerdotii…* → «Salve, tu que, de pé junto à Cruz, tens parte no
     sacerdócio; faze que pela Eucaristia Cristo viva em nós, para que sejamos santos que santificam.»
- **Tratamento e maiúsculas de reverência.** Não há fala dirigida a ninguém. As maiúsculas seguem o
  original palavra a palavra: *qu'Il tient*, *qu'Il enseigne* → «que Ele segura», «que Ele ensina»;
  *parler de Lui* → «falar Dele» (como «Nele» na Primeira parte); *Victime sainte* → «a Vítima santa»;
  *Cœur de la très sainte Vierge* → «Coração da Santíssima Virgem» (guia); *Orantes*, *Catacombes*,
  *Adolescent*, *sainte Image* → «Orantes», «Catacumbas», «Adolescente», «santa Imagem». *Elle* (Maria)
  só aparece com maiúscula em começo de frase; *elle* no meio da frase está em minúscula e ficou
  «ela». *l'auguste mère de Dieu*, com *mère* em minúscula, → «a augusta mãe de Deus».

## Termos

| francês | português | observação |
|---|---|---|
| *Épilogue* | Epílogo | guia |
| *Marie Immaculée* | Maria Imaculada | guia |
| *gravure byzantine* | gravura bizantina | |
| *Verbe incarné* | Verbo encarnado | |
| *divin Adolescent* | divino Adolescente | |
| *rouleau de son Evangile* | rolo do seu Evangelho | |
| *Orantes des Catacombes* | Orantes das Catacumbas | as figuras em oração, de braços abertos |
| *porte-Verbe*, *porte-voix* | porta-Verbo, porta-voz | ver Passagens |
| *ostensoir* | ostensório | |
| *débordement* | transbordamento | como no título de II.2 |
| *exposition Mariale* | exposição Mariana | com a maiúscula do original |
| *Académie pontificale romaine d'archéologie* | Academia pontifícia romana de arqueologia | caixa do original |
| *des Blachernes* | das Blaquernas | o santuário de Constantinopla |
| *Pulchérie* | Pulquéria | |
| *Kiew, Nowgorod, Moscou* | Kiev, Novgorod, Moscou | formas usuais no Brasil |
| *Alexis Comnène, Michel Ducas* | Aleixo Comneno, Miguel Ducas | |
| *M. Wuescher-Becchi* | o sr. Wuescher-Becchi | minúscula, como «o sr. Dupont» na Primeira parte |

Nomes mantidos: Rohault de Fleury (sobrenome francês); PANAGHIA PARTHENOS, PARTHENOS, NICOPOTAS (grego
transliterado, em versalete no livro, mantido em maiúsculas e sem tradução).

## Passagens difíceis e leitura adotada

- ***L'idéal parfait de l'apostolat, nous aimons à le méditer…*** O deslocamento do objeto ficou, com o
  pronome retomado: «O ideal perfeito do apostolado, gostamos de meditá-lo». *Tel que nous le montre* →
  «tal como nos mostra», sem o «no-lo», que soaria arcaico.
- ***comme une Eucharistie dont les voiles seraient déchirés.*** O condicional francês de hipótese virou
  imperfeito do subjuntivo: «cujos véus estivessem rasgados».
- ***que sera profonde notre vie intérieure et fécond notre apostolat.*** Guardei a inversão e a elipse
  do verbo: «que será profunda a nossa vida interior e fecundo o nosso apostolado».
- ***elle est le porte-Verbe, le porte-voix, l'ostensoir de Jésus.*** O autor joga com *porte-Verbe* e
  *porte-voix*. O guia dá «portador de Cristo» para *porte-Christ*, mas aqui «portadora do Verbo, a
  porta-voz» perderia o paralelo. Ficou «a porta-Verbo, a porta-voz», decalcado de «porta-voz», que é
  palavra corrente e de dois gêneros. O feminino concorda com Maria, como pede o português; o francês tem
  o masculino, que é o gênero gramatical desses compostos.
- ***répétons-le encore*** → «repitamo-lo ainda uma vez», com ênclise, que é o lugar do pronome no
  imperativo.
- ***Les reproductions de cette célèbre peinture, se retrouvent…*** A vírgula entre sujeito e verbo,
  que está no livro, caiu na tradução.
- ***constituant un des monuments les plus insignes*** → «e um dos monumentos mais insignes», em
  aposição a «objeto de valor incomparável», sem o gerúndio.
- ***EXTRAIT DES ACTES DU CONGRÈS MARIAL.*** Traduzido em maiúsculas, como o resto do versalete do livro:
  «EXTRATO DAS ATAS DO CONGRESSO MARIANO». Se se preferir tratar *Actes du Congrès marial* como título de
  publicação (o guia manda manter os títulos na língua original), a forma seria «(EXTRATO DOS _ACTES DU
  CONGRÈS MARIAL_)».

## Remissões

Nenhuma remissão a número de página. Há duas remissões de lugar, que a mudança da prancha feita pelo
LEIAME tornou inexatas nesta edição. Foram traduzidas como estão no livro (ver Dúvidas):

- Épilogue, 2º parágrafo: *la gravure byzantine… reproduite au milieu de ce livre* → «reproduzida no meio
  deste livro». Nesta edição, a prancha vem logo depois do Epílogo.
- Prancha, última linha: *(Voir l'Epilogue à la fin de ce volume)* → «(Ver o Epílogo no fim deste
  volume)». Continua certa, mas o Epílogo agora vem logo antes.

## Emendas

Nenhuma. O texto-base confere com a imagem nas quatro páginas. Uma divergência de conteúdo, que não é
gralha e ficou como está: o Épilogue data a gravura do *VIe siècle*, e a nota da prancha diz que o
original foi dom da imperatriz Pulquéria (450-453), isto é, do século V.

## Dúvidas para quem coordena

1. **As duas remissões de lugar** (ver acima). Proponho uma destas saídas:
   - deixar como está, porque é fiel ao autor;
   - ou acrescentar ao fim do 2º parágrafo do Epílogo «[Trad.: nesta edição, a gravura e a sua legenda
     vêm logo depois do Epílogo.]», e retirar ou anotar a última linha da prancha, que é do editor e não
     do autor.
2. **Tradução das saudações latinas.** Ficaram sem `[Trad.: …]`, pela regra do guia e pelo precedente do
   Prelúdio. Mas são quatro frases inteiras, que o leitor sem latim não entende, e o autor não as traduz
   em parte alguma. Se se decidir acrescentar, as traduções estão acima, prontas.
3. **Itálico da nota da prancha.** Pus em itálico, como está no livro e como a citação de Pio X em II.1.
   Se se entender que ali o itálico é só o estilo de legenda da prancha, basta tirar os sublinhados dos
   três parágrafos.
