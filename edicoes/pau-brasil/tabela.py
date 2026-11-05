"""Pau Brasil — refaz grafia.tsv, a tabela palavra a palavra da grafia de 1925 para a de hoje.

    python3 edicoes/pau-brasil/tabela.py        (na raiz do repositório)

Ponto de partida: edicoes/sao-bernardo/grafia1990.py (léxico do sistema + textos publicados; esqueleto que iguala
annos/anos, ph/f, y/i, ll/l…). Por cima, MANUAL (a forma certa onde a automática erra ou não acha par) e MANTER
(formas de Oswald e palavras estrangeiras, que ficam como estão). A tabela gravada é a que o montar.py usa: o
resultado não depende do léxico do momento. Revisar o grafia.tsv inteiro depois de mudar algo aqui.
"""
import collections, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, 'edicoes', 'sao-bernardo')); sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
import grafia1990 as G  # noqa: E402
from edicao.tokens import TOK, e_palavra  # noqa: E402

# formas de Oswald (fala popular, criação, grafia de propósito), estrangeirismos e nomes que ficam
MANTER = set('''
sordado Qué apanhá singulá vortas Postretutas famias Sipantarrou sipantou comê bebê pitá Quá comade Coa coa arraiá mio mió pió
teado pensamenteado Encumbi Miquilina Dlendlena Mivam Abranhão marcineiro meúdas Trenador Trenar boxista toelette felecidade Sstyle
Picássos quadrangula hurla Domingaliza Bengalo Cretones fox-trota assi Assi pera fruita espadoas saradinhas guedelha toutiço aturado
registados Registe curteza aprendimentos Cabralismo gabinetismo palmilhação primitividade confettismo aquoibonismo haïkaï
jaboticabas gabirobas Capiberibe Paraty Carrie d’Eu Bertolini’s Pedr Dum doirado loiro Pra pra Exma Sra
II III IV VI I V Janeiro Maio filles mare récompense Rémy très rendez-vous lèvre Particulière poète Frühling frühling attrayante coustume
cow-boy d’Abbeville d’Angleterre Sur Est Et Il Les Le La Des Ni On Qui Cette Mi Los Sin Ahora una mia la des les le et une un son vers
atelier Atelier cabarets chauffeurs Chauffage boxeur feerie hangars bourgogne Maquereau garçonne garçonniere Kodak Sometimes called
Amerenglish Modern New-Garden Jardin plebeius sermo Hernani Salon jersey jockeys record records ringue clinches klaxon swing whisky
yankee film team offices yole Walzertraum veredictum gigolôs alfandegueiros altifalante Cielo
'''.split())

