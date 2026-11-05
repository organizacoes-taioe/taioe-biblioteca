"""Poesias Completas (Machado de Assis, 1901): rascunho de cada poema para a conferência nas imagens.

    python3 edicoes/poesias-completas-machado/rascunho.py [id ...]     (na raiz do repositório)

Testemunhos (fora do git, em ~/.cache/claude-pedidos-0511/poesias-completas-machado/, ver FALTA.md):
  tess/NNN.txt   OCR Tesseract (por, 300 dpi) de cada página do fac-símile de 1901 (Commons, Google I7oQAAAAIAAJ);
  ws/NNN.txt     Wikisource, páginas do mesmo PDF de 1901 (só as Ocidentais estão transcritas);
  ws-Chrysalidas, ws-Phalenas, ws-Americanas: Wikisource, as primeiras edições (1864, 1870, 1875), revistas.
Para cada poema de poemas.json, alinha palavra a palavra o OCR de 1901 com a transcrição do Wikisource e grava
em rascunho/<id>.txt o texto do Wikisource com as divergências marcadas:
  ⟦ws‖ocr⟧   a palavra (ou o sinal) difere: vale o que estiver na imagem de 1901;
  ⟦+ ...⟧    só o OCR de 1901 tem (verso acrescentado, título, epígrafe, ou sujeira do OCR);
  ⟦- ...⟧    só o Wikisource tem (verso cortado em 1901, ou perda do OCR).
As diferenças só de grafia (chave() de ferramentas/edicao/grafia.py) não se marcam: fica a forma do Wikisource.
"""
import json, os, re, sys
from difflib import SequenceMatcher

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao.grafia import chave  # noqa: E402

B = os.path.expanduser('~/.cache/claude-pedidos-0511/poesias-completas-machado')
WSDIR = {'Chrysalidas': 'ws-Chrysalidas', 'Phalenas': 'ws-Phalenas', 'Americanas': 'ws-Americanas', '1901': 'ws'}
TOK = re.compile(r"\.{2,}|[^\W_]+(?:['’′\-][^\W_]+)*|[—–]|_|[^\w\s]", re.U)
LIVROS = ['CHRYSALIDAS', 'PHALENAS', 'AMERICANAS', 'OCCIDENTAES', 'NOTAS']


def ws_pagina(t):
    t = re.sub(r'<noinclude>.*?</noinclude>', '\n', t, flags=re.S)
    t = re.sub(r'<ref[^>]*>.*?</ref>', '', t, flags=re.S)
    t = re.sub(r'<section[^>]*/>', '', t)
    t = re.sub(r'</?poem[^>]*>', '\n', t)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'</?(big|small|div|span|center)[^>]*>', '', t)
    t = re.sub(r"'''", '', t)
    t = re.sub(r"''", '_', t)
    t = re.sub(r'\[\[[^\]|]*\|([^\]]*)\]\]', r'\1', t)
    t = re.sub(r'\[\[([^\]]*)\]\]', r'\1', t)
    t = re.sub(r'\{\{NOP\}\}|\{\{linha horizontal[^}]*\}\}|\{\{Iwpage[^}]*\}\}', '', t)
    for _ in range(4):   # moldes simples: fica o último parâmetro
        t = re.sub(r'\{\{(?:sc|c|d|direita|t2|t3|x-larger|xx-larger|smaller|larger|esquerda|recuo|Mais|menor|maior)\|([^{}]*)\}\}',
                   lambda m: m.group(1).split('|')[0], t)
    t = re.sub(r'\{\{[^{}]*\}\}', '', t)
    t = re.sub(r'(?m)^[: \t]+', '', t)
    return t


def ws_texto(fonte, a, b):
    out = []
    for n in range(a, b + 1):
        f = os.path.join(B, WSDIR[fonte], '%03d.txt' % n)
        if os.path.exists(f):
            out.append(ws_pagina(open(f, encoding='utf-8').read()))
    t = '\n'.join(out)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()


def parece_cabeco(l):
    s = re.sub(r'[^A-Z]', '', l.upper())
    if not s:
        return len(l) <= 6
    if len(s) <= 3 and len(l) <= 6:
        return True
    return any(SequenceMatcher(None, s, x).ratio() > 0.6 for x in LIVROS)


def tess_texto(a, b):
    pags = []
    for n in range(a, b + 1):
        ls = open(os.path.join(B, 'tess', '%03d.txt' % n), encoding='utf-8').read().split('\n')
        ls = [l.rstrip() for l in ls]
        # cabeço: a primeira linha não vazia, se é o nome do livro e/ou o número da página
        vistos = 0
        for i, l in enumerate(ls):
            if l.strip():
                if parece_cabeco(l.strip()):
                    ls[i] = ''
                vistos += 1
                if vistos == 2:
                    break
        ls = [l for l in ls if not re.search(r'Digitized|Google|Goog', l)]
        pags.append('\n'.join(ls).strip())
    return '\n\n'.join(pags).strip()


