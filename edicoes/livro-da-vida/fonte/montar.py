"""Monta prólogo, 40 capítulos e epílogo (Silverio 1915) a partir de linhas.json → bmc_estrutura.json
[{'id': 'prologo'|1..40|'epilogo', 'cab': 'CAPITULO…', 'titulo': '…', 'pars': [(texto, pagina)]}]"""
import json, re, sys
B = json.load(open(sys.argv[1]))
secs = []; cur = None; modo = None
def novo(id_, cab=''):
    global cur
    cur = {'id': id_, 'cab': cab, 'titulo': [], 'pars': []}; secs.append(cur)
ROM = {}
def rom2int(s):
    v = {'I':1,'V':5,'X':10,'L':50,'C':100}; s = s.upper().replace('Í','I'); n = 0
    for i, c in enumerate(s):
        x = v.get(c, 0); n += -x if i + 1 < len(s) and v.get(s[i+1], 0) > x else x
    return n
ncap = 0
for tipo, t, pag in B:
    t = t.strip()
    if pag == 140 and tipo == 'CENTRO' and t.startswith('Jhs'):
        novo('prologo'); modo = 'texto'; continue
    if cur is None: continue
    if tipo == 'CENTRO' and t in ('Jesús', 'Jhs.', '/'):
        if pag == 508 and t == 'Jhs.': modo = 'texto'
        continue
    if tipo == 'CAP':
        ncap += 1; novo(ncap, t); modo = 'titulo'; continue
    if t.startswith('CARTA QUE LA SANTA ESCRIBIO'):
        novo('epilogo', t); modo = 'titulo'; continue
    if modo == 'titulo':
        letras = [c for c in t if c.isalpha()]
        maius = letras and sum(c.isupper() for c in letras) / len(letras) > 0.8
        if not maius:
            modo = 'texto'
        else:
            cur['titulo'].append(t); continue
    if tipo == 'PAR' or not cur['pars'] or modo == 'novo':
        modo = 'texto'
        cur['pars'].append([t, pag])
    else:
        cur['pars'][-1][0] += '\n' + t
def limpar(s):
    s = re.sub(r'-\n', '', s)            # hífen do fim da linha
    s = s.replace('\n', ' ')
    s = re.sub(r'\s*\(\s*[1-9]\d?\s*\)', '', s)   # chamadas de nota
    s = re.sub(r'\s+', ' ', s).strip()
    return s
for s in secs:
    s['titulo'] = limpar('\n'.join(s['titulo']))
    s['pars'] = [[limpar(t), p] for t, p in s['pars']]
json.dump(secs, open(sys.argv[2], 'w'), ensure_ascii=False, indent=0)
for s in secs:
    print(s['id'], len(s['pars']), sum(len(t.split()) for t, _ in s['pars']), '|', s['titulo'][:70])
