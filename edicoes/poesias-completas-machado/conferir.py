"""Poesias Completas (1901): pontos de divergência entre o OCR de 1901 e o Wikisource, decididos por regra ou
nas imagens (pranchas de recortes), e o texto de 1901 que sai das decisões.

    python3 edicoes/poesias-completas-machado/conferir.py pontos [id ...]   grava pontos/<id>.json e pranchas/
    python3 edicoes/poesias-completas-machado/conferir.py aplicar [id ...]  grava base/<id>.txt (1901, grafia antiga)

Decisões nas imagens: conferencia.json, {"<id>:<n>": "ws" | "ocr" | "<texto livre>"} (o texto livre substitui
os dois lados; "" apaga). Regras automáticas: ver decidir().
"""
import glob, json, os, re, sys
from difflib import SequenceMatcher

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import rascunho as R  # noqa: E402
from edicao.grafia import mesma_palavra, sem_acento  # noqa: E402

B = R.B
PAG = os.path.join(B, 'pag')
ESCALA = 0.62


def ocr_tokens(a, b):
    """Tokens do OCR de 1901 (TSV do Tesseract), com página e caixa da linha; sem cabeços nem marca do Google."""
    out = []
    for n in range(a, b + 1):
        f = os.path.join(B, 'tess', '%03d.tsv' % n)
        linhas = {}
        for l in open(f, encoding='utf-8').read().split('\n')[1:]:
            c = l.split('\t')
            if len(c) < 12 or c[0] != '5' or not c[11].strip():
                continue
            k = (int(c[2]), int(c[3]), int(c[4]))
            x, y, w, h = map(int, c[6:10])
            linhas.setdefault(k, []).append((c[11], x, y, w, h))
        ordem = sorted(linhas, key=lambda k: min(t[2] for t in linhas[k]))
        vistos = 0
        for k in ordem:
            ws = linhas[k]
            txt = ' '.join(w[0] for w in ws)
            if re.search(r'Digitized|Google|Goog', txt):
                continue
            if vistos < 2:
                vistos += 1
                if R.parece_cabeco(txt):
                    continue
            x0 = min(w[1] for w in ws); y0 = min(w[2] for w in ws)
            x1 = max(w[1] + w[3] for w in ws); y1 = max(w[2] + w[4] for w in ws)
            for w in ws:
                for t in R.TOK.findall(w[0]):
                    out.append({'t': t, 'pag': n, 'linha': (x0, y0, x1, y1), 'cx': (w[1], w[2], w[1] + w[3], w[2] + w[4]), 'txt': txt})
    return out


_LEX = None


def lexico():
    """Palavras conhecidas, grafia antiga e moderna: as transcrições do Wikisource e o dicionário do sistema."""
    global _LEX
    if _LEX is None:
        lex = set()
        for d in ('ws', 'ws-Chrysalidas', 'ws-Phalenas', 'ws-Americanas'):
            for f in glob.glob(os.path.join(B, d, '*.txt')):
                for w in re.findall(r"[^\W\d_]+", open(f, encoding='utf-8').read()):
                    lex.add(w.lower())
        for f in ('/usr/share/dict/brazilian', '/usr/share/dict/portuguese'):
            if os.path.exists(f):
                for w in open(f, encoding='utf-8', errors='ignore'):
                    lex.add(w.strip().lower())
        _LEX = lex
    return _LEX


ROMANO = re.compile(r'^[IVXLC]+\.?$')
CONFUSOES = {'0': 'o', '6': 'ó', '1': 'l', '4': 'á'}


def palavras(s):
    return [w for w in s.split() if re.match(r'[^\W_]', w)]


