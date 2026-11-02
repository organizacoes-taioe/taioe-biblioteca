"""Mensagem (1934), de Fernando Pessoa: monta conteudo/fernando-pessoa/mensagem.js.

    python3 edicoes/mensagem/montar.py

Base: texto.json (os 44 poemas na grafia brasileira de hoje, conferidos palavra por palavra com a
transcrição validada da 1ª edição no Wikisource e, nos pontos de dúvida, com as imagens do fac-símile).
"""
import json, os
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
d = json.load(open(os.path.join(AQUI, 'texto.json'), encoding='utf-8'))
partes = []
for k, p in enumerate(d['poemas'], 1):
    cab = [f'_{x}_' for x in p.get('cabecalho', [])]
    estrofes = ['\n'.join('| ' + v for v in e.split('\n')) for e in p['texto'].split('\n\n')]
    fim = [f'_{p["fecho"]}_'] if p.get('fecho') else []
    partes.append({'n': '', 'titulo': p['titulo'], 'texto': '\n\n'.join(cab + estrofes + fim)})
obra = {
    'id': 'mensagem', 'autor': 'fernando-pessoa', 'titulo': 'Mensagem', 'ano': 1934, 'genero': 'Poesia',
    'divisao': {'singular': 'poema', 'plural': 'poemas'},
    'descricao': d['descricao'], 'edicao': d['edicao'], 'partes': partes,
}
js = ('/* Mensagem — Fernando Pessoa\n   Gerado por edicoes/mensagem/montar.py. Não edite à mão:\n'
      '   corrija edicoes/mensagem/texto.json e rode de novo.\n*/\nBIBLIOTECA.obra(' +
      json.dumps(obra, ensure_ascii=False, indent=1) + ');\n')
open(os.path.join(RAIZ, 'conteudo', 'fernando-pessoa', 'mensagem.js'), 'w', encoding='utf-8').write(js)
print(len(partes), 'poemas,', sum(p['texto'].count('| ') for p in partes), 'versos')
