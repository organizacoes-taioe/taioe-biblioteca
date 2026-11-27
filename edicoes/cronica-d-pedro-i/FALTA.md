# Crônica de D. Pedro I (Fernão Lopes): estado

Branch `pedido-cronica-d-pedro-i`. Não-ficção, gênero «História»; autor novo `fernao-lopes` (entrada em
`conteudo/autores.js`, já no commit). **Pronta para juntar e publicar** (27/11).

## Para o principal (na raiz do repo, nesta ordem)
1. `python3 edicoes/cronica-d-pedro-i/publicar.py` → grava `conteudo/fernao-lopes/cronica-de-d-pedro-i.js` e a linha do `index.html`.
2. `node ferramentas/site/gerar.mjs` e `node ferramentas/site/conferir.mjs` (passaram na worktree: «tudo certo»).
3. Catálogo `obras` (obra nova); `python3 ferramentas/traducoes_revisao.py --revisao ../infra/dados/paginas` (7 escolhas). Sem `_redirects`.

## O que está na pasta (vai ao git)
- `original/parte-NN.txt` (00 prólogo, 01–44 capítulos): texto de 1816 (Collecção de livros ineditos, t. IV, Academia,
  pp. 3–116), ſ → s, sem as notas de variantes nem as aspas de linha. `atualizado/parte-NN.txt`: grafia de hoje, mesmos
  parágrafos (os da edição de 1895). `titulos.json`: títulos (1816 e hoje). `sobre.md`: a página «Sobre».
- `revisao.json`: 7 decisões (base, original ao lado, parágrafos, palavras antigas, el-rei, nomes, grã/grão).
- Vocabulário: `edicoes/vocabulario/cronica-d-pedro-i.json`, 276 verbetes, `conferir` ok.
- Scripts da cadeia (só para refazer o texto; o principal não precisa): `linhas.py` (hOCR → linhas) → `limpar.py`
  (cabeçalho, notas de rodapé, reclamo, títulos, aspas) → `colacao.py` (4 testemunhos alinhados ao pivô D) →
  `estabelecer.py` (escolha por apoio, s longo e ligaduras, alinhamento com 1895) → `montar.py` (correções de
  `decisoes.py`, OCR por tipo, junções, títulos, `modernizar.py` + `grafia.py` + `grafia-cauda.tsv`, parágrafos de
  1895). Entradas fora do git, em `/mnt/arquivos/claude-tmp/pedidos-2711b/cronica-d-pedro-i/ia/` (só neste PC): os hOCR
  do Internet Archive (`collecadeliv04corruoft` = B, `collecadelivrosi04acad` = A, `collecadeliv03corr` = C,
  `gri_33125011168180` = D, 2ª ed. 1925, com as pp. 121–122 escaneadas duas vezes) e o Gutenberg 16633 (`pg16633.txt`).
  Refazer: `linhas.py` e `limpar.py` em cada testemunho, depois `colacao.py <pasta>`, `estabelecer.py <pasta>`,
  `montar.py <pasta>`. As posições de `decisoes.CORRECOES` valem para o `estab.json` de 27/11.

## Limites conhecidos
- O lado «Original (1816)» vem de OCR colacionado (4 leituras + 1895); ~300 pontos e os 44 títulos conferidos nas
  imagens. Devem sobrar erros miúdos de letra (ordem de grandeza: 1 a cada poucas centenas de palavras), sobretudo
  ſ/f/l, c/e, acentos e palavras juntas ou separadas. Confiar mais no lado moderno, que passou também pela leitura de 1895.
- Pontuação: a de 1816 pela maioria das leituras; vírgula antes de maiúscula virou ponto.
- Notas gerais: não feitas (vão por lotes).
- Dúvidas de leitura que ficaram como estão: «dic» (cap. XL?), «cambos» (1895 «campos»), «desassouho», «emadeo» (→ enadeu),
  «Moutoyo», «Seirom», «afremosenta» (arcaica, fica).
