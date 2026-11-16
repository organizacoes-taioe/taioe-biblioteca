"""Confere tradução × original: python3 ferramentas/conferir.py [NN …] (na pasta da obra; sem argumento, todos os
que têm tradução). Blocos na mesma ordem, as mesmas marcas [n.k], os subtítulos ## no mesmo lugar, título na 1ª
linha, nenhuma coluna {PG} na tradução, nenhuma mesóclise."""
import os, re, sys
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MESO = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")


def blocos(arq):
    s = open(arq, encoding='utf-8').read().replace('\r', '')
    linhas = s.split('\n')
    cab = {}
    while linhas and (linhas[0].startswith('# ') or not linhas[0].strip()):
        m = re.match(r'# (\w+): (.*)', linhas[0])
        if m: cab[m.group(1)] = m.group(2)
        linhas.pop(0)
    return cab, [b.strip() for b in '\n'.join(linhas).split('\n\n') if b.strip()]


def marca(b):
    if b.startswith('## '): return '##'
    m = re.match(r'\[(\d+\.\d+)\]', b)
    return m.group(1) if m else None


def conferir(nome):
    o = os.path.join(AQUI, 'original', nome); t = os.path.join(AQUI, 'traducao', nome)
    erros = []
    co, bo = blocos(o); ct, bt = blocos(t)
    if 'titulo' not in ct: erros.append('sem # titulo')
    if len(bo) != len(bt): erros.append('blocos: original %d, tradução %d' % (len(bo), len(bt)))
    for i, (x, y) in enumerate(zip(bo, bt)):
        if marca(x) != marca(y):
            erros.append('bloco %d: marca %s no original, %s na tradução (%s…)' % (i + 1, marca(x), marca(y), y[:40])); break
    if bt and marca(bt[0]) is not None: erros.append('o 1º bloco deve ser o título do degrau')
    for i, y in enumerate(bt):
        if '{PG' in y: erros.append('bloco %d com {PG}' % (i + 1))
        if MESO.search(y): erros.append('mesóclise no bloco %d: %s' % (i + 1, MESO.search(y).group(0)))
        if re.search(r'[Ͱ-Ͽἀ-῿]{4,}', y) and not re.search(r'_[^_]*[Ͱ-Ͽἀ-῿]', y):
            erros.append('grego solto no bloco %d' % (i + 1))
    return erros


args = sys.argv[1:]
nomes = ['degrau-%02d.txt' % int(a) for a in args] if args else sorted(
    f for f in os.listdir(os.path.join(AQUI, 'traducao')) if f.endswith('.txt'))
tudo_ok = True
for n in nomes:
    if not os.path.exists(os.path.join(AQUI, 'traducao', n)): print(n, 'sem tradução'); tudo_ok = False; continue
    e = conferir(n)
    print(n, 'ok' if not e else '\n  ' + '\n  '.join(e))
    tudo_ok = tudo_ok and not e
sys.exit(0 if tudo_ok else 1)
