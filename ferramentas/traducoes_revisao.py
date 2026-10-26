"""As decisões delicadas das traduções nossas (Catolicismo) para o Gere, em /admin/pendencias/
(tipo «Biblioteca: traduções»; pedido dele, 26/10/2026). Não vale para a Não-ficção comentada, que
tem a sua revisão no comentadas.py.

    python3 ferramentas/traducoes_revisao.py                  → só confere
    python3 ferramentas/traducoes_revisao.py --revisao <pasta> → grava <pasta>/traducoes.json
                                                                (../infra/dados/paginas; depois
                                                                gerar.py e Catálogo, como a Bíblia)

Fonte: edicoes/<pasta>/revisao*.json, um arquivo por obra publicada:
    {"id", "rotulo", "url", "escolhas": [{"id", "titulo", "ref", "contexto",
                                          "opcoes": [{"id", "texto", "nota", "recomendada"}]}]}
Uma decisão por escolha (só perguntas pontuais; nada de divisão do texto nem de registro geral).
Escolha respondida e aplicada sai do arquivo e vai para o CONVENCOES.md da obra; arquivo sem
escolhas pode ficar (a obra não aparece na página).
"""
import json
import pathlib
import re
import sys
from datetime import date

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ID = re.compile(r'^[a-z0-9][a-z0-9:._-]{0,119}$')


def carregar():
    caps, erros = [], []
    for arq in sorted((RAIZ / 'edicoes').glob('*/revisao*.json')):
        nome = arq.relative_to(RAIZ)
        r = json.loads(arq.read_text(encoding='utf-8'))
        for chave in ('divisao', 'registro'):
            if chave in r:
                erros.append(f'{nome}: «{chave}» não vai ao Gere (só escolhas pontuais)')
        vistos = set()
        for e in r.get('escolhas', []):
            onde = f'{nome}: {e.get("id")}'
            if e['id'] in vistos:
                erros.append(f'{onde}: id repetido')
            vistos.add(e['id'])
            if not e.get('titulo', '').rstrip('» ').endswith('?'):
                erros.append(f'{onde}: o título tem de ser uma pergunta')
            ops = e.get('opcoes', [])
            if not 2 <= len(ops) <= 4:
                erros.append(f'{onde}: {len(ops)} opções (de 2 a 4)')
            if sum(1 for o in ops if o.get('recomendada')) != 1:
                erros.append(f'{onde}: precisa de exatamente uma opção recomendada')
            if len({o['id'] for o in ops}) != len(ops):
                erros.append(f'{onde}: opções com id repetido')
        if not r.get('escolhas'):
            continue
        itens = [dict(e, id=f'{r["id"]}:escolha:{e["id"]}', tipo='escolha') for e in r['escolhas']]
        for it in itens:
            if not ID.match(it['id']):
                erros.append(f'{nome}: id inválido para o banco: {it["id"]}')
        caps.append({'id': r['id'], 'rotulo': r['rotulo'], 'url': r['url'], 'rotuloUrl': 'Abrir o livro',
                     'secoes': [{'id': 'escolhas', 'titulo': 'Escolhas de tradução', 'itens': itens}]})
    return caps, erros


def main():
    caps, erros = carregar()
    if erros:
        sys.exit('\n'.join(erros))
    hoje = date.today().strftime('%d/%m/%Y')
    for c in caps:
        n = len(c['secoes'][0]['itens'])
        c['estado'] = f'no ar; {n} {"decisão" if n == 1 else "decisões"}, atualizado em {hoje}'
    total = sum(len(c['secoes'][0]['itens']) for c in caps)
    if '--revisao' not in sys.argv:
        print(f'ok: {total} escolhas em {len(caps)} obras')
        return
    destino = pathlib.Path(sys.argv[sys.argv.index('--revisao') + 1]) / 'traducoes.json'
    pag = {'slug': 'traducoes', 'titulo': 'Biblioteca: traduções', 'capitulos': caps}
    destino.write_text(json.dumps(pag, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
    print(f'{destino}: {total} itens em {len(caps)} obras')


if __name__ == '__main__':
    main()
