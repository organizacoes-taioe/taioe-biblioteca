"""Confere tradução × original: blocos, marcas [c.s] e versos por bloco; mesóclise. Uso: conferir.py (na pasta da obra)"""
import re, glob, os, sys
MES = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")
ok = True
for f in sorted(glob.glob('original/livro*.txt')):
    t = os.path.join('traducao', os.path.basename(f))
    if not os.path.exists(t): print('falta', t); continue
    corpo = lambda x: [b for b in re.sub(r'(?m)^#.*\n', '', open(x, encoding='utf-8').read()).strip().split('\n\n')]
    ob, tb = corpo(f), corpo(t)
    erros = []
    if len(ob) != len(tb): erros.append(f'blocos {len(ob)} × {len(tb)}')
    for i, (a, b) in enumerate(zip(ob, tb)):
        if re.findall(r'\[\d+\.\d+\]', a) != re.findall(r'\[\d+\.\d+\]', b): erros.append(f'marcas no bloco {i + 1}')
        if a.count('| ') != b.count('| ') and a.startswith('| '): erros.append(f'versos no bloco {i + 1}')
        if a.count('[') - len(re.findall(r'\[\d+\.\d+\]', a)) != b.count('[') - len(re.findall(r'\[\d+\.\d+\]', b)): erros.append(f'colchetes no bloco {i + 1}')
    if MES.search(open(t, encoding='utf-8').read()): erros.append('mesóclise')
    print(os.path.basename(f), 'ok' if not erros else erros); ok = ok and not erros
sys.exit(0 if ok else 1)
