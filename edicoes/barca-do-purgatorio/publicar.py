"""Auto da Barca do Purgatório: de texto.txt ao arquivo do site, conteudo/gil-vicente/auto-da-barca-do-purgatorio.js.

texto.txt já está no formato do site (fala «@ Nome», verso «| », rubrica em _itálico_), passado a limpo
à mão da Copilação de 1562 pela reimpressão de Hamburgo (1834), tomo I, pp. 245–273: lido nas imagens do
exemplar obrasdegilvicen00montgoog do Internet Archive (páginas n295–n323) e conferido palavra por palavra
com o OCR das três cópias (00montgoog, 04vicegoog, 03vicegoog), que estão em
ferramentas/cache/barca-do-inferno/ (fora do git). Regras em CONVENCOES.md.

uso: python3 edicoes/barca-do-purgatorio/publicar.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao import montar as site  # noqa: E402

META = {
    'id': 'auto-da-barca-do-purgatorio',
    'autor': 'gil-vicente',
    'titulo': 'Auto da Barca do Purgatório',
    'ano': 1518,
    'genero': 'Teatro',
    'divisao': {'singular': 'parte', 'plural': 'partes'},
    'descricao': 'Auto de moralidade representado nas matinas do Natal de 1518, a segunda das três barcas.',
}

APRESENTACAO = """**Texto-base.** Este texto reproduz o _Auto da Barca do Purgatório_ como está na _Copilaçam de todalas obras de Gil Vicente_ (Lisboa, 1562), a edição das obras preparada por seus filhos, na grafia brasileira de hoje.

**Como foi estabelecido.** A Copilação foi lida na reimpressão de Hamburgo (1834), que a reproduz: página a página, nas imagens de um exemplar, e conferida palavra por palavra com a leitura automática de três digitalizações dessa edição. Ao contrário do _Auto da Barca do Inferno_, deste auto não se conhece folheto impresso em vida do autor; o texto vem só da Copilação.

**Grafia.** A mesma regra de _Os Lusíadas_ e da _Barca do Inferno_: muda só a maneira de escrever, nunca a forma da palavra. Ficam _pera_, _assi_, _cousa_, _noute_, _mi_, _inda_, _samicas_, _eramá_, _bofá_, _rezão_, _perém_, _imigo_, _concrusão_, _Satão_. O latim do Lavrador e do Pastor fica como está.

**Divisão.** O auto é uma cena só, a segunda das três barcas, representada à rainha Dona Leonor nas matinas do Natal de 1518. Para facilitar a leitura, ele está dividido aqui em sete partes, pela chegada de cada personagem; a divisão é nossa."""

FONTES = [
    {'nome': 'Obras de Gil Vicente, tomo I (Hamburgo, 1834), exemplar digitalizado pelo Google', 'url': 'https://archive.org/details/obrasdegilvicen00montgoog',
     'nota': 'reimpressão da Copilação de 1562; o texto foi lido nas imagens deste exemplar (pp. 245–273)'},
    {'nome': 'Obras de Gil Vicente, tomo I (Hamburgo, 1834), outro exemplar', 'url': 'https://archive.org/details/obrasdegilvicen04vicegoog',
     'nota': 'para a conferência palavra por palavra'},
    {'nome': 'Obras de Gil Vicente, tomo I (Hamburgo, 1834), terceiro exemplar', 'url': 'https://archive.org/details/obrasdegilvicen03vicegoog',
     'nota': 'para a conferência palavra por palavra'},
]


# divisão nossa, pela chegada de cada personagem (o auto é uma cena só)
PARTES = [('_Vem um Lavrador', 'O Lavrador'), ('_Vem ũa regateira', 'Marta Gil'), ('_Vem um Pastor', 'O Pastor'),
          ('_Vem ũa Pastora', 'A Pastora'), ('_Vem um Menino', 'O Menino'), ('_Cantando, metem os Anjos', 'O Taful')]


def publicar():
    texto = open(os.path.join(AQUI, 'texto.txt'), encoding='utf-8').read().strip()
    blocos = [b for b in texto.split('\n\n') if b.strip()]
    partes = []
    for b in blocos:
        tit = next((t for marca, t in PARTES if b.startswith(marca)), None)
        if tit or not partes:
            partes.append({'n': '', 'titulo': tit or 'Os Arrais', 'paragrafos': []})
        partes[-1]['paragrafos'].append(b)
    assert len(partes) == len(PARTES) + 1, [p['titulo'] for p in partes]
    edicao = {'base': 'Edição de 1834', 'apresentacao': APRESENTACAO, 'fontes': FONTES}
    destino = os.path.join(RAIZ, 'conteudo', META['autor'], META['id'] + '.js')
    comentario = ('Auto da Barca do Purgatório — Gil Vicente\n   Gerado por edicoes/barca-do-purgatorio/publicar.py. Não edite à mão:\n'
                  '   corrija edicoes/barca-do-purgatorio/texto.txt e rode de novo.')
    site.publicar(destino, META, partes, edicao, comentario)
    rel = 'conteudo/' + META['autor'] + '/' + META['id'] + '.js'
    if site.registrar_no_index(os.path.join(RAIZ, 'index.html'), rel):
        print('acrescentado ao index.html:', rel)
    print('publicado:', destino, f'({texto.count(chr(10) + "| ") + 1} versos)')


if __name__ == '__main__':
    publicar()
