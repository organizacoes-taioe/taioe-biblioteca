"""Confronta o grego do Perseus com o OCR do fac-símile (IA plutarchslives07plut). Uso: colacao.py"""
import json, re, sys, unicodedata, difflib
B = sys.argv[1]
ocr = open(B + '/dl/djvu.txt', encoding='utf-8').read().split('\n')
def grego(s):
    l = [c for c in s if c.isalpha()]
    g = [c for c in l if 'Ͱ' <= c <= 'Ͽ' or 'ἀ' <= c <= '῿']
    return len(l) >= 4 and len(g) / len(l) > 0.6
def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    w = re.sub(r"[᾽᾿ʼ’'΄`´῾]", '', w)
    return w.replace('ς', 'σ').replace('ϲ', 'σ')
PAL = re.compile(r'[Ͱ-Ͽἀ-῿̀-ͯ᾽᾿ʼ’\']+')
def toks(texto):
    return [w for w in PAL.findall(texto) if any(c.isalpha() for c in w)]
# OCR: do início de Alexandre (linha com «Tov ᾿Αλεξάνδρου») até o fim
ini = next(i for i, l in enumerate(ocr) if 'συκοφαντεῖν. οὔτε' in l) - 12
linhas = [l.rstrip() for l in ocr[ini:] if grego(l)]
txt = ''
for l in linhas:
    txt += (l[:-1] if l.endswith('-') else l + ' ')
ot = toks(txt)
on = [norm(w) for w in ot]
res = []; ins = []; une = []; ace = []
for f, nome in [('alex.json', 'Alex'), ('caes.json', 'Caes')]:
    d = json.load(open(B + '/' + f))
    pt, pref = [], []
    for c, secs in d['caps']:
        for s, t in secs:
            for w in toks(t.replace('⟦n⟧', ' ')):
                pt.append(w); pref.append(f'{c}.{s}')
    pn = [norm(w) for w in pt]
    # janela no OCR: procurar início pelo 1º trigrama
    sm = difflib.SequenceMatcher(None, pn, on, autojunk=False)
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(a2 - a1):
                P, O = pt[a1+k].replace('ʼ','’'), ot[b1+k].replace('᾽','’')
                if unicodedata.normalize('NFC', P.lower()) != unicodedata.normalize('NFC', O.lower()) and not re.search(r'[᾿῾]', O):
                    ace.append(f"{nome} {pref[a1+k]}\t{pt[a1+k]}\t{ot[b1+k]}\t{' '.join(pt[max(0,a1+k-3):a1+k+4])}")
            continue
        if a2 - a1 > 40 or b2 - b1 > 40:
            res.append(f'{nome} {pref[min(a1,len(pref)-1)]}\tGRANDE {op} {a2-a1}/{b2-b1}')
            continue
        if op == 'insert' or (op == 'replace' and a2 - a1 < b2 - b1):
            extra = [w for w in ot[b1:b2] if len(norm(w)) >= 3]
            if extra:
                ins.append(f"{nome} {pref[min(a1,len(pref)-1)]}\t{op}\tP: {' '.join(pt[a1:a2])}\tO: {' '.join(ot[b1:b2])}\t{' '.join(pt[max(0,a1-3):a2+3])}")
        if op == 'replace' and a2 - a1 != b2 - b1 and a2-a1<=4 and b2-b1<=4:
            P=''.join(pn[a1:a2]); O=''.join(on[b1:b2])
            if len(O) >= len(P) and difflib.SequenceMatcher(None,P,O).ratio() > 0.5:
                une.append(f"{nome} {pref[a1]}\tP: {' '.join(pt[a1:a2])}\tO: {' '.join(ot[b1:b2])}")
        if op != 'replace' or a2 - a1 != b2 - b1:
            continue
        for k in range(a2 - a1):
            x, y = pn[a1+k], on[b1+k]
            if x == y:
                P, O = pt[a1+k].replace('ʼ','’'), ot[b1+k].replace('᾽','’')
                if unicodedata.normalize('NFC', P.lower()) != unicodedata.normalize('NFC', O.lower()) and not re.search(r'[᾿῾]', O):
                    ace.append(f"{nome} {pref[a1+k]}\t{pt[a1+k]}\t{ot[b1+k]}\t{' '.join(pt[max(0,a1+k-3):a1+k+4])}")
                continue
            r = difflib.SequenceMatcher(None, x, y).ratio()
            if r < 0.6 and not (len(y) >= 5 and len(x) >= 3): continue
            res.append(f"{nome} {pref[a1+k]}\t{pt[a1+k]}\t{ot[b1+k]}\t{r:.2f}\t{' '.join(pt[max(0,a1+k-3):a1+k+4])}")
open(B + '/colacao.tsv', 'w').write('\n'.join(res) + '\n'); open(B + '/acentos.tsv', 'w').write('\n'.join(ace) + '\n'); open(B + '/desiguais.tsv', 'w').write('\n'.join(une) + '\n'); open(B + '/insercoes.tsv', 'w').write('\n'.join(ins) + '\n')
print(len(res))
