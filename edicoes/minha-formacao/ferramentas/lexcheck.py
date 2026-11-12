import re, sys, collections
sys.path.insert(0, '/home/geremias/.cache/claude-wt5-minha-formacao/edicoes/sao-bernardo')
sys.path.insert(0, '/home/geremias/.cache/claude-wt5-minha-formacao/ferramentas')
import grafia1990
from edicao.grafia import chave
lex = grafia1990.lexico()
t = open('/home/geremias/.cache/claude-wt5-minha-formacao/ferramentas/cache/minha-formacao/relatorios/texto.txt', encoding='utf-8').read()
c = collections.Counter()
for w in re.findall(r'[^\W\d_]+(?:[-’\'][^\W\d_]+)*', t):
    partes = re.split(r'[-’\']', w)
    if any(p.lower() not in lex and p not in lex for p in partes if p and len(p) > 1):
        c[w] += 1
print(len(c))
print(' '.join(f'{w}:{n}' for w, n in sorted(c.items())))
