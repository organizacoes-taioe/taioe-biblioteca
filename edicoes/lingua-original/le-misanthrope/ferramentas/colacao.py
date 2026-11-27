"""Confronta o texto montado (partes/, Louandre 1910) com dois OCRs do Internet Archive: Boully (1899, «texte revu
sur l'éd. de 1667», ortografia moderna) e van Bever (1923, «publiée sur les textes originaux», a grafia de 1667).
Grava as diferenças de palavra num relatório (tsv), com o verso, para decidir uma a uma.
python3 -I colacao.py <partes/> <boully djvu.txt> <vanbever djvu.txt> <saída.tsv>"""
import difflib, os, re, sys, unicodedata

PAL = re.compile(r"[^\W\d_]+", re.U)


def esqueleto(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(ch for ch in w if not unicodedata.combining(ch))
    w = w.replace('œ', 'oe').replace('æ', 'ae')
    # grafia antiga → moderna, por alto
    w = re.sub(r'oy', 'oi', w).replace('y', 'i')
    w = re.sub(r'oi(s|t|ent)$', r'ai\1', w)
    w = re.sub(r'oient$', 'aient', w)
    w = re.sub(r'([aeiou])s([bcdfgjlmnpqtv])', r'\1\2', w)   # estre → etre, mesme → meme
    w = w.replace('sç', 's').replace('ç', 'c')
    w = re.sub(r'ens$', 'ents', w)   # sermens → serments
    return w


def texto_nosso(pasta):
    toks = []   # (palavra, verso, linha)
    for nome in sorted(os.listdir(pasta), key=lambda s: [int(x) for x in re.findall(r'\d+', s)]):
        n = None
        for l in open(os.path.join(pasta, nome), encoding='utf-8'):
            l = l.rstrip('\n')
            m = re.match(r'::versos (\d+)', l)
            if m:
                n = int(m.group(1)); continue
            if l.startswith('::fala') or l.startswith('::rubrica') or not l.strip():
                continue
            if l.startswith('::prosa'):
                l = l[8:]
            else:
                if not l.startswith(' '):
                    n += 1
            l2 = re.sub(r'\[[^\]]*\]', ' ', l)
            for w in PAL.findall(l2):
                toks.append((w, n, l.strip()))
    return toks


def texto_ocr(arq, i, f):
    linhas = open(arq, encoding='utf-8', errors='replace').read().split('\n')
    toks = []
    for l in linhas[i - 1:f]:
        if re.fullmatch(r'\s*[A-ZÉÈÀÂÎÔÛÇ’\' ,.]+\s*', l):   # nomes de quem fala, títulos
            continue
        for w in PAL.findall(l):
            toks.append((w, l.strip()))
    return toks


nosso = texto_nosso(sys.argv[1])
A = [esqueleto(w) for w, _n, _l in nosso]
saida = []
# as linhas do djvu.txt onde a peça começa e acaba (Boully: 3305–13206; van Bever: 1160–5579)
for rot, arq, ini, fim in (('boully', sys.argv[2], 3305, 13206), ('vanbever', sys.argv[3], 1160, 5579)):
    ocr = texto_ocr(arq, ini, fim)
    B = [esqueleto(w) for w, _l in ocr]
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal':
            continue
        if op == 'insert' and b2 - b1 > 3:
            continue   # notas, cabeçalhos
        if a2 - a1 > 6:
            saida.append('%s\t%s\tGRANDE\t%d palavras nossas sem par' % (rot, nosso[a1][1], a2 - a1)); continue
        nos = ' '.join(w for w, _n, _l in nosso[a1:a2])
        ele = ' '.join(w for w, _l in ocr[b1:b2])
        if op == 'replace' and a2 - a1 == 1 and b2 - b1 == 1 and difflib.SequenceMatcher(None, A[a1], B[b1]).ratio() >= .8:
            continue   # erro de OCR ou grafia
        k = a1 if a1 < len(nosso) else len(nosso) - 1
        ctx = ocr[b1][1] if b1 < len(ocr) else ''
        saida.append('%s\t%s\t%s\t%s → %s\t%s\t||\t%s' % (rot, nosso[k][1], op, nos, ele, nosso[k][2], ctx))
with open(sys.argv[4], 'w', encoding='utf-8') as f:
    f.write('\n'.join(saida) + '\n')
print(len(saida), 'diferenças')
