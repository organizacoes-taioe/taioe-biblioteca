"""Correção por regra dos erros de OCR de Silverio 1915 (bmc_estrutura.json → bmc_corr.json), com registro
em dl/correcoes.tsv e as dúvidas que sobram em dl/duvidas.tsv (palavra rara sem apoio em BAE 53 nem Heitz)."""
import json, re, unicodedata
from collections import Counter
S = json.load(open('dl/bmc_estrutura.json'))
def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-zñ0-9]', '', w.replace('ñ', 'n'))
def txt_norms(arq, a, b):
    t = '\n'.join(open(arq, encoding='utf-8').read().split('\n')[a-1:b])
    t = re.sub(r'-\s*\n\s*', '', t)
    return Counter(norm(w) for w in t.split())
outros = txt_norms('dl/bae53.txt', 4628, 19279) + txt_norms('dl/heitz.txt', 1489, 17131)
RX = re.compile(r'^([^\wÁÉÍÓÚáéíóúÑñÜü]*)(.*?)([^\wÁÉÍÓÚáéíóúÑñÜü]*)$')
cont = Counter()
for s in S:
    for t, _ in s['pars']:
        for w in t.split():
            m = RX.match(w); cont[m.group(2).lower()] += 1
def conhecida(c):
    return cont[c.lower()] >= 3
SUBS = [('fí', 'ñ'), ('fi', 'ñ'), ('ri', 'n'), ('q', 'g'), ('cj', 'q'), ('tj', 'q'), ('ij', 'y'), ('ii', 'n'), ('ti', 'n'), ('/', 'j'), ('/', 'l'), ('c', 'o'), ('r', 'i'), ('g', 'y'), ('rn', 'm'), ('tn', 'm'), ('ni', 'm'), ('in', 'm'), ('f', 't'), ('c', 'e'), ('e', 'c'), ('l', 'i'), ('i', 'l'),
        ('1', 'l'), ('li', 'h'), ('Q', 'O'), ('fc', 't'), ('$', 't'), ('9', 'y'), ('o', 'e'), ('a', 'e'), ('h', 'b'), ('b', 'h'),
        ('u', 'n'), ('n', 'u'), ('í', 'i'), ('i', 'í'), ('ü', 'u'), ('é', 'e'), ('e', 'é'), ('ó', 'o'), ('o', 'ó'), ('á', 'a'), ('a', 'á'),
        ('v', 'y'), ('y', 'v'), ('s', 'e'), ('t', 'f'), ('ñ', 'A'), ('M', 'Ah'), ('I', 'l'), ('J', 'T'), ('L', 't'), ('L', 'T'), ('j', 'i')]
def candidatos(c):
    out = set()
    for a, b in SUBS:
        if a in c:
            out.add(c.replace(a, b))
            for k in [m.start() for m in re.finditer(re.escape(a), c)]:
                out.add(c[:k] + b + c[k+len(a):])
    for k in range(len(c)):           # sujeira a mais (letra fina, sinal)
        if c[k] in "ijlf1'^*;,.~|!í" and len(c) > 3:
            out.add(c[:k] + c[k+1:])
    return [x for x in out if x]
reg, duv = [], []
for s in S:
    for pi, (t, pag) in enumerate(s['pars']):
        ws = t.split()
        k = 0
        while k < len(ws) - 1:
            a, b = RX.match(ws[k]).group(2), RX.match(ws[k + 1]).group(2)
            ok_a = conhecida(a) or norm(a) in outros
            ok_b = conhecida(b) or norm(b) in outros
            if a and b and not (ok_a and ok_b) and (cont[(a + b).lower()] >= 2 or (outros[norm(a + b)] >= 2 and not ok_a and not ok_b)) and not a.endswith('.'):
                reg.append((str(s['id']), str(pi), str(k), ws[k] + ' ' + ws[k + 1], ws[k] + ws[k + 1], str(pag)))
                ws[k:k + 2] = [re.sub(r'(?<=[^\W\d_])[-.*^]+(?=[^\W\d_])', '', ws[k] + ws[k + 1])]
            k += 1
        novo = []
        for wi, w in enumerate(ws):
            m = RX.match(w); pre, c, pos = m.groups()
            pre = pre.replace('j', '¡') if False else pre
            if c == 'g': c2 = 'y'
            elif c == '9' : c2 = 'y'
            elif not c or conhecida(c) or norm(c) in outros or re.fullmatch(r'[IVXLCDM]+|\d+', c):
                c2 = c
            else:
                cands = [x for x in candidatos(c) if conhecida(x)]
                # «jQue» / «íCuán» / «iCuán»: a exclamação de abertura lida como letra
                if not cands and len(c) > 1 and c[0] in 'jíi' and conhecida(c[1:]):
                    pre, cands = pre + '¡', [c[1:]]
                if cands:
                    gy = c.replace('g', 'y')
                    cands.sort(key=lambda x: (x != gy, -cont[x.lower()]))
                    c2 = cands[0]
                    if c[:1].isupper() and not c2[:1].isupper(): c2 = c2[:1].upper() + c2[1:]
                else:
                    c2 = c
                    ctx = ' '.join(ws[max(0, wi-6):wi+7])
                    duv.append((str(s['id']), str(pi), str(wi), w, str(pag), ctx))
            if c2 != c: reg.append((str(s['id']), str(pi), str(wi), w, pre + c2 + pos, str(pag)))
            novo.append(pre + c2 + pos)
        s['pars'][pi][0] = ' '.join(novo)
json.dump(S, open('dl/bmc_corr.json', 'w'), ensure_ascii=False, indent=0)
open('dl/correcoes.tsv', 'w').write('\n'.join('\t'.join(r) for r in reg) + '\n')
open('dl/duvidas.tsv', 'w').write('\n'.join('\t'.join(r) for r in duv) + '\n')
print('correções', len(reg), 'dúvidas', len(duv))
