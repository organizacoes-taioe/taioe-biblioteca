"""Poesias de Olavo Bilac (edição definitiva, Garnier, 1902): monta conteudo/olavo-bilac/poesias.js.

Fonte: os textos do corpus do Versificador (Solar/producao/versificador/corpus/bilac), transcritos das
imagens do fac-símile de 1902 (Brasiliana Mindlin, no Wikimedia Commons), copiados em texto/.
Aqui só se aplica a grafia de hoje nas formas com apóstrofo (d'essa > dessa, n'um > num,
outr'ora > outrora; ficam minh'alma, d'alma, d'água, que são elisão do verso) e as correções de ERROS.
Uso, na raiz do repositório: python3 edicoes/poesias-de-olavo-bilac/montar.py
"""
import json, os, re, glob
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
PARTES = [('panoplias', 'Panóplias'), ('via-lactea', 'Via Láctea'), ('sarcas-de-fogo', 'Sarças de Fogo'),
          ('alma-inquieta', 'Alma Inquieta')]  # as outras: ver FALTA.md
ERROS = {('panoplias--01', 'Que ofício tal.. nem há notícia'): 'Que ofício tal... nem há notícia'}
# grafia de hoje que o corpus não aplicou (por que nas perguntas, afora, trás, vazios, cor-de-rosa, campo-santo)
GRAFIA = {
    'alma-inquieta--03': [('Porque, para uma ignota', 'Por que, para uma ignota')],
    'alma-inquieta--13': [('corpo a fora', 'corpo afora')],
    'alma-inquieta--21': [('Campo Santo', 'Campo-Santo')],
    'alma-inquieta--23': [('Porque partir tão cedo?', 'Por que partir tão cedo?'), ('porque partir tão cedo?', 'por que partir tão cedo?'),
                          ('horizonte a fora', 'horizonte afora')],
    'alma-inquieta--26': [('lugares vasios', 'lugares vazios'), ('carne cor de rosa', 'carne cor-de-rosa')],
    'alma-inquieta--30': [('Para traz! para traz!', 'Para trás! para trás!')],
    'alma-inquieta--31': [('Porque, belo navio', 'Por que, belo navio')],
    'alma-inquieta--32': [('porque vieste?', 'por que vieste?')],
    'alma-inquieta--33': [('Porque é que', 'Por que é que'), ('Porque, fugindo', 'Por que, fugindo'), ('Porque me ouviste', 'Por que me ouviste')],
    'alma-inquieta--36': [('Porque me vens', 'Por que me vens'), ('Porque levantas', 'Por que levantas'), ('Porque, entre as sombras', 'Por que, entre as sombras')],
    'alma-inquieta--37': [('Olhos, porque inda', 'Olhos, por que inda'), ('Porque é que choro', 'Por que é que choro')],
}
FICAM = {"minh'alma", "d'alma", "d'água"}
ROM = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII',
       'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV']

def grafia(v):
    def tr(m):
        w = m.group(0)
        if w.lower() in FICAM: return w
        a, b = w.split("'")
        if a.lower() == 'outr': return a + b
        if a in ('E',) and b == '': return 'É'
        return a + b
    v = re.sub(r"\b[A-Za-zÀ-ÿ]+'[A-Za-zÀ-ÿ]*", tr, v)
    return v.replace('Gœthe', 'Goethe').replace('Luiz Guimarães', 'Luís Guimarães').replace('De Calderon', 'De Calderón')

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
        l = l.rstrip()
        if not l: linhas.append(''); continue
        if l.startswith('**'): linhas.append(l); continue
        l = ERROS.get((chave, l.strip()), l.strip())
        for de, para in GRAFIA.get(chave, []): l = l.replace(de, para)
        linhas.append('| ' + grafia(l))
    t = re.sub(r'\n{3,}', '\n\n', '\n'.join(linhas)).strip()
    t = re.sub(r'(\*\*[IVX]+\*\*)\n(?=\|)', r'\1\n\n', t)
    pre = []
    if 'subtitulo' in cab: pre.append('_' + cab['subtitulo'].strip('().') + '_')
    if 'dedicatoria' in cab: pre.append('_' + grafia(cab['dedicatoria']).rstrip('.') + '_')
    if 'epigrafe' in cab: pre.append('_' + cab['epigrafe'] + '_')
    if 'data' in cab: t += '\n\n_' + cab['data'] + '_'
    return cab, ('\n\n'.join(pre) + '\n\n' if pre else '') + t

partes, textos = [], []
for slug, nome in PARTES:
    for i, f in enumerate(sorted(glob.glob(os.path.join(AQUI, 'texto', slug + '--*.txt'))), 1):
        cab, t = poema(f)
        if slug == 'via-lactea':
            prim = next(l for l in t.split('\n') if l.startswith('| '))[2:].rstrip(' ,.;:')
            prim = prim.lstrip('—«» ')
            if prim.count('(') != prim.count(')'): prim = prim.split('(')[0].rstrip(' ,')
            tit = ROM[i] + ' · ' + prim
        else:
            tit = grafia(cab['titulo'])
        partes.append({'n': nome, 'titulo': tit}); textos.append(t)
pal = sum(len(re.findall(r"[A-Za-zÀ-ÿ]+", t)) for t in textos)
obra = {'id': 'poesias-de-olavo-bilac', 'autor': 'olavo-bilac', 'titulo': 'Poesias', 'ano': 1902, 'genero': 'Poesia',
        'divisao': {'singular': 'poema', 'plural': 'poemas', 'rotulo': 'titulo', 'agrupar': True},
        'descricao': 'A edição definitiva em vida (Garnier, 1902). Por enquanto, as quatro primeiras partes: _Panóplias_, _Via Láctea_, _Sarças de Fogo_ e _Alma Inquieta_.',
        '_palavras': pal, 'partes': partes,
        'edicao': json.load(open(os.path.join(AQUI, 'edicao.json'), encoding='utf-8'))}
js = ('/* Poesias — Olavo Bilac (1902). Gerado por edicoes/poesias-de-olavo-bilac/montar.py; não edite à mão. */\n'
      'BIBLIOTECA.obra(' + json.dumps(obra, ensure_ascii=False) + ');\n'
      'BIBLIOTECA.textos(' + json.dumps({'poesias-de-olavo-bilac': {'t': textos}}, ensure_ascii=False) + ');\n')
open(os.path.join(RAIZ, 'conteudo', 'olavo-bilac', 'poesias.js'), 'w', encoding='utf-8').write(js)
print(len(partes), 'poemas,', pal, 'palavras')
