"""Monta original/capitulo-N.txt de *St. Francis of Assisi* (Chesterton, 1923).

Base: a 1ª edição (Londres, Hodder & Stoughton, 1923), na transcrição do Project Gutenberg nº 63084,
conferida palavra por palavra com as três leituras OCR de três exemplares de 1923 no Internet Archive
(ver original/LEIAME.md). Onde o Gutenberg se afasta da impressão, fica a impressão (EMENDAS).

Uso: python3 edicoes/sao-francisco-de-assis/montar.py [caminho do pg63084.txt]
     (padrão: ferramentas/cache/sao-francisco-de-assis/pg63084.txt)
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))

# (capítulo, texto do Gutenberg, texto da edição de 1923): cada um tem de ocorrer uma vez só no capítulo.
EMENDAS = [
    (1, 'the hearth and the firefight and', 'the hearth and the firelight and'),
    (2, 'spirit of antiquity: the republic', 'spirit of antiquity; the republic'),
    (3, 'racing across the market place like', 'racing across the market-place like'),
    (5, 'his city upside down has', 'his city upside-down has'),
    (9, 'of the fingering of a shadow', 'of the lingering of a shadow'),
]

def capitulos(caminho):
    s = open(caminho, encoding='utf-8').read().replace('\r', '')
    corpo = s[s.index(' _Chapter I_'):]
    corpo = corpo[:corpo.find('HODDER AND STOUGHTON')]
    partes = re.split(r'\n _Chapter ([IVX]+)_\n _([^\n]+)_\n', '\n' + corpo)
    caps = []
    for k in range(1, len(partes), 3):
        rom, tit, txt = partes[k], partes[k + 1], partes[k + 2]
        pars = []
        for bloco in re.split(r'\n\s*\n', txt):
            if not bloco.strip():
                continue
            linhas = bloco.split('\n')
            if all(l.startswith('  ') for l in linhas if l.strip()):   # versos citados (Belloc, cap. III)
                pars.append('\n'.join('| ' + l.strip() for l in linhas if l.strip()))
            else:
                pars.append(re.sub(r'\s+', ' ', bloco).strip())
        caps.append((rom, tit, pars))
    return caps

def main():
    fonte = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, 'ferramentas/cache/sao-francisco-de-assis/pg63084.txt')
    caps = capitulos(fonte)
    assert len(caps) == 10
    for n, (rom, tit, pars) in enumerate(caps, 1):
        texto = '\n\n'.join(pars)
        for c, a, b in EMENDAS:
            if c == n:
                assert texto.count(a) == 1, (n, a)
                texto = texto.replace(a, b)
        cab = (f'# titulo: St. Francis of Assisi — Chapter {rom}: {tit}\n'
               '# fonte: Project Gutenberg, eBook nº 63084, conferido com três exemplares da 1ª edição no Internet Archive\n'
               '# edicao: G. K. Chesterton, St. Francis of Assisi (London, Hodder and Stoughton, 1923)\n\n')
        open(os.path.join(AQUI, 'original', f'capitulo-{n}.txt'), 'w', encoding='utf-8').write(cab + texto + '\n')
        print(n, tit, len(pars), 'parágrafos', len(texto.split()), 'palavras')

main()
