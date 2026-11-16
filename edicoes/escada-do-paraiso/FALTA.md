# Escada do Paraíso (São João Clímaco): estado

Branch `pedido-escada-do-paraiso` do `taioe-biblioteca` (worktree `~/.cache/claude-wt5-escada-do-paraiso`). Regras da
rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`. Trabalho (páginas, OCR, léxico): `~/.cache/claude-pedidos-0511/escada-do-paraiso/`.

## Como o grego é feito (scripts em `ferramentas/`, rodados da pasta de trabalho)
1. `baixar.sh 311 601`: folhas jp2 da PG 88 (IA `bim_early-english-books-1641-1700_1860_88`), PNG cinza meia escala em `pag/`.
2. `ocr-todas.sh` (`ocr.py`, Tesseract grc, as duas colunas) → `ocr/`; `lacunas.py pag ocr` relê as linhas puladas.
   2ª leitura: `ocr-dco.sh` (PDF do DCO, imagens de 912 px ampliadas 3×) → `dcoocr/`.
3. Léxico de formas: `lexico.py` sobre First1KGreek + Perseus (`lex-*.json`); `lex.py` corrige χ/κ, δ/β etc.
4. `linhas.py ocr 0 linhas.json` e `linhas.py dcoocr 315 linhas-dco.json` (coluna grega, sem latim, cabeçalho, notas);
   `montar.py` (hifenização, léxico, 2ª leitura → `blocos.json`, `duvidas.json`); `dividir.py <original/> [degraus]`
   (estrutura por ids em `estrutura.json`, cortes congelados em `cortes.json`; **não apagar `cortes.json`**: a
   tradução está alinhada aos blocos).
5. Conferência nas imagens das dúvidas (pranchas, subagente Sonnet) → `correcoes.json` → repetir 4.

## Feito
- Grego provisório dos 30 degraus em `original/` (OCR + léxico + 2ª leitura; falta a conferência nas imagens das
  ~2.600 palavras duvidosas e das linhas relidas). Estrutura: `ferramentas/estrutura-frases.json` →
  `resolver.py` → `estrutura.json`; títulos em `titulos.json` (lidos nas imagens); cortes em `cortes.json`
  (cópia em `ferramentas/`, **a tradução depende deles**).
- Tradução: degrau 1.

## Falta
- OCR completo, 2ª leitura, estrutura dos 30 degraus, conferência das dúvidas.
- Cartas (João de Raitu e a resposta) e prólogo (`inicio.txt`); degraus 2–30; `obra.py` com a «Sobre»;
  `revisao.json` (~8 decisões); autor `sao-joao-climaco`; vocabulário; `original/LEIAME.md`.
- Pontos a ver na imagem: 1.9 πυρώσεως (πωρώσεως?), 1.31 ἀγαθείας (ἀπαθείας?), 1.26 fim da frase «περικειμένῳ».
- A carta ao pastor (PG 88.1165–1210) fica para depois, se couber.
