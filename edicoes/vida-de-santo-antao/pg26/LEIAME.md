# O grego da Vida de Santo Antão conferido com a PG 26

O grego ao lado é `original/vida.txt` (Migne, PG 26, na digitação do TLG), conferido em 2026-10-26
com o fac-símile do Internet Archive (`patrologiae_cursus_completus_gr_vol_026`, folhas 435–506,
colunas 837–976). O OCR do próprio Archive leu tudo como grego e não serve.

- `antao_colunas.py`: recorta a coluna grega de cada folha (ela alterna entre a esquerda e a
  direita; embaixo vêm Evágrio e as notas) e a reconhece com o Tesseract `grc` (o modelo foi
  extraído sem `sudo` em `~/.cache/tesseract-local/raiz`, como o `por`).
- `antao.py`: alinha o OCR ao texto e lista as divergências. 16.416 das 18.400 palavras iguais
  letra a letra; nas outras, só erros do OCR (κ→χ, β→δ, ν→υ, π→τ). Corrigido «ἐξ ἔστω» (cap. 65).
