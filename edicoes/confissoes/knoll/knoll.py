"""Confissões: o latim de Knöll (CSEL 33, 1896) a partir de três OCRs do Internet Archive,
alinhados ao texto de trabalho (O'Donnell, Latin Library), que dá a divisão e desempata.
uso: python3 -I knoll.py <pasta-original-odonnell> <pasta-ocr> <saida>"""
import sys, re, os, json, difflib, unicodedata
ORIG, OCR, SAIDA = sys.argv[1:4]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
OCRS = ['corpusscriptoru11wiengoog', 'corpusscriptorum0033unse', 'sanctiaureliaugu33augu']

def norm(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if 'a' <= c <= 'z')
    return t.replace('v', 'u').replace('j', 'i')

import hocr
CORPO = {}   # o -> lista de (pagina, bbox) por token, paralela a ocr_toks
def tokens_ocr(o):
    """as palavras do corpo do texto (sem cabeço, aparato nem testemunhos), pelo tamanho da linha no hOCR"""
    toks, meta = [], []
    pend = None
    for pi, (n, bb, ls) in enumerate(hocr.paginas(os.path.join(OCR, o + '.hocr.html'))):
        cheias = [l for l in ls if len(l['w']) >= 5]
        vals = sorted({round(l['xs']) for l in cheias}, reverse=True)
        corpo = None
        for v in vals:
            if sum(1 for l in cheias if abs(l['xs'] - v) <= v * 0.06) >= 3: corpo = v; break
        if corpo is None: continue
        for li, l in enumerate(ls):
            if l['xs'] < corpo * 0.92 or l['xs'] > corpo * 1.12: continue
            ws = [[w[0].strip(), w[1]] for w in l['w'] if w[0].strip()]
            txt = ' '.join(w[0] for w in ws)
            if li <= 1 and re.search(r'AVG|AYG|CONF|LIB|CAP', txt) and len(ws) < 9: continue
            while ws and re.fullmatch(r'[0-9lI|]{1,3}|io|lo|IO|i5|I5|l5', ws[0][0]) and len(ws) > 1: ws = ws[1:]
            while ws and re.fullmatch(r'[0-9l|]{1,3}|io|lo|IO|i5|I5|l5', ws[-1][0]) and len(ws) > 1: ws = ws[:-1]
            if not ws: continue
            if pend:
                ws[0] = [pend[0] + ws[0][0], pend[1]]; pend = None
            if re.search(r'[a-zA-Z][¬\-]$', ws[-1][0]):
                pend = [ws[-1][0][:-1], (pi, ws[-1][1])]; ws = ws[:-1]
            for w in ws:
                toks.append(w[0]); meta.append(w[1] if isinstance(w[1], tuple) and len(w[1]) == 2 and isinstance(w[1][0], int) and isinstance(w[1][1], tuple) else (pi, w[1]))
    CORPO[o] = meta
    return toks

def ler_odonnell(k):
    txt = open(os.path.join(ORIG, f'livro-{k:02d}.txt'), encoding='utf-8').read()
    cab = [l for l in txt.split('\n') if l.startswith('# ')]
    corpo = '\n'.join(l for l in txt.split('\n') if not l.startswith('# ')).strip()
    pars = [p for p in re.split(r'\n\s*\n', corpo) if p.strip()]
    toks = []  # (par, texto)
    for i, p in enumerate(pars):
        for linha_i, linha in enumerate(p.split('\n')):
            for w in linha.split():
                toks.append([i, linha_i, w])
    return cab, pars, toks

def eh_marca(w): return re.fullmatch(r'\[[IVXLC]+\.\d+\]', w) is not None

ocr_toks = {o: tokens_ocr(o) for o in OCRS}
ocr_norm = {o: [norm(t) for t in ocr_toks[o]] for o in OCRS}

def achar(o, seq, ini=0):
    """posição no OCR o onde começa a sequência normalizada seq: a primeira janela de 14 tokens
    que contém ao menos 7 dos 9 primeiros, a partir do primeiro que bate"""
    s = ocr_norm[o]; alvo = seq[:9]; conj = set(alvo)
    for i in range(ini, len(s) - 14):
        if s[i] not in conj: continue
        janela = s[i:i + 14]
        if sum(1 for x in alvo if x in janela) >= 7:
            return i - alvo.index(s[i]) if alvo.index(s[i]) <= i - ini else i
    return None

relatorio = {'variantes': [], 'acrescimos': [], 'duvidas': []}
# decisões da conferência nas imagens (pranchas de revisar.py): índice do item -> ação
ITENS = json.load(open(os.environ['ITENS'], encoding='utf-8')) if os.environ.get('ITENS') else []
DEC = {}
if os.environ.get('DECISOES'):
    for linha in open(os.environ['DECISOES'], encoding='utf-8'):
        linha = linha.strip()
        if not linha: continue
        k, acao = linha.split(' ', 1)
        x = ITENS[int(k)]
        DEC[(x['tipo'], x['livro'], x['i'])] = acao
