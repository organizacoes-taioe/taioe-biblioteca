# Heródoto, Histórias (livro I): estado

Branch `pedido-herodoto` do `taioe-biblioteca` (worktree `~/.cache/claude-wt5-herodoto`). Regras da rodada:
`~/.cache/claude-pedidos-0511/BRIEF.md`. Pedido «em partes»: agora só o livro I; os outros livros vêm depois.

## Pronto (2026-11-12)
- Grego de Godley (1920) conferido com o fac-símile de 1921 (`original/LEIAME.md`); scripts em `ferramentas/`, rodados
  de `~/.cache/claude-pedidos-0511/herodoto/` (downloads do Perseus e do Internet Archive, páginas e OCR do Tesseract
  em `pag/` e `ocr/`; para refazer: `extrair.py dl/her-grc2.xml 1 l1.json`, `colacao.py .`, `acentos.py .`,
  `montar.py . <obra>`).
- Tradução inteira do livro I (17 partes, ~34 mil palavras): 1–14 pelo principal, 15–216 por tradutores Opus com o
  `CONVENCOES.md`, revisão contra o grego por dois revisores Sonnet (registro no fim de cada `traducao/notas-*.md`),
  uniformização pelo principal. `python3 ferramentas/conferir.py` (na pasta da obra) confere blocos, marcas, versos.
- `obra.py` com a «Sobre», `revisao.json` (8 decisões), autor `herodoto`, `conteudo/herodoto/`,
  `edicoes/vocabulario/herodoto-historias.json` (48 verbetes, `conferir` ok).

## Para o principal
- Juntar a branch, `node ferramentas/site/gerar.mjs`, Catálogo `obras` (obra nova), `traducoes_revisao.py --revisao` e
  Catálogo `traducoes`; tirar dos pedidos. Nenhuma regra de `_redirects`.
- O pedido continua «em andamento» para os livros II–IX (ou sai e cada livro vira pedido novo, a critério do Gere).

## Livro seguinte (como continuar)
- `extrair.py dl/her-grc2.xml 2 l2.json`; Tesseract nas páginas do livro II do mesmo fac-símile (PDF p. 300 em diante,
  pares); `colacao.py`, `acentos.py` e `montar.py` hoje leem `l1.json` e gravam `livro1-*`: generalizar o número do
  livro. Partes novas em `obra.py` com a sigla `Livro II`; a «Sobre» diz quais livros estão no ar.
- Notas gerais (lote futuro): o jogo Κυνώ/Σπακώ (110.1), παθήματα/μαθήματα (207.1), as Musas nos títulos.
