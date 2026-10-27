"""Os Lusíadas — leitura das duas fontes e chave de grafia.

  1572  1ª edição (Lisboa, António Gonçalves), transcrição diplomática do Projeto Gutenberg nº 27236,
        feita sobre as imagens da Biblioteca Nacional de Portugal: a base da lição;
  ws    Wikisource, «Os Lusíadas (grafia atualizada)»: a base da pontuação, da divisão em versos e da
        grafia (portuguesa, anterior ao Acordo; passada à brasileira em montar.py).
Os arquivos ficam em ferramentas/cache/os-lusiadas/ (fora do git): pg27236.txt e ws-I.txt … ws-X.txt
(o wikitexto de cada canto).
"""
import re, sys, unicodedata
import os
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
from edicao.tokens import alinhar
D = os.path.join(AQUI, '..', '..', 'ferramentas', 'cache', 'os-lusiadas') + os.sep
CANTOS = 'I II III IV V VI VII VIII IX X'.split()

def ws_estrofes():
    """[(canto, n, [linhas])] do Wikisource, sem links."""
    out = []
    for c in CANTOS:
        t = open(D + f'ws-{c}.txt').read()
        p = re.search(r'<poem>(.*?)</poem>', t, re.S).group(1)
        p = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', p)
        p = re.sub(r'\{\{[^{}]*\}\}', '', p)
        for bloco in re.split(r'\n\s*\n', p.strip()):
            ls = [l.rstrip() for l in bloco.split('\n') if l.strip() and not re.search(r'\d+px', l)]
            m = re.match(r'::+\s*(\d+)', ls[0]) if ls else None
            if not m:
                if ls: print('bloco sem número', c, ls[:2], file=sys.stderr)
                continue
            out.append((c, int(m.group(1)), ls[1:]))
    return out

def g_texto():
    g = open(D + 'pg27236.txt').read()
    i = g.find('As armas, & os ba-'); j = g.find('*** END')
    return g[i:j]

def sem_acento(w):
    w = unicodedata.normalize('NFD', w)
    til = w.replace('̃', '~')
    return ''.join(ch for ch in til if unicodedata.category(ch) != 'Mn')

def chave(w):
    """Colapsa só as diferenças de grafia (não de pronúncia)."""
    w = w.lower().replace('ſ', 's').replace('-', '').replace("'", '').replace('’', '').replace(' ', '')
    w = sem_acento(w)
    w = w.replace('ph', 'f').replace('th', 't').replace('rh', 'r').replace('y', 'i')
    w = re.sub(r'ch(?=r|l)', 'c', w)
    w = re.sub(r'^h', '', w); w = re.sub(r'(?<=[aeiou])h(?=[aeiou])', '', w)
    w = w.replace('u~', 'um').replace('e~', 'en').replace('i~', 'in').replace('o~', 'on')
    w = re.sub(r'a~o$|a~o(?=s$)|am$', 'AO', w); w = re.sub(r'a~(?=[os])', 'AO', w)
    w = re.sub(r'am(?=s$)', 'AO', w)
    w = re.sub(r'a~e|a~i', 'AE', w); w = w.replace('a~', 'AN')
    w = re.sub(r'(?<=[a-z])v(?=[^aeiou]|$)', 'u', w)
    w = w.replace('v', 'u').replace('j', 'i')
    w = re.sub(r'([bcdfglmnprst])\1', r'\1', w)
    w = re.sub(r'c(?=t)|p(?=t)|m(?=pt)|b(?=d)', '', w); w = w.replace('pt', 't')
    w = re.sub(r'sc(?=[ei])', 'c', w); w = re.sub(r'ç(?=[ei])', 'c', w)
    w = re.sub(r'([ei])o(s?)$', r'\1u\2', w)          # Deos, ceo, vio
    w = re.sub(r'ao(s?)$', r'au\1', w)                 # mao, naos, pao
    w = re.sub(r'ae(s?)$', r'ai\1', w)                 # quaes, reaes
    w = re.sub(r'ue(s?)$', r'ui\1', w)                 # azues
    w = re.sub(r'([gq])o(?=a)', r'\1u', w)             # agoa, lingoa, igoal
    w = w.replace('ct', 't').replace('qu', 'k').replace('c', 'k')
    w = w.replace('z', 's').replace('ss', 's').replace('ç', 's')
    w = re.sub(r'ei(?=a)', 'e', w)                     # cheia/chea, feia/fea: ver a regra
    return w

def g_estrofes():
    """[(canto, [palavras])] da 1ª edição, uma entrada por estrofe."""
    g = g_texto()
    partes = re.split(r'\n❧ Canto [^\n]*\n|\nCanto primeiro\.\n', '\n' + g)
    out = []
    for c, p in zip(CANTOS, [x for x in partes if x.strip()]):
        fim = p.find('\nFIM')
        if fim > 0: p = p[:fim]
        for b in re.split(r'\n\s*\n', p.strip()):
            b = re.sub(r'-\n', '', b)
            ms = list(re.finditer(r"[^\W\d_]+|&", b))
            pal = [("e" if m.group() == "&" else m.group()) for m in ms]
            fim = [('\n' in b[m.end():(ms[i + 1].start() if i + 1 < len(ms) else len(b))]) for i, m in enumerate(ms)]
            if len(pal) > 3: out.append((c, pal, b, fim))
    return out
