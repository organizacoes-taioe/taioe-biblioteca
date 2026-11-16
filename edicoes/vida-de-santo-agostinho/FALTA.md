# O que falta (Vida de Santo Agostinho, São Possídio)

Branch `pedido-vida-de-santo-agostinho`. Base: PL 32 (Migne, 1841; texto dos Maurinos), col. 33–66; o cap. 30
completado pela Ep. 228, nn. 10–14, da PL 33 (col. 1017–1019), onde a PL 32 corta a carta («Caetera videre est in
tomo secundo, epist. 228»). Weiskotten (Princeton, 1919) só serviu de esqueleto e para conferir: data de morte dele
não achada, e a edição é crítica.

## Feito
- Leituras OCR baixadas e alinhadas (scripts em `texto/scripts/`, dados em `~/.cache/claude-pedidos-0511/vida-de-santo-agostinho/`):
  PL 32 de 1845 (A), 1841 t. 1–2 (B), 1841 t. 1 (C), 1844 Google (G); PL 33 de 1845 e 1841 para a carta;
  Weiskotten em dois exemplares (W, W2). `fluxos.py` → `alinhar.py` → `votar.py` → (`fluxos_ep.py`,
  `alinhar_ep.py`, `votar.py` na carta) → `juntar.py` → `compor.py` → `render.py` / `colunas.py`.
- Texto provisório por coluna do fac-símile de 1845 em `texto/colunas/NN-plVOL-fPAG-cCOL.txt`.

## Falta
1. Conferência visual de cada coluna com o fac-símile (recortes pelo IIIF: `texto/colunas/urls.tsv`;
   baixar com `texto/scripts/baixar_imgs.sh`): corrigir os `.txt` até baterem com a impressão (sem notas, sem as
   referências bíblicas entre parênteses dos Maurinos, sem os sumários dos capítulos; linha em branco = parágrafo).
2. Juntar as colunas em `original/vita.txt` (um bloco por parágrafo; `[n]` no primeiro de cada capítulo; `[0]` o prefácio).
3. Tradução em `traducao/vita.txt`, mesmos parágrafos; `obra.py`, `CONVENCOES.md`, `original/LEIAME.md`,
   `revisao.json` (6–8 pontos), vocabulário `edicoes/vocabulario/vida-de-santo-agostinho.json`, autor `sao-possidio`
   em `conteudo/autores.js`; `python3 ferramentas/traducoes.py vida-de-santo-agostinho`; gerar e conferir o site.
