"""São Bernardo — lista das mudanças de 1947 sobre a 1ª edição (1934), para a página «Sobre esta edição».

  python3 ferramentas/texto.py sao-bernardo          (estabelece o texto)
  python3 edicoes/sao-bernardo/mudancas.py           (grava edicoes/sao-bernardo/mudancas.json)
  python3 ferramentas/texto.py sao-bernardo --publicar

Compara o texto final com o de 1934 (o 'a34' do confronto) posto na grafia de hoje pelas mesmas
regras, de modo que as diferenças só de grafia somem. As mudanças de 1938 e de 1947 vão juntas: a
2ª edição impressa não está digitalizada. Ficam de fora as contrações desfeitas (dum → de um),
ditas em bloco na apresentação.
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
    spec = importlib.util.spec_from_file_location('sb_' + nome, os.path.join(AQUI, nome + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


CONTRACOES = {('dum',): ('de', 'um'), ('duma',): ('de', 'uma'), ('duns',): ('de', 'uns'), ('dumas',): ('de', 'umas'),
              ('num',): ('em', 'um'), ('numa',): ('em', 'uma'), ('nuns',): ('em', 'uns'), ('numas',): ('em', 'umas'),
              ('dalgum',): ('de', 'algum'), ('dalguma',): ('de', 'alguma'), ('doutro',): ('de', 'outro'),
              ('doutra',): ('de', 'outra'), ('dêle',): ('de', 'ele'), ('dele',): ('de', 'ele'),
              ("d'água",): ('de', 'água'), ('d’água',): ('de', 'água'), ('d', '’', 'água'): ('de', 'água'),
              ('d', "'", 'água'): ('de', 'água')}


from config import de_1934  # noqa: E402


def k(t):
    return chave(t.replace('’', "'"))


# grafias de 1934 que as regras não alcançam (a mesma palavra)
MESMAS = {('cincoenta', 'cinquenta'), ('magdalena', 'madalena'), ('mandaracus', 'mandacarus'), ('cognac', 'conhaque'),
          ('kilos', 'quilos'), ('kilo', 'quilo'), ('nickel', 'níquel'), ('nickeis', 'níqueis'), ('enguliu', 'engoliu'),
          ('engulia', 'engolia'), ('candieiro', 'candeeiro'), ('candieiros', 'candeeiros'), ('accordams', 'acórdãos'),
          ('machina', 'máquina'), ('machinas', 'máquinas'), ('taboleiro', 'tabuleiro'), ('engulir', 'engolir')}


def mesma(a, b):
    """a (1934, já na grafia de hoje pelas regras) e b (o texto final) são a mesma palavra? Iguais na
    grafia antiga e moderna, salvo se as duas existem hoje como palavras diferentes (tudo × todo)."""
    la, lb = a.lower().replace('-', ''), b.lower().replace('-', '')
    if la == lb or (la, lb) in MESMAS or chave(la) == chave(lb) or la.replace('ch', 'x') == lb.replace('ch', 'x'):
        return True
    lex = grafia1990.lexico()
    if not mesma_palavra(la, lb):
        return False
    return not (la in lex and lb in lex)


def so_grafia(A, B):
    """O trecho A (1934) → B (final) muda só a grafia, as palavras juntas ou separadas (mil reis →
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


def sem_aspas_nos_jornais(ts):
    """Em 1934 os jornais vão em itálico e entre aspas; em 1947, só em itálico: as aspas não contam."""
    from config import ITALICOS
    nomes = [n.split() for n in ITALICOS]
    out, i = [], 0
    while i < len(ts):
        if ts[i] in ('«', '“', '"') and any(ts[i + 1:i + 1 + len(n)] == n and i + 1 + len(n) < len(ts)
                                           and ts[i + 1 + len(n)] in ('»', '”', '"') for n in nomes):
            n = next(n for n in nomes if ts[i + 1:i + 1 + len(n)] == n)
            out += n
            i += len(n) + 2
            continue
        out.append(ts[i])
        i += 1
    return out


def mudancas():
    dec = carregar('decisoes')
    t34 = pickle.load(open(cache('sao-bernardo', 'testemunhos34.pkl'), 'rb'))
    r = pickle.load(open(cache('sao-bernardo', 'resultado.pkl'), 'rb'))
    E34 = sem_aspas_nos_jornais([t for t in achatar(t34['a34']) if t != '_'])
    out34, _, _ = grafia1990.modernizar([de_1934(t) if e_palavra(t) else t for t in E34], dec.MANUAL)
    # (os versos, que 1934 compõe um por parágrafo e 1947 num bloco só, comparam-se como parágrafos)
    limpa = lambda ts: [('—' if t == '-' else '¶' if t == '/' else t) for t in aspas_angulares(ts) if t != '_']
    A, B = limpa(out34), limpa(r['out'])
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


if __name__ == '__main__':
    itens, contr = mudancas()
    json.dump({'contracoes': contr, 'itens': itens}, open(os.path.join(AQUI, 'mudancas.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(itens), 'mudanças;', contr, 'contrações desfeitas;', Counter(x['tipo'] for x in itens))
