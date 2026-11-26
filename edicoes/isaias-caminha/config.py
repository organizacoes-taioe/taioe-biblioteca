"""Recordações do Escrivão Isaías Caminha — fontes.

Edições em vida do autor (morto em 1922): 1ª, Lisboa, A. M. Teixeira, 1909; 2ª, Rio de Janeiro, A. de
Azevedo & Costa, 1917, «revista e augmentada», com a «Breve notícia» (que restabelece o prefácio de
Isaías, cortado em 1909) e uma errata. A 2ª é a última revista pelo autor e está em fac-símile na
Brasiliana USP (BBM 4808): é a edição-base. A Brasiliana tem também a 1ª (BBM 4799), que serve para a
lista das mudanças (mudancas.py).

Testemunhos de 1917 (um exemplar só, duas leituras de programas diferentes):
  t17  OCR próprio (Tesseract, tesseract.py) do BBM 4808. Base do confronto.
  c17  o OCR que vem no PDF do BBM 4808.
Os dois recebem a divisão (partes e parágrafos) da edição moderna de 1917 (bv, abaixo) (ocr.estrutura_como) e são
limpos pelas guias (ocr.limpar: só palavras inexistentes, trocadas pela parecida alinhada). Sem maioria
(dois votos), vale a leitura apoiada pelas edições modernas; sem apoio, a com menos palavras
inexistentes (DESEMPATE_LEXICO), e o ponto vai para a conferência nas imagens (conferencia.json, pela
assinatura do ponto; ver rever()).
Edições modernas (só para a grafia e o desempate; não são texto), as duas no Formulário de 1943:
  bv  a da Biblioteca Virtual do Estudante Brasileiro (USP), da edição da Ática (1995): o texto de 1917
      (traz os trechos acrescentados em 1917), sem a «Breve notícia»; a dela vem do Wikisource.
  ws  a do Wikisource (importada em 2007, de origem não declarada): a «Breve notícia» de 1917, mas o
      romance pelo texto de 1909 (faltam-lhe os acréscimos de 1917: o charadista e o cronista esportivo
      no cap. VIII etc.). Vale como 2ª referência de grafia e para achar as mudanças (mudancas.py).
As duas leem «a compreensão» no começo, onde 1909 e 1917 têm «a compressão».

Divisão: a «Breve notícia» de Lima Barreto (com o prefácio de Isaías dentro) e os capítulos I a XIV,
sem título, como em 1917.
"""
import csv
import glob
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
from edicao import fontes, ocr  # noqa: E402
from edicao.grafia import chave, esqueleto  # noqa: E402
from edicao.tokens import VERSO  # noqa: E402

OBRA = 'isaias-caminha'

META = {
    'id': OBRA,
    'autor': 'lima-barreto',
    'titulo': 'Recordações do Escrivão Isaías Caminha',
    'ano': 1909,
    'genero': 'Romance',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'Romance publicado em 1909 e revisto pelo autor na 2ª edição, de 1917.',
}

BASE = 't17'
REFERENCIAS = [('bv', False), ('ws', False)]
DESEMPATE_LEXICO = True

ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV']
PDF17 = 'bbm4808-1917'
PAGS17 = (11, 238)          # da «Breve notícia» ao fim do romance (a p. 239 é a errata)

# dedicatória (1917, p. [7] do PDF 9; conferida no fac-símile)
DEDICATORIA = ['A Benedito de Souza', 'meu compadre e meu amigo']


# ------------------------------------------------------------------ edições modernas

