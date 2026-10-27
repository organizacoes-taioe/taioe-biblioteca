"""Grava o obra.py de cada documento do Magistério (os dados que ferramentas/traducoes.py lê).

    python3 edicoes/magisterio/obras.py [documento ...]

Os dados de cada documento ficam em DOCS, abaixo; as correções feitas no texto de base, em
CORRECOES (resumo do que está nas notas do tradutor, traducao/notas-<documento>.md). Publicar:
python3 ferramentas/traducoes.py magisterio/<documento>.
"""
import os
import pprint
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))

# id: (título, subtítulo, tipo, papa, data por extenso, ano, língua, código, citação, url do texto, url do PDF)
DOCS = {
    'divini-redemptoris': ('Divini Redemptoris', 'Sobre o comunismo ateu', 'Carta encíclica', 'Pio XI',
        '19 de março de 1937', 1937, 'latim', 'la', 'AAS 29 (1937), p. 65-106',
        'https://www.vatican.va/content/pius-xi/la/encyclicals/documents/hf_p-xi_enc_19370319_divini-redemptoris.html',
        'https://www.vatican.va/archive/aas/documents/AAS-29-1937-ocr.pdf'),
    'quadragesimo-anno': ('Quadragesimo Anno', 'Sobre a restauração da ordem social', 'Carta encíclica', 'Pio XI',
        '15 de maio de 1931', 1931, 'latim', 'la', 'AAS 23 (1931), p. 177-228',
        'https://www.vatican.va/content/pius-xi/la/encyclicals/documents/hf_p-xi_enc_19310515_quadragesimo-anno.html',
        'https://www.vatican.va/archive/aas/documents/AAS-23-1931-ocr.pdf'),
    'divini-illius-magistri': ('Divini Illius Magistri', 'Sobre a educação cristã da juventude', 'Carta encíclica', 'Pio XI',
        '31 de dezembro de 1929', 1929, 'latim', 'la', 'AAS 22 (1930), p. 49-86',
        'https://www.vatican.va/content/pius-xi/la/encyclicals/documents/hf_p-xi_enc_31121929_divini-illius-magistri.html',
        'https://www.vatican.va/archive/aas/documents/AAS-22-1930-ocr.pdf'),
    'mortalium-animos': ('Mortalium Animos', 'Sobre a promoção da verdadeira unidade religiosa', 'Carta encíclica', 'Pio XI',
        '6 de janeiro de 1928', 1928, 'latim', 'la', 'AAS 20 (1928), p. 5 e seguintes',
        'https://www.vatican.va/content/pius-xi/la/encyclicals/documents/hf_p-xi_enc_19280106_mortalium-animos.html',
        'https://www.vatican.va/archive/aas/documents/AAS-20-1928-ocr.pdf'),
    'maximum-illud': ('Maximum Illud', 'Sobre a propagação da fé católica no mundo', 'Carta apostólica', 'Bento XV',
        '30 de novembro de 1919', 1919, 'latim', 'la', 'AAS 11 (1919), p. 440-455',
        'https://www.vatican.va/content/benedict-xv/la/apost_letters/documents/hf_ben-xv_apl_19191130_maximum-illud.html',
        'https://www.vatican.va/archive/aas/documents/AAS-11-1919-ocr.pdf'),
    'pascendi': ('Pascendi Dominici Gregis', 'Sobre as doutrinas dos modernistas', 'Carta encíclica', 'São Pio X',
        '8 de setembro de 1907', 1907, 'latim', 'la', 'ASS 40 (1907), p. 593 e seguintes',
        'https://www.vatican.va/content/pius-x/la/encyclicals/documents/hf_p-x_enc_19070908_pascendi-dominici-gregis.html',
        'https://www.vatican.va/archive/ass/documents/ASS-40-1907-ocr.pdf'),
    'tra-le-sollecitudini': ('Tra le sollecitudini', 'Sobre a música sacra', 'Motu proprio', 'São Pio X',
        '22 de novembro de 1903', 1903, 'italiano', 'it', 'ASS 36 (1903-1904), p. 329-339',
        'https://www.vatican.va/content/pius-x/it/motu_proprio/documents/hf_p-x_motu-proprio_19031122_sollecitudini.html',
        'https://www.vatican.va/archive/ass/documents/ASS-36-1903-4-ocr.pdf'),
    'rerum-novarum': ('Rerum Novarum', 'Sobre a condição dos operários', 'Carta encíclica', 'Leão XIII',
        '15 de maio de 1891', 1891, 'latim', 'la', 'ASS 23 (1890-1891), p. 641-670',
        'https://www.vatican.va/content/leo-xiii/la/encyclicals/documents/hf_l-xiii_enc_15051891_rerum-novarum.html',
        'https://www.vatican.va/archive/ass/documents/ASS-23-1890-91-ocr.pdf'),
    'immortale-dei': ('Immortale Dei', 'Sobre a constituição cristã dos Estados', 'Carta encíclica', 'Leão XIII',
        '1º de novembro de 1885', 1885, 'latim', 'la', 'ASS 18 (1885), p. 161 e seguintes',
        'https://www.vatican.va/content/leo-xiii/la/encyclicals/documents/hf_l-xiii_enc_01111885_immortale-dei.html',
        'https://www.vatican.va/archive/ass/documents/ASS-18-1885-ocr.pdf'),
    'humanum-genus': ('Humanum Genus', 'Sobre a seita dos maçons', 'Carta encíclica', 'Leão XIII',
        '20 de abril de 1884', 1884, 'latim', 'la', 'ASS 16 (1883-1884), p. 417 e seguintes',
        'https://www.vatican.va/content/leo-xiii/la/encyclicals/documents/hf_l-xiii_enc_18840420_humanum-genus.html',
        'https://www.vatican.va/archive/ass/documents/ASS-16-1883-84-1-576+supplemento-17-96-ocr.pdf'),
}
ACTA = {'AAS': '_Acta Apostolicae Sedis_', 'ASS': '_Acta Sanctae Sedis_'}
NUMERACAO = {   # de onde vem a numeração dos parágrafos (a marca à margem)
    'tra-le-sollecitudini': 'Os números dos parágrafos são os do próprio documento.',
}
CORRECOES = {}  # id: frase sobre as correções feitas no texto de base


