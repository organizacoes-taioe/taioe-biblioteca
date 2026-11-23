# O Uraguai: andamento

Pedido de 2026-11-23 (branch `pedido-o-uraguai`). Base: 1ª edição (Lisboa, Régia Oficina Tipográfica, 1769).
Regras e formato em `CONVENCOES.md`.

## Feito (2026-11-23)
- Testemunhos: dois exemplares de 1769 no Internet Archive (`ouruaguaypoema00gama`, Boston Public Library, o
  mesmo do DjVu do Wikisource; `ouraguaypoema00gama`, Fisher/Toronto; página de Toronto = Boston + 6,
  `mapa_tor.json`), com a camada OCR dos PDFs e o Tesseract em cada um (quatro leituras); a transcrição de 1769 do
  Wikisource («O Uraguay», 48 páginas revisadas; as outras 55 são cópia do texto moderno com ſ, sem as notas); o
  texto moderno do Wikisource («O Uraguai», igual ao do Domínio Público).
- Versos: 1.377 (244, 365, 329, 289, 150). O texto moderno tinha 1.380: três linhas de nota entre os versos.
- `texto.txt`: lição e pontuação de 1769; 27 lições corrigem o texto moderno (decisoes.json), todas vistas nas
  imagens; ~250 pontos de pontuação decididos nas imagens (pontuacao_conferida.json).
- Notas: 88, transcritas das imagens (`notas1769.txt`, um subagente Sonnet com as quatro leituras OCR e o WS de
  ajuda; conferidas por amostra) e passadas à grafia de hoje por `notas.py` → `notas.txt`.
- Dedicatória (`abertura.txt`) e os sonetos «Ao Autor» (`fecho.txt`), passados à mão das imagens.
- `publicar.py` (via `montar.py --publicar`), autor `basilio-da-gama` em `conteudo/autores.js`,
  vocabulário (`edicoes/vocabulario/o-uraguai.json`, 81 verbetes, `conferir` ok), `revisao.json` (5 decisões).
- Gerado e conferido no local (`gerar.mjs` e `conferir.mjs` ok; 7 partes, ~13.700 palavras).

## Falta (para o principal)
- `python3 edicoes/o-uraguai/montar.py --publicar` (grava `conteudo/basilio-da-gama/o-uraguai.js` e a linha do
  `index.html`), gerar o site, Catálogo `obras` e `traducoes` (o revisao.json) no teste e na produção.
- O número do verso à margem usa `{e N}`, cujo `title` no gerador diz «estrofe N»; se quiser, trocar no
  `gerar.mjs` o título para «verso» quando a obra for O Uraguai (não mexi no gerador).
- Notas gerais (lote futuro) e a revisão das 5 decisões pelo Gere.

## Como refazer
Cache em `ferramentas/cache/o-uraguai/` (ou `URAGUAI_CACHE`); só neste PC, em
`~/.cache/claude-pedidos-2311/tmp-o-uraguai/`. Passo a passo no topo de `montar.py`. `montar.py --publicar`
não precisa do cache (lê texto.txt, notas.txt, abertura.txt, fecho.txt).
