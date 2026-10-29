"""Triste Fim de Policarpo Quaresma — texto da página «Sobre esta edição»."""

COMENTARIO = '''Triste Fim de Policarpo Quaresma — Lima Barreto
   Gerado por ferramentas/texto.py a partir de edicoes/policarpo-quaresma/. Não edite à mão:
   corrija as decisões em edicoes/policarpo-quaresma/ e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso;
     - «## Capítulo N — título» abre cada capítulo, e «{§ P.c}» marca o seu primeiro parágrafo
       (só para o site dividir as páginas; não aparece no texto).'''

APRESENTACAO = '''**Texto-base.** Este texto reproduz a primeira edição em livro de _Triste Fim de Policarpo Quaresma_ (Rio de Janeiro, Typ. «Revista dos Tribunaes», 1915), a única publicada em vida do autor, morto em 1922. O romance tinha saído antes em folhetim no _Jornal do Commercio_, de agosto a outubro de 1911; o volume de 1915 traz depois dele sete contos, que não entram aqui. A data no fim do romance («Todos os Santos (Rio de Janeiro), janeiro — março de 1911») é a do livro.

**Como foi estabelecido.** Foram confrontadas palavra por palavra três leituras da edição de 1915, feitas sobre três exemplares diferentes: a transcrição do Projeto Gutenberg (2022, sobre as imagens do exemplar da Biblioteca Nacional), o reconhecimento automático (OCR) do exemplar da Universidade de Princeton, digitalizado pelo Google, e um OCR novo, feito para esta edição, do exemplar da Brasiliana USP. Onde as três divergiam, valeu a maioria; os pontos em que a transcrição do Gutenberg ficava em minoria, os que não tinham maioria e os que podiam esconder um erro de palavra foram conferidos um a um nas imagens do livro: cerca de setecentos pontos. Assim se corrigiram várias leituras da transcrição («terríveis provas», e não «terríveis armas»; «um lento e seguido trabalho», e não «um lenço»; «a coroa na cabeça», e não «a corda»; «nem nas leis», e não «nem mas leis») e se recuperaram palavras e sinais que ela tinha perdido. As edições modernas gratuitas (a da Biblioteca Virtual do Estudante Brasileiro, da USP, e a do Wikisource, as duas da linhagem da edição da Ática) serviram só para a grafia: elas escrevem as horas por extenso, mudam a pontuação e emendam o texto em vários pontos; aqui ficou o de 1915.

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1915: letras trocadas ou repetidas («sinceriddae», «inquidade», «musclos», «Mas quem quem havia»), nomes estropiados («Boungainville», «Warnhagen», «Fustel de Conlangos»), palavras trocadas que a frase não admite («salvar da norte», «para tantas pesos», «Quaresma o não pia», «Quaresma passavam» por «Quando passavam», emenda feita à mão no próprio exemplar da Brasiliana) e a pontuação evidentemente errada (ponto antes de minúscula, vírgula antes de maiúscula). A lista completa vem abaixo. Ficaram as formas do autor que podem ser intencionais ou que não têm correção segura («lhe sabiam a causa», «como se a Bíblia estivesse sido criada», «os menenanan», «prescrutador», «o alcunha»).

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990, na forma brasileira: _elle_ → ele, _Polycarpo_ → Policarpo, _sub-secretario_ → subsecretário, _idéa_ → ideia, _Socego_ → Sossego. As formas antigas de palavras que continuam em uso passaram à forma atual (_cousa_ → coisa, _dous_ → dois, _logar_ → lugar, _cincoenta_ → cinquenta, _divan_ → divã), e as contrações da fala perderam o apóstrofo, como hoje se escreve (_p'ra_ → pra), salvo nos versos, onde a elisão conta na medida. O vocabulário e as construções do autor ficaram como estão: a colocação dos pronomes, as palavras estrangeiras (_pince-nez_, _bibelot_, _cavaignac_, _toilette_), a fala das personagens («É sô coroné!», «Hom-brôô... ármas!»), os números das horas («às 4 e 15»), a pontuação, as aspas angulares, os itálicos e as abreviaturas da época (_S. Januário_, _V. Ex._, _D. Adelaide_).

**Divisão.** O romance tem três partes, cada uma com cinco capítulos numerados e com título, como em 1915; cada capítulo é uma página desta biblioteca. A dedicatória e a epígrafe de Renan abrem a primeira parte. A carta de Quaresma à irmã termina, em 1915, com uma linha de pontos, que foi mantida.'''

BASE = 'Edição de 1915'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1915 corrigidos',
              'explica': 'Grafia de 1915 nas duas colunas; ¶ marca o começo de um parágrafo.'},
}

