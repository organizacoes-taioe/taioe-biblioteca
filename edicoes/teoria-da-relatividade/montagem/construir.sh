#!/bin/bash
# Monta o alemão da 5ª ed. (1920) em edicoes/teoria-da-relatividade/original/ a partir das fontes baixadas.
set -e
R=~/.cache/claude-pedidos-0511/teoria-da-relatividade
O=~/.cache/claude-wt5-teoria-da-relatividade/edicoes/teoria-da-relatividade/original
cd $R
python3 -I scripts/montar_g.py dl/g77850.txt g >/dev/null
cp g/g-vorwort.txt $O/prefacio.txt; cp g/g-teil-1.txt $O/parte-1.txt; cp g/g-teil-2.txt $O/parte-2.txt
python3 -I scripts/aplicar1920.py $O
python3 -I scripts/ocr.py dl/bub_gb_kTdWAAAAMAAJ.txt 3521 3871 fix-p3.tsv $O/parte-3.txt
python3 -I scripts/ocr.py dl/berdiespezielle00unkngoog.txt 4485 4830 fix-anh.tsv $O/apendice.txt
python3 -I scripts/italico.py $O/apendice.txt
python3 -I scripts/ocr.py dl/bub_gb_kTdWAAAAMAAJ.txt 116 122 fix-nach.tsv nach.txt
printf '\n' >> $O/prefacio.txt; cat nach.txt >> $O/prefacio.txt
python3 -I scripts/pos.py $O
python3 -I scripts/renumerar.py $O/*.txt
