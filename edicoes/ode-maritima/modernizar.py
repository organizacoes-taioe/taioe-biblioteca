"""Ode Marítima: de texto/orpheu-1915.txt (a transcrição do Orpheu 2, abril-junho de 1915, na grafia da época)
a texto/ode.txt (a grafia brasileira de hoje), palavra por palavra pelo dicionário abaixo.

    python3 edicoes/ode-maritima/modernizar.py        (na raiz do repositório)

Só muda a maneira de escrever; ficam como em 1915 as onomatopeias, os gritos, as palavras inglesas, as
maiúsculas, as reticências e a pontuação, e as contrações «pró», «prá», «prós», «pr'», «plas», «pla». Depois de
rodar, o texto/ode.txt ainda leva as correções à mão listadas em CORRECOES (erros do exemplar transcrito).
"""
import os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
D = {}
def d(a, b):
    for x, y in zip(a.split(), b.split()): D[x] = y
# acentos de 1915 que hoje não se escrevem
d('acôrdo amôr apêlo aquélas aquêle arôma bôca cêdo côr côres dêle dêles dêste dôce dôr êle êles êsse êsses êstes fôgo fôr fôram fôrça fôsse fôssem fôste fôstes favôr frescôr fóra éco gôlfos mêdo mêses môços modêlo nêles nêrvos núvem núvens pavôr pessôa póde póros pôço prôa rigôr rochêdos rêde rêdes sabôr sêco sêde sêr sôa sôbre sômos sôpro sózinho supônho têma torpôr tôscos vapôr vapôres vêr vêrem vêrga vêr-te ólho ôca ôsso cordâme poleâme carnágem pilhágem paquête paquêtes cartaginêses portuguêses catrinêta cálquem cáem sáem caír saír saíndo atraír baïas histería comóvem-me sentí-los nítidamente súbitamente físicamente insensívelmente sensívelmente trémulamente tambêm pára transpôrem-se aguilhôo',
  'acordo amor apelo aquelas aquele aroma boca cedo cor cores dele deles deste doce dor ele eles esse esses estes fogo for foram força fosse fossem foste fostes favor frescor fora eco golfos medo meses moços modelo neles nervos nuvem nuvens pavor pessoa pode poros poço proa rigor rochedos rede redes sabor seco sede ser soa sobre somos sopro sozinho suponho tema torpor toscos vapor vapores ver verem verga ver-te olho oca osso cordame poleame carnagem pilhagem paquete paquetes cartagineses portugueses catrineta calquem caem saem cair sair saindo atrair baías histeria comovem-me senti-los nitidamente subitamente fisicamente insensivelmente sensivelmente tremulamente também para transporem-se aguilhoo')
# acentos que faltavam em 1915
d('abominaveis angustia edificios caricia comercio crueis duvida epoca escrupulo especie especies extase facil furia furias futil genero gloria halito herois higienica higienico historia homerico hoteis humanissimo humanitario importancia impossivel inexplicavel infancia inuteis uteis inutil lagrimas literaria maquinas maritima maritimas maritimo maritimos misterio necessarias numero odios paciencias patria politicas principio proletario proposito provincia proximas proximo revolucionaria silencio simpatico subito tambem transatlanticos transitorios varias voluntario',
  'abomináveis angústia edifícios carícia comércio cruéis dúvida época escrúpulo espécie espécies êxtase fácil fúria fúrias fútil gênero glória hálito heróis higiênica higiênico história homérico hotéis humaníssimo humanitário importância impossível inexplicável infância inúteis úteis inútil lágrimas literária máquinas marítima marítimas marítimo marítimos mistério necessárias número ódios paciências pátria políticas princípio proletário propósito província próximas próximo revolucionária silêncio simpático súbito também transatlânticos transitórios várias voluntário')
# trema e acento de palavras de origem latina
d('antiqùíssimo obliqùo obliqùídade longinqùas longinqùos longinquos tranqùílas tranqùílos tranquilo tranquilamente',
  'antiquíssimo oblíquo obliquidade longínquas longínquos longínquos tranquilas tranquilos tranquilo tranquilamente')
