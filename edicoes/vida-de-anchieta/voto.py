"""Vida de Anchieta — voto das três leituras do OCR (ver ocr.py), página a página.

  python3 edicoes/vida-de-anchieta/voto.py [PASTA]

Leituras: A = tess/<n>.tsv (Tesseract 300 dpi, psm 4: dá as linhas e o recuo), B = tess2/<n>.txt
(Tesseract 400 dpi limiarizado, psm 6), C = pdf/<n>.txt (camada de texto do PDF, que põe acentos
modernos: só vota na palavra sem acento). Grava voto/<p>.txt (p = página impressa), uma linha por
linha impressa, com «¶» no começo de parágrafo e ⟦a|b|c⟧ onde não houve maioria. Esse texto é o
ponto de partida da conferência nas imagens (o resultado conferido fica em 1897/).
"""
import difflib
import os
import re
import sys
import unicodedata

PASTA = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/.cache/claude-pedidos-0511/vida-de-anchieta')
PAGINAS = range(7, 54)
LIXO = '“”"\'`´*^|[]{}_~»«°•■□¦‘’…©®'
PALAVRA = re.compile(r"[A-Za-zÀ-ÿ0-9ºª]+(?:[-'][A-Za-zÀ-ÿ0-9ºª]+)*\.?")


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
                p = re.sub(r'[^,;:.!?()]', '', t)
                if out and p:
                    out[-1][2] += p
                continue
            pal = w.group(0)
            resto = re.sub(r'[^,;:.!?()]', '', t[w.end():])
            ab = re.sub(r'[^(]', '', t[:w.start()])
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
    atual = None
    for l in open(os.path.join(PASTA, 'tess', f'{n}.tsv'), encoding='utf-8').read().splitlines()[1:]:
        c = l.split('\t')
        if len(c) < 12 or c[0] != '5' or not c[11].strip():
            continue
        chave = (c[2], c[3], c[4])
        if chave != atual:
            atual = chave
            linhas.append([])
            recuos.append(int(c[6]))
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
    a, b, c = tokens(la), tokens(ler('tess2', n)), tokens(ler('pdf', n))
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
            pal = next(x for x in cands[:2] if sem_acento(x) == melhor) if sem_acento(w) == melhor or (tb and sem_acento(tb[1]) == melhor) else cands[2]
            if tb and sem_acento(w) == sem_acento(tb[1]) and w != tb[1]:
                pal = '⟦' + w + '|' + tb[1] + '⟧'
                duvidas += 1
        else:
            pal = '⟦' + '|'.join(cands) + '⟧'
            duvidas += 1
        ps = [p] + [t[2] for t in (tb, tc) if t]
        pont = max(set(ps), key=ps.count) if len(ps) >= 2 and ps.count(max(set(ps), key=ps.count)) >= 2 else p
        if len(set(ps)) > 1 and ps.count(pont) < 2:
            pont = pont + '⟨' + '/'.join(x or '∅' for x in ps) + '⟩'
        saida.setdefault(k, []).append(pal + pont)
    linhas = []
    for k in range(len(la)):
        if k not in saida:
            continue
        ini = '¶ ' if recuos[k] > margem + 60 else ''
        linhas.append(ini + ' '.join(saida[k]))
    return linhas, duvidas


if __name__ == '__main__':
    os.makedirs(os.path.join(PASTA, 'voto'), exist_ok=True)
    total = 0
    for n in PAGINAS:
        linhas, d = pagina(n)
        total += d
        open(os.path.join(PASTA, 'voto', f'{n - 4:02d}.txt'), 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
    print('dúvidas:', total)
