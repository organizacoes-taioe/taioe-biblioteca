"""Diário Íntimo (Lima Barreto): da transcrição da Biblioteca Nacional (fontes/bn2002.txt, que segue a edição de
1956), corrigida pela conferência com o fac-símile de 1956 (correcoes.tsv), ao texto do site, na grafia do
Acordo de 1990.

  python3 -I edicoes/diario-intimo/montar.py              relatórios em edicoes/diario-intimo/relatorios/ (fora do git)
  python3 -I edicoes/diario-intimo/montar.py --publicar   grava conteudo/lima-barreto/diario-intimo.js

Fica de fora tudo o que é do organizador (Francisco de Assis Barbosa): a nota prévia, as notas de cada ano, as
chamadas delas no texto, as rubricas «Sem data» e o subtítulo da primeira versão de Clara dos Anjos."""
import collections
import csv
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao.grafia import ao1990  # noqa: E402

nfc = lambda s: unicodedata.normalize('NFC', s)

# partes do site: título → anos (ou o capítulo da primeira versão de Clara dos Anjos)
PARTES = [
    ('1900', ['1900']), ('1903', ['1903']), ('1904', ['1904']), ('1905', ['1905']),
    ('1906 e 1907', ['1906', '1907']), ('1908', ['1908']), ('1910', ['1910']), ('1911', ['1911']),
    ('1912 a 1915', ['1912', '1913', '1914', '1915']), ('1916', ['1916']), ('1917', ['1917']),
    ('1918', ['1918']), ('1919', ['1919']), ('1920 e 1921', ['1920', '1921']),
    ('Clara dos Anjos, I', ['CA-I']), ('Clara dos Anjos, II', ['CA-II']), ('Clara dos Anjos, III', ['CA-III']),
    ('Clara dos Anjos, IV', ['CA-IV']),
]

# Acordo de 1990: palavras com hífen que se juntam; nomes de pessoas e palavras estrangeiras que não mudam
HIFEN = {'anti-sociais': 'antissociais', 'contra-regra': 'contrarregra', 'pseudo-revolucionário': 'pseudorrevolucionário',
         'semi-agitada': 'semiagitada', 'semi-embriaguez': 'semiembriaguez', 'semi-feminino': 'semifeminino',
         'semi-feriado': 'semiferiado', 'semi-mancebia': 'semimancebia', 'semi-século': 'semisséculo',
         'semi-ébrio': 'semiébrio'}
FICA = {'Méier', 'Pompéia'}


def blocos_fonte():
    return nfc(open(os.path.join(AQUI, 'fontes', 'bn2002.txt'), encoding='utf-8').read()).split('\n\n')


