"""Confronta o grego do Perseus (já com graves.py) com duas leituras do fac-símile de Godley:
  O1 = Tesseract (grc) da impressão de 1921 (Internet Archive herodotud0000adgo), com as caixas das palavras (hOCR);
  O2 = OCR do Internet Archive da reimpressão de 1975 (historiesvolumei00hero_249), mesmas chapas.
Uso: colacao.py <pasta-trabalho>   (lê l1.json, ocr/*.hocr, dl/historiesvolumei00hero_249.txt; grava col-*.tsv)
Listas: col-letras.tsv (as duas leituras concordam entre si e não com o Perseus, nas letras), col-acentos.tsv
(mesmas letras, acentos ou espíritos diferentes, as duas leituras iguais), col-fracas.tsv (só uma leitura
discorda, parecida com o Perseus), col-buracos.tsv (palavras do Perseus que nenhuma leitura tem, e palavras
que as duas leituras têm e o Perseus não)."""
import json, re, sys, os, glob, html, unicodedata as u, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graves import corrigir
B = sys.argv[1]
PAL = re.compile(r"[Ͱ-Ͽἀ-῿̀-ͯ᾽᾿ʼ’'΄`´῾]+")
def norm(w):
    w = u.normalize('NFD', w.lower())
    w = ''.join(c for c in w if not u.combining(c))
    w = re.sub(r"[᾽᾿ʼ’'΄`´῾]", '', w)
    return w.replace('ς', 'σ').replace('ϲ', 'σ')
def forma(w):
    w = u.normalize('NFC', w.replace('᾽', '’').replace('ʼ', '’').replace("'", '’').replace('᾿', '’'))
    return w.lower()
def toks(t):
    return [w for w in PAL.findall(t) if any(c.isalpha() for c in w)]
# Perseus
d = json.load(open(B + '/l1.json', encoding='utf-8'))
pt, pref = [], []
for c, secs in d['caps']:
    for s, t in secs:
        t = corrigir(t.replace('⟦n⟧', ' ').replace('⟦gap⟧', ' ').replace('⟦l⟧', ' ').replace('⟦/l⟧', ' '))[0]
        for w in toks(t):
            pt.append(w); pref.append(f'{c}.{s}')
pn = [norm(w) for w in pt]
# O1: hOCR da impressão de 1921
o1, o1pos = [], []
for f in sorted(glob.glob(B + '/ocr/*.hocr')):
    pag = os.path.basename(f)[:3]
    h = open(f, encoding='utf-8').read()
    linhas = re.findall(r"<span class='ocr_line'.*?</span>\s*</span>", h, re.S)
    lst = []
    for ln in linhas:
        ws = re.findall(r"<span class='ocrx_word'[^>]*title='bbox (\d+) (\d+) (\d+) (\d+)[^']*'[^>]*>(.*?)</span>", ln, re.S)
        lst.append([(html.unescape(re.sub('<[^>]+>', '', w[4])), tuple(map(int, w[:4]))) for w in ws])
    # tira o título corrente (1ª linha) se não tiver minúsculas gregas
    if lst and not re.search(r'[α-ω]', ' '.join(w for w, _ in lst[0])):
        lst = lst[1:]
    pend = None
    for ln in lst:
        for k, (w, bb) in enumerate(ln):
            if pend is not None:
                w = pend[0] + w; bb = pend[1]; pend = None
            if k == len(ln) - 1 and w.endswith(('-', '‐', '—')) and len(w) > 1:
                pend = (w.rstrip('-‐—'), bb); continue
            for x in toks(w):
                o1.append(x); o1pos.append((pag, bb))
on1 = [norm(w) for w in o1]
# O2: djvu.txt do Internet Archive (reimpressão de 1975)
ocr = open(B + '/dl/historiesvolumei00hero_249.txt', encoding='utf-8').read().split('\n')
def grego(s):
    l = [c for c in s if c.isalpha()]
    g = [c for c in l if 'Ͱ' <= c <= 'Ͽ' or 'ἀ' <= c <= '῿']
    return len(l) >= 4 and len(g) / len(l) > 0.6
