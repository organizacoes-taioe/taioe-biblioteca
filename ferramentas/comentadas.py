"""Obras comentadas da Não-ficção (a primeira: a Apologia de Sócrates), no esquema da Bíblia Taioé:
tradução nossa com o original ao lado, a paginação de referência à margem, notas e comentários
por tema. Monta o conteúdo do site e as páginas de revisão do Gere.

Também serve a obra em português antigo que não é tradução (a Carta de Caminha, desde 27/10/2026):
o texto na grafia de hoje fica em atualizado/ (no lugar de traducao/), sem comentários, com a marca
da folha do manuscrito ({fl. 1v}) e, no obra.json, `rotulos` ({orig, trad}: os nomes dos botões dos
dois textos) no lugar de `original` (o título na língua da tradução).

    python3 ferramentas/comentadas.py                 # confere e grava conteudo/
    python3 ferramentas/comentadas.py --revisao DIR   # também DIR/nao-ficcao.json e
                                                      # DIR/nao-ficcao-comentarios.json (o infra)

Fonte de cada obra, em edicoes/<obra>/:
  obra.json          título, partes (n, titulo, st, trechos [{id, titulo, par}]), notas
                     [{id, parte, st, apos, texto, revista?}], apresentação, fontes e o que vai à
                     revisão (só `revisao.escolhas`: uma pergunta pontual cada; a divisão e o
                     registro ficam no CONVENCOES.md da obra, sem passar pelo Gere, pedido de 24/10)
  original/parte-N.txt, traducao/parte-N.txt (ou atualizado/parte-N.txt)
                     um parágrafo por bloco, os mesmos nos dois; a marca {St 17a} (ou {fl. 1v})
                     no mesmo parágrafo nos dois lados
  comentarios.json   [{parte, trecho?, id, titulo, st, resumo, revisto?, itens: [{id, autor, sobre,
                     obra, passagem, link, original, texto, revisto?}]}], na ordem do texto

Montagem dos comentários (uma vez, e de novo só se a escolha mudar):
    python3 ferramentas/comentadas.py --montar <obra>
  junta edicoes/<obra>/temas.json ([{parte, trecho?, id, titulo, st, resumo, itens: [ids]}]) com os
  achados da pesquisa (edicoes/<obra>/pesquisa/achados-*.json) e grava comentarios.json, que daí em
  diante é a fonte (as respostas do Gere se aplicam nele).

Grava conteudo/nao-ficcao.js (o registro das obras) e conteudo/<autor>/<obra>.js (os textos,
as notas e os comentários). Depois: node ferramentas/site/gerar.mjs.
"""
import json
import pathlib
import re
import sys
from datetime import date

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OBRAS = ['apologia-de-socrates', 'carta']
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-"
                       r"(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")
MARCA = re.compile(r'\{(St [0-9]+[a-e]|fl\. [0-9]+[rv])\}')
ID = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
erros = []


def ler_blocos(arq):
    return [b.strip() for b in arq.read_text(encoding='utf-8').strip().split('\n\n') if b.strip()]


