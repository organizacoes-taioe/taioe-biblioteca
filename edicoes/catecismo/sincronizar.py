"""Copia de novo os dados do Catecismo da Igreja Católica para a Biblioteca.

O texto é preparado na pasta do Catecismo (Software MEU/catecismo): cada ponto em
dados/*.json e o manifesto (blocos, aberturas e subtítulos) calculado lá por estrutura.py.
Aqui fica uma cópia fiel dessa pasta dados/, que o gerador do site lê
(ferramentas/site/catecismo.mjs). Depois de acrescentar pontos no Catecismo:

    (na pasta do Catecismo)  python estrutura.py
    python edicoes/catecismo/sincronizar.py [pasta do Catecismo]
    node ferramentas/site/gerar.mjs
    node ferramentas/site/conferir.mjs

Sem argumento, a pasta do Catecismo é a vizinha da pasta taioe (../../../../catecismo a
partir deste arquivo). A cópia é um espelho: arquivo que saiu do manifesto sai daqui também.
Antes de copiar, confere o que o site precisa: todo ponto anunciado no manifesto existe, as
chamadas de nota do corpo batem com as notas do ponto, e as aberturas e os subtítulos caem
dentro dos pontos publicados. Também procura mesóclises (só avisa: o texto é do Catecismo).
"""
import json
import os
import re
import shutil
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(AQUI, 'dados')
PADRAO = os.path.normpath(os.path.join(AQUI, '..', '..', '..', '..', 'catecismo'))

REF = re.compile(r'<a class="ref" href="#nota-(\d+)" data-n="(\d+)">(\d+)</a>')
MESOCLISE = re.compile(r'[^\W\d_]+-(?:lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-'
                       r'(?:ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)(?![^\W\d_])')


def ler_json(arq):
    with open(arq, encoding='utf-8') as f:
        return json.load(f)


def conferir(origem):
    """Devolve (manifesto, arquivos, problemas, avisos)."""
    man = ler_json(os.path.join(origem, 'manifesto.json'))
    problemas, avisos, arquivos, pontos = [], [], ['manifesto.json'], set()
    for b in man['blocos']:
        arq = os.path.join(origem, b['file'])
        if not os.path.exists(arq):
            problemas.append(f"{b['file']}: anunciado no manifesto, mas não existe")
            continue
        arquivos.append(b['file'])
        d = ler_json(arq)
        for n in range(b['de'], b['ate'] + 1):
            p = d.get(str(n))
            if not p:
                problemas.append(f"ponto {n}: anunciado em {b['file']}, mas ausente")
                continue
            pontos.add(n)
            for campo in ('trail', 'body', 'notes'):
                if campo not in p:
                    problemas.append(f'ponto {n}: sem «{campo}»')
            refs = REF.findall(p.get('body', ''))
            if len(refs) != p.get('body', '').count('<a '):
                problemas.append(f'ponto {n}: link no corpo fora do formato <a class="ref" href="#nota-N" data-n="N">N</a>')
            if any(a != b2 or a != c for a, b2, c in refs):
                problemas.append(f'ponto {n}: chamada de nota com números desencontrados')
            notas = [x.get('n') for x in p.get('notes', [])]
            if [int(r[0]) for r in refs] != notas:
                problemas.append(f'ponto {n}: chamadas {[int(r[0]) for r in refs]} × notas {notas}')
            for x in p.get('notes', []):
                if not x.get('fonte'):
                    problemas.append(f"ponto {n}, nota {x.get('n')}: sem fonte")
            texto = json.dumps(p, ensure_ascii=False)
            if re.search(r'\sstyle=|\son[a-z]+=|<script', texto):
                problemas.append(f'ponto {n}: estilo ou script no HTML (a CSP do site bloqueia)')
            for m in MESOCLISE.finditer(texto):
                avisos.append(f'ponto {n}: mesóclise «{m.group(0)}»')
    if pontos and (min(pontos) != man['min'] or max(pontos) != man['max'] or len(pontos) != man['max'] - man['min'] + 1):
        problemas.append(f"manifesto diz {man['min']}–{man['max']}, mas os blocos trazem {len(pontos)} pontos")
    for chave in ('aberturas', 'subtitulos'):
        for k in man.get(chave, {}):
            if int(k) not in pontos:
                problemas.append(f'{chave}: {k} fora dos pontos publicados (rode estrutura.py no Catecismo)')
    return man, arquivos, problemas, avisos


def main():
    origem_raiz = sys.argv[1] if len(sys.argv) > 1 else PADRAO
    origem = os.path.join(origem_raiz, 'dados')
    if not os.path.exists(os.path.join(origem, 'manifesto.json')):
        sys.exit(f'não achei {origem}/manifesto.json; passe a pasta do Catecismo como argumento')
    man, arquivos, problemas, avisos = conferir(origem)
    for a in avisos:
        print('aviso:', a)
    if problemas:
        print(f'{len(problemas)} problema(s); nada foi copiado:')
        for p in problemas[:40]:
            print('  ' + p)
        sys.exit(1)
    os.makedirs(DESTINO, exist_ok=True)
    copiados = 0
    for a in arquivos:
        de, para = os.path.join(origem, a), os.path.join(DESTINO, a)
        with open(de, 'rb') as f:
            novo = f.read()
        if os.path.exists(para):
            with open(para, 'rb') as f:
                if f.read() == novo:
                    continue
        shutil.copyfile(de, para)
        copiados += 1
    removidos = [a for a in os.listdir(DESTINO) if a.endswith('.json') and a not in arquivos]
    for a in removidos:
        os.remove(os.path.join(DESTINO, a))
    print(f"pontos {man['min']}–{man['max']}, {len(man.get('aberturas', {}))} aberturas, "
          f"{len(man.get('subtitulos', {}))} subtítulos; {copiados} arquivo(s) copiado(s), {len(removidos)} removido(s).")
    print('Agora: node ferramentas/site/gerar.mjs && node ferramentas/site/conferir.mjs')


if __name__ == '__main__':
    main()
