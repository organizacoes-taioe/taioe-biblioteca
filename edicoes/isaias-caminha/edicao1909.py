"""Recordações do Escrivão Isaías Caminha — o texto da 1ª edição (Lisboa, A. M. Teixeira, 1909), só para a
lista das mudanças de 1917 (mudancas.py); não é publicado.

  python3 edicoes/isaias-caminha/edicao1909.py      (grava ferramentas/cache/isaias-caminha/texto1909.pkl)

Duas leituras do exemplar da Brasiliana (BBM 4799, p. 11–319 do PDF; errata nas p. 321–322): o
Tesseract (tess-bbm4799-1909/, tesseract.py) e o OCR que vem no PDF. Mesmo método do texto de 1917
(config.py), com a edição do Wikisource, que segue o texto de 1909, como guia e desempate.
"""
import os
import pickle
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
sys.path.insert(0, AQUI)
from edicao import estabelecer, fontes, ocr  # noqa: E402

import config  # noqa: E402

PDF09 = 'bbm4799-1909'
PAGS09 = (11, 319)


def texto1909():
    md = config.modernas()
    ws = [p for p in md['ws'] if p['n']]           # sem a «Breve notícia» (só de 1917)
    bv = [p for p in md['bv'] if p['n']]
    guias = [ws, bv]
    tr = {}
    for nome, obra in (('t09', config._obra_ocr(config.linhas_tesseract(PDF09, *PAGS09))),
                       ('c09', config.camada('c09', PAGS09))):
        o, n = ocr.limpar(obra, guias)
        print(f'OCR {nome}: palavras corrigidas pelas guias:', n)
        o = ocr.estrutura_como(o, ws)
        for p, b in zip(o, ws):
            p['titulo'] = b['titulo']
        tr[nome] = o
    mods = {'ws': ws, 'bv': bv}
    E, sitios = estabelecer.estabelecer(tr, 't09', mods, lexico=True)
    E, sitios = config._rever(tr, mods, sitios, 't09', 'c09', 'ws', False)
    print('divergências 1909:', len(sitios))
    return E


if __name__ == '__main__':
    E = texto1909()
    pickle.dump(E, open(fontes.cache(config.OBRA, 'texto1909.pkl'), 'wb'))
    print('gravado:', fontes.cache(config.OBRA, 'texto1909.pkl'), len(E), 'tokens')