def toks(t):
    """Tokens com a linha de origem: (token, nº da linha)."""
    out = []
    for k, l in enumerate(t.split('\n')):
        for w in TOK.findall(l):
            out.append((w, k))
    return out


def norm(w):
    w = w.replace('’', "'").replace('′', "'")
    if re.match(r'\w', w):
        return chave(w)
    return {'«': '"', '»': '"', '“': '"', '”': '"', '–': '—', '-': '—', '…': '...'}.get(w, w)


def rascunho(p):
    ocr = tess_texto(*p['pdf'])
    ws = ws_texto(p['ws'], *p['ws_pag']) if p['ws'] else ''
    if not ws:
        return ocr, 0
    O, W = toks(ocr), toks(ws)
    a = [norm(w) for w, _ in W]
    b = [norm(w) for w, _ in O]
    sm = SequenceMatcher(None, a, b, autojunk=False)
    ops = sm.get_opcodes()
    # o Wikisource pode ter o fim do poema anterior ou o começo do seguinte (página partilhada)
    blocos = [m for m in sm.get_matching_blocks() if m.size >= 4]
    w0 = blocos[0].a if blocos else 0
    w1 = blocos[-1].a + blocos[-1].size if blocos else len(a)
    linhas = {}   # nº da linha do Wikisource -> lista de pedaços
    marcas = 0
    extra = {}    # linhas extras do OCR, penduradas antes da linha k do Wikisource
    ultima_k = 0
    for op, i1, i2, j1, j2 in ops:
        if op == 'equal':
            for i in range(i1, i2):
                linhas.setdefault(W[i][1], []).append(W[i][0]); ultima_k = W[i][1]
            continue
        wsp = [W[i] for i in range(i1, i2) if w0 <= i < w1]
        ocp = [O[j][0] for j in range(j1, j2)]
        if not wsp and not ocp:
            continue
        if i2 <= w0 or i1 >= w1:
            if ocp:
                k = W[w0][1] if i2 <= w0 else ultima_k
                extra.setdefault(k if i2 <= w0 else k + 0.5, []).append('⟦+ ' + ' '.join(ocp) + '⟧')
                marcas += 1
            continue
        marcas += 1
        if wsp and ocp:
            ks = sorted({k for _, k in wsp})
            texto = '⟦' + ' '.join(w for w, _ in wsp) + '‖' + ' '.join(ocp) + '⟧'
            linhas.setdefault(ks[0], []).append(texto)
            for k in ks[1:]:
                linhas.setdefault(k, [])
            ultima_k = ks[-1]
        elif wsp:
            por = {}
            for w, k in wsp:
                por.setdefault(k, []).append(w)
            for k, ws_ in por.items():
                linhas.setdefault(k, []).append('⟦- ' + ' '.join(ws_) + '⟧')
            ultima_k = max(por)
        else:
            k = W[i1][1] if i1 < len(W) else ultima_k
            linhas.setdefault(k, []).append('⟦+ ' + ' '.join(ocp) + '⟧')
    out = []
    wsl = ws.split('\n')
    for k in range(len(wsl)):
        if k in extra:
            out.append(' '.join(extra[k]))
        if k in linhas:
            out.append(juntar(linhas[k]))
        elif not wsl[k].strip():
            out.append('')
        if k + 0.5 in extra:
            out.append(' '.join(extra[k + 0.5]))
    t = re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip()
    return t, marcas


def juntar(ps):
    s = ' '.join(ps)
    s = re.sub(r' ([,.;:!?)»”])', r'\1', s)
    s = re.sub(r'([(«“]) ', r'\1', s)
    s = re.sub(r"_ (.*?) _", r'_\1_', s)
    return s


if __name__ == '__main__':
    P = json.load(open(os.path.join(AQUI, 'poemas.json'), encoding='utf-8'))
    so = set(sys.argv[1:])
    os.makedirs(os.path.join(AQUI, 'rascunho'), exist_ok=True)
    total = 0
    for p in P:
        if so and p['id'] not in so:
            continue
        t, m = rascunho(p)
        total += m
        open(os.path.join(AQUI, 'rascunho', p['id'] + '.txt'), 'w', encoding='utf-8').write(
            '# %s (pdf %d–%d; Wikisource: %s %s)\n\n%s\n' % (p['titulo'], p['pdf'][0], p['pdf'][1], p['ws'], p['ws_pag'], t))
        print('%-36s %4d marcas' % (p['id'], m))
    print('total', total)
