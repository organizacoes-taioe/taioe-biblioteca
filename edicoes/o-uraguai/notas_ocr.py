"""Notas de rodapé de 1769 pelas quatro leituras OCR (TB mestre; AB, AT, TT votam) e o WS de 1769 (páginas revisadas).
Grava notas_ocr.json: [{pag, ini (começa nota nova?), texto (voto), leituras}] por parágrafo de nota."""
import json, os, re, sys, difflib, collections
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI)
from comum import *
import linhas as LN
from confronto import L
MT = {int(k): v for k, v in json.load(open(os.path.join(AQUI, 'mapa_tor.json'))).items()}
CONF = json.load(open(D + 'confronto.json'))
TOKN = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*|\d+|[^\s\w]")

def ultimo_verso(pag, fonte):
    ls = [x['leit'].get(fonte) for x in CONF if x['pag'] == pag]
    return [l['linha'] for l in ls if l]

def regiao(ls, versos, alt_nota):
    """linhas depois do último verso, sem o reclamo; devolve [(x0, texto)]."""
    idx = [i for i, l in enumerate(ls) if l[2] in versos]
    ini = (max(idx) + 1) if idx else 0
    out = []
    for l in ls[ini:]:
        hs = sorted(w[3] - w[1] for w in l[3]); h = hs[len(hs) // 2]
        letras = sum(c.isalpha() for c in l[2])
        if letras < 4 or len(l[3]) <= 2 and not out: continue      # reclamo, sujeira
        if h > alt_nota: continue                                  # resto de verso
        out.append((l[1], l[2]))
    return out

def juntar(linhas):
    """parágrafos: linha recuada abre nota nova; hífen no fim da linha junta a palavra."""
    if not linhas: return []
    xs = sorted(x for x, t in linhas); base = xs[len(xs) // 2]
    pars = []
    for x, t in linhas:
        nova = x > base + (25 if base > 100 else 5)
        t = t.strip()
        if not pars or nova: pars.append({'ini': nova, 't': t})
        else:
            p = pars[-1]['t']
            if re.search(r'[\w][-¬]$', p): pars[-1]['t'] = p[:-1] + t
            else: pars[-1]['t'] = p + ' ' + t
    return pars

def pagina(pag):
    fontes = {}
    bos = D + 'bos/ouruaguaypoema00gama.pdf'; tor = D + 'tor/ouraguaypoema00gama.pdf'
    tp = MT.get(pag)
    fontes['TB'] = regiao(LN.tess(D + 'bos/tess/%03d.tsv' % pag), set(ultimo_verso(pag, 'TB')), 45)
    fontes['AB'] = regiao(LN.pdf(bos, pag), set(ultimo_verso(pag, 'AB')), 5.8)
    if tp:
        fontes['TT'] = regiao(LN.tess(D + 'tor/tess/%03d.tsv' % tp), set(ultimo_verso(pag, 'TT')), 45)
        fontes['AT'] = regiao(LN.pdf(tor, tp), set(ultimo_verso(pag, 'AT')), 5.8)
    return {f: juntar(v) for f, v in fontes.items()}

if __name__ == '__main__' and sys.argv[1:] != ['--todas']:
    import pprint
    for p in map(int, sys.argv[1:]):
        r = pagina(p)
        for f, ps in r.items():
            print('==', p, f)
            for x in ps: print('  ', '*' if x['ini'] else ' ', x['t'][:150])

# ------------------------------------------------------------------ voto
def toks(s):
    s = s.replace('’', "'")
    return TOKN.findall(s)

def chave(t):
    if re.match(r'[^\W\d_]', t): return L(t) or t.lower()
    return {';': ',', ':': ',', '5': ','}.get(t, t)

def alinhar(M, O):
    """para cada token de M, o token de O alinhado (ou None)."""
    A = [chave(t) for t in M]; B = [chave(t) for t in O]
    res = [None] * len(M)
    for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes():
        if op == 'equal' or (op == 'replace' and a2 - a1 == b2 - b1):
            for k in range(a2 - a1): res[a1 + k] = O[b1 + k]
        elif op == 'replace':
            usados = set()
            for k in range(a1, a2):
                best, bj = 0, None
                for j in range(b1, b2):
                    if j in usados: continue
                    r = difflib.SequenceMatcher(None, A[k], B[j]).ratio()
                    if r > best: best, bj = r, j
                if bj is not None and best >= 0.5: usados.add(bj); res[k] = O[bj]
    return res

def votar(pag, ws_notas=None):
    r = pagina(pag)
    if not r.get('TB'): return []
    M = []; marcas = []
    for p in r['TB']:
        marcas.append(len(M)); M += toks(p['t'])
    outros = {f: [t for p in ps for t in toks(p['t'])] for f, ps in r.items() if f != 'TB'}
    if ws_notas:
        outros['WS'] = [t for n in ws_notas for t in toks(n)]
    al = {f: alinhar(M, O) for f, O in outros.items()}
    saida = []; duvidas = []
    for i, t in enumerate(M):
        cand = [('TB', t)] + [(f, al[f][i]) for f in al if al[f][i] is not None]
        peso = collections.Counter()
        for f, c in cand:
            peso[chave(c)] += 2 if f == 'WS' else 1
        (k, n), = peso.most_common(1)
        formas = collections.Counter(c for f, c in cand if chave(c) == k)
        # forma: a do WS, se votou nela; senão a mais comum entre as que dão a chave vencedora
        ws = [c for f, c in cand if f == 'WS' and chave(c) == k]
        forma = ws[0] if ws else formas.most_common(1)[0][0]
        saida.append(forma)
        tot = sum(peso.values())
        if n * 2 <= tot or tot < 3: duvidas.append((i, forma, dict(cand)))
    pars = []
    for j, m in enumerate(marcas):
        fim = marcas[j + 1] if j + 1 < len(marcas) else len(saida)
        pars.append({'pag': pag, 'ini': r['TB'][j]['ini'], 'toks': saida[m:fim],
                     'duvidas': [(i - m, f, c) for i, f, c in duvidas if m <= i < fim]})
    return pars

def ws_notas(pag):
    """notas do WS de 1769 na página (só revisadas): as continuações (follow) primeiro, depois as outras."""
    for p in ws1769():
        if p['pag'] == pag and p['nivel'] >= 3:
            seg = [n['texto'] for n in p['notas'] if n['segue']]
            out = [n['texto'] for n in p['notas'] if not n['segue'] and n['texto'].strip()]
            return [re.sub(r'_', '', t) for t in seg + out] or None
    return None

def todas():
    pars = []
    for pag in range(5, 111):
        try:
            pars += votar(pag, ws_notas(pag))
        except FileNotFoundError:
            pass
    return pars

if __name__ == '__main__' and sys.argv[1:] == ['--todas']:
    pars = todas()
    json.dump(pars, open(D + 'notas_voto.json', 'w'), ensure_ascii=False, indent=0)
    for p in pars:
        print('%3d %s %s' % (p['pag'], '*' if p['ini'] else ' ', ' '.join(p['toks'])[:200]))
