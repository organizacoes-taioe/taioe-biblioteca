# Auto da Barca do Inferno: convenções da edição

Texto da Copilação de 1562 (reimpressão de Hamburgo, 1834) na grafia brasileira de hoje, passado a
limpo à mão a partir de duas cópias OCR da edição de 1834 (a terceira desempata). Fontes em
`ferramentas/cache/barca-do-inferno/` (fora do git); o Wikisource (folheto de c. 1518) serviu só para
entender versos estragados pelo OCR, nunca como lição.

- `texto.txt` já está no formato do site: fala «@ Nome», verso «| », rubrica em _itálico_, blocos
  separados por linha em branco. `publicar.py` divide em dez partes pela chegada de cada personagem.
- Grafia como em `../os-lusiadas/CONVENCOES.md`: muda a maneira de escrever, a forma fica (pera, assi,
  cousa, dous, mi, inda, samicas, eramá, muitieramá, bo'hora, jentar, encubri, re-não).
- Latim macarrônico e castelhano ficam como na edição de 1834, só com a grafia corrigida do OCR.
- Emenda: «Ora venho a caro a ré» (1834) → «Ora venha o caro a ré» (folheto).
- Decisão para o Gere (`revisao.json`): Copilação × folheto.
