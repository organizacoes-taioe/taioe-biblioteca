"""Triste Fim de Policarpo Quaresma — decisões editoriais.

EMENDAS: intervenções no texto-base, na grafia de 1915: (tipo, trecho, troca)
  'erro'    erro tipográfico evidente da edição de 1915
  'ocr'     erro das transcrições; o impresso de 1915 traz a forma certa (conferido no fac-símile)
  'revisao' lição de 1915 conferida no fac-símile que o confronto perdeu
AJUSTES: depois da modernização, em tokens separados por espaço: (tipo, antes, de, para, depois)
MANUAL: grafia final de palavras que as edições de referência não resolvem
TITULOS: os títulos dos capítulos (config.TITULOS), na grafia de hoje
corrigir: ajustes de composição sobre o texto pronto
Os pontos conferidos no fac-símile que o voto decide ficam em conferencia.json (ver config.rever).
"""
import importlib.util
import os
import re

_spec = importlib.util.spec_from_file_location('pq_config', os.path.join(os.path.dirname(__file__), 'config.py'))
_cfg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cfg)
TITULOS = dict(_cfg.TITULOS)

EMENDAS = [
    # erros do Gutenberg que o voto não corrigiu (um dos OCRs erra junto), conferidos no fac-símile
    ('ocr', "Tinha ainda a corda na cabeça", "Tinha ainda a corôa na cabeça"),
    ('ocr', "nem mas leis", "nem nas leis"),
    ('ocr', "portar-se mal em fazer-lhe", "portar-se mal era fazer-lhe"),
    ('ocr', "de muitos, recumava", "de muitos, reçumava"),
    ('ocr', "não pemittiriam", "não permittiriam"),
    ('ocr', "suas irmães", "suas irmãs"),
    ('ocr', "sua educacão", "sua educação"),
    ('ocr', "commando: Hom-brõo", "commando: Hom-brôô"),
    ('ocr', "para ella, pão era", "para ella, não era"),
    ('ocr', "por falta da", "por falta do"),
    ('ocr', "que se vão casar, De resto", "que se vão casar. De resto"),
    ('ocr', "rezava o papel, O Sr.", "rezava o papel, o Sr."),
    ('ocr', "Era uma moca", "Era uma moça"),
    ('ocr', "leva de desgraça a sahir", "leva de desgraçados a sahir"),
    # erros tipográficos evidentes da edição de 1915 (conferidos no fac-símile)
    ('erro', "Cook, Boungainville", "Cook, Bougainville"),
    ('erro', "Handelmann (Geschitchte von", "Handelmann (Geschichte von"),
    ('erro', "Southey, Warnhagen", "Southey, Varnhagen"),
    ('erro', "Hans Stade,", "Hans Staden,"),
    ('erro', "humilhante contigencia", "humilhante contingencia"),
    ('erro', "lhe inflingir", "lhe infligir"),
    ('erro', "com outras materiaes", "com outros materiaes"),
    ('erro', "não se incommode, Não é", "não se incommode. Não é"),
    ('erro', "arvores fruticferas", "arvores fructiferas"),
    ('erro', "arvores fructiferas. um capoeirão", "arvores fructiferas, um capoeirão"),
    ('erro', "instrumentos metereologicos", "instrumentos meteorologicos"),
    ('erro', "nossos musclos", "nossos musculos"),
    ('erro', "charfurdar-se", "chafurdar-se"),
    ('erro', "terriveis hymhopteros", "terriveis hymenopteros"),
    ('erro', "boa fé, sinceriddae", "boa fé, sinceridade"),
    ('erro', "Uma inquidade", "Uma iniquidade"),
    ('erro', "longo e tristes dias", "longos e tristes dias"),
    ('erro', "faz um reduzido", "faz uso reduzido"),
    ('erro', "transcedente medicina", "transcendente medicina"),
    ('erro', "Fustel de Conlangos", "Fustel de Coulanges"),
    ('erro', "para tantas pesos", "para tantas pessoas"),
    ('erro', "e as sua unhas", "e as suas unhas"),
    ('erro', "salvar da norte", "salvar da morte"),
    ('erro', "levantamento moral a intellectual", "levantamento moral e intellectual"),
    ('erro', "precisavam desse processos", "precisavam desses processos"),
    ('erro', "examinando o soldado, Era branco", "examinando o soldado. Era branco"),
    ('erro', "da população. inteira", "da população inteira"),
    ('erro', "Quaresma viu caixão do coche", "Quaresma viu o caixão do coche"),
    ('erro', "com o o seu terno", "com o seu terno"),
    ('erro', "desesperada a a nossa roça", "desesperada a nossa roça"),
    ('erro', "a irmã da Quaresma a perguntar", "a irmã de Quaresma a perguntar"),
    ('erro', "Ismenia, cumprimentado-a", "Ismenia, cumprimentando-a"),
    ('erro', "paixão do foklorista", "paixão do folklorista"),
    ('erro', "em um polygno", "em um polygono"),
    ('erro', "todas aquelles que", "todos aquelles que"),
    ('erro', "obedecia a a uma", "obedecia a uma"),
    ('erro', "bem encaminhando e", "bem encaminhado e"),
]

