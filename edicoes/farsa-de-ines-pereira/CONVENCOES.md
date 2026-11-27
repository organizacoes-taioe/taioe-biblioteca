# Farsa de Inês Pereira: convenções da edição

Texto da Copilação de 1562 (fac-símile da BNP, purl.pt/11494, PDF `res-175-a`, pp. 440–454 = fól. CCXIII v.º–
CCXX v.º, «Auto de Ines Pereyra» … «Laus Deo») na grafia brasileira de hoje. Não há folheto avulso conhecido.
O fac-símile (212 MB) e as páginas recortadas ficam fora do git, em `~/.cache/claude-pedidos-2711/farsa-de-ines-pereira/`
(só no notebook); para refazer: baixar o PDF de `https://purl.pt/11494/6/` e `pdftoppm -f 440 -l 454 -r 200`.

## Como o texto foi feito
1. Reimpressão de Hamburgo (1834), tomo III, pp. 121–159: OCR do exemplar de Toronto (`colacao/ocr-1834-toronto.txt`),
   desempatado pelo do exemplar do Google, passado a limpo na grafia de 1834 (`colacao/v1834-A.txt` e `-B.txt`).
2. Colação de 1834 com 1562, coluna por coluna, por dois Sonnet (`colacao/colacao-A.tsv` e `-B.tsv`), e depois
   releitura de todas as 30 colunas de 1562 pelo principal (achou uns 60 pontos que a colação deixou passar,
   sobretudo formas e rubricas).
3. `modernizar.py`: 1834 → grafia de hoje (`grafia.py`: tabela à mão; o resto por regras conferidas no léxico).
   Gera `colacao/moderno-1834.txt`, `sem-decisao.txt` (tem de ficar vazio) e `automaticas.txt` (conferir).
4. `montar.py`: aplica `licoes.py` (as lições de 1562, ~150) e grava `texto.txt`. `publicar.py` divide em dez partes.

## Lição
- Vale 1562 (decisão no `revisao.json`, recomendação aplicada). 1834 só serve de leitura auxiliar.
- Rubricas: as de 1562; saem as que 1834 acrescentou («sai», «vai-se», «à parte», «lê a carta», «lê o sobrescrito»)
  e entram as de 1562 que 1834 tirou («Falado.», «Prossegue.», «Sobrescrito.», «Laus Deo.»).
- Emendas (erro evidente de 1562; segunda decisão do `revisao.json`): «ou marido ou maridinho / tenha o que houver
  mister» (1562 «marinho», «tenho»), «Sirvo allí mi Dios Cupido» (1562 «mis dias»), e «Dai-me vós cá essa chave / e i
  buscar vossa vida» com Inês (1562 sem nome de fala, ficaria com o Moço).
- A pontuação é a de 1834 (1562 quase não pontua), salvo onde muda com a lição.
- Leituras incertas de 1562 em que ficou 1834: «Donaso» (1562 «dona so»), «esfandangado» (1562 «esfandagado»?),
  «saí»/«saí vós i» (1562 «sabi», duas vezes), «Quanto a dizer abraçar» (1562 «quanta»), «Vilha Caslim» (1562 «Castim»?).

## Grafia (como em `../barca-do-inferno/CONVENCOES.md` e `../os-lusiadas/CONVENCOES.md`)
- Muda a maneira de escrever, a forma fica: pera, assi, cousa (mas «coisa» onde 1562 tem «coysa»), dous, mi, sam (= sou),
  perém, milhor, fogir, cospir, curuja, lião, exempro, concrusão, malino, tisouro, ofecial, canteguinha, cerimônias,
  leixar, ereos, amenhã, ajais, creo, veria (= viria), compre (= cumpre), mochacho, cadarrão, estrogirá, vilanzinho,
  Spírito, frágoa, eramá/ieramá/muitieramá, aque d'el-Rei, al (= outra coisa), i (= aí).
- «ũa», «algũa» (1562 «hũa»); «ò» = ao (1562 «oo»), «à» crase; «hi» → «i»; «ora» por «hora» → «hora» (má hora).
- fea/chea/aldea/pea → feia/cheia/aldeia/peia (regra de Os Lusíadas); «mercea» fica (rima rústica de Pero).
- Imperativos em -ae → -ai (dai, ficai); «-ão» átono → «-am» (folgam, gabaram); mesóclises do autor ficam
  (chamá-lo-ei, levar-me-eis, fechá-la-ás, far-lhe-ei).
- Castelhano (o Ermitão, «Mal ferida iba la garza», «Mal me quieren en Castilla») na grafia de 1834, que é a
  corrente; só «ferida» (1562) no lugar de «herida».
- Nomes: Inês, Lianor Vaz (1834 diz «Leonor» nas rubricas), Pero Marques, Brás da Mata, Latão, Vidal.
- Título: o do pedido e o corrente, *Farsa de Inês Pereira*; a Copilação o abre como «Auto de Inês Pereira» e o
  argumento o chama «farsa» (dito na «Sobre»).
