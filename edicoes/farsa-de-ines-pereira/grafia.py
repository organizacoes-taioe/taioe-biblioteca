"""Farsa de Inês Pereira: a grafia de hoje das palavras de 1834 que as regras de modernizar.py não
resolvem, ou resolvem errado. GRAFIA: forma de 1834 (minúscula) → forma de hoje. MANTER: formas antigas
que ficam como estão (a forma da palavra, regra das Barcas e de Os Lusíadas). As linhas em castelhano
(falas do Ermitão, cantigas) não passam pela modernização (CASTELHANO, em modernizar.py)."""

GRAFIA = {
    # grafia
    'he': 'é', 'hum': 'um', 'huma': 'ũa', 'húa': 'ũa', 'hũa': 'ũa', 'hua': 'ũa', 'humas': 'ũas',
    'huns': 'uns', 'algua': 'algũa', 'deos': 'Deus', 'judeos': 'Judeus', 'ceos': 'céus', 'veos': 'véus',
    'mao': 'mau', 'maos': 'maus', 'inez': 'Inês', 'inezinha': 'Inesinha', 'ella': 'ela', 'elle': 'ele',
    'chórão': 'choram', 'ensinárão': 'ensinaram', 'pharaó': 'Faraó', 'montez': 'montês', 'arrea': 'arrea',
    'abraçae': 'abraçai', 'aguardae': 'aguardai', 'buscae': 'buscai', 'casae': 'casai', 'cerrae': 'cerrai',
    'contae': 'contai', 'dae': 'dai', 'deitae': 'deitai', 'esforçae': 'esforçai', 'esperae': 'esperai',
    'fartae': 'fartai', 'ficae': 'ficai', 'lavrae': 'lavrai', 'leixae': 'leixai', 'mostrae': 'mostrai',
    'namorae': 'namorai', 'olhae': 'olhai', 'perdoae': 'perdoai', 'tomae': 'tomai', 'vae': 'vai',
    'pae': 'pai', 'pardaes': 'pardais', 'cascaes': 'Cascais', 'sae': 'sai', 'descalsae': 'descalçai',
    'affeitado': 'afeitado', 'agua': 'água', 'ahi': 'aí', 'aindaque': 'ainda que', 'anginho': 'anjinho',
    'canceira': 'canseira', 'candea': 'candeia', 'candeiasinha': 'candeiazinha', 'cantadella': 'cantadela',
    'capello': 'capelo', 'castella': 'Castela', 'cavalleirão': 'cavaleirão', 'comnosco': 'conosco',
    'comtigo': 'contigo', 'comvosco': 'convosco', 'couse': 'couce', 'damno': 'dano', 'farça': 'farsa',
    'geito': 'jeito', 'geitar': 'jeitar', 'grãa': 'Grã', 'irmãa': 'irmã', 'irman': 'irmã', 'hade': 'há de',
    'hombro': 'ombro', 'hontem': 'ontem', 'oudivellas': 'Oudivelas', 'pardeos': 'Par Deus', 'pez': 'pês',
    'prizão': 'prisão', 'sahi': 'saí', 'sahirei': 'sairei', 'sobrescripto': 'sobrescrito', 'somno': 'sono',
    'spirito': 'Spírito', 'tejo': 'Tejo', 'cardial': 'Cardeal', 'elrei': 'el-Rei', 'eirei': 'el-Rei',
    'chamâ': 'chamá', 'badajoz': 'Badajoz', 'arzila': 'Arzila', 'trazi': 'trazia',
    # lições de 1562 de uma palavra só (as outras em montar.py)
    'danaso': 'Donaso', 'amanhan': 'amenhã', 'muchacho': 'mochacho', 'mochaço': 'mochacho',
    'catarrão': 'cadarrão', 'estrugirá': 'estrogirá', 'villãosinho': 'vilanzinho', 'tuberas': 'túbaras',
    'sanpisco': 'Sampisco', 'ceremonias': 'ceremônias', 'fragoa': 'frágoa',
}

MANTER = {
    'sam', 'assi', 'pera', 'cousa', 'cousas', 'dous', 'mi', 'abraham', 'canaam', 'jacob', 'anojada',
    'anojarei', 'anoje', 'aosadas', 'aporfieis', 'aquenta', 'assolverei', 'assolverás', 'atafoneiro',
    'atégora', 'avò', 'boamente', 'boleima', 'breviairo', 'brigoso', 'bugia', 'cajo', 'camarinhas',
    'canaval', 'casade', 'caslim', 'castilla', 'chantou', 'chentadas', 'choute', 'chuiva', 'cousinha',
    'dello', 'descancarado', 'desenfadar', 'desque', 'dixestes', 'doudo', 'empacho', 'empuxão', 'en',
    'quieren', 'enfadamento', 'escarnefuchão', 'esfandangado', 'esgravatá', 'esperade', 'espojar',
    'essora', 'estoutro', 'fadem', 'fermosura', 'foes', 'folhinas', 'folão', 'friúra', 'gramateca',
    'guaiado', 'havedes', 'hereos', 'home', 'lastimeiros', 'leixa', 'leixais', 'leixar', 'leixarei',
    'leixemos', 'leixo', 'leixou', 'levades', 'lianor', 'manim', 'marichal', 'maridinho', 'maviosa',
    'mesura', 'migada', 'morgado', 'muitembora', 'obrou', 'oiço', 'olival', 'outrem', 'pardelhas',
    'parvoíce', 'pea', 'peas', 'peitogueira', 'pentein', 'pereli', 'perla', 'perlas', 'perpinhão', 'poer',
    'precatares', 'prenhe', 'prouguesse', 'prouvesse', 'pujemos', 'rabizarão', 'rebentinha', 'releva',
    'requesta', 'retouço', 'revolvedor', 'riba', 'safeo', 'sarnosa', 'sarra', 'senhos', 'sesudo',
    'sinalzinho', 'siquaes', 'sobejava', 'sopeada', 'sotrancão', 'tamanhouço', 'tavanés', 'tavila',
    'tomade', 'toutiço', 'trosquiada', 'unheiro', 'vasco', 'vendima', 'vilha', 'voda', 'vodas', 'zote',
    'mercea', 'canteu', 'corregê', 'noss', 'guar', 'far', 'mir', 'heis', 'l', 'raiso', 'rigo',
    'stou', 'stae', 'stava', 'va', 'sahe', 'prosegue', 'ermita', 'mochacho', 'aguçosa', 'alfaqui',
    'baboso', 'cantiguinha', 'carapatento',
}
