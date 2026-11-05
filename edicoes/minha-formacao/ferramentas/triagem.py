import csv, sys, re, unicodedata
def k(w):
    w = unicodedata.normalize('NFD', w.lower().replace('œ','oe'))
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in w if unicodedata.category(c) != 'Mn'))
pg = open('/home/geremias/.cache/claude-wt5-minha-formacao/ferramentas/cache/minha-formacao/pg76030.txt', encoding='utf-8').read()
lex = set(k(w) for w in re.findall(r'[^\W\d_]+', pg))
for r in csv.reader(open(sys.argv[1], encoding='utf-8'), delimiter='\t'):
    if r[0] == 'decisão' or r[0].startswith(('maioria (pg', 'pontuação', 'espaços')):
        continue
    L = dict(x.split(': ', 1) if ': ' in x else (x.rstrip(':'), '') for x in r[4].split(' || '))
    p = [k(w) for w in L.get('pg', '').split() if k(w)]
    plaus = []
    for n in ('ia', 'hv'):
        ws = [k(w) for w in L.get(n, '').split() if k(w)]
        if ws and ws != p and all(w in lex or w.isdigit() for w in ws) and ''.join(ws) != ''.join(p):
            plaus.append(n)
    if plaus or r[0].startswith('maioria (ia'):
        print(r[0], '|', r[2][-35:], '[', r[4], ']', r[6][:25], '| mod:', r[5])