def decidir(p):
    """Regra automática: 'ws', 'ocr', '' (apagar) ou None (vai para a prancha)."""
    ws, oc = p['ws'], p['ocr']
    lex = lexico()
    if p['tipo'] == 'cab':
        return 'cab'
    if p['tipo'] == '+':
        if not palavras(oc):
            return None if re.search(r'[,.;:!?—]', oc) else ''
        if all(not w.isalpha() or len(w) <= 2 and w.lower() not in ('é', 'e', 'o', 'a', 'ó', 'ai', 'ah', 'oh', 'eu', 'tu', 'se', 'me', 'te', 'lhe', 'no', 'na', 'do', 'da', 'de', 'em', 'um', 'ou', 'os', 'as', 'há', 'ha', 'só', 'já', 'vê', 'lá', 'cá', 'aí') for w in oc.split()):
            return ''   # letras soltas, números de página
        if re.search(r'CHRYS|PHAL|AMERIC|OCCID|NOTAS', oc) and len(palavras(oc)) <= 3:
            return ''
        return None
    if re.fullmatch(r'[IVXLC]+\.?', ws.strip()) and len(palavras(oc)) <= 1 and not re.search(r'[a-z]{2}', oc):
        return 'ws'   # número da estrofe: o OCR não lê os romanos
    m = re.fullmatch(r'([IVXLC]+) (.+)', ws.strip())
    if m and len(oc.split()) == 2 and mesma_palavra(m.group(2), oc.split()[1]):
        return 'ws'
    if re.fullmatch(r'[«»"“”]', ws.strip()) and not palavras(oc) and not re.search(r'[,.;:!?]', oc):
        return 'ws'   # aspas no começo do verso: o OCR as perde
    if re.fullmatch(r'[«»] (\S+)', ws.strip()) and len(oc.split()) == 1 and mesma_palavra(ws.split()[1], oc) :
        return 'ws'
    if p['tipo'] == '-':
        if not palavras(ws) and re.fullmatch(r'[_\s]*', ws):
            return 'ws'   # itálico do Wikisource
        return None
    # troca
    wsw, ocw = palavras(ws), palavras(oc)
    if not wsw and not ocw and re.fullmatch(r"[A-ZÀ-Ý' ,.]+", p.get('ctx_ws', '').strip() or 'x') and len(p['ctx_ws']) < 40:
        return 'ws'   # pontuação do nome de quem fala (CLEON.) ou de um título em caixa alta
    if re.fullmatch(r'[<>/p\s]+', ws) and not ocw:
        return ''
    if len(wsw) == len(ocw) == 1 and len(ws.split()) == len(oc.split()) == 1:
        a, b = wsw[0], ocw[0]
        if mesma_palavra(a, b) or mesma_palavra(re.sub('ão(?=$|-)', 'am', a), b) or mesma_palavra(a, re.sub('ão(?=$|-)', 'am', b)):
            return 'ws'
        if re.search(r'\d', b) and not re.search(r'\d', a):
            bb = ''.join(CONFUSOES.get(ch, ch) for ch in b)
            if sem_acento(bb).lower() == sem_acento(a).lower():
                return 'ws'
            return 'ws' if b.lower() not in lex else None
        if ROMANO.match(a) and not ROMANO.match(b):
            return 'ws'
        if b.lower() not in lex and a.lower() in lex:
            return 'ws'   # o OCR leu uma palavra que não existe
        if sem_acento(a).lower() == sem_acento(b).lower():
            return 'ws'   # só acento: a grafia se resolve depois
    if not wsw and not ocw:
        return None   # pontuação: na imagem
    return None


def pontos(p):
    ws = R.ws_texto(p['ws'], *p['ws_pag'])
    W = R.toks(ws)
    O = ocr_tokens(*p['pdf'])
    a = [R.norm(w) for w, _ in W]
    b = [R.norm(o['t']) for o in O]
    sm = SequenceMatcher(None, a, b, autojunk=False)
    blocos = [m for m in sm.get_matching_blocks() if m.size >= 4]
    w0 = blocos[0].a if blocos else 0
    w1 = blocos[-1].a + blocos[-1].size if blocos else len(a)
    wsl = ws.split('\n')
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        ii = [i for i in range(i1, i2) if w0 <= i < w1]
        if not ii and j1 == j2:
            continue
        if (i2 <= w0 or i1 >= w1) and j1 == j2:
            continue
        tipo = 'x' if ii and j2 > j1 else '-' if ii else '+'
        if tipo == '+' and i2 <= w0:
            tipo = 'cab'
        oc = O[j1:j2]
        # caixa: as linhas do OCR envolvidas, ou a vizinhança
        viz = [O[j] for j in range(max(0, j1 - 1), j2) if j < len(O)] or [O[j] for j in (j1 - 1, j1) if 0 <= j < len(O)]
        if not oc and j1 < len(O):
            viz.append(O[j1])
        pag = viz[0]['pag'] if viz else p['pdf'][0]
        lin = sorted({tuple(o['cx']) for o in viz if o['pag'] == pag}, key=lambda c: c[1])
        kws = sorted({W[i][1] for i in ii}) or ([W[i1][1]] if i1 < len(W) else [])
        out.append({'n': len(out) + 1, 'tipo': tipo, 'i': [i1, i2], 'j': [j1, j2],
                    'ws': ' '.join(W[i][0] for i in ii), 'ocr': ' '.join(o['t'] for o in oc),
                    'pag': pag, 'linhas': lin,
                    'ctx_ws': ' / '.join(wsl[k] for k in kws[:2]) if kws else '',
                    'ctx_ocr': ' / '.join(dict.fromkeys(o['txt'] for o in viz))})
    for q in out:
        q['auto'] = decidir(q)
        # sujeira no pé da página (assinatura do caderno, marca do Google, manchas)
        ys = [O[j]['cx'][1] for j in range(q['j'][0], q['j'][1])]
        if q['auto'] is None and q['tipo'] == '+' and ys and min(ys) > 1850:
            q['auto'] = ''
    return out, W, O, (w0, w1)


