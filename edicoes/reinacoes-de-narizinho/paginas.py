"""Reinações de Narizinho (1931): o texto de cada página do fac-símile, pela transcrição do Wikisource.

    python3 -I edicoes/reinacoes-de-narizinho/paginas.py      (na raiz do repositório)

Lê as páginas «Página:As Reinações de Narizinho.pdf/N» (baixadas por ferramentas/edicao/fontes.py para
ferramentas/cache/reinacoes-de-narizinho/wikisource_paginas.json) e grava em 1931/paginas.json, para cada
página do PDF (9–320), o texto na grafia de 1931 numa marcação simples:
  «### título»       abre uma história (o título como no índice de 1931)
  «## N — título»    abre um capítulo
  «| linha»          linha de um bloco centrado (bilhetes, letreiros, o programa do circo)
  _itálico_
  parágrafos separados por linha em branco; «+» no começo da página = o parágrafo continua da anterior.
As páginas sem texto (ilustrações) não entram. As pp. 249 e 282 do livro (PDF 260 e 294) faltam no
fac-símile do Museu Monteiro Lobato: o Wikisource as preencheu com o texto de outra edição (ver FALTA.md).
"""
import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
WS = os.path.join(RAIZ, 'ferramentas', 'cache', 'reinacoes-de-narizinho', 'wikisource_paginas.json')

HISTORIAS = ['NARIZINHO ARREBITADO', 'O SITIO DO PICAPAU AMARELLO', 'O MARQUEZ DE RABICÓ', 'O CASAMENTO DE NARIZINHO',
             'AVENTURAS DO PRINCIPE', 'O GATO FELIX', 'CARA DE CORUJA', 'O IRMÃO DE PINOCCHIO',
             'O CIRCO DE ESCAVALLINHO', 'A PENNA DE PAPAGAIO', 'O PÓ DE PIRLIMPIMPIM']
# títulos de história como o Wikisource os transcreve, quando diferem do índice de 1931 (ver conferencia)
HISTORIA_WS = {'O CIRCO DE DE ESCAVALLINHO': 'O CIRCO DE ESCAVALLINHO'}
CAP = re.compile(r'^([IVXL]+)\s*[—―-]\s*(.+)$')


def _limpar_modelos(t):
    t = re.sub(r'\{\{PT\|\|[^{}]*\}\}', '\u0008', t)         # o resto da palavra que fica na página seguinte: juntar
    t = re.sub(r'\{\{PT\|([^{}|]*)\}\}', r'\1', t)
    t = re.sub(r'\{\{(?:dropinitial|capitular)\|([^{}]*)\}\}', r'\1', t)
    t = re.sub(r'\{\{--\}\}', '—', t)
    t = re.sub(r'\{\{(?:nop|NOP)\}\}', '\u0006', t)            # fim de parágrafo no fim da página
    t = re.sub(r'\{\{(?:gap|dhr|rule)(?:\|[^{}]*)?\}\}', '', t)
    t = re.sub(r'\{\{(?:smaller|larger|w|letter-spacing\|[^|{}]*)\|([^{}]*)\}\}', r'\1', t)
    return t


def _centrado(s):
    s = s.replace('\u0007', '\n')
    return ['| ' + l.strip() for l in s.split('\n') if l.strip()]


