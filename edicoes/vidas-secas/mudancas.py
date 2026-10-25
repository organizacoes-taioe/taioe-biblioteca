"""Vidas Secas — lista das mudanças da 2ª edição (1947) sobre a 1ª (1938), para a página «Sobre esta edição».

  python ferramentas/texto.py vidas-secas          (estabelece o texto)
  python edicoes/vidas-secas/mudancas.py           (grava edicoes/vidas-secas/mudancas.json)
  python ferramentas/texto.py vidas-secas --publicar

Compara o texto final com o da 1ª edição atualizado do mesmo modo (mesma edição de referência e
mesmo MANUAL), de modo que as diferenças só de grafia somem. Ficam de fora as contrações desfeitas
(dum → de um, d’água → de água), ditas em bloco na apresentação.
"""
import importlib.util
import json
import os
import pickle
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
from edicao import modernizar  # noqa: E402
from edicao.fontes import cache  # noqa: E402
from edicao.montar import aspas_angulares  # noqa: E402
from edicao.tokens import achatar, alinhar, e_palavra, texto  # noqa: E402


def carregar(nome):
    spec = importlib.util.spec_from_file_location('vs_' + nome, os.path.join(AQUI, nome + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# palavras de 1938 que a edição de referência não atualiza (porque ali 1947 mudou o texto)
GRAFIA_1938 = {'ella': 'ela', 'elle': 'ele', 'paletot': 'paletó', 'd’agua': 'd’água', 'aquillo': 'aquilo',
               'reconhecel-o': 'reconhecê-lo', 'bonnet': 'boné', 'maguavam-no': 'magoavam-no'}

CONTRACOES = {('dum',): ('de', 'um'), ('duma',): ('de', 'uma'), ('duns',): ('de', 'uns'), ('dumas',): ('de', 'umas'),
              ('d’água',): ('de', 'água')}


def igual_na_grafia(de, para):
    """As mudanças de decisoes.AJUSTES do tipo 'grafia' (porque → por que nas perguntas, A → À) não
    são lições de 1947."""
    n = lambda s: s.lower().replace('por quê', 'porquê').replace('por que', 'porque').replace('à tarde', 'a tarde')
    return n(de) == n(para)


def contracao(a, b):
    a, b = tuple(GRAFIA_1938.get(x, x).lower() for x in a), tuple(x.lower() for x in b)
    if CONTRACOES.get(a) == b:
        return True
    # «d’água» chega partida: d ’ água
    return a == ('d', '’', 'água') and b == ('de', 'água')


def mudancas():
    config, dec = carregar('config'), carregar('decisoes')
    tr, md = pickle.load(open(cache('vidas-secas', 'fontes.pkl'), 'rb'))
    r = pickle.load(open(cache('vidas-secas', 'resultado.pkl'), 'rb'))
    refs = [(n, md[n], pos) for n, pos in config.REFERENCIAS]
    E38 = [t for t in achatar(tr['ws38']) if t != '_']
    out38, _, _ = modernizar.modernizar(E38, refs, dec.MANUAL)
    limpa = lambda ts: [('—' if t == '-' else t) for t in aspas_angulares(ts) if t != '_']
    A, B = limpa(out38), limpa(r['out'])
    titulos, cap = {}, None
    for i, t in enumerate(B):                       # título do capítulo de cada posição
        if t.startswith('#'):
            cap = texto(B[i + 2:B.index('¶', i + 2)])
        titulos[i] = cap
    ops = [o for o in alinhar(A, B, chave=lambda x: GRAFIA_1938.get(x, x).lower()) if o[0] != 'equal']
    contr = sum(1 for _, i1, i2, j1, j2 in ops if contracao(A[i1:i2], B[j1:j2]))
    ops = [o for o in ops if not contracao(A[o[1]:o[2]], B[o[3]:o[4]])]
    juntos = []                                     # mudanças a até 3 sinais uma da outra: um item só
    for o in ops:
        if juntos and o[1] - juntos[-1][2] <= 3 and '¶' not in A[juntos[-1][2]:o[1]]:
            juntos[-1] = ('replace', juntos[-1][1], o[2], juntos[-1][3], o[4])
        else:
            juntos.append(o)
    itens = []
    for t, i1, i2, j1, j2 in juntos:
        if any(x.startswith('#') for x in A[i1:i2] + B[j1:j2]):
            continue
        # contexto: até duas palavras de cada lado, sem passar de parágrafo
        a0, b0 = i1, j1
        n = 0
        while a0 > 0 and n < 2 and A[a0 - 1] != '¶' and not A[a0 - 1].startswith('#'):
            a0 -= 1; b0 -= 1; n += e_palavra(A[a0])
        a3, b3 = i2, j2
        n = 0
        while a3 < len(A) and b3 < len(B) and n < 2 and A[a3] != '¶' and A[a3] == B[b3]:
            n += e_palavra(A[a3]); a3 += 1; b3 += 1
        mostra = lambda ts: re.sub(r'\s*¶\s*', ' ¶ ', texto([GRAFIA_1938.get(x, x) for x in ts])).strip()
        de, para = mostra(A[a0:a3]), mostra(B[b0:b3])
        if igual_na_grafia(de, para):
            continue
        itens.append({'cap': titulos.get(j1), 'de': de, 'para': para,
                      'tipo': 'parágrafo' if set(A[i1:i2] + B[j1:j2]) <= {'¶'} else
                              ('pontuação' if not any(e_palavra(x) for x in A[i1:i2] + B[j1:j2]) else 'palavras')})
    return itens, contr


if __name__ == '__main__':
    itens, contr = mudancas()
    json.dump({'contracoes': contr, 'itens': itens}, open(os.path.join(AQUI, 'mudancas.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(itens), 'mudanças;', contr, 'contrações desfeitas;', Counter(x['tipo'] for x in itens))
