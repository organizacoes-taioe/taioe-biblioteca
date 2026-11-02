"""Amor de Perdição — decisões editoriais.

EMENDAS: intervenções no texto-base, na grafia da 1ª edição: (tipo, trecho, troca)
  'erro'    erro tipográfico evidente da 1ª edição
  'ocr'     erro da transcrição digital; a 1ª edição traz a forma correta (conferido no fac-símile)
AJUSTES: depois da modernização, em tokens separados por espaço: (tipo, antes, de, para, depois)
MANUAL: grafia final de palavras que as edições de referência não resolvem
"""

EMENDAS = [
    # leituras da camada de texto do Commons que as imagens desmentem
    ('ocr', 'deixou aneedotas', 'deixou anecdotas'),
    ('ocr', "fidalgo de Castrod'Aire", "fidalgo de Castro-d'Aire"),
    # erros da transcrição (o Wikisource copiou o Gutenberg); todos conferidos no fac-símile de 1862
    # (Commons, 2026-11-02), que traz a forma correta. Lições da 1ª edição conferidas e mantidas:
    # «sasões», «promenores», «dezoitos annos» (p. 247; «dezoito» na p. 243), «estorturoso», «su villão»
    ('ocr', 'Chegou o ferrador a Monehique', 'Chegou o ferrador a Monchique'),
    ('ocr', 'fidalgo de Gastro-d\'Aire', 'fidalgo de Castro-d\'Aire'),
    ('ocr', 'acerescentou o desembargador', 'accrescentou o desembargador'),
    ('ocr', 'imaginou desvairadaraente', 'imaginou desvairadamente'),
    ('ocr', 'mãos convuísamente enlaçadas', 'mãos convulsamente enlaçadas'),
    ('ocr', 'e egualmenle nobre', 'e egualmente nobre'),
    ('ocr', 'era excellenle flautista', 'era excellente flautista'),
    ('ocr', 'nem sequer eslava sentida', 'nem sequer estava sentida'),
    ('ocr', 'por fcar doida', 'por ficar doida'),
    ('ocr', 'interrogou sua fllha', 'interrogou sua filha'),
    ('ocr', 'em tão hoa hora', 'em tão boa hora'),
    ('ocr', "n'nma hora de má digestão", "n'uma hora de má digestão"),
    ('ocr', 'em quanto naaa póde esperar', 'em quanto nada póde esperar'),
    ('ocr', 'mandar-lhe o presenle de', 'mandar-lhe o presente de'),
    ('ocr', 'a mão de urn homem', 'a mão de um homem'),
    ('ocr', 'aos olhas de Simão', 'aos olhos de Simão'),
    ('ocr', 'templo, onde cabira', 'templo, onde cahira'),
    ('ocr', 'Erguei-se Simão Botelho', 'Ergueu-se Simão Botelho'),
    ('ocr', 'agradecido lhe estou-disse Simão', 'agradecido lhe estou — disse Simão'),
    ('ocr', 'Monchique? — pergutou Simão', 'Monchique? — perguntou Simão'),
]

AJUSTES = []

