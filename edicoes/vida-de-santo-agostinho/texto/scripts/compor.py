"""Compõe o texto do PL a partir dos votos. Grava texto provisório e a lista do que conferir na imagem."""
import sys, json, re, collections, difflib
v = json.load(open('votos_m.json')); al = json.load(open('alinhado_m.json')); lex = json.load(open('lexico.json'))
W = al['W']; SRC = [k for k in ('A','B','C','G') if k in al]
dec = {}
if len(sys.argv) > 1:
    try: dec = json.load(open(sys.argv[1]))
    except FileNotFoundError: pass
def base(t):
    t = t.lower().replace('æ','ae').replace('œ','oe').replace('ﬀ','ff').replace('ﬁ','fi').replace('ﬂ','fl')
    t = re.sub(r'[^a-zà-ÿſ]', '', t)
    return t.translate(str.maketrans('jvàáâèéêìíîòóôùúûë', 'iuaaaeeeiiiooouuue'))
def nolex(k): return lex.get(k.replace('ſ','s'), 0) == 0 and lex.get(k.replace('ſ','f'), 0) == 0
CONF = {frozenset(x) for x in ['tl','ce','nu','il','hb','az','it','fs','oe','co','rt','ri','ae','ec','tf','ln','in','au','ui','gq','ao','ij','ft','sl']}
def so_ocr(a, b):
    """a e b diferem só por trocas típicas de OCR?"""
    a = a.replace('ae','e').replace('oe','e'); b = b.replace('ae','e').replace('oe','e')
    sm = difflib.SequenceMatcher(None, a, b)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag == 'equal': continue
        x, y = a[i1:i2], b[j1:j2]
        if tag == 'replace' and len(x) == len(y) and all(frozenset((p,q)) in CONF for p,q in zip(x,y)): continue
        if {x,y} in ({'m','rn'},{'m','in'},{'m','ni'},{'n','ri'},{'u','ii'},{'n','ii'},{'h','li'},{'d','cl'}): continue
        return False
    return True
def resolve_s(f, wk):
    """troca cada ſ por s ou f, conforme a chave de Weiskotten"""
    if 'ſ' not in f: return f
    pos = [i for i,c in enumerate(f) if c == 'ſ']
    import itertools
    for comb in itertools.product('sf', repeat=min(len(pos),4)):
        g = list(f)
        for p_, c in zip(pos, comb): g[p_] = c
        g = ''.join(g)
        if base(letras(g)) == wk: return g
    return f
def limpa(f):
    f = f.replace('|', ' ')
    f = re.sub(r'(?<=[a-zæœſ])[-—](?=[a-zæœſ])', '', f)
    f = f.replace('ſ','s').replace('ﬀ','ff').replace('ﬁ','fi').replace('ﬂ','fl').replace('“','').replace('„','').replace('*','')
    f = re.sub(r'(?<=[A-Za-z])[0-9]+', '', f)
    return f
def pont(f):
    m = re.search(r'[^A-Za-zÀ-ÿæœÆŒſ]*$', f); p = m.group(0)
    p = re.sub(r'[^.,;:?!]', '', p)
    return p
def letras(f):
    if '|' in f:
        ps = f.split('|'); return '|'.join(ps[:-1]) + '|' + letras(ps[-1]) if letras(ps[-1]) else letras('|'.join(ps[:-1]))
    m = re.match(r'^[^A-Za-zÀ-ÿæœÆŒſ]*(.*?)[^A-Za-zÀ-ÿæœÆŒſ]*$', f); return m.group(1)
def melhor_w(i):
    a = v[i]['w']; b = v[i].get('w2') or a
    fa = lex.get(base(letras(a)),0); fb = lex.get(base(letras(b)),0)
    return b if fb > fa*3 else a
def forma_w(i):
    return letras(melhor_w(i))
# capítulos
cap = {}
for i,x in enumerate(W):
    if x['t'] in ('CAPUT','PRAEFATIO'):
        num = W[i+1]['t'] if x['t']=='CAPUT' else 'praef'
        cap[i] = num
pular = set()
for i in cap:
    pular.add(i)
    if cap[i] != 'praef': pular.add(i+1)
