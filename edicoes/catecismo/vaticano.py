"""Grava edicoes/catecismo/vaticano.json: para cada um dos 2865 pontos, o endereço da página do
vatican.va onde ele está por extenso, com um fragmento de texto (#:~:text=) que leva o navegador
direto ao começo do ponto.

    python edicoes/catecismo/vaticano.py

Roda uma vez (e de novo só se o Vaticano mudar as páginas); o gerador do site só lê o JSON.

- As páginas vêm do índice (indice_po.html); o nome de cada uma traz a faixa de pontos
  (p1s1c1_26-49_po.html). Nada de lista fixa aqui.
- As páginas não têm âncora por ponto; cada ponto começa num parágrafo «27. O desejo de Deus…».
  O fragmento é «N.» com as primeiras palavras do ponto COMO ESTÃO NA PÁGINA DO VATICANO (o
  texto da Biblioteca foi adaptado ao português do Brasil), alongado até que a primeira
  ocorrência na página seja o começo do ponto. Codificado por inteiro (também «-», «,», «&»).
- Navegador sem suporte a fragmento de texto abre a página no alto, o que serve.
"""
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, 'vaticano.json')
BASE = 'https://www.vatican.va/archive/cathechism_po/index_new/'
INDICE = BASE + 'indice_po.html'
TOTAL = 2865
MIN_PALAVRAS, MAX_PALAVRAS = 4, 30
# Erros de numeração nas páginas do Vaticano (outubro de 2026): o ponto 2217 está impresso
# como «2117.» e o 2439 como «1439.». O fragmento usa o número como está na página.
NUMERO_NA_PAGINA = {2217: 2117, 2439: 1439}


def baixar(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Biblioteca Taioe)'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode('windows-1252')


def paginas():
    """[(href como está no índice, de, até)], na ordem dos pontos."""
    vistos, lista = set(), []
    for m in re.finditer(r'href="\s*([^"#]+?_po\.html)\s*(?:#[^"]*)?"', baixar(INDICE)):
        href = m.group(1).strip()
        faixa = re.search(r'(\d+)-(\d+)_po\.html$', urllib.parse.unquote(href))
        if not faixa or href in vistos:
            continue
        vistos.add(href)
        lista.append((href, int(faixa.group(1)), int(faixa.group(2))))
    return sorted(lista, key=lambda x: x[1])


BLOCO = re.compile(r'<(?:p|/p|br|hr|blockquote|/blockquote|td|/td|tr|div|/div|h\d|/h\d|li|/li|table|/table)\b[^>]*>', re.I)
NEGRITO = '\x02'                      # marca provisória do <b>, que some do texto


def texto_da_pagina(fonte):
    """Os blocos de texto da página, como o navegador os mostra (espaços juntados), cada um com
    a indicação de começar em negrito (o número do ponto vem em negrito; o das notas, não)."""
    corpo = re.sub(r'(?is)<(script|style)\b.*?</\1>', ' ', fonte)
    corpo = re.sub(r'(?i)<b\b[^>]*>', NEGRITO, corpo)
    blocos = []
    for b in BLOCO.split(corpo):
        t = html.unescape(re.sub(r'<[^>]+>', '', b))
        t = re.sub(r'[ \t\r\n\f]+', ' ', t).strip()
        negrito = t.startswith(NEGRITO)
        t = re.sub(r'[ \t\r\n\f]+', ' ', t.replace(NEGRITO, '')).strip()
        if t:
            blocos.append((t, negrito))
    return blocos


def normal(t):
    """Para comparar como o navegador: sem diferença de maiúsculas nem de espaços (o nbsp conta como espaço)."""
    return re.sub(r'\s+', ' ', t.replace('\xa0', ' ')).lower()


def codificar(t):
    return urllib.parse.quote(t, safe='').replace('-', '%2D')


def fragmentos(href, de, ate):
    """{ponto: url} da página; e a lista de problemas."""
    url = BASE + href
    marcados = texto_da_pagina(baixar(url))
    blocos = [t for t, _ in marcados]
    corrido = normal(' \n '.join(blocos))
    # posição de cada bloco no texto corrido
    pos, p = [], 0
    for b in blocos:
        k = corrido.index(normal(b), p)
        pos.append(k)
        p = k + len(normal(b))
    saida, problemas, i = {}, [], 0
    for n in range(de, ate + 1):
        # «27. O desejo…», «179.  A fé…», «2553 Inveja…» (sem ponto), sempre em negrito
        cabeca = re.compile(r'^(%d(?:\s?\.)?)[\s\xa0]+(\S.*)$' % NUMERO_NA_PAGINA.get(n, n))
        antes = i
        while i < len(blocos) and not (marcados[i][1] and cabeca.match(blocos[i])):
            i += 1
        if i == len(blocos):
            problemas.append(f'{n}: começo não achado em {href}')
            saida[n] = url
            i = antes
            continue
        # O fragmento é o começo do bloco tal como o navegador o mostra, com os espaços duros
        # (&nbsp;) onde a página os tem: «179.&nbsp; A fé» não casa com «179. A fé».
        bruto = blocos[i]
        fins = [x.end() for x in re.finditer(r'[^ \xa0]+', bruto)]
        npal = len(fins) - len(cabeca.match(bruto).group(1).split())
        achou = None
        for k in range(1, min(MAX_PALAVRAS, npal) + 1):
            if k < MIN_PALAVRAS and k < npal:
                continue
            frag = bruto[:fins[len(fins) - npal + k - 1]]
            # o navegador procura a partir do começo da página e para na primeira ocorrência
            # que comece e acabe em fronteira de palavra
            for x in re.finditer(r'(?<![\w])' + re.escape(normal(frag)) + r'(?![\w])', corrido):
                if x.start() == pos[i]:
                    achou = frag
                break
            if achou:
                break
        if not achou:
            problemas.append(f'{n}: fragmento não ficou único em {href}')
            saida[n] = url
        else:
            saida[n] = url + '#:~:text=' + codificar(achou)
        i += 1
    return saida, problemas


def main():
    lista = paginas()
    tudo, problemas = {}, []
    esperado = 1
    for href, de, ate in lista:
        if de != esperado:
            problemas.append(f'faixa fora de ordem: {href} começa em {de}, esperava {esperado}')
        esperado = ate + 1
        s, pr = fragmentos(href, de, ate)
        tudo.update(s)
        problemas += pr
        print(f'{urllib.parse.unquote(href)}: {de}–{ate}' + (f' ({len(pr)} problema(s))' if pr else ''))
    faltam = [n for n in range(1, TOTAL + 1) if n not in tudo]
    if faltam:
        problemas.append(f'{len(faltam)} pontos sem página: {faltam[:10]}…')
    for p in problemas:
        print('  ' + p)
    with open(SAIDA, 'w', encoding='utf-8', newline='\n') as f:
        f.write('{\n' + ',\n'.join(f'"{n}": {json.dumps(tudo[n])}' for n in sorted(tudo)) + '\n}\n')
    print(f'{len(lista)} páginas, {len(tudo)} pontos, {len(problemas)} problema(s); gravado {os.path.relpath(SAIDA)}')
    return 1 if problemas else 0


if __name__ == '__main__':
    sys.exit(main())
