"""Recordações do Escrivão Isaías Caminha — os pontos a conferir nas imagens de 1917.

  python3 ferramentas/texto.py isaias-caminha
  python3 edicoes/isaias-caminha/pontos.py              (grava relatorios/pontos.tsv e pontos-busca.tsv)
  python3 edicoes/isaias-caminha/conferir.py ferramentas/cache/isaias-caminha/relatorios/pontos-busca.tsv
  (pranchas em ferramentas/cache/isaias-caminha/ver/pontos-busca-1917-<n>.png)

Compara o texto estabelecido (antes da grafia de hoje: resultado.pkl, 'E0') com a edição moderna de 1917
(Ática, bv). Fica de fora a diferença só de grafia, a abreviatura que a moderna desdobra (sr. → senhor)
e o que o texto de 1917 tem igual ao do Wikisource (texto de 1909): ali a Ática emendou. O resto é
sujeira de OCR que os dois OCRs leram igual, ou lição de 1917 que a Ática mudou: as duas coisas se
decidem na imagem. A decisão vai para conferencia.json com a chave 'c|antes|atual|depois' (ver
config.corrigir_lidos), e o valor é o que o impresso traz no lugar de 'atual', na grafia de 1917.
"""
import json
import os
import pickle
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
sys.path.insert(0, AQUI)
from edicao.fontes import cache  # noqa: E402
from edicao.grafia import ao1990, chave, esqueleto, mesma_palavra  # noqa: E402
from edicao.tokens import _mapeador, achatar, alinhar, e_palavra, texto  # noqa: E402

import config  # noqa: E402

EXPANSOES = {'senhor', 'senhora', 'senhores', 'doutor', 'são', 'santa', 'santo', 'dona', 'vossa', 'senhoria',
             'excelência', 'companhia', 'cia', 'número', 'doutora', 'doutores'}


FORMAS = {('cousa', 'coisa'), ('cousas', 'coisas'), ('dous', 'dois'), ('bebedo', 'bêbado'), ('bebedos', 'bêbados'),
          ('cognac', 'conhaque'), ('wagon', 'vagão'), ('restaurant', 'restaurante'), ('lage', 'laje')}


def mesma(a, b):
    if (a.lower(), b.lower()) in FORMAS:
        return True
    return (chave(a) == chave(b) or esqueleto(a) == esqueleto(b) or mesma_palavra(a, b)
            or chave(ao1990(b)) == chave(a))


def so_grafia(we, wm):
    if len(we) == len(wm) and all(mesma(a, b) for a, b in zip(we, wm)):
        return True
    return bool(we) and bool(wm) and esqueleto(''.join(we)) == esqueleto(''.join(wm))


def abreviatura(we, wm):
    return (we and all(w in config.ABREV or len(w) == 1 and w.isupper() for w in we)
            and all(w.lower() in EXPANSOES for w in wm))


def pontos():
    r = pickle.load(open(cache(config.OBRA, 'resultado.pkl'), 'rb'))
    E = r['E0']
    md = config.modernas()
    M = achatar(md['bv'])
    W = achatar(md['ws'])
    mw = _mapeador(alinhar(E, W, chave=chave))
    out = []
    for tp, i1, i2, j1, j2 in alinhar(E, M, chave=chave):
        if tp == 'equal':
            continue
        ev, mv = E[i1:i2], M[j1:j2]
        if any(t.startswith('#') for t in ev + mv):
            continue
        we = [t for t in ev if e_palavra(t)]
        wm = [t for t in mv if e_palavra(t)]
        if not we and not wm:
            continue                                  # só pontuação
        if so_grafia(we, wm) or abreviatura(we, wm):
            continue
        a, b = mw(i1, True), mw(i2, True)
        ww = [t for t in W[a:b] if e_palavra(t)]
        if we and len(ww) == len(we) and all(mesma(x, y) for x, y in zip(we, ww)) and not any(config.lixo(t) for t in ev):
            continue                                  # 1917 = Wikisource (1909): emenda da Ática
        antes = E[max(0, i1 - 5):i1]
        depois = E[i2:i2 + 5]
        chave_c = 'c|' + ' '.join(antes) + '|' + ' '.join(ev) + '|' + ' '.join(depois)
        lixo = any(config.lixo(t) for t in ev)
        pa = [t for t in E[max(0, i1 - 12):i1] if e_palavra(t)][-3:]
        pd = [t for t in E[i2:i2 + 12] if e_palavra(t)][:3]
        out.append({'chave': chave_c, 'atual': texto(ev), 'moderna': texto(mv), 'tipo': 'lixo' if lixo else 'variante',
                    'busca': ' '.join(pa + we + pd), 'contexto': texto(E[max(0, i1 - 12):i1]) + ' [' + texto(ev) + '] ' + texto(E[i2:i2 + 12])})
    return out


if __name__ == '__main__':
    P = pontos()
    conf = json.load(open(os.path.join(AQUI, 'conferencia.json'), encoding='utf-8')) if os.path.exists(os.path.join(AQUI, 'conferencia.json')) else {}
    P = [p for p in P if p['chave'] not in conf]
    pasta = cache(config.OBRA, 'relatorios')
    with open(os.path.join(pasta, 'pontos.tsv'), 'w', encoding='utf-8') as f:
        f.write('n\ttipo\tatual\tmoderna\tcontexto\tchave\n')
        for k, p in enumerate(P, 1):
            f.write(f"{k}\t{p['tipo']}\t{p['atual']}\t{p['moderna']}\t{p['contexto']}\t{p['chave']}\n")
    with open(os.path.join(pasta, 'pontos-busca.tsv'), 'w', encoding='utf-8') as f:
        for k, p in enumerate(P, 1):
            f.write(f"{k}\t{p['busca']}\n")
    from collections import Counter
    print(len(P), 'pontos', Counter(p['tipo'] for p in P))