conf = []   # a conferir
out = []
for x in v:
    i = x['i']
    if i in pular:
        out.append(('CAP', cap[i]) if i in cap else None); continue
    cls = x['cls']; leit = x['leit']
    pal = None; src = None
    if str(i) in dec:
        d = dec[str(i)]
        if d == '-': out.append(None); continue
        pal = d; src = 'dec'
    elif cls == 'sem':
        out.append(None); continue
    elif cls == 'ok':
        pal = resolve_s(x['forma'].replace('|',''), base(forma_w(i))); src = x['de']
    elif cls in ('ruido','fraco','dub') and re.fullmatch(r'[A-R*]{1,9}[,.;]?|om\.?|edd[.,]*|codd[.,]*|cf\.?', v[i]['w'].strip()):
        out.append(None); continue
    elif cls == 'pl':
        f = x['forma']; k = base(letras(f))
        wk = base(forma_w(i))
        if '|' in f and base(f) != wk:
            pal = f; src = x['de']
            conf.append({'i': i, 'tipo': 'fundido', 'w': v[i]['w'], 'pl': f, 'leit': leit})
        elif (nolex(k) and not nolex(wk)) or so_ocr(k.replace('ſ','s'), wk):
            pal = melhor_w(i); src = 'W'      # erro comum de OCR das duas leituras
        else:
            pal = f; src = x['de']
            conf.append({'i': i, 'tipo': 'variante', 'w': W[i]['t'], 'pl': f, 'leit': leit})
    else:  # dub, ruido, fraco
        pal = melhor_w(i); src = 'W'
        fund = [l for k,l in leit.items() if l and k != 'G' and '|' in l and len(l.split('|')) == 2 and base(l.split('|')[0]) == base(letras(pal)) ]
        if fund:
            conf.append({'i': i, 'tipo': 'fundido', 'w': v[i]['w'], 'pl': fund[0], 'leit': leit})
            pal = letras(pal) + '|' + fund[0].split('|')[1]
        col = lambda t: base(letras(t)).replace('ae','e').replace('oe','e')
        com_ae = [l for k,l in leit.items() if l and k != 'G' and col(l) == col(pal) and re.search(r'æ|œ|ae|oe', l.lower())]
        if com_ae and not re.search(r'ae|oe|æ|œ', pal.lower()):
            pal = com_ae[0]; src = 'ae'
        cands = [l for l in leit.values() if l]
        if cls == 'dub':
            sims = [(difflib.SequenceMatcher(None, base(l), base(forma_w(i))).ratio(), l) for l in cands]
            plaus = [l for s,l in sims if not nolex(base(letras(l))) and base(letras(l)) != base(forma_w(i)) and not so_ocr(base(letras(l)).replace('ſ','s'), base(forma_w(i)))]
            if plaus:
                conf.append({'i': i, 'tipo': 'duvida', 'w': W[i]['t'], 'pl': plaus[0], 'leit': leit})
    # pontuação: da fonte escolhida; se as leituras do PL divergem, a da maioria
    ps = collections.Counter(pont(l) for k,l in leit.items() if l and k != 'G')
    p = ps.most_common(1)[0][0] if ps else pont(W[i]['t'])
    if not p and pont(v[i]['w']) in ('.',';',':','?','!') and i+1 < len(v) and re.match(r'[A-Z]', letras(v[i+1]['w']) or 'a'):
        p = pont(v[i]['w'])
    out.append((limpa(letras(pal)), p, src, i))
# inserções do PL (duas leituras ou mais com a mesma palavra no mesmo vão)
ins = collections.defaultdict(list)
RREF = re.compile(r'^\(|\)|^[ivxlc]+[.,;]?$|^[A-Z][a-z]{1,4}\.$|^(lib|cap|Cd|Cod|edit|Edit)\.?$')
for k in SRC:
    for g, toks in al[k]['gap'].items():
        if len(toks) > 3: continue
        if any(RREF.search(t['t']) for t in toks): continue
        for t in toks:
            kk = base(letras(t['t']))
            if len(kk) >= 2 and not nolex(kk) and '(' not in t['t'] and ')' not in t['t']:
                ins[int(g)].append((k, kk, t['t']))
inseridos = {}
for g, l in ins.items():
    c = collections.Counter(kk for _,kk,_ in l)
    for kk, nn in c.items():
        fontes = {k for k,k2,_ in l if k2==kk}
        if len(fontes) >= 2:
            f = next(t for k,k2,t in l if k2==kk)
            inseridos.setdefault(g, []).append(f)
            conf.append({'i': g, 'tipo': 'insercao', 'w': None, 'pl': f, 'leit': {k: t for k,k2,t in l if k2==kk}})
json.dump({'out': out, 'ins': inseridos}, open('composto.json','w'), ensure_ascii=False)
json.dump(conf, open('conferir.json','w'), ensure_ascii=False, indent=0)
print('saida', sum(1 for o in out if o and o[0]!='CAP'), 'a conferir', collections.Counter(c['tipo'] for c in conf))
