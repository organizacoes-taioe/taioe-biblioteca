"""Pau Brasil (Oswald de Andrade, 1925): monta conteudo/oswald-de-andrade/pau-brasil.js.

    python3 edicoes/pau-brasil/montar.py        (na raiz do repositório)

Fonte: original/pau-brasil-1925.txt, o texto da 1ª edição (Paris, Au Sans Pareil, 1925) na grafia do livro,
conferido nas imagens da Brasiliana (ver FALTA.md). Formato:
    =p Título      parte em prosa (parágrafo por linha; «| » = verso citado; «> » = data e assinatura)
    = Título       parte em verso (estrofes separadas por linha em branco; espaços no começo = recuo)
    § Nome         seção do livro (as partes seguintes levam esse nome no índice)
    == Título      título de poema dentro da parte (História do Brasil: um cronista por parte)
    ~ texto        linha em itálico (dedicatória, subtítulo)
    ⁂              o asterismo da Falação
Passos: CORRECOES (erros evidentes da composição de 1925, listados na página «Sobre») → grafia de hoje palavra a
palavra pela tabela grafia.tsv (tabela.py) → FRASES (compostos e grafias de mais de uma palavra) → LINHAS (versos
que pedem decisão caso a caso: «tem» / «têm»). Os versos em outra língua (ESTRANGEIRAS) ficam como impressos.
"""
import json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
NBSP = '\u00a0'

# erros evidentes da composição de 1925 (o livro foi composto em Paris): (impresso, corrigido, onde)
CORRECOES = [
    ('da nossa nacionalidades', 'da nossa nacionalidade', 'Poesia Pau Brasil'),
    ('num deperdicio lamentavel', 'num desperdicio lamentavel', 'Poesia Pau Brasil'),
    ('Como Nietsche', 'Como Nietzsche', 'Poesia Pau Brasil'),
    ('Mœriken e Uhland', 'Mörike e Uhland', 'Poesia Pau Brasil'),
    ('scepticimo', 'scepticismo', 'Poesia Pau Brasil'),
    ('descrentes a cançados', 'descrentes e cançados', 'Poesia Pau Brasil'),
    ('á pyogravura', 'á pyrogravura', 'Falação'),
    ('Barbaros, pictorescose e credulos', 'Barbaros, pictorescos e credulos', 'Falação'),
    ('Primeiro chà', 'Primeiro chá', 'Pero Vaz Caminha (título)'),
    ('tão altas et tão saradinhas', 'tão altas e tão saradinhas', 'Pero Vaz Caminha («As meninas da gare»)'),
    ('aos que a vam buscar.', 'aos que a vam buscar', 'Gandavo («Hospedagem»)'),
    ('Mas recream a accrescentam', 'Mas recream e accrescentam', 'Gandavo («Salubridade»)'),
    ('tem un cheiro muy suave', 'tem um cheiro muy suave', 'Gandavo («Natureza morta»)'),
    ('Cidras limões a laranjas', 'Cidras limões e laranjas', 'Gandavo («Riquezas naturais»)'),
    ("Que ainda que ande’ quinze", 'Que ainda que ande quinze', 'Gandavo («Festa da raça»)'),
    ('Aves des rouleaux', 'Avec des rouleaux', 'O Capuchinho Claude d’Abbeville («A moda»)'),
    ('Et ruissellet dedans', 'Et ruissellent dedans', 'O Capuchinho Claude d’Abbeville («O país»)'),
    ('== Cà e là', '== Çà e là', 'O Capuchinho Claude d’Abbeville (título)'),
    ('Como un meridiano', 'Como um meridiano', 'Noturno'),
    ('a serraria como un poema', 'a serraria como um poema', 'Versos de Dona Carrie'),
    ('Como un photographo', 'Como um photographo', 'Sol'),
    ('Der frühling', 'Der Frühling', 'Escola Berlites'),
    ('No amphithetro', 'No amphitheatro', 'Ocaso'),
    ('sanidade è perfeita', 'sanidade é perfeita', 'Anúncio de São Paulo'),
]
# o «â» por «ã» da composição parisiense (Bestâo, tâo, Nâo, Canhâo, mâos, construcçâo) a tabela já resolve

