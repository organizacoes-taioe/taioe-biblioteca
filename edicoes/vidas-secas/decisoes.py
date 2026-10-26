"""Vidas Secas — decisões editoriais sobre o texto estabelecido.

EMENDAS: (tipo, busca, troca) na grafia do texto-base (tokens separados como no texto).
  'revisao' — lição de 1947, conferida no fac-símile, que o confronto automático perdeu;
  'erro'    — erro tipográfico da edição de 1947, corrigido.
AJUSTES: (tipo, antes, de, para, depois) em tokens do texto já atualizado.
MANUAL: grafia atual de palavras que a edição de referência não resolve.
"""

EMENDAS = [
    # --- lições de 1947 conferidas no fac-símile (o OCR estava ilegível, ou a edição moderna lê outra coisa)
    ('revisao', 'elle queria dizer . E havia', 'elle queria dizer . ¶ E havia'),
    ('revisao', 'uma esteira . — Desafasta', 'uma esteira . ¶ — Desafasta'),
    ('revisao', 'pisar com força , Fabiano', 'pisar com força . Fabiano'),
    ('revisao', 'seguindo uma rez , esguelava-se demais', 'seguindo uma rez , êle se esgoelava de mais'),
    ('revisao', 'magoavam-nos em demasia', 'magoavam-no em demasia'),
    ('revisao', 'espinhaço curvo : — Quem', 'espinhaço curvo : ¶ — Quem'),
    ('revisao', 'metteu-os no aiol', 'metteu-os no aió'),
    # --- erros de 1947
    ('erro', 'o boca cheia', 'a boca cheia'),                         # também em 1938
]
# Os outros erros de 1947 («uma guarda-sol», «ao pulos», «Os animais estava mortos») não estão no
# texto, que ali segue 1938 e a edição moderna: vão listados em notas.ERROS_ANTERIORES.

AJUSTES = [
    # «por mor de», de «por amor de» (a edição moderna põe «mor»; a regra geral de grafia.FORMAS_ATUAIS,
    # feita para «a mor parte» do Machado, o trocaria por «maior»)
    ('grafia', '¶ Por', 'maior', 'mor', 'de uma peste'),
    ('grafia', 'gestos oblíquos .', 'A', 'À', 'tarde puxou'),         # 1938 A’, 1947 À; a edição moderna, «A»
    # «porque» das perguntas diretas e «porquê» final: «por que», «por quê», pela norma atual
    ('grafia', '', 'Porque', 'Por que', 'seria que seu Inácio'),
    ('grafia', '', 'Porque', 'Por que', 'tinham feito aquilo'),
    ('grafia', 'Então', 'porque', 'por que', 'um sem-vergonha desordeiro'),
    ('grafia', '', 'Porque', 'Por que', 'vinham bulir'),
    ('grafia', '', 'Porque', 'Por que', 'não tinham removido'),
    ('grafia', '', 'Porque', 'Por que', 'seria ?'),
    ('grafia', '', 'Porque', 'Por que', 'seria que aquele safado'),
    ('grafia', '', 'Porque', 'Por que', 'motivo o governo'),
    ('grafia', '', 'Porque', 'Por que', 'seria que o coração'),
    ('grafia', '', 'Porque', 'Por que', 'não haveriam de ser gente'),
    ('grafia', '', 'Porque', 'Por que', 'haveriam de ser sempre'),
    ('grafia', 'Não sabia', 'porquê', 'por quê', ', mas era'),
    ('grafia', 'bolandeira .', 'Porquê', 'Por quê', '? Só se era'),
    ('grafia', 'a ninguém .', 'Porquê', 'Por quê', '? Sufocava-se'),
]

MANUAL = {
    'sinha': 'sinha', 'Sinha': 'Sinha',            # a forma do autor (a edição moderna põe «sinhá»)
    'barahunas': 'baraúnas',
    'desgracas': 'desgraças',
    'tambem': 'também',
    'êle': 'ele',
    'Ás': 'Às', 'Às': 'Às',                         # 1947 imprime «As vezes», sem o acento na maiúscula
    # locuções que perderam o hífen no Acordo de 1990
    'pé-de-vento': 'pé de vento', 'à-toa': 'à toa', 'trinta-e-um': 'trinta e um',
}
