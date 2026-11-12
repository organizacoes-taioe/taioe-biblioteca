# Heródoto, Histórias (livro I): estado

Branch `pedido-herodoto` do `taioe-biblioteca` (worktree `~/.cache/claude-wt5-herodoto`). Regras da rodada:
`~/.cache/claude-pedidos-0511/BRIEF.md`. Pedido «em partes»: agora só o livro I; os outros livros vêm depois.

## Pronto
- Grego de Godley (1920) conferido com o fac-símile de 1921 (`original/LEIAME.md`); scripts em `ferramentas/`, rodados
  de `~/.cache/claude-pedidos-0511/herodoto/` (downloads do Perseus e do Internet Archive, páginas renderizadas e
  OCR do Tesseract em `pag/` e `ocr/`; para refazer: `extrair.py dl/her-grc2.xml 1 l1.json`, `colacao.py .`,
  `acentos.py .`, `montar.py . <obra>`).
- `CONVENCOES.md`, `obra.py` (partes; «Sobre» provisória).

## Falta
- Tradução, um arquivo de `traducao/` para cada um de `original/` (17), com `traducao/notas-<arquivo>.md`.
  Feitos: (nenhum).
- Revisão contra o grego (subagente Sonnet), uniformização dos nomes e termos.
- «Sobre» no `obra.py`, `revisao.json` (~8 decisões), autor `herodoto` em `conteudo/autores.js`, `python3
  ferramentas/traducoes.py herodoto`, vocabulário (`edicoes/vocabulario/herodoto-historias.json`), gerar e conferir.
