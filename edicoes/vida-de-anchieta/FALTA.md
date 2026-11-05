# Vida do Padre José de Anchieta (Pero Rodrigues): o que falta

Branch `pedido-vida-de-anchieta`. Não-ficção, «biografias e memórias» (`/admin/sugestoes/`). Autor novo
`pero-rodrigues`, área `nao-ficcao`.

## Fonte (achada em 05/11)
- Edição-base: _Annaes da Bibliotheca Nacional do Rio de Janeiro_, vol. XIX (1897), pp. 1–49: a cópia de
  A. F. Barata (Évora, ago. 1896) do códice da Biblioteca de Évora, datado «Na Baia a 30 de Janeiro de
  1607», 25 capítulos («Fim do Livro 3.º»), já na ortografia de 1896 com algumas formas antigas deixadas
  de propósito (giolho, antre, devação). Nota de Eduardo Prado (Lisboa, 1897) sobre a cópia mais longa de
  Alcobaça (BNP, ALC. 306, 4 livros, 1608–1609), que **não** está nesse volume.
- Fac-símile: Brasiliana USP, https://digital.bbm.usp.br/handle/bbm/6953 (exemplar José Mindlin, o volume
  XIX encadernado sem rosto; PDF 276 p.; página impressa = página do PDF − 4). Baixado em
  `~/.cache/claude-pedidos-0511/vida-de-anchieta/dl/bbm6953.pdf`.
- O IA não tem o vol. XIX (tem XVIII, XX…); a BN Digital dá 403.

## Feito
- `ocr.py`: três leituras (camada do PDF, Tesseract 300 dpi psm 4, Tesseract 400 dpi limiarizado psm 6).

## Falta
1. Voto das três leituras → transcrição de 1897 por página, com as dúvidas marcadas.
2. Conferência página a página nas imagens → `1897/` limpo.
3. Grafia de hoje (`grafia.py`) → `atual/`; ambíguos decididos à mão.
4. `montar.py --publicar` → `conteudo/pero-rodrigues/vida-de-anchieta.js`, autor em `autores.js`, linha no
   `index.html`; vocabulário; `revisao.json`; gerar e conferir o site.
