"""Notas do autor: da transcrição diplomática de 1769 (notas1769.txt) à grafia de hoje (notas.txt).

  python3 edicoes/o-uraguai/notas.py      grava notas.txt e lista as palavras sem par no léxico (sem_par)

notas1769.txt: «=== pág N» (página do DjVu, Boston), «## » nota nova, «+ » continuação da página anterior,
«| » verso citado, «> » referência da citação; itálico entre _sublinhados_. Transcrita das imagens dos dois
exemplares, com o OCR votado (notas_ocr.py) e o Wikisource de ajuda.

A grafia: grafia1990.atual (São Bernardo: léxico + esqueleto) depois das regras de 1769 (he → é, hum → um,
pretérito em -ão → -am); MANUAL traz o que o léxico não resolve. Latim, francês e as referências bibliográficas
ficam como estão (ESTRANGEIRO). Gentílicos e meses em minúscula (Acordo de 1990).
"""
import os, re, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, os.path.join(RAIZ, 'edicoes', 'sao-bernardo'))
import grafia1990 as G  # noqa: E402

CANTOS = {1: range(7, 26), 2: range(27, 52), 3: range(53, 75), 4: range(75, 94), 5: range(95, 109)}
PALAVRA = re.compile(r"[^\W\d_]+(?:-[^\W\d_]+)*")

# trechos (em itálico ou não) que não se tocam: latim, francês, títulos e referências
ESTRANGEIRO = [
    'Corneil. Horac.', 'misit illos binos', 'Post bellum auxilium', 'Praed. rust. Lib.', 'Species plantarum',
    'Dominico S. R. E. Card. Passion. S. J. superstes.', 'V. P. Gabr. Malagr. in Portugall, pro fide occisus.',
    'Xamti', 'Tien', 'Vanier', 'Rheed', 'Linn', 'Hort. Malab', 'Le Philosophe de Sans-souci', 'Epitre a Darget',
]

# 1769 → hoje, palavra a palavra (o que o léxico não resolve, e as formas antigas que mudam só a grafia)
MANUAL = json.load(open(os.path.join(AQUI, 'notas_manual.json'), encoding='utf-8')) \
    if os.path.exists(os.path.join(AQUI, 'notas_manual.json')) else {}

MINUSCULAS = {'Indios', 'Indio', 'Indias', 'Jesuitas', 'Jesuita', 'Portuguezes', 'Portuguez', 'Hespanhoes', 'Hespanhol',
              'Castelhanos', 'Castelhano', 'Chinezes', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
              'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro', 'Tartaros', 'Americano', 'Europeos'}

sem_par = {}


def preterito(w):
    """-ão de 1769 → -am de hoje quando é o pretérito ou o presente (tinhão, declamárão, levão);
    o futuro (serão, farão) e os nomes (mão, razão) ficam."""
    lw = w.lower()
    m = re.match(r'^(.*?)([áéíô])(rão)$', lw)
    if m:                                         # declamárão, pertendêrão: pretérito marcado
        return w[:len(m.group(1))] + {'á': 'a', 'é': 'e', 'ê': 'e', 'í': 'i', 'ô': 'o'}[m.group(2)] + 'ram'
    if lw.endswith('ão'):
        base = lw[:-2]
        lex = G.lexico()
        if lw not in lex and (base + 'am') in lex:
            return w[:-2] + 'am'
        if lw.endswith('ião') and (base + 'am') in lex:   # vivião, pertendião
            return w[:-2] + 'am'
    return w


def palavra(w):
    if w in MANUAL:
        return MANUAL[w]
    if re.fullmatch(r'[IVXLC]+', w) and len(w) > 1 or w in ('V', 'X'):
        return w                                   # algarismo romano (Henrique III, Clemente XI)
    lw = w.lower()
    if lw in ('he',):
        out = 'é'
    elif lw in ('hum', 'huma', 'huns', 'humas'):
        out = lw[1:]
    else:
        partes = w.split('-')
        partes = [preterito(p) if p else p for p in partes]
        w2 = '-'.join(partes)
        out, fonte = G.atual(w2)
        if fonte == 'SEM_PAR':
            sem_par[w] = sem_par.get(w, 0) + 1
    if w[:1].isupper() and w not in MINUSCULAS:
        out = out[:1].upper() + out[1:]
    elif w in MINUSCULAS:
        out = out[:1].lower() + out[1:]
    return out


