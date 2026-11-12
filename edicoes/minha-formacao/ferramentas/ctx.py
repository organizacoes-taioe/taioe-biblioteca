import pickle, sys
r = pickle.load(open('/home/geremias/.cache/claude-wt5-minha-formacao/ferramentas/cache/minha-formacao/resultado.pkl', 'rb'))
E = r['E']
for w in sys.argv[1:]:
    ws = w.split()
    for i in range(len(E)):
        if E[i:i + len(ws)] == ws:
            print(f'{w!r}:', ' '.join(E[max(0, i - 8):i + len(ws) + 8]))
