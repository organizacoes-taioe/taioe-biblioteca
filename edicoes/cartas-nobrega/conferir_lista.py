"""Lista as linhas de 1886/ a conferir nas imagens: palavra fora do léxico, troca por esqueleto que não é só
grafia sistemática (ph, th, ll, y, acento…) e dúvida do voto sem solução. Grava relatorios/conferir.json
({página: [{k, linha, motivos}]}) e prepara as imagens ver/<p>.png (texto escuro em fundo claro, recortado).

  python3 -I edicoes/cartas-nobrega/conferir_lista.py
"""
import collections
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.argv = sys.argv[:1]
import montar  # noqa: E402  (carrega o léxico)
import cartas  # noqa: E402
import decisoes as D  # noqa: E402
G = montar.G
PASTA = os.path.expanduser('~/.cache/claude-pedidos-0511/cartas-nobrega')


def sa(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()


def sistematico(a, b):
    """a (1886) → b (hoje) só por grafia regular?"""
    x, y = sa(a), sa(b)
    for rx, sub in ((r'ph', 'f'), (r'th', 't'), (r'chr', 'cr'), (r'y', 'i'), (r'([bcdfglmnprst])\1', r'\1'), (r'ct', 't'),
                    (r'pt', 't'), (r'z', 's'), (r'ç', 'c'), (r'sc(?=[ei])', 's'), (r'^h', '')):
        x = re.sub(rx, sub, x)
        y = re.sub(rx, sub, y)
    return x == y


def main():
    dup = json.load(open(os.path.join(AQUI, 'relatorios', 'duvidas.json'))) if os.path.exists(os.path.join(AQUI, 'relatorios', 'duvidas.json')) else {}
    duv = collections.defaultdict(list)
    for l in open(os.path.join(AQUI, 'relatorios', 'duvidas.tsv'), encoding='utf-8'):
        p, k, c, e = l.rstrip('\n').split('\t')
        duv[(int(p), int(k))].append(c)
    out = collections.defaultdict(list)
    n = 0
    for c in cartas.CARTAS:
        for p, k, l in montar.linhas_carta(c):
            motivos = []
            for t in montar.tokens(l):
                if not re.match(r'[A-Za-zÀ-ÿ]', t):
                    continue
                t0 = t.rstrip('.')
                lw = t0.lower()
                if lw in D.MANUAL or t0 in D.MANUAL_EXATO or lw in ('á', 'ás') or len(t0) > 1 and '-' in t0 and False:
                    continue
                novo, fonte = G.atual(t0)
                if fonte == 'SEM_PAR':
                    motivos.append(t0)
                elif fonte == 'esqueleto' and not sistematico(t0, novo):
                    motivos.append(f'{t0}→{novo}')
            if (p, k) in duv:
                motivos += ['dúvida: ' + x for x in duv[(p, k)]]
            if motivos:
                out[p].append({'k': k, 'linha': re.sub(r'^¶ ', '', l), 'motivos': motivos})
                n += 1
    json.dump(out, open(os.path.join(AQUI, 'relatorios', 'conferir.json'), 'w'), ensure_ascii=False, indent=1)
    print('páginas:', len(out), 'linhas:', n, 'motivos:', sum(len(x['motivos']) for v in out.values() for x in v))


main()
