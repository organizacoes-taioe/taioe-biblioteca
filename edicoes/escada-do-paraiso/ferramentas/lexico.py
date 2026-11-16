"""Monta léxico de formas gregas (contagem) a partir de XMLs TEI baixados. Uso: lexico.py <pasta> <saida.json> [mais.json…]"""
import sys, os, re, json, unicodedata, collections
cnt = collections.Counter()
pal = re.compile(r"[Ͱ-Ͽἀ-῿’᾽']+")
for raiz, _, arqs in os.walk(sys.argv[1]):
    for a in arqs:
        if not a.endswith('.xml'): continue
        s = open(os.path.join(raiz, a), encoding='utf-8', errors='ignore').read()
        i = s.find('<body'); s = s[i:] if i >= 0 else s
        s = re.sub(r'<note.*?</note>', ' ', s, flags=re.S)
        s = re.sub(r'<[^>]+>', ' ', s)
        s = unicodedata.normalize('NFC', s)
        for w in pal.findall(s):
            w = w.strip("'’᾽")
            if len(w) > 0: cnt[w] += 1
json.dump(cnt, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
print(len(cnt), sum(cnt.values()))
