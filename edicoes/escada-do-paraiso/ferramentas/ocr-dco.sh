cd ~/.cache/claude-pedidos-0511/escada-do-paraiso
um() { b=$1; [ -s dcoocr/$b.json ] && return; python3 -I -c "
from PIL import Image;import sys;im=Image.open(sys.argv[1]).convert('L');im=im.resize((im.width*3,im.height*3),Image.LANCZOS);im.save(sys.argv[2])" dco/p-$b.jpg dco/u-$b.png && python3 -I scripts/ocr.py dco/u-$b.png dcoocr/$b.json; rm -f dco/u-$b.png; }
export -f um
ls dco | grep '^p-' | sed 's/p-\(.*\)\.jpg/\1/' | xargs -P 3 -I{} bash -c 'um {}'
