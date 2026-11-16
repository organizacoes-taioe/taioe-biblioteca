# Heródoto, Histórias: estado

Livro I no ar (PR #100). Livro II em andamento na branch `pedido-herodoto-2` do `taioe-biblioteca` (worktree
`~/.cache/claude-wt5-herodoto-2`). Regras da rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`. A obra cresce por livros.

## Livro II (Euterpe), 2026-11-16
- [x] Grego montado e conferido (`original/livro2-*.txt`, 18 partes; `original/LEIAME.md`, «Livro II»). Scripts
  generalizados: `extrair.py dl/her-grc2.xml 2 l2.json`, `colacao.py . 2`, `acentos.py . 2`, `montar.py . <obra> 2`,
  rodados de `~/.cache/claude-pedidos-0511/herodoto/` (OCR do livro II em `ocr2/`, pranchas em `ver2/`).
- [x] `CONVENCOES.md` com os nomes e termos do livro II. Marcas `[121α.1]`…`[121ζ.2]` (Rampsinito); o
  `ferramentas/traducoes.py` e o `conferir.py` da obra aceitam a letra.
- [ ] Tradução, lotes (um tradutor de cada vez; cada lote com `traducao/notas-livro2-*.md`):
  - principal: 1–4, 5–18;
  - T1: 19–27, 28–34, 35–41, 42–53;
  - T2: 54–64, 65–76, 77–90, 91–98;
  - T3: 99–110, 111–120, 121–123, 124–136;
  - T4: 137–146, 147–157, 158–171, 172–182.
- [ ] Revisão contra o grego (Sonnet, só relata; registro no fim de cada `notas-livro2-*.md`); uniformização.
- [ ] `obra.py`: PARTES do livro II (sigla `Livro II`, títulos em `ferramentas/montar.py`, `PARTES2`) e a «Sobre»
  (livros I e II no ar). Só acrescentar quando todas as traduções existirem (o gerador pula a obra incompleta).
- [ ] `revisao.json`: decisões novas (candidatas: cavalos do rio × hipopótamos; νομός → distrito × nomo).
- [ ] Vocabulário: palavras novas do livro II em `edicoes/vocabulario/herodoto-historias.json` (`capitulo` = número da
  parte na obra: o livro II começa na parte 18); `node ferramentas/vocabulario.mjs conferir …` ok.
- [ ] `node ferramentas/site/gerar.mjs` e `conferir.mjs` sem erro na worktree (sem commitar `public/`).

## Para o principal
- Juntar a branch, gerar, Catálogo `obras` (a obra já existe: atualiza) e `traducoes` se houver decisões novas.
  Nenhuma regra de `_redirects`.
- Mudança comum: `ferramentas/traducoes.py` aceita marca `[121α.1]` (letra grega depois do capítulo).

## Livro seguinte (como continuar)
- O livro III está no vol. II de Godley (Loeb, 1921): outro fac-símile (procurar no Internet Archive a impressão mais
  antiga do vol. II) e outra 2ª leitura; `colacao.py` lê `dl/historiesvolumei00hero_249.txt` (só vol. I): generalizar
  o arquivo e o recorte (título «BOOK III» até «BOOK IV»). Novo bloco em `LIVROS` no `montar.py`.
- Notas gerais (lote futuro): livro I, o jogo Κυνώ/Σπακώ (110.1), παθήματα/μαθήματα (207.1), as Musas nos títulos.
