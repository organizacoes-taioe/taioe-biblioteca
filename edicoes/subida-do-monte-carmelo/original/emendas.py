# Emendas ao texto votado pelo montar.py, conferidas uma a uma na imagem do volume de 1929
# (recortes das linhas com recorte.py; ver LEIAME.md). Cada item: (texto votado, texto certo[, vezes]).
# O montar.py recusa a emenda que não bate o número de vezes, para nunca trocar no lugar errado.
# A acentuação de hoje (así, más, sí…) entra também aqui quando a regra automática não a alcança.

EMENDAS = {
    ('subida', 0): [
        ('Tcdi? la doctrina', 'Toda la doctrina'),
        ('segunlo pidiere', 'según lo pidiere'),
        ('| Quien yo bien me sabia,', '| Quien yo bien me sabía,'),
        ('| Quedeme, y olvídeme,', '| Quedeme, y olvideme,'),
        ('y purgacion suya a la union del Amado', 'y purgación suya a la unión del Amado'),
        ('conforme con su perecer', 'conforme con su parecer'),
        ('hacerlo ha m¿poco saber', 'hacerlo ha mi poco saber'),
        ('a io menos', 'a lo menos'),
        ('que la mia;', 'que la mía;'),
    ],
    ('subida', 1): [
        # títulos e versos
        ('qué sea npche oscura', 'qué sea noche oscura'),   # «npche» é erro do próprio volume (as duas leituras)
        ('| Sal i sin ser notada,»', '| Salí sin ser notada,'),
        # capítulos 1–5
        ('Quae conventio lucí ad tenebras?', 'Quae conventio luci ad tenebras?'),
        ('tenía en si el sabor', 'tenía en sí el sabor'),
        ('tendrá en si el verdadero maná', 'tendrá en sí el verdadero maná'),
        ('venga a tener en si esta ley', 'venga a tener en sí esta ley'),
        ('Sapientia enim hujus mundi stultitia es\' \'apud Deum', 'Sapientia enim hujus mundi stultitia est apud Deum'),
        ('ad vos clamito, ct vox', 'ad vos clamito, et vox'),
        ('Audite guía de rebus', 'Audite quia de rebus'),
        ('Melior cst f rucias meus', 'Melior est fructus meus'),
        ('Atended pequefluelos', 'Atended pequeñuelos'),
        ('diceles que adviertan', 'díceles que adviertan'),
        ('renuntiat ómnibus quae', 'renuntiat omnibus quae'),
        ('non potest mcus esse', 'non potest meus esse'),
        ('en otros exiraños gustos', 'en otros extraños gustos'),
        ('ni jue faltase jamás', 'ni que faltase jamás'),
        ('Esto tarnbicn es lo que', 'Esto también es lo que'),
        # capítulo 6
        ('capítulo U: Dúo mala fecit Populas meus: dereUquerunt fontem aquae vivae, et ¡oderunt',
         'capítulo II: Duo mala fecit Populus meus: dereliquerunt fontem aquae vivae, et foderunt'),
        ('Dejáronme a mi, que soy', 'Dejáronme a mí, que soy'),
        ('cavaron para si cisternas rotas, que no Queden tener agua (I).',
         'cavaron para sí cisternas rotas, que no pueden tener agua.'),
        ('sumere panem f\'diorum,', 'sumere panem filiorum,'),
        ('ctum daré canibus', 'ctum dare canibus'),
        ('Cum satiatus fueni,', 'Cum satiatus fuerit,'),
        ('quasi mare fcrvens', 'quasi mare fervens'),
        ('porcue, como comúnmente', 'porque, como comúnmente'),
        ('echándole lefia', 'echándole leña'),
        ('Declinaba ad dexteram', 'Declinabit ad dexteram'),
        # capítulo 7
        ('ct exarserunt sicut', 'et exarserunt sicut'),
        ('Rodeáronse de mi como', 'Rodeáronse de mí como'),
        ('encendiéronse contra mi,', 'encendiéronse contra mí,'),
        ('Defecit anima c/us', 'Defecit anima ejus'),
        ('Quantum g/ori/icavit se, et in deliciis ¡uit, tantum date Mi tormentum',
         'Quantum glorificavit se, et in deliciis fuit, tantum date illi tormentum'),
        ('venite ad aguas;', 'venite ad aquas;'),
        ('et labor ern vestrum', 'et laborem vestrum'),
        ('qui labor atis,', 'qui laboratis,'),
        ('invenietis réquiem animabus', 'invenietis requiem animabus'),
        ('que hace mas sequía', 'que hace más sequía'),
        # capítulo 8
        ('en si el rostro presente, y menos la tiene ia memoria', 'en sí el rostro presente, y menos la tiene la memoria'),
        ('Si caecus caceo ducatum praestet, ambo in joveam', 'Si caecus caeco ducatum praestet, ambo in foveam'),
        ('Supercccidit ignis', 'Supercecidit ignis'),
        ('ni la vera hasta', 'ni la verá hasta'),
        ('Priusquam intelligcrcnt spinae vestrac rhamnum', 'Priusquam intelligerent spinae vestrae rhamnum'),
        ('in ira absorbet ros.', 'in ira absorbet eos.'),
        ('impegimus meridic, quasi ¡n tenebris', 'impegimus meridie, quasi in tenebris'),
        # capítulo 9
        ('Qui teügerit picem. inquinabitur', 'Qui tetigerit picem, inquinabitur'),
        ('Nazaraei ejns nive', 'Nazaraei ejus nive'),
        ('rubicundiores ebore antiguo,', 'rubicundiores ebore antiquo,'),
        ('conforme a «u cuantidad', 'conforme a su cuantidad'),
        ('la cual en si es una\' hermosísima', 'la cual en sí es una hermosísima'),
        ('entre la excelenJ La e. p. en vez de Dios pone e/ Señor: "Como dijo el Señor al profeta Jonás." cia del alma',
         'entre la excelencia del alma'),   # nota de Silverio no meio do texto
        # capítulo 10
        ('es como el ag"ua,', 'es como el agua,'),
        ('así las liema el Eclesiástico, diciendo.', 'así las llama el Eclesiástico, diciendo:'),
        ('no ponen al dmn bien ninguno, sino quítenle', 'no ponen al alma bien ninguno, sino quítanle'),
        ('y mátanlp quedando', 'y mátanle quedando'),
        # capítulo 11
        ('de peor en peor. ti. También en el Libro de Josué', 'de peor en peor.\n\n[8] También en el Libro de Josué'),
        ('enseñándonos cuan desasida', 'enseñándonos cuán desasida'),
        # capítulo 12
        ('y otros oíros, y los demás', 'y otros otros, y los demás'),
        ('en cierta maner? son privativos, llamárnoslos', 'en cierta manera son privativos, llamámoslos'),
        # capítulo 13
        ('como se \'hubiera él.', 'como se hubiera él.'),
        ('son tan \'perjudiciales', 'son tan perjudiciales'),
        ('a lo que no \'posees,', 'a lo que no posees,'),
        ('«Miserable de mi,', '«Miserable de mí,'),
        ('sino a fo más dificultoso', 'sino a lo más dificultoso'),
        ('| Cuando reparas en algo, dejas de arrojarte al todo;', '| Cuando reparas en algo,\n| dejas de arrojarte al todo;'),
        ('porque esta en el centro de su humildad', 'porque está en el centro de su humildad'),
        ('conseguirlas en perfección, la cual consiste', 'conseguirlas en perfección; la cual consiste'),
    ],
}
