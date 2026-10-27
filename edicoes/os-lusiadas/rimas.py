"""Confere as rimas de cada oitava (ABABABCC) pelas últimas letras; sobram as rimas imperfeitas de Camões."""
import re, unicodedata
def sem(w): return ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn')
def chave(l):
    w = re.findall(r"[^\W\d_]+", l)[-1].lower()
    w = sem(w).replace('ç', 's').replace('ss', 's').replace('z', 's').replace('x', 's')
    w = re.sub(r'am$', 'ao', w)
    return w[-3:]
def conferir(est):
    ruins = []
    for c, n, ls in est:
        if len(ls) != 8: ruins.append((c, n, 'linhas', len(ls))); continue
        k = [chave(l) for l in ls]
        for g in [(0, 2, 4), (1, 3, 5), (6, 7)]:
            ks = {k[i][-2:] for i in g}
            if len(ks) > 1: ruins.append((c, n, [ls[i].split()[-1] for i in g]))
    return ruins
