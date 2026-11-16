"""Cartas de Anchieta — o léxico que separa as palavras certas das duvidosas na leitura de 1933.

O léxico ampliado da Vida de Anchieta (montar._lexico_ampliado: dicionário do Brasil e de Portugal + textos
publicados), as formas de 1933 que ele não tem (cousa, quasi, veiu, deante…) e as palavras latinas e tupis
que se repetem nas peças. Nome próprio (maiúscula) não é conferido por aqui.
"""
import os
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'sao-bernardo'))
sys.path.insert(0, AQUI)

ANTIGAS = set('''cousa cousas quasi veiu deante adeante maximê maximé naus comsigo comtudo pola polas polo polos peor
peores assucar brasilica brasilicas brasilico brasilicos defensão deshonra deshonrar cincoenta subtil subtis
barregão soia soiam sinão assi ende governança catecúmena catecúmeno incançavel quadrimestre quadrimestres
quadrimestrais salutifera abundantissimo copiosissimos frequentissimamente facinorosos benignamente
mangedoura pera té comnosco convosco emfim rezão aqueloutros comenos crear creação creado creatura creaturas
dezaseis dezasete dezanove mezinhas mezinha ácerca acêrca'''.split())

LATIM = set('''civitatem scilicet quia persequeris facere omnes electionis sicut extremis etiam ut furtum tibi excessu
iniquitatis filius sunt ingredere virtus in infirmitate perficitur et super flumina babylonis medio pro paupere
fratre pauper inutilis vos opto bene valere est mihi iste vas die convertionis pauli act militia vita hominis
homini terram consortibus suis non ad quam deus meus quid me dereliquisti cum de qui quae quod nos mutuerunt
semper oretis rogo minimus societatis jesu jesus christi pax domine dominus durum contra stimulum calcitrare
saule saulus es ego sum quem tu lux caelo calo cecidit leo tribu juda radix david vicit lupus rapax mane
comedet praedam predam vespere dividet spolia incipiebam incipiebat enim mori nisi dominus adiuvit paulo minus
habitasset inferno anima mea sine effusione sanguinis fit remissio amen'''.split())

_LEX = None


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()


def _carregar():
    global _LEX
    if _LEX is None:
        import montar  # noqa: F401  (amplia o léxico da grafia ao ser importado)
        import grafia1990 as G
        lex = G.lexico()
        _LEX = (lex, {sem_acento(w) for w in lex}, G)
    return _LEX


_CACHE = {}


def ok(w):
    """A palavra (sem pontuação) existe? Maiúscula conta como nome próprio."""
    if w in _CACHE:
        return _CACHE[w]
    lex, lexsa, G = _carregar()
    lw = w.lower()
    r = (w[:1].isupper() or lw in lex or sem_acento(lw) in lexsa or lw in ANTIGAS or lw in LATIM
         or ('-' in lw and all(ok(p) for p in lw.split('-') if p))
         or G.atual(lw)[1] != 'SEM_PAR')
    _CACHE[w] = r
    return r
