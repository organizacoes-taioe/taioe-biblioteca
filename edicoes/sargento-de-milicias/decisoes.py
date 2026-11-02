"""Memórias de um Sargento de Milícias — decisões editoriais (EM ANDAMENTO: ver FALTA.md).

EMENDAS: intervenções no texto-base, na grafia de 1854–55: (tipo, trecho, troca)
  'erro'    erro tipográfico evidente da edição de 1854–55
  'ocr'     erro dos OCRs; o impresso traz a forma certa (conferido no fac-símile)
  'revisao' lição de 1854–55 conferida no fac-símile que o confronto perdeu
AJUSTES: depois da modernização, em tokens separados por espaço: (tipo, antes, de, para, depois)
MANUAL: grafia final de palavras que a edição de referência não resolve
TITULOS: os títulos dos capítulos (config.TITULOS), na grafia de hoje
"""
import importlib.util
import os

_spec = importlib.util.spec_from_file_location('sm_config', os.path.join(os.path.dirname(__file__), 'config.py'))
_cfg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cfg)
TITULOS = dict(_cfg.TITULOS)

EMENDAS = [
    # leituras dos OCRs que o voto não corrigiu, conferidas no fac-símile (pranchas de 02/11, pontos 1–20)
    ('ocr', 'um sem numero do pontos', 'um sem numero de pontos'),
    ('ocr', 'certa Maria do hortaliça', 'certa Maria da hortaliça'),
    ('ocr', 'foi a honrai', 'foi a honra!'),
    ('ocr', 'arrependida doudicesde rapariga', 'arrependida..... doudices de rapariga'),
    ('ocr', 'e acahe-se tudo', 'e acabe-se tudo'),
    # pontos 41–62
    ('ocr', 'habitada por unia', 'habitada por uma'),
    ('ocr', 'talvez para ã cadê,', 'talvez para a cadêa...'),
    ('ocr', 'os industriosos ]', 'os industriosos!'),
    ('ocr', 'meirinho!.;. Nada', 'meirinho!... Nada'),
    # pontos 63–72
    ('ocr', 'eimaginouqueopequeno ajleria', 'e imaginou que o pequeno a teria'),
    ('ocr', 'Ciganos. Tinhãoesses meninos', 'Ciganos. Tinhão esses meninos'),
    # palavras que só os OCRs têm (relatorios/modernas.tsv), de correção evidente; a moderna arbitra
    ('ocr', 'eslevlado', 'este lado'),
    ('ocr', 'iembrasse', 'lembrasse'),
    ('ocr', 'com prelenções de', 'com pretenções de'),
    ('ocr', 'suas prelenções ou', 'suas pretenções ou'),
    ('ocr', 'mpito', 'muito'),
    ('ocr', 'imniunda', 'immunda'),
]

AJUSTES = []

MANUAL = {
    # formas de 1854 que a moderna, no mesmo ponto, não alinha 1:1
    'dansa': 'dança', 'dansão': 'dançam', 'dansavão': 'dançavam', "fizerão-n'a": 'fizeram-na', 'mudavão-se': 'mudavam-se',
    # resíduo evidente de OCR (relatorios/vocabulario.tsv: palavras que nenhuma edição moderna tem); a moderna arbitra
    'Leopardo': 'Leonardo', 'Leonardo-Pataça': 'Leonardo-Pataca', 'Jesé': 'José', 'Ob': 'Oh', 'abaridonado': 'abandonado',
    'ainigo': 'amigo', 'appareeer': 'aparecer', 'aqnellas': 'aquelas', 'assumplo': 'assunto', 'comsSgo': 'consigo',
    'conliverão-se': 'contiveram-se', 'consa': 'coisa', 'consas': 'coisas', 'digainos': 'digamos', 'ejla': 'ela',
    'emfini': 'enfim', 'eseravo': 'escravo', 'finalmgnte': 'finalmente', 'gue': 'que', 'hayia': 'havia',
    'incomniodava': 'incomodava', 'jue': 'que', 'mesino': 'mesmo', 'pelQ': 'pelo', 'possivei': 'possível',
    'prometlia': 'prometia', 'qfie': 'que', 'qjue': 'que', 'sugeilinho': 'sujeitinho', 'triumpbo': 'triunfo',
    'typq': 'tipo', 'utn': 'um', 'vizihança': 'vizinhança',
}
