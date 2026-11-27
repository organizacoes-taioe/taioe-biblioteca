"""Vida de D. Frei Bertolameu dos Mártires — grava conteudo/frei-luis-de-sousa/vida-de-frei-bartolomeu.js a partir
de atual/ (texto na grafia de hoje, um arquivo por capítulo; ver modernizar.py) e de sobre.py.

  python3 -I edicoes/vida-de-frei-bartolomeu/publicar.py

Partes: a dedicatória e os seis livros, como em 1619. Em cada livro, «## Capítulo N — título» e a marca
«{§ I.N}» no primeiro parágrafo, que o gerador usa para dar uma página a cada capítulo (divisao.marcas = false
a esconde), como na Vida de Anchieta. As citações à margem de 1619 vão no fim do capítulo, como notas do autor.
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, AQUI)
import sobre  # noqa: E402

SAIDA = os.path.join(RAIZ, 'conteudo', 'frei-luis-de-sousa', 'vida-de-frei-bartolomeu.js')
ROM = ['I', 'II', 'III', 'IV', 'V', 'VI']
NOMES = ['Livro primeiro', 'Livro segundo', 'Livro terceiro', 'Livro quarto', 'Livro quinto', 'Livro sexto']


def js_texto(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def ler(nome):
    return open(os.path.join(AQUI, 'atual', nome), encoding='utf-8').read().strip()


def main():
    partes = [{'n': 'Dedicatória', 'titulo': 'Dedicatória', 'texto': ler('dedicatoria.txt')}]
    for b in range(1, 7):
        corpo = []
        caps = sorted(f for f in os.listdir(os.path.join(AQUI, 'atual')) if re.match(rf'l{b}-c\d+\.txt$', f))
        for f in caps:
            c = int(re.search(r'c(\d+)', f).group(1))
            bl = ler(f).split('\n\n')
            assert bl[0].startswith('## '), f
            corpo.append(f'## Capítulo {c} — {bl[0][3:].strip()}')
            pars = bl[1:]
            k = next(i for i, p in enumerate(pars) if not p.startswith('¤ '))
            pars[k] = f'{{§ {ROM[b - 1]}.{c}}} ' + pars[k]
            corpo += pars
        partes.append({'n': ROM[b - 1], 'titulo': NOMES[b - 1], 'texto': '\n\n'.join(corpo)})
    meta = {
        'id': 'vida-de-frei-bartolomeu', 'autor': 'frei-luis-de-sousa',
        'titulo': 'Vida de D. Frei Bartolomeu dos Mártires', 'ano': 1619, 'genero': 'Hagiografia',
        'divisao': {'singular': 'livro', 'plural': 'livros', 'rotulo': 'nome', 'marcas': False},
        'descricao': sobre.DESCRICAO,
    }
    edicao = sobre.edicao()
    linhas = ['/* Vida de D. Frei Bartolomeu dos Mártires — Frei Luís de Sousa (1619)',
              '   Gerado por edicoes/vida-de-frei-bartolomeu/publicar.py a partir de edicoes/vida-de-frei-bartolomeu/atual/.',
              '   Não edite à mão: corrija as fontes e rode de novo. */',
              'BIBLIOTECA.obra({']
    for chave, v in meta.items():
        linhas.append(f'  {chave}: {json.dumps(v, ensure_ascii=False)},')
    linhas.append('  edicao: ' + json.dumps(edicao, ensure_ascii=False, indent=2).replace('\n', '\n  ') + ',')
    linhas.append('  partes: [')
    for i, b in enumerate(partes):
        fim = ',' if i + 1 < len(partes) else ''
        linhas.append(f'    {{ n: {json.dumps(b["n"], ensure_ascii=False)}, titulo: {json.dumps(b["titulo"], ensure_ascii=False)}, '
                      f'texto: `{js_texto(b["texto"])}` }}{fim}')
    linhas.append('  ]')
    linhas.append('});')
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    open(SAIDA, 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
    print('gravado', os.path.relpath(SAIDA, RAIZ), sum(len(re.findall(r'\w+', b['texto'])) for b in partes), 'palavras')
    idx = os.path.join(RAIZ, 'index.html')
    h = open(idx, encoding='utf-8').read()
    linha = '<script defer src="conteudo/frei-luis-de-sousa/vida-de-frei-bartolomeu.js"></script>'
    if linha not in h:
        h = h.replace('</head>', linha + '\n</head>', 1)
        open(idx, 'w', encoding='utf-8').write(h)


if __name__ == '__main__':
    main()
