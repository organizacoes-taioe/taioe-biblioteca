"""Poesias Completas (Machado de Assis, 1901): monta conteudo/machado-de-assis/poesias-completas.js.

    python3 edicoes/poesias-completas-machado/montar.py        (na raiz do repositório)

Fonte: texto/<id>.txt (a grafia de hoje, de modernizar.py), na ordem de poemas.json; as notas do autor
(texto/notas.txt) vão para o fim do poema a que se referem, como na Iracema («¤ »), sem o número da página.
Erros de 1901 corrigidos: conferencia.json («ws!» e «!texto») e ajustes.ERROS_EXTRA, na grafia de hoje.
"""
import json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))

MESES = r'(Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)'


def sem_sublinhado(s):
    return s.replace('_', '')


def epigrafe(v):
    m = re.match(r'(.*?)\s*\(([^()]*(?:\([^()]*\)[^()]*)*)\)\s*$', v)
    texto, autor = (m.group(1), m.group(2)) if m else (v, '')
    partes = [x.strip() for x in texto.split(' / ') if x.strip()]
    if len(partes) == 1 and len(partes[0]) > 140:   # epígrafe em prosa
        out = '_' + sem_sublinhado(partes[0]) + '_'
        return out + ('\n\n— ' + autor if autor else '')
    ls = ['| _' + sem_sublinhado(x) + '_' for x in partes]
    if autor:
        ls.append('| — ' + autor)
    return '\n'.join(ls)


def nome(s):
    return ' '.join(w[:1] + w[1:].lower() for w in s.split())


def poema(t):
    """Texto do site a partir de texto/<id>.txt. Devolve (cabeçalho, texto)."""
    cab, blocos, est, prosa = {}, [], [], []

    def fecha():
        if est:
            blocos.append('\n'.join('| ' + x for x in est)); est.clear()
    corpo_visto = False
    for l in t.split('\n'):
        m = re.match(r'^# (\w+):? ?(.*)$', l)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if k in ('titulo', 'nota'):
                cab.setdefault(k, v); continue
            fecha()
            if k == 'epigrafe': blocos.append(epigrafe(v))
            elif k in ('subtitulo', 'dedicatoria'): blocos.append('_' + v + '_')
            elif k == 'parte': blocos.append('**' + v + '**')
            elif k == 'fala': blocos.append('@ ' + nome(v))
            elif k == 'cena': blocos.append('## ' + v)
            elif k == 'rubrica': blocos.append('_' + v.replace('_', '') + '_')
            elif k == 'lugar': blocos.append('_' + v + '_')
            elif k == 'personagens': blocos.append('**Personagens**\n\n' + '\n'.join('| ' + x.strip() for x in v.split(' / ')))
            elif k == 'lacuna': blocos.append('| . . . . . . . . . . . . . . .')
            elif k == 'data': blocos.append('_' + re.sub(MESES, lambda x: x.group(1).lower(), v) + '_')
            elif k == 'assinatura': blocos.append(v)
            else: raise SystemExit('marca desconhecida: ' + k)
            continue
        if not l.strip():
            fecha(); continue
        est.append(l.strip())
    fecha()
    return cab, '\n\n'.join(blocos)


def prosa(t):
    cab, ps = {}, []
    for l in t.split('\n'):
        m = re.match(r'^# (\w+):? ?(.*)$', l)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if k == 'data': ps.append('_' + re.sub(MESES, lambda x: x.group(1).lower(), v) + '_')
            elif k == 'assinatura': ps.append(v)
            else: cab.setdefault(k, v)
            continue
        if l.strip():
            ps.append(l.strip())
    return cab, '\n\n'.join(ps)


def notas():
    """{id: [blocos «¤ »]} de texto/notas.txt."""
    por, atual, nota = {}, None, None
    def fecha():
        if nota:
            por.setdefault(atual, []).extend(nota)
    for l in open(os.path.join(AQUI, 'texto', 'notas.txt'), encoding='utf-8').read().split('\n'):
        if l.startswith('#') or not l.strip():
            continue
        if l.startswith('@ '):
            fecha(); atual = l[2:].strip(); nota = None; continue
        if l.startswith('= '):
            continue
        if l.startswith('> '):
            fecha()
            lema = ' / '.join(x.strip() for x in l[2:].split(' / '))
            nota = ['¤ _' + lema.rstrip('.') + '._ —']
            continue
        if l.startswith('|'):
            v = l[1:].strip()
            if nota and nota[-1].startswith('¤ |'):
                nota[-1] += '\n|' + (' ' + v if v else '')
            else:
                nota.append('¤ |' + (' ' + v if v else ''))
            continue
        if nota and nota[-1].endswith('—'):
            nota[-1] += ' ' + l.strip()
        else:
            nota.append('¤ ' + l.strip())
    fecha()
    # estrofes dos versos citados: a linha «|» vazia separa blocos
    for k, v in por.items():
        novo = []
        for b in v:
            if b.startswith('¤ |') and '\n|\n' in b + '\n':
                for x in re.split(r'\n\|(?:\n|$)', b):
                    if x.strip():
                        novo.append(x if x.startswith('¤ ') else '¤ ' + x)
            else:
                novo.append(b)
        por[k] = novo
    return por


