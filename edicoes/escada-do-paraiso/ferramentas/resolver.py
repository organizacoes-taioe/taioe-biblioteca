"""resolver.py: lê estrutura-frases.json ({n: [[frase_ini, frase_fim, subtítulo?], …]}), acha cada frase no texto
montado (palavras seguidas; a 1ª ocorrência depois da anterior) e grava estrutura.json com os ids."""
import json, os, sys, re, unicodedata
A = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso/')
b = json.load(open(A + 'blocos.json', encoding='utf-8'))
plano = [(w, t) for x in b for w, t in x['pal'] if t]
def norm(w): return re.sub(r'[^\w]', '', unicodedata.normalize('NFD', w.lower())).replace('ς', 'σ')
def basev(w): return ''.join(c for c in norm(w) if unicodedata.category(c) != 'Mn')
N = [basev(w) for w, t in plano]
def acha(frase, desde):
    dep = frase.startswith('depois:')
    f = [basev(x) for x in frase.replace('depois:', '').split()]
    f = [x for x in f if x]
    for k in range(desde, len(N) - len(f)):
        if all(N[k + i] == f[i] for i in range(len(f))): return k + len(f) if dep else k
    raise SystemExit('não achei: %s (desde %d)' % (frase, desde))
E = json.load(open(A + 'estrutura-frases.json', encoding='utf-8'))
out, pos = {}, 0
for n in sorted(E, key=int):
    fat = []
    for sl in E[n]:
        a = acha(sl[0], pos); z = acha(sl[1], a + 1); pos = z
        fat.append([plano[a][1], plano[z][1]] + sl[2:])
    out[n] = fat
json.dump(out, open(A + 'estrutura.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(out), 'degraus')
