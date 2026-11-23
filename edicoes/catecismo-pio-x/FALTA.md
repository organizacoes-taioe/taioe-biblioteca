# Catecismo Maior de São Pio X — o que está feito e o que falta

Pedido do Gere (rodada de 2026-11-23). Branch `pedido-catecismo-pio-x` do `taioe-biblioteca`.

## Feito (preparador, 2026-11-23)

- **Original** (`original/`, 41 arquivos, 993 perguntas, ~41 mil palavras): montado por `montar.py` das páginas
  validadas (nível 4) do it.wikisource, «Pagina:Compendio della dottrina cristiana, Roma, 1905.djvu/87» a «/299»
  (= pp. 75-287 da edição de Roma, Tipografia Vaticana, 1905; o fac-símile é o do Commons, digitalização do Google
  Livros, exemplar da Bibliothèque S.J. de Chantilly). Um arquivo por capítulo; a Penitência (IV.6) em dois.
  Para refazer: `python3 edicoes/catecismo-pio-x/baixar.py <pasta>` e `montar.py <pasta>`.
- **Conferência com o fac-símile**: ver «Conferência» abaixo. Correções pela imagem em `CORRECOES` do `montar.py`.
- **`obra.py`** (autor `igreja-catolica`, gênero Magistério, grupo São Pio X, 1905, italiano ao lado, página
  «Sobre»), **`CONVENCOES.md`** (formato, tom, termos, fórmulas), **`conferir.py`** (confere a tradução contra o
  original), **`revisao.json`** (6 decisões para o Gere, rascunho do preparador).
- **Tradução-modelo**: `traducao/p0-licao-preliminare.txt` (perguntas 1-14) e `traducao/p1-c01.txt` (15-21).
- Testado: `python3 ferramentas/traducoes.py catecismo-pio-x` e `node ferramentas/site/gerar.mjs` com a tradução
  provisória (cópia do original nos arquivos que faltam), sem commitar o que eles geram.

## Feito (tradutores e uniformizador, 2026-11-23)

- **Tradução** completa nos 4 lotes (`traducao/`, 41 arquivos, ~41 mil palavras; `conferir.py` «ok» em todos, sem
  mesóclise). Notas de cada tradutor em `traducao/notas-lote-N.md`.
- **Uniformização**: tabelas de termos dos 4 lotes juntas no `CONVENCOES.md` (§ 3 e § 4); varredura por script dos
  ~170 lemas de conteúdo mais frequentes do italiano, comparando por lote a palavra portuguesa usada. Acertados:
  virtudes, vícios e novíssimos em minúscula (73 + 13 trocas), «méritos» de Cristo × «merecimentos» nossos (7),
  maiúsculas soltas (pároco, céu, jubileu, doutrina cristã, Comunhão sacramental, Anjos e Santos, paixão,
  ressurreição, Cruz de Cristo, «unir-me a vós»), _Pai-Nosso_ em itálico na 283. Os termos dos lotes já batiam
  (mentira oficiosa, Santos Óleos, perdoar/remissão, salvação/saúde).
- **Erros do italiano** apontados pelos tradutores, vistos na imagem (`img/pN.jpg`):
  - da transcrição, corrigidos em `CORRECOES` e `original/` regravado: 283 (_Pater noster_ em redondo na pergunta),
    334 «nel l’ora» → «nell’ora», 403 «sano» → «sono», 553 «acqua turale» → «naturale» (a p. 204 acaba em
    `{{Pt|na-|}}` sem a outra metade), 738 «pericolose di tendono» → «di peccare s’intendono», 841 «4.» → «4.º»,
    923 «è conosciamo» → «e» (na página só um pingo sobre o «e»), 933 «si» → «sì», 974 «ing nocchiarsi».
  - da edição de 1905 (ficam no original; a tradução lê a forma certa): 28 e 124 «;» por «:»; 81 «dell’attestazione»
    (por «dall’»); 83 e 502 pergunta terminada em ponto; 121 «sulle terra»; 211 «anime è al governo»; 450 «_Non
    dire_ il _falso testimonio_» (itálico partido); 656 «Messa è quello»; 741 «infinità bontà»; 772 item 4.º
    terminado em ponto; 888 «la Bibbie»; 952 «la vita dal corpo»; 964 «delle salute», «della altrui grazia»; 979
    «e dire;».
