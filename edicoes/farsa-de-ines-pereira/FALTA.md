# Farsa de Inês Pereira: o que falta

Branch `pedido-farsa-de-ines-pereira` (worktree `~/.cache/claude-wt27-farsa-de-ines-pereira`).
Trabalho de apoio (fac-símile de 1562, colunas recortadas, OCRs) em `~/.cache/claude-pedidos-2711/farsa-de-ines-pereira/`.
Método e regras em `CONVENCOES.md`.

## Feito
- Texto: Copilação de 1562 relida coluna por coluna no fac-símile da BNP, sobre o texto de 1834 passado a limpo;
  1.125 versos, 10 partes, ~5.700 palavras. `texto.txt`, `publicar.py` e `conteudo/gil-vicente/farsa-de-ines-pereira.js`
  (+ a linha do `index.html`). Gerado e conferido na worktree (`conferir.mjs`: tudo certo).
- `revisao.json`: 2 decisões (texto-base 1562 × 1834; as três emendas), recomendação aplicada.

## Falta
- Vocabulário `edicoes/vocabulario/farsa-de-ines-pereira.json` (`conferir` ok).
- Depois, só o do principal: juntar, gerar o site, PR, Catálogo `obras` e `traducoes`, tirar dos pedidos.
  Sem `_redirects`, sem autor novo (Gil Vicente ganha a pasta «Teatro» com 3 obras).
