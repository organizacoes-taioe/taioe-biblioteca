"""São Bernardo — OCR próprio (Tesseract) dos fac-símiles da Brasiliana, um segundo testemunho
independente do OCR que vem nos PDFs.

  python3 edicoes/sao-bernardo/tesseract.py bbm8421 bbm8398     (1947, a edição-base; 1934)

Cada página vira ferramentas/cache/sao-bernardo/tess-<pdf>/<n>.tsv (palavras com coordenadas, a
300 dpi, contadas a partir do recorte) e <n>.json (o recorte, em pixels). O recorte é a coluna de
texto que o OCR da Brasiliana acha (linhas com cinco palavras ou mais), com folga: nas páginas
pares, a lombada dos outros cadernos aparece à esquerda e o Tesseract a lê como letras.

O Tesseract é o do Ubuntu (tesseract-ocr, tesseract-ocr-por). Sem permissão de administrador, os
pacotes se extraem numa pasta (apt-get download + dpkg -x), e o caminho vai na variável
TESSERACT_RAIZ (padrão: ~/.cache/tesseract-local/raiz).
"""
import html
import json
import os
import re
import subprocess
import sys
from multiprocessing import Pool

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, '..', '..', 'ferramentas', 'cache', 'sao-bernardo')
DPI = 300


def _ambiente():
    raiz = os.environ.get('TESSERACT_RAIZ', os.path.expanduser('~/.cache/tesseract-local/raiz'))
    env = dict(os.environ, OMP_THREAD_LIMIT='1')
    exe = 'tesseract'
    if os.path.isdir(raiz):
        exe = os.path.join(raiz, 'usr', 'bin', 'tesseract')
        env['LD_LIBRARY_PATH'] = os.path.join(raiz, 'usr', 'lib', 'x86_64-linux-gnu')
        env['TESSDATA_PREFIX'] = os.path.join(raiz, 'usr', 'share', 'tesseract-ocr', '5', 'tessdata')
    return exe, env


def bbox(nome):
    """Camada de texto do PDF com coordenadas (pdftotext -bbox-layout), em cache."""
    xml = os.path.join(CACHE, nome + '-bbox.html')
    if not os.path.exists(xml):
        subprocess.run(['pdftotext', '-bbox-layout', '-enc', 'UTF-8', os.path.join(CACHE, nome + '.pdf'), xml], check=True)
    return open(xml, encoding='utf-8').read()


def recortes(nome):
    """Por página: (x0, x1) da coluna de texto em pontos, ou None se a página não tem texto."""
    boa = re.compile(r'^[A-Za-zÀ-ÿ]{2,}[,.;:!?]?$')
    out = {}
    for k, pag in enumerate(re.findall(r'<page [^>]*>(.*?)</page>', bbox(nome), re.S), 1):
        xs = []
        for l in re.finditer(r'<line xMin="([\d.]+)" yMin="[\d.]+" xMax="([\d.]+)"[^>]*>(.*?)</line>', pag, re.S):
            ws = [html.unescape(w) for w in re.findall(r'<word [^>]*>([^<]*)</word>', l.group(3))]
            if sum(bool(boa.match(w)) for w in ws) >= 5:
                xs.append((float(l.group(1)), float(l.group(2))))
        if len(xs) < 3:
            # OCR do PDF ilegível ou ausente (p. 114 de 1947): vale o recorte da página vizinha, se ela
            # tem texto; as páginas em branco o Tesseract devolve vazias
            out[k] = 'vizinha'
            continue
        x0 = sorted(a for a, _ in xs)[len(xs) // 10]          # sem a linha mais à esquerda (lixo)
        x1 = sorted(b for _, b in xs)[-1 - len(xs) // 10]
        out[k] = (x0 - 25, x1 + 25)
    for k, v in out.items():           # OCR ilegível: o recorte da página de mesma paridade mais perto
        if v == 'vizinha':
            out[k] = next((out[k + d] for d in (2, -2, 4, -4) if isinstance(out.get(k + d), tuple)), None)
    return out


def pagina(args):
    pdf, n, pasta, corte = args
    tsv = os.path.join(pasta, f'{n}.tsv')
    if os.path.exists(tsv) or corte is None:
        return n
    exe, env = _ambiente()
    x0, x1 = (max(0, round(v * DPI / 72)) for v in corte)
    png = os.path.join(pasta, f'{n}')
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', str(DPI), '-gray', '-png', '-singlefile',
                    '-x', str(x0), '-y', '0', '-W', str(x1 - x0), '-H', '100000', pdf, png], check=True)
    subprocess.run([exe, png + '.png', os.path.join(pasta, str(n)), '-l', 'por', '--psm', '4', 'tsv'],
                   check=True, env=env, capture_output=True)
    os.remove(png + '.png')
    json.dump({'x': x0, 'y': 0, 'dpi': DPI}, open(os.path.join(pasta, f'{n}.json'), 'w'))
    return n


def paginas(nome):
    pdf = os.path.join(CACHE, nome + '.pdf')
    cortes = recortes(nome)
    pasta = os.path.join(CACHE, 'tess-' + nome)
    os.makedirs(pasta, exist_ok=True)
    tarefas = [(pdf, n, pasta, c) for n, c in sorted(cortes.items())]
    with Pool(int(os.environ.get('PROCESSOS', '7'))) as p:
        for k, n in enumerate(p.imap_unordered(pagina, tarefas), 1):
            if k % 20 == 0:
                print(nome, k, '/', len(tarefas), flush=True)


if __name__ == '__main__':
    for nome in sys.argv[1:]:
        paginas(nome)
