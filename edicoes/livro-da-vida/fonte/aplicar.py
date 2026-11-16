"""Aplica correções de leitura ao original/: TSV com «marca<TAB>errado<TAB>certo<TAB>motivo» (marca = 6.1, ou 00/41
para prólogo e epílogo + o nº do parágrafo: «00.2»). Troca só dentro do parágrafo marcado, só se «errado» aparece
ali exatamente uma vez; senão avisa. Uso: python3 fonte/aplicar.py correcoes.tsv [--aplicar]"""
import re, sys, os
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def blocos(f):
    cab, _, corpo = open(f, encoding='utf-8').read().partition('\n\n')
    return cab, re.split(r'\n\n', corpo.rstrip('\n'))
apl = '--aplicar' in sys.argv
ok = falha = 0
arqs = {}
for ln in open(sys.argv[1], encoding='utf-8'):
    if not ln.strip() or ln.startswith('#'): continue
    p = ln.rstrip('\n').split('\t')
    if len(p) < 3: print('linha ruim:', ln.strip()); falha += 1; continue
    marca, errado, certo = p[0].strip(), p[1], p[2]
    c, _, k = marca.partition('.')
    f = os.path.join(AQUI, 'original', f'{int(c):02d}.txt')
    if f not in arqs: arqs[f] = blocos(f)
    cab, bl = arqs[f]
    if int(c) in (0, 41):
        pars = [i for i, b in enumerate(bl) if not b.startswith('## ') and b != 'Jhs.']
        idx = pars[int(k) - 1] if k and int(k) <= len(pars) else None
    else:
        idx = next((i for i, b in enumerate(bl) if b.startswith(f'[{marca}] ')), None)
    if idx is None: print('marca não achada:', marca); falha += 1; continue
    n = bl[idx].count(errado)
    if n != 1: print(f'{marca}: «{errado}» aparece {n} vezes'); falha += 1; continue
    bl[idx] = bl[idx].replace(errado, certo); ok += 1
if apl:
    for f, (cab, bl) in arqs.items():
        open(f, 'w', encoding='utf-8').write(cab + '\n\n' + '\n\n'.join(bl) + '\n')
print(f'{ok} aplicáveis, {falha} com problema' + ('' if apl else ' (nada gravado: use --aplicar)'))
