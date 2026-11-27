"""Farsa de Inês Pereira: passo 2 do texto. Aplica as lições da Copilação de 1562 (licoes.py) sobre o
texto de 1834 já na grafia de hoje (colacao/moderno-1834.txt, de modernizar.py) e grava texto.txt, no
formato do site (fala «@ Nome», verso «| », rubrica em _itálico_), que publicar.py leva ao site.

uso: python3 edicoes/farsa-de-ines-pereira/modernizar.py && python3 edicoes/farsa-de-ines-pereira/montar.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from licoes import ARGUMENTO, EMENDAS, LICOES  # noqa: E402


def main():
    t = open(os.path.join(AQUI, 'colacao', 'moderno-1834.txt'), encoding='utf-8').read()
    # o argumento e a rubrica de abertura, como estão em 1562
    ini = t.index('\n\n@ Inês\n')
    t = ARGUMENTO + t[ini:]
    erros = 0
    for antes, depois in LICOES:
        n = t.count(antes)
        if n != 1:
            print(f'achado {n} vezes: {antes!r}')
            erros += 1
            continue
        t = t.replace(antes, depois)
    for trecho, _ in EMENDAS:
        if t.count(trecho) != 1:
            print('emenda não achada:', repr(trecho))
            erros += 1
    if erros:
        sys.exit(1)
    open(os.path.join(AQUI, 'texto.txt'), 'w', encoding='utf-8').write(t)
    versos = sum(1 for l in t.split('\n') if l.startswith('| '))
    print('texto.txt:', versos, 'linhas de verso,', len(LICOES), 'lições de 1562 aplicadas')


if __name__ == '__main__':
    main()
