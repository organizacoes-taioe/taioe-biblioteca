"""Monta edicoes/catecismo-pio-x/original/ a partir das páginas do Wikisource italiano.

    python3 edicoes/catecismo-pio-x/baixar.py <pasta>     (uma vez: grava <pasta>/pag/NNN.json)
    python3 edicoes/catecismo-pio-x/montar.py <pasta> [--teste]

Base: «Pagina:Compendio della dottrina cristiana, Roma, 1905.djvu/87» a «/299» (o Catechismo maggiore,
pp. 75-287 da edição), todas no nível 4 (validadas) do it.wikisource, transcritas do fac-símile do Google
Livros (id ZpJqhlYxa8o) que está no Commons. As correções feitas pela imagem estão em CORRECOES.

Saída: um arquivo por capítulo («Capo»), com «## n. título» e a marca «[parte.n]» no começo do primeiro
bloco (para o site fazer uma página por capítulo; a marca não aparece: divisao.marcas = False); os §§
como «## § n. título»; cada pergunta num bloco, «**n. pergunta**» (o «D.» da edição vira o negrito; o
que a edição põe em redondo dentro da pergunta em itálico vai em _itálico_ dentro do negrito), e a
resposta no bloco seguinte, sem o «R.»; as respostas em lista (o Credo, os mandamentos…) com uma linha
por item, começando com «| ». Numeração das perguntas contínua, de 1 a 993, como nas edições correntes.
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PRIMEIRA, ULTIMA = 87, 299
TOTAL = 993

# (página do djvu, errado, certo): erros da transcrição validada do Wikisource, conferidos na imagem do fac-símile
# (achados pela comparação com um OCR próprio, Tesseract italiano, das 213 páginas; 2026-11-23)
CORRECOES = [
    (87, "R. certamente necessario", "R. È certamente necessario"),
    (88, "D. ''D. chi dobbiamo", "D. ''Da chi dobbiamo"),
    (92, "giudicare i i vivi", "giudicare i vivi"),
    (194, "'''Pagar le decime", "''Pagar le decime"),
    (89, 'Comandamenti, ei Sacramenti', 'Comandamenti, e i Sacramenti'),
    (93, 'Dio e Padre, 1.º', 'Dio è Padre, 1.º'),
    (93, 'Dio ė Padre', 'Dio è Padre'),
    (94, 'terra per che ha fatto', 'terra perchè ha fatto'),
    (100, 'commise con atto', 'commise con un atto'),
    (103, 'sal vati', 'salvati'),
    (103, 'questi annunzio', 'questi annunziò'),
    (108, 'Colui che condanno', 'Colui che condannò'),
    (119, 'per veniamo', 'perveniamo'),
    (142, 'L’orazione e una', 'L’orazione è una'),
    (143, 'e nel tempio.', 'e nel sacro tempio.'),
    (166, 'alle sette anticristiane', 'alle sètte anticristiane'),
    (173, 'comanda mento', 'comandamento'),
    (176, 'e perchè perchè toglie', 'e perchè toglie'),
    (178, 'per donare', 'perdonare'),
    (181, 'de gli altri', 'degli altri'),
    (199, 'sacramenti e la cosa', 'sacramenti è la cosa'),
    (203, 'Penitenza e necessaria', 'Penitenza è necessaria'),
    (209, 'cri stiani', 'cristiani'),
    (210, 'Crisma e olio', 'Crisma è olio'),
    (215, 'vi e del vino', 'vi è del vino'),
    (225, 'pur che si', 'purchè si'),
    (228, 'sacerdote e il ministro', 'sacerdote è il ministro'),
    (239, 'attrizione e quello', 'attrizione è quello'),
    (248, 'in quieto', 'inquieto'),
    (251, 'possono, nè debbono', 'possono, ma debbono'),
    (261, 'con tiene', 'contiene'),
    (277, 'Tradizione e la parola', 'Tradizione è la parola'),
    (278, 'per con seguirlo', 'per conseguirlo'),
    (282, 'Prudenza e la virtù', 'Prudenza è la virtù'),
]
ROMANOS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII']
PARTES = {'PRIMA': 1, 'SECONDA': 2, 'TERZA': 3, 'QUARTA': 4, 'QUINTA': 5}
TITULOS_PARTE = {1: 'Del Simbolo degli Apostoli detto volgarmente il «Credo»', 2: 'Dell’orazione',
                 3: 'Dei comandamenti di Dio e della Chiesa', 4: 'Dei sacramenti',
                 5: 'Delle virtù principali e di altre cose necessarie a sapersi dal cristiano'}
# capítulo longo partido em dois arquivos (para os lotes de tradução): (parte, capítulo): começo do 2º arquivo
DIVIDIR = {(4, 6): '## § 6.'}


def expandir(t):
    """Desfaz os modelos do Wikisource, dos mais internos para fora."""
    def um(m):
        ps = m.group(1).split('|')
        nome, args = ps[0].strip(), ps[1:]
        pos = [a for a in args if not re.match(r'^\s*\w+\s*=', a)]
        if nome in ('Sc', 'sc'):
            return pos[0]
        if nome == '§':
            return pos[1] if len(pos) > 1 else '§ ' + pos[0]
        if nome in ('ec', 'Ec'):
            return pos[1]
        if nome == 'Pt':
            return pos[1] if len(pos) > 1 else ''
        if nome == 'nop':
            return '\n\n'
        if nome == 'indent':
            return '\n⇥' + pos[-1]
        if nome == 'Rule':
            return '\n\n'
        if nome == 'Ct':
            return '\n\n⟦' + pos[-1].replace('\n', ' ') + '⟧\n\n'
        raise ValueError('modelo desconhecido: ' + nome)
    ant = None
    while ant != t:
        ant, t = t, re.sub(r'\{\{([^{}]*)\}\}', um, t)
    return t


def ler_paginas(pasta):
    textos = []
    for n in range(PRIMEIRA, ULTIMA + 1):
        t = json.load(open(os.path.join(pasta, 'pag', f'{n:03d}.json'), encoding='utf-8'))['t']
        for p, a, b in CORRECOES:
            if p == n:
                assert t.count(a) == 1, (n, a, t.count(a))
                t = t.replace(a, b)
        t = re.sub(r'<noinclude>.*?</noinclude>', '', t, flags=re.S)
        t = t.replace('ė', 'è').replace('ả', 'à')   # restos do OCR na transcrição (nė, potestả): a edição tem è, à
        if n == PRIMEIRA:   # a seção s1 da p. 75 é o título geral «Catechismo maggiore»
            t = t[t.index('<section end="s1" />') + len('<section end="s1" />'):]
        t = re.sub(r'<section [^>]*/>', '', t)
        t = re.sub(r'<references\s*/>', '', t)
        textos.append(t)
    # junta as páginas: «{{nop}}» abre parágrafo; palavra partida («rin-» / «graziato») se junta
    out = textos[0].rstrip()
    for t in textos[1:]:
        if t.startswith('{{nop}}') or re.match(r'\s*(D\.|R\.|\{\{(Ct|Ec)|::)', t):
            out += '\n\n' + t
        elif re.search(r'[a-zàèéìòù]-$', out):
            out = out[:-1] + t.lstrip()
        else:
            out += (' ' if not out.endswith('\n') else '') + t.lstrip()
        out = out.rstrip()
    return out


def italicos(s):
    return re.sub(r"''(.+?)''", r'_\1_', s).replace('_ _', ' ')


def pergunta(s):
    """A pergunta, toda em itálico na edição, vai em negrito; o redondo de dentro dela vira _itálico_."""
    partes = s.split("''")
    out = []
    for k, x in enumerate(partes):
        if k % 2 == 1 or not re.search(r'\w', x):
            out.append(x)
        else:
            m = re.match(r'^(\W*)(.*?)(\W*)$', x, re.S)
            out.append(m.group(1) + '_' + m.group(2) + '_' + m.group(3))
    q = re.sub(r'\s+', ' ', ''.join(out)).strip()
    q = q.replace('_ _', ' ')
    return q


def montar(pasta):
    bruto = expandir(ler_paginas(pasta))
    bruto = re.sub(r'\n\s*\n(?=⇥|::)', '\n', bruto)      # os itens de uma lista ficam num bloco só
    pars = [re.sub(r'[ \t]+', ' ', p).strip() for p in re.split(r'\n\s*\n', bruto)]
    pars = [p for p in pars if p]
    caps = []            # [(parte, n, título, [blocos])]
    parte, atual, nq = 0, None, 0
    pendente_parte = None
    for p in pars:
        if p.startswith('⟦'):
            h = re.sub(r"'''+", '', p.strip('⟦⟧ ')).replace('<br />', ' ').replace('<br/>', ' ')
            h = re.sub(r'\s+', ' ', h).strip()
            m = re.match(r'PARTE (\w+)$', h)
            if m:
                parte = PARTES[m.group(1)]
                pendente_parte = parte
                continue
            if pendente_parte:       # o título da parte, logo depois de «PARTE …»
                caps.append(('titulo-parte', parte, h, []))
                pendente_parte = None
                continue
            if h.startswith('LEZIONE PRELIMINARE'):
                continue
            if h.startswith('DELLA DOTTRINA CRISTIANA'):
                atual = (0, 0, 'Lezione preliminare. Della dottrina cristiana e delle sue parti principali', [])
                caps.append(atual)
                continue
            m = re.match(r'Capo ([IVX]+)\s*\.?\s*(.+)$', h)
            if m:
                n = ROMANOS.index(m.group(1)) + 1
                titulo = m.group(2).strip().rstrip('.')
                atual = (parte, n, titulo, [])
                caps.append(atual)
                continue
            m = re.match(r'§ (\d+)\s*\.?\s*-\s*(.+)$', h)
            if m:
                atual[3].append(f'## § {m.group(1)}. ' + m.group(2).strip().rstrip('.'))
                continue
            raise ValueError('título desconhecido: ' + h)
        linhas = p.split('\n')
        corpo = ' '.join(l for l in linhas if not l.startswith('⇥') and not l.startswith('::')).strip()
        lista = [l.lstrip('⇥:').strip() for l in linhas if (l.startswith('⇥') or l.startswith('::')) and l.strip('⇥: ')]
        m = re.match(r'D\.\s*(.*)$', corpo, re.S)
        if m and not lista:
            nq += 1
            marca = f'[{ROMANOS[atual[0] - 1]}.{atual[1]}]\n' if atual[0] and not any(re.match(r'(\[.*?\]\n)?\*\*\d', b) for b in atual[3]) else ''
            atual[3].append(marca + f'**{nq}. ' + pergunta(m.group(1)) + '**')
            continue
        corpo = re.sub(r'^R\s*[.,:]\s*', '', corpo)
        if lista:
            bloco = '\n'.join('| ' + italicos(x) for x in ([corpo] if corpo else []) + lista)
        else:
            bloco = italicos(corpo)
        atual[3].append(bloco)
    assert nq == TOTAL, nq
    return caps


CAB = ('# obra: Compendio della dottrina cristiana prescritto da Sua Santità Papa Pio X alle diocesi della '
       'provincia di Roma, Catechismo maggiore (Roma, Tipografia Vaticana, 1905)\n'
       '# fonte: it.wikisource, Pagina:Compendio della dottrina cristiana, Roma, 1905.djvu/87-299 (nível 4, '
       'validadas), https://it.wikisource.org/wiki/Compendio_della_dottrina_cristiana/Catechismo_maggiore\n'
       '# edicao: fac-símile no Commons, File:Compendio della dottrina cristiana, Roma, 1905.djvu (Google '
       'Livros, id ZpJqhlYxa8o), pp. 75-287\n'
       '# nota: gerado por montar.py; não editar à mão (correções vão em CORRECOES)\n')


def gravar(caps):
    destino = os.path.join(AQUI, 'original')
    os.makedirs(destino, exist_ok=True)
    titulos_parte = {}
    arquivos = []
    for c in caps:
        if c[0] == 'titulo-parte':
            titulos_parte[c[1]] = c[2]
            continue
        parte, n, titulo, blocos = c
        if parte == 0:
            nome = 'p0-licao-preliminare.txt'
            texto = '## Della dottrina cristiana e delle sue parti principali\n\n' + '\n\n'.join(blocos)
            cab = f'# titulo: {titulo}\n'
        else:
            nome = f'p{parte}-c{n:02d}.txt'
            texto = f'## {n}. {titulo}\n\n' + '\n\n'.join(blocos)
            cab = f'# titulo: Parte {ROMANOS[parte - 1]}, {TITULOS_PARTE[parte]}; Capo {ROMANOS[n - 1]}, {titulo}\n'
            assert titulos_parte[parte].lower() == TITULOS_PARTE[parte].lower(), titulos_parte[parte]
        pedacos = [(nome, cab, texto)]
        if (parte, n) in DIVIDIR:
            k = texto.index('\n\n' + DIVIDIR[(parte, n)])
            pedacos = [(nome.replace('.txt', 'a.txt'), cab.rstrip('\n') + ' (1ª metade)\n', texto[:k]),
                       (nome.replace('.txt', 'b.txt'), cab.rstrip('\n') + ' (2ª metade)\n', texto[k + 2:])]
        for nome, cab, texto in pedacos:
            with open(os.path.join(destino, nome), 'w', encoding='utf-8') as f:
                f.write(cab + CAB + '\n' + texto + '\n')
            arquivos.append(nome)
    return arquivos, titulos_parte


if __name__ == '__main__':
    caps = montar(sys.argv[1])
    if '--teste' in sys.argv:
        for c in caps:
            print(c[0], c[1], c[2], len(c[3]))
    else:
        arqs, tp = gravar(caps)
        print(len(arqs), 'arquivos;', tp)
