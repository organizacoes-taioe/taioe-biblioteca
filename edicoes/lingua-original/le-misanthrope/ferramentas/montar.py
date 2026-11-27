"""cenas.json (Louandre 1910, fr.wikisource; extrair.py) → os arquivos das partes do Misanthrope, no formato da
língua original, na divisão de 1667 (22 cenas; a de Louandre, que é a de 1734, tem 28).
python3 -I montar.py cenas.json <pasta de saída (partes/)>

- A cena traz no alto «::versos N» (os versos antes dela: a numeração corre pela peça inteira, 1–1808, como em
  Despois–Mesnard) e «::rubrica» com quem está em cena, pela lista de 1667 (Despois–Mesnard; onde o OCR
  dela falha, a de van Bever, 1923, que segue as edições originais).
- As cenas que 1734 abre só porque alguém sai (III, 5 e 7; V, 5 a 8) voltam a ser uma só, como em 1667.
- As cartas lidas em voz alta (V, 4) são prosa: «::prosa», sem número; as falas curtas que as interrompem não
  entram na numeração (como nas edições), e vão também como «::prosa».
- Texto e correções: o que `colacao.py` decidiu está em CORRECOES (verso → (texto de Louandre, texto certo))."""
import json, os, re, sys

c = json.load(open(sys.argv[1], encoding='utf-8'))
saida = sys.argv[2]
ROM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
# (ato, cena de 1667) → índices das cenas de Louandre (0 = I, 1) e quem está em cena (1667)
DIVISAO = [
    (1, 1, [0], 'Philinte, Alceste.'),
    (1, 2, [1], 'Oronte, Alceste, Philinte.'),
    (1, 3, [2], 'Philinte, Alceste.'),
    (2, 1, [3], 'Alceste, Célimène.'),
    (2, 2, [4], 'Célimène, Alceste, Basque.'),
    (2, 3, [5], 'Basque, Alceste, Célimène.'),
    (2, 4, [6], 'Éliante, Philinte, Acaste, Clitandre, Alceste, Célimène, Basque.'),
    (2, 5, [7], 'Basque, Alceste, Célimène, Éliante, Acaste, Philinte, Clitandre.'),
    (2, 6, [8], 'Garde, Alceste, Célimène, Éliante, Acaste, Philinte, Clitandre.'),
    (3, 1, [9], 'Clitandre, Acaste.'),
    (3, 2, [10], 'Célimène, Acaste, Clitandre.'),
    (3, 3, [11], 'Célimène, Acaste, Clitandre, Basque.'),
    (3, 4, [12, 13], 'Arsinoé, Célimène, Clitandre, Acaste.'),
    (3, 5, [14, 15], 'Alceste, Célimène, Arsinoé.'),
    (4, 1, [16], 'Éliante, Philinte.'),
    (4, 2, [17], 'Alceste, Éliante, Philinte.'),
    (4, 3, [18], 'Célimène, Alceste.'),
    (4, 4, [19], 'Du Bois, Célimène, Alceste.'),
    (5, 1, [20], 'Alceste, Philinte.'),
    (5, 2, [21], 'Célimène, Oronte, Alceste.'),
    (5, 3, [22], 'Éliante, Philinte, Célimène, Oronte, Alceste.'),
    (5, 4, [23, 24, 25, 26, 27], 'Acaste, Clitandre, Arsinoé, Philinte, Éliante, Oronte, Célimène, Alceste.'),
]
NOMES = {'Dubois': 'Du Bois'}
# as falas curtas que interrompem a leitura das cartas (V, 4): fora da numeração
FORA = ('Il devrait être ici.', 'C’est moi-même, messieurs, sans nulle vanité.', 'À vous le dé, monsieur.',
        'Voici votre paquet.', 'Me voici maintenant, moi.')
# nas cartas (prosa, V, 4): as lições de 1667 onde Louandre segue 1682
PROSA = [('je ne vous le pardonnerai', 'je ne vous la pardonnerai'),
         ('Et pour l’homme au sonnet…', 'Et pour l’homme à la veste…'),
         ('» Et pour l’homme au sonnet,', '» Et pour l’homme à la veste,')]
CORRECOES = {}
arq = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'correcoes.json')
if os.path.exists(arq):
    CORRECOES = {int(k): v for k, v in json.load(open(arq, encoding='utf-8')).items()}


def rubrica(s):
    s = s.strip()
    if s.startswith('(') and s.endswith(')'):
        s = s[1:-1].strip()
    s = s[:1].upper() + s[1:]
    if not s.endswith(('.', ':', '\xa0:')):
        s += '.'
    return s


def indicacao(s):
    s = s.strip().rstrip('.')
    return '[' + s[:1].lower() + s[1:] + ']' if s else ''


os.makedirs(saida, exist_ok=True)
partes = []
n = 0
usadas = set()
for ato, cena, idx, quem in DIVISAO:
    out = ['::versos %d' % n, '::rubrica ' + quem, '']
    ini = n
    ultimo_fala = None
    for k in idx:
        for x in c[k]['itens']:
            if x[0] == 'pers':
                continue
            if x[0] == 'rubrica':
                if out[-1] != '':
                    out.append('')
                out.append('::rubrica ' + rubrica(x[1]))
                out.append('')
                continue
            if x[0] == 'fala':
                if out[-1] != '':
                    out.append('')
                out.append('::fala ' + NOMES.get(x[1], x[1]))
                ultimo_fala = indicacao(x[2])
                continue
            _, t, rec, _num = x
            pre = ''
            if ultimo_fala:
                pre = ultimo_fala + ' '
                ultimo_fala = None
            if ato == 5 and cena == 4 and (t.startswith(('«', '»')) or t in FORA):
                for a, b in PROSA:
                    if a in t:
                        t = t.replace(a, b); usadas.add(a)
                out.append('::prosa ' + pre + t)
                continue
            if not rec:
                n += 1
                if n in CORRECOES:
                    a, b = CORRECOES[n]
                    if a not in t:
                        sys.exit('correção do verso %d não casa: %r em %r' % (n, a, t))
                    t = t.replace(a, b, 1)
                    usadas.add(n)
            out.append(' ' * max(4, rec) + pre + t if rec else pre + t)
    while out and out[-1] == '':
        out.pop()
    nome = '%d-%d.txt' % (ato, cena)
    with open(os.path.join(saida, nome), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    partes.append({'titulo': 'Ato %s, cena %d' % (['I', 'II', 'III', 'IV', 'V'][ato - 1], cena),
                   'arquivo': 'partes/' + nome, 'versos': [ini + 1, n]})
falta = (set(CORRECOES) | {a for a, _b in PROSA}) - usadas
if falta:
    sys.exit('correções sem verso: %s' % sorted(map(str, falta)))
json.dump(partes, open(os.path.join(saida, '..', 'partes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(partes), 'partes,', n, 'versos')
