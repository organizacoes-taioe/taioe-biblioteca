"""Aplica ao texto de 1917 (original/*.txt, já divididos) as mudanças da 5ª ed. (1920).
Uso: aplicar1920.py <pasta original> (grava no lugar; rodar sobre a saída do montar_g.py)"""
import re, sys, os
R = '/home/geremias/.cache/claude-pedidos-0511/teoria-da-relatividade/'
P = sys.argv[1]
def ocr(f):
    t = open(R + 'dl/' + f, encoding='utf-8').read()
    t = re.sub(r'Digitized\s+by\s+(Google)?', ' ', t)
    t = re.sub(r'(?m)^\s*[-—–]\s*\d+\s*[-—–].*$', ' ', t)
    t = re.sub(r'-\s*\n\s*', '', t); return re.sub(r'\s+', ' ', t)
A, B = ocr('berdiespezielle00unkngoog.txt'), ocr('bub_gb_kTdWAAAAMAAJ.txt')
def nota(src, ini, fim, fixes=()):
    t = src[src.index(ini):]; t = t[:t.index(fim) + len(fim)]
    for v, n in fixes:
        assert v in t, (ini, v); t = t.replace(v, n)
    return t.strip()
NOTAS = [  # (arquivo, âncora no texto, nota)
 ('parte-1.txt', 'bezeichnet wird', nota(B, 'Eine einfache Ableitung', 'gegeben.')),
 ('parte-1.txt', 'dunkel ist', nota(B, 'Die allgemeine Relativitätstheorie legt', 'werden.')),
 ('parte-1.txt', 'geometrischen Raumes', nota(B, 'Vgl. die etwas', 'Anhang.')),
 ('parte-2.txt', 'erhoffen dürfen', nota(B, 'Die Existenz der', 'Crommelin.', [('jrde', 'wurde'), ('rch zwei', 'durch zwei'), ('der itung', 'der Leitung')])),
 ('parte-2.txt', 'größere Zahl', nota(B, 'Bei der ganzen Betrachtung', 'Gravitationsfeld).', [
   ('Galilei sehe (nicht >tierende) System K', 'Galileische (nicht rotierende) System _K_'), ('relativ j K', 'relativ zu _K_'),
   ('ankommen werden', 'angenommen werden'), ('relativ zu K herrscht', 'relativ zu _K′_ herrscht')])),
 ('parte-2.txt', 'Wahl des Bezugskörpers unabhängig ist', nota(B, 'Vgl. Anhang. Die dort', 'Differenzen).', [('(IIa)', '(11a)')])),
]
SUBST = [  # (arquivo, início e fim do trecho de 1917, trecho novo tirado do OCR de 1920)
 ('parte-2.txt', 'Weise zu numerieren.', 'als „zeitliche“ unterscheiden kann.',
  nota(B, 'Weise numerieren.', 'auffassen müßte.', [('Weise numerieren', 'Weise zu numerieren'), ('nicht einmal derartige', 'nicht einmal eine derartige'),
   ('xly x2, x3', '_x₁_, _x₂_, _x₃_'), ('„räumliche" Kod dinaten, x4 als „zeitliche"', '„räumliche“ Koordinaten, _x₄_ als „zeitliche“')])),
 ('parte-2.txt', 'Außerdem haben aus der Theorie', 'Bestätigung finden werden.',
  nota(B, 'Außerdem hat aus der Theorie', 'finden wird.', [('(d. h.', '(d. h.')])),
]
TROCAS = [l.split('\t') for l in open(R + 'fix-g.tsv', encoding='utf-8').read().split('\n') if l.strip() and not l.startswith('#')]
for arq in ('prefacio.txt', 'parte-1.txt', 'parte-2.txt'):
    t = open(os.path.join(P, arq), encoding='utf-8').read()
    for a, v, n in [x for x in TROCAS if x[0] == arq]:
        if v not in t: print('NÃO ACHEI', arq, v[:40]); continue
        t = t.replace(v, n.replace('¶', '\n\n'), 1)
    for f, ini, fim, novo in SUBST:
        if f != arq: continue
        i = t.find(ini); j = t.find(fim, i)
        if i < 0 or j < 0: print('SUBST?', ini); continue
        t = t[:i] + novo + t[j + len(fim):]
    for k, (f, anc, txt) in enumerate(NOTAS):
        if f != arq: continue
        i = t.find(anc)
        if i < 0: print('ÂNCORA?', anc); continue
        j = i + len(anc)
        t = t[:j] + f'[n{k}]' + t[j:]
        fimp = t.find('\n\n', j)
        fimp = len(t) if fimp < 0 else fimp
        t = t[:fimp] + f'\n\n¤ [n{k}] {txt}' + t[fimp:]
    open(os.path.join(P, arq), 'w', encoding='utf-8').write(t)
print('ok')
