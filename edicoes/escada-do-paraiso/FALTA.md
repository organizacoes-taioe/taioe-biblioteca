# Escada do Paraíso (São João Clímaco): estado

Branch `pedido-escada-do-paraiso` do `taioe-biblioteca` (worktree `~/.cache/claude-wt5-escada-do-paraiso`). Regras da
rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`. Trabalho (páginas, OCR, léxico, pranchas, decisões da conferência):
`~/.cache/claude-pedidos-0511/escada-do-paraiso/` (só neste PC).

## Pronto (2026-11-16), publicável
- Grego dos 30 degraus (`original/`, PG 88 = Rader 1633), OCR nosso conferido nas imagens; método e limites em
  `original/LEIAME.md`. Desde a conferência, o `original/` se edita à mão.
- Tradução dos 30 degraus (`traducao/`, ~69 mil palavras): degrau 1 pelo principal, 2–15 e 16–30 por dois tradutores
  Opus com o `CONVENCOES.md`; notas de cada degrau em `traducao/notas-degrau-NN.md`. `python3 ferramentas/conferir.py`
  (na pasta da obra) dá ok nos 30; sem mesóclise.
- `obra.py` com a «Sobre»; `revisao.json` (8 decisões); autor novo `sao-joao-climaco` (Catolicismo);
  `conteudo/sao-joao-climaco/escada-do-paraiso.js`; `edicoes/vocabulario/escada-do-paraiso.json` (50 verbetes, `conferir` ok).

## Em andamento (branch `pedido-escada-2`, worktree `~/.cache/claude-wt5-escada-2`)
- Grego das cartas e prólogo (`original/inicio.txt`) e da _Carta ao pastor_ (`original/carta-ao-pastor.txt`) pronto,
  conferido linha a linha nas imagens (método em `original/LEIAME.md`).
- Falta: traduzir os dois (`traducao/inicio.txt`, `traducao/carta-ao-pastor.txt`, com `CONVENCOES.md`; subtítulos
  `##` e marcas `[I.1]` iguais ao grego; `python3 ferramentas/conferir.py`), pôr as duas partes no `obra.py`
  (`('', 'Cartas e prólogo', ['inicio.txt'])` antes do degrau 1, `('', 'Carta ao pastor', ['carta-ao-pastor.txt'])`
  depois do 30), «Sobre», `revisao.json` e vocabulário.

## Para o principal
- Juntar a branch, `node ferramentas/site/gerar.mjs`, Catálogo `obras` (obra nova), `traducoes_revisao.py --revisao`
  e Catálogo `traducoes`; tirar dos pedidos. Nenhuma regra de `_redirects`.

## Falta (melhorias, não impedem publicar)
- Grego: releitura linha a linha dos degraus 26–30 (sobretudo 26.1–54, 26.100–175, 27.8–20, 27.43–53, 28.1–12,
  28.35–40, 30.5–7, 30.13) e das passagens com «[al. …]»; a conferência trocou em série `ἣ` por `ἢ` (quase sempre
  certo: o OCR lia ἢ como ἣ; o relativo ἣ pode ter sido trocado em algum lugar). Dúvidas da conferência:
  `~/.cache/claude-pedidos-0511/escada-do-paraiso/decisoes/ANDAMENTO.md`.
- Tradução: uniformização fina entre os três tradutores (lida por amostra; termos-chave conferidos por contagem);
  passagens obscuras marcadas nas notas: 3.14, 3.24, 4.4, 13.1, 15.3, 15.33, 26.57, 26.65, 27.14, 27.28–29, 30.7.
  Em 30.19 o subtítulo «Exortação breve…» está no meio do bloco, sem `##`.
- Notas gerais (lote futuro).