def trecho(s):
    """moderniza um trecho, respeitando os estrangeiros."""
    for e in ESTRANGEIRO:
        if e in s:
            i = s.index(e)
            return trecho(s[:i]) + e + trecho(s[i + len(e):])
    return PALAVRA.sub(lambda m: palavra(m.group()), s)


# locuções e trechos (depois da grafia de cada palavra)
FRASES = [
    (r'\bá\b', 'à'), (r'\bás\b', 'às'), (r'\bÁ\b', 'À'),
    (r'\bjá mais\b', 'jamais'), (r'\b([Cc])om tudo(?! isto)\b', r'\1ontudo'),
    (r'\bem fim\b', 'enfim'), (r'\bEm quanto\b', 'Enquanto'), (r'\bA pesar de\b', 'Apesar de'), (r'\ba pesar de\b', 'apesar de'),
    (r'\bTão de pressa\b', 'Tão depressa'), (r'\bRio de janeiro\b', 'Rio de Janeiro'), (r'\bSargento maior\b', 'Sargento-mor'),
    (r'\bEngenheiro maior\b', 'Engenheiro-mor'), (r'\bTenente Coronel\b', 'Tenente-Coronel'), (r'\bTatu Guaçu\b', 'Tatu-Guaçu'),
    (r'\bjesuítas tem tido\b', 'jesuítas têm tido'), (r'\bárvores são altíssimas, e tem\b', 'árvores são altíssimas, e têm'),
    (r'\bque eles tem na\b', 'que eles têm na'), (r'\bportos tem entre\b', 'portos têm entre'),
    (r'\bao todo O Autor\b', 'ao todo. O Autor'),
]


def linha(l):
    if l.startswith('| ') or l.startswith('> '):
        return l                                   # verso citado (latim, francês) e referência: como no impresso
    # itálicos estrangeiros inteiros ficam
    def ital(m):
        t = m.group(1)
        palavras = PALAVRA.findall(t)
        lex = G.lexico()
        conhecidas = sum(1 for p in palavras if p.lower() in lex or palavra(p).lower() in lex)
        if palavras and conhecidas / len(palavras) < 0.5 and len(palavras) > 2:
            return '_' + t + '_'
        return '_' + trecho(t) + '_'
    partes = re.split(r'(_[^_]*_)', l)
    return frases(''.join(ital(re.match(r'_(.*)_', p, re.S)) if p.startswith('_') and p.endswith('_') and len(p) > 1 else trecho(p)
                   for p in partes))


def frases(s):
    for a, b in FRASES:
        s = re.sub(a, b, s)
    return s


def ler():
    """[(canto, pagina, tipo, texto)] tipo: nota, cont, verso, ref"""
    out = []; pag = None
    for l in open(os.path.join(AQUI, 'notas1769.txt'), encoding='utf-8'):
        l = l.rstrip('\n')
        if not l.strip():
            continue
        m = re.match(r'=== pág (\d+)', l)
        if m:
            pag = int(m.group(1)); continue
        canto = next(c for c, r in CANTOS.items() if pag in r)
        if l.startswith('## '): out.append([canto, pag, 'nota', l[3:]])
        elif l.startswith('+ '): out.append([canto, pag, 'cont', l[2:]])
        elif l.startswith('| '): out.append([canto, pag, 'verso', l])
        elif l.startswith('> '): out.append([canto, pag, 'ref', l])
        else: raise SystemExit('linha sem marca: ' + l)
    return out


def montar():
    """Notas por canto, na grafia de hoje: {canto: [ [linhas da nota] ]}."""
    notas = {c: [] for c in CANTOS}
    for canto, pag, tipo, t in ler():
        if tipo == 'nota':
            notas[canto].append([linha(t)])
        elif tipo == 'cont':
            ult = notas[canto][-1]
            if ult[-1].startswith(('| ', '> ')): ult.append(linha(t))
            else: ult[-1] = ult[-1] + ' ' + linha(t)
        else:
            notas[canto][-1].append(linha(t))
    return notas


if __name__ == '__main__':
    notas = montar()
    with open(os.path.join(AQUI, 'notas.txt'), 'w', encoding='utf-8', newline='\n') as f:
        for c in notas:
            f.write('# Canto %d\n' % c)
            for n in notas[c]:
                f.write('\n'.join(n) + '\n\n')
    print(sum(len(v) for v in notas.values()), 'notas;', {c: len(v) for c, v in notas.items()})
    print('sem par:', ' '.join('%s(%d)' % kv for kv in sorted(sem_par.items())))
