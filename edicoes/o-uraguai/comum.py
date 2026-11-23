import json, os, re, unicodedata
D = os.environ.get('URAGUAI_CACHE') or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ferramentas', 'cache', 'o-uraguai') + '/'
CANTOS = {1: range(7, 26), 2: range(27, 52), 3: range(53, 75), 4: range(75, 94), 5: range(95, 109)}
def ws1769():
    return json.load(open(D + 'ws1769.json'))
def canto_de(pag):
    for c, r in CANTOS.items():
        if pag in r: return c
def versos1769():
    """{canto: [(pag, nivel, verso)]}"""
    out = {c: [] for c in CANTOS}
    for p in ws1769():
        c = canto_de(p['pag'])
        if not c: continue
        for v in p['versos']:
            if re.match(r'^(_?CANTO|Fim do Canto)', v, re.I): continue
            if any(re.sub(r'[ſ]', 's', v).startswith(x) for x in ESPURIOS): continue
            out[c].append((p['pag'], p['nivel'], v))
    return out
def wsmod():
    out = {}
    for i, c in enumerate(['I', 'II', 'III', 'IV', 'V'], 1):
        t = open(D + 'wsmod/%s.txt' % c).read()
        t = re.sub(r'\{\{navegar.*?\n\}\}', '', t, flags=re.S)
        poem = '\n'.join(re.findall(r'<poem[^>]*>(.*?)</poem>', t, flags=re.S))
        ls = []
        for l in poem.split('\n'):
            l = re.sub(r"'''?", '', l); l = re.sub(r'<[^>]+>', '', l); l = re.sub(r'\{\{[^}]*\}\}', '', l).strip()
            if l and not any(l.startswith(x) for x in ESPURIOS): ls.append(l)
        out[i] = ls
    return out
def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
# linhas de nota que o texto moderno (Wikisource e Domínio Público) meteu entre os versos
ESPURIOS = ['Aqui não temos. Os padres', 'Aqui não temos. Os Padres', 'portugueses eram gente sem lei', 'portugueses erão gente sem lei', 'O bom padre. Balda.']
WORD = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*")