def prancha(pid, pts, nome):
    from PIL import Image, ImageDraw, ImageFont
    fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
    tiras = []
    for q in pts:
        im = Image.open(os.path.join(PAG, 'p-%03d.png' % q['pag'])).convert('L')
        if q['linhas']:
            y0 = min(c[1] for c in q['linhas']) - 22; y1 = max(c[3] for c in q['linhas']) + 22
            x = [c[0] for c in q['linhas']] + [c[2] for c in q['linhas']]
        else:
            y0, y1, x = 150, 400, [600]
        y0 = max(0, y0); y1 = min(im.height, max(y1, y0 + 70))
        corte = im.crop((80, y0, im.width - 40, y1))
        d0 = ImageDraw.Draw(corte)
        for c in q['linhas']:   # sublinha o lugar do ponto
            d0.line((c[0] - 80, c[3] - y0 + 4, c[2] - 80, c[3] - y0 + 4), fill=150, width=3)
        corte = corte.resize((int(corte.width * ESCALA), int(corte.height * ESCALA)), Image.LANCZOS)
        rot = '%s:%d  p%d   WS «%s»   OCR «%s»' % (pid, q['n'], q['pag'], q['ws'][:45], q['ocr'][:45])
        rot2 = 'WS: ' + q['ctx_ws'][:95]
        t = Image.new('L', (max(corte.width, 760), corte.height + 42), 255)
        dr = ImageDraw.Draw(t)
        dr.text((4, 2), rot, fill=0, font=fonte); dr.text((4, 21), rot2, fill=90, font=fonte)
        t.paste(corte, (0, 42))
        tiras.append(t)
    larg = max(t.width for t in tiras)
    alt = sum(t.height + 5 for t in tiras)
    folha = Image.new('L', (larg, alt), 200)
    y = 0
    for t in tiras:
        folha.paste(t, (0, y)); y += t.height + 5
    folha.save(nome)


def carregar_decisoes():
    dec = {}
    for f in sorted(glob.glob(os.path.join(AQUI, 'conferencia*.json'))):
        dec.update(json.load(open(f, encoding='utf-8')))
    return dec


