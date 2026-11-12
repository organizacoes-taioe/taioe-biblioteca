"""Diário da navegação — grava conteudo/pero-lopes-de-sousa/diario-da-navegacao.js (chamado por montar.py --publicar).

Oito partes (divisão nossa, por trechos da viagem, com as datas); cada parágrafo é um dia do diário, como no
impresso de 1839. Sem marcas de página.
"""
import json
import os
import re

import decisoes as D

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
SAIDA = os.path.join(RAIZ, 'conteudo', 'pero-lopes-de-sousa', 'diario-da-navegacao.js')

# (primeira entrada, título): a última vai até a próxima
PARTES = [
    (0, 'De Lisboa a Cabo Verde (dezembro de 1530)'),
    (25, 'De Cabo Verde ao cabo de Santo Agostinho (janeiro de 1531)'),
    (52, 'As naus francesas e Pernambuco (31 de janeiro a 19 de fevereiro de 1531)'),
    (64, 'De Pernambuco ao Rio de Janeiro (março e abril de 1531)'),
    (114, 'O Rio de Janeiro e a costa do sul (30 de abril a setembro de 1531)'),
    (126, 'O temporal e a perda da nau capitânia (setembro a novembro de 1531)'),
    (157, 'O rio da Prata e o Uruguai (novembro e dezembro de 1531)'),
    (188, 'A volta a São Vicente (janeiro e fevereiro de 1532)'),
]

APRESENTACAO = """**Texto-base.** Esta edição reproduz o diário de Pero Lopes de Sousa impresso por Francisco Adolfo de Varnhagen em Lisboa, em 1839 (_Diário da navegação da armada que foi à terra do Brasil em 1530 sob a capitania-mor de Martim Afonso de Sousa, escrito por seu irmão Pero Lopes de Sousa_, Tipografia da Sociedade Propagadora dos Conhecimentos Úteis, pp. 3–59), a primeira edição da obra. Varnhagen imprimiu uma cópia do século XVIII, de 72 páginas, que lhe chegou às mãos, e a cotejou com um códice quase contemporâneo da Biblioteca Real (hoje da Ajuda), copiado por volta do tempo do autor, o único outro que achou inteiro. O título «Diário» é dele; o códice da Ajuda traz, em letra mais tardia, «Navegação que fez Pero Lopes de Sousa no descobrimento da costa do Brasil militando na capitania de Martim Afonso de Sousa seu irmão». O texto de 1839 já vem com a ortografia regularizada por Varnhagen (nam, hum, meo, menhãa, cousa), mas as palavras são as do manuscrito; ele imprimiu em grifo as palavras que o códice da Ajuda traz riscadas, e aqui não há marca nenhuma delas.

**Como foi estabelecido.** O texto saiu do fac-símile do Internet Archive. Foram confrontadas três leituras por OCR (a do próprio Archive, uma nossa com o Tesseract e a do outro exemplar de 1839, do Google Livros), cada linha foi conferida nas imagens das páginas, e a quarta edição de Varnhagen (Rio de Janeiro, 1867) serviu de terceira testemunha nos pontos duvidosos. A edição comentada de Eugênio de Castro (1927) não foi usada.

**Divisão.** O diário corre por dias, e cada parágrafo é um dia (o autor muitas vezes escreve só «do dito mês»). A divisão em oito partes, com os títulos e as datas, é nossa: segue os trechos da viagem. Fica de fora o resto do volume de Varnhagen (biografias, notas, documentos) e o fragmento da volta de Pero Lopes a Portugal (maio a agosto de 1532, do códice da Ajuda), que ele pôs numa nota, pp. 109–113.

**Grafia.** Ortografia de hoje (Acordo de 1990, forma brasileira), com as palavras e a ordem do impresso: nam → não, hum → um, hũa → uma, meo → meio, cousa → coisa, assi → assim, antre → entre, fermosa → formosa, menhãa → manhã, graos → graus, leguas → léguas, homẽs → homens, a nao → a nau, todolos → todos os, despois → depois. A forma «gram» antes de substantivo vai para «grande»; «mui» fica. O capitão que o texto chama «capitam J.» (no códice da Ajuda, «I.», que Varnhagen lê como «irmão») é Martim Afonso, e vai como «o capitão». Os dias da semana levam hífen (segunda-feira). Nomes de pessoas e lugares na forma de hoje (Lisboa, Noronha, Maranhão, Sofala, Tenerife, Piratininga, São Vicente, Santo Agostinho); os nomes dos povos e dos rios da região do Prata ficam como no impresso (Beguoais, Chanás, Carandins). Os rumos da agulha ganham o hífen e o acento de hoje (nornordeste → nor-nordeste, lesnordeste → lés-nordeste, essudoeste → és-sudoeste). As palavras náuticas e antigas que não se usam mais ficam como estão, com nota no vocabulário (a quarta, o bordo, pairar, a modorra, abarlaventear, o bargantim)."""