def carregar(slug):
    d = RAIZ / 'edicoes' / slug
    o = json.loads((d / 'obra.json').read_text(encoding='utf-8'))
    com = json.loads((d / 'comentarios.json').read_text(encoding='utf-8')) if (d / 'comentarios.json').exists() else []
    o['_t'], o['_o'] = [], []
    texto = 'atualizado' if (d / 'atualizado').is_dir() else 'traducao'
    for i, p in enumerate(o['partes'], 1):
        t, g = ler_blocos(d / texto / f'parte-{i}.txt'), ler_blocos(d / 'original' / f'parte-{i}.txt')
        onde = f'{slug}, parte {i}'
        if len(t) != len(g):
            erros.append(f'{onde}: {len(t)} parágrafos na tradução e {len(g)} no original')
        for k, (a, b) in enumerate(zip(t, g), 1):
            if MARCA.findall(a) != MARCA.findall(b):
                erros.append(f'{onde}, parágrafo {k}: marcas diferentes {MARCA.findall(a)} × {MARCA.findall(b)}')
        # a mesóclise é proibida no que nós escrevemos; a do autor (Caminha) fica
        for m in MESOCLISE.finditer('' if 'rotulos' in o else '\n'.join(t)):
            erros.append(f'{onde}: mesóclise «{m.group(0).strip()}»')
        for tr in p.get('trechos', []):
            if not ID.match(tr['id']) or not 1 <= tr['par'] <= len(t):
                erros.append(f'{onde}: trecho {tr["id"]} com parágrafo {tr["par"]} fora da parte')
        o['_t'].append(t)
        o['_o'].append(g)
    ids = set()
    for n in o['notas']:
        if n['id'] in ids or not ID.match(n['id']):
            erros.append(f'{slug}: nota com id repetido ou inválido: {n["id"]}')
        ids.add(n['id'])
        texto = '\n\n'.join(o['_t'][n['parte'] - 1])
        vezes = texto.count(n['apos'])
        if (vezes != 1 and 'ocorrencia' not in n) or not 1 <= n.get('ocorrencia', 1) <= vezes:
            erros.append(f'{slug}: nota {n["id"]}: «{n["apos"]}» aparece {vezes} vezes na parte {n["parte"]} (use «ocorrencia»)')
        for m in MESOCLISE.finditer(n['texto']):
            erros.append(f'{slug}: nota {n["id"]}: mesóclise «{m.group(0).strip()}»')
    vistos = set()
    for x in com:
        if not ID.match(x['id']) or (x['parte'], x['id']) in vistos:
            erros.append(f'{slug}: tema com id repetido ou inválido: parte {x["parte"]}, {x["id"]}')
        vistos.add((x['parte'], x['id']))
        trechos = [tr['id'] for tr in o['partes'][x['parte'] - 1].get('trechos', [])]
        if (x.get('trecho') not in trechos) if trechos else x.get('trecho'):
            erros.append(f'{slug}: tema {x["id"]}: trecho «{x.get("trecho")}» não é da parte {x["parte"]}')
        if not x['itens']:
            erros.append(f'{slug}: tema {x["id"]} sem comentários')
        for it in x['itens']:
            for campo in ('id', 'autor', 'sobre', 'obra', 'passagem', 'link', 'texto'):
                if not it.get(campo):
                    erros.append(f'{slug}: tema {x["id"]}, comentário {it.get("id")}: falta «{campo}»')
            if it.get('link', '').startswith('http:') and not it['link'].startswith('http://www.zeno.org/'):  # o zeno.org não tem https
                erros.append(f'{slug}: comentário {it["id"]}: link sem https')
            for m in MESOCLISE.finditer(it.get('texto', '')):
                erros.append(f'{slug}: comentário {it["id"]}: mesóclise «{m.group(0).strip()}»')
            if re.search(r'\[[^\]]*(conferir|pesquisador|texto da edição)[^\]]*\]', it.get('texto', ''), re.I):
                erros.append(f'{slug}: comentário {it["id"]}: nota do pesquisador entre colchetes')
    o['_com'] = com
    return o


def js(v):
    return json.dumps(v, ensure_ascii=False)


def aprovados(o, i):
    """Os temas da parte i que vão ao site (o Gere, 26/10: «os comentários só vão aparecer depois
    que forem aceitos por mim»): só o comentário aprovado (`revisto`, sem aviso de corte), só o tema
    com o título aprovado e algum comentário aprovado, e o resumo só aprovado."""
    temas = []
    for x in o['_com']:
        rev = x.get('revisto', [])
        itens = [it for it in x['itens'] if it.get('revisto') and not it.get('aviso_corte')]
        if x['parte'] != i or 'titulo' not in rev or not itens:
            continue
        temas.append({'id': x['id'], 'titulo': x['titulo'], 'st': x.get('st', ''),
                      'resumo': x.get('resumo', '') if 'resumo' in rev else '', 'trecho': x.get('trecho', ''),
                      'itens': [{k: it[k] for k in ('autor', 'sobre', 'obra', 'passagem', 'link', 'texto')} for it in itens]})
    return temas


