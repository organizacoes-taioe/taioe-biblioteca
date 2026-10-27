"""Infância — os pontos a conferir nas imagens de 1947, numa lista só.

  python3 ferramentas/texto.py infancia
  python3 edicoes/infancia/revisao.py            (grava relatorios/pontos.tsv e pontos.json)
  python3 edicoes/infancia/conferir.py ferramentas/cache/infancia/relatorios/pontos.tsv

Junta: (b) os desempates sem maioria (config.rever: mais de uma leitura é toda de palavras que
existem); (c) os acentos que os OCRs de 1947 leem diferente e o voto não resolveu (config.acentos);
(d) ponto seguido de minúscula fora de abreviatura; (e) as palavras fora do léxico que não são nomes;
(f) sujeira; (g) vírgula antes de maiúscula. Os pontos já decididos em conferencia.json (pelo
'para') saem da lista.

Cada ponto: id, trecho para achar na imagem, capítulo, tipo, 'para' (o texto final em volta, como
está), e as leituras. As decisões vão para conferencia.json: {id, cap, de, para, texto, cod}.
"""
import importlib.util
import json
import os
import pickle
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
sys.path.insert(0, AQUI)
from edicao import estabelecer  # noqa: E402
from edicao.fontes import cache  # noqa: E402
from edicao.tokens import e_palavra, texto  # noqa: E402

import config  # noqa: E402
import grafia1990  # noqa: E402


def carregar(nome):
    spec = importlib.util.spec_from_file_location('ca_' + nome, os.path.join(AQUI, nome + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def final():
    """Tokens do texto final (o out de texto.py) e a seção de cada um."""
    r = pickle.load(open(cache('infancia', 'resultado.pkl'), 'rb'))
    out = [t for t in r['out'] if t != '_']
    caps, cap = [], None
    for t in out:
        if t.startswith('#'):
            cap = t[1:]
        caps.append(cap)
    return out, caps


def trecho(out, i, j, antes=3, depois=3):
    """O texto final em volta de out[i:j], sem passar de parágrafo."""
    a = i
    n = 0
    while a > 0 and n < antes and out[a - 1] != '¶' and not out[a - 1].startswith('#'):
        a -= 1; n += e_palavra(out[a])
    b = j
    n = 0
    while b < len(out) and n < depois and out[b] != '¶' and not out[b].startswith('#'):
        n += e_palavra(out[b]); b += 1
    return texto(out[a:b])


NOMES = set()


def pontos():
    NOMES.update(pickle.load(open(cache('infancia', 'testemunhos.pkl'), 'rb'))['nomes'])
    decididos = json.load(open(os.path.join(AQUI, 'conferencia.json'), encoding='utf-8'))
    conf = {d['para'] for d in decididos}
    leituras_vistas = {d['de'] for d in decididos if d.get('de')}
    out, caps = final()
    itens = []

    def ponto(tipo, para, cap, leituras='', busca=None):
        if para in conf or leituras and leituras in leituras_vistas or any(x['para'] == para for x in itens):
            return
        itens.append({'tipo': tipo, 'para': para, 'busca': busca or para, 'cap': cap, 'leituras': leituras})

    def moderno(s):
        return texto(grafia1990.modernizar(_tok(s), dec.MANUAL)[0])

    dec = carregar('decisoes')
    # (b) desempates sem apoio: refaz o confronto para ter as dúvidas de rever()
    tr, md = pickle.load(open(cache('infancia', 'fontes.pkl'), 'rb'))
    E0, sitios = estabelecer.estabelecer(tr, config.BASE, md, config.CORRELACIONADOS, None, config.UM_VOTO)
    config.rever(tr, md, sitios)
    for x in config.DUVIDAS:
        a = ' '.join(x['antes'].split(' ')[-3:])
        d = ' '.join(x['depois'].split(' ')[:2])
        busca = f"{a} {x['escolha_txt']} {d}".replace('¶', ' ').strip()
        leit = ' || '.join(f'{n}: {v}' for n, v in x['leituras'].items())
        ponto('desempate', moderno(busca), None, leit, busca)

    # (c) acentos
    tt = pickle.load(open(cache('infancia', 'testemunhos.pkl'), 'rb'))
    for t, b, esc, duvida, ctx in tt['acentos']:
        if duvida:
            ponto('acento', moderno(ctx), None, f't47: {t} || b47: {b} || escolha: {esc}', ctx)

    # (d) ponto seguido de minúscula
    for k in range(1, len(out) - 1):
        if out[k] == '.' and e_palavra(out[k - 1]) and e_palavra(out[k + 1]) and out[k + 1][:1].islower() \
                and out[k - 1].lower() not in config.ABREVIATURAS:
            ponto('ponto', trecho(out, k - 1, k + 2, 2, 2), caps[k])

    # (f) sujeira: aspas sem par no parágrafo, dígito solto, sinal estranho, pontuação dobrada
    ini = 0
    for k in range(len(out) + 1):
        if k == len(out) or out[k] in ('¶', '/') or out[k].startswith('#'):
            par = out[ini:k]
            if par.count('«') != par.count('»'):
                j = next((j for j, t in enumerate(par) if t in ('«', '»')), 0)
                ponto('sujeira', trecho(out, ini + j, ini + j + 1, 3, 3), caps[min(ini + j, len(caps) - 1)], 'aspas sem par')
            ini = k + 1
    estranhos = {'‘', '’', "'", '"', '&', '®', '•', '©', '~', '^', '*', '+', '=', '<', '>', '..', '\\', '%', '$', '#'}
    for k, t in enumerate(out):
        if t in estranhos or re.fullmatch(r'\d', t) and not (k + 1 < len(out) and out[k + 1] in ('.º', 'º')) \
                or t in (',', '.', ';', ':') and k + 1 < len(out) and out[k + 1] in (',', '.', ';', ':'):
            ponto('sujeira', trecho(out, k, k + 1, 3, 3), caps[k], t)

    # (g) vírgula antes de maiúscula que não é nome (o Tesseract lê ponto como vírgula)
    for k in range(1, len(out) - 1):
        if out[k] == ',' and e_palavra(out[k + 1]) and out[k + 1][:1].isupper() and out[k + 1].lower() not in NOMES \
                and out[k + 1] not in ('D', 'Dr', 'Ó', 'São', 'Seu', 'Sinha') and len(out[k + 1]) > 1:
            ponto('vírgula', trecho(out, k - 1, k + 2, 3, 3), caps[k], out[k + 1])

    # (e) fora do léxico
    nomes = NOMES
    for k, t in enumerate(out):
        if not e_palavra(t) or t[:1].isupper() and t.lower() in nomes or t in dec.LEXICO_OK:
            continue
        if any(p and grafia1990.atual_parte(p)[1] == 'SEM_PAR' and p.lower() not in nomes for p in t.split('-')):
            ponto('léxico', trecho(out, k, k + 1, 2, 2), caps[k], t)
    return itens


def _tok(s):
    from edicao.tokens import TOK
    return TOK.findall(s)


if __name__ == '__main__':
    itens = pontos()
    arq = cache('infancia', os.path.join('relatorios', 'pontos.tsv'))
    with open(arq, 'w', encoding='utf-8') as f:
        for n, x in enumerate(itens, 1):
            x['id'] = n
            f.write(f"{n}\t{x['busca']}\t{x['tipo']}\t{x['cap']}\t{x['para']}\t{x['leituras']}\n")
    json.dump(itens, open(arq[:-4] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(itens), 'pontos', Counter(x['tipo'] for x in itens), 'em', arq)
