# Heródoto, Histórias: estado

Livros I a III no ar (PRs #100, #113 e #115). Livro IV pronto na branch `pedido-herodoto-4` (worktree
`~/.cache/claude-wt5-herodoto-4`). Regras da rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`. A obra cresce por livros.

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
- O livro V está no vol. III de Godley (Loeb, 1922; Godley morreu em 1925): achar o fac-símile de 1922 no Internet
  Archive (e uma 2ª leitura com OCR grego), acrescentar ao `colacao.py` o recorte do V (O1/O2 do vol. III) e ao
  `montar.py` o bloco 5 (`ED3`, título «Ε · ΤΕΡΨΙΧΟΡΗ»); o resto como no IV (`extrair.py dl/her-grc2.xml 5 l5.json`).
- Notas gerais (lote futuro): livro I, o jogo Κυνώ/Σπακώ (110.1), παθήματα/μαθήματα (207.1), as Musas nos títulos.
