"""As chaves das fichas (### chave) que ainda não têm verbete no glossario.json do Misanthrope.
python3 edicoes/lingua-original/le-misanthrope/ferramentas/faltam.py <pasta das fichas> [fichas-NN.txt ...]"""
import glob, json, os, re, sys
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
arq = os.path.join(RAIZ, 'edicoes', 'lingua-original', 'le-misanthrope', 'glossario.json')
vb = json.load(open(arq, encoding='utf-8'))['verbetes'] if os.path.exists(arq) else {}
nomes = sys.argv[2:] or sorted(os.path.basename(x) for x in glob.glob(os.path.join(sys.argv[1], 'fichas-*.txt')))
total = 0
for nome in nomes:
    ks = re.findall(r'(?m)^### (\S+)', open(os.path.join(sys.argv[1], nome), encoding='utf-8').read())
    f = [k for k in ks if k not in vb]
    total += len(f)
    print('%s: %d chaves, %d sem verbete%s' % (nome, len(ks), len(f), (': ' + ' '.join(f[:40])) if f else ''))
sys.exit(1 if total else 0)
