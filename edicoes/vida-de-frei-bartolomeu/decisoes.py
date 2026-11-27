"""Vida de D. Frei Bertolameu dos Mártires — decisões de grafia (ver grafia.py).

As chaves estão na forma do texto estabelecido (grafia de 1619, sem ſ e sem abreviaturas, como as edições
de Lisboa a escrevem). Regra da Biblioteca: grafia de hoje sem trocar palavra; sem forma arcaica de palavra
atual (cousa → coisa, pera → para); palavra que não se usa mais fica e ganha verbete no vocabulário.
"""
import re

ABREVIATURAS = {'s', 'd', 'n', 'fr', 'lib', 'cap', 'etc', 'v', 'ms', 'vs', 'p', 'dr', 'sr', 'm', 'mg'}
CLITICOS = {'lo', 'la', 'los', 'las', 'no', 'na', 'nos', 'nas', 'me', 'te', 'se', 'lhe', 'lhes', 'vos',
            'o', 'a', 'os', 'as', 'mo', 'ma', 'mos', 'mas', 'lho', 'lha', 'lhos', 'lhas', 'to', 'ta'}

# palavras que o léxico deve conhecer (formas antigas que ficam, nomes): entram no léxico
LEXICO_EXTRA = set()

# palavras latinas soltas, sem mudança
LATIM_PALAVRAS = set()

# ------------------------------------------------------------------ antes da grafia (regex no parágrafo)
PRE = [
    (r'\bS\. Domingos\b', 'São Domingos'),
]
DEPOIS = []

# ------------------------------------------------------------------ pronome junto ao verbo (1619: fezlhes, dandonos)
PRONOMES_JUNTOS = ['selhes', 'selhe', 'senos', 'sevos', 'seme', 'lhos', 'lhas', 'lhes', 'lhe', 'lho', 'lha',
                   'nos', 'vos', 'se', 'me', 'te', 'los', 'las', 'lo', 'la', 'mo', 'ma']
PRONOME_FORMA = {'selhes': 'se-lhes', 'selhe': 'se-lhe', 'senos': 'se-nos', 'sevos': 'se-vos', 'seme': 'se-me'}

_G = None


def _g():
    global _G
    if _G is None:
        import grafia1990
        _G = grafia1990
    return _G


def resolve(w):
    """A palavra antiga tem forma de hoje (no léxico ou pelo esqueleto)?"""
    G = _g()
    lw = w.lower()
    if lw in MANUAL or lw in G.lexico():
        return True
    return G.atual(lw)[1] != 'SEM_PAR'


def verbo_valido(base, pron):
    """«levantarse» → levantar + se: só se a palavra inteira não existe e a base existe (para -lo/-la, a base
    com o «r» do infinitivo: fazelo → fazer)."""
    inteira = base + pron
    if resolve(inteira) or len(base) < 3:
        return False
    if pron in ('lo', 'la', 'los', 'las'):
        return re.search(r'[aeiou]$', base) is not None and resolve(base + 'r')
    return resolve(base)


def antes_de_clitico(base, pron):
    """fazer + lo: a forma da base antes do pronome (só muda nos -lo/-la: fazê-lo, dá-lo, pô-lo)."""
    if pron in ('lo', 'la', 'los', 'las') and re.search(r'[aeiou]$', base):
        return base[:-1] + {'a': 'á', 'e': 'ê', 'i': 'i', 'o': 'ô', 'u': 'u'}[base[-1]]
    return base


