"""Fichas para o glossário do Macbeth: por lote de chaves ainda sem verbete, as ocorrências, os
verbetes já feitos noutros textos em inglês e as definições do en.wiktionary (forma e lema).
python3 fichas.py <worktree> <partes: 1-1,1-2…> <tamanho do lote> <pasta de saída>"""
import json, os, re, sys
WT = sys.argv[1]
sys.path.insert(0, os.path.join(WT, 'ferramentas'))
import lingua_original as L

partes = sys.argv[2].split(',')
tam = int(sys.argv[3])
saida = sys.argv[4]
os.makedirs(saida, exist_ok=True)
mb = L.achar('macbeth')
g = L.ler_glossario('macbeth') or {'verbetes': {}, 'ocorrencias': {}}
feitos = set(g['verbetes'])
pool = {}
for p in L.ler_obras()['poemas']:
    if p['lingua'] != 'en' or p['pasta'] == 'macbeth':
        continue
    gg = L.ler_glossario(p['pasta'])
    for k, v in (gg or {}).get('verbetes', {}).items():
        pool.setdefault(k.split('#')[0], []).append(v)

def simples(t):
    t = re.sub(r'<ref.*?(</ref>|/>)', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '', t)
    for _ in range(3):
        t = re.sub(r'\{\{(?:lb|lbl|label)\|en\|([^{}]*)\}\}', lambda m: '(' + ', '.join(x for x in m.group(1).split('|') if x and x != '_' and '=' not in x) + ')', t)
        t = re.sub(r'\{\{(?:l|m|w|ll|1|cap|taxlink|vern|q|qualifier|i|gloss|gl|sense)\|(?:en\|)?([^{}|]*)[^{}]*\}\}', r'\1', t)
        t = re.sub(r'\{\{(?:non-gloss definition|n-g|ngd)\|([^{}]*)\}\}', r'\1', t)
        t = re.sub(r'\{\{([a-z -]*(?: of|form|sp|spelling))\|en\|([^{}|]*)[^{}]*\}\}', r'[\1: \2]', t)
        t = re.sub(r'\{\{(en-[a-z -]+ of)\|([^{}|]*)[^{}]*\}\}', r'[\1: \2]', t)
        t = re.sub(r'\{\{[^{}]*\}\}', '', t)
    t = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', t)
    t = re.sub(r"'''?", '', t)
    return ' '.join(t.split())

FORMA = re.compile(r'\{\{([a-z -]*(?: of|form|sp|spelling))\|en\|([^{}|]+)|\{\{(en-[a-z -]+ of)\|([^{}|]+)')

def verbete(pagina):
    """(título, [linhas], lemas) do verbete inglês, ou None"""
    try:
        r = L.wikitext('en', pagina)
    except Exception as e:
        return None
    if r['erro'] or not r['wikitext']:
        return None
    sec = L.secao_da_lingua(r['wikitext'], 'en', 'en')
    if sec is None:
        return None
    linhas, lemas, cab, subs = [], [], None, 0
    for l in sec.split('\n'):
        m = re.match(r'^(=+)\s*(.*?)\s*=+\s*$', l)
        if m:
            cab = m.group(2)
            if not L.FORA.search(cab) and cab not in ('English',) and not cab.startswith('Etymology') and cab not in ('Alternative forms', 'Usage notes', 'Conjugation', 'Declension', 'Hypernyms', 'Hyponyms', 'Coordinate terms', 'Collocations', 'Meronyms', 'Holonyms', 'Troponyms', 'Statistics', 'Gallery', 'Notes', 'Trivia', 'Abbreviations'):
                linhas.append('<%s>' % cab)
            else:
                cab = None
            continue
        if cab is None:
            continue
        mm0 = re.match(r'^(#+)[^*:#]', l)
        if mm0:
            for mm in FORMA.finditer(l):
                lemas.append((mm.group(2) or mm.group(4)).strip())
            s = simples(l[len(mm0.group(1)):])
            nivel = len(mm0.group(1)) - 1
            if nivel == 0:
                subs = 0
            else:
                subs += 1
                if subs > 2:
                    continue
            if s:
                linhas.append('  ' * nivel + '- ' + s[:170 if nivel == 0 else 120])
    # tira cabeçalhos sem definição
    lim = []
    for i, x in enumerate(linhas):
        if x.startswith('<') and (i + 1 == len(linhas) or linhas[i + 1].startswith('<')):
            continue
        lim.append(x)
    defs = [x for x in lim if x.lstrip().startswith('- ')]
    so_formas = defs and len(defs) <= 3 and all(x.startswith('- [') for x in defs[:1])
    return r['titulo'], lim[:24], list(dict.fromkeys(lemas)) if so_formas else []

