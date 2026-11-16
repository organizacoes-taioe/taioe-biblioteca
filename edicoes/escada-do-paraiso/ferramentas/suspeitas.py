"""suspeitas.py [NN …]: palavras do grego de original/degrau-NN.txt que não estão no léxico (First1KGreek + Perseus,
pelo lex.py da pasta de trabalho), com o bloco e, quando acha, a folha, o x e o y da linha no OCR.
Grava ~/.cache/claude-pedidos-0511/escada-do-paraiso/suspeitas/degrau-NN.tsv"""
import sys, os, re, json
W = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso')
sys.path.insert(0, os.path.join(W, 'scripts'))
from lex import corrigir2, chave
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GREGO = re.compile(r'[Ͱ-Ͽἀ-῿]')
loc = {}
for p in json.load(open(os.path.join(W, 'linhas.json'), encoding='utf-8')):
    for l in p['linhas']:
        for t in l['toks']:
            loc.setdefault(chave(re.sub(r'[^\w]', '', t[0])), []).append((p['folha'], t[2], t[3]))
os.makedirs(os.path.join(W, 'suspeitas'), exist_ok=True)
args = sys.argv[1:] or [str(n) for n in range(1, 31)]
tot = 0
for a in args:
    n = int(a)
    s = open(os.path.join(AQUI, 'original', 'degrau-%02d.txt' % n), encoding='utf-8').read()
    out = []
    for b in s.split('\n\n'):
        m = re.match(r'\[(\d+\.\d+)\]', b)
        if not m: continue
        for w in re.sub(r'\{PG[^}]*\}', ' ', b[m.end():]).split():
            core = re.sub(r'^[^\w]+|[^\w]+$', '', w)
            if not core or not GREGO.search(core) or len(core) < 3: continue
            if corrigir2(core)[1] == '?':
                L = loc.get(chave(re.sub(r'[^\w]', '', core)), [])
                out.append('%s\t%s\t%s' % (m.group(1), core, ' '.join('%d:%d:%d' % x for x in L[:2])))
    open(os.path.join(W, 'suspeitas', 'degrau-%02d.tsv' % n), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    tot += len(out); print(n, len(out))
print('total', tot)
