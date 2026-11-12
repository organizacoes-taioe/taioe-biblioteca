"""Minha Formação — decisões editoriais.

EMENDAS: intervenções no texto-base, na grafia de 1900: (tipo, trecho, troca)
  'erro'    erro tipográfico evidente da edição de 1900 (conferido no fac-símile de Toronto; os dois OCRs,
            de dois exemplares, o confirmam)
  'ocr'     erro da transcrição do Gutenberg; o impresso de 1900 traz a forma certa (conferido no fac-símile)
AJUSTES: depois da modernização, em tokens separados por espaço: (tipo, antes, de, para, depois)
MANUAL: grafia final de palavras que as edições de referência não resolvem (ou resolvem mal)
corrigir: ajustes de composição sobre o texto pronto
"""
import re

EMENDAS = [
    # erros da transcrição do Gutenberg (conferidos no fac-símile)
    ('ocr', 'Sua Eminencia, cora effeito', 'Sua Eminencia, com effeito'),
    ('ocr', 'isolava-se, ciystallisava-se', 'isolava-se, crystallisava-se'),
    ('ocr', 'da casatudo que', 'da casa tudo que'),
    # erros tipográficos de 1900 (os dois exemplares, de Toronto e de Harvard, os têm)
    ('erro', 'communhão de vida, individuæ vitæ consuetuoinem', 'communhão de vida, individuæ vitæ consuetudinem'),
    ('erro', 'pura e ciaphana atmosphera', 'pura e diaphana atmosphera'),
    ('erro', 'seus pratos architectomicos', 'seus pratos architectonicos'),
    ('erro', 'de vida á parte, de reponsabilidade', 'de vida á parte, de responsabilidade'),
    ('erro', 'republicano concidiu com', 'republicano coincidiu com'),
    ('erro', 'pelo governo parlementar', 'pelo governo parlamentar'),
    ('erro', 'ajudado a resgastar', 'ajudado a resgatar'),
    ('erro', 'e aida peior', 'e ainda peior'),
    ('erro', 'subverter as instituções', 'subverter as instituições'),
    ('erro', 'os homens, as instituções rivaes', 'os homens, as instituições rivaes'),
    ('erro', 'de velhos servidares', 'de velhos servidores'),
    ('erro', 'esses suecos de vida', 'esses succos de vida'),
    ('erro', 'Nenhum da nós', 'Nenhum de nós'),
    ('erro', 'deante de um de um grande chefe', 'deante de um grande chefe'),
    ('erro', 'exercer sobre a mim', 'exercer sobre mim'),
    ('erro', 'um clero a cuja mãos', 'um clero a cujas mãos'),
    ('erro', 'invenção, sua marcas', 'invenção, suas marcas'),
    ('erro', 'em um religião revelada', 'em uma religião revelada'),
    ('erro', 'perfeita da cravações', 'perfeita das cravações'),
    ('erro', 'que os agasalhada', 'que os agasalhava'),
    ('erro', 'que põem acida de tudo', 'que põem acima de tudo'),
    ('erro', 'elle devesse bulbuciar', 'elle devesse balbuciar'),
    ('erro', 'A Restauração, póde-dizer', 'A Restauração, póde-se dizer'),
    ('erro', 'uma emenda constitutional', 'uma emenda constitucional'),
    ('erro', 'o nosso self-governement', 'o nosso self-government'),
    ('erro', 'Alexandre Hamilton. Un homem', 'Alexandre Hamilton. Um homem'),
    ('erro', 'da sua esphera contencisa', 'da sua esphera contenciosa'),
    ('erro', 'de convencionanismo e cerimonial', 'de convencionalismo e cerimonial'),
]

AJUSTES = []

MANUAL = {
    # formas antigas de palavras atuais (o texto do Wikisource não dá o par, ou dá outro)
    'absorpção': 'absorção', 'presumpção': 'presunção', 'assumpção': 'assunção', 'redempção': 'redenção',
    'redempções': 'redenções', 'schisma': 'cisma', 'iman': 'ímã', 'Strabão': 'Estrabão', 'Slavos': 'Eslavos',
    'extasis': 'êxtase', 'cincoenta': 'cinquenta', 'coiro': 'couro', 'rans': 'rãs', 'praeiras': 'praieiras',
    'taixas': 'tachas', 'regimen': 'regímen', 'regimem': 'regímen', 'specimen': 'espécimen', 'Sahi': 'Saí',
    'Itapoan': 'Itapoã', 'Nazareth': 'Nazaré', 'Magdalena': 'Madalena', 'Piumhy': 'Piumhi',
    'Pirassinunga': 'Pirassununga', 'Lethes': 'Letes', 'Gœthe': 'Goethe', 'Rœntgen': 'Roentgen',
    'Tautphœus': 'Tautphoeus', 'Corrêa': 'Correia', 'Commercio': 'Comércio', 'Actualidade': 'Atualidade',
    'd’ouro': 'de ouro', 'd’arte': 'de arte', 'd’ora': 'de ora',
    # nomes e palavras estrangeiras que ficam como estão (o texto do Wikisource os estropia)
    'Lafayette': 'Lafayette', 'Jeanne': 'Jeanne', 'Gallery': 'Gallery', 'Burckhardt': 'Burckhardt',
    'James’s': 'James’s', 'Dürer': 'Dürer', 'Münster': 'Münster', 'Orléans': 'Orléans',
    'Macaulayiano': 'macaulayiano', 'Lords': 'Lords', 'Lord': 'Lord', 'club': 'club', 'clubs': 'clubs',
    'Club': 'Club', 'cœur': 'cœur', 'Cœur': 'Cœur', 'l’œuvre': 'l’œuvre', 'Joconde': 'Joconde', 'Mgr': 'Mgr',
    'd’Enfance': 'd’Enfance', 'Francisco': 'Francisco', 'Gambetta': 'Gambetta', 'Whitehall': 'Whitehall',
    'leaders': 'leaders', 'estrenuo': 'estrênuo', 'diptycos': 'dípticos', 'escorço': 'escorço', 'destróem': 'destroem',
    'Trappa': 'Trapa', 'San-Sebastian': 'San Sebastián', 'arrêter': 'arrêter', 'distillava': 'destilava', 'recompuz': 'recompus', 'bailada': 'bailada', 'cravado': 'cravado', 'inda': 'inda', 'conservatismo': 'conservatismo',
}


def corrigir(out, flags):
    """Ajustes de composição sobre o texto pronto: «M.me» (M^me em 1900) como «Mme.», a forma do resto do
    livro; as versaletes do quadro do «Caminho de ferro subterrâneo» (o Gutenberg as dá em maiúsculas)."""
    novo, nf = [], []
    i = 0
    while i < len(out):
        t = out[i]
        if t == '¹' and out[i + 1:i + 3] == ['⁄', '₂']:
            novo.append('½'); nf.append(False); i += 3; continue
        if t == 'M' and out[i + 1:i + 3] == ['me', '.']:
            novo.append('Mme'); nf.append(False); i += 2; continue
        novo.append(t); nf.append(flags[i]); i += 1
    return novo, nf
