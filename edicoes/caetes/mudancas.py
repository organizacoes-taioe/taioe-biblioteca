"""Caetés — lista das mudanças de 1947 sobre a 1ª edição (_Cahetés_, 1933), para a página «Sobre esta edição».

  python3 ferramentas/texto.py caetes                (estabelece o texto)
  python3 edicoes/caetes/edicao1933.py               (estabelece o texto de 1933)
  python3 edicoes/caetes/mudancas.py                 (grava edicoes/caetes/mudancas.json)
  python3 ferramentas/texto.py caetes --publicar

Compara o texto final com o de 1933 (o 'a33' de edicao1933.py) posto na grafia de hoje pelas mesmas
regras, de modo que as diferenças só de grafia somem. Ficam de fora as contrações desfeitas (dum →
de um), ditas em bloco na apresentação.
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
    spec = importlib.util.spec_from_file_location('ca_' + nome, os.path.join(AQUI, nome + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


CONTRACOES = {('dum',): ('de', 'um'), ('duma',): ('de', 'uma'), ('duns',): ('de', 'uns'), ('dumas',): ('de', 'umas'),
              ('num',): ('em', 'um'), ('numa',): ('em', 'uma'), ('nuns',): ('em', 'uns'), ('numas',): ('em', 'umas'),
              ('dalgum',): ('de', 'algum'), ('dalguma',): ('de', 'alguma'), ('doutro',): ('de', 'outro'),
              ('doutra',): ('de', 'outra'), ('dêle',): ('de', 'ele'), ('dele',): ('de', 'ele'),
              ("d'água",): ('de', 'água'), ('d’água',): ('de', 'água'), ('d', '’', 'água'): ('de', 'água'),
              ('d', "'", 'água'): ('de', 'água')}


import re as _re  # noqa: E402


def de_1933(t):
    """Uma palavra de 1933 na grafia de hoje (fazel-o → fazê-lo, annos → anos)."""
    t = _re.sub(r'(\w)l-(o|a|os|as)$', r'\1-l\2', t)
    crase = {'á': 'à', 'ás': 'às', 'Á': 'À', 'Ás': 'Às'}             # 1933 marca a crase com o agudo
    if t in crase:
        return crase[t]
    return grafia1990.atual(t)[0]


def k(t):
    return chave(t.replace('’', "'"))


# grafias de 1933 que as regras não alcançam (a mesma palavra)
MESMAS = {('cincoenta', 'cinquenta'), ('magdalena', 'madalena'), ('mandaracus', 'mandacarus'), ('cognac', 'conhaque'),
          ('kilos', 'quilos'), ('nazareth', 'nazaré'), ('manoel', 'manuel'), ('hein', 'hem'), ('kilo', 'quilo'), ('nickel', 'níquel'), ('nickeis', 'níqueis'), ('enguliu', 'engoliu'),
          ('engulia', 'engolia'), ('candieiro', 'candeeiro'), ('candieiros', 'candeeiros'), ('accordams', 'acórdãos'),
          ('machina', 'máquina'), ('machinas', 'máquinas'), ('taboleiro', 'tabuleiro'), ('engulir', 'engolir')}


def mesma(a, b):
    """a (1933, já na grafia de hoje pelas regras) e b (o texto final) são a mesma palavra? Iguais na
    grafia antiga e moderna, salvo se as duas existem hoje como palavras diferentes (tudo × todo)."""
    la, lb = a.lower().replace('-', ''), b.lower().replace('-', '')
    if la == lb or (la, lb) in MESMAS or chave(la) == chave(lb) or la.replace('ch', 'x') == lb.replace('ch', 'x'):
        return True
    lex = grafia1990.lexico()
    if not mesma_palavra(la, lb):
        return False
    return not (la in lex and lb in lex)


def so_grafia(A, B):
    """O trecho A (1933) → B (final) muda só a grafia, as palavras juntas ou separadas (mil reis →
    mil-réis, semvergonheza → sem-vergonheza) ou o hífen?"""
    pa = [t for t in A if e_palavra(t)]
    pb = [t for t in B if e_palavra(t)]
    if [t for t in A if not e_palavra(t)] != [t for t in B if not e_palavra(t)]:
        return False
    if len(pa) == len(pb) and all(mesma(x, y) for x, y in zip(pa, pb)):
        return True
    return bool(pa) and mesma(''.join(pa), ''.join(pb))


def contracao(a, b):
    a, b = tuple(x.lower() for x in a), tuple(x.lower() for x in b)
    return CONTRACOES.get(a) == b or CONTRACOES.get(tuple(chave(x) for x in a)) == tuple(chave(x) for x in b)


def carregar_conferencia():
    return json.load(open(os.path.join(AQUI, 'conferencia.json'), encoding='utf-8'))


def mudancas():
    dec = carregar('decisoes')
    t33 = pickle.load(open(cache('caetes', 'testemunhos33.pkl'), 'rb'))
    r = pickle.load(open(cache('caetes', 'resultado.pkl'), 'rb'))
    E33 = [t for t in achatar(t33['a33']) if t != '_']
    out33, _, _ = grafia1990.modernizar([de_1933(t) if e_palavra(t) else t for t in E33], dec.MANUAL)
    # (os versos, que 1933 compõe um por parágrafo e 1947 num bloco só, comparam-se como parágrafos)
    limpa = lambda ts: [('—' if t == '-' else '¶' if t == '/' else t) for t in aspas_angulares(ts) if t != '_']
    A, B = limpa(out33), limpa(r['out'])
    caps, cap = {}, None
    for i, t in enumerate(B):
        if t.startswith('#'):
            cap = t[1:]
        caps[i] = cap
    ops = [o for o in alinhar(A, B, chave=k) if o[0] != 'equal']
    contr = sum(1 for _, i1, i2, j1, j2 in ops if contracao(A[i1:i2], B[j1:j2]))
    ops = [o for o in ops if not contracao(A[o[1]:o[2]], B[o[3]:o[4]]) and not so_grafia(A[o[1]:o[2]], B[o[3]:o[4]])]
    juntos = []                                     # mudanças a até 3 sinais uma da outra: um item só
    for o in ops:
        if juntos and o[1] - juntos[-1][2] <= 3 and '¶' not in A[juntos[-1][2]:o[1]]:
            juntos[-1] = ('replace', juntos[-1][1], o[2], juntos[-1][3], o[4])
        else:
            juntos.append(o)
    conf = {(d['de'], d['para']): d['cod'] for d in carregar_conferencia()}
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
        if de == para or conf.get((de, para)) in ('g', 'ws'):
            continue
        itens.append({'cap': caps.get(j1), 'de': de, 'para': para,
                      'tipo': 'parágrafo' if set(A[i1:i2] + B[j1:j2]) <= {'¶'} else
                              ('pontuação' if not any(e_palavra(x) for x in A[i1:i2] + B[j1:j2]) else 'palavras')})
    return itens, contr


# erros tipográficos de 1933 que 1947 corrige (não são mudanças do autor): o trecho de 1933
ERROS_1933 = ['abatoou', 'baixe-los', 'defintivamente', 'Borroca', 'vegarosamente', 'Poe eu', 'prejuciaes', 'Anciãs',
              'sueco', 'bando de alegria', 'do bando', 'um cantiga', 'com era', 'do quatro']


def robustas(itens):
    """Só as mudanças em que as três leituras de 1933 (edicao1933.py) trazem o mesmo trecho: a
    concordância das três afasta o erro de leitura. Pontuação e parágrafos ficam de fora (a pontuação
    de 1933 o OCR lê mal: as aspas, os pontos, as falas que se juntam)."""
    dec = carregar('decisoes')
    t33 = pickle.load(open(cache('caetes', 'testemunhos33.pkl'), 'rb'))
    lidos = []
    for n in ('t33', 'b33', 'e33'):
        ts = [t for t in achatar(t33[n]) if t != '_']
        out, _, _ = grafia1990.modernizar([de_1933(t) if e_palavra(t) else t for t in ts], dec.MANUAL)
        lidos.append(' ' + ' '.join(k(t) for t in aspas_angulares(out) if t != '¶' and not t.startswith('#')) + ' ')
    ok = []
    for x in itens:
        if x['tipo'] != 'palavras':
            continue
        de = ' ' + ' '.join(k(t) for t in _re.findall(r"[\w’'-]+|[^\w\s]", x['de']) if t != '¶') + ' '
        if all(de in l for l in lidos) and not any(e in x['de'] for e in ERROS_1933):
            ok.append(x)
    return ok


if __name__ == '__main__':
    itens, contr = mudancas()
    todas = len(itens)
    itens = robustas(itens)
    print(todas, 'diferenças;', len(itens), 'com as três leituras de 1933 de acordo')
    json.dump({'contracoes': contr, 'itens': itens}, open(os.path.join(AQUI, 'mudancas.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(itens), 'mudanças;', contr, 'contrações desfeitas;', Counter(x['tipo'] for x in itens))