def erros():
    """Lista dos erros de 1901 corrigidos, na grafia de hoje: [{cap, de, para}]."""
    import ajustes, modernizar as M
    P = {p['id']: p for p in json.load(open(os.path.join(AQUI, 'poemas.json'), encoding='utf-8'))}
    rel = json.load(open(os.path.join(AQUI, 'relatorio-1901.json'), encoding='utf-8'))
    out = []
    for pid, r in rel.items():
        for chave, de, para, ctx in r['erros']:
            out.append((pid, de, para, ctx))
    for pid, de, para in ajustes.ERROS_EXTRA:
        out.append((pid, de, para, ''))
    lista = []
    for pid, de, para, ctx in out:
        if ctx and para.strip() and para.strip() in ctx:
            k = ctx.rfind(para.strip()) if not re.match(r'\w', para.strip()) else ctx.find(para.strip())
            linha_de = (ctx[:k] + de.strip() + ctx[k + len(para.strip()):]).replace('  ', ' ').strip()
            linha_para = M.modernizar_linha(ctx, []).strip()
            de, para = linha_de, linha_para
        else:
            para = M.modernizar_linha(para, []).strip()
        lista.append({'cap': P[pid]['titulo'], 'de': de.strip(), 'para': para, 'ctx': ctx})
    return lista


if __name__ == '__main__':
    P = json.load(open(os.path.join(AQUI, 'poemas.json'), encoding='utf-8'))
    N = notas()
    partes = []
    for p in P:
        if p['id'] == 'notas':
            continue
        t = open(os.path.join(AQUI, 'texto', p['id'] + '.txt'), encoding='utf-8').read()
        if p['id'] == 'advertencia':
            cab, texto = prosa(t)
        else:
            cab, texto = poema(t)
        if p['id'] in N:
            texto += '\n\n' + '\n\n'.join(N.pop(p['id']))
        partes.append({'n': p['livro'], 'titulo': p['titulo'], 'texto': texto})
    if N:
        raise SystemExit('notas sem poema: %s' % list(N))
    pal = sum(len(re.findall(r"[A-Za-zÀ-ÿ]+", x['texto'])) for x in partes)
    versos = sum(len(re.findall(r'(?m)^\| ', x['texto'])) for x in partes)
    edicao = json.load(open(os.path.join(AQUI, 'edicao.json'), encoding='utf-8'))
    # a lista vem de erros() (python3 -c 'import montar; montar.erros()'), passada a limpo à mão em erros.json
    edicao['erros'] = json.load(open(os.path.join(AQUI, 'erros.json'), encoding='utf-8'))
    obra = {'id': 'poesias-completas', 'autor': 'machado-de-assis', 'titulo': 'Poesias Completas', 'ano': 1901,
            'genero': 'Poesia', 'divisao': {'singular': 'poema', 'plural': 'poemas', 'rotulo': 'titulo', 'agrupar': True},
            'descricao': 'O volume que Machado de Assis organizou e reviu em 1901: _Crisálidas_, _Falenas_ e _Americanas_, na forma revista, e o livro novo, _Ocidentais_, com as notas do autor.',
            '_palavras': pal, 'partes': partes, 'edicao': edicao}
    js = ('/* Poesias Completas — Machado de Assis (1901). Gerado por edicoes/poesias-completas-machado/montar.py;\n'
          '   não edite à mão: corrija edicoes/poesias-completas-machado/1901/ (ou as decisões) e rode o fluxo de novo. */\n'
          'BIBLIOTECA.obra(' + json.dumps(obra, ensure_ascii=False, indent=1) + ');\n')
    open(os.path.join(RAIZ, 'conteudo', 'machado-de-assis', 'poesias-completas.js'), 'w', encoding='utf-8').write(js)
    print(len(partes), 'partes,', versos, 'linhas de verso,', pal, 'palavras,', len(edicao['erros']), 'erros de 1901')