AJUSTES = [
    # o alinhamento com a edição moderna (Ática) trouxe a leitura dela; 1915 tem «em desordem»
    ('grafia', 'enormes bigodes', 'en desorden', 'em desordem', ';'),
    # nos versos, as elisões ficam como em 1915 (contam na medida)
    ('grafia', "murundu ' /", 'Pra', "P'ra", 'cumê sinhozinho'),
    ('grafia', 'sinhozinho /', 'Com', "C'um", 'bucado de angu'),
    # «fealdade.»» em 1915; o Gutenberg põe o ponto depois das aspas, e o voto deixava os dois
    ('grafia', 'e fealdade . »', '.', '', '¶'),
    # pontos que o voto deslocou (conferidos no fac-símile): «Europa!»», «doutor. ¶ D. Adelaide»
    ('grafia', 'ir à Europa', '»', '! »', 'O major'),
    ('grafia', 'observou o doutor', '¶ .', '. ¶', 'D . Adelaide'),
]

MANUAL = {
    # formas antigas de palavras atuais (as edições de referência não dão o par)
    'comnosco': 'conosco', 'regimen': 'regímen', 'divan': 'divã', 'divans': 'divãs', 'longiquo': 'longínquo',
    'chromo': 'cromo', 'homœpathia': 'homeopatia', 'dolman': 'dólmã', 'talisman': 'talismã', 'Styge': 'Estige',
    'specimens': 'espécimens', 'afflux': 'afluxo', 'Aquidaban': 'Aquidabã', 'mandigueiro': 'mandingueiro',
    'Evangelios': 'Evangelhos', 'cataclysma': 'cataclisma', 'parallepipedo': 'paralelepípedo', 'Cordova': 'Córdova',
    'Christovam': 'Cristóvão', 'Oedipo-Rei': 'Édipo-Rei', 'Shakspeare': 'Shakespeare', 'presumpçosos': 'presunçosos',
    'bebedo': 'bêbedo', 'aboboda': 'abóbada', 'lugubre': 'lúgubre', 'sentiamo-lhe': 'sentíamo-lhe', 'tel-o': 'tê-lo',
    'pagal-as': 'pagá-las', 'Approximavam-se': 'Aproximavam-se', 'reçumava': 'ressumava', 'enleiado': 'enleado',
    'joven': 'jovem', 'içal-a': 'içá-la', 'folklorista': 'folclorista', 'polygono': 'polígono',
    'idéas': 'ideias', 'ella': 'ela', 'janella': 'janela', 'nacionaes': 'nacionais', 'portugueza': 'portuguesa',
    'cincoenta': 'cinquenta', 'activa': 'ativa', 'agua': 'água', 'Colonia': 'Colônia', 'nellas': 'nelas',
    'proximo': 'próximo', 'cadaveres': 'cadáveres', 'poetico-musical': 'poético-musical', 'Meier': 'Méier', 'Meyer': 'Méier',
    'Jacob': 'Jacó', 'bonet': 'boné', 'pret': 'pré', "chamaram-n'o": 'chamaram-no',
    # contrações da fala sem o apóstrofo, como hoje (p'ra -> pra), como as edições modernas já fazem
    'ahi': 'aí', 'Ahi': 'Aí',                      # a edição moderna dá às vezes «ai»
    "p'ra": 'pra', "P'ra": 'Pra', "p'r'o": 'pro',
    # palavras que ficam como estão (nomes, estrangeirismos, a fala das personagens)
    'Paysandon': 'Paysandon', 'menenanan': 'menenanan', 'hom-broôô': 'hom-broôô', 'Hom-brôô': 'Hom-brôô',
    'Vó': 'Vó', 'crôtando': 'crôtando', 'ármas': 'ármas', 'Hom': 'Hom', 'brôoo': 'brôoo', 'Mei-ããã': 'Mei-ããã', 'Mei-ãã': 'Mei-ãã', 'cavaignac': 'cavaignac', 'khan': 'khan',
}