- **`revisao.json`**: 8 decisões (as 6 do preparador revistas, com «Hoje no site», e mais 2: «vós» ao confessor nas
  fórmulas da confissão; «maometanos» na 226). `ferramentas/traducoes_revisao.py` aceita.

## Falta

1. ~~Tradução~~ (feita) e ~~uniformização~~ (feita, acima).
2. ~~Revisão contra o italiano~~ (2026-11-23: dois revisores, 31 achados; 24 aplicados pelo uniformizador, 7 recusados: «sé» 193/206, _ab eterno_ 133, «me dai» 306, «culpável» 363/424, «povo hebreu» 389, «retamente» 923).
3. **Vocabulário** (regra para todo livro em português): `edicoes/vocabulario/catecismo-pio-x.json`
   (`node ferramentas/vocabulario.mjs …`, `edicoes/vocabulario/LEIA.md`). Provavelmente poucas palavras.
4. ~~`revisao.json`~~ (8 decisões, feito).
5. Publicar (principal): `traducoes.py catecismo-pio-x`, gerador, Catálogo etc.

### Os 4 lotes

Cada lote: traduzir os arquivos da lista, de `original/<arquivo>` para `traducao/<arquivo>`, seguindo
`CONVENCOES.md` (ler inteiro antes, e também `edicoes/CONVENCOES-TRADUCAO.md`) e o modelo
(`traducao/p0-licao-preliminare.txt`, `traducao/p1-c01.txt`, lidos lado a lado com o original). Ao terminar cada
arquivo: `python3 edicoes/catecismo-pio-x/conferir.py <arquivo>` tem de dar «ok» (mesmo número de blocos, mesmo
número em cada pergunta, mesmas linhas `| `, a marca `[parte.n]` no mesmo bloco, sem mesóclise). As fórmulas do
§ 5 do guia entram letra por letra. Notas em `traducao/notas-lote-N.md`.

| lote | arquivos | perguntas | palavras (it.) |
|---|---|---|---|
| 1 | `p1-c02.txt` a `p1-c13.txt` (Parte I, cap. II-XIII: o Credo, artigo por artigo; a Igreja em I.10) | 22-252 | ~9.500 |
| 2 | `p2-c01.txt` a `p2-c04.txt` (Parte II, a oração: Pai-Nosso e Ave-Maria) e `p3-c01.txt` a `p3-c04.txt` (Parte III, cap. I-IV: mandamentos de Deus e preceitos da Igreja) | 253-507 | ~10.200 |
| 3 | `p3-c05.txt` (deveres de estado, conselhos evangélicos), `p4-c01.txt` a `p4-c05.txt` (sacramentos em geral, Batismo, Crisma, Eucaristia, Missa) e `p4-c06a.txt` (Penitência, §§ 1-5) | 508-741 | ~9.400 |
| 4 | `p4-c06b.txt` (Penitência, §§ 6-10), `p4-c07.txt` a `p4-c09.txt` (Extrema-Unção, Ordem, Matrimônio) e `p5-c01.txt` a `p5-c08.txt` (Parte V: virtudes, dons, bem-aventuranças, obras de misericórdia, pecados, vícios, novíssimos, exercícios do dia) | 742-993 | ~10.300 |

Pontos de cada lote que pedem cuidado:
- Lote 1: os artigos do Credo citados nas perguntas (forma do § 5); I.10 (a Igreja, ~3.700 palavras): Papa,
  Bispos, Igreja docente/discente, militante/padecente/triunfante; a citação de Mt 16 (pergunta 153).
- Lote 2: o Pai-Nosso (pergunta 284) e cada pedido citado nas perguntas 288-318 («dívidas», «livrai-nos do
  mal»); a Ave-Maria e as palavras do anjo e de Santa Isabel (327, 330); os mandamentos (343) e os preceitos (474)
  exatamente como no § 5, e o mandamento citado em cada pergunta que o explica.