def gravar_conteudo(obras):
    reg = ['/* Gerado por ferramentas/comentadas.py a partir de edicoes/<obra>/obra.json. Não editar à mão. */']
    for o in obras:
        dest = RAIZ / 'conteudo' / o['autor'] / f'{o["id"]}.js'
        # Só o aprovado vai ao site (pedido do Gere, 26/10): a obra, só sem escolha de tradução
        # esperando a resposta dele; a nota, só `revista` ou na obra revisada; os comentários, aprovados().
        if (o.get('revisao') or {}).get('escolhas'):
            dest.unlink(missing_ok=True)
            continue
        partes = [{'n': p['n'], 'titulo': p['titulo'], 'folhas': p['st']} for p in o['partes']]
        # tradução (a Apologia): a língua e o título do original; obra em português antigo (Caminha):
        # só os nomes dos botões dos dois textos
        lado = {'rotulos': o['rotulos']} if 'rotulos' in o else {'traducao': {'lingua': 'grego', 'codigo': 'grc', 'titulo': o['original']}}
        reg.append('BIBLIOTECA.obra(' + js({
            'id': o['id'], 'autor': o['autor'], 'titulo': o['titulo'], 'genero': o['genero'], 'datas': o['datas'],
            'divisao': {'singular': 'parte', 'plural': 'partes'}, 'comentada': True,
            **lado,
            'descricao': o['descricao'], 'edicao': {'titulo': 'Sobre esta edição', 'apresentacao': o['apresentacao'], 'fontes': o['fontes']},
            'arquivo': f'conteudo/{o["autor"]}/{o["id"]}.js', 'partes': partes}) + ');')
        extra = []
        for i, p in enumerate(o['partes'], 1):
            extra.append({
                'trechos': p.get('trechos', []),
                'notas': [{k: n[k] for k in ('id', 'st', 'apos', 'texto', 'ocorrencia') if k in n} for n in o['notas']
                          if n['parte'] == i and (o['estado'] == 'revisado' or n.get('revista'))],
                'temas': aprovados(o, i)})
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text('/* Gerado por ferramentas/comentadas.py a partir de edicoes/' + o['id'] + '/. Não editar à mão. */\n'
                        'BIBLIOTECA.textos(' + js({o['id']: {'t': ['\n\n'.join(t) for t in o['_t']], 'o': ['\n\n'.join(g) for g in o['_o']]}}) + ');\n'
                        'if (BIBLIOTECA.comentadas) BIBLIOTECA.comentadas(' + js({o['id']: extra}) + ');\n',
                        encoding='utf-8', newline='\n')
    (RAIZ / 'conteudo' / 'nao-ficcao.js').write_text('\n'.join(reg) + '\n', encoding='utf-8', newline='\n')
    indice = RAIZ / 'index.html'
    h = indice.read_text(encoding='utf-8')
    linha = '<script defer src="conteudo/nao-ficcao.js"></script>'
    if linha not in h:
        ultimo = [m for m in re.finditer(r'<script defer src="conteudo/[^"]+"></script>\n', h)][-1]
        h = h[:ultimo.end()] + linha + '\n' + h[ultimo.end():]
        indice.write_text(h, encoding='utf-8', newline='\n')


def frase(texto, trecho):
    """A frase do texto em que está o trecho (para a nota na página de revisão)."""
    limpo = MARCA.sub('', texto).replace('  ', ' ')
    k = limpo.find(trecho)
    ini = max(limpo.rfind(c, 0, k) for c in '.?!:;')
    fim = min([x for x in (limpo.find(c, k + len(trecho)) for c in '.?!;') if x >= 0] or [len(limpo) - 1])
    return limpo[ini + 1:fim + 1].strip().lstrip('»” ')


