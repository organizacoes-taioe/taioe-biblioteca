"""Auto da Barca do Inferno: de texto.txt ao arquivo do site, conteudo/gil-vicente/auto-da-barca-do-inferno.js.

texto.txt já está no formato do site (fala «@ Nome», verso «| », rubrica em _itálico_), passado a limpo
à mão da Copilação de 1562 pela reimpressão de Hamburgo (1834): duas cópias OCR (Internet Archive
obrasdegilvicen04vicegoog e obrasdegilvicen00montgoog; a 03vicegoog para desempatar), em
ferramentas/cache/barca-do-inferno/ (fora do git). Regras em CONVENCOES.md.

uso: python3 edicoes/barca-do-inferno/publicar.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao import montar as site  # noqa: E402

META = {
    'id': 'auto-da-barca-do-inferno',
    'autor': 'gil-vicente',
    'titulo': 'Auto da Barca do Inferno',
    'ano': 1517,
    'genero': 'Teatro',
    'divisao': {'singular': 'parte', 'plural': 'partes'},
    'descricao': 'Auto de moralidade representado em 1517: as almas chegam ao rio e escolhem entre a barca do Inferno e a da Glória.',
}

APRESENTACAO = """**Texto-base.** Este texto reproduz o _Auto da Barca do Inferno_ como está na _Copilaçam de todalas obras de Gil Vicente_ (Lisboa, 1562), a edição das obras preparada por seus filhos, na grafia brasileira de hoje.

**Como foi estabelecido.** A Copilação foi lida na reimpressão de Hamburgo (1834), que a reproduz. Foram confrontadas palavra por palavra duas digitalizações dessa edição, e uma terceira desempatou as leituras duvidosas. O auto já tinha sido impresso em vida do autor, num folheto de cerca de 1518, que difere da Copilação em muitos versos (é esse o texto do Wikisource); aqui se segue a versão das Obras. Uma emenda: na terceira fala do Diabo, «Ora venho a caro a ré», da edição de 1834, passou a «Ora venha o caro a ré», como no folheto.

**Grafia.** A mesma regra de _Os Lusíadas_: muda só a maneira de escrever, nunca a forma da palavra. Ficam _pera_, _assi_, _cousa_, _dous_, _mi_, _inda_, _samicas_, _eramá_, _muitieramá_, _bo'hora_, _jentar_. O latim macarrônico do Corregedor, do Diabo e do Parvo fica como está, e a cantiga do Diabo, em castelhano.

**Divisão.** O auto é uma cena só, a primeira das três barcas (o Purgatório e a Glória são autos à parte). Para facilitar a leitura, ele está dividido aqui em dez partes, pela chegada de cada personagem; a divisão é nossa."""

FONTES = [
    {'nome': 'Obras de Gil Vicente, tomo I (Hamburgo, 1834), exemplar digitalizado pelo Google', 'url': 'https://archive.org/details/obrasdegilvicen04vicegoog',
     'nota': 'reimpressão da Copilação de 1562; a primeira das duas cópias confrontadas'},
    {'nome': 'Obras de Gil Vicente, tomo I (Hamburgo, 1834), outro exemplar', 'url': 'https://archive.org/details/obrasdegilvicen00montgoog',
     'nota': 'a segunda cópia confrontada'},
    {'nome': 'Obras de Gil Vicente, tomo I (Hamburgo, 1834), terceiro exemplar', 'url': 'https://archive.org/details/obrasdegilvicen03vicegoog',
     'nota': 'para desempatar as leituras duvidosas'},
]


# divisão nossa, pela chegada de cada personagem (o auto é uma cena só)
PARTES = [('_Chega um Onzeneiro', 'O Onzeneiro'), ('_Vem um Parvo', 'O Parvo'), ('_Vem um Sapateiro', 'O Sapateiro'),
          ('_Entra um Frade', 'O Frade'), ('_Vem ũa Alcoviteira', 'A Alcoviteira'), ('_Vem um Judeu', 'O Judeu'),
          ('_Vem um Corregedor', 'O Corregedor e o Procurador'), ('_Vem um Enforcado', 'O Enforcado'),
          ('_Vêm quatro fidalgos', 'Os Cavaleiros')]


def publicar():
    texto = open(os.path.join(AQUI, 'texto.txt'), encoding='utf-8').read().strip()
    blocos = [b for b in texto.split('\n\n') if b.strip()]
    partes = []
    for b in blocos:
        tit = next((t for marca, t in PARTES if b.startswith(marca)), None)
        if tit or not partes:
            partes.append({'n': '', 'titulo': tit or 'O Fidalgo', 'paragrafos': []})
        partes[-1]['paragrafos'].append(b)
    assert len(partes) == len(PARTES) + 1, [p['titulo'] for p in partes]
    edicao = {'base': 'Edição de 1834', 'apresentacao': APRESENTACAO, 'fontes': FONTES}
    destino = os.path.join(RAIZ, 'conteudo', META['autor'], META['id'] + '.js')
    comentario = ('Auto da Barca do Inferno — Gil Vicente\n   Gerado por edicoes/barca-do-inferno/publicar.py. Não edite à mão:\n'
                  '   corrija edicoes/barca-do-inferno/texto.txt e rode de novo.')
    site.publicar(destino, META, partes, edicao, comentario)
    rel = 'conteudo/' + META['autor'] + '/' + META['id'] + '.js'
    if site.registrar_no_index(os.path.join(RAIZ, 'index.html'), rel):
        print('acrescentado ao index.html:', rel)
    print('publicado:', destino, f'({texto.count(chr(10) + "| ") + 1} versos)')


if __name__ == '__main__':
    publicar()
