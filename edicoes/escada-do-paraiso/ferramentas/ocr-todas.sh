cd ~/.cache/claude-pedidos-0511/escada-do-paraiso
for p in pag/*.png; do b=$(basename $p .png); [ -s ocr/$b.json ] || echo $b; done | xargs -P 3 -I{} python3 -I scripts/ocr.py pag/{}.png ocr/{}.json
