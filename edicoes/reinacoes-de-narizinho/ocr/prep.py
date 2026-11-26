"""Normaliza o fundo de uma página fotografada (divide pelo fundo borrado). uso: prep.py entrada saída"""
import sys
import numpy as np
from PIL import Image, ImageFilter
im = Image.open(sys.argv[1]).convert('L')
fundo = im.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(25))
a = np.asarray(im, dtype=np.float32); b = np.asarray(fundo, dtype=np.float32)
c = np.clip(a * 255.0 / np.maximum(b, 1), 0, 255)
c = np.where(c > 175, 255, np.where(c < 110, 0, c)).astype(np.uint8)
Image.fromarray(c).save(sys.argv[2])
