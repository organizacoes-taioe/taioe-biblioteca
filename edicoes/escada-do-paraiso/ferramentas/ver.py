"""Recorta uma região de uma folha: ver.py <folha> <x0> <y0> <x1> <y1> <saida.png> [escala]"""
import sys
from PIL import Image
f, x0, y0, x1, y1, out = sys.argv[1:7]
e = float(sys.argv[7]) if len(sys.argv) > 7 else 0.5
im = Image.open('/home/geremias/.cache/claude-pedidos-0511/escada-do-paraiso/pag/%04d.png' % int(f)).crop(tuple(map(int, (x0, y0, x1, y1))))
im.resize((int(im.width * e), int(im.height * e))).save(out)