ORT = [('inm','imm'),('inp','imp'),('inb','imb'),('conl','coll'),('conm','comm'),('conp','comp'),('conb','comb'),('adp','app'),('adt','att'),('adr','arr'),('adl','all'),('adc','acc'),('adf','aff'),('adg','agg'),('ads','ass'),('inr','irr'),('inl','ill'),('conr','corr'),('k','c'),('ae','e'),('quicq','quidq'),('michi','mihi'),('nil','nihil'),('intellig','intelleg'),('y','i'),('ph','f'),('th','t'),('h','')]
def ort(a):
    a = norm(a)
    for x, y in ORT: a = a.replace(x, y)
    return a
os.makedirs(SAIDA, exist_ok=True)
pos = {o: 0 for o in OCRS}
for k in range(1, 14):
    cab, pars, toks = ler_odonnell(k)
    ws = [t for t in toks if not eh_marca(t[2])]
    on = [norm(t[2]) for t in ws]
    on_idx = [i for i, x in enumerate(on) if x]
    chave_ini = [on[i] for i in on_idx[:9]]
    k2 = None
    if k < 13:
        _, _, tn = ler_odonnell(k + 1)
        nn = [norm(t[2]) for t in tn if not eh_marca(t[2])]
        chave_fim = [x for x in nn if x][:9]
    posicoes = {}
    leitura = {}   # o -> lista, por índice de ws: (forma ocr ou None)
    insercoes = {}  # o -> {indice_antes: [tokens]}
    for o in OCRS:
        if k == 1: pos[o] = achar(o, chave_ini, 0)
        a = pos[o]; b = min(len(ocr_norm[o]), a + int(len(ws) * 2.3) + 800)
        seg_t = ocr_toks[o][a:b]; seg_n = ocr_norm[o][a:b]
        # só os tokens com letras
        idx = [i for i, x in enumerate(seg_n) if x]
        sn = [seg_n[i] for i in idx]
        sm = difflib.SequenceMatcher(None, [on[i] for i in on_idx], sn, autojunk=False)
        lt = [None] * len(ws); ins = {}; lp = [None] * len(ws)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
                for d in range(i2 - i1):
                    lt[on_idx[i1 + d]] = seg_t[idx[j1 + d]]
                    lp[on_idx[i1 + d]] = CORPO[o][a + idx[j1 + d]]
            elif op == 'replace':
                lt[on_idx[i1]] = ('SEG', [seg_t[idx[j]] for j in range(j1, j2)], i2 - i1)
                lp[on_idx[i1]] = CORPO[o][a + idx[j1]]
            elif op == 'insert':
                ins[on_idx[i1 - 1] if i1 > 0 else -1] = [seg_t[idx[j]] for j in range(j1, j2)]
        leitura[o] = lt; insercoes[o] = ins; posicoes[o] = lp
        # o fim do livro: o último token alinhado (o resto da janela é do livro seguinte)
        ult = max((j2 for op, i1, i2, j1, j2 in sm.get_opcodes() if op == 'equal' and i2 >= len(on_idx) - 40), default=None)
        if ult is None:
            ult = max(j2 for op, i1, i2, j1, j2 in sm.get_opcodes() if op == 'equal')
        pos[o] = a + idx[ult - 1] + 1
    # votação
    cob = [sum(1 for o in OCRS if leitura.get(o) is not None and leitura[o][i] is not None) for i in range(len(ws))]
    print('  COBERTURA livro', k, {n: cob.count(n) for n in range(4)}, {o: sum(1 for x in (leitura.get(o) or []) if x is not None) for o in OCRS})
    saida_toks = []  # (indice ws, forma)
    def forma_limpa(f):
        return f.strip("'’‘|")
    i = 0
    resultado = [None] * len(ws)
    pulos = set()
    for i, t in enumerate(ws):
        if i in pulos: continue
        od = t[2]
        if not norm(od):
            resultado[i] = od; continue
        cand = []
        for o in OCRS:
            lt = leitura.get(o)
            if lt is None: continue
            x = lt[i]
            if isinstance(x, tuple):
                juntos = ''.join(re.sub(r'[¬\-]$', '', y) for y in x[1])
                if x[2] == 1 and norm(juntos) == norm(od): cand.append(juntos); continue
                cand.append(('SEG', x)); continue
            cand.append(x)
        simples = [c for c in cand if isinstance(c, str)]
        ns = [norm(c) for c in simples]
        if ns.count(norm(od)) >= 1 and (ns.count(norm(od)) >= 2 or len(set(ns)) == len(ns)):
            # o O'Donnell confirmado (ou OCRs discordantes): forma do OCR que bate, para a pontuação de Knöll
            fs = [forma_limpa(c) for c in simples if norm(c) == norm(od)]
            # pontuação por maioria
            melhor = max(set(fs), key=fs.count)
            resultado[i] = melhor if fs.count(melhor) >= 2 or len(fs) == 1 else melhor
            continue
        # maioria de OCRs com outra palavra
        maior = max(set(ns), key=ns.count) if ns else None
        if maior and ns.count(maior) >= 2 and maior != norm(od):
            fs = [forma_limpa(c) for c in simples if norm(c) == maior]
            f = max(set(fs), key=fs.count)
            resultado[i] = f
            relatorio['variantes'].append({'livro': k, 'i': i, 'n': ns.count(maior), 'de': len(ns), 'od': od, 'knoll': f,
                'onde': {o: posicoes[o][i] for o in OCRS if posicoes.get(o) and posicoes[o][i]},
                'ctx': ' '.join(x[2] for x in ws[max(0, i - 6):i + 7])})
            continue
        # sem acordo: fica o O'Donnell; a forma de um OCR, se só muda a grafia; nada, se falta nos três
        resultado[i] = od
        orto = [forma_limpa(c) for c in simples if ort(c) == ort(od)]
        if orto: resultado[i] = orto[0]
        elif not simples and all(c is None for c in cand) and len(cand) == 3: resultado[i] = ''
        perto = {}
        for o in OCRS:
            lp = posicoes.get(o) or []
            for d in (1, -1, 2, -2, 3, -3):
                if 0 <= i + d < len(lp) and lp[i + d]: perto[o] = lp[i + d]; break
        relatorio['duvidas'].append({'livro': k, 'i': i, 'par': t[0], 'od': od, 'ocr': [str(c)[:60] for c in cand], 'perto': perto,
            'onde': {o: posicoes[o][i] for o in OCRS if posicoes.get(o) and posicoes[o][i]},
            'ctx': ' '.join(x[2] for x in ws[max(0, i - 6):i + 7])})
    # acréscimos de Knöll (inserções curtas presentes em 2 OCRs, sem números nem siglas)
    acresc = {}
    for i in range(-1, len(ws)):
        vs = []
        for o in OCRS:
            ins = insercoes.get(o, {}).get(i)
            if ins: vs.append(tuple(ins))
        if len(vs) < 2: continue
        nv = [tuple(norm(x) for x in v) for v in vs]
        maior = max(set(nv), key=nv.count)
        if nv.count(maior) < 2: continue
        v = vs[nv.index(maior)]
        txt = ' '.join(v)
        if len(v) > 40 or re.search(r'[0-9\]]|\b[A-Z]{1,3}\b|\bom\.|\badd\.|\bcorr\.|\bm\. ?2', txt): 
            if len(v) <= 40: relatorio['duvidas'].append({'livro': k, 'insercao_rejeitada': txt, 'depois_de': ws[i][2] if i >= 0 else '^'})
            continue
        if all(len(x) < 2 and x not in ('a', 'e', 'o') for x in maior): continue
        if all(re.fullmatch(r'[IVXLCl1]+\.?|io|lo|[0-9]+', y) for y in v): continue
        acresc[i] = [forma_limpa(x) for x in v]
        perto = {o: posicoes[o][i] for o in OCRS if posicoes.get(o) and i >= 0 and posicoes[o][i]}
        relatorio['acrescimos'].append({'livro': k, 'i': i, 'perto': perto, 'n': nv.count(maior), 'depois_de': ' '.join(x[2] for x in ws[max(0, i - 5):i + 1]), 'knoll': txt})
    # as decisões da conferência
    for (tipo, lv, i), acao in DEC.items():
        if lv != k: continue
        if tipo == 'A':
            if acao == 'O': acresc.pop(i, None)
            continue
        if acao == 'O': resultado[i] = ws[i][2]
        elif acao == 'K': pass
        elif acao.startswith('='):
            m = re.fullmatch(r'=(.+?)(?: /(\d+))?', acao)
            resultado[i] = m.group(1)
            for d in range(1, int(m.group(2) or 1)): resultado[i + d] = ''
    # remonta os parágrafos com as marcas do texto de trabalho
    por_par = {}
    j = 0
    for t in toks:
        lst = por_par.setdefault((t[0], t[1]), [])
        if eh_marca(t[2]): lst.append(t[2]); continue
        lst.append(resultado[j])
        if j in acresc: lst.extend(acresc[j])
        j += 1
    out = []
    for pi, p in enumerate(pars):
        linhas = []
        for li in range(len(p.split('\n'))):
            linhas.append(' '.join(x for x in por_par.get((pi, li), []) if x))
        out.append('\n'.join(linhas))
    with open(os.path.join(SAIDA, f'livro-{k:02d}.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(cab) + '\n\n' + '\n\n'.join(out) + '\n')
    print('livro', k, 'tokens', len(ws), 'variantes', sum(1 for v in relatorio['variantes'] if v['livro'] == k),
          'acréscimos', sum(1 for v in relatorio['acrescimos'] if v['livro'] == k),
          'dúvidas', sum(1 for v in relatorio['duvidas'] if v['livro'] == k))
json.dump(relatorio, open(os.path.join(SAIDA, 'relatorio.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
