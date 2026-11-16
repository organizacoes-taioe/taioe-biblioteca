#!/bin/bash
# baixa as folhas jp2 da PG 88 (IA, 1860) e grava PNG em cinza, metade do tamanho
ID=bim_early-english-books-1641-1700_1860_88
D=~/.cache/claude-pedidos-0511/escada-do-paraiso/pag
mkdir -p $D
for n in $(seq $1 $2); do
  f=$(printf "%04d" $n)
  [ -s $D/$f.png ] && continue
  curl -s -L -A 'TaioeBiblioteca/1.0' "https://archive.org/download/$ID/${ID}_jp2.zip/${ID}_jp2%2F${ID}_$f.jp2" -o $D/$f.jp2
  python3 -I -c "
from PIL import Image;import sys
im=Image.open(sys.argv[1]).convert('L');im=im.resize((im.width//2,im.height//2),Image.LANCZOS);im.save(sys.argv[2])" $D/$f.jp2 $D/$f.png && rm $D/$f.jp2
done
