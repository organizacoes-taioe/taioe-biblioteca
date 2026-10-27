"""Caetés — o texto da 1ª edição (_Cahetés_, Schmidt, 1933), só para a lista das mudanças de 1947.

  python3 edicoes/caetes/tesseract.py bbm8400:15-240
  python3 ferramentas/texto.py caetes            (antes: a guia dos capítulos é o texto de 1947)
  python3 edicoes/caetes/edicao1933.py           (grava ferramentas/cache/caetes/testemunhos33.pkl)
  python3 edicoes/caetes/mudancas.py

Testemunhos: o Tesseract do exemplar 1 ('t33', bbm/8400) e as camadas de texto dos dois exemplares
('b33', bbm/8400; 'e33', bbm/8395). Em 1933 cada capítulo abre página nova, com o número no alto:
a leitura das páginas é a de São Bernardo (edicoes/sao-bernardo/config.py), carregada com as páginas
e a pasta de Caetés. Os capítulos que não forem achados vêm do alinhamento com o texto de 1947.
"""
import importlib.util
import os
import pickle
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
sys.path.insert(0, AQUI)
from edicao import estabelecer, fontes, ocr  # noqa: E402

import config  # noqa: E402
import tesseract  # noqa: E402


def leitor_sb():
    """O config de São Bernardo, com as páginas, os capítulos e a pasta de Caetés."""
    spec = importlib.util.spec_from_file_location('sb_config', os.path.join(AQUI, '..', 'sao-bernardo', 'config.py'))
    sb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sb)
    sb.OBRA = config.OBRA
    sb.tesseract = tesseract
    sb.NUMEROS = config.NUMEROS
    sb.PAGINAS = {'bbm8400': (15, 240), 'bbm8395': (17, 242)}
    return sb


LEITURAS = {'t33': ('bbm8400', '_linhas_tess'), 'b33': ('bbm8400', '_linhas_bbm'), 'e33': ('bbm8395', '_linhas_bbm')}


def estabelecer33():
    sb = leitor_sb()
    guia = pickle.load(open(fontes.cache(config.OBRA, 'fontes.pkl'), 'rb'))[0][config.BASE]
    obras = {}
    for n, (pdf, f) in LEITURAS.items():
        o = sb.obra_de_linhas(getattr(sb, f)(pdf), pdf)
        achados = [p['n'] for p in o]
        print(n, len(o), 'capítulos achados')
        if achados != config.NUMEROS:
            o = sb.capitulos_como(o, guia)
        obras[n] = o
    conta = {}
    for o in obras.values():
        for w in sb._palavras(o):
            conta[w] = conta.get(w, 0) + 1
    atestadas = {w for w, k in conta.items() if k >= 2}
    nomes = set(pickle.load(open(fontes.cache(config.OBRA, 'testemunhos.pkl'), 'rb'))['nomes'])
    obras = {n: sb.consertar(o, nomes, atestadas) for n, o in obras.items()}
    E33, sitios = estabelecer.estabelecer(obras, 't33', {}, um_voto=False)
    E33 = desempatar(obras, sitios)
    a33 = fontes.normalizar(ocr.obra_de_tokens(E33))
    pickle.dump({**obras, 'sitios33': sitios, 'a33': a33}, open(fontes.cache(config.OBRA, 'testemunhos33.pkl'), 'wb'))
    print(len(sitios), 'divergências entre as leituras de 1933;', dict(estabelecer.resumo(sitios)))


def desempatar(obras, sitios):
    """Sem maioria (as três leituras diferem), vence a que tem menos palavras fora do léxico depois de
    posta na grafia de hoje (as três erram em lugares diferentes); empate, o Tesseract."""
    import grafia1990
    from edicao.tokens import achatar, e_palavra
    from config import _toks
    spec = importlib.util.spec_from_file_location('ca_mudancas', os.path.join(AQUI, 'mudancas.py'))
    mud = importlib.util.module_from_spec(spec)      # pelo caminho: o leitor de São Bernardo põe a pasta
    spec.loader.exec_module(mud)                     # dele no sys.path, com outro mudancas.py
    de_1933 = mud.de_1933

    def ruins(ts):
        n = 0
        for t in ts:
            if e_palavra(t):
                w = de_1933(t)
                n += sum(1 for p in w.split('-') if p and grafia1990.atual_parte(p)[1] == 'SEM_PAR')
        return n
    B = achatar(obras['t33'])
    E, pos = [], 0
    for x in sitios:
        if x['por'].startswith('sem maioria'):
            T = {n: _toks(v) for n, v in x['leituras'].items() if v != '(lacuna)'}
            esc = min(T, key=lambda n: (ruins(T[n]), n != 't33'))
            x['escolha'], x['por'] = T[esc], 'léxico; ' + esc
        E.extend(B[pos:x['s']])
        E.extend(x['escolha'])
        pos = x['e']
    E.extend(B[pos:])
    return [t for t in E if t != '*']


if __name__ == '__main__':
    estabelecer33()
