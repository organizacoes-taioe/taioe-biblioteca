"""Cartas de Anchieta — título, descrição e a página «Sobre esta edição» (usados por publicar.py)."""

TITULO = 'Cartas, informações e sermão'

DESCRICAO = ('Treze peças escolhidas das cartas, informações e sermões de São José de Anchieta, de 1554 a 1594, '
             'pela edição da Academia Brasileira de Letras (1933): os primeiros anos de São Paulo, as coisas '
             'naturais de São Vicente, as pazes de Iperoig, a fundação do Rio de Janeiro e a informação do Brasil de 1584.')

# a linha em itálico no começo das peças que Anchieta escreveu em latim ou castelhano
_T = 'Tradução portuguesa da edição de 1933 (Academia Brasileira de Letras).'
LINHA_TRADUCAO = {
    'I': 'Escrita em latim. ' + _T,
    'III': 'Escrita em castelhano. ' + _T,
    'X': 'Escrita em latim. ' + _T,
    'XI': 'Escrita em castelhano. ' + _T,
    'XIV': 'Escrita em castelhano. ' + _T,
    'XV': 'Escrita em castelhano. ' + _T,
    'XXVII': 'Escrita em castelhano. ' + _T,
}

APRESENTACAO = """**Texto-base.** Esta seleção segue o volume _Cartas, informações, fragmentos históricos e sermões do Padre Joseph de Anchieta, S. J. (1554-1594)_, publicado pela Academia Brasileira de Letras na coleção «Cartas Jesuíticas» (Rio de Janeiro, Civilização Brasileira, 1933), com nota preliminar de Afrânio Peixoto e as notas de Antônio de Alcântara Machado. O volume reúne 28 cartas, 8 informações e fragmentos e 2 sermões. O fac-símile usado é o do exemplar da Biblioteca Nacional de Portugal, no Internet Archive.

**A seleção.** Ficaram treze peças, com o número que têm na edição de 1933: a primeira grande carta de Piratininga, de 1554, que conta os começos de São Paulo (I); uma carta aos irmãos enfermos de Coimbra (II) e outra a Santo Inácio de Loiola (III), do mesmo ano; a carta de 1560 sobre as coisas naturais de São Vicente, uma das primeiras descrições da natureza do Brasil (X), e a carta do mês seguinte (XI); a da guerra de Piratininga, de 1563 (XIV); a longa carta de janeiro de 1565 sobre as pazes com os Tamoios em Iperoig, onde Anchieta ficou como refém (XV); a de julho de 1565 sobre a armada de Estácio de Sá e o começo do Rio de Janeiro (XVI); um bilhete de 1579 ao capitão Jerônimo Leitão (XX); a última carta, de 1594, ao Padre Cláudio Aquaviva (XXVII); a _Informação do Brasil e de suas capitanias_, de 1584 (XXIX); a _Informação dos casamentos dos índios do Brasil_ (XXXIII); e o _Sermão da Conversão de São Paulo_, pregado em Piratininga em 25 de janeiro de 1568 (XXXVIII). Os títulos das peças são nossos; os da edição de 1933 e os seus sumários não foram reproduzidos.

**As traduções.** Anchieta escrevia em português, castelhano, latim e tupi. Das treze peças, duas foram escritas em latim (I e X) e cinco em castelhano (III, XI, XIV, XV e XXVII); vão na tradução portuguesa impressa em 1933, que o volume não atribui carta a carta. A nota preliminar diz que os «traslados e traduções de cartas» do volume são de Antônio de Alcântara Machado (1901–1935); as notas de cada carta registram as versões anteriores: a de Teixeira de Melo (1833–1907), nos _Anais da Biblioteca Nacional_ (1876) e no _Diário Oficial_ (1887–1888), com cortes; a do cônego Januário da Cunha Barbosa (1780–1846), na _Revista do Instituto Histórico_ (1840), para a XIV; e a dos _Anais do Rio de Janeiro_ de Baltasar da Silva Lisboa (1761–1840), para a XI. As cartas III e XXVII saíram em português pela primeira vez em 1933. Todos esses tradutores morreram antes de 1955. Duas peças do volume ficaram de fora porque nele vêm na tradução do professor João Vieira de Almeida (São Paulo, 1900), cuja data de morte não se conhece: a carta VII e a _Breve narração_ de 1584 (XXXI). A tradução da carta X que o volume traz não é a dele: foi conferida com a edição de 1900.

**Os textos em português.** A carta II vem pela _Vida_ de Anchieta escrita por Simão de Vasconcelos (1672), de onde a tirou a edição de 1933; as demais peças em português vêm de cópias antigas (Biblioteca de Évora, Biblioteca Nacional, o registro de cartas da casa de São Roque), salvo a XX, impressa pelo original do Museu Paulista, e o sermão, pelas fotografias do original de Antuérpia. As duas _Informações_ não levam assinatura: a de 1584 foi atribuída a Anchieta por Varnhagen e por Capistrano de Abreu, que a publicou em 1886 entre as _Informações e fragmentos históricos do Padre Joseph de Anchieta_; a dos casamentos, pela edição de 1933, depois de a _Revista do Instituto Histórico_ a dar como dele (1846).

**Como foi estabelecido.** Três leituras por OCR (duas nossas, com o Tesseract, e a do Internet Archive), com as linhas em que divergiam e as palavras duvidosas conferidas nas imagens, uma a uma; também se conferiram nas imagens as linhas que uma das leituras pulou. Para a _Informação_ de 1584 houve um segundo testemunho, a edição de Capistrano de Abreu (1886), que corrigiu uma linha trocada na composição de 1933. As edições modernas, que são protegidas, não foram usadas.

**Grafia.** Ortografia de hoje (Acordo de 1990, forma brasileira), com as palavras e a ordem das frases da edição de 1933: cousa → coisa, pera → para, assi → assim, pola → pela, peor → pior, deante → diante, quasi → quase, maximè → máxime, êste → este. As formas antigas de palavras que ainda se usam vão na forma de hoje; as palavras que não se usam mais ficam como estão. Nomes de pessoas e de lugares na forma de hoje (Nóbrega, Luís, Brás, Inácio, Estácio, Bahia); os nomes indígenas e as palavras tupis, como na edição de 1933 (Iperuig, Pindobuçú, Cunhambeba, _mandaró_). Os trechos em latim vão em itálico. Fica a mesóclise dos textos (ver-se-á, dir-vo-lo-ei). As chamadas das notas de 1933 saíram do texto."""

FONTES = [
    {'nome': 'Cartas, informações, fragmentos historicos e sermões do Padre Joseph de Anchieta, S. J. (1554-1594), '
             'Academia Brasileira / Civilização Brasileira, 1933 (Internet Archive, exemplar da Biblioteca Nacional de Portugal)',
     'url': 'https://archive.org/details/r-19794-v_0000_grav-569_t24-C-R0150', 'nota': 'texto-base'},
    {'nome': 'Informações e fragmentos historicos do padre Joseph de Anchieta, S. J. (1584-1586), ed. Capistrano de Abreu, 1886 '
             '(Brasiliana USP)',
     'url': 'https://digital.bbm.usp.br/handle/bbm/8015', 'nota': 'segundo testemunho da Informação de 1584'},
    {'nome': 'Carta fazendo a descripção das innumeras coisas naturaes… seguida de outras cartas inéditas, trad. João Vieira '
             'de Almeida, 1900 (Brasiliana USP)',
     'url': 'https://digital.bbm.usp.br/handle/bbm/4683', 'nota': 'só para comparar a tradução da carta X'},
]
