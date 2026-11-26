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
