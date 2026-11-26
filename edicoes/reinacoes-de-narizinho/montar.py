"""Reinações de Narizinho: junta as páginas de 1931 (1931/paginas.json), aplica as correções conferidas no
fac-símile (decisoes.py), passa à grafia de hoje (grafia.py) e grava o texto.

    python3 -I edicoes/reinacoes-de-narizinho/montar.py              texto/1931.txt e texto/hoje.txt (para revisar)
    python3 -I edicoes/reinacoes-de-narizinho/montar.py --publicar   e conteudo/monteiro-lobato/reinacoes-de-narizinho.js

Cada história é uma parte (I–XI) e cada capítulo uma página («## Capítulo N — título» + «{§ P.c}», com
divisao.marcas = false, como em Policarpo Quaresma).
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, AQUI)
import decisoes  # noqa: E402
import grafia  # noqa: E402
import notas  # noqa: E402
from obra import HISTORIAS, META, ROM  # noqa: E402


def conferencia():
    """As linhas de conferencia.tsv: pagina, chave (do comparar.py), de, para, tipo (ws | erro | ok), nota."""
    import csv
    arq = os.path.join(AQUI, 'conferencia.tsv')
    if not os.path.exists(arq):
        return []
    return list(csv.DictReader(open(arq, encoding='utf-8'), delimiter='\t'))


LUGAR = {}          # (página, trecho) -> «História, cap. N», para a lista de erros da «Sobre»


def lugares(P):
    """Para cada página, os capítulos que começam nela (posição no texto, rótulo)."""
    por_cab = {h[0]: h for h in HISTORIAS}
    out, hist, cap = {}, None, None
    for n in sorted(P):
        t = P[n]['texto']
        marcas = [(0, hist, cap)]
        for m in re.finditer(r'(?m)^(###|##) (.+)$', t):
            if m.group(1) == '###':
                hist = por_cab[m.group(2)][1]
            else:
                mm = re.match(r'([IVXL]+) —', m.group(2))
                if mm:
                    cap = decisoes.NUMEROS_CAP.get(('II', mm.group(1)), mm.group(1)) if hist == 'O Sítio do Picapau Amarelo' else mm.group(1)
            marcas.append((m.start(), hist, cap))
        out[n] = marcas
    return out


def lugar(P, mapa, pag, trecho):
    i = P[pag]['texto'].find(trecho)
    h, c = None, None
    for pos, hh, cc in mapa[pag]:
        if pos <= max(i, 0):
            h, c = hh, cc
    return f'{h}, cap. {c}' if h else f'p. {pag}'


def paginas_corrigidas():
    P = {int(k): v for k, v in json.load(open(os.path.join(AQUI, '1931', 'paginas.json'), encoding='utf-8')).items()}
    mapa = lugares(P)
    corr = list(decisoes.CORRECOES)
    for r in conferencia():
        if r['tipo'] in ('ws', 'erro'):
            corr.append((int(r['pagina']), r['de'], r['para'], r['tipo']))
    for i, (pag, de, para, tipo) in enumerate(corr):
        if tipo == 'erro':
            LUGAR[(pag, de)] = lugar(P, mapa, pag, de)
        t = P[pag]['texto']
        if tipo.endswith('*') and t.count(de) >= 1:     # todas as ocorrências da página
            P[pag]['texto'] = t.replace(de, para)
            continue
        if t.count(de) != 1:
            raise SystemExit(f'correção {i} (p. {pag}): {de!r} aparece {t.count(de)} vezes')
        P[pag]['texto'] = t.replace(de, para)
    return P


def juntar(P):
    """As páginas em sequência -> lista de blocos (parágrafos, cabeçalhos, blocos centrados)."""
    blocos = []
    pend = False                      # o último bloco continua na página seguinte
    for n in sorted(P):
        v = P[n]
        bs = v['texto'].split('\n\n')
        if blocos and pend and v['continua'] and bs and not bs[0].startswith(('#', '| ')):
            ult = blocos[-1]
            if ult.endswith('\u0008'):
                blocos[-1] = ult[:-1] + bs[0]
            elif re.search(r'[^\W\d_]-$', ult):
                a = re.search(r'([^\W\d_]+)-$', ult).group(1)
                b = re.match(r'([^\W\d_]+)', bs[0])
                junto = (a + (b.group(1) if b else '')).lower()
                if junto in decisoes.HIFEN_FICA:
                    blocos[-1] = ult + bs[0]
                else:
                    blocos[-1] = ult[:-1] + bs[0]
            else:
                blocos[-1] = ult + ' ' + bs[0]
            bs = bs[1:]
        blocos += bs
        pend = not v['fecha']
    if any('\u0008' in b for b in blocos):
        raise SystemExit('marca de junção sobrando: ' + next(b for b in blocos if '\u0008' in b)[-80:])
    return blocos


def estrutura(blocos):
    """[{'n': 'I', 'titulo': ..., 'caps': [{'n', 'titulo', 'blocos'}]}]"""
    hist, atual, cap = [], None, None
    por_cab = {h[0]: h for h in HISTORIAS}
    for b in blocos:
        if b.startswith('### '):
            h = por_cab[b[4:]]
            atual = {'n': ROM[len(hist)], 'titulo': h[1], 'nomes': h[2], 'caps': []}
            hist.append(atual)
            continue
        m = re.match(r'^## ([IVXL]+) — (.+)$', b)
        if m:
            k = len(atual['caps'])
            num = decisoes.NUMEROS_CAP.get((atual['n'], m.group(1)), m.group(1))
            if num != ROM[k]:
                raise SystemExit(f'{atual["titulo"]}: capítulo {m.group(1)} na posição {k + 1}')
            cap = {'n': num, 'titulo': atual['nomes'][k], 'blocos': [], 'cab1931': m.group(2)}
            atual['caps'].append(cap)
            continue
        if b.startswith('## — '):                     # intertítulo sem número («O CASAMENTO»)
            cap['blocos'].append('## ' + decisoes.INTERTITULOS[b[5:]])
            continue
        cap['blocos'].append(b)
    for h in hist:
        if len(h['caps']) != len(h['nomes']):
            raise SystemExit(f'{h["titulo"]}: {len(h["caps"])} capítulos, {len(h["nomes"])} títulos')
    return hist


def aspas(t):
    """Aspas retas e curvas -> angulares. Cada aspa abre ou fecha pelo contexto (abre depois de espaço,
    travessão ou começo; fecha depois de letra ou pontuação); a ambígua alterna. Parágrafo de citação que
    continua no seguinte abre com « e não fecha, como em 1931 (aspas de continuação)."""
    t = t.replace('“', '"').replace('”', '"').replace('„', '"')
    out, aberto = [], False
    for i, ch in enumerate(t):
        if ch != '"':
            out.append(ch)
            continue
        antes = t[i - 1] if i else ' '
        depois = t[i + 1] if i + 1 < len(t) else ' '
        if antes in ' \n—(_|' and depois not in ' \n':
            abre = True
        elif depois in ' \n,.;:!?)_—' and antes not in ' \n':
            abre = False
        else:
            abre = not aberto
        out.append('«' if abre else '»')
        aberto = abre
    r = ''.join(out)
    if r.count('«') < r.count('»'):
        ASPAS_IMPARES.append(r[:120])
    return r


ASPAS_IMPARES = []


def moderno(b, rel):
    """Um bloco na grafia de hoje; os trechos de FICA_TRECHOS ficam como em 1931."""
    protegidos = {}
    for k, tr in enumerate(decisoes.FICA_TRECHOS):
        if tr in b:
            chave = f'\u0010{k}\u0011'
            protegidos[chave] = tr
            b = b.replace(tr, chave)
    if b.startswith('| '):
        linhas = []
        for l in b.split('\n'):
            corpo = l[2:]
            linhas.append('| ' + grafia.texto(corpo, rel))
        b = '\n'.join(linhas)
    else:
        b = grafia.texto(b, rel)
    for chave, tr in protegidos.items():
        b = b.replace(chave, tr)
    for de, para in decisoes.FINAL:
        b = b.replace(de, para)
    return aspas(b)


def italico_por_linha(b):
    """Num bloco de linhas «| », o itálico que corre várias linhas fecha e reabre em cada uma."""
    if not b.startswith('| ') or '_' not in b:
        return b
    out, aberto = [], False
    for l in b.split('\n'):
        corpo = l[2:]
        if aberto:
            corpo = '_' + corpo
        n = corpo.count('_')
        aberto = n % 2 == 1
        if aberto:
            corpo += '_'
        out.append('| ' + corpo)
    return '\n'.join(out)


def primeira_palavra(b):
    """A capitular de 1931 vem seguida da palavra em versaletes («NUMA casinha»): só a inicial fica maiúscula."""
    return re.sub(r'^(— )?([A-ZÀ-Ú])([A-ZÀ-Ú]+)\b', lambda m: (m.group(1) or '') + m.group(2) + m.group(3).lower(), b)


def montar():
    P = paginas_corrigidas()
    hist = estrutura(juntar(P))
    rel = []
    for h in hist:
        for c in h['caps']:
            bl = [italico_por_linha(b) for b in c['blocos']]
            bl[0] = primeira_palavra(bl[0])
            c['hoje'] = [moderno(b, rel) for b in bl]
            c['velho'] = bl
    return hist, rel


def texto_da_parte(h):
    out = []
    for k, c in enumerate(h['caps'], 1):
        out.append(f'## Capítulo {c["n"]} — {c["titulo"]}')
        corpo = list(c['hoje'])
        if corpo[0].startswith(('| ', '## ')):
            raise SystemExit(f'{h["titulo"]}, cap. {c["n"]}: começa com bloco especial')
        corpo[0] = f'{{§ {h["n"]}.{k}}} ' + corpo[0]
        out += corpo
    return '\n\n'.join(out)


def js_texto(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def publicar(hist):
    edicao = notas.edicao(lambda p, de=None: LUGAR.get((p, de), f'p. {p}'))
    L = ['/* Reinações de Narizinho — Monteiro Lobato',
         '   Gerado por edicoes/reinacoes-de-narizinho/montar.py --publicar a partir de 1931/paginas.json.',
         '   Não edite à mão: corrija as decisões em edicoes/reinacoes-de-narizinho/ e rode de novo.',
         '',
         '   Formato do texto de cada parte (uma história):',
         '     - parágrafos separados por uma linha em branco;',
         '     - _itálico_ entre sublinhados;',
         '     - linhas começadas por "| " formam um bloco de linhas (bilhetes, letreiros, o programa do circo);',
         '     - «## Capítulo N — título» abre cada capítulo, e «{§ P.c}» marca o seu primeiro parágrafo',
         '       (só para o site dividir as páginas; não aparece no texto); «## título» sem número é intertítulo.',
         '*/',
         'BIBLIOTECA.obra({']
    L += [f'  {c}: {json.dumps(v, ensure_ascii=False)},' for c, v in META.items()]
    L.append('  edicao: ' + json.dumps(edicao, ensure_ascii=False, indent=2).replace('\n', '\n  ') + ',')
    L.append('  partes: [')
    for i, h in enumerate(hist):
        L.append(f'    {{ n: {json.dumps(h["n"])}, titulo: {json.dumps(h["titulo"], ensure_ascii=False)}, '
                 f'texto: `{js_texto(texto_da_parte(h))}` }}' + (',' if i + 1 < len(hist) else ''))
    L += ['  ]', '});']
    saida = os.path.join(RAIZ, 'conteudo', META['autor'], META['id'] + '.js')
    os.makedirs(os.path.dirname(saida), exist_ok=True)
    open(saida, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
    from edicao.montar import registrar_no_index
    if registrar_no_index(os.path.join(RAIZ, 'index.html'), f'conteudo/{META["autor"]}/{META["id"]}.js'):
        print('acrescentado ao index.html')
    print('gravado', os.path.relpath(saida, RAIZ))


def main():
    hist, rel = montar()
    pasta = os.path.join(os.path.expanduser('~/.cache/claude-pedidos-2611/reinacoes-de-narizinho'), 'texto')
    os.makedirs(pasta, exist_ok=True)
    for nome, chave in (('1931.txt', 'velho'), ('hoje.txt', 'hoje')):
        with open(os.path.join(pasta, nome), 'w', encoding='utf-8') as f:
            for h in hist:
                f.write(f'\n\n######## {h["n"]}. {h["titulo"]}\n')
                for c in h['caps']:
                    f.write(f'\n#### {c["n"]} — {c["titulo"]}\n\n')
                    f.write('\n\n'.join(c[chave]) + '\n')
    from collections import Counter
    cont = Counter((a, b, f) for a, b, f in rel)
    with open(os.path.join(pasta, 'grafia.tsv'), 'w', encoding='utf-8') as f:
        for (a, b, fo), c in sorted(cont.items(), key=lambda x: (x[0][2], x[0][0].lower())):
            f.write(f'{fo}\t{a}\t{b}\t{c}\n')
    pal = sum(len(re.findall(r'[^\W\d_]+', ' '.join(c['hoje']))) for h in hist for c in h['caps'])
    print(len(hist), 'histórias,', sum(len(h['caps']) for h in hist), 'capítulos,', pal, 'palavras')
    print('SEM_PAR:', len({a for a, b, f in rel if f == 'SEM_PAR'}), '; aspas ímpares:', len(ASPAS_IMPARES))
    for a in ASPAS_IMPARES[:30]:
        print('   ', a)
    if '--publicar' in sys.argv:
        publicar(hist)


if __name__ == '__main__':
    main()
