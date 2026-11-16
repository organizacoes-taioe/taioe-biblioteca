"""Das linhas gregas (linhas.json do IA, linhas-dco.json da 2ª leitura) ao texto: junta hifenizadas, corrige pelo
léxico e pela 2ª leitura, tira os números dos escólios, separa parágrafos pelo recuo. Grava:
  bruto.txt      blocos (parágrafos de Rader) com {PG 88.n}; a palavra duvidosa leva ⟦id⟧ logo depois, se --ids
  blocos.json    [{'texto', 'toks': [ids das palavras]}]
  duvidas.json   palavras sem decisão: {id, folha, caixa, caixa2, ocr, dco}
Decisões da conferência nas imagens: correcoes.json ({id: forma}); «=» mantém a do OCR."""
import sys, os, re, json, unicodedata, difflib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lex import corrigir2 as corrigir, chave as lchave
AQUI = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso')
GREGO = re.compile(r'[Ͱ-Ͽἀ-῿]')
PUN = re.compile(r'^([«“"(\[]*)(.*?)([.,;·:»”"\'’᾽)\]!]*)$')


def tokens(pags):
    toks = []
    for p in pags:
        toks.append({'m': '{PG 88.%d}' % p['col'], 'folha': p['folha']})
        for l in p['linhas']:
            n = len(l['toks'])
            for i, t in enumerate(l['toks']):
                toks.append({'t': unicodedata.normalize('NFC', t[0]), 'folha': p['folha'], 'caixa': t[2:6], 'conf': t[1],
                             'par': i == 0 and l['rec'] > 30, 'ult': i == n - 1})
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if 't' in t and t['ult'] and re.search(r'[-‐]\W?$', t['t']) and len(t['t']) > 1:
            j, marcas = i + 1, []
            while j < len(toks) and 'm' in toks[j]: marcas.append(toks[j]); j += 1
            if j < len(toks) and GREGO.match(toks[j]['t']):
                n = toks[j]
                u = dict(t); u['t'] = re.sub(r'[-‐]\W?$', '', t['t']) + n['t']; u['caixa2'] = [n['folha']] + n['caixa']
                u['ult'] = n['ult']; u['conf'] = min(t['conf'], n['conf'])
                out.append(u); out.extend(marcas); i = j + 1
                continue
        out.append(t); i += 1
    return out


def nucleo(w):
    return PUN.match(w).groups()


def k(w):
    return lchave(nucleo(w)[1]) if w else ''


ia = tokens(json.load(open(os.path.join(AQUI, 'linhas.json'), encoding='utf-8')))
dco_arq = os.path.join(AQUI, 'linhas-dco.json')
lado = {(p['folha'], p['ci']) for p in json.load(open(os.path.join(AQUI, 'linhas.json'), encoding='utf-8'))}
dco = tokens([p for p in json.load(open(dco_arq, encoding='utf-8')) if (p['folha'], p['ci']) in lado]) if os.path.exists(dco_arq) else []
por_folha, ia_folha, par_dco = {}, {}, {}
for t in dco:
    if 't' in t: por_folha.setdefault(t['folha'], []).append(t)
for idx, t in enumerate(ia):
    if 't' in t: ia_folha.setdefault(t['folha'], []).append(idx)
for f, idxs in ia_folha.items():
    d = por_folha.get(f, [])
    if not d: continue
    a = [k(ia[i]['t']) for i in idxs]; b = [k(x['t']) for x in d]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
            for x in range(i2 - i1): par_dco[idxs[i1 + x]] = d[j1 + x]['t']

