"""Divide o texto provisório pelas colunas do fac-símile de 1845 (PL 32 e, na carta, PL 33) e baixa os recortes."""
import json, re, os, sys, subprocess, collections
sys.path.insert(0, 'scripts')
from djvu import paginas
d = json.load(open('composto.json')); out = d['out']; ins = {int(k):v for k,v in d['ins'].items()}
al = json.load(open('alinhado_m.json'))
I0, I1 = 10111, 11053
ID = {'32': 'bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1845_32',
      '33': 'bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1845_33'}
dims = {}
for vol, f in (('32','dl/bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1845_32.djvu.xml'),('33','dl/A33.djvu.xml')):
    for i,(W,H,ls) in enumerate(paginas(f, ate=515 if vol=='33' else 45)):
        dims[(vol,i)] = (W,H)
grupos = []  # (chave, [itens])
loc = None
def rom(s):
    s = re.sub(r'[^IVXL]', '', s.upper()); v = {'I':1,'V':5,'X':10,'L':50}; t = 0
    for i,c in enumerate(s): t += -v[c] if i+1 < len(s) and v[c] < v[s[i+1]] else v[c]
    return t
caixas = collections.defaultdict(list)
for idx, o in enumerate(out):
    if o is None: continue
    if o[0] == 'CAP':
        txt = f"\n[{0 if o[1]=='praef' else rom(o[1])}]"; i = None
    else:
        txt = o[0] + o[1]; i = o[3]
    if i is not None:
        s = al['A']['slot'][i]
        if s:
            vol = '33' if I0 <= i < I1 else '32'
            fase = 0 if i < I0 else (1 if i < I1 else 2)
            nl = (fase, vol, s[0]['p'], s[0]['c'])
            if loc is None or nl != loc:
                # só muda de coluna se a nova vier depois (evita saltos do alinhamento)
                if loc is None or nl > loc:
                    loc = nl
            if loc == nl: caixas[loc].append(s[0]['b'])
    if not grupos or grupos[-1][0] != loc: grupos.append((loc, []))
    grupos[-1][1].append(txt)
    for f in ins.get(idx, []): grupos[-1][1].append(re.sub(r'[*“„]', '', f.replace('ſ','s')))
g2 = []
pend = []
for loc, toks in grupos:
    if loc is None: pend += toks; continue
    if g2 and g2[-1][0] == loc: g2[-1][1].extend(pend+toks)
    else: g2.append((loc, pend+toks))
    pend = []
grupos = g2
os.makedirs('conf', exist_ok=True)
lista = []
for n,(loc,toks) in enumerate(grupos):
    fase,vol,p,c = loc
    t = ' '.join(toks); t = re.sub(r' +([.,;:?!])', r'\1', t).replace('æ','ae').replace('œ','oe').strip()
    nome = f'conf/{n+1:02d}-pl{vol}-f{p}-c{c}'
    open(nome+'.txt','w').write(t+'\n')
    W,H = dims[(vol,p)]
    bs = caixas[loc]
    x1 = max(0, min(b[0] for b in bs)-60); x2 = min(W, max(b[2] for b in bs)+60)
    y1 = max(0, min(b[1] for b in bs)-120); y2 = min(H, max(b[3] for b in bs)+120)
    meio = (y1+y2)//2
    for k,(a,b) in enumerate(((y1, meio+80), (meio-80, y2))):
        reg = f'pct:{100*x1/W:.2f},{100*a/H:.2f},{100*(x2-x1)/W:.2f},{100*(b-a)/H:.2f}'
        url = f"https://iiif.archive.org/iiif/{ID[vol]}${p}/{reg}/1000,/0/default.jpg"
        lista.append((nome+f'-{"ab"[k]}.jpg', url))
open('conf/urls.tsv','w').write('\n'.join(f'{a}\t{b}' for a,b in lista)+'\n')
print(len(grupos), [ (g[0][1:], len(g[1])) for g in grupos])
