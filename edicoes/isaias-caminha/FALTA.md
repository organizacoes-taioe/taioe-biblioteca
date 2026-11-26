# Isaías Caminha — o que falta (branch `pedido-isaias-caminha`)

Fontes (em `ferramentas/cache/isaias-caminha/`, fora do git; baixar de novo se sumirem):
- `bbm4808-1917.pdf`: 2ª ed., 1917 (edição-base), https://digital.bbm.usp.br/handle/bbm/4808 (PDF 001228_COMPLETO.pdf);
  «Breve notícia» nas p. 11–17 do PDF, romance 19–238, errata na 239 (5 emendas). Página do livro = PDF − 4.
- `bbm4799-1909.pdf`: 1ª ed., 1909, https://digital.bbm.usp.br/handle/bbm/4799 (001179_COMPLETO.pdf), para as mudanças.
- `c17.txt`, `c09.txt`: `pdftotext` dos dois PDFs (a camada de OCR da Brasiliana).
- `ws_moderno.json`: Wikisource pt (API, as 15 páginas); `bveb.pdf`/`bveb.txt` (`pdftotext -layout`):
  https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/lima-barreto/isaias-caminha.pdf
- `tess-bbm4808-1917/`: `PROCESSOS=2 systemd-run --user --scope --slice=pesado.slice -q -- python3 edicoes/isaias-caminha/tesseract.py bbm4808-1917:11-239`

Etapas:
1. [x] fontes achadas e baixadas; config.py com os leitores.
2. [ ] `python3 ferramentas/texto.py isaias-caminha`; ler `relatorios/`.
3. [ ] conferência nas imagens dos pontos sem apoio (`conferir.py`, `conferencia.json`).
4. [ ] errata de 1917 (EMENDAS 'erro'); erros tipográficos de 1917.
5. [ ] Tesseract de 1909 e `mudancas.py` (lista 1909 → 1917 na «Sobre»).
6. [ ] notas.py («Sobre»), `--publicar`, gerar/conferir o site, revisao.json (1909 × 1917).
7. [ ] vocabulário `edicoes/vocabulario/isaias-caminha.json`.