# versos e frases em outra língua: não passam pela grafia
ESTRANGEIRAS_PARTES = {'O Capuchinho Claude d’Abbeville'}
ESTRANGEIRAS = {'Mi pensamiento hacia Medina del Campo', 'Ahora Sevilla envuelta en oro pulverizado',
                'Los naranjos salpicados de frutos', 'Como una dadiva a mis ojos enamorados', 'Sin embargo que tarde la mia',
                'The spring', 'Der Frühling', 'La primavera scapigliata', 'Sometimes called the Chicago of South America',
                'Modern Sstyle'}

# depois da tabela: grafias de mais de uma palavra
FRASES = [('lá em baixo', 'lá embaixo'), ('del Rei', 'del-Rei'), ('muito pau brasil', 'muito pau-brasil'),
          ("Pedr’ Álvares", "Pedr’Álvares"), ('3 de Maio', '3 de maio'), ('regresso a Pátria', 'regresso à Pátria'),
          ('cor de rosa', 'cor-de-rosa'), ('Cana de açúcar', 'Cana-de-açúcar'), ('pedra sabão', 'pedra-sabão'),
          ('Porta Estandarte', 'Porta-Estandarte')]
# versos que pedem decisão caso a caso (texto já na grafia de hoje → como fica)
LINHAS = {
    'Vem tão puros e coados': 'Vêm tão puros e coados',
    'Todos tem remédio de vida': 'Todos têm remédio de vida',
    'Depois que são maduras tem um cheiro mui suave': 'Depois que são maduras têm um cheiro mui suave',
    'E os tem em maior estima': 'E os têm em maior estima',
    'A praça publica está cheia': 'A praça pública está cheia',
}


