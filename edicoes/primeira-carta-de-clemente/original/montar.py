"""Monta os arquivos do grego a partir de grego.txt (c.v<TAB>texto, tirado do XML do First1KGreek) e de
correcoes.tsv (os erros de digitalização). Uso: python3 montar.py <grego.txt> <correcoes.tsv>"""
import os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
PARTES = [('01-corinto', 0, 3, 'A igreja de Corinto, antes e agora'), ('02-ciume', 4, 6, 'O ciúme e os seus males'),
          ('03-arrependimento', 7, 12, 'O arrependimento, a obediência, a fé e a hospitalidade'),
          ('04-humildade', 13, 18, 'A humildade'), ('05-paz', 19, 23, 'A paz e a ordem da criação'),
          ('06-ressurreicao', 24, 28, 'A ressurreição'), ('07-santidade', 29, 36, 'O caminho da santidade'),
          ('08-ordem', 37, 44, 'A ordem na Igreja e a sucessão dos apóstolos'),
          ('09-discordia', 45, 50, 'A discórdia de Corinto e o louvor do amor'),
          ('10-apelo', 51, 58, 'O apelo aos autores da sedição'), ('11-oracao', 59, 61, 'A grande oração'),
          ('12-conclusao', 62, 65, 'Conclusão')]
vs = {}
for l in open(sys.argv[1], encoding='utf-8').read().strip().split('\n'):
    r, t = l.split('\t'); vs[r] = t
n = 0
for l in open(sys.argv[2], encoding='utf-8').read().strip().split('\n'):
    c = l.split('\t')
    if len(c) < 3 or c[0] not in vs: continue
    assert vs[c[0]].count(c[1]) == 1, l
    vs[c[0]] = vs[c[0]].replace(c[1], c[2]); n += 1
SUB = 'Ἐπιστολὴ τῶν Ῥωμαίων πρὸς τοὺς Κορινθίους.'
assert vs['65.2'].endswith(SUB); vs['65.2'] = vs['65.2'][:-len(SUB)].strip()
caps = {}
for r, t in vs.items():
    c, v = r.split('.'); caps.setdefault(int(c), []).append((int(v), t))
for nome, a, b, tit in PARTES:
    ps = []
    for c in range(a, b + 1):
        if c == 0:
            ps += ['ΚΛΗΜΕΝΤΟΣ ΠΡΟΣ ΚΟΡΙΝΘΙΟΥΣ Α', caps[0][0][1]]
        else:
            ps.append(' '.join(f'[{c}.{v}] {t}' for v, t in sorted(caps[c])))
    if b == 65: ps.append(SUB)
    cab = (f'# titulo: ΚΛΗΜΕΝΤΟΣ ΠΡΟΣ ΚΟΡΙΝΘΙΟΥΣ Α ({tit})\n'
           '# fonte: First1KGreek (Open Greek and Latin), tlg1271.tlg001.1st1K-grc1, https://github.com/OpenGreekAndLatin/First1KGreek (CC BY-SA 4.0)\n'
           '# edicao: Kirsopp Lake, The Apostolic Fathers, vol. 1 (Loeb, Londres e Nova York, 1912), p. 8–121; erros de digitalização corrigidos (ver LEIAME.md)\n'
           '# marcas: «[1.1]» = capítulo.versículo, a numeração usual; a saudação vem sem número; um parágrafo por capítulo\n\n')
    open(os.path.join(AQUI, nome + '.txt'), 'w', encoding='utf-8').write(cab + '\n\n'.join(ps) + '\n')
print(n, 'correções aplicadas')
