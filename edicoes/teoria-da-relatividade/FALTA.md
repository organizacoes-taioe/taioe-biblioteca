# Teoria da relatividade (Einstein): o que falta

Branch `pedido-teoria-da-relatividade`. Rascunhos e scripts fora do git em `~/.cache/claude-pedidos-0511/teoria-da-relatividade/`
(`dl/`: Gutenberg 77850, 1ª ed. 1917, e os dois exemplares da 5ª ed., 1920, do Internet Archive, PDF e OCR;
`scripts/montar_g.py` divide o Gutenberg; `scripts/diff1920*.py` lista as mudanças de 1917 → 1920; `pag/`: páginas em PNG).

Edição-base: **5ª ed. (Vieweg, 1920)**, com o «Nachtrag zur dritten Auflage», a parte III («Betrachtungen über die Welt
als Ganzes», §§ 30–32) e o Anhang (derivação de Lorentz e mundo de Minkowski). Livre no Brasil (†1955) e nos EUA
(publicada antes de 1931). O texto de 1917 (Gutenberg, revisado pelo DP) é a base das partes I e II, com as mudanças
de 1920 aplicadas (lista em `diff1920.txt` no rascunho); parte III, Anhang e notas novas vêm do OCR das duas cópias
de 1920, conferido nas imagens. **O alemão só entra por script** (nunca colado à mão).

Estado (2026-11-12): **pronta para publicar** (falta só a revisão final de um leitor, ver abaixo).
- [x] alemão montado por script: `bash montagem/construir.sh` (os caminhos apontam para `~/.cache/claude-pedidos-0511/teoria-da-relatividade/`,
  onde ficam os downloads; o original/ inteiro sai de lá). Detalhe em `original/LEIAME.md`.
- [x] tradução completa: prefácio + adendo, partes I–III (§§ 1–32), apêndice; `CONVENCOES.md`, `obra.py`,
  `revisao.json` (9 decisões), `edicoes/vocabulario/teoria-da-relatividade.json` (12 verbetes, `conferir` ok),
  `conteudo/` gravado por `traducoes.py teoria-da-relatividade`; gerar + conferir sem erro.
- [x] figuras: 5 SVG em `conteudo/img/teoria-da-relatividade/` (Fig. 1 em alemão e português, 2, 3, tubo de Fizeau).

Para o principal:
- **Gerador** (`ferramentas/site/gerar.mjs`): bloco `{fig pasta/nome}` vira `<figure class="figura"><img …>` e
  `conteudo/img/` é copiado para `public/biblioteca/img/` (`img` entrou nos RESERVADOS); `divisao.marcas = false`
  agora tira as marcas `{§ …}` também do original ao lado. CSS das figuras no fim de `ferramentas/site/estilo.css`
  (invertidas no tema escuro). O `de` já estava em `LINGUAS`.
- Autor novo `albert-einstein` no fim de `conteudo/autores.js` (resolver por união; conferir o «});»).
- Gerar, PR, Catálogo `obras`, merge; `traducoes_revisao.py --revisao` para as 9 decisões; tirar dos pedidos.
- Notas gerais: ficam para os lotes.
