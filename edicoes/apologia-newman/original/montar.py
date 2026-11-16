"""Monta os arquivos do original inglês da Apologia pro Vita Sua (Newman) a partir do Gutenberg #22088.

Uso: python3 -I montar.py <caminho do 22088-0.txt>
O texto baixado não fica no repositório; o resultado, sim (NN-<nome>.txt, nesta pasta).
Ver LEIAME.md: fonte, edição, o que foi tirado, notas do autor, cortes.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTE = '# fonte: Project Gutenberg, eBook #22088 (https://www.gutenberg.org/ebooks/22088), arquivo 22088-0.txt (revisão de 2024-05-14)'
EDICAO = ('# edicao: John Henry Cardinal Newman, Apologia pro Vita Sua: being a History of his Religious Opinions '
          '(London: Longmans, Green, and Co., 1890), forma final do texto (a de 1865, com o título de 1873 e as notas acrescentadas até 1890)')
NOTA_PADRAO = ('# nota: um parágrafo por bloco; «## » título interno do autor; «* * *» quebra do autor; notas de rodapé do autor '
               'renumeradas a partir de 1 em cada arquivo, chamada «[n]» e texto em «¤ [n] …» no fim do arquivo; '
               'itálico «_assim_»; travessão «--» como no Gutenberg')

PEQUENAS = {'and', 'of', 'the', 'to', 'in', 'on', 'from', 'a', 'an', 'for', 'by', 'at', 'or', 'with', 'page', 'pages'}


def caso_titulo(t):
    """«SEVENTH AND EIGHTH CENTURIES.» → «Seventh and Eighth Centuries.»; «II.--THE DIOCESE» → «II.--The Diocese»."""
    out, inicio = [], True
    for w in re.split(r'( |--)', t):
        if w in (' ', '--'):
            out.append(w)
            if w == '--':
                inicio = True
            continue
        m = re.match(r'^([^A-Za-zÀ-ÿ]*)([A-Za-zÀ-ÿ\'’.]*?)([.,:;"]*)$', w)
        if not m:
            out.append(w)
            continue
        pre, core, pos = m.groups()
        if re.fullmatch(r'([A-Z]\.)+[A-Z]?', core + pos[:1]) or re.fullmatch(r'[IVXLC]+', core):
            out.append(w)          # iniciais (E., J. H. N.) e romanos ficam
        elif not inicio and core.lower() in PEQUENAS:
            out.append(pre + core.lower() + pos)
        else:
            out.append(pre + core[:1].upper() + core[1:].lower().replace("'s", "'s") + pos)
        inicio = bool(re.fullmatch(r'[IVXLC]+', core)) and pos.startswith('.')
    return ''.join(out).replace('. And ', '. and ')


def blocos(texto):
    out, cur = [], []
    for l in texto.split('\n'):
        if l.strip():
            cur.append(l.rstrip())
        elif cur:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def ehmaiusc(b):
    t = ' '.join(x.strip() for x in b)
    letras = re.sub(r'[^A-Za-zÀ-ÿ]', '', t)
    return letras and letras == letras.upper() and len(letras) > 2


def junta(b):
    return re.sub(r' {2,}', ' ', ' '.join(x.strip() for x in b)).strip()


# Versos latinos citados (os dois únicos «poem» do HTML do Gutenberg)
VERSOS = ('"Victrix causa diis placuit', '"Pentheu,')
ESTRELAS = re.compile(r'^\*(\s+\*){4}$')
NOTA_RODAPE = re.compile(r'^\[(\d+)\] ')


def paragrafos(bls, cabecalhos=()):
    """Blocos do Gutenberg → parágrafos do arquivo; notas de rodapé renumeradas e postas no fim."""
    corpo, notas, mapa = [], [], {}
    for b in bls:
        t = junta(b)
        if ESTRELAS.match(t):
            corpo.append('* * *')
        elif t.startswith(VERSOS):
            corpo.append('\n'.join('| ' + re.sub(r' {2,}', ' ', x.strip()) for x in b))
        elif NOTA_RODAPE.match(t):
            n = NOTA_RODAPE.match(t).group(1)
            assert n in mapa, f'nota [{n}] sem chamada'
            notas.append('¤ ' + NOTA_RODAPE.sub(f'[{mapa[n]}] ', t))
        elif t in cabecalhos or t.startswith('§ ') and len(t) < 6:
            corpo.append('## ' + (caso_titulo(t) if ehmaiusc(b) else t))
        else:
            def troca(m):
                mapa.setdefault(m.group(1), str(len(mapa) + 1))
                return f'[{mapa[m.group(1)]}]'
            corpo.append(re.sub(r'\[(\d+)\]', troca, t))
    assert len(notas) == len(mapa), (len(notas), len(mapa))
    return corpo + notas


# ---------------------------------------------------------------- Nota D: o calendário dos santos
CAL_ENTRADA = re.compile(r'^(\s*\d{1,4}(-\d+)?( |----|$)|\s{2,8}(Jan|Feb|Mar|Ap|Apr|May|June|July|Aug|Sept|Oct|Nov|Dec)\b|'
                         r'(bef|abt|aft)\. |\s*----|\s+")')
# grupos marcados por chave no impresso: (primeiro nome do grupo, entradas, rótulo)
CAL_GRUPOS = [('Mellitus', 5, 'Companions of St. Augustine.'),
              ('Idaburga', 5, 'Daughters of King Penda.'),
              ('Milburga', 3, 'Grand-daughters of Penda.'),
              ('Willibald', 3, 'Children of St. Richard.'),
              ('Willibald', 6, 'Companions of St. Boniface.'),
              ('Wigbert', 7, 'Companions of St. Boniface.')]
CAL_TITULOS = re.compile(r'^([A-Z][A-Z ]+\.|Part [IVX]+\..*|Welsh Schools\.|Missions\.)$')


def calendario(bls):
    """Linhas do calendário: «| » por linha (não é verso: só guarda as linhas da lista); títulos em «## »."""
    out = []
    for b in bls:
        linhas = list(b)
        while linhas and CAL_TITULOS.match(linhas[0].strip()):
            t = linhas.pop(0).strip()
            out.append('## ' + (caso_titulo(t) if t == t.upper() else t))
        if not linhas:
            continue
        if linhas[0].startswith('N.B.'):
            out.append(junta(linhas))
            continue
        ent, chave = [], []
        for l in linhas:
            esq = l.split('}')[0].rstrip()
            if ent and not CAL_ENTRADA.match(l):
                ent[-1] = (ent[-1] + ' ' + esq.strip()).strip()
                chave[-1] = chave[-1] or '}' in l
            else:
                ent.append(re.sub(r' {2,}', ' ', esq.strip()))
                chave.append('}' in l)
        # rótulos das chaves, depois da última entrada de cada grupo
        fins = {}
        for nome, n, rot in CAL_GRUPOS:
            for k, e in enumerate(ent):
                if chave[k] and nome in e and not any(chave[j] and nome in ent[j] for j in range(k)):
                    fins.setdefault(k + n - 1, []).append(rot)
        linhas_out = []
        for k, e in enumerate(ent):
            linhas_out.append('| ' + e if e else '|')
            for rot in fins.get(k, []):
                linhas_out.append('| } ' + rot)
        out.append('\n'.join(linhas_out))
    return out


