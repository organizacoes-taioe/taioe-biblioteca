"""Insônia — a grafia de 1947 (Formulário Ortográfico de 1943) passada à do Acordo de 1990,
palavra por palavra, sem edição moderna de referência. Cópia da de São Bernardo; o léxico leva os
outros romances do Graciliano já publicados (não este: os erros de leitura dele voltariam como palavras).

Léxico: a lista de palavras do português do Brasil do sistema (/usr/share/dict/brazilian, grafia
de 1971, posta no Acordo por grafia.ao1990) e as palavras dos textos já publicados na Biblioteca.
Para cada palavra, a primeira forma do léxico entre: ela mesma; ela sem os acentos que caíram em
1971 (o diferencial de êle, sôbre, côr, e o grave de sòzinho); e as formas de mesmo esqueleto
(quási → quase; as formas de 1934 que sobrarem: annos → anos). Nomes próprios e o que não estiver
no léxico ficam como estão e vão para o relatório (`sem_par.tsv`), para o MANUAL de decisoes.py.
"""
import glob
import itertools
import os
import re
import sys
import unicodedata
from difflib import SequenceMatcher

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao.grafia import ao1990, chave, esqueleto, forma_atual, igualar_caixa  # noqa: E402
from edicao.tokens import TOK, e_palavra  # noqa: E402

DICIONARIO = '/usr/share/dict/brazilian'
CLITICOS = {'lo', 'la', 'los', 'las', 'no', 'na', 'nos', 'nas', 'me', 'te', 'se', 'lhe', 'lhes', 'vos',
            'o', 'a', 'os', 'as', 'mo', 'ma', 'to', 'ta', 'lho', 'lha'}
CRASE = {'à', 'às', 'àquele', 'àquela', 'àqueles', 'àquelas', 'àquilo'}
# acentos que podem ter caído desde 1943: o grave da sílaba subtônica, o circunflexo e o agudo
# diferenciais, o trema
CAIDOS = {'ò': 'o', 'è': 'e', 'ì': 'i', 'ù': 'u', 'à': 'a', 'ê': 'e', 'ô': 'o', 'é': 'e', 'ó': 'o', 'ü': 'u',
          'í': 'i', 'â': 'a', 'á': 'a', 'ú': 'u'}

_LEX = None
_IDX = None


def nfc(s):
    return unicodedata.normalize('NFC', s)


def lexico():
    global _LEX, _IDX
    if _LEX is None:
        lex = set()
        if os.path.exists(DICIONARIO):
            for w in open(DICIONARIO, encoding='utf-8'):
                w = nfc(w.strip())
                if w:
                    lex.add(ao1990(w).lower())
        for f in glob.glob(os.path.join(RAIZ, 'conteudo', 'machado-de-assis', '*.js')) + \
                [f for f in glob.glob(os.path.join(RAIZ, 'conteudo', 'graciliano-ramos', '*.js'))
                 if not f.endswith('insonia.js')]:
            corpo = nfc(open(f, encoding='utf-8').read())
            corpo = corpo[corpo.find('partes: ['):]                 # só o texto (a página «Sobre» traz grafias antigas)
            for w in TOK.findall(corpo):
                if e_palavra(w) and '-' not in w:
                    lex.add(w.lower())
        _LEX = lex
        _IDX = {}
        for w in lex:
            _IDX.setdefault(esqueleto(w), []).append(w)
    return _LEX


def _variantes(w):
    """w e as formas sem os acentos que podem ter caído, das que mudam menos às que mudam mais."""
    pos = [i for i, ch in enumerate(w) if ch in CAIDOS]
    out = [w]
    for n in range(1, min(len(pos), 3) + 1):
        for comb in itertools.combinations(pos, n):
            out.append(''.join(CAIDOS[ch] if i in comb else ch for i, ch in enumerate(w)))
    return out


def atual_parte(p, antes_de_clitico=False):
    """Grafia atual de uma palavra sem hífen. Devolve (forma, fonte)."""
    lex = lexico()
    lw = p.lower()
    if lw in CRASE:
        return lw, 'lexico'
    if lw.endswith('mente') and len(lw) > 7:
        # advérbio: o acento da base, que em 1943 vira grave (pèssimamente, ràpidamente) e o OCR às vezes
        # lê agudo ou circunflexo, caiu em 1971
        lw = re.sub(r'[áéíóúâêôàèìòù](?=.*mente$)', lambda m: CAIDOS[m.group(0)], lw)
    if antes_de_clitico and re.search(r'[áéêíóôú]$', lw):          # considerá-lo, fê-lo, construí-lo
        if re.search(r'(?:[^aeiouáéíóú]|[gq]u)í$', lw):                # despedí-lo (1943) → despedi-lo; fica
            lw = lw[:-1] + 'i'                                       # o hiato: construí-lo, atraí-la
        return ao1990(lw), 'lexico'
    for v in _variantes(lw):
        a = ao1990(v)
        if a in lex:
            return a, 'lexico'
    # forma de mesmo esqueleto só se a diferença for de grafia (director → diretor, annos → anos):
    # a chave de alinhamento iguala ct/t, pt/t, ph/f, y/i, consoantes dobradas; vogais diferentes não
    ops = [o for o in _IDX.get(esqueleto(lw), []) if chave(o) == chave(lw)]
    if ops:
        return max(ops, key=lambda o: (SequenceMatcher(None, lw, o).ratio(), o)), 'esqueleto'
    # fora do léxico: só os acentos que caíram com certeza (grave fora da crase, trema)
    a = re.sub(r'[òèìù]', lambda m: CAIDOS[m.group(0)], lw)
    return ao1990(a), 'SEM_PAR'


