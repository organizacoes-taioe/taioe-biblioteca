"""Iracema — lista das mudanças da 3ª edição (1878) sobre a 1ª (1865), para a página «Sobre esta edição».

  python3 ferramentas/texto.py iracema            (estabelece o texto)
  python3 edicoes/iracema/mudancas.py             (grava edicoes/iracema/mudancas.json)
  python3 ferramentas/texto.py iracema --publicar

Compara o texto final com o da 1ª edição (Wikisource) atualizado do mesmo modo (mesmas edições de
referência, mesmo léxico, mesmo MANUAL), de modo que as diferenças só de grafia somem. As notas do autor
(passadas a limpo à parte) e o pós-escrito (que 1865 não tem) ficam de fora. As correções nossas de erros
de 1878 não contam. Na 2ª edição (1870), que não se pôde ler, já estava parte destas mudanças.
"""
import importlib.util
import json
import os
import pickle
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
from edicao.fontes import cache  # noqa: E402
from edicao.montar import aspas_angulares  # noqa: E402
from edicao.grafia import sem_acento  # noqa: E402
from edicao.tokens import achatar, alinhar, e_palavra, texto  # noqa: E402


def carregar(nome):
    spec = importlib.util.spec_from_file_location('ir_' + nome, os.path.join(AQUI, nome + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def chave(x):
    """Iguala o que só é grafia: acentos e o «-ão» átono de 1865 (sairão = saíram, gostão = gostam)."""
    if not e_palavra(x):
        return x
    return re.sub(r'ao$', 'am', sem_acento(x.lower()))


def mudancas():
    config, dec = carregar('config'), carregar('decisoes')
    tr, md = pickle.load(open(cache('iracema', 'fontes.pkl'), 'rb'))
    r = pickle.load(open(cache('iracema', 'resultado.pkl'), 'rb'))
    erros = [(b, t) for tipo, b, t in dec.EMENDAS if tipo == 'erro']
    so = lambda obra: [p for p in obra if p['titulo'] not in (config.POS, config.DEDICATORIA)]
    E65 = [t for t in achatar(so(tr['ws65'])) if t != '_']
    out65, _, _ = config.modernizar(E65, dec.MANUAL)
    limpa = lambda ts: [('—' if t == '-' else t) for t in aspas_angulares(ts) if t != '_']
    B0 = limpa(r['out'])
    # o texto final sem o pós-escrito e a dedicatória (pelas marcas de parte)
    B, dentro = [], True
    for i, t in enumerate(B0):
        if t.startswith('#'):
            tit = texto(B0[i + 2:B0.index('¶', i + 2)]) if t == '#' else ''
            dentro = not (tit.startswith('Pós-escrito') or tit.startswith('Dedicatória'))
        if dentro:
            B.append(t)
    A = limpa(out65)
    titulos, cap = {}, None
    for i, t in enumerate(B):
        if t.startswith('#'):
            cap = t[1:] or texto(B[i + 2:B.index('¶', i + 2)])
            cap = dec.TITULOS.get(cap, cap)
        titulos[i] = cap
    ops = [o for o in alinhar(A, B, chave=chave) if o[0] != 'equal']
    juntos = []
    for o in ops:
        if juntos and o[1] - juntos[-1][2] <= 3 and '¶' not in A[juntos[-1][2]:o[1]]:
            juntos[-1] = ('replace', juntos[-1][1], o[2], juntos[-1][3], o[4])
        else:
            juntos.append(o)
    itens = []
    for t, i1, i2, j1, j2 in juntos:
        if any(x.startswith('#') for x in A[i1:i2] + B[j1:j2]):
            continue
        a0, b0, n = i1, j1, 0
        while a0 > 0 and n < 2 and A[a0 - 1] != '¶' and not A[a0 - 1].startswith('#'):
            a0 -= 1; b0 -= 1; n += e_palavra(A[a0])
        a3, b3, n = i2, j2, 0
        while a3 < len(A) and b3 < len(B) and n < 2 and A[a3] != '¶' and chave(A[a3]) == chave(B[b3]):
            n += e_palavra(A[a3]); a3 += 1; b3 += 1
        mostra = lambda ts: re.sub(r'\s*¶\s*', ' ¶ ', texto(ts)).strip()
        de, para = mostra(A[a0:a3]), mostra(B[b0:b3])
        if [chave(x) for x in A[a0:a3]] == [chave(x) for x in B[b0:b3]]:
            continue
        tipo = ('parágrafo' if set(A[i1:i2] + B[j1:j2]) <= {'¶'} else
                'pontuação' if not any(e_palavra(x) for x in A[i1:i2] + B[j1:j2]) else 'palavras')
        itens.append({'cap': titulos.get(j1), 'de': de, 'para': para, 'tipo': tipo})
    return itens


if __name__ == '__main__':
    itens = mudancas()
    json.dump({'itens': itens}, open(os.path.join(AQUI, 'mudancas.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(itens), 'mudanças;', Counter(x['tipo'] for x in itens))