def correcoes():
    """correcoes.tsv: bloco, posição, de, para, motivo (linha com # é comentário). A posição é a do «de» no bloco
    original de fontes/bn2002.txt; «*» procura o «de», que tem de aparecer uma vez só. «para» vazio apaga.
    Bloco «-»: só entra na lista de erros de 1956 da página «Sobre» (o texto de 2002 já está certo)."""
    out = collections.defaultdict(list)
    arq = os.path.join(AQUI, 'correcoes.tsv')
    for c in csv.reader(open(arq, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        if not c or c[0].startswith('#') or c[0] in ('bloco', '-'):
            continue
        out[int(c[0])].append((c[1], nfc(c[2]).replace('\\n', '\n'), nfc(c[3]).replace('\\n', '\n'), c[4] if len(c) > 4 else ''))
    return out


def corrigir(bl):
    corr = correcoes()
    novos = []
    for i, b in enumerate(bl):
        fixas = sorted([x for x in corr.get(i, []) if x[0] != '*'], key=lambda x: (-int(x[0]), not x[1]))
        for pos, de, para, _ in fixas:
            p = int(pos)
            if b[p:p + len(de)] != de:
                raise SystemExit(f'correcoes.tsv: bloco {i}, posição {p}: esperava «{de}», achou «{b[p:p + len(de)]}»')
            b = b[:p] + para + b[p + len(de):]
        for pos, de, para, _ in [x for x in corr.get(i, []) if x[0] == '*']:
            q = b.count(de)
            if q != 1:
                raise SystemExit(f'correcoes.tsv: bloco {i}: «{de}» aparece {q} vezes')
            b = b.replace(de, para)
        novos.append(b)
    return [b for b in novos if b.strip()]


def pontuacao_1956(s):
    """Regras de pontuação da transcrição de 2002 que a edição de 1956 não segue."""
    s = re.sub(r'([?!…]|\.\.\.)»\.', r'\1»', s)               # «… cor?». → «… cor?»
    s = re.sub(r'\betc\.,\s*etc', 'etc. etc', s)
    s = re.sub(r'(\b[IVXLC]+|\b\d+[ºª]?)\.-\s?', r'\1 — ', s)   # «Capítulo III.- A festa» → «Capítulo III — A festa»
    return s


def travessoes(s):
    """A transcrição de 2002 (na Cervantes) troca o travessão por hífen: é travessão o que não está entre letras."""
    s = re.sub(r'(?<![0-9A-Za-zÀ-ÿ])-|-(?![0-9A-Za-zÀ-ÿ])', '—', s)
    s = re.sub(r'[ \t]*—[ \t]*', ' — ', s)                   # espaço dos dois lados, como em 1956
    s = re.sub(r'(^|\n|[«(\[]) — ', lambda m: m.group(1) + '— ', s)
    s = re.sub(r' — ([,.;:!?»)])', r' —\1', s)
    return '\n'.join(l.rstrip() for l in s.split('\n'))


PAL = re.compile(r"[A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)*")


def grafia(s, rel):
    def um(m):
        w = m.group(0)
        if w.lower() in HIFEN:
            n = HIFEN[w.lower()]
            n = n[0].upper() + n[1:] if w[0].isupper() else n
        elif w in FICA:
            return w
        else:
            n = '-'.join(ao1990(p) for p in w.split('-'))
        if n != w:
            rel[(w, n)] += 1
        return n
    # o que está em língua estrangeira fica (itálicos com palavras francesas, inglesas etc. são do autor)
    return PAL.sub(um, s)


ESTRANGEIRO = re.compile(r"\b(le|la|les|des|du|une|est|the|of|and|el|los|que|qui|et|il|ne|pas|à|sont|dans)\b")


def grafia_bloco(b, rel):
    # trechos em itálico com cara de língua estrangeira não passam pelo Acordo
    pedacos = re.split(r'(_[^_]+_)', b)
    out = []
    for p in pedacos:
        if p.startswith('_') and len(ESTRANGEIRO.findall(p)) >= 2:
            out.append(p)
        else:
            out.append(grafia(p, rel))
    return ''.join(out)


def site(bl):
    """Os blocos da transcrição na marcação do site, agrupados por ano: {ano: [blocos]} e a ordem dos anos."""
    anos, ordem, atual = collections.OrderedDict(), [], 'cabeça'
    anos[atual] = []
    pend = []          # bloco de versos/citação em construção (linhas «| »)

    def solta():
        if pend:
            anos[atual].append('\n'.join(pend))
            pend.clear()
    for b in bl:
        if b.startswith('#ANO '):
            solta()
            atual = b[5:].strip()
            if atual.startswith('Clara dos Anjos'):
                atual = 'CA'
            anos[atual] = []
            continue
        if atual.startswith('CA'):
            m = re.fullmatch(r'## [-—] ([IV]+) [-—]', b)
            if m:
                solta()
                atual = 'CA-' + m.group(1)
                anos[atual] = []
                continue
        if b == '## Lima Barreto' or b == '## Sem data' or b.lower().startswith('primeira versão incompleta'):
            solta()
            continue
        if b.startswith('q: '):
            pend.extend('| ' + x for x in b[3:].split('\n'))
            continue
        if b.startswith('= '):
            pend.extend('| ' + x for x in b[2:].split('\n'))
            solta()
            continue
        if b.startswith('| ') or b == '|':
            solta()
            estrofes = re.split(r'\n\|\n?', b)
            for e in estrofes:
                linhas = [x for x in e.split('\n') if x.strip() not in ('', '|')]
                if linhas:
                    anos[atual].append('\n'.join(l if l.startswith('| ') else '| ' + l for l in linhas))
            continue
        if b.startswith('t: '):
            solta()
            linhas = []
            for x in b.split('\n'):
                cel = [c.strip() for c in x[3:].split('|')]
                cel = [c for c in cel if c]
                if not cel or all(re.fullmatch(r'_+', c) for c in cel):
                    linhas.append('| ————')
                else:
                    linhas.append('| ' + ' — '.join(cel))
            anos[atual].append('\n'.join(linhas))
            continue
        if b.startswith('-'):
            m = re.match(r'(-+) (.*)', b, re.S)
            pend.append('| ' + ('– ' if len(m.group(1)) > 1 else '') + m.group(2))
            continue
        solta()
        if b == '* * *':
            anos[atual].append('## * * *')
        elif b == '....':
            anos[atual].append('## . . . . . . . . . .')
        elif b.startswith('## '):
            anos[atual].append(b)
        elif b.startswith('>> '):
            x = b[3:]
            if re.fullmatch(r'\d{1,2} de [a-zç]+', x):
                anos[atual].append('## ' + x)            # data
            else:
                anos[atual].append('\n'.join('| ' + l for l in x.split('\n')) if '\n' in x else x)
        else:
            anos[atual].append(b.replace('\n', ' '))
    solta()
    return anos


def gerar():
    rel = collections.Counter()
    bl = [travessoes(pontuacao_1956(b)) if not b.startswith(('#ANO', 't: ')) else b for b in corrigir(blocos_fonte())]
    bl = [grafia_bloco(b, rel) for b in bl]
    anos = site(bl)
    partes = []
    cabeca = anos.pop('cabeça')
    for titulo, chaves in PARTES:
        bs = []
        for k in chaves:
            if len(chaves) > 1:
                bs.append('## ' + k)
            if k == 'CA-I':
                bs += anos.pop('CA')          # a epígrafe de Taine, antes do capítulo I
            bs += anos.pop(k)
        if titulo == '1900':
            bs = cabeca + bs
        # separador no começo ou no fim, ou dois seguidos, não fazem sentido
        limpo = []
        for b in bs:
            if b == '## * * *' and (not limpo or limpo[-1] == '## * * *' or re.fullmatch(r'## \d{4}', limpo[-1])):
                continue
            limpo.append(b)
        while limpo and limpo[-1] == '## * * *':
            limpo.pop()
        partes.append((titulo, limpo))
    if anos:
        raise SystemExit(f'sobrou: {list(anos)}')
    return partes, rel


if __name__ == '__main__':
    partes, rel = gerar()
    os.makedirs(os.path.join(AQUI, 'relatorios'), exist_ok=True)
    with open(os.path.join(AQUI, 'relatorios', 'grafia.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), c in sorted(rel.items()):
            f.write(f'{a}\t{b}\t{c}\n')
    with open(os.path.join(AQUI, 'relatorios', 'texto.txt'), 'w', encoding='utf-8') as f:
        for t, bs in partes:
            f.write(f'\n\n######## {t}\n\n' + '\n\n'.join(bs))
    pal = lambda bs: sum(len(re.findall(r'[A-Za-zÀ-ÿ0-9]+', b)) for b in bs)
    for t, bs in partes:
        print(f'{t}: {pal(bs)} palavras')
    print('total', sum(pal(bs) for _, bs in partes))
    if '--publicar' in sys.argv:
        sys.path.insert(0, AQUI)
        import publicar
        publicar.gravar(partes)