def gravar(nome, titulo, corpo, nota=NOTA_PADRAO):
    cab = [f'# titulo: {titulo}', FONTE, EDICAO, nota]
    txt = '\n'.join(cab) + '\n\n' + '\n\n'.join(corpo).strip() + '\n'
    open(os.path.join(AQUI, nome), 'w', encoding='utf-8').write(txt)
    pal = sum(len(re.sub(r'^[|#¤]+ ?', '', p, flags=re.M).split()) for p in corpo)
    print(f'{nome}: {len(corpo)} parágrafos, {pal} palavras')


def main(arq):
    texto = open(arq, encoding='utf-8').read().replace('\r', '')
    texto = texto.split('*** START OF THE PROJECT GUTENBERG EBOOK 22088 ***', 1)[1]
    texto = texto.split('*** END OF THE PROJECT GUTENBERG EBOOK 22088 ***', 1)[0]
    texto = texto.replace('EXTRACT OF A LETTER PROM THE REV.', 'EXTRACT OF A LETTER FROM THE REV.')  # erro de digitação do Gutenberg
    texto = texto.replace('[oe]', 'œ')   # ligadura que o Gutenberg escreveu entre colchetes (man[oe]uvre)
    bl = blocos(texto)
    tx = [junta(b) for b in bl]

    def idx(t, desde=0):
        return tx.index(t, desde)

    # ---- prefácio
    i0, i1 = idx('PREFACE.'), idx('CONTENTS.')
    gravar('00-prefacio.txt', 'Apologia pro Vita Sua — Preface', paragrafos(bl[i0 + 1:i1]))

    # ---- capítulos
    caps = [idx(f'CHAPTER {r}.', idx('MY RELIGIOUS OPINIONS.')) for r in ('I', 'II', 'III', 'IV', 'V')]
    fim_caps = idx('NOTES.', caps[-1])
    cortes = {1: [4], 2: [4], 3: [5, 9], 4: [2]}   # corte antes da n-ésima «* * *» do capítulo (a marca sai)
    nomes = {0: ['01-capitulo-1'], 1: ['02-capitulo-2a', '03-capitulo-2b'], 2: ['04-capitulo-3a', '05-capitulo-3b'],
             3: ['06-capitulo-4a', '07-capitulo-4b', '08-capitulo-4c'], 4: ['09-capitulo-5a', '10-capitulo-5b']}
    romanos = ['I', 'II', 'III', 'IV', 'V']
    for k, a in enumerate(caps):
        b = caps[k + 1] if k + 1 < len(caps) else fim_caps
        titulo_cap = caso_titulo(tx[a + 1]).rstrip('.')
        miolo = list(range(a + 2, b))
        estrelas = [j for j in miolo if ESTRELAS.match(tx[j])]
        pedacos, ini = [], a + 2
        for n in cortes.get(k, []):
            j = estrelas[n - 1]
            pedacos.append((ini, j))
            ini = j + 1
        pedacos.append((ini, b))
        for p, (x, y) in enumerate(pedacos):
            parte = f' (part {p + 1} of {len(pedacos)})' if len(pedacos) > 1 else ''
            gravar(nomes[k][p] + '.txt', f'Apologia pro Vita Sua — Chapter {romanos[k]}: {titulo_cap}{parte}',
                   paragrafos(bl[x:y], cabecalhos=('PROTEST.',)))

    # ---- Notas A–G
    letras = 'ABCDEFG'
    arqs = ['11-nota-a', '12-nota-b', '13-nota-c', '14-nota-d', '15-nota-e', '16-nota-f', '17-nota-g']
    pos = [next(j for j in range(fim_caps, len(tx)) if re.match(rf'NOTE {L}\. ON PAGE \d+\.$', tx[j])) for L in letras]
    sup = idx('SUPPLEMENTAL MATTER.', pos[-1])
    for k, a in enumerate(pos):
        b = pos[k + 1] if k + 1 < len(pos) else sup
        pag = re.search(r'ON PAGE (\d+)', tx[a]).group(1)
        tit = caso_titulo(tx[a + 1]).rstrip('.')
        titulo = f'Apologia pro Vita Sua — Note {letras[k]}, on page {pag}: {tit}'
        if letras[k] == 'D':
            c = idx('CALENDAR OF ENGLISH SAINTS.', a)
            corpo = paragrafos(bl[a + 2:c]) + ['## Calendar of English Saints.'] + calendario(bl[c + 1:b])
            nota = NOTA_PADRAO + ('; no calendário, cada linha da lista vai em «| » só para guardar as quebras '
                                  '(não é verso), e as chaves do impresso, que agrupam santos, viram uma linha «| } rótulo» depois do grupo')
            gravar(arqs[k] + '.txt', titulo, corpo, nota)
        else:
            gravar(arqs[k] + '.txt', titulo, paragrafos(bl[a + 2:b]))

    # ---- Suplementos III e IV (I e II, as listas de cartas e de obras, ficam de fora: ver LEIAME)
    s3, s4, adic = idx('III.', sup), idx('IV.', sup), idx('ADDITIONAL NOTES.', sup)
    t3 = caso_titulo(tx[s3 + 1]).rstrip('.')
    gravar('18-carta-do-bispo.txt', f'Apologia pro Vita Sua — Supplemental Matter, III: {t3}', paragrafos(bl[s3 + 2:s4]))
    t4 = caso_titulo(tx[s4 + 1]).rstrip('.')
    cab4 = tuple(t for t in tx[s4 + 2:adic] if re.match(r'^[IVX]+\.( AND [IVX]+\.)?(--| )[A-ZÜ ,.]+\.$', t))
    gravar('19-cartas-do-clero-e-leigos.txt', f'Apologia pro Vita Sua — Supplemental Matter, IV: {t4}',
           paragrafos(bl[s4 + 2:adic], cabecalhos=cab4))

    # ---- Notas adicionais (1–8)
    cab = tuple(t for t in tx[adic + 1:] if (ehmaiusc([t]) and not t.startswith('"')) or re.fullmatch(r'\d\.', t))
    gravar('20-notas-adicionais.txt', 'Apologia pro Vita Sua — Additional Notes',
           paragrafos(bl[adic + 1:], cabecalhos=cab))


if __name__ == '__main__':
    main(sys.argv[1])
