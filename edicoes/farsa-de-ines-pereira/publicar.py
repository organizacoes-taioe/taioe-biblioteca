"""Farsa de Inês Pereira: de texto.txt ao arquivo do site, conteudo/gil-vicente/farsa-de-ines-pereira.js.

texto.txt já está no formato do site (fala «@ Nome», verso «| », rubrica em _itálico_). Sai de dois passos:
modernizar.py (o texto de 1834, passado a limpo em colacao/v1834-*.txt, na grafia de hoje) e montar.py
(as lições da Copilação de 1562, lidas no fac-símile da BNP, em licoes.py). Regras em CONVENCOES.md.

uso: python3 edicoes/farsa-de-ines-pereira/modernizar.py && python3 edicoes/farsa-de-ines-pereira/montar.py
     python3 edicoes/farsa-de-ines-pereira/publicar.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao import montar as site  # noqa: E402

META = {
    'id': 'farsa-de-ines-pereira',
    'autor': 'gil-vicente',
    'titulo': 'Farsa de Inês Pereira',
    'ano': 1523,
    'genero': 'Teatro',
    'divisao': {'singular': 'parte', 'plural': 'partes'},
    'descricao': 'Farsa representada a Dom João III no convento de Tomar, em 1523, sobre o dito «mais quero asno que me leve que cavalo que me derrube».',
}

APRESENTACAO = """**Texto-base.** Este texto reproduz a farsa como está na _Copilaçam de todalas obras de Gil Vicente_ (Lisboa, 1562), a edição das obras preparada por seus filhos, onde ela abre com o título «Auto de Inês Pereira», na grafia brasileira de hoje. Não se conhece folheto avulso impresso em vida do autor.

**Como foi estabelecido.** O texto da reimpressão de Hamburgo (1834), que reproduz a Copilação, foi passado a limpo a partir da leitura automática de duas digitalizações e depois relido verso a verso contra o fac-símile de 1562 da Biblioteca Nacional de Portugal. Onde as duas edições divergem, vale a de 1562: a edição de 1834 trocou palavras e formas, mudou a fala de alguns versos, reescreveu rubricas e acrescentou outras (as indicações «sai», «vai-se», «à parte», «lê a carta» não estão na Copilação e saíram daqui). Ficaram de 1834 só três emendas de erros evidentes de 1562: «ou marido ou maridinho / tenha o que houver mister» (1562: «marinho», «tenho»), «Sirvo allí mi Dios Cupido» (1562: «mis dias») e a fala «Dai-me vós cá essa chave», que 1562 não dá a Inês.

**Grafia.** A mesma regra de _Os Lusíadas_ e das duas Barcas: muda só a maneira de escrever, nunca a forma da palavra. Ficam _pera_, _assi_, _cousa_, _dous_, _mi_, _sam_ (sou), _perém_, _milhor_, _fogir_, _cospir_, _curuja_, _lião_, _exempro_, _concrusão_, _leixar_, _ũa_. As falas do Ermitão e as cantigas castelhanas ficam em castelhano, na grafia de 1834.

**Divisão.** A farsa é uma cena só. Para facilitar a leitura, ela está dividida aqui em dez partes, pela chegada de cada personagem; a divisão e os títulos são nossos."""

FONTES = [
    {'nome': 'Copilaçam de todalas obras de Gil Vicente (Lisboa, 1562), fac-símile da Biblioteca Nacional de Portugal', 'url': 'https://purl.pt/11494',
     'nota': 'o texto-base; a farsa está nos fólios CCXIII v.º–CCXX v.º'},
    {'nome': 'Obras de Gil Vicente, tomo III (Hamburgo, 1834), exemplar da Universidade de Toronto', 'url': 'https://archive.org/details/obrasvic03viceuoft',
     'nota': 'reimpressão da Copilação; pp. 121–159, passadas a limpo e conferidas com 1562'},
    {'nome': 'Obras de Gil Vicente, tomo III (Hamburgo, 1834), outro exemplar', 'url': 'https://archive.org/details/obrasdegilvicen02vicegoog',
     'nota': 'para desempatar a leitura automática'},
]

# divisão nossa, pela chegada de cada personagem (a farsa é uma cena só); cada marca vale uma vez, em ordem
PARTES = [('@ Lianor Vaz', 'Lianor Vaz'), ('_Vem Pero Marques', 'Pero Marques'),
          ('@ Latão', 'Os Judeus casamenteiros'), ('_Vem o Escudeiro', 'O Escudeiro'),
          ('_Vem a Mãe com certas moças', 'A boda'), ('_Vai-se, e fica o Escudeiro', 'O marido'),
          ('_Entra o Moço com ũa carta', 'A carta de Arzila'), ('_Vem Lianor Vaz visitá-la', 'O segundo casamento'),
          ('_Vem um Ermitão', 'O Ermitão')]


def publicar():
    texto = open(os.path.join(AQUI, 'texto.txt'), encoding='utf-8').read().strip()
    blocos = [b for b in texto.split('\n\n') if b.strip()]
    partes = [{'n': '', 'titulo': 'Inês e a Mãe', 'paragrafos': []}]
    prox = 0
    for b in blocos:
        if prox < len(PARTES) and b.startswith(PARTES[prox][0]):
            partes.append({'n': '', 'titulo': PARTES[prox][1], 'paragrafos': []})
            prox += 1
        partes[-1]['paragrafos'].append(b)
    assert prox == len(PARTES), [p['titulo'] for p in partes]
    edicao = {'base': 'Copilação de 1562', 'apresentacao': APRESENTACAO, 'fontes': FONTES}
    destino = os.path.join(RAIZ, 'conteudo', META['autor'], META['id'] + '.js')
    comentario = ('Farsa de Inês Pereira — Gil Vicente\n   Gerado por edicoes/farsa-de-ines-pereira/publicar.py. Não edite à mão:\n'
                  '   corrija edicoes/farsa-de-ines-pereira/licoes.py ou grafia.py e rode modernizar.py, montar.py e este.')
    site.publicar(destino, META, partes, edicao, comentario)
    rel = 'conteudo/' + META['autor'] + '/' + META['id'] + '.js'
    if site.registrar_no_index(os.path.join(RAIZ, 'index.html'), rel):
        print('acrescentado ao index.html:', rel)
    print('publicado:', destino, f'({texto.count(chr(10) + "| ") + 1} versos, {len(partes)} partes)')


if __name__ == '__main__':
    publicar()