def pagina(bruto):
    """(texto, continua) de uma página."""
    t = re.sub(r'<noinclude>.*?</noinclude>', '', bruto, flags=re.S)
    continua = not re.match(r'\s*\n\s*\n', t) and not t.lstrip().startswith(('{{t2', '{{T2', '{{t3', '<center>'))
    t = re.sub(r'<br\s*/?>', '\u0007', t)
    t = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', t)      # [[:w:pt:Pixoxó|pichochó]] -> pichochó
    t = re.sub(r'(?m)^:+', '\n', t)          # cartas recuadas (pp. 65 e 97 do livro): um parágrafo por linha
    t = _limpar_modelos(t)
    for _ in range(3):
        t = _limpar_modelos(t)
    blocos = []
    # tabelas (os bilhetes do circo, p. 230 do livro): o miolo, sem a moldura
    t = re.sub(r'\{\|.*?\n\|\}', lambda m: '\n\n' + re.sub(r'^(?:\{\||\|\}|\|)\s*$', '', re.sub(r'^\{\|.*$', '', m.group(0), flags=re.M), flags=re.M) + '\n\n', t, flags=re.S)
    # cabeçalhos e blocos centrados viram linhas próprias
    t = re.sub(r'<center><p[^>]*>(.*?)</p></center>', lambda m: '\n\n\u0001' + m.group(1) + '\n\n', t, flags=re.S)
    t = re.sub(r'\{\{(?:t2|T2|t3)\|(.*?)(?:\|sp=[^}]*)?\}\}', lambda m: '\n\n\u0001' + m.group(1) + '\n\n', t)
    t = re.sub(r'\{\{(?:c|C|right|left)\|((?:[^{}]|\{\{[^{}]*\}\})*)\}\}', lambda m: '\n\n\u0002' + m.group(1) + '\n\n', t)
    t = re.sub(r'\{\{cabeçalho\|([^{}]*)\}\}', lambda m: '\n\n\u0002' + '   '.join(x for x in m.group(1).split('|') if x) + '\n\n', t)
    t = re.sub(r'\{\{tabela[^{}]*?título\s*=\s*([^|{}]*?)\s*\|\s*página\s*=\s*([^|{}]*?)\s*\}\}',
               lambda m: '\n\n\u0002' + m.group(1) + ' — ' + m.group(2) + '\n\n', t, flags=re.S)
    t = t.replace("'''", '')
    t = re.sub(r"''(.*?)''", r'_\1_', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '', t)
    if '{{' in t:
        raise SystemExit('modelo não tratado: ' + t[t.index('{{'):t.index('{{') + 60])
    fim_par = '\u0006' in t or not t.rstrip().endswith(('-',)) and False
    t = t.replace('\u0006', '\n\n\u0006')
    for b in re.split(r'\n\s*\n', t):
        b = b.strip()
        if not b:
            continue
        if b == '\u0008':
            blocos.append('\u0008'); continue
        if b == '\u0006':
            blocos.append('\u0006'); continue
        if b.startswith('\u0001'):
            h = re.sub(r'\s+', ' ', b[1:].replace('_', '')).strip()
            h = HISTORIA_WS.get(h, h)
            if h in HISTORIAS:
                blocos.append('### ' + h)
            elif CAP.match(h):
                m = CAP.match(h)
                blocos.append(f'## {m.group(1)} — {m.group(2).strip()}')
            elif h == 'O CASAMENTO':                       # capítulo sem número em «O Marquez de Rabicó»
                blocos.append('## — O CASAMENTO')
            else:
                blocos.extend(_centrado(h) if h else [])
                blocos.append('')
            continue
        if b.startswith('\u0002'):
            blocos.append('\n'.join(_centrado(b[1:])))
            continue
        b = re.sub(r'(?<=\w)-\u0007', '', b).replace('\u0007', ' ')      # linhas de uma carta: palavra partida
        blocos.append(re.sub(r'\s*\n\s*', ' ', b))
    # junta linhas centradas seguidas num bloco só
    out = []
    for b in blocos:
        if b == '':
            continue
        if b.startswith('| ') and out and out[-1].startswith('| '):
            out[-1] += '\n' + b
        else:
            out.append(b)
    fecha = bool(out) and out[-1] == '\u0006'
    out = [b for b in out if b != '\u0006']
    t = '\n\n'.join(out)
    return t, continua, fecha


def main():
    p = {int(k): v for k, v in json.load(open(WS, encoding='utf-8')).items()}
    res = {}
    for n in range(9, 321):
        if n not in p or p[n]['qualidade'] == 0:
            continue
        texto, continua, fecha = pagina(p[n]['texto'])
        if not texto:
            continue
        res[n] = {'texto': texto, 'continua': continua, 'fecha': fecha, 'qualidade': p[n]['qualidade']}
    os.makedirs(os.path.join(AQUI, '1931'), exist_ok=True)
    json.dump(res, open(os.path.join(AQUI, '1931', 'paginas.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cab = [(n, l) for n, v in res.items() for l in v['texto'].split('\n\n') if l.startswith('#')]
    for n, l in cab:
        print(n, l)
    print(len(res), 'páginas')


if __name__ == '__main__':
    main()
