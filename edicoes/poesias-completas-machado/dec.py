"""Grava decisões da conferência: python3 dec.py <arquivo.json> id:n=valor ...   (valor: ws, ocr, ws! = 1901 errou e
se corrige pelo WS, ou texto livre; '_' = vazio)."""
import json, os, sys
f = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1])
d = json.load(open(f, encoding='utf-8')) if os.path.exists(f) else {}
for a in sys.argv[2:]:
    k, v = a.split('=', 1)
    d[k] = '' if v == '_' else v
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
print(len(d), 'decisões')