def candidatos(k, exemplo):
    c = [k]
    if exemplo[:1].isupper():
        c.append(exemplo)
        c.append(k[:1].upper() + k[1:])
    if "'" in k:
        c += [re.sub(r"'d$", 'ed', k), re.sub(r"'st$", 'est', k), re.sub(r"'s$", '', k), k.replace("'", '')]
    if k.endswith("'s"):
        c.append(k[:-2])
    return list(dict.fromkeys(x for x in c if x))

ocs = {}
for nome in partes:
    kp, _x = L.achar_parte(mb, nome)
    linhas = {n: t for n, t, _i, _d in L.linhas_do_poema(mb, kp)}
    for ref, pal, n, *_r in L.ocorrencias(mb, kp):
        k = g.get('ocorrencias', {}).get(ref, L.chave(pal))
        if k in feitos:
            continue
        ocs.setdefault(k, []).append((ref, pal, linhas[n].strip()))
chaves = list(ocs)
print(len(chaves), 'chaves novas')
lote = 0
for i in range(0, len(chaves), tam):
    lote += 1
    out = []
    for k in chaves[i:i + tam]:
        lst = ocs[k]
        out.append('### %s   (%d×)' % (k, len(lst)))
        passo = max(1, len(lst) // 6)
        for ref, pal, t in lst[::passo][:6]:
            out.append('  %s  %s' % (ref, t))
        for v in pool.get(k, [])[:2]:
            out.append('  JÁ FEITO: ' + json.dumps(v, ensure_ascii=False)[:500])
        vistos = set()
        for c in candidatos(k, lst[0][1]):
            v = verbete(c)
            if not v or v[0] in vistos:
                continue
            vistos.add(v[0])
            out.append('  WIKI «%s»:' % v[0])
            out += ['    ' + x for x in v[1][:8 if pool.get(k) else 24]]
            for lema in v[2][:2]:
                if lema in vistos:
                    continue
                w = verbete(lema)
                if w:
                    vistos.add(w[0])
                    out.append('  WIKI lema «%s»:' % w[0])
                    out += ['    ' + x for x in w[1]]
            break
        if not vistos:
            out.append('  (sem verbete no en.wiktionary para %s)' % ', '.join(candidatos(k, lst[0][1])))
        out.append('')
    arq = os.path.join(saida, 'fichas-%02d.txt' % lote)
    with open(arq, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print(arq, len(chaves[i:i + tam]), 'chaves', os.path.getsize(arq), 'bytes')

# ------------------------------------------------------------------ mapear e revisar
# mapear.txt: as chaves com variantes (chave#2…) e cada ocorrência delas nestas partes, com a chave de agora;
# revisar.txt: as chaves já feitas (palavras de conteúdo, sem variantes) que voltam nestas partes, com a
# definição de agora e os versos daqui, para ver se o sentido é o mesmo
vb = g['verbetes']
bases = {}
for k in vb:
    bases.setdefault(k.split('#')[0], []).append(k)
GRAM = re.compile(r'artigo|preposição|conjunção|pronome|auxiliar|numeral|interjeição|contração')
def curta(x):
    d = x.get('def') or [x.get('nota', '')] if 'partes' not in x else [' + '.join(p.get('def', [''])[0] for p in x['partes'])]
    return ('%s; %s' % (x.get('classe', ''), (d[0] if d else '')[:90]))
mapear, revisar = [], []
porchave = {}
for nome in partes:
    kp, _x = L.achar_parte(mb, nome)
    linhas = {n: t for n, t, _i, _d in L.linhas_do_poema(mb, kp)}
    for ref, pal, n, *_r in L.ocorrencias(mb, kp):
        k = g.get('ocorrencias', {}).get(ref, L.chave(pal))
        b = k.split('#')[0]
        if b in feitos or b in bases:
            porchave.setdefault(b, []).append((ref, k, linhas[n].strip()))
for b, lst in porchave.items():
    vs = sorted(bases.get(b, []))
    if len(vs) > 1:
        mapear.append('### %s' % b)
        for v in vs:
            mapear.append('  = %-12s %s' % (v, curta(vb[v])))
        for ref, k, t in lst:
            mapear.append('  %-9s [%s] %s' % (ref, k, t))
        mapear.append('')
    elif vs and vb[vs[0]].get('classe') != 'nome próprio' and (not GRAM.search(vb[vs[0]].get('classe', '')) or '«' in vb[vs[0]].get('nota', '')):
        x = vb[vs[0]]
        revisar.append('### %s  = %s%s' % (b, curta(x), '  (nota: %s)' % x['nota'][:140] if x.get('nota') else ''))
        for ref, k, t in lst[:3]:
            revisar.append('  %-9s %s' % (ref, t))
for nome, conteudo in (('mapear.txt', mapear), ('revisar.txt', revisar)):
    with open(os.path.join(saida, nome), 'w', encoding='utf-8') as f:
        f.write('\n'.join(conteudo))
    print(nome, os.path.getsize(os.path.join(saida, nome)), 'bytes')
