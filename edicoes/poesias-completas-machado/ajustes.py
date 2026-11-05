"""Poesias Completas (1901): cabeçalhos e ajustes finais de cada poema, de base/<id>.txt para 1901/<id>.txt.

    python3 edicoes/poesias-completas-machado/ajustes.py [id ...]

base/ sai de conferir.py aplicar (o texto do Wikisource com as decisões tomadas nas imagens). Aqui: o cabeçalho
(título, subtítulo, epígrafes, conferidos no fac-símile), o corte do que vem antes do primeiro verso (título e
epígrafes como o Wikisource os tem), as marcas (# parte, # subtitulo, teatro) e os consertos que a conferência de
linhas (linhas.py) apontou, todos vistos na imagem. Os poemas com MANUAL = True foram passados a limpo à mão em
1901/ e não se regravam.
"""
import json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))

MANUAL = {'lira-chinesa', 'advertencia', 'notas'}

# id: (cabeçalho, início (começo do 1º verso), trocas [(antes, depois)], modo das linhas em caixa alta)
A = {
 'musa-consolatrix': ([], None, [], None),
 'visio': ([], None, [], None),
 'quinze-anos': (["# epigrafe: Oh! la fleur de l'Eden, pourquoi l'as-tu fanée, / Insouciant enfant, belle Eve aux blonds cheveux? (Alfred de Musset)"],
                 'Era uma pobre', [], None),
 'stella': ([], None, [], None),
 'epitafio-do-mexico': ([], 'Dobra o joelho', [], None),
 'polonia': (['# epigrafe: E ao terceiro dia a alma deve voltar ao corpo, e a nação resuscitará. (Mickiewicz)'], 'Como aurora', [], None),
 'erro': ([], None, [], None),
 'elegia': (["# epigrafe: A bondade choremos / Cortada em flor que, pela mão da morte, / Nos foi arrebatada d'entre a gente. (Camões)"],
            'Se, como outr', [], None),
 'sinha': (['# epigrafe: O teu nome é como o oleo derramado. (Cantico dos Canticos)'], 'Nem o perfume', [], None),
 'horas-vivas': ([], 'Noite', [], None),
 'versos-a-corina': (['# epigrafe: Tacendo il nome di questa gentilissima. (Dante)', '', '# parte: I'], 'Tu nasceste',
                     [('\nTu\n\nque, como a illusão', '\nTu que, como a illusão'), ('\nLUZ\n', '\nA LUZ\n')], 'subtitulo'),
 'ultima-folha': ([], 'Musa, desce', [], None),
 'flor-da-mocidade': ([], None, [], None),
 'quando-ela-fala': (['# epigrafe: She speaks! / O speaks again, bright angel! (Shakesp.)'], 'Quando ella', [], None),
 'manha-de-inverno': ([], None, [], None),
 'la-marchesa-de-miramar': (['# epigrafe: A miserrima Dido / Pelos paços reaes vaga ululando. (Garção)'], 'De quanto sonho', [], None),
 'sombras': ([], None, [('lançar-te ao ⟦?19 ‖ceu:⟧', 'lançar-te ao céu!')], None),
 'ite-missa-est': ([], None, [('O ⟦?25 ‖veu⟧ do', 'O véu do')], None),
 'ruinas': (['# epigrafe: _No hay pájaros en los nidos de antaño._ (Proverbio hespanhol)'], 'Cobrem plantas', [('⟦?7 ‖e:⟧ Melancolia', 'Melancolia')], None),
 'musa-dos-olhos-verdes': ([], None, [], None),
 'noivado': ([], None, [], None),
 'a-elvira': (['# subtitulo: (Lamartine)'], 'Quando, comtigo', [], None),
 'lagrimas-de-cera': ([], 'Passou', [('Passou; a porta aberta.', 'Passou; viu a porta aberta.')], None),
 'livros-e-flores': ([], None, [], None),
 'passaros': (['# epigrafe: _Je veux changer mes pensées en oiseaux._ (C. Marot)'], 'Olha como', [], None),
 'o-verme': ([], None, [], None),
 'un-vieux-pays': (['# epigrafe: ... juntamente choro e rio. (Camões)'], 'Il est un', [], None),
 'luz-entre-sombras': ([], None, [], None),
 'uma-ode-de-anacreonte': (['# subtitulo: (A Manuel de Mello)', '', '# personagens: Lysias / Cleon / Myrto / Tres escravos',
                            '# lugar: A scena é em Samos.', '',
                            '# rubrica: Sala de festim em casa de Lysias. A esquerda a mesa do festim; á direita uma mesa tendo em cima uma lampada apagada, e junto da lampada um rolo de papyro.'],
                           'SCENA I', [], 'teatro'),
 'palida-elvira': (["# subtitulo: (A Francisco Paz)", "# epigrafe: _Ulysse, jeté sur les rives d'Ithaque, ne les reconnaît pas et pleure sa patrie. Ainsi l'homme dans le bonheur possédé ne reconnaît pas son rêve et soupire._ (Daniel Stern)"],
                   'I\n', [('⟦?177 LVII Correm-se‖Correm os⟧', 'LVII\n\nCorrem os')], None),
 'potira': (['# epigrafe: Os Tamoyos, entre outras presas que fizeram, levaram esta india, a qual pretendeu o capitão da empreza violar: resistiu valorosamente dizendo em lingua brasilica: «Eu sou christã e casada; não heide fazer traição a Deus e a meu marido; bem pódes matar-me e fazer de mim o que quizeres.» Deu-se por affrontado o barbaro, e em vingança lhe acabou a vida com grande crueldade. (Vasc., _Chr. da Comp. de Jesus_, liv. 3º)', '', '# parte: I'],
            None, [('⟦?70 Pelas‖Pela⟧ fadigas', 'Pelas fadigas')], None),
 'niani': (['# subtitulo: (Historia guaycurú)',
            '# epigrafe: Desde então cobriu-se Nanine de uma mortal melancolia, sendo seus olhos sempre chorosos. Assim se passaram trez mezes, quando um dia, estando deitada na sua rustica cama, lhe deram a noticia que seu desleal marido se tinha casado com uma rapariga de menor esphera. Senta-se então Nanine na cama, como arrebatada, chama para junto de si um pequeno indio que era seu captivo, e diz-lhe na presença de varios antecris: «És meu captivo; dou-te a liberdade, com a condição de que te chamarás toda a vida Panenioxe.» (F. Rodrigues Prado, _Hist. dos Indios Cavalleiros_)',
            '# epigrafe: ... che piagne / Vedova sola. (Dante)'],
           'Contam-se', [], None),
 'a-crista-nova': (['# epigrafe: ... essa mesma foi levada captiva para uma terra extranha. (Nahum, cap. III, v. 10)', '', '# parte: Parte I', '', '# parte: I'],
                   'Olhos fitos', [('Aquelles olhos,\n\n⟦?60 A nova christã‖⟧\nAquella', 'Aquelles olhos,\nAquella'),
                                   ('⟦?109 ‖fachar⟧', 'fechar')], None),
 'jose-bonifacio': ([], None, [], None),
 'a-visao-de-jaciuca': ([], None, [('Prestess', 'Prestes')], None),
 'a-goncalves-dias': (['# epigrafe: Ninguem virá, com titubiantes passos, / E os olhos lacrimosos, procurando / O meu jazigo... (Gonçalves Dias, _Ult. cant._)',
                       '# epigrafe: Tu vivo e goza a luz serena e pura. (J. Bazilio da Gama, _Urug._, c. V)'], 'Assim vagou', [], None),
 'os-semeadores': (['# subtitulo: (Seculo XVI)', '# epigrafe: Eis ahi saiu o que semêa a semear. (Math., XIII, 3)'], 'Vós os que', [], None),
 'a-flor-do-embirocu': (['# epigrafe: Noite, melhor que o dia, quem não te ama? (Fil. Elysio)'], 'Quando a no', [], None),
 'lua-nova': ([], None, [], None),
 'sabina': ([], None, [], None),
 'ultima-jornada': (['# parte: I'], None, [], None),
 'os-orizes': (['# subtitulo: (Fragmento)'], 'I\n', [], None),
 'o-desfecho': ([], None, [], None),
 'circulo-vicioso': ([], None, [], None),
 'uma-criatura': ([], None, [], None),
 'a-artur-de-oliveira-enfermo': ([], None, [], None),
 'mundo-interior': ([], None, [], None),
 'o-corvo': (['# subtitulo: (Edgar Poe)'], 'Em certo dia', [], None),
 'perguntas-sem-resposta': ([], None, [], None),
 'to-be-or-not-to-be': (['# subtitulo: (Shakespeare)'], 'Ser ou não', [], None),
 'lindoia': ([], None, [], None),
 'suave-mari-magno': ([], None, [], None),
 'a-mosca-azul': ([], None, [], None),
 'antonio-jose': (['# subtitulo: (21 de Outubro de 1739)'], None, [], None),
 'spinoza': ([], None, [], None),
 'goncalves-crespo': ([], None, [], None),
 'alencar': ([], None, [], None),
 'camoes': (['# parte: I'], None, [], None),
 '1802-1885': ([], None, [], None),
 'jose-de-anchieta': ([], None, [], None),
 'soneto-de-natal': ([], None, [], None),
 'os-animais-iscados-da-peste': (['# subtitulo: (La Fontaine)'], None, [('(La FonTAINE) Mal que', 'Mal que')], None),
 'dante': (['# subtitulo: (Purgatorio, canto XXV.)'], 'Acabára', [], None),
 'a-felicio-dos-santos': ([], None, [], None),
 'maria': ([], None, [(', ha no seu gesto', 'Maria, ha no seu gesto')], None),
 'a-uma-senhora-que-me-pediu-versos': ([], None, [], None),
 'clodia': ([], None, [], None),
 'velho-fragmento': ([], 'I\n', [('\nReinava\n', '\n# lacuna Reinava\n'), ('⟦?3 II‖o. q q.⟧', '# lacuna\n\nII'),
                                  ('passava o tempo ⟦?23. V‖,⟧', 'passava o tempo.\n\nV')], None),
 'no-alto': ([], None, [], None),
}
# a cabeça do Velho fragmento: «I» e a linha de pontos antes de «Reinava»
A['velho-fragmento'] = (['# parte: I'], '# lacuna', A['velho-fragmento'][2], None)

