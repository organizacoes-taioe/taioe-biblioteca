# O Uraguai: andamento

Pedido de 2026-11-23 (branch `pedido-o-uraguai`). Base: 1ª edição (Lisboa, Régia Oficina Tipográfica, 1769).

## Feito
- Testemunhos: dois exemplares de 1769 no Internet Archive (`ouruaguaypoema00gama`, Boston Public Library, o
  mesmo do DjVu do Wikisource; `ouraguaypoema00gama`, Fisher/Toronto; página de Toronto = Boston + 6,
  `mapa_tor.json`), com a camada OCR dos PDFs e o Tesseract em cada um (quatro leituras); a transcrição de 1769 do
  Wikisource («O Uraguay», 48 páginas revisadas; as outras 55 são cópia do texto moderno com ſ, sem as notas); o
  texto moderno do Wikisource («O Uraguai», igual ao do Domínio Público).
- Versos: 1.377 (244, 365, 329, 289, 150). O texto moderno tinha 1.380: três linhas de nota metidas entre os
  versos (II, depois de «Aqui não temos»; IV, «O bom padre. Balda.»), que saíram.
- `texto.txt` pronto (montar.py): lição e pontuação de 1769; 30 palavras do texto moderno corrigidas pela 1ª
  edição, conferidas nas imagens (decisoes.json); pontuação por voto e 220 pontos conferidos nas imagens
  (pontuacao_conferida.json).
- Nenhum erro de impressão de 1769 achado nos versos até aqui.

## Falta
- Notas do autor (rodapé de 1769, ~85 notas), soneto ao Conde de Oeiras, epígrafes, os dois sonetos «Ao Autor».
- publicar.py, autor, vocabulário, revisao.json, CONVENCOES.md.

## Como refazer
Cache em `ferramentas/cache/o-uraguai/` (ou `URAGUAI_CACHE`); passo a passo no topo de `montar.py`.
