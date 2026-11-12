# Cartas de Anchieta (seleção): estado

Branch `pedido-cartas-anchieta`. Não-ficção, «outras» (`/admin/sugestoes/`, pedido `cartas-anchieta`). Autor novo
`jose-de-anchieta` (área `nao-ficcao`). Modelo: *Vida de Anchieta* (`edicoes/vida-de-anchieta/`).

## Fonte
- Base: *Cartas, informações, fragmentos historicos e sermões do Padre Joseph de Anchieta, S. J. (1554-1594)*,
  Rio, Civilização Brasileira / Academia Brasileira, 1933 (Cartas Jesuíticas III; nota preliminar de Afrânio
  Peixoto †1947, notas de Antônio de Alcântara Machado †1935). Fac-símile: Internet Archive
  `r-19794-v_0000_grav-569_t24-C-R0150` (exemplar da BNP). Folha = página − 3.
- Traduções: a nota preliminar credita a Alcântara Machado (1901–1935) «traslados e traduções de cartas»;
  as notas de cada carta citam versões anteriores (Teixeira de Melo †1907, cônego Januário da Cunha Barbosa
  †1846, Baltasar da Silva Lisboa †1840) e as do prof. João Vieira de Almeida (S. Paulo, 1900; data de
  morte desconhecida). Conferido: a X de 1933 **não** é a de Vieira de Almeida (1900, BBM 4683); a XXXI
  (Breve narração) é a dele: por isso a XXXI e a VII ficaram de fora.
- Seleção: 13 peças, em `pecas.py`.

## Como refazer (na raiz do repo)
1. Baixar o `_jp2.zip` e o `_djvu.xml` do item do IA para `~/.cache/claude-pedidos-0511/cartas-anchieta/dl/`.
2. `python3 edicoes/cartas-anchieta/ocr.py` (duas leituras do Tesseract + a do IA).

## Falta
- voto, conferência nas imagens, grafia de hoje, publicar, vocabulário, revisao.json.
