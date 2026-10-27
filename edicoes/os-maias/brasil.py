"""Da grafia portuguesa das edições modernas (Acordo de 1990 na norma de Portugal, ou a de 1945) à
grafia brasileira do Acordo de 1990, palavra por palavra.

- PALAVRAS: formas que mudam inteiras (facto -> fato, connosco -> conosco, aspeto -> aspecto: o
  Acordo deixou cair em Portugal consoantes que no Brasil se pronunciam e se escrevem);
- CONSOANTES: c e p mudos da grafia de 1945 (acção -> ação), nas palavras que só a edição de 1945
  resolve;
- acento: é e ó tônicos antes de m ou n passam a ê e ô (génio -> gênio, António -> Antônio);
- pretérito em -ámos -> -amos (acabámos -> acabamos).
"""
import re

PALAVRAS = {
    'facto': 'fato', 'factos': 'fatos',
    'connosco': 'conosco',
    'tacto': 'tato',
    'contacto': 'contato', 'contactos': 'contatos',
    'secção': 'seção', 'secções': 'seções',
    'carácter': 'caráter',
    'húmido': 'úmido', 'húmida': 'úmida', 'húmidos': 'úmidos', 'húmidas': 'úmidas',
    'humidade': 'umidade', 'humidades': 'umidades', 'humedecer': 'umedecer',
    'dezassete': 'dezessete', 'dezasseis': 'dezesseis', 'dezanove': 'dezenove',
    'comummente': 'comumente',
    'bebé': 'bebê', 'bebés': 'bebês',
    # consoantes que o Brasil conserva (Portugal as tirou em 1990)
    'aspeto': 'aspecto', 'aspetos': 'aspectos',
    'receção': 'recepção', 'receções': 'recepções',
    'conceção': 'concepção', 'deceção': 'decepção', 'deceções': 'decepções',
    'perceção': 'percepção', 'perceções': 'percepções', 'percetível': 'perceptível',
    'impercetível': 'imperceptível', 'impercetíveis': 'imperceptíveis', 'percetíveis': 'perceptíveis',
    'perspetiva': 'perspectiva', 'perspetivas': 'perspectivas',
    'espetador': 'espectador', 'espetadores': 'espectadores', 'espetadora': 'espectadora',
    'espetro': 'espectro', 'espetros': 'espectros',
    'respetivo': 'respectivo', 'respetiva': 'respectiva', 'respetivos': 'respectivos', 'respetivas': 'respectivas',
    'circunspeto': 'circunspecto', 'circunspeta': 'circunspecta', 'circunspetos': 'circunspectos',
    'circunspeção': 'circunspecção',
    'prospeto': 'prospecto', 'prospetos': 'prospectos',
    'excecional': 'excepcional', 'excecionais': 'excepcionais', 'excecionalmente': 'excepcionalmente',
    'retrospetivo': 'retrospectivo', 'retrospetiva': 'retrospectiva',
    'infeção': 'infecção', 'infeções': 'infecções',
    'detetar': 'detectar', 'concetual': 'conceptual',
    'recetivo': 'receptivo', 'recetiva': 'receptiva',
    'inspeção': 'inspecção',
    'rutura': 'ruptura',
    # formas que só Portugal conserva
    'baptista': 'batista', 'egipto': 'egito', 'acta': 'ata', 'actas': 'atas', 'atracção': 'atração',
    'jacto': 'jato', 'jactos': 'jatos',
    'omnipotente': 'onipotente', 'omnipotência': 'onipotência', 'omnipresente': 'onipresente',
    'omnisciente': 'onisciente', 'indemnizar': 'indenizar', 'indemnização': 'indenização',
}

# c e p mudos da grafia de 1945 que a edição de 1990 não resolveu (palavra que ela não tem)
CONSOANTES = {}

ACENTO_EXCECOES = {'éden', 'hífen'}


def _caixa(modelo, nova):
    if modelo.isupper() and len(modelo) > 1:
        return nova.upper()
    if modelo[:1].isupper():
        return nova[:1].upper() + nova[1:]
    return nova


def _palavra(w, acento=True):
    b = w.lower()
    if b in PALAVRAS:
        return _caixa(w, PALAVRAS[b])
    if b in CONSOANTES:
        return _caixa(w, CONSOANTES[b])
    if b in ACENTO_EXCECOES:
        return w
    # é/ó tônicos antes de m, n (+ vogal ou fim): ê/ô
    if not acento:
        return re.sub(r'ámos$', 'amos', w)
    n = re.sub(r'é(?=[mn][aeiouáéíóúâêôãõh])', 'ê', w)
    n = re.sub(r'ó(?=[mn][aeiouáéíóúâêôãõh])', 'ô', n)
    n = re.sub(r'É(?=[mnMN][aeiouáéíóúâêôãõAEIOU])', 'Ê', n)
    n = re.sub(r'Ó(?=[mnMN][aeiouáéíóúâêôãõAEIOU])', 'Ô', n)
    # pretérito: -ámos -> -amos
    n = re.sub(r'ámos$', 'amos', n)
    return n


def converter(t, velho=''):
    """Um token: as partes ligadas por hífen são convertidas uma a uma (levámos-lhe, António-José).
    velho: a palavra na 1ª edição; se ela já trazia é/ó (nomes e palavras francesas: Bénédictine),
    o acento não muda."""
    if not t[:1].isalpha():
        return t
    acento = not re.search(r'[éóÉÓ]', velho)
    return '-'.join(_palavra(p, acento) if p else p for p in t.split('-'))


def converter_frase(s, velho=''):
    return ' '.join(converter(t, velho) for t in s.split(' '))