# erros de composição de 1901 corrigidos aqui (além dos de conferencia.json, «ws!»): (id, 1901, texto)
ERROS_EXTRA = [('potira', 'Pela fadigas da viagem longa', 'Pelas fadigas da viagem longa'),
               ('a-crista-nova', 'fachar seus labios', 'fechar seus labios'),
               ('lira-chinesa', '(sem o número V)', 'V'),
               ('velho-fragmento', 'passava o tempo,', 'passava o tempo.'),
               ('palida-elvira', 'outras lembranças', 'outras lembranças.')]

ROMANO = re.compile(r'^(?:PARTE )?[IVXLC]+\.?$')


def titulo_caixa(s):
    s = s.strip().rstrip('.')
    pequenas = {'de', 'da', 'do', 'das', 'dos', 'e', 'a', 'o', 'as', 'os', 'em', 'ao'}
    ws = s.lower().split()
    return ' '.join(w if (i and w in pequenas) else w[:1].upper() + w[1:] if i == 0 else w for i, w in enumerate(ws))


def finalizar(pid, texto, titulo):
    cab, inicio, trocas, modo = A[pid]
    for a, b in trocas:
        if a not in texto:
            raise SystemExit('%s: troca não achada: %r' % (pid, a))
        texto = texto.replace(a, b)
    ls = texto.split('\n')
    if inicio:
        k = next((i for i, l in enumerate(ls) if (l + '\n').startswith(inicio) or l.startswith(inicio.rstrip('\n'))), None)
        if k is None:
            raise SystemExit('%s: início não achado: %r' % (pid, inicio))
        ls = ls[k:]
    else:
        # o título em caixa alta (e o que vier antes) sai
        if ls and re.fullmatch(r"[A-ZÁÉÍÓÚÂÊÔÃÕÇÀ0-9 ,.'’\-—()]+", ls[0].strip()) and not ROMANO.match(ls[0].strip()):
            ls = ls[1:]
    out = []
    for l in ls:
        s = l.strip()
        if '⟦' in s:
            raise SystemExit('%s: marca não resolvida: %s' % (pid, s))
        if s.startswith('# lacuna'):
            out += ['', '# lacuna', '']
            resto = s[len('# lacuna'):].strip()
            if resto:
                out.append(resto)
            continue
        if ROMANO.match(s) and (not out or out[-1] == ''):
            n = s.rstrip('.')
            n = 'Parte ' + n[6:] if n.startswith('PARTE ') else n
            out += ['', '# parte: ' + n, '']
            continue
        if modo == 'teatro':
            if re.fullmatch(r'SCENA [IVX]+\.?', s):
                out += ['', '# cena: ' + titulo_caixa(s), '']; continue
            if re.fullmatch(r"[A-Z .,]+", s) and len(s) > 3:
                nome = s.strip(' .')
                if ',' in nome or nome.startswith('OS MESMOS'):
                    out += ['# rubrica: ' + ', '.join(x.strip().capitalize() if not x.strip().startswith('OS MESMOS') else x.strip().capitalize() for x in nome.split(',')).replace('Os mesmos', 'Os mesmos') + '.', '']
                else:
                    out += ['', '# fala: ' + nome, '']
                continue
            if s.startswith('(') and (s.endswith(')') or s.endswith(').')):
                out += ['', '# rubrica: ' + s, '']; continue
        if modo == 'subtitulo' and re.fullmatch(r"[A-ZÁÉÍÓÚÂÊÔÃÕÇ ]{3,}", s):
            out += ['', '# subtitulo: ' + titulo_caixa(s), '']; continue
        out.append(s)
    corpo = re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip()
    corpo = re.sub(r'(# (?:fala|parte|cena): [^\n]*)\n\n(?=[^#\n])', r'\1\n', corpo)
    return '# titulo: ' + titulo + '\n' + '\n'.join(cab) + ('\n' if cab else '') + '\n' + corpo + '\n'



