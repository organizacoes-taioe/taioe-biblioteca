"""Dos blocos montados (blocos-<parte>.json) ao arquivo da obra: aplica a conferência (correcoes.tsv), põe os títulos
no lugar das linhas ⟪H:…⟫, divide os parágrafos longos nos fins de frase (cortes-2.json guarda o id da palavra que
abre cada bloco, para a divisão não mudar com as correções) e grava original/inicio.txt e original/carta-ao-pastor.txt.
correcoes.tsv: «folha:idx<TAB>palavra<TAB>forma impressa» (forma vazia tira a palavra; «palavra#2» = a 2ª igual na
linha; forma com pontuação substitui tudo, sem pontuação mantém a de antes) e «folha:idx<TAB>+<TAB>linha que falta»
(entra depois da linha folha:idx). Uso: final.py <pasta original/ da obra>"""
import sys, os, re, json, unicodedata
AQUI = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-2')
NUM = 'Α Β Γ Δ Ε Ϛ Ζ Η Θ Ι ΙΑ ΙΒ ΙΓ ΙΔ ΙΕ'.split()
ROM = 'I II III IV V VI VII VIII IX X XI XII XIII XIV XV'.split()
TIT = {'ep1': 'ΕΠΙΣΤΟΛΗ ΤΟΥ ΑΓΙΟΥ ΙΩΑΝΝΟΥ τοῦ ἡγουμένου τῆς Ῥαϊθοῦ. Πρὸς Ἰωάννην τὸν ἀξιάγαστον τὸν τοῦ Σιναίου ὄρους ἡγούμενον.',
       'resp': '## ΙΩΑΝΝΗΣ ΙΩΑΝΝῌ ΧΑΙΡΕΙΝ.', 'prol1': '## ΠΡΟΛΟΓΟΣ.', 'prol2': '## ΠΡΟΛΟΓΟΣ.',
       'proem': '## ΠΡΟΟΙΜΙΟΝ.'}
for i, n in enumerate(NUM): TIT['k%d' % (i + 1)] = '## ΚΕΦΑΛ. %s΄.' % n
PARTES = {'inicio': ('inicio.txt', 'ΕΠΙΣΤΟΛΑΙ ΚΑΙ ΠΡΟΛΟΓΟΣ', None),
          'pastor': ('carta-ao-pastor.txt', 'ΙΩΑΝΝΟΥ ΣΧΟΛΑΣΤΙΚΟΥ ΠΡΟΣ ΤΟΝ ΠΟΙΜΕΝΑ ΛΟΓΟΣ.', 'ΙΩΑΝΝΟΥ ΣΧΟΛΑΣΤΙΚΟΥ ΠΡΟΣ ΤΟΝ ΠΟΙΜΕΝΑ ΛΟΓΟΣ.')}
ALVO = 45
GLOBAL = {'θαλάττῇ': 'θαλάττῃ', 'Ῥαῖθοῦ': 'Ῥαϊθοῦ', 'Ῥαῖθου': 'Ῥαϊθοῦ', 'ἄνενδεὴς': 'ἀνενδεὴς',
          'πνευματικαι.': 'πνευματικαί.', 'ὥνησας': 'ὤνησας', 'καταμαῤαϊνειν': 'καταμαραίνειν'}
PUN = re.compile(r'^([«“"(\[]*)(.*?)([.,;·:»”"\'’᾽)\]!]*)$')
nfc = lambda s: unicodedata.normalize('NFC', s)
core = lambda w: PUN.match(w).group(2)
CORTES = os.path.join(AQUI, 'cortes-2.json')
cortes = json.load(open(CORTES, encoding='utf-8')) if os.path.exists(CORTES) else {}
corr = []
if os.path.exists(os.path.join(AQUI, 'correcoes.tsv')):
    for l in open(os.path.join(AQUI, 'correcoes.tsv'), encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) >= 2 and re.match(r'^\d+:\d+$', p[0]): corr.append((p[0], nfc(p[1].strip()), nfc(p[2].strip()) if len(p) > 2 else ''))
