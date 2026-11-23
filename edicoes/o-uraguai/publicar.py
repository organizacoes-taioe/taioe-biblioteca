"""O Uraguai: de texto.txt, notas.txt e abertura.txt ao arquivo do site, conteudo/basilio-da-gama/o-uraguai.js.

Chamado por montar.py --publicar (não precisa do cache). Partes: a dedicatória (o que vem antes do poema na
1ª edição), os cinco cantos (os versos num bloco só, como em 1769, com o número do verso à margem de 10 em 10,
pela marca {v N} do gerador; as notas do autor, que em 1769 vêm no pé das páginas, no fim de cada canto) e os
dois sonetos «Ao Autor» do fim do livro.
"""
import json, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao import montar as site  # noqa: E402

META = {
    'id': 'o-uraguai',
    'autor': 'basilio-da-gama',
    'titulo': 'O Uraguai',
    'ano': 1769,
    'genero': 'Epopeia',
    'divisao': {'singular': 'canto', 'plural': 'cantos'},
}

TITULOS = ['Canto Primeiro', 'Canto Segundo', 'Canto Terceiro', 'Canto Quarto', 'Canto Quinto']

APRESENTACAO = """**Texto-base.** Este texto reproduz a primeira edição de _O Uraguai_ (Lisboa, na Régia Oficina Tipográfica, 1769), na grafia brasileira de hoje, com tudo o que ela traz: a dedicatória, o soneto ao Conde de Oeiras, as notas do autor e os dois sonetos «Ao Autor» do fim do livro, de Joaquim Inácio de Seixas Brandão e Inácio José de Alvarenga Peixoto.

**Como foi estabelecido.** Foram confrontados palavra por palavra, por programa, dois exemplares da 1ª edição digitalizados no Internet Archive (o da Biblioteca Pública de Boston e o da Biblioteca Fisher, da Universidade de Toronto), em quatro leituras por OCR, a transcrição da 1ª edição no Wikisource e o texto em grafia atualizada que circula na internet (Wikisource e Domínio Público). Cada diferença de palavra ou de pontuação entre as leituras foi decidida nas imagens dos dois exemplares. O texto corrente tem erros que a 1ª edição corrige («Ninfas do amor» por «Ninfas do mar», «Podres choupanas» por «Pobres choupanas», «Quando pode o temor» por «Quanto pode o temor», entre outros; lista abaixo), perde palavras («nem os caudalosos», «princípio à guerra») e mete entre os versos três linhas das notas. O poema tem 1.377 versos: 244, 365, 329, 289 e 150 nos cinco cantos.

**Grafia.** Mudou só a maneira de escrever (ſ, y, ph, letras dobradas, acentos, _he_ → _é_, _hum_ → _um_), e as formas antigas que não pesam no verso passaram à forma de hoje (_cousa_ → _coisa_, _dous_ → _dois_, _cuberto_ → _coberto_, _frecha_ → _flecha_, _artilheria_ → _artilharia_). Ficam as que mudam o número de sílabas do decassílabo: _inda_, _mui_, _exprimentada_, _galopear_, _até li_ (até ali) e as contrações de «com» com o artigo (_co'o_, _co'a_, _co'os_, _co'as_). Os nomes ficam na forma do autor (_Cepé_, _Gerardo_, _Catâneo_), com a grafia de hoje (_Lindoia_, _Cobé_). A pontuação é a de 1769.

**Notas.** As notas do autor, que na 1ª edição estão no pé das páginas, vêm no fim de cada canto, cada uma com as palavras do verso a que se refere. As citações em latim e em francês ficam como no impresso.

**Divisão.** Cinco cantos, com o número do verso à margem de dez em dez."""

FONTES = [
    {'nome': 'O Uraguay, 1ª edição, 1769, exemplar da Boston Public Library (Internet Archive)',
     'url': 'https://archive.org/details/ouruaguaypoema00gama', 'nota': 'fac-símile; texto-base'},
    {'nome': 'O Uraguay, 1ª edição, 1769, exemplar da Biblioteca Fisher, Universidade de Toronto (Internet Archive)',
     'url': 'https://archive.org/details/ouraguaypoema00gama', 'nota': 'fac-símile; segundo exemplar, para as passagens gastas ou manchadas'},
    {'nome': 'Wikisource, O Uraguay (transcrição da 1ª edição)', 'url': 'https://pt.wikisource.org/wiki/O_Uraguay',
     'nota': 'revisada em parte; conferida palavra por palavra'},
    {'nome': 'Wikisource, O Uraguai (grafia atualizada)', 'url': 'https://pt.wikisource.org/wiki/O_Uraguai',
     'nota': 'base da grafia de hoje; corrigida pela 1ª edição'},
]

ERROS = [
    {'cap': 'V, nota «As brancas velas»', 'de': 'a virtude ao todo O Author', 'para': 'a virtude ao todo. O Autor'},
]

ROMANOS = ['I', 'II', 'III', 'IV', 'V']


def ler_texto():
    cantos, atual = [], None
    for l in open(os.path.join(AQUI, 'texto.txt'), encoding='utf-8'):
        l = l.rstrip('\n')
        if l.startswith('# '):
            atual = []; cantos.append(atual)
        elif l.strip():
            atual.append(l)
    return cantos