def atual(w, manual=None):
    """Grafia atual de um token (palavra com ou sem hífen). Devolve (forma, fonte)."""
    manual = manual or {}
    if w in manual:
        return manual[w], 'manual'
    partes = w.split('-')
    novas, fontes_ = [], []
    for k, p in enumerate(partes):
        if not p:
            novas.append(p)
            continue
        seguinte = partes[k + 1].lower() if k + 1 < len(partes) else ''
        n, f = atual_parte(p, seguinte in CLITICOS)
        if k and p.lower() in CLITICOS:
            n, f = p.lower(), 'lexico'
        novas.append(n)
        fontes_.append(f)
    novas = [igualar_caixa(p, n) if p else n for p, n in zip(partes, novas)]   # Bom-Sucesso: a caixa de cada parte
    novo = '-'.join(novas)
    fonte = 'SEM_PAR' if 'SEM_PAR' in fontes_ else ('esqueleto' if 'esqueleto' in fontes_ else 'lexico')
    return forma_atual(novo), fonte


# compostos que o Acordo de 1990 juntou ou separou, e os topônimos compostos, que ele escreve sem hífen
# (Base XV: «os outros topônimos compostos escrevem-se com os elementos separados»)
COMPOSTOS = {
    'ante-ontem': 'anteontem', 'contra-ordem': 'contraordem', 'contra-senso': 'contrassenso',
    'contra-revolução': 'contrarrevolução', 'contra-revolucionária': 'contrarrevolucionária',
    'contra-revolucionário': 'contrarrevolucionário', 'contra-revolucionários': 'contrarrevolucionários',
    'chove-não-molha': 'chove não molha', 'deus-nos-acuda': 'deus nos acuda', 'dias-santos': 'dias santos',
    'dia-santo': 'dia santo', 'à-toa': 'à toa', 'bê-a-bá': 'bê-á-bá', "paus-d'arco": 'paus-d’arco',
    "pau-d'arco": 'pau-d’arco', 'pau-a-pique': 'pau a pique', 'rio-de-janeiro': 'Rio de Janeiro',
    'bom-sucesso': 'Bom Sucesso', 'pão-de-açúcar': 'Pão de Açúcar', 'jacaré-dos-homens': 'Jacaré dos Homens',
    'ponta-da-terra': 'Ponta da Terra', 'pão-sem-miolo': 'Pão sem Miolo',
    # Caetés
    'há-de': 'há de', 'hei-de': 'hei de', 'hão-de': 'hão de', 'hás-de': 'hás de', 'havemos-de': 'havemos de',
    'palmeira-dos-índios': 'Palmeira dos Índios', 'palmeira-de-fora': 'Palmeira de Fora',
    'coruripe-da-praia': 'Coruripe da Praia', 'miguel-de-campos': 'Miguel de Campos',
    'passo-de-camaragibe': 'Passo de Camaragibe', 'riacho-do-mel': 'Riacho do Mel',
    'boca-de-maceió': 'Boca de Maceió', 'santa-cruz': 'Santa Cruz', 'república-argentina': 'República Argentina',
    'pernambuco-novo': 'Pernambuco Novo', 'ante-câmara': 'antecâmara', 'ante-véspera': 'antevéspera',
    'testa-de-ferro': 'testa de ferro',
}


def composto(w):
    n = COMPOSTOS.get(w.lower())
    if n is None:
        return w
    return n[0].upper() + n[1:] if w[:1].isupper() and n[:1].islower() else n


def porque(out, juntar=True):
    """«porque» das perguntas: «por que» no começo da pergunta, «por quê» quando tônico, antes da
    pontuação (a regra de hoje, como em Vidas Secas). O causal fica."""
    novo = list(out)
    for i, t in enumerate(out):
        if t.lower() not in ('porque', 'porquê'):
            continue
        seg = out[i + 1:i + 2]
        if seg and seg[0] in ('?', '!', '.', ',', '...', '…'):
            novo[i] = 'Por quê' if t[:1].isupper() else 'por quê'
            continue
        j = i + 1                                          # fim da frase
        abrev = {'d', 'D', 'dr', 'Dr', 'S', 'sr', 'Sr', 'sra', 'Sra', 'srs', 'exa', 'Exa', 'excia', 'Excia', 'etc'}
        while j < len(out) and not (out[j] in ('.', '!', '?', '¶', '...', '…') and not (out[j] == '.' and out[j - 1] in abrev)) \
                and not out[j].startswith('#'):
            j += 1
        antes = out[i - 1] if i else '¶'
        if j < len(out) and out[j] == '?' and antes.lower() not in ('é', 'que'):
            novo[i] = 'Por que' if t[:1].isupper() else 'por que'
    return [x for t in novo for x in t.split(' ')] if juntar else novo


def modernizar(E, manual=None):
    """Mesma interface de edicao.modernizar.modernizar: (tokens, origem, relatório)."""
    manual = manual or {}
    out, origem, rel = [], [], []
    i = 0
    while i < len(E):
        t = E[i]
        if not e_palavra(t):
            out.append(t); origem.append(i); i += 1
            continue
        novo, fonte = atual(t, manual)
        novo = composto(novo)
        rel.append((t, novo, fonte, i))
        for x in novo.split(' '):
            out.append(x); origem.append(i)
        i += 1
    novo_out, novo_orig = [], []
    for t, o, n in zip(out, origem, porque(out, juntar=False)):
        for x in n.split(' '):
            novo_out.append(x); novo_orig.append(o)
    return novo_out, novo_orig, rel
