"""Do OCR (ocr/*.json) às linhas gregas limpas de cada página: escolhe a coluna grega, tira ruído, corrige
letras pelo léxico. Grava linhas.json: [{folha, col (nº da coluna da PG), linhas:[{t, rec, y, x0, palavras}]}]
e trocas.tsv (forma do OCR → forma corrigida, contagem)."""
import sys, os, re, json, glob, unicodedata, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lex import corrigir, freq
AQUI = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso')
GREGO = re.compile(r'[Ͱ-Ͽἀ-῿]')
PUNCT = '.,;·:»«“”"\'’᾽()[]—-!?'

def nucleo(t):
    return t.strip(PUNCT + '·;')

def taxa(words):
    ns = [nucleo(w[0]) for w in words]
    ns = [n for n in ns if len(n) >= 3 and GREGO.search(n)]
    if not ns: return 0.0, 0
    return sum(1 for n in ns if freq(n) > 0 or corrigir(n)[1] in ('troca1', 'troca1f')) / len(ns), len(ns)

def limpar_token(t):
    t = unicodedata.normalize('NFC', t)
    t = t.replace('ϐ', 'β').replace('ϑ', 'θ')
    return t

trocas = collections.Counter()
saida = []
ENTRADA = sys.argv[1] if len(sys.argv) > 1 else 'ocr'
DESLOC = int(sys.argv[2]) if len(sys.argv) > 2 else 0     # DCO: p-000 = folha 315
SAIDA = sys.argv[3] if len(sys.argv) > 3 else 'linhas.json'
for f in sorted(glob.glob(os.path.join(AQUI, ENTRADA, '*.json'))):
    folha = int(os.path.basename(f).split('.')[0]) + DESLOC
    d = json.load(open(f, encoding='utf-8'))
    h = d['size'][1]
    esq = 633 + 2 * (folha - 316)
    for ci, col in enumerate(d['cols']):
        boas = []
        for l in col:
            r, n = taxa(l['words'])
            l['taxa'], l['n'] = r, n
        # margem esquerda da coluna: mediana dos x0 das linhas gregas
        greg = [l for l in col if l['n'] >= 2 and l['taxa'] >= .5]
        if len(greg) < 4: continue
        xs = sorted(l['x0'] for l in greg); x0 = xs[len(xs) // 4]
        xr = sorted(max(w[4] for w in l['words']) for l in greg); xmax = xr[len(xr) * 3 // 4]
        import difflib
        xr_lin = sorted(max(w[4] for w in l['words'] if len(nucleo(w[0])) >= 3) for l in greg if any(len(nucleo(w[0])) >= 3 for w in l['words']))
        margem_d = xr_lin[len(xr_lin) * 6 // 10] if xr_lin else 10 ** 6
        col = sorted(col, key=lambda l: l['y'])
        txt = [' '.join(w[0] for w in l['words']) for l in col]
        for k, l in enumerate(col):
            if l.get('relida'):     # releitura que repete a linha vizinha
                mine = [nucleo(w).lower() for w in txt[k].split() if len(nucleo(w)) >= 3]
                cf = lambda q: sum(w[1] for w in q['words']) / len(q['words'])
                for j in (k - 1, k + 1):
                    if not (0 <= j < len(col)) or col[j].get('relida'): continue
                    vv = [nucleo(w).lower() for w in txt[j].split() if len(nucleo(w)) >= 3]
                    iguais = sum(1 for w in mine if any(difflib.SequenceMatcher(None, w, x).ratio() > .75 for x in vv))
                    if mine and iguais / len(mine) >= .5:
                        (col[j] if cf(col[j]) < cf(l) else l)['dup'] = True
        for l in col:
            if l.get('dup'): continue
            if l['y'] < h * .066 or l['y'] > h * .95: continue
            l['words'] = [w for w in l['words'] if not (w[2] > margem_d - 5 and len(nucleo(w[0])) <= 3)] or l['words']      # cabeçalho, pé
            ws = sorted(l['words'], key=lambda w: w[2])
            # corta pelo vão grande: sujeira na margem, letras A B C D na calha, sobras da outra coluna
            grupos, g = [], [ws[0]]
            for w in ws[1:]:
                if w[2] - g[-1][4] > 70: grupos.append(g); g = [w]
                else: g.append(w)
            grupos.append(g)
            ws = max(grupos, key=lambda g: sum(len(nucleo(w[0])) for w in g))
            ws = [w for w in ws if not (w[4] < x0 - 8 and len(nucleo(w[0])) <= 2)]
            ws = [w for w in ws if w[0] not in ('Α', 'Β', 'Γ', 'Δ', 'C', 'D', 'B', 'A', 'Ο', 'Ὁ\u0332')]   # letras da calha
            if not ws: continue
            conf = sum(w[1] for w in ws) / len(ws)
            r, n = taxa(ws)
            if conf < (45 if l.get('relida') else 60) and r < .6: continue          # latim lido como grego (confiança baixa)
            if n >= 2 and r < .34: continue          # latim que invadiu
            if n == 0 and not any(GREGO.search(w[0]) for w in ws): continue
            if n <= 1 and r == 0 and len(ws) <= 2 and l['y'] > h * .85: continue   # nota de pé solta
            toks = []
            for w in ws:
                t = limpar_token(w[0])
                m = re.match(r'^([^\w]*)(.*?)([^\w]*)$', t)
                a, core, b = m.groups()
                toks.append([a + core + b, w[1], w[2], w[3], w[4], w[5]])
            boas.append({'y': l['y'], 'y1': l['y1'], 'x0': ws[0][2], 'rec': ws[0][2] - x0, 'toks': toks})
        # notas de pé: de baixo para cima, depois de um vão grande no fim da página, as linhas que não são grego
        corte = None
        for k in range(len(boas) - 1, max(0, len(boas) - 6), -1):
            if boas[k]['y'] - boas[k - 1]['y1'] > 60 and boas[k]['y'] > h * .75:
                corte = k; break
        if corte is not None:
            fica = boas[:corte]
            for b in boas[corte:]:
                tx = taxa([[t[0]] for t in b['toks']])[0]
                ruim = tx < .5 or re.match(r'^[\d\W]', b['toks'][0][0])
                if not ruim: fica.append(b)
            boas = fica
        # recuo pela margem local (a página costuma estar torta): 30º percentil dos x0 das 15 linhas vizinhas
        for k, l in enumerate(boas):
            viz = sorted(b['x0'] for b in boas[max(0, k - 7):k + 8])
            l['rec'] = l['x0'] - viz[len(viz) * 3 // 10]
        if boas:
            saida.append({'folha': folha, 'ci': ci, 'col': esq + ci, 'x0': x0, 'linhas': boas})
json.dump(saida, open(os.path.join(AQUI, SAIDA), 'w', encoding='utf-8'), ensure_ascii=False)
with open(os.path.join(AQUI, 'trocas.tsv'), 'w', encoding='utf-8') as o:
    for (a, b), n in trocas.most_common(): o.write(f'{a}\t{b}\t{n}\n')
por = collections.Counter(s['folha'] for s in saida)
print('páginas', len(por), 'com duas colunas gregas:', [k for k, v in por.items() if v > 1])
