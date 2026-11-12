"""Mostra o trecho do OCR (a ou b, já juntado) entre duas âncoras. Uso: trecho.py a|b 'inicio' n_chars"""
import re, sys
f = {'a': 'berdiespezielle00unkngoog.txt', 'b': 'bub_gb_kTdWAAAAMAAJ.txt'}[sys.argv[1]]
t = open('/home/geremias/.cache/claude-pedidos-0511/teoria-da-relatividade/dl/' + f, encoding='utf-8').read()
t = re.sub(r'Digitized\s+by\s+(Google)?', ' ', t)
t = re.sub(r'-\s*\n\s*', '', t); t = re.sub(r'\s+', ' ', t)
i = t.find(sys.argv[2]); print(t[i:i + int(sys.argv[3])] if i >= 0 else '?')
