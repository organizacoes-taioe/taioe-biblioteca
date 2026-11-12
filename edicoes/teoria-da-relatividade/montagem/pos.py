"""Acabamento do alemão: cabeçalhos, marcas [I.n], fórmulas em Unicode."""
import re, sys, os
O = sys.argv[1]
ED = '# edicao: A. Einstein, Über die spezielle und die allgemeine Relativitätstheorie (Gemeinverständlich), 5. Aufl., Braunschweig, Vieweg, 1920; ver LEIAME.md'
TIT = {'prefacio.txt': 'Vorwort', 'parte-1.txt': 'Erster Teil. Über die spezielle Relativitätstheorie',
       'parte-2.txt': 'Zweiter Teil. Über die allgemeine Relativitätstheorie',
       'parte-3.txt': 'Betrachtungen über die Welt als Ganzes', 'apendice.txt': 'Anhang'}
ROM = {'parte-1.txt': 'I', 'parte-2.txt': 'II', 'parte-3.txt': 'III'}
def formula(s):
    s = s.replace('_', '')
    s = re.sub(r'sqrt ?\(', '√(', s)
    s = s.replace('√((1−v²/c²)', '√(1 − v²/c²)')
    s = re.sub(r'(?<=[\w)²])([−+])(?=[\w(])', r' \1 ', s)
    s = s.replace('(t − vx/c² )', '(t − (v/c²) x)').replace('x{(Stabanfang)}', 'x(Stabanfang)').replace('x{(Stabende)}', 'x(Stabende)')
    s = s.replace(' ,', ',')
    s = s.replace('P: u; v P′: u + du, v + dv,', 'P: u, v\n| P′: u + du, v + dv,').replace('2 g₁₂ dx₁ dx₂ ... + g₄₄', '2g₁₂ dx₁ dx₂ + … + g₄₄')
    for v, n in [('mc² + E₀ / √', '(mc² + E₀) / √'), ('(m + E₀ / c²) c²', '(m + E₀/c²) c²'), ('t′ = t − v/c² x / √', 't′ = (t − (v/c²) x) / √'),
                 ('W = v + w (A)', 'W = v + w . . . (A)'), ('W = (v + w) / (1 + vw/c²), (B)', 'W = (v + w) / (1 + vw/c²) . . . (B)'),
                 ('3/8 m v⁴/c² + ...', '(3/8) m v⁴/c² + …'), ('| m v²/2', '| m v²/2')]:
        s = s.replace(v, n)
    return s
for arq, tit in TIT.items():
    p = os.path.join(O, arq)
    t = open(p, encoding='utf-8').read()
    t = re.sub(r'(?m)^# kopf:.*\n*', '', t)
    t = re.sub(r'(?m)^# titulo:.*\n*|^# edicao:.*\n*', '', t)
    bl = [b for b in t.strip().split('\n\n') if b.strip()]
    out = []
    for b in bl:
        if b.startswith(('(Kraft) =', '(Beschleunigung) =', '_ds²_ =', '_dx²_ +')):
            b = '| ' + b
        if b.startswith('| '):
            b = b.replace(') . (', ') · (').replace(') . (', ') · (')
            b = '\n'.join(formula(l) for l in b.split('\n'))
        else:
            b = re.sub(r'sqrt ?\(1 ?− ?v²/c² = 0\)', '√(1 − v²/c²) = 0', b)
            b = re.sub(r'1/sqrt\(1−v²/c²\)', '1/√(1 − v²/c²)', b)
            b = re.sub(r'sqrt ?\(1 ?− ?v²/c²\)', '√(1 − v²/c²)', b)
            b = re.sub(r'sqrt\(−1\)|sqrt\(-1\)', '√−1', b)
            b = b.replace('Lorentz−Transformation', 'Lorentz-Transformation')
            b = re.sub(r' {2,}', ' ', b)
            for v, n in [('Raum-Zeit -Punkte', 'Raum-Zeit-Punkte'), ('X′- Achse', 'X′-Achse'), ('Lorentz- Transformation', 'Lorentz-Transformation'),
                         ('durch. Quadrieren', 'durch Quadrieren'), ('von _x′_ − ct′.', 'von _x′_ − _ct′_.'), ('von _x_ − ct das', 'von _x_ − _ct_ das'), ('Lorentz -Transformation', 'Lorentz-Transformation'), (' X′-Achse', ' _X′_-Achse'), ('imaginäre √−1 · ct einführt', 'imaginäre √−1 · _ct_ einführt')]:
                b = b.replace(v, n)
        m = re.match(r'(\[[IV]+\.\d+\] )?\{FIG: \[Illustration(?:: Fig\. (\d))?\.?\]\}', b)
        if m: b = (m.group(1) or '') + '{fig teoria-da-relatividade/fig-' + {'1': '1-de'}.get(m.group(2), m.group(2) or 'fizeau') + '}'
        out.append(b)
    junto = []
    for b in out:
        if b.startswith('| ') and junto and junto[-1].startswith('| '):
            junto[-1] += '\n' + b
        else:
            junto.append(b)
    out = [b for b in junto if b != '## Vorwort.']
    for i in range(len(out) - 1):
        if re.match(r'\[[IV]+\.\d+\] \{fig', out[i]):
            mk, fg = out[i].split(' ', 1)
            out[i], out[i + 1] = mk + ' ' + out[i + 1], fg
    if arq in ROM:
        for i, b in enumerate(out):
            m = re.match(r'## § (\d+)\.', b)
            if m and out[i + 1].startswith('{fig'):
                out[i + 1], out[i + 2] = out[i + 2], out[i + 1]
            if m and not out[i + 1].startswith('['):
                out[i + 1] = f'[{ROM[arq]}.{m.group(1)}] ' + out[i + 1]
    t = f'# titulo: {tit}\n{ED}\n\n' + '\n\n'.join(out) + '\n'
    open(p, 'w', encoding='utf-8').write(t)
