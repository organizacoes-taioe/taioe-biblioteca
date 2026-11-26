"""Ode Marítima (Álvaro de Campos / Fernando Pessoa): monta conteudo/fernando-pessoa/ode-maritima.js.

    python3 edicoes/ode-maritima/montar.py        (na raiz do repositório)

Fonte: texto/ode.txt, o poema inteiro na grafia de hoje (gerado por modernizar.py a partir de
texto/orpheu-1915.txt, a transcrição do Orpheu 2, e com as correções à mão que o modernizar.py lista).
Uma linha = um verso; linha em branco = estrofe nova. Cada décimo verso leva a marca {v N} (número do verso à
margem). Uma página só (`documento`). Ver FALTA.md e edicao.json.
"""
import json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
estrofes, n = [], 0
for bloco in re.split(r'\n\s*\n', open(os.path.join(AQUI, 'texto', 'ode.txt'), encoding='utf-8').read().strip()):
    vs = []
    for l in bloco.split('\n'):
        n += 1
        vs.append('| ' + ('{v %d} ' % n if n % 10 == 0 else '') + l.strip())
    estrofes.append('\n'.join(vs))
texto = '\n\n'.join(estrofes)
pal = len(re.findall(r"[A-Za-zÀ-ÿ]+", re.sub(r'\{v \d+\}', '', texto)))
obra = {'id': 'ode-maritima', 'autor': 'fernando-pessoa', 'titulo': 'Ode Marítima', 'ano': 1915,
        'genero': 'Poesia', 'divisao': {'singular': 'parte', 'plural': 'partes'},
        'descricao': 'A grande ode de Álvaro de Campos, heterônimo de Fernando Pessoa: um cais, um paquete que entra, e o poeta dividido entre o porto e todos os mares. Saiu em 1915, no segundo número da revista _Orpheu_, dedicada a Santa-Rita Pintor.',
        '_palavras': pal, 'partes': [{'n': '', 'titulo': '', 'texto': texto}],
        'edicao': json.load(open(os.path.join(AQUI, 'edicao.json'), encoding='utf-8'))}
js = ('/* Ode Marítima — Álvaro de Campos (Fernando Pessoa). Gerado por edicoes/ode-maritima/montar.py;\n'
      '   não edite à mão: corrija edicoes/ode-maritima/texto/ e rode de novo. */\n'
      'BIBLIOTECA.obra(' + json.dumps(obra, ensure_ascii=False, indent=1) + ');\n')
open(os.path.join(RAIZ, 'conteudo', 'fernando-pessoa', 'ode-maritima.js'), 'w', encoding='utf-8').write(js)
print(n, 'versos,', len(estrofes), 'estrofes,', pal, 'palavras')