# consertos de ordem e de quebra de linha que o alinhamento deixou (vistos no OCR e na imagem)
EXTRA = {
 'potira': [('\nE a dor expande em lobregos soluços, Co′o doce', '\nE a dor expande em lobregos soluços,\nCo′o doce')],
 'palida-elvira': [('é publicaco.,\nNestas estrophes pallidas e mausas\nPara te divertir de outras lembranças', 'é publicado.\nNestas estrophes pallidas e mansas,\nPara te divertir de outras lembranças.'), ('Correm os\n\nbanhos', 'Correm os banhos'), ('\nXLTX\n', '\nXLIX\n')],
 'niani': [('morreu\n\n! IV', 'morreu!\n\nIV'), ('despareceu..,', 'despareceu...')],
 'a-crista-nova': [('O hardido Bento,\na perfilar-se corre', 'O hardido Bento, a perfilar-se corre')],
 'sabina': [('as azas Toda enlevo e paixão, sincera e ardente\n', 'as azas\n'),
            ('Aquelles dias unicos na vida\n', 'Aquelles dias unicos na vida\nToda enlevo e paixão, sincera e ardente\n')],
 'dante': [('Pernas e coxas vi-as tão unidas Imita a cauda bifida a figura\nQue nem leve signal dava a juntura\nDe que tivessem sido divididas.\n',
            'Pernas e coxas vi-as tão unidas\nQue nem leve signal dava a juntura\nDe que tivessem sido divididas.\n\nImita a cauda bifida a figura\n')],
 'a-flor-do-embirocu': [('\nAMERICANAS\n', '\n')],
 'uma-ode-de-anacreonte': [('se a alma esquece O prazer', 'se a alma esquece\nO prazer')],
}
for k, v in EXTRA.items():
    c, i, t, m = A[k]
    A[k] = (c, i, t + v, m)
A['potira'] = (A['potira'][0], 'Moça christã', A['potira'][2], None)


if __name__ == "__main__":
    P = json.load(open(os.path.join(AQUI, 'poemas.json'), encoding='utf-8'))
    so = set(sys.argv[1:])
    for p in P:
        if p['id'] in MANUAL or not p['ws'] or (so and p['id'] not in so):
            continue
        t = open(os.path.join(AQUI, 'base', p['id'] + '.txt'), encoding='utf-8').read()
        open(os.path.join(AQUI, '1901', p['id'] + '.txt'), 'w', encoding='utf-8').write(finalizar(p['id'], t, p['titulo']))
    print('ok')
