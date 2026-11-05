"""O Guardador de Rebanhos (Alberto Caeiro): monta conteudo/fernando-pessoa/o-guardador-de-rebanhos.js.

    python3 edicoes/o-guardador-de-rebanhos/montar.py        (na raiz do repositório)

Fonte: texto/NN.txt, um arquivo por poema (I a XLIX), já na grafia de hoje, com estas exceções que se
resolvem aqui: «cousa» fica nos arquivos como Pessoa a escreveu e sai «coisa» (regra do guia: nenhuma forma
arcaica de palavra atual; decisão 1 do revisao.json), e o «porque» das perguntas diretas sai «por que».
Cabeçalho de cada arquivo: «# numero:», «# base: athena|atica» (a edição seguida) e «# nota:» (o que se
conferiu e as diferenças). Ver FALTA.md e edicao.json.
"""
import glob, json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
GRAFIA = [(r'\bcous(a|as)\b', r'cois\1'), (r'\bCous(a|as)\b', r'Cois\1')]
CONTA = {'por que': []}


def por_que(t, onde):
    """«porque» de pergunta direta (antes do «?» da mesma frase) > «por que»."""
    def frase(m):
        s = m.group(0)
        if '?' not in s: return s
        def tr(x):
            CONTA['por que'].append((onde, s.strip().replace('\n', ' / ')[:90]))
            return x.group(1) + 'or que'
        return re.sub(r'(?<!\bo )\b([Pp])orque\b(?=[^.!]*\?)', tr, s)
    return re.sub(r'[^.!?]*[.!?]+', frase, t)


def poema(f):
    cab, estrofes, est = {}, [], []
    for l in open(f, encoding='utf-8').read().split('\n'):
        m = re.match(r'^# (\w+): ?(.*)$', l)
        if m:
            cab.setdefault(m.group(1), m.group(2).strip()); continue
        if not l.strip():
            if est: estrofes.append(est); est = []
            continue
        est.append(l.strip())
    if est: estrofes.append(est)
    t = '\n\n'.join('\n'.join(e) for e in estrofes)
    for a, b in GRAFIA: t = re.sub(a, b, t)
    t = por_que(t, cab['numero'])
    return cab, '\n\n'.join('\n'.join('| ' + v for v in e.split('\n')) for e in t.split('\n\n'))


arqs = sorted(glob.glob(os.path.join(AQUI, 'texto', '[0-9][0-9].txt')))
if len(arqs) != 49: raise SystemExit('esperava 49 poemas, achei %d' % len(arqs))
partes, bases = [], {}
for f in arqs:
    cab, t = poema(f)
    bases[cab['base']] = bases.get(cab['base'], 0) + 1
    partes.append({'n': cab['numero'], 'titulo': '', 'texto': t})
pal = sum(len(re.findall(r"[A-Za-zÀ-ÿ]+", p['texto'])) for p in partes)
obra = {'id': 'o-guardador-de-rebanhos', 'autor': 'fernando-pessoa', 'titulo': 'O Guardador de Rebanhos', 'ano': 1946,
        'genero': 'Poesia', 'divisao': {'singular': 'poema', 'plural': 'poemas'},
        'descricao': 'Os 49 poemas do ciclo de Alberto Caeiro, heterônimo de Fernando Pessoa. Pessoa publicou 23 deles na revista _Athena_ (1925); o ciclo inteiro saiu em livro em 1946.',
        '_palavras': pal, 'partes': partes,
        'edicao': json.load(open(os.path.join(AQUI, 'edicao.json'), encoding='utf-8'))}
js = ('/* O Guardador de Rebanhos — Alberto Caeiro (Fernando Pessoa). Gerado por edicoes/o-guardador-de-rebanhos/montar.py;\n'
      '   não edite à mão: corrija edicoes/o-guardador-de-rebanhos/texto/ e rode de novo. */\n'
      'BIBLIOTECA.obra(' + json.dumps(obra, ensure_ascii=False, indent=1) + ');\n')
open(os.path.join(RAIZ, 'conteudo', 'fernando-pessoa', 'o-guardador-de-rebanhos.js'), 'w', encoding='utf-8').write(js)
print(len(partes), 'poemas,', sum(p['texto'].count('| ') for p in partes), 'versos,', pal, 'palavras;', bases)
for x in CONTA['por que']: print('  por que:', *x)
