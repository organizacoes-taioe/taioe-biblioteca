"""Extrai um trecho do OCR (linhas a..b), limpa e junta num fluxo; aplica correções de um arquivo TSV
(antigo<TAB>novo, uma por linha; «¶» no novo = quebra de parágrafo). Uso: ocr.py <ocr> a b <fix.tsv> <saida>"""
import re, sys
arq, a, b, fix, saida = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
ls = open(arq, encoding='utf-8').read().split('\n')[a - 1:b]
out = []
for l in ls:
    l = re.sub(r'\s+', ' ', l).strip()
    if not l or re.fullmatch(r'(Digitized by|Google|Digitized by Google|[-—–•■!\'. ]*\d*[-—–•■!\'. ]*)', l):
        continue
    out.append(l)
t = ''
for l in out:
    if t.endswith('-') and not t.endswith(' -'):
        t = t[:-1] + l
    else:
        t += (' ' if t else '') + l
for linha in open(fix, encoding='utf-8').read().split('\n'):
    if not linha.strip() or linha.startswith('#'):
        continue
    if linha.startswith('RE\t'):
        _, v, n = linha.split('\t')
        t2 = re.sub(v, lambda m: n.replace('¶', '\n\n'), t, count=1, flags=re.S)
        if t2 == t: print('RE NÃO ACHOU:', v[:50], file=sys.stderr)
        t = t2; continue
    v, n = linha.split('\t')
    if v not in t:
        print('NÃO ACHEI:', v[:40], file=sys.stderr)
    t = t.replace(v, n.replace('¶', '\n\n'))
for m in list(re.finditer(r'⟦NOTA(\w+) (.*?)⟧ ?', t, re.S)):
    k, corpo = m.group(1), m.group(2)
    t = t.replace(m.group(0), '')
    t = t.replace('¤ NOTA' + k, '¤ [' + k.split('_')[-1] + '] ' + corpo.strip())
t = re.sub(r' *\n\n *', '\n\n', t)
t = re.sub(r'„([^„"“]*)"', r'„\1“', t)
open(saida, 'w', encoding='utf-8').write(t.strip() + '\n')
