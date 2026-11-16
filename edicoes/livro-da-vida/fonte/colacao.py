"""Colação: Silverio 1915 (OCR, bmc_estrutura.json) × de la Fuente BAE 53 (OCR) × Heitz (diplomático).
Grava dl/colacao.json: lista de pontos {sec, par, i (índice da palavra no parágrafo), bmc, bae, auto}."""
import json, re, sys, unicodedata, difflib
from collections import Counter
S = json.load(open('dl/bmc_estrutura.json'))
def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-zñ0-9]', '', w.replace('ñ', 'n'))
TOK = re.compile(r'\S+')
def toks_txt(arq, a, b):
    L = open(arq, encoding='utf-8').read().split('\n')[a-1:b]
    t = '\n'.join(L)
    t = re.sub(r'-\s*\n\s*', '', t)
    return [norm(w) for w in TOK.findall(t) if norm(w)]
bae = toks_txt('dl/bae53.txt', 4628, 19279)
hei = toks_txt('dl/heitz.txt', 1489, 17131)
bmc = []   # (norm, sec, par, i, orig)
for s in S:
    for k, (t, pag) in enumerate(s['pars']):
        for i, w in enumerate(TOK.findall(t)):
            n = norm(w)
            if n: bmc.append((n, s['id'], k, i, w))
freq = Counter(x[0] for x in bmc) + Counter(bae) + Counter(hei)
fb = Counter(x[0] for x in bmc)
sm = difflib.SequenceMatcher(None, [x[0] for x in bmc], bae, autojunk=False)
pontos = []
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal': continue
    a = bmc[i1:i2]; b = bae[j1:j2]
    if op == 'replace' and len(a) == len(b):
        for x, y in zip(a, b):
            if x[0] == y: continue
            auto = None
            if (freq[x[0]] - fb[x[0]] == 0 and fb[x[0]] <= 2) and freq[y] >= 3:
                auto = y
            pontos.append({'sec': x[1], 'par': x[2], 'i': x[3], 'bmc': x[4], 'bae': y, 'auto': auto})
    else:
        for x in a:
            if freq[x[0]] - fb[x[0]] == 0 and fb[x[0]] <= 2:
                pontos.append({'sec': x[1], 'par': x[2], 'i': x[3], 'bmc': x[4], 'bae': ' '.join(b) or '—', 'auto': None})
json.dump(pontos, open('dl/colacao.json', 'w'), ensure_ascii=False, indent=0)
print('palavras bmc', len(bmc), 'bae', len(bae), 'heitz', len(hei), 'pontos', len(pontos), 'auto', sum(1 for p in pontos if p['auto']))
print('raras sem par', sum(1 for x in bmc if freq[x[0]] - fb[x[0]] == 0 and fb[x[0]] <= 2))
