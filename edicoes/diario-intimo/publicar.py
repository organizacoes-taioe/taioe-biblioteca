"""Diário Íntimo: grava conteudo/lima-barreto/diario-intimo.js (chamado por montar.py --publicar)."""
import csv
import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
SAIDA = os.path.join(RAIZ, 'conteudo', 'lima-barreto', 'diario-intimo.js')

APRESENTACAO = """**O livro.** Lima Barreto guardou, de 1900 até perto da morte, cadernos e folhas soltas com notas do dia, contas, listas de leitura, cópias de cartas e de recortes, planos de romances e capítulos começados. Pensou em publicar parte disso como memórias, mas o _Diário Íntimo_ só saiu em 1953, organizado por Francisco de Assis Barbosa a partir dos manuscritos que a família guardou (hoje na Biblioteca Nacional). Na edição de 1956 das _Obras de Lima Barreto_ (São Paulo, Brasiliense, vol. XIV), o volume cresceu: entraram os esboços de romance de 1900, 1906, 1910 e 1914 e, no fim, a primeira versão de _Clara dos Anjos_, de 1904, que o autor deixou incompleta e é outra obra que não a novela do mesmo nome, escrita em 1921 e 1922.

**Texto-base.** Esta edição segue o texto de 1956, o mais completo, na sua ordem: as notas datadas pelo autor vão pelas datas dele; as que ele não datou ficam onde o organizador as pôs, entre as do mesmo ano. É só o texto de Lima Barreto: ficam de fora o prefácio, a nota prévia e as notas do organizador ao fim de cada ano, as chamadas dessas notas e as rubricas «Sem data». Ficam as marcas com que o organizador assinalou o que não pôde ler nos manuscritos: [...] para o trecho ilegível, [?] para a leitura duvidosa, e as iniciais seguidas de reticências (C...) com que abreviou alguns nomes.

**Como foi estabelecido.** O ponto de partida foi a transcrição da Fundação Biblioteca Nacional (2002), que segue a edição de 1956 já na ortografia de 1971, como a publica a Biblioteca Virtual Miguel de Cervantes. Ela foi confrontada palavra por palavra com duas leituras por OCR de um exemplar de 1956 (a do Internet Archive e uma nossa, com o Tesseract), e cada divergência foi conferida nas imagens das páginas. {CORRECOES}

**Divisão.** Uma parte por ano, como no livro; os anos com poucas notas vão juntos (1906 e 1907, 1912 a 1915, 1920 e 1921). Os asteriscos separam as notas, como no impresso. A primeira versão de _Clara dos Anjos_ fecha o volume, nos seus quatro capítulos.

**Grafia.** Ortografia de hoje (Acordo de 1990, forma brasileira): ideia, frequente, cinquenta, antissociais, semiembriaguez. As formas antigas que a edição de 1956 ainda trazia (cousa, dous, contacto) vão na forma atual. As palavras e as citações em outras línguas ficam como o autor as escreveu."""

FONTES = [
    {'nome': 'Diário Íntimo, em Obras de Lima Barreto, vol. XIV (São Paulo, Brasiliense, 1956), exemplar digitalizado no Internet Archive',
     'url': 'https://archive.org/details/barreto-l.-diario-intimo_202302', 'nota': 'texto-base, conferido nas imagens'},
    {'nome': 'Diário Íntimo, transcrição da Fundação Biblioteca Nacional (2002), na Biblioteca Virtual Miguel de Cervantes',
     'url': 'https://www.cervantesvirtual.com/obra/diario-intimo--0/', 'nota': 'ponto de partida da transcrição'},
    {'nome': 'Wikisource em português, a mesma transcrição de 2002', 'url': 'https://pt.wikisource.org/wiki/Di%C3%A1rio_%C3%8Dntimo_(Lima_Barreto)',
     'nota': 'só para comparar'},
]


def js_texto(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def correcoes():
    erros, n_bn = [], 0
    for c in csv.reader(open(os.path.join(AQUI, 'correcoes.tsv'), encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        if not c or c[0].startswith('#') or c[0] == 'bloco':
            continue
        motivo = c[4] if len(c) > 4 else ''
        if motivo.startswith('erro1956'):
            parte = motivo.split(':', 1)[1].strip() if ':' in motivo else ''
            erros.append({'cap': parte, 'de': c[2], 'para': c[3]})
        elif motivo.startswith('1956'):
            n_bn += 1
    return erros, n_bn


def gravar(partes):
    erros, n_bn = correcoes()
    frase = (f'A conferência devolveu ao texto {n_bn} lições de 1956 que a transcrição de 2002 tinha perdido ou trocado '
             '(palavras, linhas, maiúsculas, itálicos)')
    frase += (f', e corrigiu {len(erros)} erros evidentes do próprio impresso de 1956, listados abaixo.' if erros else '.')
    edicao = {'base': 'Edição de 1956', 'apresentacao': APRESENTACAO.replace('{CORRECOES}', frase), 'fontes': FONTES}
    if erros:
        edicao['secoes'] = {'erros': {'titulo': 'Erros da edição de 1956 corrigidos', 'explica': 'Na ortografia de 1956.',
                                      'de': '1956', 'para': 'Corrigido'}}
        edicao['erros'] = erros
    meta = {'id': 'diario-intimo', 'autor': 'lima-barreto', 'titulo': 'Diário Íntimo', 'ano': 1953, 'datas': '1900–1921',
            'genero': 'Diário', 'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome', 'marcas': False},
            'descricao': 'Notas, apontamentos e esboços de romance que Lima Barreto escreveu de 1900 a 1921, publicados depois da sua morte, com a primeira versão, incompleta, de Clara dos Anjos.'}
    L = ['/* Diário Íntimo — Lima Barreto', '   Gerado por edicoes/diario-intimo/montar.py --publicar a partir de fontes/bn2002.txt e correcoes.tsv.',
         '   Não edite à mão: corrija as decisões e rode de novo. */', 'BIBLIOTECA.obra({']
    L += [f'  {c}: {json.dumps(v, ensure_ascii=False)},' for c, v in meta.items()]
    L.append('  edicao: ' + json.dumps(edicao, ensure_ascii=False, indent=2).replace('\n', '\n  ') + ',')
    L.append('  partes: [')
    for i, (titulo, bs) in enumerate(partes):
        L.append(f'    {{ n: "", titulo: {json.dumps(titulo, ensure_ascii=False)}, texto: `{js_texto((chr(10) * 2).join(bs))}` }}'
                 + (',' if i + 1 < len(partes) else ''))
    L += ['  ]', '});']
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    open(SAIDA, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('gravado', os.path.relpath(SAIDA, RAIZ))
    idx = os.path.join(RAIZ, 'index.html')
    h = open(idx, encoding='utf-8').read()
    linha = '<script defer src="conteudo/lima-barreto/diario-intimo.js"></script>'
    if linha not in h:
        ant = '<script defer src="conteudo/lima-barreto/isaias-caminha.js"></script>'
        h = h.replace(ant, ant + '\n' + linha, 1) if ant in h else h.replace('</head>', linha + '\n</head>', 1)
        open(idx, 'w', encoding='utf-8').write(h)
