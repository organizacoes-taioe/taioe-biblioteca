"""Monta original/*.txt das Moradas a partir de trab/votado2.json + trab/correcoes.json.
correcoes.json: {"<pos>": "forma"} (forma '' apaga o token; pode ter várias palavras)."""
import sys, json, re, os, collections, unicodedata
base, saida = sys.argv[1], sys.argv[2]
V = json.load(open(f'{base}/votado2.json')); tok = list(V['tok'])
cor = json.load(open(f'{base}/correcoes.json')) if os.path.exists(f'{base}/correcoes.json') else {}
for p, f in cor.items():
    tok[int(p)] = f
def limpo(t):
    t = re.sub(r'^[■‘^{|“"]+(?=[¡\wÁÉÍÓÚÑáéíóúñ])', '', t)
    t = t.replace('$e', 'se').replace('(r]', '[r]')
    return t
tok = [limpo(t) for t in tok]
tok = [t for t in tok if t not in ('+;', '+', '■')]
txt = ' '.join(t for t in tok if t != '')
for a, b in (json.load(open(f'{base}/remendos.json')) if os.path.exists(f'{base}/remendos.json') else []):
    if a.startswith('re:'):
        txt = re.sub(a[3:], b, txt)
    else:
        if a not in txt: print("remendo sem efeito:", a)
        txt = txt.replace(a, b)
txt = re.sub(r' \*(?= )', '', txt)
EM = json.load(open(f'{base}/ementas.json'))
ps = [re.sub(r'\s+', ' ', p).strip() for p in txt.split('¶')]
ps = [p for p in ps if p]
LIXO = json.load(open(f'{base}/lixo.json')) if os.path.exists(f'{base}/lixo.json') else []
ps = [p for p in ps if p not in LIXO]
def parenteses(p):
    ws = p.split(); abre = None
    for i, w in enumerate(ws):
        if '(' in w:
            if abre is not None: ws[abre] = ws[abre].replace('(', '', 1)
            abre = i
        if ')' in w:
            if abre is None: ws[i] = ws[i].replace(')', '', 1)
            else: abre = None
    if abre is not None: ws[abre] = ws[abre].replace('(', '', 1)
    return ' '.join(ws)
ps = [parenteses(p) for p in ps]
def maius(p):
    let = re.sub(r'[^A-Za-zÁÉÍÓÚÑáéíóúñÜü]', '', p)
    return len(let) > 2 and sum(c.isupper() for c in let) / len(let) > 0.7
# léxico do corpo: forma sem acento -> forma mais comum; maiúscula no meio da frase
corpo = [p for p in ps if not maius(p)]
def sem(x): return ''.join(ch for ch in unicodedata.normalize('NFD', x) if unicodedata.category(ch) != 'Mn')
formas = collections.defaultdict(collections.Counter); cap = collections.Counter(); mins = collections.Counter()
for p in corpo:
    ws = p.split()
    for i, w in enumerate(ws):
        x = re.sub(r'[^\wÁÉÍÓÚÑáéíóúñÜü]', '', w)
        if not x: continue
        formas[sem(x.lower())][x.lower()] += 1
        if i > 0 and not re.search(r'[.!?:]$', ws[i - 1]):
            (cap if x[0].isupper() else mins)[x.lower()] += 1
def caixa(p):
    out = []
    for i, w in enumerate(p.split()):
        m = re.match(r'^(\W*)([\wÁÉÍÓÚÑáéíóúñÜü]+)(.*)$', w)
        if not m: out.append(w.lower()); continue
        a, x, z = m.groups(); lo = x.lower()
        f = formas[sem(lo)].most_common(1)[0][0] if formas.get(sem(lo)) else lo
        if cap[lo] > mins[lo]: f = f[0].upper() + f[1:]
        if i == 0 or re.search(r'[.!?]$', out[-1] if out else ''): f = f[0].upper() + f[1:]
        out.append(a + f + z.lower())
    return ' '.join(out)
NOMES = {'PRIMERAS': 'primeras', 'SEGUNDAS': 'segundas', 'TERCERAS': 'terceras', 'CUARTAS': 'cuartas', 'QUINTAS': 'quintas', 'SEXTAS': 'sextas', 'SETIMAS': 'sétimas', 'SÉTIMAS': 'sétimas'}
ORD = ['PRIMERAS', 'SEGUNDAS', 'TERCERAS', 'CUARTAS', 'QUINTAS', 'SEXTAS', 'SETIMAS']
ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
CAPN = {'PRIMERO': 1, 'UNICO': 1, 'ÚNICO': 1, 'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11}
arquivos = collections.OrderedDict(); atual = '00-prologo'; arquivos[atual] = []
morada = 0; cap_n = 0; esperando = None; i = 0
while i < len(ps):
    p = ps[i]; P = sem(p.upper())
    m = re.match(r'^(?:MORADAS )?(PRIMERAS|SEGUNDAS|TERCERAS|CUARTAS|QUINTAS|SEXTAS|SETIMAS)(?: MORADAS)?$', P)
    if m:
        morada = ORD.index(m.group(1)) + 1
        atual = f'{morada:02d}-{["primeiras","segundas","terceiras","quartas","quintas","sextas","setimas"][morada-1]}-moradas'
        arquivos[atual] = [f'# titulo: {"Moradas " + NOMES[m.group(1)] if morada in (1,2,5,6) else NOMES[m.group(1)].capitalize() + " moradas"}']
        i += 1
        if i < len(ps) and maius(ps[i]) and re.match(r'^(HAY|CONTIENEN)', sem(ps[i].upper())):
            arquivos[atual].append('_' + caixa(ps[i]).rstrip('.').replace('capitulo', 'capítulo') + '._'); i += 1
        continue
    m = re.match(r'^CAPITULO ([IVX]+|PRIMERO|UNICO)\.?$', P)
    if m:
        cap_n = CAPN[m.group(1)]
        i += 1
        em = []
        while i < len(ps) and maius(ps[i]):
            em.append(ps[i]); i += 1
        chave = f'{ROM[morada-1]}.{cap_n}'
        ementa = EM.get(chave, caixa(' '.join(em)))
        if 'UNICO' in P:
            arquivos[atual] += ['## Capítulo único', f'[{chave}] _' + ementa + '_']
        else:
            arquivos[atual].append(f'## Capítulo {cap_n} — ' + ementa)
            esperando = f'[{chave}] '
        continue
    if re.match(r'^J[Hh][Ss]\.?$', p) and morada == 7 and cap_n == 4:
        atual = '08-epilogo'; arquivos[atual] = ['# titulo: Epílogo', 'JHS']; i += 1; continue
    if p.startswith('_Este tratado'):
        arquivos[atual].append(p); i += 1; continue
    if maius(p) and len(p) < 40:
        arquivos[atual].append(p); i += 1; continue
    if esperando:
        p = esperando + p; esperando = None
    arquivos[atual].append(p); i += 1
os.makedirs(saida, exist_ok=True)
for nome, bl in arquivos.items():
    open(f'{saida}/{nome}.txt', 'w').write('\n\n'.join(bl) + '\n')
    print(nome, len(bl), sum(len(b.split()) for b in bl))