- Lote 3: termos da Eucaristia e da Missa (espécies, transubstanciação, jejum natural, ouvir Missa); da Penitência
  (exame, dor, contrição, atrição, propósito).
- Lote 4: acusação, absolvição, satisfação, indulgências, jubileu; Ordem e Matrimônio (impedimentos); na Parte V as
  listas (virtudes, dons, bem-aventuranças, obras de misericórdia, vícios capitais) exatamente como no § 5; as
  orações e jaculatórias do cap. V.8 por «vós».

## Conferência com o fac-símile

- A transcrição do Wikisource está toda no nível 4 (validada), feita sobre o mesmo djvu do Commons (folha de rosto:
  «Compendio della dottrina cristiana prescritto da Sua Santità Papa Pio X alle diocesi della provincia di Roma.
  Roma, Tipografia Vaticana, 1905»; a carta ao cardeal Respighi é de 14 de junho de 1905). Não há numeração das
  perguntas na edição; contadas, são 993, o mesmo número das edições de hoje.
- Método: OCR próprio das 213 páginas (Tesseract, modelo italiano `tessdata_best`, imagens de 960 px do Commons),
  comparado palavra por palavra com a transcrição; cada diferença que não era erro do OCR foi vista na imagem
  (recortes). Também vistas inteiras as pp. 75 e 81 (começo da lição preliminar e do cap. I.2), e o começo das
  cinco partes passou pela mesma comparação.
- Resultado: 34 erros da transcrição, corrigidos pela imagem (`CORRECOES` e a troca de «ė», «ả» no `montar.py`):
  «e» por «è» (10 vezes, ex.: «L’orazione e una elevazione»), palavra partida por espaço (11: «sal vati», «comanda
  mento», «per donare», «in quieto»…), acento faltando no passado («annunzio», «condanno»), palavra faltando
  («È certamente», «con un atto», «nel sacro tempio»), sobrando («perchè perchè»), trocada («nè debbono» por «ma
  debbono», «D. chi» por «Da chi»). Nenhuma diferença sistemática de texto nem de ordem: a transcrição é desta
  edição. Ficaram como a edição as grafias dela (_sètte_ «seitas», com o acento da página).
- Resíduo possível: erro que o OCR repetiu igual (raro). O tradutor que estranhar o italiano anota o número da
  pergunta; o principal confere a página no djvu (página do djvu = página impressa + 12).
- Material de trabalho (só neste PC, fora do git): `~/.cache/claude-pedidos-2311/tmp-catecismo-pio-x/` (`pag/` as
  páginas do Wikisource, `img/pN.jpg` as imagens, `ocr/pN.txt` o OCR) e os scripts em
  `~/.cache/claude-pedidos-2311/scripts-catecismo/` (`recortes.py` recorta a linha de um ponto suspeito). Apagar
  depois da publicação.

## Fora desta edição (para depois, se o Gere quiser)

- As outras partes do *Compendio* de 1905: «Prime nozioni di catechismo per i fanciulli di tenera età», o
  «Catechismo breve», a «Istruzione sopra le feste del Signore, della B. Vergine e dei Santi» e a «Breve storia della
  religione» (no mesmo djvu e no it.wikisource). Também a «Avvertenza» e a carta de Pio X ao cardeal Respighi (14 de
  junho de 1905) que abrem o volume.
- O catecismo de 1912 (*Catechismo della dottrina cristiana*, 433 perguntas) é outro livro: não misturar.

## Ideias para o gerador (não feitas: o preparador não mexe no gerador)

- Um pouco mais de espaço antes de cada pergunta (hoje os parágrafos ficam colados, `.texto p + p` com .15em), e a
  resposta sem o recuo da primeira linha. Por ora a pergunta em negrito separa bem.
- Os títulos de § (`## § n.`) saem como «cena» de teatro (versalete pequeno, centrado). Servem; um estilo próprio de
  subtítulo seria melhor.
- «Ir à pergunta n» (como o «Ir ao ponto» do Catecismo da Igreja Católica).
