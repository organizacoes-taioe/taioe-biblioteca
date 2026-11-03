"""Lira dos Vinte Anos (Álvares de Azevedo): monta conteudo/alvares-de-azevedo/lira-dos-vinte-anos.js.

    python3 edicoes/lira-dos-vinte-anos/montar.py        (na raiz do repositório)

Fonte: texto/, um arquivo por poema no formato do corpus do Versificador: os 37 que já estavam no corpus
(Solar/producao/versificador/corpus/alvares-de-azevedo, copiados sem mudança) e os 48 que faltavam, estabelecidos
aqui sobre os fac-símiles (1ª e 2ª parte pela 1ª edição, 1853; a 3ª pelo tomo III de 1862, onde saiu pela primeira
vez), mais o prefácio da 2ª parte (prefacio-segunda-parte.txt). Ver FALTA.md e edicao.json.
Aqui só se aplicam a grafia das contrações com apóstrofo que têm forma de hoje (n'um > num, d'ela > dela; ficam as
elisões do verso: minh'alma, d'alma, d'oiro, co'a, p'ra…), «por que» nas perguntas e as formas de GRAFIA.
"""
import glob, json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
PARTES = {0: '', 1: 'Primeira parte', 2: 'Segunda parte', 3: 'Terceira parte'}
JUNTAR = {"n'um": 'num', "n'uma": 'numa', "n'uns": 'nuns', "n'umas": 'numas', "d'ela": 'dela', "d'elas": 'delas',
          "d'ele": 'dele', "d'eles": 'deles', "n'ela": 'nela', "n'ele": 'nele', "d'aquele": 'daquele', "d'aquela": 'daquela',
          "d'aqueles": 'daqueles', "d'aquelas": 'daquelas', "outr'ora": 'outrora', "n'esta": 'nesta', "n'este": 'neste',
          "n'essa": 'nessa', "n'esse": 'nesse', "d'esta": 'desta', "d'este": 'deste', "d'essa": 'dessa', "d'esse": 'desse',
          "d'estes": 'destes', "d'estas": 'destas', "d'esses": 'desses', "d'essas": 'dessas', "d'entre": 'dentre',
          "n'aquele": 'naquele', "n'aquela": 'naquela', "d'antes": 'dantes', "d'outro": 'doutro', "d'outra": 'doutra',
          "n'outro": 'noutro', "n'outra": 'noutra', "d'aqui": 'daqui', "d'ali": 'dali', "d'onde": 'donde', "d'isso": 'disso',
          "d'isto": 'disto', "n'isso": 'nisso', "n'isto": 'nisto'}
# formas antigas de palavra de hoje e uniformizações (o resto já vem resolvido em texto/)
GRAFIA = [(r'\bcous(a|as)\b', r'cois\1'), (r'\bCous(a|as)\b', r'Cois\1'), (r'\bdous\b', 'dois'), (r'\bDous\b', 'Dois'),
          (r'\bdoud(o|a|os|as)\b', r'doid\1'), (r'\bDoud(o|a|os|as)\b', r'Doid\1'), (r'\blangor\b', 'languor')]


def juntar(v):
    def tr(m):
        w = m.group(0)
        j = JUNTAR.get(w.lower())
        if not j: return w
        return j[0].upper() + j[1:] if w[0].isupper() else j
    v = re.sub(r"\b[A-Za-zÀ-ÿ]+'[A-Za-zÀ-ÿ]+", tr, v)
    for a, b in GRAFIA: v = re.sub(a, b, v)
    return v


def por_que(t):
    """«porque» de pergunta direta (antes do «?» da mesma frase) > «por que»."""
    def frase(m):
        s = m.group(0)
        if '?' not in s: return s
        return re.sub(r'(?<!\bo )\b([Pp])orque\b(?=[^.!]*\?)', lambda x: x.group(1) + 'or que', s)
    return re.sub(r'[^.!?]*[.!?]+', frase, t)


def epigrafe(v):
    m = re.match(r'(.*?)\s*\(([^()]*)\)\s*$', v)
    texto, autor = (m.group(1), m.group(2)) if m else (v, '')
    ls = ['| _' + x.strip() + '_' for x in texto.split(' / ') if x.strip()]
    if autor: ls.append('| — ' + autor)
    return '\n'.join(ls)


