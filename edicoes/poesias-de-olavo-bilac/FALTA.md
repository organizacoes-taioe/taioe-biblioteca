# Poesias de Olavo Bilac (1902): o que está feito e o que falta

## Feito (2026-11-02)
- Obra `poesias-de-olavo-bilac` (Literatura, autor `olavo-bilac`), montada por `montar.py` a partir de `texto/`
  (cópia dos arquivos do corpus do Versificador, transcritos das imagens do fac-símile de 1902, Brasiliana
  Mindlin no Wikimedia Commons, `File:Poesias_(1902).pdf`).
- As seis partes: **Panóplias** (12; *Para a Rainha Dona Amélia*, que não está em 1902, fica de fora),
  **Via Láctea** (35 sonetos, com as dedicatórias de 1902), **Sarças de Fogo** (30), **Alma Inquieta** (38),
  **As Viagens** (14) e **O Caçador de Esmeraldas**: 130 poemas, 29.367 palavras.
- Confronto palavra por palavra: (1) transcrição do corpus × Wikisource (poemas avulsos da
  `Categoria:Olavo_Bilac`, grafia atual, edição não indicada): 72 divergências nas duas primeiras partes, 43 nas
  Sarças, 69 na Alma Inquieta, 59 nas Viagens, 18 no Caçador; (2) as divergências conferidas na camada de OCR do
  próprio PDF de 1902 (`pdftotext -layout`). Em todas as conferidas, 1902 dá a lição do corpus; as do Wikisource
  são de outras edições (Bilac reescreveu versos d'*A morte de Tapir*, da *Via Láctea* etc.) ou erros de leitura
  (Neto, dava, precipitar, asserena, tio, batei, dano por clarão). Sem Wikisource: *Abyssus*, *É nestas noites
  sossegadas*, *Noite de inverno*, *Wilfredo* (corpus × OCR, sem divergência real) e *Baladas românticas*.
- Erro de 1902 corrigido: «tal..» → «tal...» (*Profissão de fé*). Mantidas como em 1902: «Heliostes» (2 vezes,
  por «heliastas»), «hetere», «fermosura», «No liminar da morte», «Jacob», «cœli», «vêm» (= veem, monossílabo).
- Grafia: AO1990 já feita no corpus; o `montar.py` passa d'essa/n'um/outr'ora a dessa/num/outrora e mantém as
  elisões do verso (minh'alma, d'alma, d'água); E' → É; Gœthe → Goethe; Luiz → Luís; títulos Fenícios, Índias,
  Brasil. O que o corpus deixou na grafia antiga vai em `GRAFIA` (montar.py): «por que» nas perguntas (Alma
  Inquieta, Viagens), afora, trás, vazios, cor-de-rosa, Campo-Santo, Caos, Cristãs, juçaras, antemanhã, Guaicuí,
  dar-lhe-ás (mesóclise do autor, fica).
- Vocabulário: `edicoes/vocabulario/poesias-de-olavo-bilac.json` (195 palavras, tiradas do
  `olavo-bilac-poesia.json` já revisado, com `so_capitulos` = número do poema na obra; `conferir` dá ok).
- **Duplicação resolvida** (como na Mensagem e nos Primeiros Cantos): `OBRAS_PROPRIAS` em `ferramentas/poesia.py`
  (pasta `bilac`: `panoplias--01-` a `--12-` e os prefixos das outras cinco partes; *Para a Rainha Dona Amélia*
  continua entre os avulsos) e `python3 ferramentas/poesia.py --fonte …/versificador`: saíram 130 poemas de
  `conteudo/olavo-bilac/poesia.js` (ficam Dona Amélia, o Hino à Bandeira e *Tarde*). O vocabulário do autor
  (`olavo-bilac-poesia.json`) ficou só com os poemas que restam: 100 obras, 142 palavras (`conferir` dá ok; algumas
  guardam `exemplo`/`obra_ex` de poema que saiu, só informativo). `redirects.txt`: os 130 endereços antigos → os
  novos (301), a acrescentar ao `public/_redirects` ao gerar.
- **Por que o `gerar.mjs` mudou** (`soPoesia`, `htmlLivrosDePoesia`, `trilhaGenero`): um livro de poemas inteiro
  (obra com partes, gênero «Poesia», não `poema`) não aparecia em lugar nenhum. Com ele, `soPoesia` deixava de valer
  e a página do autor virava «Gêneros → Poesia» (um clique a mais); na página do gênero, `htmlPastas` põe a obra
  (forma «outras») na pasta «Outras formas», que só lista poemas soltos, e ela some. Agora o autor só de poesia
  continua com a página direta, e o livro entra numa seção «Livros», em cima das formas (também na página do
  gênero Poesia, para quem tem outros gêneros).
- **Mensagem e Primeiros Cantos sem essa mudança** (gerado em 02/11 nas branches deles, sobre a `main`):
  a página do autor vira «Gêneros → Poesia» nos dois. A *Mensagem* fica **sem link nenhum** (Pessoa tem pastas de
  formas; ela cai na «Outras formas» e some). *Primeiros Cantos* aparece na página Poesia (Gonçalves Dias não tem
  pastas), mas listado entre os poemas do grupo «Avulsos · 1846». Com o `gerar.mjs` desta branch, os três ficam em
  «Livros», na página direta do autor: juntar as três branches com esta mudança.

## Falta
- *Baladas românticas*: conferida só com o OCR de 1902 (não está no Wikisource), sem divergência real.
- Ver se 1902 numera os poemas d'*As Viagens* (o Wikisource põe I–XIV) e se há nota ou prefácio a incluir.
- Scripts do confronto (`parte.py <slug>`, `diff.py`, `ocr.py`, `ocr1.py`) em `~/.cache/claude-pedidos-0211/scr-bilac/`,
  só neste PC.
