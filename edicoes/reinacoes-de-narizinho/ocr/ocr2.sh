#!/bin/bash
# Segunda leitura: Tesseract (por, --psm 6) da imagem original, sem normalização. Saída: tess2/NNN.tsv
D=~/.cache/claude-pedidos-2611/reinacoes-de-narizinho
R=~/.cache/tesseract-local/raiz
export LD_LIBRARY_PATH=$R/usr/lib/x86_64-linux-gnu TESSDATA_PREFIX=$R/usr/share/tesseract-ocr/5/tessdata OMP_THREAD_LIMIT=1
mkdir -p $D/tess2
for n in $(seq ${1:-9} ${2:-321}); do
  f=$(printf "%03d" $n)
  [ -s "$D/tess2/$f.tsv" ] && continue
  $R/usr/bin/tesseract "$D/dl/pag/$f.jpg" "$D/tess2/$f" -l por --psm 6 tsv >/dev/null 2>&1
done
echo fim
