"""Recordações do Escrivão Isaías Caminha — decisões editoriais.

EMENDAS: intervenções no texto-base, na grafia de 1917: (tipo, trecho, troca)
  'erro'    erro tipográfico evidente da edição de 1917 (ou corrigido pela errata do próprio volume)
  'ocr'     erro das leituras; o impresso de 1917 traz a forma certa (conferido no fac-símile)
  'revisao' lição de 1917 conferida no fac-símile que o confronto perdeu
AJUSTES: depois da modernização, em tokens separados por espaço: (tipo, antes, de, para, depois)
MANUAL: grafia final de palavras que as edições de referência não resolvem
Os pontos conferidos no fac-símile que o voto decide ficam em conferencia.json (ver config.rever).
"""

EMENDAS = [
    # a errata do próprio volume de 1917 (p. [235]): «veio» por «vinha», «deserrollar-se» (a errata dá a forma
    # errada igual à certa, «desenrolar-se»); as outras três («attendia», «dissolver-se», «diminuiu-lhe») o
    # confronto já trouxe corrigidas: ver notas.ERROS_ANTERIORES
    ('erro', "uma vez ou outra, veio perturbar", "uma vez ou outra, vinha perturbar"),
    ('erro', "algo de grave deserrollar-se", "algo de grave desenrolar-se"),
    # linhas que a composição de 1917 perdeu, completadas pela 1ª edição (1909)
    ('erro', "engrossadores com as, a senhora", "engrossadores com as suas mulheres e filhas encontravam-se alli em "
             "tocantes despedidas a amigos das duas camaras. A viscondessa de Varennes, a famosa Odalina, poetisa de "
             "muito merito e tão do gosto de Floc, viera tambem. O dr. Ricardo afastou-se logo d'ella com a senhora"),
    ('erro', "com um engenhoso aptablado de magica", "com um engenhoso apparelho de apparições e eclipses, especie "
             "complicada de tablado de magica"),
    # erros tipográficos evidentes de 1917 (conferidos no fac-símile; quase todos ausentes de 1909)
    ('erro', "creio descobrir descobrir alguma", "creio descobrir alguma"),
    ('erro', "escrever alguma verrinas", "escrever algumas verrinas"),
    ('erro', "estava em nós, na na nossa", "estava em nós, na nossa"),
    ('erro', "entre vinte cinco ou", "entre vinte e cinco ou"),
    ('erro', "das suas biographicas heroicas", "das suas biographias heroicas"),
    ('erro', "Sendo obrigado obrigado a", "Sendo obrigado a"),
    ('erro', "responder Plinio — Pagou sim, apressou-se em responder Plinio de Andrade", "responder Plinio de Andrade"),
    ('erro', "me convidada a jantar", "me convidava a jantar"),
    ('erro', "esperava essa perguntou", "esperava essa pergunta"),
    ('erro', "ou em pelotiqueiro", "ou um pelotiqueiro"),
    ('erro', "recitar versos na salas", "recitar versos nas salas"),
    ('erro', "encontrados ortos a facadas", "encontrados mortos a facadas"),
    ('erro', "dez horas eu recebera", "dez horas e eu recebera"),
    ('erro', "para o fortuna do dr", "para a fortuna do dr"),
    ('erro', "Fomos a una venda", "Fomos a uma venda"),
    ('erro', "de força. alvez se sentisse", "de força. Talvez se sentisse"),
    ('erro', "tudo aquillo á ser lido", "tudo aquillo ia ser lido"),
    ('erro', "de fraqueza, de décisão é mais", "de fraqueza, de decisão e mais"),
    ('erro', "ferir a marmellada", "ferir a martellada"),
    ('erro', "me venham ar sensações", "me venham as sensações"),
    ('erro', "parecia ser em homem rico", "parecia ser um homem rico"),
    ('erro', "arqueologia, e muita certa", "arqueologia, e muito certa"),
    ('erro', "debaixo das nações livrescas", "debaixo das noções livrescas"),
]

AJUSTES = [
]

MANUAL = {
    # formas antigas de palavras atuais (as edições de referência não dão o par)
    'cousa': 'coisa', 'cousas': 'coisas', 'Cousa': 'Coisa', 'dous': 'dois', 'bebedo': 'bêbedo',
    # abreviaturas da época (a edição moderna as desdobra)
    'dr': 'dr', 'Dr': 'Dr', 'Sr': 'Sr', 'sr': 'sr', 'snr': 'snr', 'Snr': 'Snr', 'srs': 'srs', 'Srs': 'Srs',
    'D': 'D', 'S': 'S', 'Ex': 'Ex', 'V': 'V', 'C': 'C', 'Club': 'Club',
}

import os  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ferramentas'))
from edicao.tokens import TOK  # noqa: E402

# nomes uniformizados (revisao.json, «loberant»): 1909 e 1917 imprimem «Leborant» do cap. IX em diante
NOMES = {'Leborant': 'Loberant', 'Leborante': 'Loberant'}

# versos citados que o texto moderno compõe um por parágrafo: (começo do 1º verso, número de versos)
VERSOS_BLOCOS = []

# trechos em itálico em 1917 (conferidos nas imagens); (trecho, de, até): só os tokens trecho[de:até]
ITALICOS = []

TROCAS_NOMES = []


def _toks(s):
    return TOK.findall(s)


def corrigir(out, flags):
    """Sobre o texto pronto (grafia de hoje): nomes uniformizados, blocos de versos e itálicos."""
    out, flags = list(out), list(flags)
    TROCAS_NOMES.clear()
    for i, t in enumerate(out):
        if t in NOMES:
            TROCAS_NOMES.append(t)
            out[i] = NOMES[t]
    for primeiro, n in VERSOS_BLOCOS:
        P = _toks(primeiro)
        achados = [i for i in range(1, len(out) - len(P)) if out[i - 1] == '¶' and out[i:i + len(P)] == P]
        if len(achados) != 1:
            raise SystemExit(f'versos {primeiro!r}: {len(achados)} ocorrências')
        i, k = achados[0], 1
        while k < n:
            i += 1
            if out[i] == '¶':
                out[i] = '/'
                k += 1
    falhas = []
    for item in ITALICOS:
        trecho, desde, ate = (item, 0, None) if isinstance(item, str) else item
        P = _toks(trecho)
        ate = len(P) if ate is None else ate
        achados = [i for i in range(len(out) - len(P) + 1) if out[i:i + len(P)] == P]
        if not achados:
            falhas.append(trecho)
        for a in achados:
            for k in range(a + desde, a + ate):
                flags[k] = flags[k] or out[k][:1].isalpha()
    if falhas:
        print('itálicos sem lugar:', falhas)
    return out, flags
