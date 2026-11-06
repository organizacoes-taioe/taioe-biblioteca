# Narrativa da vida de Frederick Douglass: o que falta

Branch `pedido-narrativa-douglass` (worktree `~/.cache/claude-wt5-narrativa-douglass`). Regras da rodada:
`~/.cache/claude-pedidos-0511/BRIEF.md`. Downloads e scripts (dividir, corrigir, comparar com os OCRs, conferir
tradução × original): `~/.cache/claude-pedidos-0511/narrativa-douglass/`.

Pronto (2026-11-06): texto inglês de 1845 (`original/`, LEIAME), tradução das 14 partes (prefácio, carta, I–XI,
apêndice; 38.597 palavras), versos pelo Versificador (`versos/`, LEIA.md), `revisao.json` (9 decisões, todas já
aplicadas na recomendação), `CONVENCOES.md`, vocabulário (38 verbetes, `conferir` ok), `conteudo/` gerado pelo
`traducoes.py`, autor novo `frederick-douglass` em `conteudo/autores.js`. O `gerar.mjs` e o `conferir.mjs` rodam sem erro.

Falta (do principal): juntar a branch, `python3 ferramentas/traducoes.py narrativa-douglass` se mudar algo,
gerar o site, Catálogo `obras`, `traducoes_revisao.py --revisao` (Catálogo `traducoes`), tirar dos pedidos. Notas
gerais: entram por lote, depois.

Não feito: revisão por um segundo leitor (crítico) da prosa; a conferência de 1845 cobriu os pontos em que os dois
OCRs concordam contra o Gutenberg, não uma leitura corrida das imagens (pontuação e maiúsculas são as do Gutenberg).