# locuções que a edição moderna (de antes do Acordo) hifeniza e que o Acordo de 1990 escreve
# separadas, como 1915; e enganos de digitalização dela que o alinhamento trouxe
SEPARAR = {
    'chapéu-de-sol': 'chapéu de sol', 'ajudante-de-ordens': 'ajudante de ordens',
    'ajudantes-de-ordens': 'ajudantes de ordens', 'dona-de-casa': 'dona de casa', 'mestre-de-obras': 'mestre de obras',
    'Capitão-de-fragata': 'Capitão de Fragata', 'pó-de-arroz': 'pó de arroz', 'boca-de-sino': 'boca de sino',
    'carvão-de-pedra': 'carvão de pedra', 'pau-a-pique': 'pau a pique', 'autos-de-fé': 'autos de fé',
    'bicos-de-gás': 'bicos de gás', 'língua-de-vaca': 'língua de vaca', 'tão-somente': 'tão somente',
    'Urubu-de-Baixo': 'Urubu de Baixo', 'trinta-Réis': 'trinta réis',
    'azulferrete': 'azul-ferrete', 'beijos-defrade': 'beijos-de-frade', 'cipóchumbo': 'cipó-chumbo',
}


def corrigir(out, flags):
    """Ajustes de composição sobre o texto pronto: «n' «O Paiz»» numa palavra só, como em 1915
    (n'«O País»); números de milhar partidos («3. 000»); o ordinal à brasileira («1º»)."""
    novo, nf = [], []
    i = 0
    while i < len(out):
        t = out[i]
        if t in SEPARAR:
            partes = SEPARAR[t].split(' ')
            ital = flags[i] or t == 'trinta-Réis'          # «_trinta réis_», em itálico em 1915
            novo += partes; nf += [ital] * len(partes); i += 1; continue
        if t == 'nhãnhã' and novo[-2:] == ['vê', ',']:   # «Vó vê, nhã nhã...»; adiante, «nhãnhã»
            novo += ['nhã', 'nhã']; nf += [flags[i]] * 2; i += 1; continue
        if t == 'n' and out[i + 1:i + 4] == ["'", '«', 'O']:
            novo.append("n'«O"); nf.append(flags[i]); i += 4; continue
        if t.isdigit() and out[i + 1:i + 2] == ['.'] and i + 2 < len(out) and re.fullmatch(r'\d{3}', out[i + 2]):
            novo.append(t + '.' + out[i + 2]); nf.append(False); i += 3; continue
        if t == "'" and novo and novo[-1][-1:].isalpha() and out[i + 1:i + 2] in (['/'], ['»'], ['¶']):
            novo[-1] += "'"; i += 1; continue                 # «tutu'», «angu'»: a elisão da fala, colada
        if t.isdigit() and out[i + 1:i + 2] in (['°'], ['º']):
            novo.append(t + 'º'); nf.append(False); i += 2; continue
        novo.append(t); nf.append(flags[i]); i += 1
    return novo, nf