FIX = {}
fx = os.path.join(AQUI, 'correcoes.json')
if os.path.exists(fx): FIX = json.load(open(fx, encoding='utf-8'))
IDS = '--ids' in sys.argv
duv, texto, est = [], [], collections.Counter()
for idx, t in enumerate(ia):
    if 'm' in t: texto.append(('M', t['m'], None)); continue
    w = t['t']
    if re.fullmatch(r'\(\w{1,3}\)[.,;·:»]*', w):       # número de escólio
        rest = re.sub(r'^\(\w{1,3}\)', '', w)
        if rest:
            for q in range(len(texto) - 1, -1, -1):
                if texto[q][0] != 'M': texto[q] = (texto[q][0], texto[q][1] + rest, texto[q][2]); break
        continue
    w = re.sub(r'\(\w{1,3}\)', '', w)
    if not re.search(r'\w', w):                          # pontuação solta: «"», «-», «᾽» são a ano teleia
        p = {'"': '·', '“': '·', '-': '·', '—': '·', '᾽': '·', '·': '·', '.': '.', ',': ',', ';': ';', ':': ':', '»': '»', '«': '«'}.get(w.strip(), '')
        if p and p != '«':
            for q in range(len(texto) - 1, -1, -1):
                if texto[q][0] != 'M': texto[q] = (texto[q][0], texto[q][1] + p, texto[q][2]); break
        continue
    if len(w) > 2 and w[0] == 'ε' and w[1].isupper(): w = '«' + w[1:]
    a, core, b = nucleo(w)
    b = b.replace('"', '·').replace('“', '·')
    if b in ('-', '᾽') and not t['ult'] and not re.search(r'[βγδθκλμπρστφχψ]$', core): b = '·'
    if a in ('"', '“'): a = '«'
    if b.startswith(';') and core and corrigir(core)[1] == '?' and corrigir(core + 'ς')[1] != '?':
        core, b = core + 'ς', b[1:]
    tid = '%d:%d:%d' % (t['folha'], t['caixa'][0], t['caixa'][1])
    why = ''
    if tid in FIX:
        if FIX[tid] != '=': core = FIX[tid]
        why = 'fix'
    elif core and GREGO.search(core):
        c2, why = corrigir(core)
        if why == '?':
            d = par_dco.get(idx)
            dc = nucleo(d)[1] if d else ''
            d2, dwhy = corrigir(dc) if dc else ('', '?')
            if dc and dwhy != '?':
                c2, why = d2, 'dco'
            elif dc and lchave(dc) == lchave(core):
                why = '2x'
            else:
                duv.append({'id': tid, 'folha': t['folha'], 'caixa': t['caixa'], 'caixa2': t.get('caixa2'), 'ocr': core, 'dco': dc})
        core = c2
    est[why or 'lex'] += 1
    s = a + core + b
    if IDS and why == '?': s += '⟦%s⟧' % tid
    texto.append(('P' if t['par'] else 'W', s, tid))

# pontuação no começo da palavra vai para a anterior (a palavra fica com o id dela)
limpo = []
for x in texto:
    if x[0] != 'M' and limpo and re.match(r'^[.,;·:»”]', x[1]):
        m = re.match(r'^([.,;·:»”]+)(.*)$', x[1])
        for q in range(len(limpo) - 1, -1, -1):
            if limpo[q][0] != 'M': limpo[q] = (limpo[q][0], limpo[q][1] + m.group(1), limpo[q][2]); break
        if not m.group(2): continue
        x = (x[0], m.group(2), x[2])
    limpo.append(x)
texto = limpo
blocos, cur, ids = [], [], []
for x in texto:
    if x[0] == 'M': cur.append((x[1], None)); continue
    ant = next((c for c, i in reversed(cur) if i), '')
    if x[0] == 'P' and ant and re.search(r'[.;·:»)!]$', ant):
        blocos.append({'texto': ' '.join(c for c, _ in cur), 'pal': cur}); cur = []
    cur.append((x[1], x[2]))
if cur: blocos.append({'texto': ' '.join(c for c, _ in cur), 'pal': cur})
open(os.path.join(AQUI, 'bruto.txt'), 'w', encoding='utf-8').write('\n\n'.join(b['texto'] for b in blocos))
json.dump(blocos, open(os.path.join(AQUI, 'blocos.json'), 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(duv, open(os.path.join(AQUI, 'duvidas.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('blocos', len(blocos), 'palavras', sum(len(b['texto'].split()) for b in blocos), 'dúvidas', len(duv), dict(est))