def ler_notas():
    notas, atual, bloco = [], None, []
    for l in open(os.path.join(AQUI, 'notas.txt'), encoding='utf-8'):
        l = l.rstrip('\n')
        if l.startswith('# Canto'):
            atual = []; notas.append(atual)
        elif not l.strip():
            if bloco: atual.append(bloco); bloco = []
        else:
            bloco.append(l)
    if bloco: atual.append(bloco)
    return notas


def nota_em_blocos(linhas):
    """uma nota → blocos «¤ »: a prosa, os versos citados juntos, a referência."""
    out, versos = [], []
    for l in linhas:
        if l.startswith('| '):
            versos.append(l); continue
        if versos:
            out.append('¤ ' + '\n'.join(versos)); versos = []
        out.append('¤ ' + (l[2:] if l.startswith('> ') else l))
    if versos:
        out.append('¤ ' + '\n'.join(versos))
    return out


def ler_abertura(nome):
    """abertura.txt / fecho.txt: blocos separados por linha em branco, já no formato do site."""
    s = open(os.path.join(AQUI, nome), encoding='utf-8').read().strip()
    return [b for b in re.split(r'\n\s*\n', s) if b.strip()]


def mantidas():
    """As lições de 1769 que corrigem o texto corrente (decisoes.json)."""
    dec = json.load(open(os.path.join(AQUI, 'decisoes.json'), encoding='utf-8'))
    cantos = ler_texto()
    out = []
    for k, v in dec['palavras'].items():
        cv, w = k.split('|'); c, n = map(int, cv.split(','))
        if not v or w.lower() == v.lower():
            continue                                   # só caixa, ou a palavra apagada (vai com a outra)
        var = 'Por que' if k == '1,56|Por' else w
        out.append({'cap': '%s, %d' % (ROMANOS[c - 1], n), 'texto': cantos[c - 1][n - 1], 'variante': var})
    for cv, linha in dec['linhas'].items():
        c, n = map(int, cv.split(','))
        var = {'1,73': '- Fontes de crimes - militar tesouro,', '2,89': 'Nem altas minas, nem caudalosos',
               '2,311': 'Mostrava descoberto o peito e o rosto', '2,318': 'Para dar outra vez princípio'}.get(cv)
        if var:
            out.append({'cap': '%s, %d' % (ROMANOS[c - 1], n), 'texto': linha, 'variante': var})
    out.append({'cap': 'II, depois de 89', 'texto': '(nada)', 'variante': 'duas linhas da nota a «Aqui não temos» entre os versos'})
    out.append({'cap': 'IV, depois de 56', 'texto': '(nada)', 'variante': '«O bom padre. Balda.», a nota, entre os versos'})
    out.sort(key=lambda x: (ROMANOS.index(x['cap'].split(',')[0]), int(re.search(r'\d+', x['cap'].split(',')[1]).group())))
    return out


def partes():
    cantos, notas = ler_texto(), ler_notas()
    ps = [{'n': '', 'titulo': 'Dedicatória', 'paragrafos': ler_abertura('abertura.txt')}]
    for i, (vs, ns) in enumerate(zip(cantos, notas)):
        linhas = [('{v %d} ' % (k + 1) if (k + 1) % 10 == 0 else '') + v for k, v in enumerate(vs)]
        blocos = ['\n'.join('| ' + l for l in linhas)]
        for n in ns:
            blocos += nota_em_blocos(n)
        ps.append({'n': i + 1, 'titulo': TITULOS[i], 'paragrafos': blocos})
    ps.append({'n': '', 'titulo': 'Ao Autor', 'paragrafos': ler_abertura('fecho.txt')})
    return ps


def publicar():
    edicao = {'apresentacao': APRESENTACAO, 'fontes': FONTES, 'erros': ERROS, 'mantidas': mantidas(),
              'secoes': {'erros': {'titulo': 'Erros da 1ª edição corrigidos',
                                   'explica': 'À esquerda, a 1ª edição na grafia original.'},
                         'mantidas': {'titulo': 'Lições da 1ª edição contra o texto corrente',
                                      'explica': 'À esquerda, o verso como está aqui (1ª edição); à direita, o que se lê no texto que '
                                                 'circula na internet (Wikisource, Domínio Público). O lugar é canto e verso.'}}}
    destino = os.path.join(RAIZ, 'conteudo', META['autor'], META['id'] + '.js')
    comentario = ('O Uraguai — Basílio da Gama\n   Gerado por edicoes/o-uraguai/montar.py --publicar. Não edite à mão:\n'
                  '   corrija texto.txt (montar.py), notas1769.txt (notas.py), abertura.txt ou fecho.txt e rode de novo.\n\n'
                  '   Os versos de cada canto num bloco («| »); {v N} põe o número do verso à margem; «¤ » as notas do autor.')
    site.publicar(destino, META, partes(), edicao, comentario)
    rel = 'conteudo/' + META['autor'] + '/' + META['id'] + '.js'
    if site.registrar_no_index(os.path.join(RAIZ, 'index.html'), rel):
        print('acrescentado ao index.html:', rel)
    print('publicado:', destino)
