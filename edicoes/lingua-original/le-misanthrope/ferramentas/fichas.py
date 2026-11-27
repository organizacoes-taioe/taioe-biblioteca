"""Fichas para o glossário do Misanthrope (fr.wiktionary): por lote de chaves ainda sem verbete, as ocorrências,
os verbetes já feitos noutros textos em francês e as definições do fr.wiktionary (a página da forma e, na forma
flexionada, a do lema).
python3 fichas.py baixar                                   # põe no cache as páginas de todas as chaves (rede)
python3 fichas.py <partes: 1-1,1-2…> <tamanho do lote> <pasta de saída> [<primeiro nº de lote>]"""
import json, os, re, sys
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
import lingua_original as L

PASTA = 'le-misanthrope'
mb = L.achar(PASTA)
g = L.ler_glossario(PASTA) or {'verbetes': {}, 'ocorrencias': {}}
feitos = set(g['verbetes'])
pool = {}
for p in L.ler_obras()['poemas']:
    if p['lingua'] != 'fr' or p['pasta'] == PASTA:
        continue
    gg = L.ler_glossario(p['pasta'])
    for k, v in (gg or {}).get('verbetes', {}).items():
        pool.setdefault(k.split('#')[0], []).append(v)


def simples(t):
    t = re.sub(r'<ref.*?(</ref>|/>)', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '', t)
    for _ in range(3):
        t = re.sub(r'\{\{(?:lexique|term|registre|figuré|figure|familier|fam|vieilli|désuet|littéraire|littéraire|ironique|'
                   r'péjoratif|par extension|en particulier|absolument|poétique|archaïque|vieux|soutenu|populaire|'
                   r'rare|transitif|intransitif|pronominal|plus rare|sens figuré|par analogie|précieux|théâtre|'
                   r'religion|droit|militaire|marine|chasse|cuisine|musique|médecine|courant|ellipse|propre|'
                   r'métonymie|hyperbole|euphémisme|injurieux|vulgaire|argot|Moyen Âge|histoire|féodalité|'
                   r'noblesse|jeux|escrime|équitation|commerce|finance|justice|politique|philosophie|'
                   r'littérature|poésie|rhétorique|grammaire|mythologie|antiquité|Antiquité)'
                   r'(?:\|[^{}]*)?\}\}', lambda m: '(' + re.split(r'[|}]', m.group(0)[2:])[0] + ')', t)
        t = re.sub(r'\{\{(?:lien|l|w|ws|nom w pc|pc|smcp|small|nobr|lien web)\|([^{}|]*)[^{}]*\}\}', r'\1', t)
        t = re.sub(r'\{\{(?:cf|voir)\|([^{}]*)\}\}', lambda m: 'cf. ' + ', '.join(x for x in m.group(1).split('|') if '=' not in x and x != 'fr'), t)
        t = re.sub(r'\{\{[^{}]*\}\}', '', t)
    t = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', t)
    t = re.sub(r"'''?", '', t)
    return ' '.join(t.split())


FLEX = re.compile(r'\{\{fr-verbe-flexion\|(?:[^|{}]*=[^|{}]*\|)*([^|{}=]+)')
LINK = re.compile(r"^#[^#*:].*?\bde\b''?\s*\[\[([^\]|#]+)")


def verbete(pagina):
    """(título, [linhas], lemas) da seção francesa, ou None"""
    try:
        r = L.wikitext('fr', pagina)
    except Exception:
        return None
    if r['erro'] or not r['wikitext']:
        return None
    sec = L.secao_da_lingua(r['wikitext'], 'fr', 'fr')
    if sec is None:
        return None
    linhas, lemas, cab, subs = [], [], None, 0
    for l in sec.split('\n'):
        m = re.match(r'^(=+)\s*(.*?)\s*=+\s*$', l)
        if m:
            c = m.group(2)
            ms = re.match(r'\{\{S\|([^|}]+)(?:\|fr)?(\|flexion)?', c)
            if ms and not L.FORA.search(ms.group(1)) and ms.group(1) not in ('étymologie', 'prononciation', 'traductions', 'voir aussi', 'références', 'anagrammes', 'synonymes', 'dérivés', 'apparentés', 'variantes', 'variantes orthographiques', 'antonymes', 'hyperonymes', 'hyponymes', 'vocabulaire', 'homophones', 'paronymes', 'citations', 'notes', 'note', 'compos', 'expressions', 'locutions', 'quasi-synonymes', 'faux-amis', 'méronymes', 'holonymes', 'gentilés', 'abréviations', 'diminutifs', 'augmentatifs', 'phrases', 'proverbes', 'dérivés autres langues', 'conjugaison', 'attestations', 'transcriptions', 'taux de reconnaissance', 'hist', 'trad-trier'):
                cab = ms.group(1) + (' (flexão)' if ms.group(2) else '')
                linhas.append('<%s>' % cab)
            else:
                cab = None
            continue
        if cab is None:
            continue
        mf = FLEX.search(l)
        if mf:
            lemas.append(mf.group(1).strip())
        mm0 = re.match(r'^(#+)[^*:#]', l)
        if mm0:
            ml = LINK.match(l)
            if ml and 'flexão' in cab:
                lemas.append(ml.group(1).strip())
            s = simples(l[len(mm0.group(1)):])
            nivel = len(mm0.group(1)) - 1
            if nivel == 0:
                subs = 0
            else:
                subs += 1
                if subs > 2:
                    continue
            if s:
                linhas.append('  ' * nivel + '- ' + s[:200 if nivel == 0 else 130])
    lim = [x for i, x in enumerate(linhas) if not (x.startswith('<') and (i + 1 == len(linhas) or linhas[i + 1].startswith('<')))]
    lemas = [x for x in lemas if not re.match(r'^(pp[mf]?[sp]?|ppr|ind|sub|imp|cond|grp|inf|pron|cat|nocat)', x)]
    return r['titulo'], lim[:28], list(dict.fromkeys(lemas))