# consoantes e letras
d('abstractos actividade acto actual acções colectores contradicção directo directos objecto recta reflectido reflectidos fluctuar facto factura facturas nocturna nocturnas nocturno comerciaes emfim quasi scismo creanças gageiros cortidas comvôsco comnosco comsigo comtigo civilisação civilisado realisando regularisar horisonte victimas atravez quizerdes compozesse gosar gosarão missanga convez convezes poz veiu sahir logar inglez japonez burguezes soes teem mãis idéa expontaneamente prasenteiro sanguesugas dispensas ância pantheismo snrs húmido prémios omnívora pirata-mór ciclónico atónitas colónias incómodas neurasténicos masóquista tenue ha ás á ágoa ágoas agua',
  'abstratos atividade ato atual ações coletores contradição direto diretos objeto reta refletido refletidos flutuar fato fatura faturas noturna noturnas noturno comerciais enfim quase cismo crianças gajeiros curtidas convosco conosco consigo contigo civilização civilizado realizando regularizar horizonte vítimas através quiserdes compusesse gozar gozarão miçanga convés conveses pôs veio sair lugar inglês japonês burgueses sóis têm mães ideia espontaneamente prazenteiro sanguessugas despensas ânsia panteísmo srs úmido prêmios onívora pirata-mor ciclônico atônitas colônias incômodas neurastênicos masoquista tênue há às à água águas água')
d('vasios socegada bonet andámos ansia estavamos cesario fustíguem longinquo longinqùa nitido semicirculo patagonia', 'vazios sossegada boné andamos ânsia estávamos cesário fustiguem longínquo longínqua nítido semicírculo patagônia')
D['ágoas'] = 'águas'; D['ágoa'] = 'água'
CASOS = [('cousa', 'coisa'), ('cousas', 'coisas'), ('cousas-reais', 'coisas-reais'), ('espíritos-cousas', 'espíritos-coisas')]
for a, b in CASOS: D[a] = b

def caixa(m, n):
    if len(m) > 1 and m.isupper(): return n.upper()
    if m[:1].isupper(): return n[:1].upper() + n[1:]
    return n

def troca(m):
    w = m.group(0)
    n = D.get(w.lower())
    if n: return caixa(w, n)
    if '-' in w:                                         # «regularisar-se», «vêr-te»: palavra a palavra
        return '-'.join(caixa(x, D.get(x.lower(), x)) if x else x for x in w.split('-'))
    return w

PAL = re.compile(r"[A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)*")

# à mão: o que o dicionário não decide sozinho (pelo contexto)
CORRECOES = [
    ('E porque, penso eu isto?', 'E por que penso eu isto?'),
    ('Em que não sei porque sugestão', 'Em que não sei por que sugestão'),
    ('Senti de mais para poder', 'Senti demais para poder'),
    ('crescido de mais para isso', 'crescido demais para isso'),
    ('lavam-o da vida', 'lavam-no da vida'),
    ('préguem-a às quilhas', 'preguem-na às quilhas'),
    ('como um gata com cio', 'como uma gata com cio'),
    ('ora as apostas', 'ora as opostas'),
    ('prático à forca', 'prático à força'),
    ('Amigos e Snrs,', 'Amigos e Srs.,'),
]

GRITO = re.compile(r'lah|yy|[Tt]-t|(?:[A-Za-zÀ-ÿ]-){3}')


def travessoes(t):
    """«--» da transcrição > «—» no texto corrido; as linhas de grito (Ahó-ó-ó--yyyy, Eh-lahô…) ficam como estão."""
    def linha(l):
        if '--' not in l or GRITO.search(l): return l
        l = re.sub(r'^--\s*', '— ', l)
        l = re.sub(r'\s*--(?=[,.;:!?])', ' —', l)
        l = re.sub(r'\s*--\s*$', ' —', l)
        return re.sub(r'\s*--\s*', ' — ', l)
    return '\n'.join(linha(l) for l in t.split('\n'))


def modernizar(t):
    t = re.sub(r'^ +', '', t, flags=re.M)               # sem recuo (o site não o tem)
    t = t.replace('*', '')                              # negritos da transcrição: a caixa-alta já os mostra
    # palavras partidas como «tranqùílas» têm o trema fora do alfabeto simples: o PAL já as pega
    t = PAL.sub(troca, t)
    return travessoes(t)

if __name__ == '__main__':
    raiz = os.path.join(AQUI, 'texto')
    t = open(os.path.join(raiz, 'orpheu-1915.txt'), encoding='utf-8').read()
    t = modernizar(t)
    for a, b in CORRECOES:
        a2 = modernizar(a)
        n = t.count(a2)
        if n != 1: raise SystemExit('correção não casa (%d): %s' % (n, a))
        t = t.replace(a2, modernizar(b) if False else b)
    open(os.path.join(raiz, 'ode.txt'), 'w', encoding='utf-8').write(t)
    print(t.count('\n'), 'linhas')
