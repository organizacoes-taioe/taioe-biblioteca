# Heródoto, Histórias: estado

Livros I a IV no ar (PRs #100, #113, #115 e #116). Livro V pronto na branch `pedido-herodoto-5` (worktree
`~/.cache/claude-wt5-herodoto-5`). Regras da rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`. A obra cresce por livros.

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
- Mudança comum: `ferramentas/traducoes.py` aceita marca `[121α.1]` (letra grega depois do capítulo).

## Livro seguinte (como continuar)
- O livro VI está no mesmo vol. III (fontes do V: no PDF `dl5/v3-1922.pdf`, o título «BOOK VI» na p. 163 e o grego
  nas páginas pares a partir da 164; a 2ª leitura, de «BOOK VI» até «BOOK VII»; o `colacao.py` já tem o recorte do 6).
  Falta no `montar.py` o bloco 6 (`ED3`, título «Ϛ · ΕΡΑΤΩ»: conferir a letra que Godley imprime).
- Notas gerais (lote futuro): livro I, o jogo Κυνώ/Σπακώ (110.1), παθήματα/μαθήματα (207.1), as Musas nos títulos.
