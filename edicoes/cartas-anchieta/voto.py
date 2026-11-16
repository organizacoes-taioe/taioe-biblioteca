"""Cartas de Anchieta — voto das três leituras do OCR (ver ocr.py), folha a folha (adaptado da Vida de Anchieta).

  python3 edicoes/cartas-anchieta/voto.py [PASTA]

Leituras: A = tess/<f>.tsv (Tesseract 2×, psm 4: dá as linhas, o recuo e as caixas), B = tess2/<f>.txt
(Tesseract 2× limiarizado, psm 6), C = ia/<f>.txt (o OCR do próprio Internet Archive). Grava
voto/<f>.txt (f = folha), uma linha por linha impressa, com «¶» no começo de parágrafo e ⟦a|b|c⟧ onde
não houve maioria, e voto/<f>.json com a caixa (x0, y0, x1, y1, na imagem 2×) de cada linha, para os
recortes da conferência.
"""
import difflib
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pecas  # noqa: E402
import json  # noqa: E402

PASTA = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/.cache/claude-pedidos-0511/cartas-anchieta')
PAGINAS = list(pecas.folhas())
LIXO = '`´*^|[]{}_~»«°•■□¦‘…©®'
PALAVRA = re.compile(r"[A-Za-zÀ-ÿ0-9ºª]+(?:[-'’][A-Za-zÀ-ÿ0-9ºª]+)*\.?|—")


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()


def tokens(linhas):
    """[(linha, palavra, pontuação seguinte)] de uma leitura, com a hifenização do fim da linha desfeita."""
    out = []
    for k, l in enumerate(linhas):
        l = ''.join(ch for ch in l if ch not in LIXO)
        l = re.sub(r'\s+', ' ', l).strip()
        for m in re.finditer(r'(\S+)', l):
            t = m.group(1)
            w = PALAVRA.search(t)
            if not w:
                p = re.sub(r'[^,;:.!?()”]', '', t.replace('"', '”'))
                if out and p:
                    out[-1][2] += p
                continue
            pal = w.group(0)
            resto = re.sub(r'[^,;:.!?()”]', '', t[w.end():].replace('"', '”'))
            ab = re.sub(r'[^(“]', '', t[:w.start()].replace('"', '“'))
            if pal.endswith('.') and len(pal) > 4 and not re.match(r'^[A-Z]', pal):
                pal, resto = pal[:-1], '.' + resto
            if t.endswith('-') or t.endswith('¬'):
                pal += '-'
            out.append([k, ab + pal, resto])
    # hifenização: palavra que acaba em «-» no fim da linha + palavra da linha seguinte
    i = 0
    while i < len(out) - 1:
        k, w, p = out[i]
        if w.endswith('-') and out[i + 1][0] == k + 1:
            out[i] = [k, w.rstrip('-') + out[i + 1][1], out[i + 1][2]]
            del out[i + 1]
        i += 1
    return out


def ler_a(n):
    linhas, recuos, x0s = [], [], []
    global CAIXAS
    CAIXAS = []
    atual = None
    for l in open(os.path.join(PASTA, 'tess', f'{n}.tsv'), encoding='utf-8').read().splitlines()[1:]:
        c = l.split('\t')
        if len(c) < 12 or c[0] != '5' or not c[11].strip():
            continue
        chave = (c[2], c[3], c[4])
        x, y, w, h = int(c[6]), int(c[7]), int(c[8]), int(c[9])
        if chave != atual:
            atual = chave
            linhas.append([])
            recuos.append(x)
            CAIXAS.append([x, y, x + w, y + h])
        cx = CAIXAS[-1]
        cx[0], cx[1], cx[2], cx[3] = min(cx[0], x), min(cx[1], y), max(cx[2], x + w), max(cx[3], y + h)
        linhas[-1].append(c[11])
    return [' '.join(x) for x in linhas], recuos


def ler(pasta, n):
    return [l for l in open(os.path.join(PASTA, pasta, f'{n}.txt'), encoding='utf-8').read().splitlines() if l.strip()]


def alinhar(a, b):
    """índice de a → token de b (ou None)."""
    sa = [sem_acento(t[1]) for t in a]
    sb = [sem_acento(t[1]) for t in b]
    m = {}
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, sa, sb, autojunk=False).get_opcodes():
        if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
            for d in range(i2 - i1):
                m[i1 + d] = b[j1 + d]
    return m


def pagina(n):
    la, recuos = ler_a(n)
    a, b, c = tokens(la), tokens(ler('tess2', n)), tokens(ler('ia', n))
    mb, mc = alinhar(a, b), alinhar(a, c)
    margem = sorted(recuos)[len(recuos) // 4] if recuos else 0
    saida = {}
    duvidas = 0
    for i, (k, w, p) in enumerate(a):
        tb, tc = mb.get(i), mc.get(i)
        cands = [w] + [t[1] for t in (tb, tc) if t]
        # palavra: maioria sem acento; a grafia (acentos) vem das leituras do Tesseract
        chaves = [sem_acento(x) for x in cands]
        melhor = max(set(chaves), key=chaves.count)
        if chaves.count(melhor) >= 2:
            iguais = [x for x in cands if sem_acento(x) == melhor]
            formas = sorted(set(iguais), key=iguais.count, reverse=True)
            if len(formas) > 1 and iguais.count(formas[0]) < 2:
                pal = '⟦' + '|'.join(cands) + '⟧'
                duvidas += 1
            else:
                pal = formas[0]
        else:
            pal = '⟦' + '|'.join(cands) + '⟧'
            duvidas += 1
        ps = [p] + [t[2] for t in (tb, tc) if t]
        pont = max(set(ps), key=ps.count) if len(ps) >= 2 and ps.count(max(set(ps), key=ps.count)) >= 2 else p
        if len(set(ps)) > 1 and ps.count(pont) < 2:
            pont = pont + '⟨' + '/'.join(x or '∅' for x in ps) + '⟩'
        saida.setdefault(k, []).append(pal + pont)
    linhas, caixas = [], []
    for k in range(len(la)):
        if k not in saida:
            continue
        ini = '¶ ' if recuos[k] > margem + 40 else ''
        linhas.append(ini + ' '.join(saida[k]))
        caixas.append(CAIXAS[k])
    return linhas, duvidas, caixas


if __name__ == '__main__':
    os.makedirs(os.path.join(PASTA, 'voto'), exist_ok=True)
    total = 0
    for n in PAGINAS:
        linhas, d, caixas = pagina(n)
        total += d
        open(os.path.join(PASTA, 'voto', f'{n}.txt'), 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
        json.dump(caixas, open(os.path.join(PASTA, 'voto', f'{n}.json'), 'w'))
    print('dúvidas:', total)
