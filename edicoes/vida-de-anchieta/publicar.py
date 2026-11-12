"""Vida de Anchieta — grava conteudo/pero-rodrigues/vida-de-anchieta.js (chamado por montar.py --publicar).

Duas partes, como o impresso («1.ª PARTE»; «2.ª Parte do Livro 3.º — Dos milagres que Deos obrou pelo
Padre José»), com os 25 capítulos numerados seguidos dentro delas: «## Capítulo N — título» e a marca
«{§ P.N}» no primeiro parágrafo, que o gerador usa para dividir as páginas (divisao.marcas = false a esconde),
como em _Policarpo Quaresma_.
"""
import json
import os
import re

import decisoes as D

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
SAIDA = os.path.join(RAIZ, 'conteudo', 'pero-rodrigues', 'vida-de-anchieta.js')

TITULOS_PARTES = ['Primeira parte', 'Segunda parte: Dos milagres que Deus obrou pelo Padre José']

APRESENTACAO = """**Texto-base.** Esta edição reproduz a _Vida do Padre José de Anchieta_ impressa nos _Anais da Biblioteca Nacional do Rio de Janeiro_, vol. XIX (1897), pp. 1–49. É a cópia que A. F. Barata fez em Évora, em agosto de 1896, de um códice da Biblioteca Pública de Évora (cota CX/1-17), que termina com a data «Na Baía, a 3º de janeiro de 1607» e a assinatura de Pero Rodrigues. Barata diz que o manuscrito talvez seja o original e que o copiou «na orthographia actual», salvo algumas palavras que deixou por caracterizarem o século («giolho», «antre», «devação»). Diz também que a divisão não é regular: o texto se abre com «1ª parte», chama a segunda de «2ª parte do livro 3º» e termina com «Fim do livro 3º», mas os 25 capítulos se numeram seguidos, e há remissões a um «livro 1º» e a um «livro 2º» que o códice não traz. No mesmo volume, Eduardo Prado informa que a Biblioteca Nacional de Lisboa (fundo de Alcobaça) guarda uma cópia muito mais longa, de 1608–1609, em quatro livros, com uma carta do provincial Fernão Cardim e a dedicatória do autor aos padres da Companhia. Essa versão não está aqui.

**Como foi estabelecido.** O texto saiu do fac-símile do exemplar de José Mindlin (Biblioteca Brasiliana Guita e José Mindlin, USP). Foram confrontadas três leituras por OCR (a camada de texto do PDF e duas feitas por nós com o Tesseract), e cada linha foi conferida nas imagens das páginas. As edições do século XX são protegidas e não foram usadas.

**Grafia.** Ortografia de hoje (Acordo de 1990, forma brasileira), com as palavras e a ordem das frases do impresso: annos → anos, Deos → Deus, cousa → coisa, pera → para, assi → assim, giolho → joelho, antre → entre, devação → devoção, lingoa → língua, logar → lugar, testimunha → testemunha, noute → noite, fuão → fulano, té → até. As mesóclises do autor ficam (chamar-se-á, lográ-la-eis). Nomes de pessoas e de lugares vão na forma de hoje (Estêvão, Cristóvão, Inácio, Luís, Tenerife, Bertioga, Itaparica, Bahia, Flandres); os nomes dos povos indígenas, como no impresso (Maramomis, Moramomis, Tupiniquis, Tumimimos, Pitigares). Palavras que não se usam mais ficam como estão (comenos, gasalhado, lacão, cofo, croncrenas, lissão). Os trechos em latim vão em itálico. A pontuação e as maiúsculas são as de 1897, salvo os meses, em minúscula, e os pontos listados abaixo.

**O que saiu do texto.** As marcas do copista: a lição do manuscrito entre parênteses, depois da palavra como ele a leu («começo (comuco)», «fervor (heiuor)», «víbora (bibara)», «José Adortio (adortio)»), cinco «(sic)» e a nota de rodapé a «lissão» («ou tissão = tição?»). Duas leituras dele marcadas com «(sic)» foram emendadas: «infabilidade» → «afabilidade» (cap. 4) e «Garcia da villa» → «Garcia d'Ávila» (cap. 19), o nome do pai de Isabel de Ávila."""

FONTES = [
    {'nome': 'Annaes da Bibliotheca Nacional do Rio de Janeiro, vol. XIX (1897), exemplar José Mindlin (Brasiliana USP, fac-símile)',
     'url': 'https://digital.bbm.usp.br/handle/bbm/6953', 'nota': 'texto-base, pp. 1–49'},
]


def js_texto(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def rotulo_cap(n):
    return ('I' if n <= 19 else 'II') + f', cap. {n}'


def gravar(partes):
    blocos = []
    for k, p in enumerate(partes):
        rom = ['I', 'II'][k]
        corpo = []
        if k == 0:
            corpo += ['_' + t.strip('_') + '_' for t in p['pre_m']]
        for c in p['caps']:
            titulo = c['titulo_m'] or '(sem título)'
            corpo.append(f'## Capítulo {c["n"]} — {titulo}')
            pars = list(c['pars_m'])
            pars[0] = f'{{§ {rom}.{c["n"]}}} ' + pars[0]
            corpo += pars
        blocos.append({'n': rom, 'titulo': TITULOS_PARTES[k], 'texto': '\n\n'.join(corpo)})
    # capítulo de cada erro: o que contém o trecho de 1897
    def cap_de(de):
        for p in partes:
            for c in p['caps']:
                if any(de in t for t, _ in c['pars']):
                    return c['n']
        raise ValueError(de)
    erros = sorted(({'n': cap_de(de), 'de': de, 'para': para} for pag, de, para, _ in D.ERROS), key=lambda e: e['n'])
    erros = [{'cap': rotulo_cap(e['n']), 'de': e['de'], 'para': e['para']} for e in erros]
    edicao = {
        'base': '1897',
        'apresentacao': APRESENTACAO,
        'secoes': {'erros': {'titulo': 'Erros do impresso de 1897 corrigidos',
                             'explica': 'Grafia de 1897 nas duas colunas.', 'de': '1897', 'para': 'Corrigido'}},
        'erros': erros,
        'fontes': FONTES,
    }
    meta = {
        'id': 'vida-de-anchieta', 'autor': 'pero-rodrigues', 'titulo': 'Vida do Padre José de Anchieta',
        'ano': 1607, 'genero': 'Hagiografia',
        'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome', 'marcas': False},
        'descricao': 'A primeira vida de São José de Anchieta, escrita no Brasil por um jesuíta que o conheceu, '
                     'a partir dos testemunhos jurados reunidos depois da sua morte; a versão do códice de Évora, de 1607.',
    }
    linhas = ['/* Vida do Padre José de Anchieta — Pero Rodrigues',
              '   Gerado por edicoes/vida-de-anchieta/montar.py --publicar a partir de edicoes/vida-de-anchieta/1897/.',
              '   Não edite à mão: corrija as decisões em edicoes/vida-de-anchieta/decisoes.py e rode de novo. */',
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
    # index.html: a linha do script
    idx = os.path.join(RAIZ, 'index.html')
    h = open(idx, encoding='utf-8').read()
    linha = '<script defer src="conteudo/pero-rodrigues/vida-de-anchieta.js"></script>'
    if linha not in h:
        h = h.replace('</head>', linha + '\n</head>', 1)
        open(idx, 'w', encoding='utf-8').write(h)
