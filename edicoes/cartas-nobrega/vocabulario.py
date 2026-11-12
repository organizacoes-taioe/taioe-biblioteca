"""Gera edicoes/vocabulario/cartas-nobrega.json a partir das definições abaixo (formas exatas do texto; exemplo e parte
achados no texto publicado). Rodar na raiz do repositório depois de `montar.py`: python3 -I edicoes/cartas-nobrega/vocabulario.py"""
import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
# (lema, formas, classe, definição)
V = [
 ('mui', ['mui'], 'antigo, advérbio', 'muito'),
 ('capitania', ['capitania', 'capitanias'], 'substantivo feminino', 'cada território da costa entregue a um capitão-donatário; aqui, também a povoação que o governa'),
 ('povoação', ['povoação'], 'substantivo feminino', 'lugar povoado; vila ou aldeia'),
 ('sertão', ['sertão'], 'substantivo masculino', 'o interior da terra, longe da costa'),
 ('feiticeiro', ['feiticeiro', 'feiticeiros'], 'substantivo masculino', 'chefe religioso e curandeiro dos índios, que os jesuítas viam como inimigo da fé'),
 ('roça', ['roças'], 'substantivo feminino', 'terreno cultivado, plantação'),
 ('mantimento', ['mantimento'], 'substantivo masculino', 'alimento, sustento'),
 ('maiormente', ['maiormente'], 'advérbio antigo', 'principalmente, sobretudo'),
 ('mantença', ['mantença'], 'substantivo feminino', 'sustento, manutenção'),
 ('légua', ['légua'], 'substantivo feminino', 'medida de distância, de uns seis quilômetros'),
 ('amancebado', ['amancebados', 'amancebado'], 'adjetivo', 'que vive com alguém como se fossem casados, sem casamento'),
 ('doutrinar', ['doutrinar', 'doutrinados', 'doutrinando', 'doutrinam', 'doutrinado', 'doutrinarem'], 'verbo', 'ensinar a doutrina cristã'),
 ('desconsolação', ['desconsolação'], 'substantivo feminino', 'tristeza, falta de consolo'),
 ('forra', ['forras', 'forros'], 'adjetivo', 'libertada, livre do cativeiro (diz-se do escravo que ganhou a liberdade)'),
 ('forrar', ['forrar'], 'verbo', 'dar a liberdade a um escravo'),
 ('derredor', ['derredor'], 'substantivo masculino', 'arredores; ao derredor: em volta'),
 ('mister', ['mister'], 'substantivo masculino', 'necessidade; haver mister: precisar'),
 ('macho', ['machos'], 'substantivo masculino', 'homem, varão (em contraste com a mulher)'),
 ('açu', ['açu'], 'tupi, adjetivo', 'grande; parte de nomes de rios, como Paraguaçu'),
 ('dantes', ['dantes'], 'advérbio', 'antigamente, antes'),
 ('avante', ['avante'], 'advérbio', 'adiante, para a frente'),
 ('dízimo', ['dízimos', 'dizimo'], 'substantivo masculino', 'a décima parte do rendimento, paga à Igreja'),
 ('folgara', ['folgara', 'folgará'], 'verbo', 'ficaria contente, alegrar-se'),
 ('mercar', ['mercar', 'merca'], 'verbo', 'comprar'),
 ('tributário', ['tributários'], 'adjetivo', 'que paga tributo; súdito obrigado a pagar ao rei'),
 ('lícito', ['licito'], 'adjetivo', 'permitido pela lei'),
 ('óleo', ['óleos'], 'substantivo masculino', 'os santos óleos, usados nos sacramentos'),
 ('salteado', ['salteados'], 'adjetivo', 'capturado de surpresa, em assalto (os índios tomados à força para escravos)'),
 ('cabaça', ['cabaça'], 'substantivo feminino', 'fruto de uma planta, seco e usado como vasilha ou chocalho'),
 ('obreiro', ['obreiros'], 'substantivo masculino', 'trabalhador, operário; aqui, missionário'),
 ('apartado', ['apartados', 'apartarem-se'], 'adjetivo', 'separado, afastado'),
 ('demanda', ['demandas'], 'substantivo feminino', 'questão levada à justiça, processo'),
 ('natura', ['natura', 'naturæ'], 'substantivo feminino', 'natureza'),
 ('quadrimestre', ['quadrimestres'], 'substantivo masculino', 'relatório que cada casa jesuíta enviava a Roma de quatro em quatro meses'),
 ('peleja', ['peleja'], 'substantivo feminino', 'luta, combate'),
 ('pelejar', ['pelejam', 'pelejavam', 'pelejar'], 'verbo', 'lutar, combater'),
 ('dextra', ['dextra'], 'substantivo feminino', 'a mão direita; o lado direito'),
 ('riba', ['riba'], 'substantivo feminino', 'em riba: em cima, no alto'),
 ('entonces', ['entonces'], 'advérbio', 'então, naquele tempo'),
 ('vianda', ['viandas'], 'substantivo feminino', 'alimentos, comida'),
 ('taipa', ['taipas', 'taipa', 'taipar'], 'substantivo feminino', 'parede de barro socado entre tábuas; taipar: erguer essas paredes'),
 ('enramada', ['enramadas'], 'substantivo feminino', 'abrigo ou galpão coberto de ramos'),
 ('frecha', ['frechas'], 'substantivo feminino', 'flecha'),
 ('gentilidade', ['gentilidade'], 'substantivo feminino', 'paganismo; o conjunto dos pagãos'),
 ('apóstata', ['apostatas'], 'substantivo masculino', 'quem abandona a fé que professava'),
 ('arraigado', ['arraigados'], 'adjetivo', 'enraizado, firmado'),
 ('injúria', ['injuria'], 'substantivo feminino', 'ofensa, ultraje'),
 ('escusar', ['escusam', 'escusará', 'escusar'], 'verbo', 'dispensar, evitar; dar-se por desobrigado'),
 ('algodoal', ['algodoais'], 'substantivo masculino', 'plantação de algodão'),
 ('vestiaria', ['vestiaria'], 'substantivo feminino', 'o fornecimento de roupa, vestuário'),
 ('escuridade', ['escuridades'], 'substantivo feminino', 'trevas, escuridão'),
 ('imos', ['imos'], 'verbo', 'vamos (forma antiga de ir)'),
 ('desterrado', ['desterrados'], 'adjetivo', 'afastado da pátria; exilado'),
 ('ladainha', ['ladainha'], 'substantivo feminino', 'oração de invocações em série, cantada em procissão'),
 ('sarar', ['sarasse', 'sarem'], 'verbo', 'curar, ficar são'),
 ('desinquietação', ['desinquietações'], 'substantivo feminino', 'inquietação, perturbação'),
 ('quietação', ['quietação'], 'substantivo feminino', 'sossego, paz'),
 ('aborrecimento', ['aborrecimento'], 'substantivo masculino', 'ódio, aversão'),
 ('manha', ['manhas'], 'substantivo feminino', 'esperteza, artimanha'),
 ('adulterar', ['adulterar'], 'verbo', 'corromper, falsificar'),
 ('escravaria', ['escravaria'], 'substantivo feminino', 'o conjunto dos escravos'),
 ('senhorear', ['senhorear', 'senhoreado', 'senhoreando', 'senhoreará'], 'verbo', 'dominar, fazer-se senhor de'),
 ('estorvar', ['estorvou'], 'verbo', 'impedir, atrapalhar'),
 ('despovoar', ['despovoaram', 'despovoam'], 'verbo', 'abandonar uma terra, deixá-la sem moradores'),
 ('monturo', ['monturos'], 'substantivo masculino', 'montão de lixo, esterqueira'),
 ('bruteza', ['bruteza'], 'substantivo feminino', 'brutalidade, rudeza'),
 ('rol', ['rol'], 'substantivo masculino', 'lista, relação de nomes'),
 ('delinquente', ['delinquentes'], 'substantivo masculino', 'quem comete crime'),
 ('diviso', ['divisos'], 'adjetivo', 'dividido, separado'),
 ('alvará', ['alvará'], 'substantivo masculino', 'documento oficial do rei ou de uma autoridade, que concede uma licença ou uma ordem'),
 ('restituição', ['restituições'], 'substantivo feminino', 'devolução do que foi tomado indevidamente'),
 ('comutar', ['comutar'], 'verbo', 'trocar uma pena ou obrigação por outra'),
 ('quietar', ['quietar'], 'verbo', 'sossegar, acalmar'),
 ('petitório', ['petitorio'], 'substantivo masculino', 'lista de pedidos'),
 ('abastar', ['abastam'], 'verbo', 'bastar, haver em abundância'),
 ('botar', ['botaram'], 'verbo', 'lançar, expulsar'),
 ('escória', ['escoria'], 'substantivo feminino', 'o que há de pior; ralé'),
 ('fidedigno', ['fidedigna'], 'adjetivo', 'digno de fé, que merece confiança'),
 ('valhacouto', ['valhacouto'], 'substantivo masculino', 'abrigo, refúgio (de bandidos ou inimigos)'),
 ('quadragésima', ['quadragésima'], 'substantivo feminino', 'a Quaresma, os quarenta dias antes da Páscoa'),
 ('barrete', ['barrete'], 'substantivo masculino', 'gorro de pano'),
 ('ceroulas', ['ceroulas'], 'substantivo feminino plural', 'calças de baixo, de pano, até os tornozelos'),
 ('benzer', ['benzer'], 'verbo', 'abençoar; fazer o sinal da cruz'),
 ('mancebo', ['mancebo', 'mancebas'], 'substantivo', 'jovem; mancebo/mancebas: concubino/concubinas'),
 ('cativar', ['cativaram', 'cativar'], 'verbo', 'prender em cativeiro, tomar como escravo'),
 ('rogo', ['rogos'], 'substantivo masculino', 'pedido, súplica'),
 ('meirinho', ['meirinho', 'meirinha'], 'substantivo masculino', 'oficial de justiça; aqui, o índio escolhido para fazer cumprir a ordem na aldeia'),
 ('pescaria', ['pescaria'], 'substantivo feminino', 'a atividade de pescar'),
 ('lactante', ['lactantes'], 'substantivo', 'que ainda mama; criança de peito'),
 ('bramar', ['bramava'], 'verbo', 'gritar com fúria, rugir'),
 ('serpe', ['serpes'], 'substantivo feminino', 'serpente, cobra'),
 ('oiteiro', ['oiteiro'], 'substantivo masculino', 'pequena elevação de terreno'),
 ('bombarda', ['bombardas', 'bombardadas'], 'substantivo feminino', 'canhão antigo, que atirava pedras ou balas'),
]


def main():
    texto = open(os.path.join(RAIZ, 'conteudo', 'manuel-da-nobrega', 'cartas-do-brasil.js'), encoding='utf-8').read()
    partes = [re.sub(r'_', '', m) for m in re.findall(r'texto: `(.*?)` \}', texto, re.S)]
    out = []
    for lema, formas, classe, d in V:
        achadas, ex, cap = [], None, None
        for n, t in enumerate(partes, 1):
            for f in formas:
                m = re.search(r'(?<![\wÀ-ÿ])' + re.escape(f) + r'(?![\wÀ-ÿ])', t)
                if m:
                    if f not in achadas:
                        achadas.append(f)
                    if cap is None:
                        cap = n
                        ex = t[max(0, m.start() - 40):m.end() + 40].replace('\n', ' ')
        if not achadas:
            print('não achei', lema)
            continue
        e = {'lema': lema, 'formas': achadas, 'classe': classe, 'def': d, 'exemplo': ex, 'capitulo': cap}
        out.append(e)
    json.dump({'obra': 'cartas-do-brasil', 'palavras': out}, open(os.path.join(RAIZ, 'edicoes', 'vocabulario', 'cartas-nobrega.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(out), 'verbetes')


main()