def poema(f):
    cab, blocos, est, visto_verso = {}, [], [], False
    pre = []

    def fecha():
        if est:
            blocos.append('\n'.join('| ' + juntar(x) for x in est)); est.clear()
    for l in open(f, encoding='utf-8').read().split('\n'):
        m = re.match(r'^# (\w+):? ?(.*)$', l)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if k in ('titulo', 'autor', 'obra', 'fonte', 'ortografia', 'forma', 'nota'):
                cab.setdefault(k, v); continue
            alvo = blocos if (visto_verso or blocos) else pre
            fecha()
            if k == 'epigrafe': alvo.append(epigrafe(v))
            elif k in ('dedicatoria', 'subtitulo', 'data'): alvo.append('_' + juntar(v) + '_')
            elif k == 'parte': blocos.append('**' + v + '**')
            elif k == 'fala': blocos.append('@ ' + v)
            elif k == 'cena': blocos.append('## ' + juntar(v))
            elif k == 'lacuna': blocos.append('| . . . . . . . . . . . . . . .')
            else: raise SystemExit('marca desconhecida: %s em %s' % (k, f))
            continue
        if not l.strip(): fecha(); continue
        est.append(l.strip()); visto_verso = True
    fecha()
    grupo = re.search(r'(Hinos do profeta|Spleen e charutos), ([IVX]+)', cab.get('obra', ''))
    if grupo: pre.insert(0, '_' + grupo.group(1) + ' · ' + grupo.group(2) + '_')
    return cab, por_que('\n\n'.join(pre + blocos))


arqs = sorted(glob.glob(os.path.join(AQUI, 'texto', 'lira-dos-vinte-anos--*.txt')))
if len(arqs) != 86: raise SystemExit('esperava 86 arquivos (dedicatória e 85 poemas), achei %d' % len(arqs))
partes = []
for f in arqs:
    n = int(re.search(r'--(\d+)-', f).group(1))
    parte = 0 if n == 0 else 1 if n <= 36 else 2 if n <= 47 else 3
    cab, t = poema(f)
    if n == 38:   # o prefácio da segunda parte vem antes do primeiro poema dela
        pref = open(os.path.join(AQUI, 'texto', 'prefacio-segunda-parte.txt'), encoding='utf-8').read().strip()
        partes.append({'n': PARTES[2], 'titulo': 'Prefácio', 'texto': por_que(juntar(pref))})
    partes.append({'n': PARTES[parte], 'titulo': cab['titulo'], 'texto': t})
pal = sum(len(re.findall(r"[A-Za-zÀ-ÿœæ]+", p['texto'])) for p in partes)
obra = {'id': 'lira-dos-vinte-anos', 'autor': 'alvares-de-azevedo', 'titulo': 'Lira dos Vinte Anos', 'ano': 1853,
        'genero': 'Poesia', 'divisao': {'singular': 'poema', 'plural': 'poemas', 'rotulo': 'titulo', 'agrupar': True},
        'descricao': 'O livro de poemas de Álvares de Azevedo, publicado depois da sua morte: as duas partes da 1ª edição (1853) e a terceira, de inéditos, acrescentada em 1862.',
        '_palavras': pal, 'partes': partes,
        'edicao': json.load(open(os.path.join(AQUI, 'edicao.json'), encoding='utf-8'))}
js = ('/* Lira dos Vinte Anos — Álvares de Azevedo (1853; 3ª parte, 1862). Gerado por edicoes/lira-dos-vinte-anos/montar.py;\n'
      '   não edite à mão: corrija edicoes/lira-dos-vinte-anos/texto/ e rode de novo. */\n'
      'BIBLIOTECA.obra(' + json.dumps(obra, ensure_ascii=False, indent=1) + ');\n')
open(os.path.join(RAIZ, 'conteudo', 'alvares-de-azevedo', 'lira-dos-vinte-anos.js'), 'w', encoding='utf-8').write(js)
print(len(partes), 'partes,', sum(p['texto'].count('| ') for p in partes), 'linhas de verso,', pal, 'palavras')
