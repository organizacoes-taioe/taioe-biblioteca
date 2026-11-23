"""O Uraguai (Basílio da Gama, 1769): o texto da 1ª edição na grafia brasileira de hoje.

uso:
  python3 edicoes/o-uraguai/montar.py             refaz texto.txt (os versos) a partir do confronto (precisa do cache)
  python3 edicoes/o-uraguai/montar.py --publicar  grava conteudo/basilio-da-gama/o-uraguai.js a partir de
                                                  texto.txt, notas.txt e abertura.txt (não precisa do cache)

Passo a passo das fontes (cache em ferramentas/cache/o-uraguai/, fora do git; ou na variável URAGUAI_CACHE):
  1. baixar_ws.py e ws_parse.py: a transcrição da 1ª edição no Wikisource (O Uraguay, páginas do DjVu) → ws1769.json;
     o texto em grafia atualizada do Wikisource (O Uraguai/I…V) vai em wsmod/I.txt … V.txt (comum.wsmod).
  2. Os dois exemplares de 1769 no Internet Archive: bos/ouruaguaypoema00gama.pdf (Boston Public Library) e
     tor/ouraguaypoema00gama.pdf (Fisher, Toronto); mapa_tor.json liga as páginas (Toronto = Boston + 6).
  3. ocr.py <pdf> <pasta>: Tesseract (por) em cada página → bos/tess, tor/tess (tsv e jpg).
  4. confronto.py → confronto.json: para cada verso do texto moderno, as leituras do WS de 1769 (páginas revisadas),
     da camada OCR dos dois PDFs (AB, AT) e do Tesseract (TB, TT).
  5. difs.py lista as diferenças de palavra; pontuacao.py vota a pontuação (pontuacao.json) e lista os empates;
     recorte.py faz as pranchas de recortes dos dois exemplares para decidir na imagem.
  6. As decisões: decisoes.json (palavras, versos, grafia) e pontuacao_conferida.json (empates da pontuação).

O esqueleto é o texto moderno do Wikisource (palavras na grafia de hoje), corrigido pela 1ª edição: a lição e a
pontuação são as de 1769.
"""
import json, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, AQUI)
DEC = json.load(open(os.path.join(AQUI, 'decisoes.json'), encoding='utf-8'))
TEXTO = os.path.join(AQUI, 'texto.txt')
PALAVRA = re.compile(r"[^\W\d_]+(?:[-’'][^\W\d_]+)*")
CANTOS = ['Canto Primeiro', 'Canto Segundo', 'Canto Terceiro', 'Canto Quarto', 'Canto Quinto']


def contracoes(l):
    """«com» + artigo numa notação só, como n'Os Lusíadas: co'o, co'a, co'os, co'as."""
    l = l.replace('’', "'").replace('côas', "co'as")
    l = re.sub(r"\b([Cc])o's\b", r"\1o'os", l)
    l = re.sub(r"\b([Cc])os\b", r"\1o'os", l)
    l = re.sub(r"\b([Cc])o (as?)\b", r"\1o'\2", l)
    l = re.sub(r"\b([Cc])o (?!(?:ele|ela|eles|elas|isto|isso)\b)(?=\w)", r"\1o'o ", l)
    return l


def verso(c, v, mod, pont, pontc):
    chave = '%d,%d' % (c, v)
    if chave in DEC['linhas']:
        return DEC['linhas'][chave]
    ws = PALAVRA.findall(mod)
    out = []
    vistos = {}
    for k, w in enumerate(ws):
        vistos[w] = vistos.get(w, 0) + 1
        dk = '%s|%s' % (chave, w)
        if vistos[w] > 1 and dk + '#%d' % vistos[w] in DEC['palavras']:
            dk += '#%d' % vistos[w]
        s = DEC['palavras'].get(dk, w) if vistos[w] == 1 or '#' in dk else w
        s = DEC['grafia'].get(s, s)
        p = pontc.get('%s,%d' % (chave, k), pont[k] if k < len(pont) else '')
        if s:
            out.append(s + p)
        elif p and out:
            out[-1] += p
    l = ' '.join(out)
    l = l.replace('…', '...')
    l = contracoes(l)
    return l[:1].upper() + l[1:]


def montar():
    from comum import wsmod
    import json as _j
    D = os.environ.get('URAGUAI_CACHE') or os.path.join(RAIZ, 'ferramentas', 'cache', 'o-uraguai')
    pont = _j.load(open(os.path.join(D, 'pontuacao.json'), encoding='utf-8'))
    pontc = _j.load(open(os.path.join(AQUI, 'pontuacao_conferida.json'), encoding='utf-8'))
    mod = wsmod()
    with open(TEXTO, 'w', encoding='utf-8', newline='\n') as f:
        for c in range(1, 6):
            f.write('# %s\n' % CANTOS[c - 1])
            for v, m in enumerate(mod[c], 1):
                f.write(verso(c, v, m, pont['%d,%d' % (c, v)], pontc) + '\n')
            f.write('\n')
    print('gravado', TEXTO, sum(len(x) for x in mod.values()), 'versos')


if __name__ == '__main__':
    if '--publicar' in sys.argv:
        import publicar
        publicar.publicar()
    else:
        montar()
