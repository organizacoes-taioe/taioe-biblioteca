# Heródoto, Histórias: estado

Livros I a IV no ar (PRs #100, #113, #115 e #116). Livros V, VI e VII prontos em branches encadeadas: `pedido-herodoto-5`,
`pedido-herodoto-6` (contém a do V) e `pedido-herodoto-7` (contém as duas; worktree `~/.cache/claude-wt5-herodoto-7`):
basta juntar a do VII. Regras da rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`. A obra cresce por livros.

## Livro VII (Polímnia): pronto (2026-11-17)
- Grego montado e conferido (`original/livro7-*.txt`, 27 partes; `original/LEIAME.md`, «Livro VII»): mesmo PDF do vol. III
  (p. 316–574; OCR em `ocr7/`, páginas em `pag7/`, pranchas em `ver7/`, na pasta de trabalho
  `~/.cache/claude-pedidos-0511/herodoto/`); `colacao.py . 7`, `acentos.py . 7`, `montar.py . <obra> 7`. 16 palavras com
  letras trocadas (Κάδμος em 164.1 é erro tipográfico do próprio Godley), seis que faltavam, os parênteses de 205.1, uns
  40 acentos; 74 pontos vistos nas imagens. Marcas 8α–8δ, 9α–9γ, 10α–10θ, 16α–16γ (o θ entrou em `montar.py`,
  `conferir.py` e `ferramentas/traducoes.py`). `montar.py` ganhou `DEPOIS7` (acentos que o `graves.py` refaria) e não
  põe maiúscula em capítulo que começa por lacuna (76.1).
- Consertos em livros já prontos: livro IV, os parênteses de 34.2 e 35.3 (sobravam «ʽ» soltos do Perseus); livros IV e
  V, cinco lugares onde a nota de Godley juntava duas palavras («Δαρείουοὐδέν»: 4.167.3, 4.169.1, 5.16.1, 5.69.2,
  5.73.1); livro VI, «Ácanto» → «Acanto» (6.44.2).
- Tradução por quatro tradutores Opus em sequência (1–7 e 121–162; 8–53; 54–120; 163–239); revisão contra o grego por
  dois revisores Sonnet (registro no fim de cada `traducao/notas-livro7-*.md`); um aplicador Opus julgou os achados (33
  aplicados, 8 recusados) e uniformizou os nomes com os livros I–VI (Artabano, Ábido, Sesto, Âmpelo, Dinômenes…):
  `traducao/notas-livro7-1-7.md`, «Revisão aplicada». `CONVENCOES.md`, seção «Livro VII», acertada pelos nomes finais.
- `obra.py` (127 partes; a «Sobre» com o livro VII), `revisao.json` (+3 decisões: o último verso do oráculo do muro de
  madeira, «mergulhai a alma na dor», 140.3, aplicada; «muita gente, mas poucos homens», 210.2; «Estrangeiro, vai dizer
  aos lacedemônios», 228.2; recomendação aplicada), vocabulário (+12 verbetes, 150 no total, `conferir` ok),
  `conteudo/` gerado. `gerar.mjs` e `conferir.mjs` sem erro; os endereços dos livros I a IV não mudam (os do V, VI e VII
  são novos).
- Candidatos que ficaram nas notas, sem ir ao Gere (recomendação aplicada): 10ε.1 «deus não deixa que ninguém tenha
  orgulho», 102.1 «valor» (ἀρετή), 139.3 «túnicas de muralhas», 176.3 «os Caldeirões», 231.1 «Aristodemo, o que tremeu».

## Livro VI (Érato): pronto (2026-11-17)
- Grego montado e conferido (`original/livro6-*.txt`, 14 partes; `original/LEIAME.md`, «Livro VI»): mesmo PDF do vol. III
  (p. 164–312; OCR em `ocr6/`, páginas em `pag6/`, pranchas em `ver6/`); `colacao.py . 6`, `acentos.py . 6`,
  `montar.py . <obra> 6`. 15 palavras com letras trocadas, duas que faltavam (53.2, 138.2), os parênteses de 69.4 e 109,
  37 acentos; 31 pontos vistos nas imagens. Marcas 86α–86δ (Glauco). Colchetes em 111.2 e no capítulo 122 inteiro.
- Tradução por quatro tradutores Opus em sequência; revisão contra o grego por dois revisores Sonnet (registro no fim de
  cada `traducao/notas-livro6-*.md`); o que se aplicou em `traducao/notas-livro6-1-10.md`. `CONVENCOES.md`, seção
  «Livro VI», acertada pelos nomes da tradução.
- `obra.py` (100 partes; a «Sobre» com o livro VI), `revisao.json` (+3 decisões: «carneiro» no jogo com Crio, 50.3;
  «Sépeia» × «Hesipeia», 77.1; «Hipoclides não se importa», 129.4; recomendação aplicada, nada muda no ar), vocabulário
  (+12 verbetes, 138 no total, `conferir` ok), `conteudo/` gerado. `gerar.mjs` e `conferir.mjs` sem erro; os endereços
  dos livros I a V não mudam.

## Livro V (Terpsícore): pronto (2026-11-17)
- Grego montado e conferido (`original/livro5-*.txt`, 13 partes; `original/LEIAME.md`, «Livro V»). Fonte nova: o vol. III
  de Godley, 1ª impressão de 1922 (IA `in.ernet.dli.2015.183370`, PDF em `dl5/`, OCR em `ocr5/`, páginas em `pag5/`,
  pranchas em `ver5/`); 2ª leitura `dl5/herodotus19203hero.txt` (reimpressão de 1982). `colacao.py . 5`, `acentos.py . 5`,
  `montar.py . <obra> 5`, rodados de `~/.cache/claude-pedidos-0511/herodoto/`. 15 correções de letras (com 5.1, erro
  tipográfico de Godley, e os parênteses de 67.3), 26 acentos; 34 pontos vistos nas imagens. Marcas 92α–92η (Hude; o
  Perseus escreve 92A–92G): `conferir.py`, `montar.py` e `ferramentas/traducoes.py` aceitam α–η.
- Tradução: 1–10 pelo principal, o resto por quatro tradutores Opus em sequência; revisão contra o grego por dois
  revisores Sonnet (registro no fim de cada `traducao/notas-livro5-*.md`); o que se aplicou em
  `traducao/notas-livro5-1-10.md`. `CONVENCOES.md`, seção «Livro V», acertada pelos nomes da tradução.
- `obra.py` (86 partes; a «Sobre» com o livro V e o fac-símile do vol. III), `revisao.json` (+3 decisões: «igualdade de
  palavra», 78.1; «um apedrejador», 67.2; Cípselo «tirado da _kypséle_, a arca», 92ε.1; recomendação aplicada, nada muda
  no ar), vocabulário (+11 verbetes, 126 no total, `conferir` ok), `conteudo/` gerado. `gerar.mjs` e `conferir.mjs` sem
  erro; os endereços dos livros I a IV não mudam.

## Livro IV (Melpômene): pronto (2026-11-16)
- Grego montado e conferido (`original/livro4-*.txt`, 22 partes; `original/LEIAME.md`, «Livro IV»): mesmo PDF do vol. II
  (p. 222–430; OCR em `ocr4/`, páginas em `pag4/`, pranchas em `ver4/`, na pasta de trabalho); `colacao.py . 4`,
  `acentos.py . 4`, `montar.py . <obra> 4`. 20 palavras com letras trocadas, uma que faltava (119.4), 116 acentos;
  44 pontos vistos nas imagens. Sem colchetes; lacunas 47.2 e 149.2.
- Tradução: 1–12 e 200–205 pelo principal, o resto por cinco tradutores Opus em sequência; revisão contra o grego
  por dois revisores Sonnet (registro no fim de cada `traducao/notas-livro4-*.md`); o que se aplicou e os nomes
  uniformizados em `traducao/notas-livro4-1-12.md`. `CONVENCOES.md`, seção «Livro IV», acertada pelos nomes da tradução.
- `obra.py` (73 partes; a «Sobre» com o livro IV), `revisao.json` (+2 decisões: «hiperbóreos… hipernótios», 36.1;
  _aigéai_ × «peles de cabra» na origem do nome «égide», 189.2; recomendação aplicada, nada muda no ar), vocabulário
  (+22 verbetes e 1 forma, 115 no total, `conferir` ok), `conteudo/` gerado. `gerar.mjs` e `conferir.mjs` sem erro; os
  endereços dos livros I a III não mudam.

## Livro III (Tália): pronto (2026-11-16)
- Grego montado e conferido (`original/livro3-*.txt`, 16 partes; `original/LEIAME.md`, «Livro III»): vol. II de
  Godley, 1921 (IA `herodotus0002adgo_j1l1`, PDF em `dl3/`, OCR em `ocr3/`, páginas em `pag3/`); 2ª leitura
  `dl/herodotus0000hero.txt` (reimpressão da revista de 1938). `colacao.py . 3`, `acentos.py . 3`,
  `montar.py . <obra> 3`, `pranchas.py … pag3`, rodados de `~/.cache/claude-pedidos-0511/herodoto/`.
- Tradução: 1–16 pelo principal, o resto por quatro tradutores Opus em sequência; revisão contra o grego por dois
  revisores Sonnet (registro no fim de cada `traducao/notas-livro3-*.md`); correções aplicadas pelo principal.
- `CONVENCOES.md` (seção «Livro III»), `obra.py` (51 partes; a «Sobre» com o livro III e o fac-símile do vol. II),
  `revisao.json` (+2 decisões: «o costume é rei de todos» × «a lei…», 38.4; «igualdade perante a lei» × «isonomia»,
  80.6; recomendação aplicada, nada muda no ar), vocabulário (+14 verbetes e 4 formas, 92 no total, `conferir` ok),
  `conteudo/` gerado. `gerar.mjs` e `conferir.mjs` sem erro; os endereços dos livros I e II não mudam.

## Livro II (Euterpe): pronto (2026-11-16)
- Grego montado e conferido (`original/livro2-*.txt`, 18 partes; `original/LEIAME.md`, «Livro II»). Scripts
  generalizados: `extrair.py dl/her-grc2.xml 2 l2.json`, `colacao.py . 2`, `acentos.py . 2`, `montar.py . <obra> 2`,
  rodados de `~/.cache/claude-pedidos-0511/herodoto/` (OCR do livro II em `ocr2/`, pranchas em `ver2/`).
- Marcas `[121α.1]`…`[121ζ.2]` (Rampsinito, numeração de Hude); `ferramentas/traducoes.py` e o `conferir.py` da obra
  aceitam a letra. `CONVENCOES.md` com os nomes e termos do livro II.
- Tradução: 1–18 pelo principal, o resto por quatro tradutores Opus em sequência; revisão contra o grego por dois
  revisores Sonnet (registro no fim de cada `traducao/notas-livro2-*.md`); uniformização e o que se aplicou ou não em
  `traducao/notas-livro2-1-18.md`.
- `obra.py` (35 partes, a «Sobre» com os livros I e II), `revisao.json` (+3 decisões: dádiva × presente, cavalos do
  rio × hipopótamos, distrito × nomo; recomendação aplicada), vocabulário (+30 verbetes, 78 no total, `conferir` ok),
  `conteudo/` gerado. `gerar.mjs` e `conferir.mjs` sem erro; os endereços do livro I não mudam.

## Para o principal
- Juntar a branch, gerar, Catálogo `obras` (a obra já existe: atualiza) e `traducoes` se houver decisões novas.
  Nenhuma regra de `_redirects`.
- Mudança comum: `ferramentas/traducoes.py` aceita marca `[121α.1]` (letra grega depois do capítulo), agora de α a θ
  (`[10θ.1]` no livro VII). O livro IV, já no ar, muda no original ao lado (34.2, 35.3, 167.3, 169.1): o Catálogo `obras`
  cobre. Decisões novas do VII: 3 (`l7-oraculo-muralhas`, `l7-poucos-homens`, `l7-estrangeiro`).

## Livros VIII e IX (como continuar)
- Fonte nova: o vol. IV de Godley, _Books VIII–IX_ (Loeb, Londres e Nova York, 1924 na folha de rosto, «MCMXXIV»; as
  reimpressões dizem «First printed 1925»). Fac-símile principal: Internet Archive `bwb_Y0-DUM-764`, a 1ª impressão
  (PDF de 430 páginas, texto a 360 ppi, já baixado em `dl8/v4-1924.pdf` na pasta de trabalho). Grego nas páginas pares:
  livro VIII de 26 até ~178; livro IX de ~182 até ~324 (o índice começa na p. 327); conferir os limites nas imagens.
  2ª leitura: o OCR do Internet Archive em `in.ernet.dli.2015.69772` (reimpressão de 1930, mesmas chapas; 32 % de letras
  gregas, `dl8/in.ernet.dli.2015.69772.txt`), de «BOOK VIII» até «BOOK IX» e de «BOOK IX» até «INDEX». O OCR do próprio
  `bwb_Y0-DUM-764` (`dl8/bwb_Y0-DUM-764.txt`) também tem grego, mas é da mesma digitalização: serve de 3ª leitura.
  Não servem: `in.ernet.dli.2015.183371` (rotulado vol. 4, é o vol. II), `herodotus04hero`, `herodotus0004adgo`,
  `bwb_C0-AWL-834_a4w3`, `herodotus0000unse_i4o7` (OCR sem grego).
- Passos, como no VII: `extrair.py dl/her-grc2.xml 8 l8.json`; roteiro de OCR `scripts/ocr1924-l8.sh` (copiar o
  `ocr1922-l7.sh`, trocando o PDF e as páginas); no `colacao.py`, `O2[8]` e o recorte do 8 (e do 9); no `montar.py`,
  `CORR8`, `ACENTOS8`, `PARTES8`, `ED4` (vol. IV) e o bloco 8 em `LIVROS` (título «Θ · ΟΥΡΑΝΙΗ»; o IX, «Ι · ΚΑΛΛΙΟΠΗ»).
  Conferir com `ast.parse` depois de mexer (a aspa do `ED1 = ('` já quebrou três vezes). `grep ʽ` no `l8.json` (parênteses
  de Godley que o Perseus marca com sinal solto) e `\w⟦n⟧\w` (já tratado). Roteiros dos tradutores e revisores:
  `~/.cache/claude-pedidos-0511/herodoto/TRADUTOR-L7.md`, `REVISOR-L7.md` (trocar 7 por 8); `scripts/godley.py 8 a b`
  imprime a tradução inglesa de Godley.

## Outros
- Notas gerais (lote futuro): livro I, o jogo Κυνώ/Σπακώ (110.1), παθήματα/μαθήματα (207.1), as Musas nos títulos.
