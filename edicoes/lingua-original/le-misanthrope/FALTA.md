# Le Misanthrope (Molière): o que falta

Pedido de 27/11/2026 (branch `pedido-le-misanthrope`, worktree `~/.cache/claude-wt27-le-misanthrope`).
Teatro na língua original, no modelo do *Macbeth*: uma parte por cena (`partes/<ato>-<cena>.txt`, 22 cenas de
1667 + `0-personagens.txt`), um `glossario.json` para a peça inteira. Autor novo, `moliere`.
Material de trabalho (downloads, cenas.json, fichas, lotes): `~/.cache/claude-pedidos-2711/le-misanthrope/`.

## Feito
- Texto montado: `ferramentas/extrair.py` (Wikisource, Louandre 1910, HTML da API) → `cenas.json` →
  `ferramentas/montar.py` (divisão de 1667, numeração seguida 1–1808 por `::versos N`, cartas do V, 4 em
  `::prosa`, correções de `ferramentas/correcoes.json` e `PROSA`). 1.808 versos, conferidos com 180 números
  de verso do OCR de Despois–Mesnard (todos batem).
- Colação (`ferramentas/colacao.py`, relatório em `~/.cache/claude-pedidos-2711/le-misanthrope/colacao.tsv`)
  com Boully 1899 e van Bever 1923 (OCRs do IA) e as notas de variantes de Despois–Mesnard: 18 versos + 3
  lugares das cartas voltam a 1667 (lista no «Sobre», em `obras.json`).
- Código: `gerar.mjs` aceita `::versos N` (numeração que corre pela peça) e `::prosa` (linha sem número, com
  notas); `lingua_original.py` dá notas ao `::prosa`; CSS `.m-prosa`.
- `obras.json` (com «Sobre» e fontes) e `conteudo/autores.js` (Molière). Todas as partes em `rascunho`.

- Glossário: 2.740 verbetes, 1.021 ocorrências apontadas a variantes; feito por dois agentes Sonnet (Personagens e
  Atos I–II; Atos III–V, branches `pedido-le-misanthrope-ga` e `-gb`, já juntas aqui), revisto por dois revisores
  Sonnet (palavras de conteúdo; lotes em `~/.cache/claude-pedidos-2711/le-misanthrope/glossario/revisao/`) e
  pelo principal (nomes próprios, sentidos do séc. XVII, ce/ce#2, soins/soins#2, grimace, veste, cape, parties).
  `conferir` dá «tudo certo»; partes fora do rascunho; `conteudo/moliere/lingua-original.js` gravado.
- `revisao-le-misanthrope.json`: 1 decisão (sem tradução ao lado, recomendada; Castilho 1874 «versão libérrima»
  como opção b ou c).

## Falta (para o principal)
- Juntar a branch, gerar o site, Catálogo `obras` (obra nova), PR; `traducoes_revisao.py --revisao` (1 escolha).
  Endereços novos (`/biblioteca/moliere/le-misanthrope/…`): nenhuma regra de `_redirects`.
- O código mudou em `gerar.mjs` (`::versos`, `::prosa`), `lingua_original.py` (`prosa` com notas) e `estilo.css`
  (`.m-prosa`); o Macbeth e os outros saem iguais.
- Se o Gere escolher a opção b ou c: o OCR de Castilho está no IA (`omisanthropocom00moligoog`, djvu.txt).

## Não conferido
- Onde o OCR de Despois–Mesnard está de cabeça para baixo (boa parte do Ato III e algumas páginas do IV e V),
  a conferência ficou com Boully e van Bever; variante em que os dois OCRs falham juntos pode ter escapado.
- A divisão do Ato III em 5 cenas é dedução (Despois–Mesnard tem a cena V com Alceste e Arsinoé; as cenas
  que 1734 abre a cada saída de personagem não existem em 1667); conferir num fac-símile de 1667 se houver.
