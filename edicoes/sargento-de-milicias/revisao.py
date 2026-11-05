"""Memórias de um Sargento de Milícias — a lista dos pontos a conferir nas imagens de 1854–55.

  python3 ferramentas/texto.py sargento-de-milicias          # antes: grava resultado.pkl
  python3 edicoes/sargento-de-milicias/revisao.py [--pranchas] [--de N]

Compara o texto pronto (resultado.pkl, depois das decisões) com o texto moderno do Wikisource, palavra
por palavra (pela chave de grafia), e lista cada lugar em que as palavras diferem além de acentos e
grafia: erro de OCR que sobrou, palavra da moderna que falta ou sobra, ou lição de 1854 que a moderna
mudou. Cada ponto leva o trecho de 1854 (para achar a linha no fac-símile), o nosso texto e o da moderna.
Grava ferramentas/cache/sargento-de-milicias/ver/pontos2.json e, com --pranchas, os recortes em
ver/q-<n>.png (10 por prancha) e ver/q-<n>.txt (o que comparar em cada um). Os pontos já decididos
(conferencia.json, pela chave 'para') não voltam.
"""
import json
import os
import pickle
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
sys.path.insert(0, AQUI)
from edicao.grafia import chave  # noqa: E402
from edicao.tokens import achatar, alinhar, e_palavra, texto as junta  # noqa: E402
import config  # noqa: E402
import decisoes  # noqa: E402

CACHE = os.path.join(AQUI, '..', '..', 'ferramentas', 'cache', 'sargento-de-milicias')


def sem_acento(s):
    s = unicodedata.normalize('NFD', s)
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def k2(w):
    """Chave mais frouxa: sem acentos, sem trema, sem caixa (idéia = ideia; -ão = -am)."""
    k = chave(w) if e_palavra(w) else w
    return re.sub(r'ao\b', 'am', k)


def pontos():
    r = pickle.load(open(os.path.join(CACHE, 'resultado.pkl'), 'rb'))
    out, E = r['out'], r['E']
    _, md = pickle.load(open(os.path.join(CACHE, 'fontes.pkl'), 'rb'))
    G = achatar(md['ws'])
    # out -> E: refaz a grafia para ter a origem de cada token (o texto final só muda «-» e aspas)
    m_out, origem, _ = config.modernizar(E, decisoes.MANUAL)
    if len(m_out) != len(out):
        origem = None
        print('aviso: o texto final não tem o tamanho da grafia (corrigir mudou tokens); sem trecho de 1854 exato')
    so_pal = lambda ts: [k2(t) for t in ts if e_palavra(t) or t in ('#',)]
    feitos = {d['para'] for d in decisoes.CONFERENCIA}
    cap, caps = None, []
    for t in out:
        if t.startswith('#'):
            cap = t[1:]
        caps.append(cap)
    res = []
    for tp, i1, i2, j1, j2 in alinhar(out, G, chave=k2):
        if tp == 'equal':
            continue
        a, b = out[i1:i2], G[j1:j2]
        if so_pal(a) == so_pal(b):
            continue                                   # só pontuação
        if any(t.startswith('#') or t == '¶' for t in a) and not [t for t in a if e_palavra(t)]:
            continue
        # contexto: 4 palavras de cada lado
        x0 = i1
        n = 0
        while x0 > 0 and n < 4:
            x0 -= 1
            n += e_palavra(out[x0])
        x1 = i2
        n = 0
        while x1 < len(out) and n < 4:
            n += e_palavra(out[x1])
            x1 += 1
        if any(t.startswith('#') for t in out[x0:x1]):
            # não atravessa o começo de capítulo
            ks = [k for k in range(x0, x1) if out[k].startswith('#')]
            if ks[0] < i1:
                x0 = ks[-1] + 2
            else:
                x1 = ks[0] - 1
        para = junta([t for t in out[x0:x1] if t != '¶'])
        if para in feitos:
            continue
        if origem:
            e0 = origem[x0] if x0 < len(origem) else len(E) - 1
            e1 = origem[x1 - 1] + 1 if x1 - 1 < len(origem) else len(E)
            v1854 = junta([t for t in E[e0:e1] if t != '¶' and not str(t).startswith('#')])
        else:
            v1854 = para
        res.append({'id': len(res) + 1, 'cap': caps[i1], 'para': para,
                    'nosso': junta([t for t in a if t != '¶']) or '(nada)',
                    'ws': junta([t for t in b if t != '¶']) or '(nada)',
                    'antes': junta([t for t in out[x0:i1] if t != '¶']),
                    'depois': junta([t for t in out[i2:x1] if t != '¶']),
                    'ws_ctx': junta([t for t in G[max(0, j1 - 6):j2 + 6] if t != '¶' and not t.startswith('#')]),
                    'v1854': v1854})
    return res


if __name__ == '__main__':
    ps = pontos()
    os.makedirs(os.path.join(CACHE, 'ver'), exist_ok=True)
    json.dump(ps, open(os.path.join(CACHE, 'ver', 'pontos2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(len(ps), 'pontos')
    if '--pranchas' in sys.argv:
        import conferir
        de = int(sys.argv[sys.argv.index('--de') + 1]) if '--de' in sys.argv else 1
        ps = [p for p in ps if p['id'] >= de]
        for k in range(0, len(ps), 10):
            lote = ps[k:k + 10]
            base = os.path.join(CACHE, 'ver', f'q-{lote[0]["id"]:04d}')
            res, arqs = conferir.montar([(str(p['id']), p['v1854']) for p in lote], 'bbm4846', base)
            achados = dict(res)
            with open(base + '.txt', 'w', encoding='utf-8') as f:
                for p in lote:
                    pag = achados.get(str(p['id']))
                    f.write(f"{p['id']}\tp{pag}\t{p['cap']}\n  nosso: {p['antes']} [{p['nosso']}] {p['depois']}\n"
                            f"  ws:    [{p['ws']}]   ({p['ws_ctx']})\n")
            print(base, len(arqs), 'não achados:', [r for r, pg in res if pg is None])
