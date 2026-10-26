"""Vidas Secas — texto da página «Sobre esta edição»."""
import json
import os

COMENTARIO = '''Vidas Secas — Graciliano Ramos
   Gerado por ferramentas/texto.py a partir de edicoes/vidas-secas/.
   Não edite à mão: corrija as decisões nessa pasta e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados.'''

APRESENTACAO = '''**Texto-base.** Este texto reproduz a segunda edição de _Vidas Secas_ (Rio de Janeiro, José Olympio, 1947), a última revista pelo autor que hoje se pode ler em fac-símile, digitalizada pela Brasiliana USP. A terceira edição (1952), a última publicada em vida do autor, não está digitalizada.

**Como foi estabelecido.** O fac-símile de 1947 só traz uma camada de texto feita por reconhecimento automático (OCR). Ela foi confrontada palavra por palavra com a transcrição da primeira edição (1938) no Wikisource, revista e validada página a página, e, nos três primeiros capítulos, com a transcrição da própria edição de 1947, também do Wikisource. Onde 1947 difere de 1938, valeu a lição de 1947 que o OCR mostra e uma edição moderna confirma; os pontos duvidosos, e todos os que a edição moderna não resolve, foram conferidos nas imagens do fac-símile.

**A segunda edição.** Em 1947 o texto mudou em mais de cem pontos. Há palavras cortadas («Ele era um bruto» → «Ele era bruto»; «e faria um estrago» → «e faria estrago») e trocadas («o odor forte do chiqueiro» → «o fartum do chiqueiro»; «coçou a testa» → «franziu a testa»), uma frase suprimida no fim de «O mundo coberto de penas», parágrafos abertos e juntados, pontuação revista e as contrações desfeitas (_dum_ → de um, _duma_ → de uma, _d’água_ → de água). A lista completa vai abaixo.

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1947 (lista abaixo). Onde a edição moderna lê diferente de 1947 e o fac-símile confirma 1947, ficou 1947; algumas dessas leituras modernas podem vir de correções posteriores do autor, que não se podem conferir, e vão listadas no fim.

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990 (_sêco_ → seco, _êle_ → ele, _fôlha_ → folha, _juàzeiro_ → juazeiro, _pé-de-vento_ → pé de vento, e _por que_ nas perguntas). O vocabulário e as construções do autor ficaram como estão: _sinha Vitória_ (e não «sinhá»), _vossemecê_, _pra_, _toicinho_, _por mor de_, as mesóclises (_Acomodar-se-iam_), a pontuação e os travessões.

**Divisão.** O livro tem treze capítulos titulados, sem número; cada um é uma página desta biblioteca. Num depoimento de 1944 a João Condé, o autor conta que os escreveu fora de ordem, em 1937, começando por «Baleia», que saiu primeiro em jornal, como conto. As datas que ele dá: «Baleia», 4 de maio; «Sinha Vitória», 18 de junho; «Cadeia», 21 de junho; «O menino mais novo», 26 de junho; «O menino mais velho», 8 de julho; «Inverno», 14 de julho; «Mudança», 16 de julho; «Festa», 22 de julho; «Contas», 29 de julho; «Fabiano», 22 de agosto; «O mundo coberto de penas», 27 de agosto; «O soldado amarelo», 6 de setembro; «Fuga», 6 de outubro.'''

BASE = 'Edição de 1947'

_M = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mudancas.json'), encoding='utf-8'))

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1947 corrigidos',
              'explica': 'Grafia atualizada nas duas colunas.'},
    'tradicao': {'titulo': 'Mudanças da segunda edição (1947)',
                 'explica': 'Todos os pontos em que o texto de 1947 difere do de 1938, fora a grafia e as '
                            f'{_M["contracoes"]} contrações desfeitas (dum → de um, duma → de uma, d’água → de água). '
                            '¶ marca o começo de um parágrafo. Grafia atualizada nas duas colunas.',
                 'de': '1ª edição (1938)', 'para': '2ª edição (1947)'},
    'mantidas': {'titulo': 'Lições de 1947 mantidas',
                 'explica': 'Pontos em que a edição moderna de referência, feita sobre as da Record, lê diferente; '
                            'em todos, o fac-símile de 1947 confirma este texto.'},
}

