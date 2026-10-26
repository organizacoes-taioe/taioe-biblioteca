"""Vida de Santo Antão: o grego da PG 26 (Migne, 1857) reconhecido pelo Tesseract nas folhas do
Internet Archive, alinhado ao texto de trabalho; lista as divergências que não são trocas típicas do OCR.
uso: python3 -I antao.py <vida.txt> <pasta-ocr> <saida.json>"""
import sys, os, re, json, difflib, unicodedata, html
VIDA, OCR, SAI = sys.argv[1:4]
def chave(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    t = re.sub(r'[^α-ωϲς]', '', t).replace('ς', 'σ').replace('ϲ', 'σ')
    for a, b in (('χ', 'κ'), ('δ', 'β'), ('γ', 'ν'), ('υ', 'ν'), ('ο', 'σ'), ('θ', 'σ'), ('ε', 'σ'), ('ι', 'ν'), ('λ', 'ν'), ('π', 'ν'), ('τ', 'ν'), ('μ', 'ν'), ('ρ', 'ν')):
        pass
    return t
def leve(t):   # chave com as trocas típicas do Tesseract na PG
    t = chave(t)
    for a, b in (('χ', 'κ'), ('δ', 'β'), ('γ', 'ν'), ('ϐ', 'β')):
        t = t.replace(a, b)
    return t
# texto de trabalho
linhas = open(VIDA, encoding='utf-8').read().split('\n')
corpo = [l for l in linhas if not l.startswith('# ')]
toks = []
for li, l in enumerate(corpo):
    for w in l.split():
        toks.append((li, w))
eh_marca = lambda w: re.fullmatch(r'\[\d+\]|\{PG|26\.\d+\}', w) is not None
idx_t = [i for i, (li, w) in enumerate(toks) if not eh_marca(w) and leve(w)]
kt = [leve(toks[i][1]) for i in idx_t]
# OCR: a coluna grega recortada (antao_colunas.py), linha a linha, com as palavras partidas juntadas
GREGO = re.compile(r'[\u0370-\u03ff\u1f00-\u1fff]')
ocr = []
for arq in sorted(f for f in os.listdir(OCR) if f.endswith('.grego.txt')):
    folha = int(arq[:4]); pend = None
    for ln, linha in enumerate(open(os.path.join(OCR, arq), encoding='utf-8').read().split('\n')):
        ws = [[w, folha, ln, 0] for w in linha.split()]
        while ws and not GREGO.search(ws[0][0]) and len(ws[0][0]) <= 3: ws = ws[1:]
        if not ws: continue
        if pend:
            ws[0][0] = pend + ws[0][0]; pend = None
        if re.search(r'[\u0370-\u03ff\u1f00-\u1fff][-‐­]$', ws[-1][0]):
            pend = ws[-1][0][:-1]; ws = ws[:-1]
        ocr.extend(ws)
ocr = [w for w in ocr if re.search(r'[Ͱ-Ͽἀ-῿]', w[0]) and leve(w[0])]
ko = [leve(w[0]) for w in ocr]
sm = difflib.SequenceMatcher(None, kt, ko, autojunk=False)
iguais = 0; divs = []; faltam = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal': iguais += i2 - i1; continue
    if op == 'insert': continue
    if op == 'delete':
        faltam += i2 - i1
        divs.append({'tipo': 'falta', 'tlg': ' '.join(toks[idx_t[i]][1] for i in range(i1, i2)), 'ocr': '',
            'ctx': ' '.join(toks[idx_t[i]][1] for i in range(max(0, i1 - 5), min(len(idx_t), i2 + 5))),
            'onde': ocr[j1][1:3] if j1 < len(ocr) else None, 'i': [idx_t[i1], idx_t[i2 - 1]]})
        continue
    divs.append({'tipo': 'troca', 'tlg': ' '.join(toks[idx_t[i]][1] for i in range(i1, i2)), 'ocr': ' '.join(ocr[j][0] for j in range(j1, j2)),
        
        'ctx': ' '.join(toks[idx_t[i]][1] for i in range(max(0, i1 - 5), min(len(idx_t), i2 + 5))),
        'onde': ocr[j1][1:3], 'i': [idx_t[i1], idx_t[i2 - 1]]})
print('tokens', len(kt), 'iguais', iguais, 'divergências', len(divs), 'faltam no OCR', faltam)
json.dump(divs, open(SAI, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
