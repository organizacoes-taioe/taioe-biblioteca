"""Broquéis (Cruz e Sousa, 1893): monta conteudo/cruz-e-sousa/broqueis.js.

    python3 edicoes/broqueis/montar.py        (na raiz do repositório)

Fonte: texto/, cópia dos 54 poemas do corpus do Versificador (Solar/producao/versificador/corpus/cruz-e-sousa),
que é a transcrição validada do Wikisource (Livro:Broqueis.pdf, o fac-símile da 1ª edição) posta na grafia de hoje.
Na cópia foram restituídas as lições de 1893 que o corpus tinha perdido (ver FALTA.md); aqui só se aplicam a grafia
das contrações com apóstrofo (d'entre > dentre, n'um > num, outr'ora > outrora; ficam as elisões do verso:
minh'alma, tu'alma, d'ouro, d'Ela, c'roado...) e as correções de ERROS (erros de composição de 1893).
"""
import json, os, re, glob
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
# erros de composição de 1893 (a lição impressa vai na «Sobre», em edicao.json)
ERROS = {('broqueis--21', 'E solta ao sóis e estranha e ondeada e espessa'): 'E solta aos sóis e estranha e ondeada e espessa'}
# contrações com apóstrofo que têm forma de hoje numa palavra só
JUNTAR = {"d'entre": 'dentre', "d'aquele": 'daquele', "d'aquela": 'daquela', "n'um": 'num', "n'uma": 'numa', "n'ela": 'nela',
          "n'ele": 'nele', "outr'ora": 'outrora', "d'este": 'deste', "d'esta": 'desta', "d'esse": 'desse', "d'essa": 'dessa'}
EPIGRAFE = ('_Seigneur, mon Dieu! accordez-moi la grâce de produire quelques beaux vers qui me prouvent à moi-même que je ne '
            'suis pas le dernier des hommes, que je ne suis pas inférieur à ceux que je méprise._\n\n_Baudelaire_')


def grafia(v):
    def tr(m):
        w = m.group(0)
        j = JUNTAR.get(w.lower())
        if not j: return w
        return j[0].upper() + j[1:] if w[0].isupper() else j
    return re.sub(r"\b[A-Za-zÀ-ÿ]+'[A-Za-zÀ-ÿ]+", tr, v)


def poema(f):
    cab, corpo = {}, []
    for l in open(f, encoding='utf-8').read().split('\n'):
        m = re.match(r'# (\w+): (.*)', l)
        if m and m.group(1) == 'parte': corpo.append('**' + m.group(2) + '**'); continue
        if m: cab.setdefault(m.group(1), m.group(2)); continue
        corpo.append(l)
    chave = re.match(r'(.+?--\d+)', os.path.basename(f)).group(1)
    linhas = []
    for l in corpo:
        l = l.strip()
        if not l: linhas.append(''); continue
        if l.startswith('**'): linhas.append(l); continue
        l = ERROS.get((chave, l), l)
        linhas.append('| ' + grafia(l))
    t = re.sub(r'\n{3,}', '\n\n', '\n'.join(linhas)).strip()
    t = re.sub(r'(\*\*[IVX]+\*\*)\n(?=\|)', r'\1\n\n', t)
    return cab, t


arqs = sorted(glob.glob(os.path.join(AQUI, 'texto', 'broqueis--*.txt')))
if len(arqs) != 54: raise SystemExit('esperava 54 poemas, achei %d' % len(arqs))
partes = []
for i, f in enumerate(arqs):
    cab, t = poema(f)
    if i == 0: t = EPIGRAFE + '\n\n' + t   # a epígrafe do livro (Baudelaire), antes da «Antífona»
    partes.append({'n': '', 'titulo': cab['titulo'], 'texto': t})
pal = sum(len(re.findall(r"[A-Za-zÀ-ÿœ]+", p['texto'])) for p in partes)
obra = {'id': 'broqueis', 'autor': 'cruz-e-sousa', 'titulo': 'Broquéis', 'ano': 1893, 'genero': 'Poesia',
        'divisao': {'singular': 'poema', 'plural': 'poemas'},
        'descricao': 'O livro de estreia de Cruz e Sousa na poesia e o marco inicial do Simbolismo no Brasil: 54 poemas, quase todos sonetos.',
        '_palavras': pal, 'partes': partes,
        'edicao': json.load(open(os.path.join(AQUI, 'edicao.json'), encoding='utf-8'))}
js = ('/* Broquéis — Cruz e Sousa (1893). Gerado por edicoes/broqueis/montar.py; não edite à mão:\n'
      '   corrija edicoes/broqueis/texto/ e rode de novo. */\n'
      'BIBLIOTECA.obra(' + json.dumps(obra, ensure_ascii=False, indent=1) + ');\n')
open(os.path.join(RAIZ, 'conteudo', 'cruz-e-sousa', 'broqueis.js'), 'w', encoding='utf-8').write(js)
print(len(partes), 'poemas,', sum(p['texto'].count('| ') for p in partes), 'versos,', pal, 'palavras')