def revisao(obras, destino):
    hoje = date.today().strftime('%d/%m/%Y')
    pag, pagc = {'slug': 'nao-ficcao', 'titulo': 'Não-ficção: revisão', 'capitulos': []}, \
        {'slug': 'nao-ficcao-comentarios', 'titulo': 'Não-ficção: comentários', 'capitulos': []}
    for o in obras:
        url = f'/biblioteca/{o["autor"]}/{o["id"]}/'
        r = o.get('revisao') or {}
        secoes = []
        esc = [dict(e, id=f'{o["id"]}:escolha:{e["id"]}', tipo='escolha') for e in r.get('escolhas', [])]
        if esc:
            secoes.append({'id': 'escolhas', 'titulo': 'Escolhas de tradução', 'itens': esc})
        letras, notas = {}, []
        for n in o['notas']:
            letras[n['parte']] = letras.get(n['parte'], 0) + 1
            if n.get('revista'):
                continue
            texto = '\n\n'.join(o['_t'][n['parte'] - 1])
            notas.append({'id': f'{o["id"]}:nota:{n["id"]}', 'tipo': 'nota', 'ref': f'Parte {n["parte"]}, {n["st"]}',
                          'letra': chr(96 + letras[n['parte']]), 'versiculo': frase(texto, n['apos']), 'texto': n['texto']})
        if notas:
            secoes.append({'id': 'notas', 'titulo': 'Notas', 'itens': notas})
        # Divisão e registro não vão mais à página (o Gere, 24/10: «me mostre apenas questões
        # pontuais, para eu decidir uma única coisa em cada pendência»).
        if r.get('divisao') or r.get('registro'):
            erros.append(f'{o["id"]}: revisao.divisao e revisao.registro não vão mais ao Gere (CONVENCOES.md da obra)')
        if secoes:
            pag['capitulos'].append({'id': o['id'], 'rotulo': o['titulo'], 'url': url,
                                     'estado': f'{o["estado"]}, atualizado em {hoje}', 'secoes': secoes})
        for i, p in enumerate(o['partes'], 1):
            sec = []
            trechos = {tr['id']: tr['titulo'] for tr in p.get('trechos', [])}
            for x in [x for x in o['_com'] if x['parte'] == i]:
                rev, base, itens = x.get('revisto', []), f'{o["id"]}-{i}', []
                if 'titulo' not in rev:
                    itens.append({'id': f'{base}:tt:{x["id"]}', 'tipo': 'tema-titulo', 'texto': x['titulo']})
                if x.get('resumo') and 'resumo' not in rev:
                    itens.append({'id': f'{base}:tr:{x["id"]}', 'tipo': 'tema-resumo', 'texto': x['resumo']})
                for it in x['itens']:
                    if not it.get('revisto'):
                        itens.append({'id': f'{base}:c:{x["id"]}:{it["id"]}'[:120], 'tipo': 'comentario',
                                      **{k: it[k] for k in ('autor', 'sobre', 'obra', 'passagem', 'link', 'texto')}})
                if itens:
                    sec.append({'id': x['id'], 'titulo': x['titulo'],
                                'sub': ' · '.join(s for s in (trechos.get(x.get('trecho', ''), ''), x.get('st', '')) if s),
                                'url': f'{url}{p["n"]}/comentarios/{x["id"]}/', 'itens': itens})
            if sec:
                pagc['capitulos'].append({'id': f'{o["id"]}-{i}', 'rotulo': f'{o["titulo"]}, parte {i}: {p["titulo"]}',
                                          'url': f'{url}{p["n"]}/', 'secoes': sec})
    for d in (pag, pagc):
        for c in d['capitulos']:
            for s in c['secoes']:
                for it in s['itens']:
                    if not re.match(r'^[a-z0-9][a-z0-9:._-]{0,119}$', it['id']):
                        erros.append(f'revisão: id inválido para o banco: {it["id"]}')
        (destino / f'{d["slug"]}.json').write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
        print(f'{destino / (d["slug"] + ".json")}: {sum(len(s["itens"]) for c in d["capitulos"] for s in c["secoes"])} itens')


def montar(slug):
    d = RAIZ / 'edicoes' / slug
    achados = {}
    for arq in sorted((d / 'pesquisa').glob('achados-*.json')):
        for x in json.loads(arq.read_text(encoding='utf-8')):
            achados[x['id']] = x
    com, usados = [], set()
    for t in json.loads((d / 'temas.json').read_text(encoding='utf-8')):
        itens = []
        for i in t['itens']:
            if i not in achados:
                erros.append(f'{slug}: tema {t["id"]}: achado {i} não existe')
                continue
            if i in usados:
                erros.append(f'{slug}: achado {i} em dois temas')
            usados.add(i)
            x = achados[i]
            texto = re.sub(r'\s*\[[^\]]*\]\s*$', '', x['traducao_pt'].strip())
            itens.append({'id': i, 'autor': x['autor'], 'sobre': x['sobre'], 'obra': x['obra'], 'passagem': x['passagem'],
                          'link': x['link'], 'texto': texto, 'original': x['original']})
        com.append({k: t[k] for k in ('parte', 'trecho', 'id', 'titulo', 'st', 'resumo') if k in t} | {'itens': itens})
    if erros:
        sys.exit('\n'.join(erros))
    (d / 'comentarios.json').write_text(json.dumps(com, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
    print(f'{slug}: {sum(len(t["itens"]) for t in com)} comentários em {len(com)} temas; {len(achados) - len(usados)} achados de fora')


def main():
    if '--montar' in sys.argv:
        montar(sys.argv[sys.argv.index('--montar') + 1])
        return
    obras = [carregar(s) for s in OBRAS]
    if erros:
        sys.exit('\n'.join(erros))
    gravar_conteudo(obras)
    if '--revisao' in sys.argv:
        revisao(obras, pathlib.Path(sys.argv[sys.argv.index('--revisao') + 1]))
    if erros:
        sys.exit('\n'.join(erros))
    for o in obras:
        print(f'{o["id"]}: {len(o["partes"])} partes, {len(o["notas"])} notas, '
              f'{sum(len(x["itens"]) for x in o["_com"])} comentários em {len(o["_com"])} temas')


if __name__ == '__main__':
    main()