MANUAL = {
    # a automática erra
    'ahi': 'aí', 'attrahe': 'atrai', 'azes': 'ases', 'bebés': 'bebês', 'bébés': 'bebês', 'caes': 'cais', 'Cahe': 'Cai', 'cahe': 'cai',
    'cahi': 'caí', 'chà': 'chá', 'epitheto': 'epíteto', 'E’s': 'És', 'là': 'lá', 'lêm': 'leem', 'páo': 'pau', 'paiz': 'país',
    'Paiz': 'País', 'photographo': 'fotógrafo', 'Photographo': 'Fotógrafo', 'sahe': 'sai', 'sahi': 'saí', 'têia': 'teia',
    'vehiculo': 'veículo', 'Annuncio': 'Anúncio', 'dactylographas': 'datilógrafas', 'Peredôa': 'Peredoa', 'Perdôa': 'Peredoa',
    # sem par no léxico
    'abrio': 'abriu', 'adherentes': 'aderentes', 'algodam': 'algodão', 'alimaria': 'alimária', 'alvi-negra': 'alvinegra',
    'Anhangabahu': 'Anhangabaú', 'archaismos': 'arcaísmos', 'architectonico': 'arquitetônico',
    'Assucar': 'Açúcar', 'assucar': 'açúcar', 'Athayde': 'Ataíde', 'azues': 'azuis', 'Azues': 'Azuis', 'bambusaes': 'bambuzais',
    'bemfeitora': 'benfeitora', 'Bemvinda': 'Benvinda', 'bençam': 'bênção', 'Bestâo': 'Bestão', 'bolea': 'boleia',
    'Cafezaes': 'Cafezais', 'cafezaes': 'cafezais', 'cançados': 'cansados', 'Catullo': 'Catulo', 'ceo': 'céu', 'chapeo': 'chapéu',
    'chicorea': 'chicória', 'Chorographia': 'Corografia', 'cinematico': 'cinemático', 'comprehendem': 'compreendem',
    'coqueiraes': 'coqueirais', 'craneo': 'crânio', 'creada': 'criada', 'creadora': 'criadora', 'creança': 'criança',
    'Creança': 'Criança', 'creançada': 'criançada', 'creanças': 'crianças', 'Creanças': 'Crianças', 'creara': 'criara',
    'creação': 'criação', 'dansa': 'dança', 'dansarem': 'dançarem', 'daçucre': 'd’açucre', 'deante': 'diante',
    'deleteria': 'deletéria', 'desperdicio': 'desperdício', 'scepticismo': 'ceticismo', 'pyrogravura': 'pirogravura', 'pictorescos': 'pitorescos', 'amphitheatro': 'anfiteatro', 'Descollocado': 'Descolocado', 'deshabitada': 'desabitada',
    'distinctos': 'distintos', 'Dithirambo': 'Ditirambo', 'd’oleo': 'd’óleo', 'egreja': 'igreja', 'Egreja': 'Igreja',
    'egrejas': 'igrejas', 'Egrejas': 'Igrejas', 'Eil-o': 'Ei-lo', 'empennacham': 'empenacham', 'emquanto': 'enquanto',
    'Emquanto': 'Enquanto', 'encyclopedismo': 'enciclopedismo', 'escarneo': 'escárnio', 'escoteyra': 'escoteira',
    'esculptura': 'escultura', 'espectaculosa': 'espetaculosa', 'exgotada': 'esgotada', 'extranha': 'estranha',
    'genovez': 'genovês', 'glú-glú': 'glu-glu', 'gorgeia': 'gorjeia', 'he': 'é', 'hespanhoes': 'espanhóis',
    'Higyenopolis': 'Higienópolis', 'hombros': 'ombros', 'Hu': 'Um', 'hu': 'um', 'hua': 'uma', 'ideas': 'ideias', 'idéas': 'ideias',
    'idéa': 'ideia', 'Immutabilidade': 'Imutabilidade', 'incomprehensão': 'incompreensão', 'inscripção': 'inscrição',
    'Itapoan': 'Itapuã', 'jurity': 'juriti', 'kagados': 'cágados', 'kilometros': 'quilômetros', 'lampeões': 'lampiões',
    'lindacôr': 'lindacor', 'Loyde': 'Loide', 'machina': 'máquina', 'Marcello': 'Marcelo', 'melopea': 'melopeia',
    'Migueis': 'Miguéis', 'mossos': 'moços', 'Mœriken': 'Mörike', 'Nietsche': 'Nietzsche', 'nam': 'não',
    'néo-impressionistas': 'neoimpressionistas', 'neologica': 'neológica', 'nhambú': 'nhambu', 'núzinho': 'nuzinho',
    'orchestra': 'orquestra', 'Paschoa': 'Páscoa', 'Passionaria': 'Passionária', 'patriarcha': 'patriarca', 'peor': 'pior',
    'pharoes': 'faróis', 'prelio': 'prélio', 'processionaes': 'processionais', 'Proteje': 'Protege', 'pyogravura': 'pirogravura',
    'quasi': 'quase', 'Quasi': 'Quase', 'rabecôa': 'rabecoa', 'rasam': 'razão', 'rastacuerico': 'rastacuérico',
    'recream': 'recreiam', 'salutifera': 'salutífera', 'Sanctuario': 'Santuário', 'sanctuarios': 'santuários',
    'snobismo': 'esnobismo', 'sobremetter': 'sobremeter', 'socego': 'sossego',
    'suffragete': 'sufragete', 'surgio': 'surgiu', 'surprehendente': 'surpreendente', 'Suruhy': 'Suruí', 'taboas': 'tábuas',
    'tafetas': 'tafetás', 'tam': 'tão', 'thomismo': 'tomismo', 'tricornio': 'tricórnio', 'triumphantes': 'triunfantes',
    'vam': 'vão', 'veiu': 'veio', 'Yguassu': 'Iguaçu', 'zangadissimo': 'zangadíssimo', 'nickel': 'níquel', 'mayor': 'maior',
    'aja': 'haja', 'ós': 'os', 'Sete-Lagôas': 'Sete Lagoas', 'Buenos-Ayres': 'Buenos Aires', 'São-Paulo': 'São Paulo',
    'Estados-Unidos': 'Estados Unidos', 'rezes': 'reses', 'Deixemol-os': 'Deixemo-los', 'sam': 'são', 'romans': 'romãs', 'Cà': 'Çà', 'è': 'é', 'escoria': 'escória',
    # palavras de 1925 que o léxico tinha (grafia antiga nos textos publicados)
    'Ella': 'Ela', 'ella': 'ela', 'Elle': 'Ele', 'elle': 'ele', 'Elles': 'Eles', 'elles': 'eles', 'Historia': 'História',
    'historia': 'história', 'Musica': 'Música', 'musica': 'música', 'Manoel': 'Manuel', 'Paes': 'Pais', 'Policia': 'Polícia',
    'Silencio': 'Silêncio', 'silencio': 'silêncio', 'Vae': 'Vai', 'vae': 'vai', 'Vicio': 'Vício', 'annos': 'anos',
    'arvore': 'árvore', 'arvores': 'árvores', 'Arvores': 'Árvores', 'bello': 'belo', 'beneficio': 'benefício', 'cavallo': 'cavalo',
    'celebre': 'célebre', 'circulo': 'círculo', 'compendio': 'compêndio', 'copia': 'cópia', 'delicias': 'delícias',
    'distancia': 'distância', 'domestica': 'doméstica', 'effeito': 'efeito', 'espirito': 'espírito', 'Espirito': 'Espírito',
    'fabricas': 'fábricas', 'facto': 'fato', 'fieis': 'fiéis', 'formulas': 'fórmulas', 'imaginarias': 'imaginárias',
    'influencia': 'influência', 'influencias': 'influências', 'interpretes': 'intérpretes', 'intimo': 'íntimo',
    'medico': 'médico', 'negocio': 'negócio', 'prognostico': 'prognóstico', 'publico': 'público', 'radio': 'rádio',
    'refugio': 'refúgio', 'revolucionaria': 'revolucionária', 'tecto': 'teto', 'transito': 'trânsito', 'ultima': 'última',
    'Antonio': 'Antônio', 'Cruzeiro': 'Cruzeiro', 'Victor': 'Victor', 'Polo': 'Polo', 'Sevilla': 'Sevilla',
}