if __name__ == '__main__':
    P = json.load(open(os.path.join(AQUI, 'poemas.json'), encoding='utf-8'))
    cmd, so = sys.argv[1], set(sys.argv[2:])
    dec = carregar_decisoes()
    os.makedirs(os.path.join(B, 'pontos'), exist_ok=True)
    os.makedirs(os.path.join(B, 'pranchas'), exist_ok=True)
    tot = {'auto': 0, 'img': 0, 'feito': 0}
    for p in P:
        if not p['ws'] or (so and p['id'] not in so):
            continue
        pts, W, O, lim = pontos(p)
        json.dump(pts, open(os.path.join(B, 'pontos', p['id'] + '.json'), 'w'), ensure_ascii=False, indent=0)
        falta = [q for q in pts if q['auto'] is None and ('%s:%d' % (p['id'], q['n']) not in dec or dec['%s:%d' % (p['id'], q['n'])] == '?')]
        tot['auto'] += sum(q['auto'] is not None for q in pts)
        tot['img'] += len(falta)
        tot['feito'] += sum('%s:%d' % (p['id'], q['n']) in dec for q in pts)
        if cmd == 'pontos':
            for f in glob.glob(os.path.join(B, 'pranchas', p['id'] + '-*.png')):
                os.remove(f)
            for k in range(0, len(falta), 14):
                prancha(p['id'], falta[k:k + 14], os.path.join(B, 'pranchas', '%s-%02d.png' % (p['id'], k // 14 + 1)))
            print('%-34s %4d pontos, %4d automáticos, %4d para as imagens' % (p['id'], len(pts), sum(q['auto'] is not None for q in pts), len(falta)))
    print(tot)


# ------------------------------------------------------------------ aplicar: o texto de 1901 (grafia antiga)

def aplicar(p, dec):
    pts, W, O, (w0, w1) = pontos(p)
    porop = {(q['i'][0], q['j'][0]): q for q in pts}
    wsl = R.ws_texto(p['ws'], *p['ws_pag']).split('\n')
    linhas = {}
    erros, mudancas, duvidas = [], [], []
    a = [R.norm(w) for w, _ in W]
    b = [R.norm(o['t']) for o in O]
    sm = SequenceMatcher(None, a, b, autojunk=False)
    ult = 0

    def por(k, toks):
        linhas.setdefault(k, []).extend(toks)

    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for i in range(i1, i2):
                por(W[i][1], [W[i][0]]); ult = W[i][1]
            continue
        q = porop.get((i1, j1))
        ii = [i for i in range(i1, i2) if w0 <= i < w1]
        ks = sorted({W[i][1] for i in ii}) or [W[i1][1] if i1 < len(W) else ult]
        if q is None:
            continue
        chave = '%s:%d' % (p['id'], q['n'])
        v = dec.get(chave, q['auto'])
        if v == 'cab':
            v = ''
        if v is None or v == '?':
            duvidas.append(chave)
            por(ks[0], ['⟦?%d %s‖%s⟧' % (q['n'], q['ws'], q['ocr'])])
            for k in ks[1:]:
                por(k, [])
            ult = ks[-1]
            continue
        if v in ('ws', 'ws!'):
            for i in ii:
                por(W[i][1], [W[i][0]])
            if v == 'ws!':
                erros.append((chave, q['ocr'], q['ws'], q['ctx_ws']))
        elif v == 'ocr':
            grupos, ant = [], None
            for o in O[j1:j2]:
                if o['linha'] != ant:
                    grupos.append([]); ant = o['linha']
                grupos[-1].append(o['t'])
            for n, g in enumerate(grupos):
                por(ks[n] if n < len(ks) else ks[-1] + 0.01 * (n - len(ks) + 1), g)
            for k in ks:
                por(k, [])
            if palavras(q['ws']) != palavras(q['ocr']):
                mudancas.append((chave, q['ws'], q['ocr'], q['ctx_ws']))
        else:
            txt = v[1:] if v.startswith('!') else v
            if v.startswith('!'):
                erros.append((chave, q['ocr'], txt, q['ctx_ws']))
            elif palavras(q['ws']) != palavras(txt):
                mudancas.append((chave, q['ws'], txt, q['ctx_ws']))
            pedacos = [x.strip() for x in txt.split(' / ')] if txt else []
            for n, ped in enumerate(pedacos):
                por(ks[n] if n < len(ks) else ks[-1] + 0.01 * (n - len(ks) + 1), R.TOK.findall(ped))
            for k in ks:
                por(k, [])
        ult = ks[-1]
    out = []
    for k in sorted(set(range(len(wsl))) | set(linhas)):
        if k in linhas:
            l = R.juntar(linhas[k]) if linhas[k] else ''
            if l:
                if re.match(r'[,.;:!?»]', l) and out and out[-1]:
                    m = re.match(r'([,.;:!?»]+)\s*(.*)', l)
                    out[-1] += m.group(1); l = m.group(2)
                if l:
                    out.append(l)
        elif not wsl[int(k)].strip():
            out.append('')
    t = re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip()
    t = t.replace(' ⟧', '⟧')
    return t, erros, mudancas, duvidas


def comando_aplicar(P, so, dec):
    rel = {}
    os.makedirs(os.path.join(AQUI, 'base'), exist_ok=True)
    for p in P:
        if not p['ws'] or (so and p['id'] not in so):
            continue
        t, er, mu, du = aplicar(p, dec)
        open(os.path.join(AQUI, 'base', p['id'] + '.txt'), 'w', encoding='utf-8').write(t + '\n')
        rel[p['id']] = {'erros': er, 'mudancas': mu, 'duvidas': du}
        print('%-34s %3d erros de 1901, %3d mudanças sobre a 1ª ed., %2d dúvidas' % (p['id'], len(er), len(mu), len(du)))
    json.dump(rel, open(os.path.join(AQUI, 'relatorio-1901.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__' and sys.argv[1] == 'aplicar':
    comando_aplicar(json.load(open(os.path.join(AQUI, 'poemas.json'), encoding='utf-8')), set(sys.argv[2:]), carregar_decisoes())