FONTES = [
    {'nome': 'Fac-símile da 2ª edição, 1947 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8480',
     'nota': 'texto-base; o OCR dele entrou no confronto, e as imagens decidiram as dúvidas'},
    {'nome': 'Wikisource em português: a 1ª edição, 1938', 'url': 'https://pt.wikisource.org/wiki/Vidas_seccas',
     'nota': 'transcrição página a página, toda validada, feita sobre o exemplar digitalizado pelo Google'},
    {'nome': 'Wikisource em português: a 2ª edição, 1947', 'url': 'https://pt.wikisource.org/wiki/Vidas_S%C3%AAcas',
     'nota': 'transcrição página a página; usadas as páginas revisadas (capítulos 1 a 3)'},
    {'nome': 'Edição digital gratuita de 2024 (Centro Paula Souza)',
     'url': 'https://bkpsitecpsnew.blob.core.windows.net/uploadsitecps/sites/255/2025/04/vidas-secas.pdf',
     'nota': 'texto moderno, da linhagem das edições da Record; referência para a ortografia'},
]

# (trecho do texto final, leitura da edição moderna, observação)
MANTIDAS = [
    ('joelhos encostados ao estômago', 'encostados no estômago', ''),
    ('estavam agarrados na terra', 'agarrados à terra', ''),
    ('com os talões de recibos', 'com talões de recibos', ''),
    ('Era só o que sabia dizer', 'Era o que sabia dizer', ''),
    ('com sentimentos revolucionários', 'com pensamentos revolucionários', ''),
    ('davam-lhe uma sensação de firmeza', 'davam-lhe sensação de firmeza', ''),
    ('cheio de alegria e de medo', 'cheio de alegria e medo', ''),
    ('A admiração que Fabiano lhe inspirava', 'A admiração a Fabiano', ''),
    ('periquitos que voavam', 'periquitos que voava', ''),
    ('faca de ponta na cintura', 'faca de ponta à cintura', ''),
    ('catingueiras murchas, na beira da lagoa', 'à beira da lagoa', ''),
    ('o cascudo na cabeça do menino mais velho', 'o cascudo no menino mais velho', ''),
    ('passou por baixo do pé de turco', 'passou pelo pé de turco', ''),
    ('Não estava alegre, mas também não podia sentir uma dor excessiva', 'Não podia sentir dor excessiva', ''),
    ('trouxe a lembrança da palavra', 'trouxe a recordação da palavra', ''),
    ('preferia saltar e espojar-se no chão', 'preferia saltar e espojar-se', ''),
    ('servindo de travesseiros aos dois filhos', 'servindo de travesseiros aos filhos', ''),
    ('em redor da trempe de pedra', 'da trempe de pedras', ''),
    ('Se pudesse ver-lhe o rosto', 'Se pudesse ver o rosto do pai', ''),
    ('os habitantes invisíveis da serra', 'invisíveis da terra', ''),
    ('ele se esgoelava demais', 'se esgoelava demais', ''),
    ('Tinha dominado a obstinação', 'Tinha vencido a obstinação', ''),
    ('magoavam-no em demasia', 'magoavam-nos em demasia', ''),
    ('Cheios de admiração e de medo', 'Admirados e medrosos', ''),
    ('o sujeito da prefeitura chegara com o talão de recibos', 'o cobrador da prefeitura chegara com o recibo', ''),
    ('empregava-as fora de propósito', 'empregava-as fora do propósito', ''),
    ('que apodrecia, os dois juazeiros', 'que apodrecia, os juazeiros', ''),
    ('os dois meninos na frente', 'os meninos à frente', ''),
    ('Não poderiam voltar a ser', 'Não poderia voltar a ser', ''),
    ('uma saudade grande', 'uma grande saudade', ''),
    ('montes baixos, cascalho', 'montes baixos, cascalhos', ''),
]

# erros de 1947 que o texto já não traz (ali vale a lição de 1938, que a edição moderna confirma)
ERROS_ANTERIORES = [
    ('Baleia', 'saiu depois sem destino, ao pulos', 'aos pulos'),
    ('Fuga', 'Os animais estava mortos', 'Os animais estavam mortos'),
    ('Fuga', 'o pequeno teria uma guarda-sol', 'um guarda-sol'),
]

TRADICAO_EXTRA = [(x['cap'], x['de'], x['para']) for x in _M['itens']]
