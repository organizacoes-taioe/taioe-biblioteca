#!/bin/bash
# Tesseract (por, --psm 3) das páginas do fac-símile de 1931 (imagens nativas extraídas com pdfimages -j,
# fundo normalizado por prep.py), uma por vez. Saída: tess/NNN.txt e tess/NNN.tsv
D=~/.cache/claude-pedidos-2611/reinacoes-de-narizinho
R=~/.cache/tesseract-local/raiz
export LD_LIBRARY_PATH=$R/usr/lib/x86_64-linux-gnu TESSDATA_PREFIX=$R/usr/share/tesseract-ocr/5/tessdata OMP_THREAD_LIMIT=1
mkdir -p $D/norm
for n in $(seq ${1:-9} ${2:-321}); do
  f=$(printf "%03d" $n)
  [ -s "$D/tess/$f.tsv" ] && continue
  [ -s "$D/norm/$f.png" ] || python3 -I $D/scr/prep.py "$D/dl/pag/$f.jpg" "$D/norm/$f.png"
  $R/usr/bin/tesseract "$D/norm/$f.png" "$D/tess/$f" -l por --psm 3 txt tsv >/dev/null 2>&1
done
echo fim