def tabela():
    t = {}
    for l in open(os.path.join(AQUI, 'grafia.tsv'), encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        a, b = l.rstrip('\n').split('\t')[:2]
        t[a] = b
    return t


GRAFIA = tabela()
PAL = re.compile(r"[\wÀ-ÿœæ$°]+(?:[-’'][\wÀ-ÿ]+)*", re.U)


def hoje(s):
    """grafia de 1925 → de hoje, palavra a palavra; crase e maiúsculas acentuadas do livro (á, A’, E’)."""
    s = s.replace('A’ ', 'À ').replace('E’ ', 'É ').replace('A’', 'À').replace('E’s', 'És').replace('E’', 'É')
    s = re.sub(r'(?<![\wÀ-ÿ])á(?![\wÀ-ÿ])', 'à', s)
    s = re.sub(r'(?<![\wÀ-ÿ])ás(?![\wÀ-ÿ])', 'às', s)
    s = PAL.sub(lambda m: GRAFIA.get(m.group(0), m.group(0)), s)
    for a, b in FRASES:
        s = s.replace(a, b)
    return s


def verso(l, estrangeira=False):
    rec = len(l) - len(l.lstrip(' '))
    v = l.strip()
    if not (estrangeira or v in ESTRANGEIRAS):
        v = hoje(v)
    v = LINHAS.get(v, v)
    return '| ' + NBSP * 4 * rec + v


def montar():
    txt = open(os.path.join(AQUI, 'original', 'pau-brasil-1925.txt'), encoding='utf-8').read()
    for a, b, _ in CORRECOES:
        if txt.count(a) != 1:
            raise SystemExit('correção não achada (ou repetida): ' + a)
        txt = txt.replace(a, b)
    partes, secao, cur = [], '', None
    for bloco in re.split(r'\n\s*\n', txt.strip()):
        linhas = bloco.split('\n')
        l0 = linhas[0]
        if l0.startswith('§ '):
            secao = hoje(l0[2:].strip()).replace('R P 1', 'RP 1'); continue
        if l0.startswith('=p ') or l0.startswith('= '):
            prosa = l0.startswith('=p ')
            tit = l0.split(' ', 1)[1].strip()
            cur = {'n': secao, 'titulo': hoje(tit), 'blocos': [], 'prosa': prosa,
                   'estrangeira': tit in ESTRANGEIRAS_PARTES}
            partes.append(cur); continue
        if l0.startswith('== '):
            cur['blocos'].append('**' + (l0[3:].strip() if cur['estrangeira'] and l0[3:].strip() != 'O paiz'
                                         else hoje(l0[3:].strip())) + '**'); continue
        if l0.startswith('~ '):
            cur['blocos'].append('_' + hoje(l0[2:].strip()) + '_'); continue
        if l0.strip() == '⁂':
            cur['blocos'].append('## ⁂'); continue
        if l0.startswith('> '):
            cur['blocos'].append('\n'.join(hoje(x[2:].strip()) for x in linhas)); continue
        if l0.startswith('| '):        # verso citado na prosa
            cur['blocos'].append('\n'.join('| ' + x[2:] for x in linhas)); continue
        if cur['prosa']:
            for x in linhas:
                cur['blocos'].append(hoje(x.strip()))
        else:
            cur['blocos'].append('\n'.join(verso(x, cur['estrangeira']) for x in linhas))
    # seção de uma parte só, com o mesmo nome (Secretário dos amantes): sem o nome repetido no índice
    for p in partes:
        if p['n'] and sum(1 for q in partes if q['n'] == p['n']) == 1 and p['n'] == p['titulo']:
            p['n'] = ''
    saida = [{'n': p['n'], 'titulo': p['titulo'], 'texto': '\n\n'.join(p['blocos'])} for p in partes]
    return saida


if __name__ == '__main__':
    partes = montar()
    pal = sum(len(re.findall(r"[A-Za-zÀ-ÿœæ]+", p['texto'])) for p in partes)
    versos = sum(p['texto'].count('| ') for p in partes)
    obra = {'id': 'pau-brasil', 'autor': 'oswald-de-andrade', 'titulo': 'Pau Brasil', 'ano': 1925, 'genero': 'Poesia',
            'divisao': {'singular': 'poema', 'plural': 'poemas', 'rotulo': 'titulo', 'agrupar': True},
            'descricao': 'O primeiro livro de poemas de Oswald de Andrade, publicado em Paris em 1925, com o prefácio de Paulo Prado e o manifesto da poesia pau-brasil («Falação»).',
            '_palavras': pal, 'partes': partes,
            'edicao': json.load(open(os.path.join(AQUI, 'edicao.json'), encoding='utf-8'))}
    obra['edicao']['erros'] = [{'cap': onde, 'de': a.replace('== ', ''), 'para': b.replace('== ', '') if 'Abbeville' in onde or 'Berlites' in onde
                                       else LINHAS.get(hoje(b), hoje(b))}
                               for a, b, onde in CORRECOES]
    js = ('/* Pau Brasil — Oswald de Andrade (Paris, 1925). Gerado por edicoes/pau-brasil/montar.py; não edite à mão:\n'
          '   corrija edicoes/pau-brasil/original/pau-brasil-1925.txt (ou as tabelas) e rode de novo. */\n'
          'BIBLIOTECA.obra(' + json.dumps(obra, ensure_ascii=False, indent=1) + ');\n')
    os.makedirs(os.path.join(RAIZ, 'conteudo', 'oswald-de-andrade'), exist_ok=True)
    open(os.path.join(RAIZ, 'conteudo', 'oswald-de-andrade', 'pau-brasil.js'), 'w', encoding='utf-8').write(js)
    print(len(partes), 'partes,', versos, 'linhas de verso,', pal, 'palavras')
