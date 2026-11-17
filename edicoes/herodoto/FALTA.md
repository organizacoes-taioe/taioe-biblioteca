# Heródoto, Histórias: estado

Livros I a III no ar (PRs #100, #113 e #115). Livro IV em andamento na branch `pedido-herodoto-4` (worktree
`~/.cache/claude-wt5-herodoto-4`). Regras da rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`. A obra cresce por livros.

## Livro IV (Melpômene): em andamento (2026-11-16)
- Feito: grego montado e conferido (`original/livro4-*.txt`, 22 partes; `original/LEIAME.md`, «Livro IV»; OCR em
  `ocr4/`, páginas em `pag4/`, pranchas em `ver4/`, na pasta de trabalho; `montar.py . <obra> 4`); `CONVENCOES.md`,
  seção «Livro IV».
- Tradução (`traducao/livro4-*.txt` + `notas-livro4-*.md`, roteiros `~/.cache/claude-pedidos-0511/herodoto/TRADUTOR-L4.md`
  e `REVISOR-L4.md`): o principal faz 1–12, 83–92, 93–98, 99–109, 110–117 e 200–205; tradutores Opus, um de cada vez:
  T1 13–58, T2 59–82 e 118–125, T3 126–158, T4 159–199. `python3 ferramentas/conferir.py` mostra o que falta.
- Depois: revisão contra o grego (Sonnet, só relata, no fim de cada `notas-livro4-*.md`), uniformização, `obra.py`
  (o livro IV em PARTES e na «Sobre»: lacunas 47.2 e 149.2, sem colchetes, «21 palavras com letras trocadas, uma que
  faltava (119.4) e uns 116 acentos»), `revisao.json` (só decisão nova), vocabulário, `ferramentas/traducoes.py`,
  gerar e conferir. **O IV entra todo de uma vez** (obra com parte sem tradução some do site).

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
- O livro IV está no mesmo vol. II de Godley: o mesmo PDF (`dl3/adgo1921-v2.pdf`, páginas gregas a partir da 222, pares,
  até antes do índice) e a mesma 2ª leitura; `colacao.py` já tem o recorte do IV (2ª ocorrência de «BOOK IV» até
  «INDEX»). Falta o OCR (copiar `scripts/ocr1921-l3.sh` com `seq 222 2 <fim>` e pasta `ocr4`), o bloco 4 em `LIVROS`
  no `montar.py` (`edicao=ED2`, título «Δ · ΜΕΛΠΟΜΕΝΗ») e a seção do IV no `CONVENCOES.md`.
- Notas gerais (lote futuro): livro I, o jogo Κυνώ/Σπακώ (110.1), παθήματα/μαθήματα (207.1), as Musas nos títulos.
