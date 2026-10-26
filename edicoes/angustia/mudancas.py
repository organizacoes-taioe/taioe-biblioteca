"""Angústia — as diferenças entre o texto impresso das provas (1946) e o texto estabelecido.

  python3 ferramentas/texto.py angustia          (estabelece o texto)
  python3 edicoes/angustia/mudancas.py           (grava relatorios/a-conferir.tsv)

Compara o texto final com o das provas, posto na grafia de hoje pelas mesmas regras. As provas só se
leem por OCR, e mal: uma diferença só conta se os dois OCRs das provas a mostram iguais. As que não
estão em conferencia.json vão para relatorios/a-conferir.tsv (revisao.py as junta aos outros pontos).
Conferidas todas em 2026-10-26: nenhuma mudança de redação entre as provas corrigidas e 1947 (as
correções à mão do autor são de composição); a página «Sobre» as descreve em prosa (notas.py).
"""
import importlib.util
import json
import os
import pickle
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
sys.path.insert(0, AQUI)
from edicao.fontes import cache  # noqa: E402
from edicao.grafia import chave, mesma_palavra  # noqa: E402
from edicao.montar import aspas_angulares  # noqa: E402
from edicao.tokens import achatar, alinhar, e_palavra, texto  # noqa: E402

import grafia1990  # noqa: E402


def carregar(nome):
    spec = importlib.util.spec_from_file_location('an_' + nome, os.path.join(AQUI, nome + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def k(t):
    return chave(t.replace('’', "'"))


def mesma(a, b):
    la, lb = a.lower().replace('-', ''), b.lower().replace('-', '')
    if la == lb or chave(la) == chave(lb):
        return True
    lex = grafia1990.lexico()
    if not mesma_palavra(la, lb):
        return False
    return not (la in lex and lb in lex)


def so_grafia(A, B):
    pa = [t for t in A if e_palavra(t)]
    pb = [t for t in B if e_palavra(t)]
    if [t for t in A if not e_palavra(t)] != [t for t in B if not e_palavra(t)]:
        return False
    if len(pa) == len(pb) and all(mesma(x, y) for x, y in zip(pa, pb)):
        return True
    return bool(pa) and mesma(''.join(pa), ''.join(pb))


def carregar_conferencia():
    return json.load(open(os.path.join(AQUI, 'conferencia.json'), encoding='utf-8'))


def diferencas(testemunho='p46'):
    """[(seção, de, para, tipo)] entre um texto das provas e o texto final, com duas palavras de contexto."""
    dec = carregar('decisoes')
    t46 = pickle.load(open(cache('angustia', 'testemunhos46.pkl'), 'rb'))
    r = pickle.load(open(cache('angustia', 'resultado.pkl'), 'rb'))
    E46 = [t for t in achatar(t46[testemunho]) if t != '_']
    out46, _, _ = grafia1990.modernizar(E46, dec.MANUAL)
    limpa = lambda ts: [('—' if t == '-' else t) for t in aspas_angulares(ts) if t != '_']
    A, B = limpa(out46), limpa(r['out'])
    caps, cap = {}, None
    for i, t in enumerate(B):
        if t.startswith('#'):
            cap = t[1:]
        caps[i] = cap
    ops = [o for o in alinhar(A, B, chave=k) if o[0] != 'equal']
    ops = [o for o in ops if not so_grafia(A[o[1]:o[2]], B[o[3]:o[4]])]
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
        a0, b0, n = i1, j1, 0
        while a0 > 0 and n < 2 and A[a0 - 1] != '¶' and not A[a0 - 1].startswith('#'):
            a0 -= 1; b0 -= 1; n += e_palavra(A[a0])
        a3, b3, n = i2, j2, 0
        while a3 < len(A) and b3 < len(B) and n < 2 and A[a3] != '¶' and k(A[a3]) == k(B[b3]):
            n += e_palavra(A[a3]); a3 += 1; b3 += 1
        mostra = lambda ts: re.sub(r'\s*¶\s*', ' ¶ ', texto(ts)).strip()
        de, para = mostra(A[a0:a3]), mostra(B[b0:b3])
        if de == para:
            continue
        tipo = 'parágrafo' if set(A[i1:i2] + B[j1:j2]) <= {'¶'} else \
            ('pontuação' if not any(e_palavra(x) for x in A[i1:i2] + B[j1:j2]) else 'palavras')
        itens.append({'cap': caps.get(j1), 'de': de, 'para': para, 'tipo': tipo})
    return itens


def mudancas():
    """As provas só se leem mal (papel amarelado, tinta das correções): uma diferença só conta se os
    dois OCRs das provas a mostram iguais (o Tesseract e o do PDF erram em lugares diferentes)."""
    conf = {(d['de'], d['para']): d['cod'] for d in carregar_conferencia()}
    chave_ = lambda x: (x['cap'], x['de'], x['para'])
    em_b = {chave_(x) for x in diferencas('b46')}
    itens, pendentes = [], []
    for x in diferencas('t46'):
        if chave_(x) not in em_b:
            continue
        cod = conf.get((x['de'], x['para']))
        if cod == 'ok':
            itens.append(x)
        elif cod is None:
            pendentes.append(x)
    return itens, pendentes


if __name__ == '__main__':
    itens, pendentes = mudancas()
    arq = cache('angustia', os.path.join('relatorios', 'a-conferir.tsv'))
    with open(arq, 'w', encoding='utf-8') as f:
        for n, x in enumerate(pendentes, 1):
            f.write(f"{n}\t{x['para']}\t{x['cap']}\t{x['de']}\t{x['tipo']}\n")
    print(len(itens), 'mudanças confirmadas;', len(pendentes), 'diferenças sem decisão em', arq)
