"""Crónica de D. Pedro I (Fernão Lopes) — grava conteudo/fernao-lopes/cronica-de-d-pedro-i.js a partir das
fontes da pasta (original/, atualizado/, titulos.json) e acrescenta a linha do index.html.

    python3 edicoes/cronica-d-pedro-i/publicar.py

Uma página por parte: o prólogo e os 44 capítulos, com o título de 1816 no lado do original. Os dois
lados têm os mesmos parágrafos (os da edição de 1895). Os botões são «Original (1816)» e «Grafia atual».
"""
import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
SAIDA = os.path.join(RAIZ, 'conteudo', 'fernao-lopes', 'cronica-de-d-pedro-i.js')
ROMANOS = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']


def romano(n):
    d, u = divmod(n, 10)
    dez = ['', 'X', 'XX', 'XXX', 'XL']
    return dez[d] + ROMANOS[u]


APRESENTACAO = open(os.path.join(AQUI, 'sobre.md'), encoding='utf-8').read().strip()

FONTES = [
    {'nome': 'Collecção de livros ineditos de historia portugueza, t. IV (Lisboa, Academia Real das Sciencias, 1816), exemplar da Universidade de Toronto no Internet Archive',
     'url': 'https://archive.org/details/collecadeliv04corruoft', 'nota': 'texto-base, pp. 3–116; imagens conferidas'},
    {'nome': 'O mesmo tomo, outros dois exemplares no Internet Archive',
     'url': 'https://archive.org/details/collecadelivrosi04acad', 'nota': 'segunda e terceira leituras (também archive.org/details/collecadeliv03corr)'},
    {'nome': 'O mesmo tomo, 2.ª edição (Lisboa, Imprensa Nacional, 1925)',
     'url': 'https://archive.org/details/gri_33125011168180', 'nota': 'quarta leitura'},
    {'nome': 'Chronica de el-rei D. Pedro I, Bibliotheca de Classicos Portuguezes (Lisboa, 1895), Project Gutenberg n.º 16633',
     'url': 'https://www.gutenberg.org/ebooks/16633', 'nota': 'leitura de apoio e parágrafos'},
]


def js_texto(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def main():
    tit = json.load(open(os.path.join(AQUI, 'titulos.json'), encoding='utf-8'))
    partes = []
    for t in tit:
        nn = f'{t["n"]:02d}'
        texto = open(os.path.join(AQUI, 'atualizado', f'parte-{nn}.txt'), encoding='utf-8').read().strip()
        orig = open(os.path.join(AQUI, 'original', f'parte-{nn}.txt'), encoding='utf-8').read().strip()
        if len(texto.split('\n\n')) != len(orig.split('\n\n')):
            raise SystemExit(f'parte {nn}: parágrafos diferentes nos dois lados')
        if t['n'] == 0:
            partes.append({'n': '', 'titulo': 'Prólogo', 'tituloOriginal': 'Prologo', 'texto': texto, 'original': orig})
        else:
            partes.append({'n': 'Capítulo ' + romano(t['n']), 'titulo': t['titulo'], 'tituloOriginal': t['original'],
                           'texto': texto, 'original': orig})
    meta = {
        'id': 'cronica-de-d-pedro-i', 'autor': 'fernao-lopes', 'titulo': 'Crônica de D. Pedro I',
        'ano': 1434, 'datas': 'c. 1434', 'genero': 'História',
        'divisao': {'singular': 'capítulo', 'plural': 'capítulos', 'rotulo': 'n'},
        'rotulos': {'orig': 'Original (1816)', 'trad': 'Grafia atual'},
        'descricao': 'A crônica do reinado de D. Pedro I de Portugal (1357–1367), o rei justiceiro de Inês de Castro, '
                     'escrita por Fernão Lopes, guarda-mor da Torre do Tombo e primeiro cronista-mor do reino.',
    }
    edicao = {'base': '1816', 'apresentacao': APRESENTACAO, 'fontes': FONTES}
    linhas = ['/* Crônica de D. Pedro I — Fernão Lopes',
              '   Gerado por edicoes/cronica-d-pedro-i/publicar.py a partir de edicoes/cronica-d-pedro-i/{original,atualizado}/.',
              '   Não edite à mão. */',
              'BIBLIOTECA.obra({']
    for k, v in meta.items():
        linhas.append(f'  {k}: {json.dumps(v, ensure_ascii=False)},')
    linhas.append('  edicao: ' + json.dumps(edicao, ensure_ascii=False, indent=2).replace('\n', '\n  ') + ',')
    linhas.append('  partes: [')
    for i, p in enumerate(partes):
        fim = ',' if i + 1 < len(partes) else ''
        linhas.append(f'    {{ n: {json.dumps(p["n"])}, titulo: {json.dumps(p["titulo"], ensure_ascii=False)}, '
                      f'tituloOriginal: {json.dumps(p["tituloOriginal"], ensure_ascii=False)},\n'
                      f'      texto: `{js_texto(p["texto"])}`,\n      original: `{js_texto(p["original"])}` }}{fim}')
    linhas.append('  ]')
    linhas.append('});')
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    open(SAIDA, 'w', encoding='utf-8', newline='\n').write('\n'.join(linhas) + '\n')
    pal = sum(len(re.findall(r'\w+', p['texto'])) for p in partes)
    print('gravado', os.path.relpath(SAIDA, RAIZ), pal, 'palavras,', len(partes), 'partes')
    idx = os.path.join(RAIZ, 'index.html')
    h = open(idx, encoding='utf-8').read()
    linha = '<script defer src="conteudo/fernao-lopes/cronica-de-d-pedro-i.js"></script>'
    if linha not in h:
        ultimo = [m for m in re.finditer(r'<script defer src="conteudo/[^"]+"></script>\n', h)][-1]
        h = h[:ultimo.end()] + linha + '\n' + h[ultimo.end():]
        open(idx, 'w', encoding='utf-8', newline='\n').write(h)


if __name__ == '__main__':
    main()