def palavras(txt):
    t = re.sub(r'^(=p|==|=|§|~|>|\|)\s', ' ', txt, flags=re.M).replace('_', ' ')
    return collections.Counter(w for w in TOK.findall(G.nfc(t)) if e_palavra(w))


if __name__ == '__main__':
    txt = open(os.path.join(AQUI, 'original', 'pau-brasil-1925.txt'), encoding='utf-8').read()
    sys.path.insert(0, AQUI)
    from montar import CORRECOES          # a tabela parte do texto já corrigido
    for a, b, _ in CORRECOES:
        txt = txt.replace(a, b)
    linhas, sem = [], []
    for w, n in sorted(palavras(txt).items(), key=lambda x: (x[0].lower(), x[0])):
        if w in MANTER:
            continue
        if w in MANUAL:
            novo, fonte = MANUAL[w], 'manual'
        else:
            novo, fonte = G.atual(w)
            novo = G.composto(novo)
            if fonte == 'SEM_PAR':
                sem.append(w)
                continue
        if novo != w:
            linhas.append('%s\t%s\t%s\t%d' % (w, novo, fonte, n))
    open(os.path.join(AQUI, 'grafia.tsv'), 'w', encoding='utf-8').write(
        '# 1925\thoje\tfonte\tvezes  (gerado por tabela.py; revisado à mão)\n' + '\n'.join(linhas) + '\n')
    print(len(linhas), 'trocas; sem par e sem decisão (ficam como estão):', len(sem))
    print(' '.join(sem))
