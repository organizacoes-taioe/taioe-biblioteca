"""Limpa a saída de knoll.py e grava edicoes/confissoes/original-knoll/livro-NN.txt.
uso: python3 -I knoll_final.py <saida-knoll> <destino>"""
import sys, os, re, unicodedata
ORIG, DEST = sys.argv[1:3]
os.makedirs(DEST, exist_ok=True)
ROM = str.maketrans({'ţ': 't', 'ş': 's', 'î': 'i', 'â': 'a', 'ă': 'a', 'Ţ': 'T', 'Ş': 'S', 'Î': 'I', 'Â': 'A', 'Ă': 'A'})
def limpa(w):
    if re.fullmatch(r'\[[IVXLC]+\.\d+\]', w): return w
    w = w.translate(ROM)
    w = re.sub(r'(?<=[A-Za-z])\d+(?=[A-Za-z])', '', w)      # número de linha grudado no meio da palavra
    w = re.sub(r'(?<=[A-Za-z.,;:?!])\d+(?=[.,;:?!]*$)', '', w)   # ... ou no fim
    w = re.sub(r'^Y(?=[a-z])', 'V', w)                       # o V maiúsculo de Knöll, lido como Y
    w = w.replace('*', '').replace('^', '').replace('|', '')
    w = re.sub(r'"$|"(?=[.,;:?!])', '“', w); w = re.sub(r'^"', '„', w)
    w = ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn')
    if not re.match(r'^[A-Z]', w): w = w.replace('v', 'u').replace('j', 'i')
    else: w = w[0] + w[1:].replace('v', 'u').replace('j', 'i')
    return w
total = 0
for k in range(1, 14):
    arq = f'livro-{k:02d}.txt'
    linhas = open(os.path.join(ORIG, arq), encoding='utf-8').read().split('\n')
    cab = [l for l in linhas if l.startswith('# ')]
    corpo = [l for l in linhas if not l.startswith('# ')]
    titulo = [l for l in cab if l.startswith('# titulo:')]
    novo = titulo + [
        '# fonte: Knöll, Sancti Aureli Augustini Confessionum libri tredecim, CSEL 33 (Viena, 1896), fac-símiles do Internet Archive (corpusscriptoru11wiengoog, corpusscriptorum0033unse, sanctiaureliaugu33augu)',
        '# edicao: o texto de Knöll, transcrito por nós: os três OCRs votados palavra a palavra, alinhados ao texto de trabalho (original/), que dá a divisão; as divergências conferidas nas imagens (2026-10-26)',
        '# nota: grafia de Knöll (u por v, inmutabilis, adparens, contemtus…); as marcas «[cap.seç]» são as de original/; os números de capítulo de Knöll e o aparato crítico ficam de fora']
    saida = []
    for l in corpo:
        ws = [limpa(w) for w in l.split()]
        ws = [w for w in ws if (w and re.search(r'[A-Za-z\[]', w) and not re.fullmatch(r'[IVXL]{2,}\.|[VXL]\.', w)) or w in ('—', '†')]
        saida.append(' '.join(ws)); total += len(ws)
    txt = '\n'.join(novo) + '\n' + '\n'.join(saida).strip('\n').join(['\n', '\n'])
    open(os.path.join(DEST, arq), 'w', encoding='utf-8').write(re.sub(r'\n{3,}', '\n\n', txt))
print('palavras', total)
