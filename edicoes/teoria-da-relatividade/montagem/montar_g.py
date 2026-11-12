"""Divide o Gutenberg 77850 (1ª ed., 1917) em arquivos por parte, no formato do traducoes.py.
Saída: <saida>/g-<parte>.txt (rascunho; as mudanças de 1920 entram à mão depois)."""
import re, sys
src, saida = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read().split('*** START')[1].split('*** END')[0]
t = t[t.index('Vorwort.'):]
NOMES = {'Galilei', 'Gauß', 'Newton', 'Maxwell', 'Minkowski', 'Boltzmann', 'L. Boltzmann', 'H. A. Lorentz', 'A. Einstein',
         'H. Minkowski', 'M. Laue', 'A. Einstein.', 'Lorentz', 'Fizeau', 'Michelson', 'Morley', 'Zeeman', 'Riemann', 'Euklid',
         'Mach', 'E. Mach', 'Faraday', 'Leverrier', 'Eötvös', 'De Sitter', 'de Sitter', 'Fitzgerald', 'Kaufmann', 'Hertz',
         'Kepler', 'Doppler', 'Faraday-Maxwell', 'FitzGerald', 'Maxwell-Lorentz', 'Zeemann', 'Leverrier', 'Eddington', 'Crommelin', 'Seeliger', 'Weyl', 'H. Weyl'}
def gesp(m):
    x = re.sub(r'\s+', ' ', m.group(1))
    return x if x in NOMES or x.rstrip('.') in NOMES else '_' + x + '_'
# notas: blocos «  [n] texto» (recuados)
notas = {}
def tira_nota(m):
    notas[m.group(1)] = re.sub(r'\+(?=[^\s+])([^+]{1,200}?)(?<=[^\s+])\+', gesp, re.sub(r'\s+', ' ', m.group(2)).strip())
    return '\n'
t = re.sub(r'(?m)^  \[(\d+)\] ((?:.+\n)(?:^ {5,}.+\n)*)', tira_nota, t)
t = re.sub(r'\+(?=[^\s+])([^+]{1,200}?)(?<=[^\s+])\+', gesp, t)
blocos = [b for b in re.split(r'\n\s*\n', t) if b.strip()]
out, cur = {}, None
for b in blocos:
    raw = b
    s = re.sub(r'\s+', ' ', b).strip()
    if s.startswith('[Illustration'):
        out.setdefault(cur, []).append('{FIG: ' + s + '}'); continue
    if s in ('Vorwort.',):
        cur = 'vorwort'; out[cur] = ['## Vorwort.']; continue
    if s in ('Erster Teil.', 'Zweiter Teil.'):
        cur = {'Erster Teil.': 'teil-1', 'Zweiter Teil.': 'teil-2'}[s]; out[cur] = [f'# kopf: {s}']; continue
    if re.match(r'^Über die (spezielle|allgemeine) Relativitätstheorie\.$', s):
        out[cur].append(f'# kopf: {s}'); continue
    m = re.match(r'^§ (\d+)\. (.+)$', s)
    if m and len(s) < 140:
        out[cur].append(f'## § {m.group(1)}. {m.group(2)}'); continue
    if re.match(r'^ {8,}', raw) and len(s) < 120:       # fórmula destacada
        out[cur].append('| ' + s); continue
    out[cur].append(s)
# junta fórmulas consecutivas num bloco só
for k, bl in out.items():
    novo = []
    for b in bl:
        if b.startswith('| ') and novo and novo[-1].startswith('| '):
            novo[-1] += '\n' + b
        else:
            novo.append(b)
    out[k] = novo
import os
os.makedirs(saida, exist_ok=True)
for k, bl in out.items():
    # notas ao fim de cada §: põe cada nota logo antes do próximo título «## »
    res, pend = [], []
    for b in bl:
        if b.startswith('## ') and pend:
            res += [f'¤ [{n}] {notas[n]}' for n in pend]; pend = []
        res.append(b)
        pend += [n for n in re.findall(r'\[(\d+)\]', b) if n in notas and b[:2] != '¤ ']
    res += [f'¤ [{n}] {notas[n]}' for n in pend]
    open(f'{saida}/g-{k}.txt', 'w', encoding='utf-8').write('\n\n'.join(res) + '\n')
    print(k, len(res))
print('notas', len(notas))