MANUAL = {
    'ILLUSTRISSIMO': 'ILUSTRÍSSIMO', 'EXCELENTISSIMO': 'EXCELENTÍSSIMO', 'Castello': 'Castelo',
    'cincoenta': 'cinquenta', 'Cincoenta': 'Cinquenta', 'Vianna': 'Viana', 'Visivel': 'Visível',
    'ha': 'há', 'á': 'à', 'Á': 'À', 'approva': 'aprova', 'bebadas': 'bêbadas', 'biscoutos': 'biscoitos',
    'canonisada': 'canonizada', 'ceremonia': 'cerimônia', 'froixo': 'frouxo', 'froixa': 'frouxa',
    'roixo': 'roxo', 'roixos': 'roxos', 'roixa': 'roxa', 'comsigo': 'consigo', 'crivel': 'crível',
    "dal-o": 'dá-lo', "ouvil-a": 'ouvi-la', "destinar-lh'a": 'destinar-lha', "dir-t'a-hei": 'dir-ta-ei',
    'aceital-o-ias': 'aceitá-lo-ias', 'desnocára': 'desnocara', 'desplicencia': 'displicência',
    'dessocêgo': 'dessossego', 'faxa': 'faixa', 'galans': 'galãs', 'immoveis': 'imóveis',
    'infanteria': 'infantaria', 'instillam': 'instilam', 'logar': 'lugar', 'occultamente': 'ocultamente',
    'oppozera': 'opusera', 'presumpçoso': 'presunçoso', 'presumpções': 'presunções', 'recahisse': 'recaísse',
    'redempção': 'redenção', 'sasões': 'sazões', 'spasmo': 'espasmo', 'subscriptado': 'subscritado',
    'vehemencia': 'veemência', 'entre-vira': 'entrevira', 'mal-querença': 'malquerença',
    'escondrijo': 'esconderijo', 'lisongeavam-o': 'lisonjeavam-o', 'dous': 'dois', "p'ra": "p'ra",
    'Thereza': 'Teresa', 'Pelagio': 'Pelágio', 'Morrerá': 'Morrerá',
    "Castro-d'Aire": 'Castro Daire', "d'Aire": 'Daire',
    # hífens que a BVEB (OCR) perdeu: a forma de hoje
    'Ave-Marias': 'Ave-Marias', 'Diffamal-os': 'Difamá-los', 'Dizia-lhe': 'Dizia-lhe', 'Eis-me': 'Eis-me',
    'Guardou-me': 'Guardou-me', 'Pediu-lhe': 'Pediu-lhe', 'Tire-a': 'Tire-a', 'conseguil-o': 'consegui-lo',
    'deliciava-se': 'deliciava-se', 'demoral-a': 'demorá-la', 'escapar-se': 'escapar-se', 'espancal-a': 'espancá-la',
    'ex-corregedor': 'ex-corregedor', 'mandam-me': 'mandam-me', 'pedindo-lhe': 'pedindo-lhe', 'tendo-lhe': 'tendo-lhe',
    'tenho-lhe': 'tenho-lhe', 'viu-a': 'viu-a', 'quer-me': 'quer-me', 'estava-no': 'estava-no', 'entre-acto': 'entreato',
    'Mira-Molim': 'Miramolim', 'sobre-rolda': 'sobre-rolda',
    'loucura': 'loucura', 'suicidio': 'suicídio',
    'exigencias': 'exigências', 'camera': 'câmara', 'coixo': 'coxo',
}

# abreviaturas com letra sobrescrita impressas na linha (Ex.ª, Ill.mo, s.ª): o tokenizador as separa

SOBRESCRITAS = {
    'ª': None, 'º': None,                                   # depois de qualquer abreviatura
    'ta': {'S', 'St'}, 't': {'S'}, 'me': {'M'}, 'mo': {'Ex', 'Exc', 'ex', 'exc', 'Ill'}, 'or': {'D'}, 'ce': {'vm', 'Vm'},
    'as': {'ex', 'exc', 'Ex', 'Exc', 'C'}, 'os': {'ex', 'exc', 'Ex', 'Exc'},
}


def corrigir(out, flags):
    novo, nf = [], []
    i = 0
    while i < len(out):
        t = out[i]
        if (i + 2 < len(out) and out[i + 1] == '.' and t[:1].isalnum() and len(t) <= 4
                and out[i + 2] in SOBRESCRITAS
                and (SOBRESCRITAS[out[i + 2]] is None or t in SOBRESCRITAS[out[i + 2]])):
            novo.append(t + '.' + out[i + 2]); nf.append(flags[i])
            i += 3
            continue
        if t == "d'a":                                                   # leitura da BVEB (OCR) por «da»
            novo.append('da'); nf.append(flags[i])
            i += 1
            continue
        if t == 'Vila-Real':                                             # a cidade: Vila Real (a BVEB põe hífen)
            novo += ['Vila', 'Real']; nf += [flags[i]] * 2
            i += 1
            continue
        novo.append('...' if t == '..' else t); nf.append(flags[i])      # «!..» da 1ª edição
        i += 1
    return novo, nf