# ------------------------------------------------------------------ palavras
# forma do texto (minúscula) → forma de hoje
MANUAL = {
    'he': 'é', 'hum': 'um', 'huma': 'uma', 'hua': 'uma', 'húa': 'uma', 'hũa': 'uma', 'huas': 'umas',
    'húas': 'umas', 'huns': 'uns', 'algua': 'alguma', 'alguas': 'algumas', 'algúa': 'alguma', 'algúas': 'algumas',
    'nenhua': 'nenhuma', 'nenhúa': 'nenhuma', 'nenhuas': 'nenhumas', 'nenhúas': 'nenhumas',
    'deos': 'deus', 'pera': 'para', 'assi': 'assim', 'assy': 'assim', 'despois': 'depois', 'cousa': 'coisa',
    'cousas': 'coisas', 'dous': 'dois', 'oje': 'hoje', 'ouve': 'houve', 'ouvesse': 'houvesse',
    'ouverão': 'houveram', 'ouvera': 'houvera', 'aver': 'haver', 'avia': 'havia', 'avião': 'haviam',
'polla': 'pela', 'pollas': 'pelas', 'pollo': 'pelo', 'pollos': 'pelos', 'pola': 'pela',
    'polas': 'pelas', 'polo': 'pelo', 'polos': 'pelos', 'ley': 'lei', 'leys': 'leis', 'rey': 'rei', 'reys': 'reis',
    'foy': 'foi', 'muyto': 'muito', 'muyta': 'muita', 'muytos': 'muitos', 'muytas': 'muitas', 'muy': 'mui',
    'mayor': 'maior', 'mayores': 'maiores', 'meyo': 'meio', 'meyos': 'meios', 'ceo': 'céu', 'ceos': 'céus',
    'sy': 'si', 'ty': 'ti', 'my': 'mi', 'aly': 'ali', 'ahi': 'aí', 'dahi': 'daí', 'daqui': 'daqui',
    'vintesinco': 'vinte e cinco', 'quasi': 'quase', 'rezão': 'razão', 'rezões': 'razões', 'reposta': 'resposta',
    'repostas': 'respostas', 'frey': 'frei', 'raynha': 'rainha', 'reyno': 'reino', 'reynos': 'reinos',
    'hespanha': 'espanha', 'hespanhas': 'espanhas', 'espanhas': 'espanhas', 'lingoa': 'língua', 'lingoas': 'línguas',
    'agoa': 'água', 'agoas': 'águas', 'legoa': 'légua', 'legoas': 'léguas', 'igreja': 'igreja',
    'mão': 'mão', 'tambem': 'também', 'porem': 'porém', 'alem': 'além', 'atè': 'até', 'atê': 'até', 'até': 'até',
    'té': 'até', 'des': 'des', 'nam': 'não', 'som': 'são',
}
MANUAL_EXATO = {'S.': 'S.', 'D.': 'D.', 'Fr.': 'Fr.'}

# «palavra|seguinte» → forma
CONTEXTO = {}

# ------------------------------------------------------------------ ambíguas (pratica × prática)
DETERMINANTES = {'o', 'a', 'os', 'as', 'um', 'uma', 'hum', 'hua', 'húa', 'huma', 'da', 'do', 'das', 'dos', 'na', 'no',
                 'nas', 'nos', 'sua', 'seu', 'suas', 'seus', 'esta', 'este', 'estas', 'estes', 'essa', 'esse',
                 'aquella', 'aquelle', 'aquela', 'aquele', 'grande', 'muyta', 'muyto', 'muita', 'muito', 'tanta',
                 'tanto', 'toda', 'todo', 'pela', 'pelo', 'pola', 'polo', 'polla', 'pollo', 'mesma', 'mesmo', 'outra',
                 'outro', 'nossa', 'nosso', 'vossa', 'vosso', 'qualquer', 'algua', 'algúa', 'alguma', 'algum',
                 'nenhua', 'nenhum', 'cada', 'tal', 'tão', 'mais', 'pouca', 'pouco', 'sem', 'com', 'de', 'em', 'por',
                 'per', 'pera', 'para', 'à', 'ao', 'aos', 'às', 'á', 'e', '&', 'minha', 'meu', 'tua', 'teu', 'boa', 'bom',
                 'santa', 'santo', 'primeira', 'primeiro', 'ultima', 'ultimo', 'verdadeira', 'verdadeiro'}
VERBAIS = {'se', 'lhe', 'lhes', 'me', 'te', 'vos', 'não', 'nam', 'eu', 'tu', 'ele', 'elle', 'ella', 'nós', 'vós',
           'quem', 'que', 'q'}
AMBIG = {}


def desambiguar(lw, ant, seg, formas):
    acentuadas = [f for f in formas if f != lw]
    if lw in AMBIG:
        return AMBIG[lw]
    if ant in DETERMINANTES and acentuadas:
        return acentuadas[0]
    if ant in VERBAIS:
        return lw
    return AMBIG_PADRAO.get(lw, lw if lw in formas else acentuadas[0])


AMBIG_PADRAO = {}