pasta = sys.argv[1]
for parte, (arq, titulo_cab, primeiro) in PARTES.items():
    linhas = json.load(open(os.path.join(AQUI, 'linhas-%s.json' % parte), encoding='utf-8'))
    lin_de = {}
    for p in linhas:
        for l in p['linhas']:
            for t in l['toks']: lin_de['%d:%d:%d' % (p['folha'], t[2], t[3])] = l.get('id')
    blocos = json.load(open(os.path.join(AQUI, 'blocos-%s.json' % parte), encoding='utf-8'))
    seq = []   # (palavra, tid, bloco)
    for bi, b in enumerate(blocos):
            for w, tid in b['pal']: seq.append([w.strip(), tid, bi])
    # conferência
    nao = []
    for lid, w, novo in corr:
        idx = [k for k, x in enumerate(seq) if x[1] and lin_de.get(x[1]) == lid]
        if not idx: continue
        if w == '-':
            for k in idx: seq[k][0] = ''
            continue
        if w == '+':
            k = idx[-1]
            novas = [[x, 'ins:%s:%d' % (lid, j), seq[k][2]] for j, x in enumerate(novo.split())]
            seq[k + 1:k + 1] = novas; continue
        alvo, n = (w.split('#') + ['1'])[:2]
        acha = [k for k in idx if nfc(core(seq[k][0])) == core(alvo) or nfc(seq[k][0]) == alvo]
        if len(acha) < int(n): nao.append('%s\t%s\t%s' % (lid, w, novo)); continue
        k = acha[int(n) - 1]
        if not novo: seq[k][0] = ''
        elif PUN.match(novo).group(1) or PUN.match(novo).group(3) or ' ' in novo: seq[k][0] = novo
        else:
            a, c, b = PUN.match(seq[k][0]).groups(); seq[k][0] = a + novo + b
    if nao: print(parte, 'correções não achadas:\n  ' + '\n  '.join(nao))
    seq = [x for x in seq if x[0]]
    # parágrafos (blocos de Rader) e títulos
    paras, cur, blo = [], [], None
    for w, tid, bi in seq:
        m = re.match(r'⟪H:(\w+)⟫', w)
        if m:
            if cur: paras.append(cur); cur = []
            paras.append([('SUB', m.group(1))]); blo = bi; continue
        if tid and blo is not None and bi != blo and cur: paras.append(cur); cur = []
        if tid: blo = bi
        cur.append((w, tid))
    if cur: paras.append(cur)
    if parte not in cortes:
        ini = []
        for sq in paras:
            if sq[0][0] == 'SUB': continue
            cont, abre = 0, True
            for k, (p, tid) in enumerate(sq):
                if not tid: continue
                if abre: ini.append(tid); abre = False; cont = 0
                cont += 1
                resto = sum(1 for q in sq[k + 1:] if q[1])
                prox = next((q[0] for q in sq[k + 1:] if q[1]), '')
                if cont >= ALVO and re.search(r'[.;]$', p) and resto >= 15 and prox.lstrip('«“(᾿’\'').strip()[:1].isupper(): abre = True
        cortes[parte] = ini
    ini = set(cortes[parte])
    saida, cur, pend = [], [], []
    for sq in paras:
        if sq[0][0] == 'SUB':
            if cur: saida.append(cur); cur = []
            saida.append(['SUB', sq[0][1]]); continue
        for p, tid in sq:
            if not tid: pend.append(p); continue
            if tid in ini and cur: saida.append(cur); cur = []
            cur.extend(pend); pend = []
            cur.append(p)
    if cur: saida.append(cur + pend)
    out = ['# titulo: ' + titulo_cab,
           '# fonte: Migne, Patrologia Graeca 88 (Paris, 1860), texto de M. Rader (1633); ver LEIAME.md', '']
    if primeiro: out += [primeiro, '']
    cap, k = 0, 0
    for c in saida:
        if c[0] == 'SUB':
            if c[1].startswith('k'): cap = int(c[1][1:]); k = 0
            out += [TIT[c[1]], '']; continue
        texto = ' '.join(c)
        if parte == 'pastor' and cap:
            k += 1; texto = '[%s.%d] %s' % (ROM[cap - 1], k, texto)
        out += [texto, '']
    txt = '\n'.join(out).rstrip() + '\n'
    # limpeza geral: aspas «» do OCR (o impresso não as tem), hífen que sobrou, ano teleia solta, formas certas
    txt = re.sub(r'[«»]', '', txt)
    txt = re.sub(r'(\w)- (\w)', r'\1\2', txt)
    txt = txt.replace(' ·', '·')
    for a, b in GLOBAL.items(): txt = txt.replace(nfc(a), nfc(b))
    open(os.path.join(pasta, arq), 'w', encoding='utf-8').write(txt)
    print(parte, len([c for c in saida if c[0] != 'SUB']), 'blocos', sum(len(c) for c in saida if c[0] != 'SUB'), 'palavras')
json.dump(cortes, open(CORTES, 'w', encoding='utf-8'), ensure_ascii=False)
