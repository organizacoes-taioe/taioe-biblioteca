"""Cartas de Anchieta — grava conteudo/jose-de-anchieta/cartas-anchieta.js (chamado por montar.py --publicar).

Uma parte por peça, na ordem da edição de 1933, com o número romano dela (I, II, III, X…) e o título nosso
(destinatário, lugar e data). As peças escritas em latim ou castelhano abrem com uma linha em itálico que diz
a língua e de quem é a tradução; o texto da «Sobre» está em sobre.py.
"""
import json
import os
import re

import decisoes as D
import sobre

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
SAIDA = os.path.join(RAIZ, 'conteudo', 'jose-de-anchieta', 'cartas-anchieta.js')

LINGUA = {'la': 'latim', 'es': 'castelhano'}


def js_texto(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def gravar(pecas_m):
    blocos = []
    for p in pecas_m:
        corpo = []
        if p['lingua'] in LINGUA:
            corpo.append('_' + sobre.LINHA_TRADUCAO[p['n']] + '_')
        corpo += p['pars']
        blocos.append({'n': p['n'], 'titulo': p['titulo'], 'texto': '\n\n'.join(corpo)})
    edicao = {
        'base': '1933',
        'apresentacao': sobre.APRESENTACAO,
        'fontes': sobre.FONTES,
    }
    if D.ERROS:
        edicao['secoes'] = {'erros': {'titulo': 'Erros do impresso de 1933 corrigidos',
                                      'explica': 'Grafia de 1933 nas duas colunas.', 'de': '1933', 'para': 'Corrigido'}}
        edicao['erros'] = [{'cap': n, 'de': de, 'para': para} for n, de, para, _ in D.ERROS]
    meta = {
        'id': 'cartas-anchieta', 'autor': 'jose-de-anchieta', 'titulo': sobre.TITULO,
        'ano': 1594, 'datas': '1554–1594', 'genero': 'Cartas',
        'divisao': {'singular': 'peça', 'plural': 'peças', 'rotulo': 'nome', 'marcas': False},
        'descricao': sobre.DESCRICAO,
    }
    linhas = ['/* Cartas, informações e sermão (seleção) — São José de Anchieta',
              '   Gerado por edicoes/cartas-anchieta/montar.py --publicar a partir de edicoes/cartas-anchieta/1933/.',
              '   Não edite à mão: corrija as decisões em edicoes/cartas-anchieta/decisoes.py e rode de novo. */',
              'BIBLIOTECA.obra({']
    for chave, v in meta.items():
        linhas.append(f'  {chave}: {json.dumps(v, ensure_ascii=False)},')
    linhas.append('  edicao: ' + json.dumps(edicao, ensure_ascii=False, indent=2).replace('\n', '\n  ') + ',')
    linhas.append('  partes: [')
    for i, b in enumerate(blocos):
        fim = ',' if i + 1 < len(blocos) else ''
        linhas.append(f'    {{ n: {json.dumps(b["n"])}, titulo: {json.dumps(b["titulo"], ensure_ascii=False)}, texto: `{js_texto(b["texto"])}` }}{fim}')
    linhas.append('  ]')
    linhas.append('});')
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    open(SAIDA, 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
    print('gravado', os.path.relpath(SAIDA, RAIZ), sum(len(re.findall(r'\w+', b['texto'])) for b in blocos), 'palavras')
    idx = os.path.join(RAIZ, 'index.html')
    h = open(idx, encoding='utf-8').read()
    linha = '<script defer src="conteudo/jose-de-anchieta/cartas-anchieta.js"></script>'
    if linha not in h:
        h = h.replace('</head>', linha + '\n</head>', 1)
        open(idx, 'w', encoding='utf-8').write(h)
