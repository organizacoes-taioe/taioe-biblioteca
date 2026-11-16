import json, re, sys
d = json.load(open('composto.json')); out = d['out']; ins = {int(k):v for k,v in d['ins'].items()}
ROM = {}
def rom(s):
    s = re.sub(r'[^IVXL]', '', s.upper()); v = {'I':1,'V':5,'X':10,'L':50}; t = 0
    for i,c in enumerate(s):
        t += -v[c] if i+1 < len(s) and v[c] < v[s[i+1]] else v[c]
    return t
caps = []; cur = None
for idx, o in enumerate(out):
    if o is None: pass
    elif o[0] == 'CAP':
        cur = {'n': 0 if o[1]=='praef' else rom(o[1]), 'p': []}; caps.append(cur)
    else:
        pal, p, src, i = o
        cur['p'].append(pal + p)
    for f in ins.get(idx, []):
        cur['p'].append(re.sub(r'[*“„]', '', f.replace('ſ','s')))
linhas = ['# titulo: Vita Sancti Augustini', '']
for c in caps:
    t = ' '.join(c['p'])
    t = re.sub(r'\s+([.,;:?!])', r'\1', t)
    linhas.append(f"[{c['n']}] {t}"); linhas.append('')
txt = '\n'.join(linhas).replace('æ','ae').replace('œ','oe').replace('Æ','Ae').replace('Œ','Oe')
import collections
pal = collections.Counter(re.findall(r'[A-Za-z]+', txt))
troca = {}
for w,n in pal.items():
    if 'j' in w.lower():
        wi = w.replace('j','i').replace('J','I')
        if pal.get(wi,0) and n >= pal[wi]: troca[wi] = w
        elif pal.get(wi,0): print('j minoritario', w, n, wi, pal[wi])
# formas com i que nunca aparecem com j no texto: regra para iam, eius etc. pelo léxico do PL
for wi,w in troca.items():
    txt = re.sub(r'\b'+wi+r'\b', w, txt)
print('i->j', len(troca))
open(sys.argv[1],'w').write(txt)
print([ (c['n'], len(c['p'])) for c in caps])
