# Heródoto, Histórias: estado

Livro I no ar (PR #100). Livro II pronto na branch `pedido-herodoto-2` do `taioe-biblioteca` (worktree
`~/.cache/claude-wt5-herodoto-2`). Regras da rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`. A obra cresce por livros.

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
- O livro III está no vol. II de Godley (Loeb, 1921): outro fac-símile (procurar no Internet Archive a impressão mais
  antiga do vol. II) e outra 2ª leitura; `colacao.py` lê `dl/historiesvolumei00hero_249.txt` (só vol. I): generalizar
  o arquivo e o recorte (título «BOOK III» até «BOOK IV»). Novo bloco em `LIVROS` no `montar.py`.
- Notas gerais (lote futuro): livro I, o jogo Κυνώ/Σπακώ (110.1), παθήματα/μαθήματα (207.1), as Musas nos títulos.