def candidatos(k, exemplo):
    c = [k]
    if exemplo[:1].isupper():
        c += [exemplo, k[:1].upper() + k[1:]]
    c.append(k.replace('’', "'"))
    return list(dict.fromkeys(x for x in c if x))


def todas_chaves():
    ocs = {}
    for kp, x in L.partes_de(mb, True):
        linhas = {n: t for n, t, _i, _d in L.linhas_do_poema(mb, kp)}
        nome = os.path.splitext(os.path.basename(x['arquivo']))[0]
        for ref, pal, n, *_r in L.ocorrencias(mb, kp):
            k = g.get('ocorrencias', {}).get(ref, L.chave(pal))
            ocs.setdefault(k, []).append((ref, pal, linhas[n].strip(), nome))
    return ocs


if sys.argv[1] in ('baixar', 'baixar-reverso'):
    ocs = todas_chaves()
    feitas = 0
    itens = list(ocs.items())
    if sys.argv[1] == 'baixar-reverso':
        itens.reverse()   # do fim da peça para o começo (enquanto as fichas do começo baixam o resto)
    for k, lst in itens:
        for c in candidatos(k, lst[0][1])[:2]:
            v = verbete(c)
            if v:
                for lema in v[2][:2]:
                    verbete(lema)
                break
        feitas += 1
        if feitas % 100 == 0:
            print(feitas, 'de', len(ocs), flush=True)
    print('pronto')
    sys.exit()

partes = sys.argv[1].split(',')
tam = int(sys.argv[2])
saida = sys.argv[3]
lote = int(sys.argv[4]) - 1 if len(sys.argv) > 4 else 0
os.makedirs(saida, exist_ok=True)
ocs_todas = todas_chaves()
# a chave entra no lote da primeira parte (na ordem da peça) em que aparece
ordem = [os.path.splitext(os.path.basename(x['arquivo']))[0] for _k, x in L.partes_de(mb, True)]
primeira = {k: min(ordem.index(o[3]) for o in lst) for k, lst in ocs_todas.items()}
chaves = [k for k, lst in ocs_todas.items() if k not in feitos and ordem[primeira[k]] in partes]
print(len(chaves), 'chaves novas')
for i in range(0, len(chaves), tam):
    lote += 1
    out = []
    for k in chaves[i:i + tam]:
        lst = ocs_todas[k]
        out.append('### %s   (%d×)' % (k, len(lst)))
        passo = max(1, len(lst) // 5)
        for ref, pal, t, _nome in lst[::passo][:5]:
            out.append('  %s  %s' % (ref, t))
        for v in pool.get(k, [])[:2]:
            out.append('  JÁ FEITO: ' + json.dumps(v, ensure_ascii=False)[:420])
        vistos = set()
        for c in candidatos(k, lst[0][1]):
            v = verbete(c)
            if not v or v[0] in vistos:
                continue
            vistos.add(v[0])
            out.append('  WIKI «%s»:' % v[0])
            out += ['    ' + x for x in v[1][:6 if pool.get(k) else 22]]
            for lema in v[2][:2]:
                if lema in vistos:
                    continue
                w = verbete(lema)
                if w:
                    vistos.add(w[0])
                    out.append('  WIKI lema «%s»:' % w[0])
                    out += ['    ' + x for x in w[1][:6 if pool.get(lema) else 22]]
            break
        if not vistos:
            out.append('  (sem verbete no fr.wiktionary para %s)' % ', '.join(candidatos(k, lst[0][1])))
        out.append('')
    arq = os.path.join(saida, 'fichas-%02d.txt' % lote)
    with open(arq, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print(arq, len(chaves[i:i + tam]), 'chaves', os.path.getsize(arq), 'bytes')
