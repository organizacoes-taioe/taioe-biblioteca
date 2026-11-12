# Vida do Padre José de Anchieta (Pero Rodrigues): estado

Branch `pedido-vida-de-anchieta`. Não-ficção, «biografias e memórias» (`/admin/sugestoes/`). Autor novo
`pero-rodrigues` (área `nao-ficcao`), gênero «Hagiografia». **Pronta para juntar e publicar** (05/11).

## Fonte
- Base: _Annaes da Bibliotheca Nacional_ XIX (1897), pp. 1–49: a cópia de A. F. Barata (Évora, ago. 1896)
  do códice CX/1-17 da Biblioteca de Évora, datado «Na Baia a 3.º de Janeiro de 1607», 25 capítulos em duas
  partes («1.ª PARTE»; «2.ª Parte do Livro 3.º — Dos milagres»), já na ortografia de 1896. A redação longa de
  Alcobaça (BNP ALC. 306, 4 livros, 1608–1609; nota de E. Prado no mesmo volume) não está aqui.
- Fac-símile: Brasiliana USP, https://digital.bbm.usp.br/handle/bbm/6953 (exemplar Mindlin, o vol. XIX sem
  rosto; página impressa = página do PDF − 4). Download em `~/.cache/claude-pedidos-0511/vida-de-anchieta/`.
  O IA não tem o vol. XIX; a BN Digital dá 403.

## Como foi feito (refazer: na raiz do repo)
1. `python3 edicoes/vida-de-anchieta/ocr.py` (três leituras) e `voto.py` (voto por página, em ~/.cache).
2. `1897/NN.txt`: transcrição de 1897 conferida linha a linha nas imagens (subagente Sonnet; dúvidas em
   `1897/DUVIDAS.md`), uma linha por linha impressa.
3. `python3 edicoes/vida-de-anchieta/montar.py --publicar`: grafia de hoje (léxico da São Bernardo refeito +
   dicionário português do sistema; decisões em `decisoes.py`), `atual/cap-NN.txt` e
   `conteudo/pero-rodrigues/vida-de-anchieta.js` (+ linha no `index.html`). Relatórios em `relatorios/`
   (fora do git).
4. Vocabulário: `edicoes/vocabulario/vida-de-anchieta.json` (161 verbetes, `conferir` ok).
5. `revisao.json`: 8 decisões (o texto segue a recomendação de todas).

## Para o principal
- Gerar, Catálogo `obras` (obra nova) e `traducoes_revisao.py --revisao` (8 escolhas novas). Sem `_redirects`.
- Notas gerais: não feitas (vão por lotes).