def meta(doc):
    tit, sub, tipo, papa, data, ano, lingua, cod, citacao, url, pdf = DOCS[doc]
    acta = ACTA[citacao[:3]]
    numeracao = NUMERACAO.get(doc, 'A pequena marca à margem dá a numeração dos parágrafos mais usada nas '
                                   'citações, a da versão inglesa do site do Vaticano.')
    texto = (f'**O documento.** {tipo} de {papa}, de {data}. O texto de base é o {lingua} oficial, publicado nas '
             f'{acta} ({citacao}), na transcrição do site da Santa Sé. ' + CORRECOES.get(doc, ''))
    return {
        'id': doc, 'autor': 'igreja-catolica', 'titulo': tit, 'subtitulo': sub,
        'ano': ano, 'datas': f'{papa}, {ano}', 'genero': 'Magistério', 'grupo': papa, 'documento': True,
        'traducao': {'lingua': lingua, 'codigo': cod, 'titulo': tit},
        'original_ao_lado': True,
        'edicao': {
            'titulo': 'Sobre esta tradução',
            'apresentacao': (
                texto.strip() + '\n\n'
                '**A tradução.** Nossa, feita do ' + lingua + ', em português do Brasil. As citações da Escritura e de '
                'outros documentos foram traduzidas como o documento as dá, e as notas são as dele. ' + numeracao + '\n\n'
                f'**O original ao lado.** O botão «{lingua.capitalize()}», no alto da página de leitura, mostra o texto '
                f'{"latino" if cod == "la" else "italiano"} junto da tradução.'),
            'fontes': [
                {'nome': f'Site da Santa Sé, texto em {lingua}', 'url': url},
                {'nome': f'{acta.strip("_")}, {citacao}', 'url': pdf, 'nota': 'o texto oficial, em fac-símile'},
            ],
        },
    }


def gravar(doc):
    pasta = os.path.join(RAIZ, doc)
    os.makedirs(pasta, exist_ok=True)
    with open(os.path.join(pasta, 'obra.py'), 'w', encoding='utf-8') as f:
        f.write(f'"""{DOCS[doc][0]} — dados para ferramentas/traducoes.py. Gerado por edicoes/magisterio/obras.py;\n'
                'não edite à mão."""\n\n')
        f.write('META = ' + pprint.pformat(meta(doc), width=110, sort_dicts=False) + '\n\n')
        f.write(f"PARTES = [('', '', ['{doc}.txt'])]\n")
    print('gravado:', os.path.relpath(os.path.join(pasta, 'obra.py'), RAIZ))


if __name__ == '__main__':
    for d in sys.argv[1:] or DOCS:
        gravar(d)
