"""Poemas na língua original, sem tradução: cada palavra abre uma nota com a definição.

    python ferramentas/lingua_original.py palavras <pasta>      # as palavras do poema e a chave de cada uma
    python ferramentas/lingua_original.py wiki <es|en|fr> <página> [<língua>]
                                                                # o verbete do Wiktionary (só a seção da língua)
    python ferramentas/lingua_original.py conferir [<pasta>]    # todo o poema tem verbete; campos; mesóclise
    python ferramentas/lingua_original.py publicar              # grava o conteúdo do site

Fonte: edicoes/lingua-original/obras.json (autor, título, livro, fontes) e, por poema,
edicoes/lingua-original/<pasta>/poema.txt (formato dos poemas da Biblioteca) e glossario.json.

glossario.json:
  {"verbetes": {"<chave>": {"lema": "prenda", "wiki": "es", "classe": "substantivo feminino",
                             "forma": "plural", "def": ["Pessoa muito amada."], "nota": "..."}},
   "ocorrencias": {"<linha>.<posição>": "<chave>"}}
- a chave padrão de uma palavra é ela mesma em minúsculas (como `palavras` mostra); quando a mesma
  palavra pede outro verbete num lugar, usa-se outra chave («fair#2») e a ocorrência aponta para ela;
- wiki: o Wiktionary de onde vem a definição ("es", "fr", "en"; o da língua do poema, se faltar);
  "en:Spanish" é o en.wiktionary na seção da língua; null quando não há verbete (só a nota);
  no latim, se faltar, vale "en:Latin" (WIKI_PADRAO): `wiki en <página> Latin`, sem mácrons;
- def: a definição do sentido que vale no poema, traduzida ao português; nota: a explicação nossa,
  quando a definição sozinha não basta para entender a palavra no verso;
- palavra composta: "partes": [{lema, wiki, classe, forma, def}, ...] no lugar de lema…def.
Grava conteudo/lingua-original.js (o índice) e conteudo/<autor>/lingua-original.js (texto e notas).
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDICAO = os.path.join(RAIZ, 'edicoes', 'lingua-original')
CACHE = os.path.join(RAIZ, 'ferramentas', 'cache', 'wiktionary')
UA = 'TaioeBiblioteca/0.1 (https://taioe.com.br/biblioteca/; contato@taioe.com.br)'
NOMES_LINGUA = {'es': 'Spanish', 'fr': 'French', 'en': 'English', 'la': 'Latin'}
# o Wiktionary padrão de cada língua é o dela; o latim usa o en.wiktionary, na seção Latin
WIKI_PADRAO = {'la': 'en:Latin'}


def wiki_padrao(lingua):
    return WIKI_PADRAO.get(lingua, lingua)

PALAVRA = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*")
# francês: o artigo, o pronome ou a conjunção elididos são palavras à parte (l’aube → l’ + aube),
# e o pronome depois do hífen também (vois-tu → vois + tu); «aujourd’hui» fica inteira
ELISAO = re.compile(r"^(jusqu|lorsqu|puisqu|quoiqu|qu|l|d|j|m|t|s|n|c)['’](?=[^\W\d_])", re.I)
PRONOME = re.compile(r"-(?:t-)?(je|tu|il|elle|on|nous|vous|ils|elles|le|la|les|lui|leur|moi|toi|en|y)$", re.I)


def ler_obras():
    with open(os.path.join(EDICAO, 'obras.json'), encoding='utf-8') as f:
        return json.load(f)


def achar(pasta):
    for p in ler_obras()['poemas']:
        if p['pasta'] == pasta:
            return p
    sys.exit('poema desconhecido: ' + pasta)


def ler_texto(pasta):
    with open(os.path.join(EDICAO, pasta, 'poema.txt'), encoding='utf-8') as f:
        return f.read().replace('\r\n', '\n').strip('\n')


def separar(texto, lingua):
    """[(início, fim)] das palavras de um trecho."""
    saida = []
    for m in PALAVRA.finditer(texto):
        ini, fim = m.start(), m.end()
        if lingua == 'fr':
            while True:
                e = ELISAO.match(texto[ini:fim])
                if not e:
                    break
                saida.append((ini, ini + e.end()))
                ini += e.end()
            p = PRONOME.search(texto[ini:fim])
            if p and p.start() > 0:
                saida.append((ini, ini + p.start()))
                saida.append((ini + p.start(1), fim))
                continue
        saida.append((ini, fim))
    return saida


def chave(s):
    return s.lower()


def linhas_do_poema(poema):
    """As linhas com palavras, numeradas: 0 é o título; depois cada verso e cada marca com texto
    (::subtitulo, ::data…), na ordem do arquivo; o subtítulo de obras.json é a linha «s». Devolve [(n, texto, índice da linha no arquivo
    ou None no título, deslocamento do texto dentro da linha)]."""
    texto = ler_texto(poema['pasta'])
    saida = [(0, poema['titulo'], None, 0)]
    if poema.get('subtitulo'):
        saida.append(('s', poema['subtitulo'], 'sub', 0))   # o subtítulo de obras.json: s.1, s.2…
    n = 0
    for i, l in enumerate(texto.split('\n')):
        if not l.strip():
            continue
        m = re.match(r'^::(\w+)\s?(.*)$', l)
        if m:
            if m.group(1) not in ('subtitulo', 'data', 'dedicatoria', 'fecho'):
                continue
            valor = m.group(2).strip()
            desl = l.index(valor) if valor else 0
            n += 1
            saida.append((n, valor, i, desl))
            continue
        n += 1
        saida.append((n, l, i, 0))
    return saida


def ocorrencias(poema):
    """[(ref "linha.posição", palavra, n, linha no arquivo, início, fim)] (início e fim no texto da marca)."""
    saida = []
    for n, texto, i, desl in linhas_do_poema(poema):
        for k, (a, b) in enumerate(separar(texto, poema['lingua']), 1):
            saida.append(('%s.%d' % (n, k), texto[a:b], n, i, a, b))
    return saida


def ler_glossario(pasta):
    arq = os.path.join(EDICAO, pasta, 'glossario.json')
    if not os.path.exists(arq):
        return None
    with open(arq, encoding='utf-8') as f:
        return json.load(f)


# ------------------------------------------------------------------ palavras
def cmd_palavras(pasta):
    poema = achar(pasta)
    linha_atual = None
    for ref, palavra, n, i, a, b in ocorrencias(poema):
        if n != linha_atual:
            linha_atual = n
            texto = [t for (m, t, _, _) in linhas_do_poema(poema) if m == n][0]
            print('\n%s  %s' % (n, texto))
        print('    %-6s %-20s chave: %s' % (ref, palavra, chave(palavra)))
    unicas = sorted({chave(p) for (_, p, *_r) in ocorrencias(poema)})
    print('\n%d palavras, %d chaves diferentes' % (len(ocorrencias(poema)), len(unicas)))


# ------------------------------------------------------------------ wiki
def baixar(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for tentativa in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception:
            if tentativa == 3:
                raise
            time.sleep(2 * (tentativa + 1))


def wikitext(wiki, pagina):
    # pasta c2: no Windows «Land» e «land» seriam o mesmo arquivo; a maiúscula vai marcada com ^
    os.makedirs(os.path.join(CACHE, wiki, 'c2'), exist_ok=True)
    nome = re.sub(r'[<>:"/\\|?*^]', lambda m: '%%%02X' % ord(m.group()), pagina)
    nome = ''.join('^' + c if c != c.lower() else c for c in nome) + '.json'
    arq = os.path.join(CACHE, wiki, 'c2', nome)
    if os.path.exists(arq):
        with open(arq, encoding='utf-8') as f:
            return json.load(f)
    url = 'https://%s.wiktionary.org/w/api.php?' % wiki + urllib.parse.urlencode({
        'action': 'parse', 'page': pagina, 'prop': 'wikitext', 'format': 'json', 'formatversion': 2, 'redirects': 1})
    d = baixar(url)
    res = {'titulo': d.get('parse', {}).get('title'), 'wikitext': d.get('parse', {}).get('wikitext'),
           'erro': d.get('error', {}).get('code')}
    with open(arq, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False)
    time.sleep(0.3)
    return res


def secao_da_lingua(wt, wiki, lingua):
    """Só a seção da língua pedida dentro do verbete."""
    if wiki == 'en':
        nome = NOMES_LINGUA.get(lingua, lingua)
        partes = re.split(r'(?m)^==([^=].*?)==\s*$', wt)
        for k in range(1, len(partes), 2):
            if partes[k].strip() == nome:
                return '==' + nome + '==' + partes[k + 1]
        return None
    if wiki == 'es':
        partes = re.split(r'(?m)^==\s*\{\{lengua\|([a-z-]+)\}\}\s*==\s*$', wt)
    else:
        partes = re.split(r'(?m)^==\s*\{\{langue\|([a-z-]+)\}\}\s*==\s*$', wt)
    for k in range(1, len(partes), 2):
        if partes[k] == lingua:
            return partes[k + 1]
    return None


def cmd_wiki(wiki, pagina, lingua=None):
    lingua = lingua or wiki
    r = wikitext(wiki, pagina)
    if r['erro'] or not r['wikitext']:
        print('(sem verbete «%s» no %s.wiktionary: %s)' % (pagina, wiki, r['erro']))
        return
    sec = secao_da_lingua(r['wikitext'], wiki, lingua)
    print('https://%s.wiktionary.org/wiki/%s' % (wiki, urllib.parse.quote(r['titulo'].replace(' ', '_'))))
    if sec is None:
        print('(o verbete existe, mas sem a seção da língua «%s»)' % lingua)
        return
    print(compacto(sec)[:30000])


FORA = re.compile(r'(?i)translations|traducciones|traductions|pronunciation|prononciation|anagram|references|'
                  r'références|further reading|voir aussi|see also|descendants|derived terms|related terms|'
                  r'synonymes|antonymes|dérivés|apparentés|hyperonymes|hyponymes|vocabulaire|holonymes|méronymes|'
                  r'quotations|informaciones adicionales|véase también|refranes|locuciones|anagramas|'
                  r'homophones|paronymes|anagrammes|compos|gentilés|proverbes|phrases|traduction|cognates|etymology|étymologie')


def compacto(sec):
    """Cabeçalhos, a linha da palavra e as definições; sem traduções, exemplos, pronúncia e etimologia."""
    saida, pular = [], False
    for l in sec.split('\n'):
        m = re.match(r'^(=+)\s*(.*?)\s*=+\s*$', l)
        if m:
            pular = bool(FORA.search(m.group(2)))
            if not pular:
                saida.append(l)
            continue
        if pular or not l.strip() or re.match(r'^\s*\|', l) or 'passage=' in l or l.startswith('<references'):
            continue
        if re.match(r'^(#[*:]|:\*|\*\s*\{\{(?:T|t|audio)|\{\{(?:t\+?|trad|ejemplo|sinónimo|antónimo|relacionado|derivad|uso|'
                    r'col-|top|mid|bottom|rel-|der-|\(|\)|clear|-|ébauche|wikipedia|pron-graf|audio))', l):
            continue
        saida.append(l)
    return '\n'.join(saida).strip()


# ------------------------------------------------------------------ conferir
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")
CAMPOS = {'lema', 'wiki', 'classe', 'forma', 'def', 'nota', 'partes'}


def conferir_parte(x, onde, problemas, lingua):
    if not isinstance(x.get('lema'), str) or not x['lema'].strip():
        problemas.append(onde + ': falta o lema')
    w = x.get('wiki', wiki_padrao(lingua))
    if w is not None and not re.match(r'^(es|fr|en)(:[A-Z][a-z]+)?$', str(w)):
        problemas.append(onde + ': wiki inválido ' + repr(w))
    if w is not None and not x.get('def'):
        problemas.append(onde + ': com wiki e sem definição')
    if 'def' in x and not (isinstance(x['def'], list) and all(isinstance(d, str) and d.strip() for d in x['def'])):
        problemas.append(onde + ': def tem de ser lista de textos')
    if not x.get('classe'):
        problemas.append(onde + ': falta a classe')


def conferir(pasta, verboso=True):
    poema = achar(pasta)
    g = ler_glossario(pasta)
    problemas = []
    if g is None:
        return ['%s: sem glossario.json' % pasta]
    vb, oc = g.get('verbetes', {}), g.get('ocorrencias', {})
    usados = set()
    refs = set()
    for ref, palavra, *_r in ocorrencias(poema):
        refs.add(ref)
        k = oc.get(ref, chave(palavra))
        if k not in vb:
            problemas.append('%s: «%s» (%s) sem verbete «%s»' % (pasta, palavra, ref, k))
        usados.add(k)
    for ref in oc:
        if ref not in refs:
            problemas.append('%s: ocorrência %s não existe' % (pasta, ref))
    for k, x in vb.items():
        onde = '%s: verbete «%s»' % (pasta, k)
        if k not in usados:
            problemas.append(onde + ' não é usado')
        extra = set(x) - CAMPOS
        if extra:
            problemas.append(onde + ': campos desconhecidos ' + ', '.join(sorted(extra)))
        if 'partes' in x:
            if not x['partes']:
                problemas.append(onde + ': partes vazia')
            for j, p in enumerate(x['partes']):
                conferir_parte(p, onde + ' parte %d' % (j + 1), problemas, poema['lingua'])
        else:
            conferir_parte(x, onde, problemas, poema['lingua'])
            if x.get('wiki', wiki_padrao(poema['lingua'])) is None and not x.get('nota'):
                problemas.append(onde + ': sem Wiktionary e sem nota')
        texto = json.dumps(x, ensure_ascii=False)
        if MESOCLISE.search(texto):
            problemas.append(onde + ': mesóclise')
    if verboso:
        print('%s: %d palavras, %d verbetes%s' % (pasta, len(refs), len(vb), '' if problemas else ', tudo certo'))
    return problemas


def cmd_conferir(pasta=None):
    pastas = [pasta] if pasta else [p['pasta'] for p in ler_obras()['poemas']]
    problemas = []
    for p in pastas:
        problemas += conferir(p)
    for x in problemas[:80]:
        print('  ' + x)
    if len(problemas) > 80:
        print('  … e mais %d' % (len(problemas) - 80))
    return not problemas


# ------------------------------------------------------------------ publicar
def url_wiki(wiki, lema, lingua):
    wiki = WIKI_PADRAO.get(wiki, wiki)   # "la" (não há la.wiktionary aqui) é o en.wiktionary, seção Latin
    w = wiki.split(':')[0]
    u = 'https://%s.wiktionary.org/wiki/%s' % (w, urllib.parse.quote(lema.replace(' ', '_'), safe="'’-"))
    if ':' in wiki:
        u += '#' + wiki.split(':')[1]
    elif w == 'en' and lingua != 'en':
        u += '#' + NOMES_LINGUA[lingua]
    return u


def parte_publica(x, lingua):
    w = x.get('wiki', wiki_padrao(lingua))
    d = {'l': x['lema'], 'c': x.get('classe', '')}
    if x.get('forma'):
        d['f'] = x['forma']
    if x.get('def'):
        d['d'] = x['def']
    if w is not None:
        d['u'] = url_wiki(w, x['lema'], lingua)
    return d


PROVISORIO = False   # publicar --provisorio: só para ver o site no local, com notas vazias onde faltam


def areas_dos_autores():
    """A área de cada autor em conteudo/autores.js («area»; sem ela, a Literatura). Os textos de
    autor do Catolicismo (as orações) não são poemas: a página «Sobre» fala em «texto»."""
    with open(os.path.join(RAIZ, 'conteudo', 'autores.js'), encoding='utf-8') as f:
        js = f.read()
    areas = {}
    for bloco in re.findall(r'BIBLIOTECA\.autor\(\{(.*?)\}\);', js, re.S):
        i = re.search(r"\bid:\s*'([^']+)'", bloco)
        a = re.search(r"\barea:\s*'([^']+)'", bloco)
        if i:
            areas[i.group(1)] = a.group(1) if a else 'literatura'
    return areas


def publicar():
    obras = ler_obras()
    if not cmd_conferir() and not PROVISORIO:
        sys.exit('corrija os problemas antes de publicar')
    areas = areas_dos_autores()
    autores = []
    por_autor = {}
    for p in obras['poemas']:
        if p['autor'] not in por_autor:
            autores.append(p['autor'])
            por_autor[p['autor']] = []
        por_autor[p['autor']].append(p)
    indice = ['/* Poemas na língua original, sem tradução: cada palavra abre uma nota com a definição.',
              '   Gerado por ferramentas/lingua_original.py a partir de edicoes/lingua-original/; não edite à mão.',
              '   O texto e as notas de cada autor ficam em conteudo/<autor>/lingua-original.js. */', '']
    for autor in autores:
        livros, poemas = [], []
        for k, p in enumerate(por_autor[autor]):
            livro = -1
            if p.get('livro'):
                livros.append({'id': re.sub(r'[^a-z0-9]+', '-', p['livro']['titulo'].lower()).strip('-'),
                               'titulo': p['livro']['titulo'], 'ano': p['livro'].get('ano')})
                livro = len(livros) - 1
            texto = ler_texto(p['pasta'])
            versos = sum(1 for l in texto.split('\n') if l.strip() and not l.startswith('::'))
            item = {'id': autor + '-' + p['pasta'], 'titulo': p['titulo'], 'forma': p['forma'], 'livro': livro,
                    'ordem': k, 'versos': versos, 'lingua': p['lingua'], 'ano': p.get('ano'), 'glossario': True}
            if p.get('subtitulo'):
                item['subtitulo'] = p['subtitulo']
            if p.get('genero'):
                item['genero'] = p['genero']   # sem ele, Poesia (as orações levam "Orações")
            if p.get('traducao'):
                tr = p['traducao']
                item['pt'] = {'tradutor': tr['tradutor'], 'titulo': tr['titulo'], 'ano': tr.get('ano')}
            poemas.append(item)
        arquivo = 'conteudo/%s/lingua-original.js' % autor
        indice.append('BIBLIOTECA.poemas({\n  autor: %s,\n  arquivo: %s,\n  livros: %s,\n  poemas: [\n    %s\n  ]\n});\n' % (
            json.dumps(autor), json.dumps(arquivo), json.dumps(livros, ensure_ascii=False),
            ',\n    '.join(json.dumps(x, ensure_ascii=False, separators=(',', ':')) for x in poemas)))
        textos = {}
        poesia = areas.get(autor, 'literatura') != 'catolicismo'
        for p in por_autor[autor]:
            textos[autor + '-' + p['pasta']] = montar(p, obras['linguas'][p['lingua']], poesia)
        os.makedirs(os.path.join(RAIZ, 'conteudo', autor), exist_ok=True)
        with open(os.path.join(RAIZ, arquivo), 'w', encoding='utf-8', newline='\n') as f:
            f.write('/* %s de %s na língua original, com as notas de cada palavra.\n'
                    '   Gerado por ferramentas/lingua_original.py; não edite à mão.\n'
                    '   t: texto; g: notas (v: verbetes; o: [linha do texto, início, fim, verbete]; t: o mesmo no título);\n'
                    '   e: página «Sobre». As definições vêm do Wiktionary (CC BY-SA 4.0), traduzidas. */\n'
                    % ('Poemas' if poesia else 'Textos', autor))
            f.write('BIBLIOTECA.textos({\n')
            f.write(',\n'.join('%s: %s' % (json.dumps(k), json.dumps(v, ensure_ascii=False, separators=(',', ':')))
                               for k, v in textos.items()))
            f.write('\n});\n')
    with open(os.path.join(RAIZ, 'conteudo', 'lingua-original.js'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(indice))
    # o gerador lê o conteúdo na ordem dos <script> do index.html antigo
    arq = os.path.join(RAIZ, 'index.html')
    with open(arq, encoding='utf-8') as f:
        html = f.read()
    linha = '<script defer src="conteudo/lingua-original.js"></script>'
    if linha not in html:
        html = html.replace('<script defer src="conteudo/poesia.js"></script>',
                            '<script defer src="conteudo/poesia.js"></script>\n' + linha, 1)
        with open(arq, 'w', encoding='utf-8', newline='') as f:
            f.write(html)
    print('publicado: %d poemas de %d autores' % (len(obras['poemas']), len(autores)))


def montar(p, info_lingua, poesia=True):
    lingua = p['lingua']
    g = ler_glossario(p['pasta'])
    if PROVISORIO and (g is None or conferir(p['pasta'], False)):
        g = {'verbetes': {chave(x[1]): {'lema': x[1], 'classe': '(em preparo)', 'def': ['(nota em preparo)']} for x in ocorrencias(p)}}
    vb, oc = g['verbetes'], g.get('ocorrencias', {})
    ids, verbetes = {}, {}
    o_linhas, o_titulo, o_sub = [], [], []
    for ref, palavra, n, i, a, b in ocorrencias(p):
        k = oc.get(ref, chave(palavra))
        if k not in ids:
            ids[k] = len(ids)
            x = vb[k]
            v = {'p': [parte_publica(y, lingua) for y in x['partes']]} if 'partes' in x else {'p': [parte_publica(x, lingua)]}
            if x.get('nota'):
                v['n'] = x['nota']
            verbetes[ids[k]] = v
        if i is None:
            o_titulo.append([a, b, ids[k]])
        elif i == 'sub':
            o_sub.append([a, b, ids[k]])
        else:
            desl = [d for (m, _t, _i, d) in linhas_do_poema(p) if m == n][0]
            o_linhas.append([i, a + desl, b + desl, ids[k]])
    fontes = [{'nome': f['nome'], 'url': f.get('url'), 'nota': f.get('nota')} for f in p.get('fontes', [])]
    wiki = wiki_padrao(lingua).split(':')[0]
    outro = wiki != lingua   # o latim: as definições vêm do en.wiktionary
    fontes.append({'nome': 'Wiktionary', 'url': 'https://%s.wiktionary.org/' % wiki,
                   'nota': ('definições das notas, da seção de %s do Wiktionary em inglês, traduzidas ao português '
                            '(CC BY-SA 4.0)' % info_lingua['nome']) if outro
                   else 'definições das notas, traduzidas ao português (CC BY-SA 4.0)'})
    tr = p.get('traducao')
    apresentacao = ('Texto em %s%s. Toque numa palavra para ver a nota: a definição do sentido que ela tem '
                    'no %s, traduzida do Wiktionary%s, com o link para o verbete original, e, quando é preciso, uma '
                    'explicação do uso %s.\n\nAs notas, como o Wiktionary, estão sob a '
                    'licença CC BY-SA 4.0.') % (info_lingua['nome'], '' if tr else ', sem tradução',
                                                'poema' if poesia else 'texto', ' em inglês' if outro else '',
                                                'no verso' if poesia else 'na frase')
    if tr:
        # uma tradução em domínio público, com o nome do tradutor (pedido de 2026-10-20); nunca uma nossa
        apresentacao += ('\n\n**Tradução.** No botão «Português», a tradução de %s, %s, em domínio público, '
                         'na ortografia de hoje.') % (tr['tradutor'], tr['publicacao'])
        fontes.insert(len(fontes) - 1, {'nome': tr['fonte']['nome'], 'url': tr['fonte'].get('url'), 'nota': tr['fonte'].get('nota')})
    saida = {'t': [ler_texto(p['pasta'])],
             'g': [{'v': verbetes, 'o': o_linhas, 't': o_titulo, 's': o_sub}],
             'e': {'titulo': 'Sobre este texto', 'apresentacao': apresentacao,
                   'fontes': [{k: v for k, v in f.items() if v} for f in fontes]}}
    if tr:
        with open(os.path.join(EDICAO, p['pasta'], 'traducao.txt'), encoding='utf-8') as f:
            saida['p'] = [f.read().replace('\r\n', '\n').strip('\n')]
    return saida


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == 'palavras' and len(a) == 2:
        cmd_palavras(a[1])
    elif a[0] == 'wiki' and len(a) in (3, 4):
        cmd_wiki(*a[1:])
    elif a[0] == 'conferir':
        sys.exit(0 if cmd_conferir(a[1] if len(a) > 1 else None) else 1)
    elif a[0] == 'publicar':
        PROVISORIO = '--provisorio' in a
        publicar()
    else:
        sys.exit(__doc__)