FONTES = [
    {'nome': 'Varnhagen, Diário da navegação da armada que foi à terra do Brasil em 1530 (Lisboa, 1839), exemplar do Internet Archive (fac-símile)',
     'url': 'https://archive.org/details/diario_navegacao_souza', 'nota': 'texto-base, pp. 3–59'},
    {'nome': 'O mesmo, outro exemplar de 1839, Google Livros (Internet Archive)',
     'url': 'https://archive.org/details/bub_gb_-F8CAAAAYAAJ', 'nota': 'segunda leitura do OCR'},
    {'nome': 'Varnhagen, Diário de navegação pela costa do Brazil até o Rio Uruguay, 4.ª ed. (Rio de Janeiro, 1867)',
     'url': 'https://archive.org/details/diariodenavegao00varngoog', 'nota': 'terceira testemunha'},
]


def js_texto(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def gravar(es, mod):
    limites = [p[0] for p in PARTES] + [len(mod)]
    blocos = []
    for k, (ini, titulo) in enumerate(PARTES):
        blocos.append({'n': str(k + 1), 'titulo': titulo, 'texto': '\n\n'.join(mod[ini:limites[k + 1]])})

    def parte_de(i):
        return max(k for k, (ini, _) in enumerate(PARTES) if ini <= i) + 1
    erros = []
    for de, para in D.ERROS:
        i = next(i for i, e in enumerate(es) if de in e)
        erros.append({'cap': f'Parte {parte_de(i)}', 'de': de, 'para': para})
    edicao = {
        'base': '1839',
        'apresentacao': APRESENTACAO,
        'secoes': {'erros': {'titulo': 'Erros do impresso de 1839 corrigidos',
                             'explica': 'Grafia de 1839 nas duas colunas.', 'de': '1839', 'para': 'Corrigido'}},
        'erros': erros,
        'fontes': FONTES,
    }
    meta = {
        'id': 'diario-da-navegacao', 'autor': 'pero-lopes-de-sousa', 'titulo': 'Diário da navegação',
        'ano': 1532, 'genero': 'Diário de viagem',
        'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome', 'marcas': False},
        'descricao': 'O diário da armada de Martim Afonso de Sousa ao Brasil e ao rio da Prata (1530–1532), '
                     'escrito dia a dia por seu irmão Pero Lopes de Sousa: a costa, os ventos, os franceses, '
                     'os índios, a fundação de São Vicente.',
    }
    linhas = ['/* Diário da navegação — Pero Lopes de Sousa',
              '   Gerado por edicoes/diario-pero-lopes/montar.py --publicar a partir de edicoes/diario-pero-lopes/1839/.',
              '   Não edite à mão: corrija as decisões em edicoes/diario-pero-lopes/decisoes.py e rode de novo. */',
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
    linha = '<script defer src="conteudo/pero-lopes-de-sousa/diario-da-navegacao.js"></script>'
    if linha not in h:
        h = h.replace('</head>', linha + '\n</head>', 1)
        open(idx, 'w', encoding='utf-8').write(h)