def wikisource_moderno():
    d = json.load(open(fontes.cache(OBRA, 'ws_moderno.json'), encoding='utf-8'))
    pags = {p['title'].split('/', 1)[1]: p['revisions'][0]['slots']['main']['*'] for p in d['query']['pages'].values()}
    obra = []
    for n in ['Breve notícia'] + ROM:
        t = pags[n]
        t = re.sub(r'^\{\{navegar.*?\n\}\}\n', '', t, flags=re.S)
        t = re.sub(r'\[\[Categoria:[^\]]*\]\]', '', t)
        t = re.sub(r'\{\{d\|(.*?)\}\}', r'\1', t, flags=re.S)
        t = t.replace('&mdash;', '—')
        t = re.sub(r'\n*\{\{separador\}\}\n*', lambda m: ' *** ' if not m.group(0).startswith('\n\n') else '\n\n* * *\n\n', t)
        t = re.sub(r'<poem>(.*?)</poem>', lambda m: '\n\n' + VERSO + m.group(1).strip() + '\n\n', t, flags=re.S)
        t = re.sub(r"'''?", '', t)
        t = re.sub(r'<[^>]+>', '', t)
        paras = []
        for b in re.split(r'\n\s*\n', t):
            b = b.strip()
            if not b:
                continue
            if b.startswith(VERSO):
                paras.append(VERSO + '\n'.join(l.strip() for l in b[1:].split('\n') if l.strip()))
            else:
                paras.append(fontes.limpar(b.replace('\n', ' ')))
        obra.append({'n': '' if n == 'Breve notícia' else n, 'titulo': n if n == 'Breve notícia' else '', 'paras': paras})
    return fontes.normalizar(obra)


def bveb():
    s = open(fontes.cache(OBRA, 'bveb.txt'), encoding='utf-8').read()
    s = s[s.index('Lima Barreto\n\n'):]
    obra, parte, par = [], None, ''
    for pag in s.split('\f'):
        for l in pag.split('\n'):
            if not l.strip():
                continue
            m = re.fullmatch(r'\s{20,}([IVX]+)\s*', l)
            if m:
                if parte is not None and par:
                    parte['paras'].append(par)
                par = ''
                parte = {'n': m.group(1), 'titulo': '', 'paras': []}
                obra.append(parte)
                continue
            if parte is None:
                continue
            ind = len(l) - len(l.lstrip())
            l = l.strip()
            if ind >= 6 and par and not re.match(r'^[a-zà-ÿ]', l) or not par:
                if par:
                    parte['paras'].append(par)
                par = l
            elif par.endswith('-') and re.match(r'^[a-zà-ÿ]', l) and not par.endswith(' -'):
                par = par[:-1] + l if not re.search(r'-(me|te|se|lhe|lhes|o|a|os|as|nos|vos|lo|la)$', par) else par + l
            else:
                par += ' ' + l
    if par:
        parte['paras'].append(par)
    for p in obra:
        p['paras'] = [fontes.limpar(x.replace('“', '"').replace('”', '"')) for x in p['paras']]
    return fontes.normalizar(obra)


_MODERNAS = {}
_LEX = set()


def LEXICO():
    """Esqueletos das palavras das edições modernas e da lista do sistema (/usr/share/dict/brazilian)."""
    if not _LEX:
        from edicao.tokens import achatar, e_palavra
        for o in modernas().values():
            _LEX.update(esqueleto(t) for t in achatar(o) if e_palavra(t))
        if os.path.exists('/usr/share/dict/brazilian'):
            _LEX.update(esqueleto(l.strip()) for l in open('/usr/share/dict/brazilian', encoding='utf-8', errors='ignore') if l.strip())
    return _LEX


def modernas():
    if not _MODERNAS:
        ws = wikisource_moderno()
        _MODERNAS.update({'bv': [ws[0]] + bveb(), 'ws': ws})
    return _MODERNAS


# ------------------------------------------------------------------ OCRs de 1917

LIXO = re.compile(r'^(BRASILIANA|Digitized by)', re.I)
CABECO = re.compile(r'^[—–\-~_. ]*\d{1,3}[—–\-~_. ]*$|^[—–\-]+$|^[—–\-]\s*\S{1,4}\s*[—–\-]?$|^[IVXLl1]{1,5}\.?$')
# cabeços (RECORDAÇÕES DO ESCRIVÃO, ISAIAS CAMINHA, BREVE NOTICIA) e números dos capítulos: sem minúsculas
TITULO_OCR = re.compile(r'^[^a-zà-ÿ]*[A-ZÀ-Ú]{2}[^a-zà-ÿ]*$')
CABECO_TXT = re.compile(r'^\W*\d*\W*(RECORDA|ISA[IÍ]AS|CAMINHA|DO ESCRIV)', re.I)