FONTES = [
    {'nome': 'Fac-símile da 1ª edição, 1915, exemplar da Brasiliana USP', 'url': 'https://digital.bbm.usp.br/handle/bbm/4361',
     'nota': 'lido por um OCR novo (Tesseract); as imagens decidiram as dúvidas'},
    {'nome': 'Fac-símile da 1ª edição, 1915, exemplar da Universidade de Princeton (Wikimedia Commons)',
     'url': 'https://commons.wikimedia.org/wiki/File:Triste_fim_de_Polycarpo_Quaresma.djvu',
     'nota': 'digitalização do Google pela HathiTrust; o OCR que vem no arquivo foi a segunda leitura'},
    {'nome': 'Projeto Gutenberg, nº 67535', 'url': 'https://www.gutenberg.org/ebooks/67535',
     'nota': 'transcrição da 1ª edição (2022), sobre as imagens do exemplar da Biblioteca Nacional'},
    {'nome': 'Biblioteca Virtual do Estudante Brasileiro (Escola do Futuro, USP)',
     'url': 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/lima-barreto/policarpo-quaresma.pdf',
     'nota': 'texto moderno, da 17ª edição da Ática; referência para a ortografia'},
    {'nome': 'Wikisource em português', 'url': 'https://pt.wikisource.org/wiki/Triste_Fim_de_Policarpo_Quaresma',
     'nota': 'texto moderno da mesma linhagem; referência para a ortografia'},
]

MANTIDAS = []

# erros de 1915 que a transcrição do Gutenberg já traz corrigidos (conferidos no fac-símile):
# (lugar, 1915, corrigido)
ERROS_ANTERIORES = [
    ('Epígrafe', 'les qualités deviennent des défauts. si bien', 'les qualités deviennent des défauts, si bien'),
    ('Epígrafe', "l'egoisme", "l'égoïsme"),
    ('Epígrafe', 'Marc-Auréle', 'Marc-Aurèle'),
    ('I, cap. I', 'Janta já? ¶ Ainda não', 'Janta já? ¶ — Ainda não'),
    ('I, cap. I', 'ao contrario. o major', 'ao contrario, o major'),
    ('I, cap. I', 'indifferentes Pequenas talvez', 'indifferentes. Pequenas talvez'),
    ('I, cap. I', 'e se se encontravam', 'e se encontravam'),
    ('I, cap. III', 'jogava-se em em silencio', 'jogava-se em silencio'),
    ('I, cap. IV', 'censurou o Arsenal, ¶ Que manhã', 'censurou o Arsenal. ¶ Que manhã'),
    ('I, cap. IV', 'como elles. faça', 'como elles, faça'),
    ('I, cap. V', 'Por fim. achou', 'Por fim, achou'),
    ('I, cap. V', 'Namorar. escrever cartinhas. fazer acenos', 'Namorar, escrever cartinhas, fazer acenos'),
    ('II, cap. I', 'de outros tempos, Indagou', 'de outros tempos. Indagou'),
    ('II, cap. I', 'mais remediados, Desde já', 'mais remediados. Desde já'),
    ('II, cap. I', 'com ingenuidade Quaresma, ¶ Antonino', 'com ingenuidade Quaresma. ¶ Antonino'),
    ('II, cap. II', 'graças aos empenho do pai', 'graças aos empenhos do pai'),
    ('II, cap. II', 'A Ismenia ooi aquella', 'A Ismenia foi aquella'),
    ('II, cap. III', 'varrendo a testada, ¶ Apezar', 'varrendo a testada. ¶ Apezar'),
    ('II, cap. III', 'difficilmente. e solemnemente', 'difficilmente, e solemnemente'),
    ('II, cap. III', 'uma hora, um pomar', 'uma horta, um pomar'),
    ('II, cap. IV', 'batalha sem treguas, Se', 'batalha sem treguas. Se'),
    ('II, cap. V', 'Deodoro nunca sôbe o que', 'Deodoro nunca soube o que'),
    ('II, cap. V', 'o Almirante, não. Quaresma passavam', 'o Almirante, não. Quando passavam'),
    ('II, cap. V', 'os pequenos. os alferes', 'os pequenos, os alferes'),
    ('III, cap. II', 'Quaresma o não pia.', 'Quaresma o não via.'),
    ('III, cap. IV', 'separados pela bahia. agora', 'separados pela bahia, agora'),
    ('III, cap. IV', 'Na rua. Genelicio', 'Na rua, Genelicio'),
    ('III, cap. V', 'Mas quem quem havia de ser', 'Mas quem havia de ser'),
]