ini = next(i for i, l in enumerate(ocr) if 'ροδότου' in l)
fim = next(i for i, l in enumerate(ocr) if l.startswith('BOOK II'))
txt = ''
for l in ocr[ini:fim]:
    l = l.rstrip()
    if not grego(l): continue
    txt += (l[:-1] if l.endswith('-') else l + ' ')
o2 = toks(txt); on2 = [norm(w) for w in o2]
print('Perseus', len(pt), 'O1', len(o1), 'O2', len(o2))
def alinhar(on):
    m = [None] * len(pn); ins = {}
    sm = difflib.SequenceMatcher(None, pn, on, autojunk=False)
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal' or (op == 'replace' and a2 - a1 == b2 - b1):
            for k in range(a2 - a1): m[a1 + k] = b1 + k
        elif op in ('insert', 'replace'):
            ins.setdefault(a1, []).extend(range(b1, b2))
            if op == 'replace':
                for k in range(min(a2 - a1, b2 - b1)): m[a1 + k] = b1 + k
    return m, ins
m1, i1 = alinhar(on1); m2, i2 = alinhar(on2)
ctx = lambda i: ' '.join(pt[max(0, i - 4):i + 5])
pos = lambda i: (f'{o1pos[m1[i]][0]}\t{",".join(map(str, o1pos[m1[i]][1]))}' if m1[i] is not None else '\t')
letras, acentos, fracas, buracos = [], [], [], []
for i in range(len(pt)):
    a = o1[m1[i]] if m1[i] is not None else None
    b = o2[m2[i]] if m2[i] is not None else None
    na, nb = (norm(a) if a else None), (norm(b) if b else None)
    if a is None and b is None:
        if len(pn[i]) >= 2: buracos.append(f'{pref[i]}\tSÓ-PERSEUS\t{pt[i]}\t\t\t{ctx(i)}\t\t')
        continue
    if na is not None and na == nb and na != pn[i]:
        letras.append(f'{pref[i]}\t{pt[i]}\t{a}\t{b}\t{ctx(i)}\t{pos(i)}')
    elif na == pn[i] and nb == pn[i]:
        if forma(a) == forma(b) and forma(a) != forma(pt[i]):
            acentos.append(f'{pref[i]}\t{pt[i]}\t{a}\t{b}\t{ctx(i)}\t{pos(i)}')
    elif (na is not None and na != pn[i]) or (nb is not None and nb != pn[i]):
        x = na if (na is not None and na != pn[i]) else nb
        r = difflib.SequenceMatcher(None, pn[i], x).ratio()
        if r >= 0.75 and len(pn[i]) >= 4 and (na == pn[i] or nb == pn[i]) is False:
            fracas.append(f'{pref[i]}\t{pt[i]}\t{a}\t{b}\t{ctx(i)}\t{pos(i)}')
for k in sorted(set(i1) & set(i2)):
    x1 = [o1[j] for j in i1[k] if len(on1[j]) >= 3]; x2 = [o2[j] for j in i2[k] if len(on2[j]) >= 3]
    comuns = [w for w in x1 if norm(w) in {norm(y) for y in x2}]
    if comuns:
        r = pref[min(k, len(pref) - 1)]
        buracos.append(f'{r}\tSÓ-FAC\t{" ".join(comuns)}\t{" ".join(x1)}\t{" ".join(x2)}\t{ctx(k)}\t{pos(min(k, len(pt)-1))}')
for nome, l in [('letras', letras), ('acentos', acentos), ('fracas', fracas), ('buracos', buracos)]:
    open(f'{B}/col-{nome}.tsv', 'w', encoding='utf-8').write('\n'.join(l) + '\n')
    print(nome, len(l))