def _juntar(linhas):
    s = ''
    for l in linhas:
        l = l.strip()
        if not l:
            continue
        if re.search(r'[A-Za-zÀ-ÿ][-¬]$', s):
            m = re.match(r"[\w']+", l)
            frag = (m.group(0) if m else '').lower()
            s = s[:-1] + ('-' + l if frag in fontes.CLITICOS else l)
        else:
            s = (s + ' ' + l) if s else l
    return s


def _obra_ocr(linhas_por_pagina):
    linhas = []
    for pag in linhas_por_pagina:
        # «_» e «#» do OCR são manchas (o itálico vem de decisoes.ITALICOS, conferido nas imagens)
        pag = [l.strip().replace('#', '').replace('_', ' ') for l in pag if l.strip() and not LIXO.match(l.strip())]
        pag = [l for l in pag if not TITULO_OCR.match(l)]
        while pag and (CABECO.match(pag[0]) or (CABECO_TXT.match(pag[0]) and len(pag[0]) < 40)):
            pag = pag[1:]
        while pag and CABECO.match(pag[-1]):
            pag = pag[:-1]
        linhas += pag
    texto = _juntar(linhas)
    texto = re.sub(r'\s+([,.;:!?])', r'\1', texto)
    texto = texto.replace('’', "'").replace('E\'', 'É')
    return [{'n': 'I', 'titulo': '', 'paras': [fontes.limpar(texto)]}]


_ESPACADAS = re.compile(r'(?<!\S)(?:[A-Za-zÀ-ÿ] ){2,}[A-Za-zÀ-ÿ](?=[\s,.;:!?»]|$)')


def juntar_espacadas(linha, lexico):
    """O OCR da Brasiliana separa as letras («h u m i l d e», «s r s»): junta as sequências de três letras
    soltas ou mais quando o resultado é palavra conhecida ou tem cinco letras ou mais."""
    def f(m):
        w = m.group(0).replace(' ', '')
        return w if len(w) >= 5 or esqueleto(w) in lexico else m.group(0)
    return _ESPACADAS.sub(f, linha)


def camada(pdf=None, faixa=None, lexico=None):
    s = open(fontes.cache(OBRA, (pdf or 'c17') + '.txt'), encoding='utf-8').read().split('\f')
    a, b = faixa or PAGS17
    lexico = lexico if lexico is not None else LEXICO()
    return _obra_ocr([[juntar_espacadas(l, lexico) for l in p.split('\n')] for p in s[a - 1:b]])


