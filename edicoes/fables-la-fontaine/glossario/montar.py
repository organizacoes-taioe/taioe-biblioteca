"""Monta os glossários das Fables: verbetes em m1–m6 (um por chave, partilhados entre as fábulas), escolha do verbete por ocorrência em escolhas.py (o resto, montar.auto pelo contexto).
    python3 edicoes/fables-la-fontaine/glossario/montar.py falta | ver <pasta> <chaves,separadas> | gravar
Depois, python3 ferramentas/lingua_original.py conferir."""
import sys, os, json, re
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
W = os.path.dirname(os.path.dirname(os.path.dirname(AQUI)))   # a raiz do repositório
sys.path.insert(0, os.path.join(W, 'ferramentas'))
import lingua_original as L
import m1, m2, m3, m4, m5, m6
from m1 import M
try:
    from escolhas import E
except ImportError:
    E = {}
PASTAS = ['la-cigale-et-la-fourmi','le-corbeau-et-le-renard','la-grenouille-et-le-boeuf','le-loup-et-le-chien','le-rat-de-ville-et-le-rat-des-champs','le-loup-et-l-agneau','le-chene-et-le-roseau','le-lion-et-le-rat','le-laboureur-et-ses-enfants','le-lievre-et-la-tortue','les-animaux-malades-de-la-peste','la-laitiere-et-le-pot-au-lait']
ob = L.ler_obras()
def cls(k):
    return M.get(k, {}).get('classe', '')
def verbo(k): return cls(k) == 'verbo'
def infin(k): return verbo(k) and M[k].get('forma') == 'infinitivo'
def ppres(k): return verbo(k) and 'particípio presente' in M[k].get('forma', '')
def subst(k): return cls(k).startswith('substantivo') or cls(k) == 'nome próprio'
def auto(toks, i):
    k = toks[i][1]; nx = toks[i+1][1] if i+1 < len(toks) and toks[i+1][2] == toks[i][2] else None
    pv = toks[i-1][1] if i > 0 and toks[i-1][2] == toks[i][2] else None
    nx2 = toks[i+2][1] if i+2 < len(toks) and toks[i+2][2] == toks[i][2] else None
    skip = nx
    if nx in ('lui', 'leur', 'y', 'en', 'en#2') and nx2: skip = nx2
    if k in ('le', 'la', 'les', 'l’'):
        if k == 'l’' and nx == 'on': return 'l’#3'
        if skip and verbo(skip) and pv not in ('à', 'de', 'par', 'pour', 'sur', 'sans', 'dans', 'en'):
            return k + '#2'
    if k in ('de', 'd’'):
        if nx and infin(nx): return k + '#2'
        if pv in ('pas', 'point', 'peu', 'assez', 'rien', 'plus', 'moins', 'beaucoup', 'n’'): return k + '#3'
    if k == 'à' and nx and infin(nx): return 'à#2'
    if k == 'en':
        if nx and ppres(nx): return 'en#3'
        if nx and (verbo(nx) or nx in ('suis',)): return 'en#2'
    if k in ('que', 'qu’'):
        if pv in ('aussi', 'plus', 'moins', 'autant', 'autre'): return k + ('#5' if k == 'que' else '#5')
        if pv and (subst(pv) or pv in ('ce', 'c’')): return k + '#2'
    if k == 'si' and nx and cls(nx) in ('adjetivo', 'advérbio') : return 'si#2'
    if k == 'il' and nx in ('faut', 'fallait', 'faudra', 'advint', 'importe', 'tiendra', 'm’', 'y', 'n’', 'est'): return 'il#2'
    if k == 'bien' and pv == 'eh': return 'bien#5'
    if k == 'des' and pv and (subst(pv) or cls(pv).startswith('adjetivo') or verbo(pv) and 'particípio' in M[pv].get('forma','')): return 'des#2'
    if k == 'plus' : return 'plus#2'
    return k
def montar(pasta, mostrar=None):
    p = [x for x in ob['poemas'] if x['pasta'] == pasta][0]
    toks = [(ref, L.chave(pal), ref.split('.')[0]) for ref, pal, *_ in L.ocorrencias(p)]
    esc = E.get(pasta, {})
    oc, usados, falta = {}, {}, []
    for i, (ref, k, lin) in enumerate(toks):
        a = esc.get(ref) or auto(toks, i)
        if a not in M:
            falta.append((ref, k, a)); continue
        if a != k: oc[ref] = a
        usados[a] = M[a]
        if mostrar is not None and (k in mostrar):
            ctx = ' '.join(t[1] for t in toks[max(0,i-3):i+4] if t[2] == lin)
            print('%-6s %-8s -> %-8s | %s' % (ref, k, a, ctx))
    return {'verbetes': usados, 'ocorrencias': oc}, falta
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'falta':
        for pasta in PASTAS:
            g, f = montar(pasta)
            print(pasta, len(g['verbetes']), 'faltam', len(f), ' '.join(sorted({x[2] for x in f})))
    elif cmd == 'ver':
        pasta = sys.argv[2]; palavras = set(sys.argv[3].split(','))
        montar(pasta, palavras)
    elif cmd == 'gravar':
        for pasta in PASTAS:
            g, f = montar(pasta)
            if f: print('FALTA', pasta, f); continue
            with open(os.path.join(W, 'edicoes/lingua-original', pasta, 'glossario.json'), 'w', encoding='utf-8') as fh:
                json.dump(g, fh, ensure_ascii=False, indent=2); fh.write('\n')
            print('gravado', pasta, len(g['verbetes']))
