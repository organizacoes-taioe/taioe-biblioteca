"""Monta Primeiros Cantos (Gonçalves Dias, 1846) como obra da Biblioteca.

    python3 edicoes/primeiros-cantos/montar.py

Lê os 44 poemas do livro no corpus do Versificador (corpus/goncalves-dias/primeiros-cantos--NN-*.txt,
transcritos da 1ª edição, Laemmert, 1846, e já na ortografia de hoje), mais o prólogo do autor
(prologo.txt, desta pasta) e as notas do autor (notas.json, no fim de cada poema, como «¤ »), e grava conteudo/goncalves-dias/primeiros-cantos.js. A «Deprecação»
(05b) vai no fim, como apêndice: é a refundição da parte II de «O Morro do Alecrim» feita para as edições de Leipzig.
"""
import glob, json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from poesia import FONTE_PADRAO  # noqa: E402

SAIDA = os.path.join(RAIZ, 'conteudo', 'goncalves-dias', 'primeiros-cantos.js')
SOBRE = os.path.join(AQUI, 'sobre.md')


def ler_poema(caminho):
    cab, corpo = {}, []
    for l in open(caminho, encoding='utf-8').read().split('\n'):
        m = re.match(r'^# (\w+): ?(.*)$', l)
        if m and m.group(1) in ('titulo', 'autor', 'obra', 'fonte', 'ortografia', 'forma', 'nota'):
            cab[m.group(1)] = (cab.get(m.group(1), '') + ' ' + m.group(2).strip()).strip()
            continue
        corpo.append(l)
    blocos, est = [], []

    def fecha():
        if est:
            blocos.append('\n'.join('| ' + v.strip() for v in est))
            est.clear()
    for l in corpo:
        m = re.match(r'^# (\w+): ?(.*)$', l)
        if m:
            fecha()
            k, v = m.group(1), m.group(2).strip()
            if k == 'parte':
                blocos.append('## ' + v)
            elif k == 'epigrafe':
                linhas = [x.strip() for x in v.split(' / ')]
                blocos.append('\n'.join('| _' + x + '_' for x in linhas))
            elif k in ('dedicatoria', 'data'):
                blocos.append('_' + v + '_')
            elif k == 'separador':
                blocos.append('* * *')
            else:
                raise SystemExit('marca desconhecida: %s em %s' % (k, caminho))
        elif not l.strip():
            fecha()
        else:
            est.append(l)
    fecha()
    return cab, '\n\n'.join(blocos)


def main():
    fonte = os.environ.get('VERSIFICADOR') or FONTE_PADRAO
    if not os.path.isdir(fonte):  # worktree fora da pasta Geremias
        fonte = os.path.expanduser('~/Geremias/Solar/producao/versificador')
    arqs = sorted(glob.glob(os.path.join(fonte, 'corpus', 'goncalves-dias', 'primeiros-cantos--*.txt')))
    apendice = [a for a in arqs if '--05b-' in a]
    arqs = [a for a in arqs if '--05b-' not in a]
    if len(arqs) != 44 or len(apendice) != 1:
        raise SystemExit('esperava 44 poemas, achei %d' % len(arqs))
    partes = [{'n': '', 'titulo': 'Prólogo', 'texto': open(os.path.join(AQUI, 'prologo.txt'), encoding='utf-8').read().strip()}]
    notas = json.load(open(os.path.join(AQUI, 'notas.json'), encoding='utf-8'))
    usadas = set()
    for a in arqs:
        cab, texto = ler_poema(a)
        if cab['titulo'] in notas:
            usadas.add(cab['titulo'])
            texto += ''.join('\n\n¤ ' + n for n in notas[cab['titulo']])
        secao = cab['obra'].split(',', 1)[1].strip()
        partes.append({'n': '', 'titulo': cab['titulo'], 'secao': secao, 'texto': texto})
    falta = set(k for k in notas if not k.startswith('_')) - usadas
    if falta:
        raise SystemExit('notas sem poema: %s' % ', '.join(sorted(falta)))
    cab, texto = ler_poema(apendice[0])
    partes.append({'n': '', 'titulo': 'Apêndice: Deprecação (versão de 1857)', 'texto':
                   '_Nas edições de Leipzig (1857 em diante), o autor refundiu a segunda parte de «O Morro do Alecrim» '
                   'neste poema, que passou a se chamar «Deprecação». O texto é o de_ Cantos _(Leipzig, Brockhaus, 1860)._\n\n' + texto})
    sobre = open(SOBRE, encoding='utf-8').read().strip()
    obra = {
        'id': 'primeiros-cantos', 'autor': 'goncalves-dias', 'titulo': 'Primeiros Cantos', 'ano': 1846,
        'genero': 'Poesia', 'divisao': {'singular': 'poema', 'plural': 'poemas'},
        'edicao': {
            'base': '1ª edição, 1846',
            'apresentacao': sobre,
            'fontes': [
                {'nome': 'Primeiros Cantos, 1ª edição (Rio de Janeiro, Laemmert, 1846), fac-símile no Wikimedia Commons',
                 'url': 'https://commons.wikimedia.org/w/index.php?title=File:Primeiros_cantos-_poesias.pdf',
                 'nota': 'texto-base'},
                {'nome': 'Wikisource, Primeiros Cantos (transcrição da 1ª edição, em parte)',
                 'url': 'https://pt.wikisource.org/wiki/Primeiros_Cantos',
                 'nota': 'confrontada palavra por palavra; base do prólogo'},
                {'nome': 'Cantos: collecção de poesias (Leipzig, Brockhaus, 1860), no Internet Archive',
                 'url': 'https://archive.org/details/cantoscollecode00diasgoog',
                 'nota': 'conferência do prólogo; texto da «Deprecação»'},
            ],
        },
        'partes': partes,
    }
    cab = ('/* Primeiros Cantos — Gonçalves Dias\n'
           '   Gerado por edicoes/primeiros-cantos/montar.py. Não edite à mão: o texto dos poemas vem do\n'
           '   corpus do Versificador; o prólogo e a página «Sobre» ficam em edicoes/primeiros-cantos/.\n*/\n')
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    with open(SAIDA, 'w', encoding='utf-8') as f:
        f.write(cab + 'BIBLIOTECA.obra(' + json.dumps(obra, ensure_ascii=False, indent=1) + ');\n')
    print('gravado', os.path.relpath(SAIDA, RAIZ), len(partes), 'partes')


if __name__ == '__main__':
    main()