def linhas_tesseract(pdf, a, b):
    pasta = fontes.cache(OBRA, 'tess-' + pdf)
    paginas = []
    for n in range(a, b + 1):
        f = os.path.join(pasta, f'{n}.tsv')
        if not os.path.exists(f):
            paginas.append([])
            continue
        linhas = {}
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] != '5' or not (r['text'] or '').strip():
                continue
            k = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
            linhas.setdefault(k, []).append((int(r['top']), int(r['left']), r['text'].strip(), int(r['height'])))
        # uma linha impressa que o Tesseract partiu em dois blocos (páginas tortas): as metades se juntam
        # quando as faixas verticais se sobrepõem em mais da metade
        faixas = []
        for ws in linhas.values():
            ys = sorted(w[0] for w in ws)
            hs = sorted(w[3] for w in ws)
            y0 = ys[len(ys) // 2]
            faixas.append([y0, y0 + hs[len(hs) // 2], list(ws)])
        faixas.sort(key=lambda f: f[0])
        juntas = []
        for f in faixas:
            for g in juntas:
                sob = min(f[1], g[1]) - max(f[0], g[0])
                if sob > 0.5 * min(f[1] - f[0], g[1] - g[0]) and not (
                        min(w[1] for w in f[2]) < max(w[1] for w in g[2]) and min(w[1] for w in g[2]) < max(w[1] for w in f[2])):
                    g[2] += f[2]
                    break
            else:
                juntas.append(f)
        juntas.sort(key=lambda f: f[0])
        paginas.append([' '.join(w[2] for w in sorted(g[2], key=lambda w: w[1])) for g in juntas])
    return paginas


def tesseract():
    return _obra_ocr(linhas_tesseract(PDF17, *PAGS17))


DICIONARIO = []


def dicionario():
    """As palavras do português (/usr/share/dict/brazilian): ocr.limpar não as troca pela da edição moderna
    (sem isso, «a compressão» de 1917 virava «a compreensão» da Ática)."""
    if not DICIONARIO and os.path.exists('/usr/share/dict/brazilian'):
        DICIONARIO.extend(l.strip() for l in open('/usr/share/dict/brazilian', encoding='utf-8', errors='ignore') if l.strip())
    return DICIONARIO


def transcricoes():
    md = modernas()
    guias = [md['bv'], md['ws']]
    out = {}
    for nome, f in (('t17', tesseract), ('c17', camada)):
        o, n = ocr.limpar(f(), guias, dicionario())
        print(f'OCR {nome}: palavras corrigidas pelas guias:', n)
        o = ocr.estrutura_como(o, md['bv'])
        for p, b in zip(o, md['bv']):
            p['titulo'] = b['titulo']
        out[nome] = o
    return out


# ------------------------------------------------------------------ publicação

# epígrafe da «Breve notícia» (1917, p. VII; conferida no fac-símile; «á», «voQfes» do OCR são «à», «voûtes»)
EPIGRAFE = ["Mon cœur profond ressemble à ces voûtes d'église", "Où le moindre bruit s'enfle en une immense voix.",
            "(Guyau. _Vers d'un philosophe_)."]

# vinheta (três pontos em triângulo) que separa o prefácio de Isaías da volta de Lima Barreto, na «Breve
# notícia» (1917, p. XII); o fluxo descarta os asteriscos, e ela volta aqui, antes do parágrafo que ela abre
SEPARADORES = {'Afora as coisas': '* * *'}


def arrumar(partes):
    """A dedicatória abre a «Breve notícia» (o site não tem página própria para ela); a vinheta volta."""
    p0 = partes[0]
    if p0['titulo'] != 'Breve notícia':
        raise SystemExit(f'primeira parte inesperada: {p0["titulo"]!r}')
    paras = []
    for x in p0['paragrafos']:
        if isinstance(x, str):
            for k, v in SEPARADORES.items():
                if x.startswith(k):
                    paras.append(v)
        paras.append(x)
    if len(paras) != len(p0['paragrafos']) + len(SEPARADORES):
        print('AVISO: vinheta da «Breve notícia» não achada')
    if not isinstance(paras[0], str) or not paras[0].startswith('Mon coeur'):
        raise SystemExit(f'epígrafe inesperada: {paras[0]!r}')
    p0['paragrafos'] = [{'verso': DEDICATORIA}, {'verso': EPIGRAFE}] + paras[1:]
    return partes


# ------------------------------------------------------------------ revisão das escolhas

def assinatura(x):
    """Chave estável de um ponto de divergência: o contexto na base e a leitura dela."""
    return f"{x['antes'][-30:]}|{x['leituras'].get(BASE)}|{x['depois'][:20]}"


def _toks(s):
    from edicao.tokens import TOK
    out = []
    for parte in re.split(r'(¶|#\S*)', s or ''):
        if parte == '¶' or parte.startswith('#'):
            out.append(parte)
        else:
            out += TOK.findall(parte)
    return out


GARBAGE = set('^|•*=~<>{}[]@$%&\\/')
LETRAS_SOLTAS = {'a', 'e', 'o', 'à', 'é', 'ó', 'A', 'E', 'O', 'À', 'É', 'Ó', 'y'}
# abreviaturas da época, que ficam (o OCR as lê bem; a edição moderna as desdobra: Senhor, São, Dona, Vossa Senhoria)
ABREV = {'Snr', 'snr', 'Sr', 'sr', 'Srs', 'srs', 'Sra', 'sra', 'Dr', 'dr', 'Drs', 'drs', 'Exa', 'Ex', 'Exma', 'Exmo',
         'Cia', 'Sta', 'Sto', 'Mme', 'Mlle', 'Mr', 'Mrs', 'etc', 'pag', 'pags', 'n', 'ns', 'Ns'}
_INGLES = set()


def _ingles():
    if not _INGLES and os.path.exists('/usr/share/dict/american-english'):
        _INGLES.update(l.strip().lower() for l in open('/usr/share/dict/american-english', encoding='utf-8', errors='ignore'))
    return _INGLES


def lixo(t):
    """Token que não pode ser do impresso: palavra inexistente, letra solta, símbolo de sujeira."""
    from edicao.tokens import e_palavra
    if t in GARBAGE or t in ("'", '’', '‘', '“', '”', '„'):
        return True
    if not e_palavra(t):
        return False
    if t in ABREV or re.fullmatch(r'[A-ZÀ-Ú]', t):
        return False
    if len(t) == 1:
        return t not in LETRAS_SOLTAS
    if re.search(r'\d', t):
        return not t.isdigit()
    if len(t) >= 4 and t.lower() in _ingles():
        return False
    return esqueleto(t) not in LEXICO()


def _sim(a, b):
    from difflib import SequenceMatcher
    a = ''.join(chave(t) for t in a if re.match(r'\w', t))
    b = ''.join(chave(t) for t in b if re.match(r'\w', t))
    if not a and not b:
        return 1.0
    return SequenceMatcher(None, a, b, autojunk=False).ratio()


def rever(tr, md, sitios):
    return _rever(tr, md, sitios, BASE, 'c17', 'bv', True)


def _rever(tr, md, sitios, base, outro, prim, com_conferencia):
    """Depois do voto: (1) os pontos conferidos no fac-símile (conferencia.json: assinatura -> 't17', 'c17'
    ou o texto) valem sobre tudo; (2) sem apoio moderno, se a leitura da edição moderna de 1917 (bv) se
    parece com a de um dos OCRs (ratio >= 0,5), vale a dela: é o impresso lido através do ruído;
    (3) varredura: onde o texto ainda tem sujeira de OCR (palavra inexistente, letra solta, símbolo) e a
    edição moderna tem um trecho do mesmo tamanho, vale o dela (relatorios/varridas.tsv); a sujeira sem
    correspondente na moderna sai."""
    from edicao.estabelecer import _aspas
    from edicao.tokens import achatar, e_palavra, texto as junta
    conf = {}
    arq = os.path.join(AQUI, 'conferencia.json')
    if com_conferencia and os.path.exists(arq):
        conf = json.load(open(arq, encoding='utf-8'))
    B = achatar(tr[base])
    usados = set()
    lidas = 0
    for x in sitios:
        L = {n: _toks(v) for n, v in x['leituras'].items() if v != '(lacuna)'}
        a = assinatura(x)
        if a in conf:
            v = conf[a]
            x['escolha'] = L[v] if v in L else _toks(v)
            x['por'] = 'conferido no fac-símile'
            x['duvida'] = False
            usados.add(a)
        elif not x['apoio'] and prim in x['modernas']:
            m = _toks(x['modernas'][prim])
            pal = lambda ts: [chave(t) for t in ts if e_palavra(t)]
            limpas = [n for n in (base, outro) if n in L and not any(lixo(t) for t in L[n])]
            junto = {n: ''.join(pal(v)) for n, v in L.items()}
            igual_m = [n for n in limpas if pal(L[n]) == pal(m)]
            # entre as que têm as palavras da moderna, a que tem também a pontuação dela
            igual_m.sort(key=lambda n: [chave(t) for t in L[n] if t != '*'] != [chave(t) for t in m if t != '*'])
            if igual_m:                          # as palavras da moderna, com a pontuação de um OCR
                x['escolha'], x['por'], x['duvida'] = L[igual_m[0]], 'OCR igual à moderna nas palavras', False
                lidas += 1
            elif limpas and len(set(junto.values())) == 1:      # os OCRs só diferem nos espaços
                x['escolha'], x['por'], x['duvida'] = L[limpas[0]], 'OCRs iguais sem os espaços', False
                lidas += 1
            elif (max(_sim(m, v) for v in L.values()) >= 0.5 and '#' not in ''.join(m)
                  and min(len(pal(v)) for v in L.values()) - 1 <= len(pal(m)) <= max(len(pal(v)) for v in L.values()) + 1):
                x['escolha'] = _aspas(B[max(0, x['s'] - 60):x['s']], [t for t in m if t != '*'])
                x['por'] = 'moderna lida nos OCRs'
                x['duvida'] = False
                lidas += 1
        x['escolha_txt'] = junta(x['escolha'])
    print('pontos sem apoio resolvidos pela moderna lida nos OCRs:', lidas)
    sobra = {k for k in conf if not k.startswith('c|')} - usados
    if sobra:
        print('conferência sem ponto correspondente:', len(sobra), list(sobra)[:5])
    E, pos = [], 0
    for x in sitios:
        E.extend(B[pos:x['s']])
        E.extend(x['escolha'])
        pos = x['e']
    E.extend(B[pos:])
    E = [t for t in E if t != '*']
    E = varrer(E, md[prim], 'varridas.tsv' if com_conferencia else 'varridas1909.tsv')
    lidos = {k: v for k, v in conf.items() if k.startswith('c|')}
    E, resto = corrigir_lidos(E, lidos)
    E = varrer_pontuacao(E, achatar(md[prim]))
    E, resto = corrigir_lidos(E, resto)          # as chaves gravadas depois da varredura da pontuação
    for k in resto:
        print('  sem lugar:', k)
    print('leituras conferidas aplicadas:', len(lidos) - len(resto), '; sem lugar:', len(resto))
    return E, sitios


def corrigir_lidos(E, corr):
    """Leituras conferidas no fac-símile fora dos pontos de divergência (pontos.py): chave
    'c|antes¦atual¦depois' (tokens separados por espaço) -> o texto impresso, na grafia de 1917.
    Devolve (E, as que não acharam lugar)."""
    resto = {}
    for k, novo in corr.items():
        _, antes, atual, depois = ['c'] + k[2:].split('¦')
        a, d, z = antes.split(), atual.split(), depois.split()
        # o ponto vizinho, já corrigido, pode ter mudado o contexto: tenta com menos contexto
        achados, aa = [], []
        for na, nz in ((len(a), len(z)), (2, 2), (len(a), 0), (0, len(z)), (1, 1)):
            aa, zz = a[len(a) - na:], z[:nz]
            pad = aa + d + zz
            if len(pad) < 3:
                continue
            achados = [i for i in range(len(E) - len(pad) + 1) if E[i:i + len(pad)] == pad]
            if len(achados) == 1:
                break
        if len(achados) != 1:
            resto[k] = novo
            continue
        i = achados[0] + len(aa)
        E = E[:i] + _toks(novo) + E[i + len(d):]
    return E, resto


VARRIDAS = []


def varrer_pontuacao(E, M):
    """Sinais que são manchas do papel lidas pelos dois OCRs, onde a edição moderna não tem nada: o ponto
    seguido de minúscula (salvo depois de abreviatura), o ponto colado a outra pontuação («animador,.»),
    a aspa angular sem par no parágrafo, e as aspas retas ou curvas, o hífen solto, «..» e «_» (1917 só usa
    aspas angulares); onde a moderna tem o sinal equivalente no mesmo lugar, ele fica (travessão,
    reticências)."""
    from edicao.tokens import alinhar, e_palavra, texto as junta
    E = list(E)
    tirar = set()
    sem_par, pilha = set(), []
    for i, t in enumerate(E):
        if t == '¶' or t.startswith('#'):
            sem_par.update(pilha); pilha = []
        elif t == '«':
            pilha.append(i)
        elif t == '»':
            if pilha:
                pilha.pop()
            else:
                sem_par.add(i)
    sem_par.update(pilha)
    EQUIV = {'-': '—', '..': '...', '_': None, '"': None, '“': None, '”': None, '„': None, '€': None, '$': None, '&': None}
    for tp, i1, i2, j1, j2 in alinhar(E, M, chave=chave):
        if tp == 'equal':
            continue
        mv = M[j1:j2]
        for i in range(i1, i2):
            t = E[i]
            if t in EQUIV:
                eq = EQUIV[t]
                if eq and eq in mv:
                    E[i] = eq
                elif t in ('"', '“', '”', '„') and any(x in ('"', '“', '”', '«', '»') for x in mv):
                    pass
                else:
                    tirar.add(i)
                continue
            if any(e_palavra(x) for x in E[i1:i2]) or any(x in ('.', '«', '»', ',', ':', ';') for x in mv):
                continue
            prox = E[i + 1] if i + 1 < len(E) else ''
            ant = E[i - 1] if i else ''
            if t == '.' and (prox[:1].islower() or prox in (',', ';', '.')) and not (
                    ant in ABREV or len(ant) == 1 and ant.isalpha() or ant in ('etc', 'Ex')):
                tirar.add(i)
            elif t == '.' and ant in (',', ';', ':'):
                tirar.add(i)
            elif t in ('«', '»') and i in sem_par:
                tirar.add(i)
    VARRIDAS.extend((junta(E[max(0, i - 6):i]), E[i], '', junta(E[i + 1:i + 7])) for i in sorted(tirar))
    print('pontuação de mancha tirada:', len(tirar))
    return [t for i, t in enumerate(E) if i not in tirar]


def varrer(E, moderna, relatorio='varridas.tsv'):
    from edicao.estabelecer import _aspas
    from edicao.tokens import achatar, alinhar, e_palavra, texto as junta
    M = achatar(moderna)
    ops = alinhar(E, M, chave=chave)
    out, pos = [], 0
    VARRIDAS.clear()
    for tp, i1, i2, j1, j2 in ops:
        if tp == 'equal':
            continue
        ev, mv = E[i1:i2], M[j1:j2]
        esq_m = {esqueleto(t) for t in mv if e_palavra(t)} | {esqueleto(t, 'k') for t in mv if e_palavra(t)}
        # sujeira: o que não é palavra conhecida nem a grafia antiga de uma palavra do trecho moderno
        if not any(lixo(t) and esqueleto(t) not in esq_m for t in ev):
            continue
        if any(t.startswith('#') for t in ev + mv) or ev.count('¶') != mv.count('¶'):
            if not mv and all(lixo(t) or t == '¶' for t in ev):
                pass                                  # sujeira pura entre parágrafos: sai
            else:
                continue
        npe = sum(e_palavra(t) for t in ev)
        npm = sum(e_palavra(t) for t in mv)
        if mv and abs(npe - npm) > max(2, npm // 2):
            continue
        novo = _aspas(out + E[pos:i1], [t for t in mv if t != '*']) if mv else [t for t in ev if t == '¶'][:1] if '¶' in ev and not mv else []
        out.extend(E[pos:i1])
        out.extend(novo)
        pos = i2
        VARRIDAS.append((junta(E[max(0, i1 - 6):i1]), junta(ev), junta(novo), junta(E[i2:i2 + 6])))
    out.extend(E[pos:])
    pasta = fontes.cache(OBRA, 'relatorios')
    os.makedirs(pasta, exist_ok=True)
    with open(os.path.join(pasta, relatorio), 'w', encoding='utf-8') as f:
        f.write('antes\tOCR\tmoderna\tdepois\n')
        for v in VARRIDAS:
            f.write('\t'.join(v) + '\n')
    print('varredura (sujeira trocada pela moderna ou tirada):', len(VARRIDAS))
    return out
