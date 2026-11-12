# Cartas do Brasil (Nóbrega): estado

Branch `pedido-cartas-nobrega`. Não-ficção, «outras» (`/admin/sugestoes/`). Autor novo `manuel-da-nobrega`.
Em andamento (12/11): fonte e OCR prontos, texto por carta montado; falta a conferência nas imagens, o resto abaixo.

## Fonte
- Base: *Cartas do Brasil do padre Manoel da Nobrega (1549–1560)* (Cartas Jesuíticas I), org. Alfredo do Valle Cabral
  (†1894), Rio de Janeiro, Imprensa Nacional, 1886. Fac-símile da Brasiliana USP, https://digital.bbm.usp.br/handle/bbm/8016
  (PDF `45000009662_Output.o.pdf`; página impressa = página do PDF − 16); o mesmo volume, de menor resolução, no Internet
  Archive (`cartaaaapdrmnelnobrg`). A edição da ABL de 1931 (Afrânio Peixoto, Rodolfo Garcia) repete o texto, não foi usada.
- O volume traz 21 cartas (1549–1560); as IV e VI são traduções do italiano feitas pelo editor e ficam de fora: 19 cartas.
  O *Diálogo sobre a conversão do gentio* e as cartas de 1561 a 1570 não estão neste volume.
- Download em `~/.cache/claude-pedidos-0511/cartas-nobrega/dl/`.

## Como refazer (na raiz do repo)
1. `python3 -I edicoes/cartas-nobrega/ocr.py`: extrai a máscara JBIG2 de 900 dpi de cada página, lê a 450 dpi (A) e 600 dpi (B)
   com o Tesseract e a camada de texto do PDF (C).
2. `python3 -I edicoes/cartas-nobrega/voto.py`: voto por palavra (grava `voto/<p>.txt` em ~/.cache; tira cabeçalho e notas).
3. `python3 -I edicoes/cartas-nobrega/transcricao.py`: `1886/<p>.txt`, as dúvidas resolvidas por freqüência.
4. `python3 -I edicoes/cartas-nobrega/montar.py [--publicar]`: grafia de hoje (`decisoes.py`; limites das cartas em `cartas.py`).
