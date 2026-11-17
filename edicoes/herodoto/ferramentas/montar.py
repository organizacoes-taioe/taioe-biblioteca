"""Monta edicoes/herodoto/original/ a partir do Perseus (Godley 1920), com as correções do fac-símile.
Uso: montar.py <pasta-trabalho> <pasta-obra> [livro=1]
Ordem: extrair.py (l<n>.json) → graves.py (regras dos acentos) → colacao.py → acentos.py → este script, que aplica
CORR (letras, conferidas nas imagens), os acentos aceitos (acentos-aceitos.tsv no livro I, acentos-aceitos-l<n>.tsv
nos outros, copiados em ferramentas/) e ACENTOS (os conferidos à mão). Cada livro tem o seu bloco em LIVROS.
Os capítulos 121A–121F do Perseus (livro II, a história de Rampsinito) saem como 121α–121ζ, a numeração de Hude;
no livro V, 92A–92G (o discurso de Sosícles) saem como 92α–92η."""
import json, os, re, sys, unicodedata as u
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graves import corrigir
B, OBRA = sys.argv[1:3]
LIVRO = int(sys.argv[3]) if len(sys.argv) > 3 else 1
AQUI = os.path.dirname(os.path.abspath(__file__))
# letras: (seção, antes, depois), conferidas no fac-símile de 1921 (pranchas da colação)
CORR1 = [
    ('32.7', 'ἔτι τελευτήσῃ', 'ἔτι τελευτήσει'), ('46.2', 'μαντείων', 'μαντηίων'), ('50.2', 'ἐπὶ μὰν', 'ἐπὶ μὲν'),
    ('55.1', 'μαντείου', 'μαντηίου'), ('60.5', 'Ἀηθναίη', 'Ἀθηναίη'), ('63.1', 'τρέπουσι', 'τράπουσι'),
    ('68.5', 'Λακεδαιμονίοσσι', 'Λακεδαιμονίοισι'), ('74.2', 'τῇ ἡμέρης', 'τῆς ἡμέρης'),
    ('80.5', 'ὤσφροντο', 'ὤσφραντο'), ('82.3', 'ἀπαμύνοιεν', 'ἐπαμύνοιεν'), ('116.3', 'ὁ Ἀστυάγεος', 'ὁ Ἀστυάγης'),
    ('117.2', 'τρέπεται', 'τράπεται'), ('119.2', 'ἐκπέμπεν', 'ἐκπέμπει'), ('134.3', 'ἀρχὸν τῶν', 'ἀρχόντων'),
    ('164.3', 'τὰ ἐν τῶν', 'τὰ ἐκ τῶν'), ('164.3', 'εἰσβάντες', 'ἐσβάντες'), ('165.1', 'Φωκαίες', 'Φωκαιέες'),
    ('170.3', 'περ ἐς δῆμοι', 'περ εἰ δῆμοι'), ('172.2', 'χέασθαι', 'χρᾶσθαι'), ('176.3', 'ἐκδημέουσι', 'ἐκδημέουσαι'),
    ('179.2', 'τάφου', 'τάφρου'), ('193.5', 'τὸν φοινίκων', 'τῶν φοινίκων'), ('199.1', 'ἀξιούμεναι', 'ἀξιεύμεναι'),
    ('199.5', 'ὅσσαι', 'ὅσαι'), ('202.2', 'ὀσμῇ', 'ὀδμῇ'), ('205.1', 'Μασαγετέων', 'Μασσαγετέων'),
    ('216.3', 'ἀλλʼ γῇ', 'ἀλλὰ γῇ'), ('153.1', 'ἐν μέσῃ ἑωυτῷ προαγορεύουσι· τῇ πόλι', 'ἐν μέσῃ τῇ πόλι'),
    ('97.1', 'ἔφη δίκαν', 'ἔφη δικᾶν'), ('120.1', 'ὁ Ἁστυάγης', 'ὁ Ἀστυάγης'), ('128.3', 'Πέρῃσι', 'Πέρσῃσι'),
    ('133.4', 'δὲμὴ ἅδῃ', 'δὲ μὴ ἅδῃ'), ('29.1', 'ἐκπλώσας,ἵνα', 'ἐκπλώσας, ἵνα'), ('145.1', 'Αἴγίον', 'Αἴγιον'), ('149.1', 'ἐν τῆ ἠπείρῳ', 'ἐν τῇ ἠπείρῳ'), ('163.2', 'μὲν ἦν, Ἀργανθώνιος', 'μὲν ἦν Ἀργανθώνιος'),
    ('166.1', 'ἑξήκόντα', 'ἑξήκοντα'), ('171.6', 'ἀποδείκνῦσι', 'ἀποδεικνῦσι'), ('173.3', 'καὶ νυν ἔτι', 'καὶ νῦν ἔτι'), ('42.2', 'χρηστοῖσἰ', 'χρηστοῖσι'),
]
# acentos e espíritos conferidos à mão (seção, forma do Perseus depois de graves.py, forma de Godley)
ACENTOS1 = [
    ('5.2', 'νέος', 'νεός'), ('7.4', 'γενεᾶς', 'γενεὰς'), ('10.2', 'νοῶ', 'νόῳ'), ('11.3', 'σε', 'σὲ'),
    ('19.1', 'ἅφθη', 'ἄφθη'), ('22.2', 'εἶπας', 'εἴπας'), ('86.5', 'εἶπας', 'εἴπας'), ('122.1', 'εἶπας', 'εἴπας'),
    ('128.2', 'εἶπας', 'εἴπας'), ('27.4', 'ὓπερ', 'ὑπὲρ'), ('31.1', 'ὀλβία', 'ὄλβια'), ('42.1', 'ἶσχον', 'ἴσχον'),
    ('44.1', 'τῳ', 'τῷ'), ('52.1', 'τῳ', 'τῷ'), ('59.2', 'δευτέρα', 'δεύτερα'),
    ('112.2', 'δευτέρα', 'δεύτερα'), ('134.2', 'δευτέρα', 'δεύτερα'), ('179.2', 'δευτέρα', 'δεύτερα'),
    ('204.2', 'δευτέρα', 'δεύτερα'), ('61.2', 'οὒ', 'οὔ'), ('68.1', 'ὀρέων', 'ὁρέων'),
    ('73.3', 'εἴλῃ', 'εἴλη'), ('82.2', 'χώρῇ', 'χώρῃ'), ('109.3', 'ἅπαις', 'ἄπαις'),
    ('114.1', 'αὑτὸν', 'αὐτὸν'), ('124.2', 'περὶ', 'πέρι'), ('125.2', 'Πέρσεων', 'Περσέων'), ('126.5', 'πείθεσθαί', 'πείθεσθαι'),
    ('136.2', 'ἰππεύειν', 'ἱππεύειν'), ('140.3', 'τἆλλα', 'τἄλλα'), ('141.2', 'ἐπεῖ', 'ἐπεὶ'), ('142.4', 'σφισι', 'σφίσι'),
    ('151.3', 'νῦν', 'νυν'), ('164.1', 'προισχόμενος', 'προϊσχόμενος'), ('164.2', 'δουλοσύνη', 'δουλοσύνῃ'),
    ('167.1', 'τῶ', 'τῷ'), ('176.1', 'ἀρετᾶς', 'ἀρετὰς'), ('183.2', 'μούνα', 'μοῦνα'), ('186.2', 'τούτω', 'τούτῳ'),
    ('187.1', 'ὕπερ', 'ὑπὲρ'), ('187.4', 'ὕπερ', 'ὑπὲρ'), ('188.1', 'προβάτοῖσι', 'προβάτοισι'), ('192.3', 'μυρίαι', 'μύριαι'),
    ('202.2', 'δίαιτᾳ', 'δίαιτα'), ('210.2', 'ἐστί', 'ἔστι'),
]
PARTES1 = [((1, 5), 'Proêmio: os raptos'), ((6, 14), 'Candaules e Giges'), ((15, 25), 'Os reis da Lídia e Árion'),
          ((26, 45), 'Creso, Sólon e Átis'), ((46, 58), 'Creso consulta os oráculos'), ((59, 70), 'Atenas e Esparta'),
          ((71, 84), 'A guerra com Ciro e a tomada de Sardes'), ((85, 94), 'Creso na fogueira; os lídios'),
          ((95, 106), 'Os medos'), ((107, 122), 'O nascimento de Ciro'), ((123, 130), 'Ciro contra Astíages'),
          ((131, 140), 'Os costumes dos persas'), ((141, 161), 'Os jônios e Pactias'),
          ((162, 176), 'Hárpago na Jônia, na Cária e na Lícia'), ((177, 187), 'Babilônia e as suas rainhas'),
          ((188, 200), 'Ciro toma Babilônia; os costumes dos babilônios'), ((201, 216), 'Tômiris e a morte de Ciro')]
# livro II (Euterpe)
CORR2 = [
    ('17.4', 'τρέπεται', 'τράπεται'), ('29.4', 'λίμνην μεγάλη', 'λίμνη μεγάλη'), ('45.3', 'εὐμένεια', 'εὐμενείη'),
    ('47.1', 'παριὼν αὐτοῖσι', 'παριὼν ὑός, αὐτοῖσι'), ('47.2', 'δικαιοῦσι', 'δικαιεῦσι'),
    ('67.1', 'ἀποφανόντες', 'ἀποθανόντες'), ('69.2', 'ταριχεύσαντες', 'ταριχεύοντες'), ('80.1', 'ἐκτρέπονται', 'ἐκτράπονται'),
    ('92.5', 'τρέπουσι', 'τράπουσι'), ('93.1', 'ἐκπλέουσι', 'ἐκπλώουσι'), ('93.2', 'ἡγεμονία', 'ἡγεμονίη'),
    ('96.4', 'ῥιπὶ', 'ῥίπεϊ'), ('113.3', 'τὸν στόματος', 'τὸν τοῦ στόματος'), ('116.3', 'ἀριστείῃ', 'ἀριστηίῃ'),
    ('120.4', 'ἐπιτρέπειν', 'ἐπιτράπειν'), ('121F.1', 'διανέμοντα', 'διαπέμποντα'), ('158.3', 'ὑπώρεαν', 'ὑπωρέην'),
    ('169.2', 'βασιληία', 'βασιλήια'),
]
ACENTOS2 = [
    ('28.4', 'ἄβυσσοί', 'ἄβυσσοι'), ('28.4', 'εἰσι', 'εἰσὶ'), ('41.6', 'τἆλλα', 'τἄλλα'), ('59.3', 'Ἡλίω', 'Ἡλίῳ'),
    ('61.1', 'προτερόν', 'πρότερόν'), ('149.4', 'ἔστἱ', 'ἔστι'), ('149.5', 'ὓδωρ', 'ὕδωρ'),
]
PARTES2 = [((1, 4), 'Psamético e os homens mais antigos'), ((5, 18), 'A terra do Egito'),
           ((19, 27), 'As cheias do Nilo'), ((28, 34), 'As fontes do Nilo'), ((35, 41), 'Os costumes dos egípcios'),
           ((42, 53), 'Héracles e os deuses dos gregos'), ((54, 64), 'Dodona e as festas dos egípcios'),
           ((65, 76), 'Os animais sagrados'), ((77, 90), 'A vida dos egípcios e os embalsamamentos'),
           ((91, 98), 'Perseu, os pântanos e o caminho do rio'), ((99, 110), 'Min, Nitócris, Méris e Sesóstris'),
           ((111, 120), 'Feros, Proteu e Helena'), ((121, 123), 'Rampsinito e o ladrão'),
           ((124, 136), 'Quéops, Quéfren e Miquerino'), ((137, 146), 'Sabacos, Setos e as gerações dos reis'),
           ((147, 157), 'Os doze reis e Psamético'), ((158, 171), 'Neco, Psâmis e Apríes'), ((172, 182), 'Amásis')]
# livro III (Thalia), no vol. II de Godley (1921)
CORR3 = [
    ('2.2', 'παρατρέπουσι', 'παρατράπουσι'), ('12.1', 'ἔκειτο', 'ἐκέετο'), ('14.11', 'Αἴγυπτους', 'Αἴγυπτον'),
    ('21.2', 'ἀνήρ δίκαιος', 'ἀνήρ ἐστι δίκαιος'), ('21.3', 'τρέπουσι', 'τράπουσι'), ('22.4', 'προκεῖσθαι', 'προκέεσθαι'),
    ('34.2', 'προσκεῖσθαι', 'προσκέεσθαι'), ('34.5', 'οἷον σε ἐκεῖνος', 'οἷον σὲ ἐκεῖνος'),
    ('65.3', 'ἀποτρέπειν', 'ἀποτράπειν'), ('81.1', 'ἐπιτρέπειν', 'ἐπιτράπειν'), ('100.1', 'κεῖται', 'κέεται'),
    ('157.1', 'ἐπιτρέπεσθαι', 'ἐπιτράπεσθαι'),
]
ACENTOS3 = []
PARTES3 = [((1, 9), 'Cambises marcha contra o Egito'), ((10, 16), 'Psamenito e a conquista do Egito'),
           ((17, 26), 'A expedição contra os etíopes'), ((27, 38), 'A loucura de Cambises'),
           ((39, 47), 'Polícrates e o anel'), ((48, 60), 'Periandro e Licofron; o cerco de Samos'),
           ((61, 66), 'O mago e a morte de Cambises'), ((67, 79), 'Os sete contra os magos'),
           ((80, 88), 'O debate sobre o governo; Dario rei'), ((89, 97), 'As satrapias e os tributos'),
           ((98, 106), 'A Índia e as formigas do ouro'), ((107, 117), 'A Arábia e os confins da terra'),
           ((118, 128), 'Intafernes; Oretes e a morte de Polícrates'), ((129, 138), 'Democedes'),
           ((139, 149), 'Silosonte e Samos'), ((150, 160), 'A revolta de Babilônia e Zópiro')]
# livro IV (Melpômene), no vol. II de Godley (1921)
CORR4 = [
    ('3.2', 'μετά γε', 'μετὰ δὲ'), ('4.1', 'Δαρεῖυς', 'Δαρεῖος'), ('20.2', 'κατʼ ὅσον', 'κατόσον'),
    ('48.3', 'Ὀρδησσὸς καὶ μέσου', 'Ὀρδησσὸς διὰ μέσου'), ('54.1', 'Ὑβλαίην', 'Ὑλαίην'),
    ('57.1', 'λίμνην καλεόμενον', 'λίμνην καλεομένην'), ('60.2', 'τρέπεται', 'τράπεται'),
    ('64.3', 'ἀποδερμάτων', 'ἀποδαρμάτων'), ('73.2', 'Σκύψαι', 'Σκύθαι'), ('78.4', 'ἐγκλῄσειε', 'ἐγκληίσειε'),
    ('101.2', 'Σκυψέων', 'Σκυθέων'), ('119.4', 'ἐπίῃ καὶ τὴν', 'ἐπίῃ καὶ ἐπὶ τὴν'),
    ('148.1', 'οἰκηιούμενος', 'οἰκηιεύμενος'), ('148.3', 'Μεμβιάρου', 'Μεμβλιάρου'), ('156.3', 'Βλατέα', 'Πλατέα'),
    ('160.1', 'κλέεται', 'καλέεται'), ('163.3', 'ἐξοπτήσεις', 'ἐξοπτήσῃς'), ('186.2', 'δικαιοῦσι', 'δικαιεῦσι'),
    ('201.1', 'Βορκαίους', 'Βαρκαίους'), ('201.3', 'ἐξῄσαν', 'ἐξήισαν'), ('203.3', 'Ἀρυνάνδεω', 'Ἀρυάνδεω'), ('205.1', 'γίνονται·ἐκ', 'γίνονται· ἐκ'),
    # os parênteses de Godley, que o Perseus marca com «ʽ» solto e um combinante no fim (conferidos nas imagens, 2026-11-17)
    ('34.2', 'ʽτὸ δὲ σῆμα', '(τὸ δὲ σῆμα'), ('34.2', 'οἱ ἐλαίἠ,', 'οἱ ἐλαίη),'),
    ('35.3', 'ʽοὗτος δὲ ὁ Ὠλὴν', '(οὗτος δὲ ὁ Ὠλὴν'), ('35.3', 'ἐν Δήλᾠ,', 'ἐν Δήλῳ),'),
]
ACENTOS4 = [
    ('4.1', 'ἧρξαν', 'ἦρξαν'), ('5.1', 'τῳ', 'τῷ'), ('7.2', 'Κολάξαιν', 'Κολάξαϊν'), ('8.1', 'ὕπερ', 'ὑπὲρ'),
    ('8.3', 'τῳ', 'τῷ'), ('9.4', 'αὕτη', 'αὐτή'), ('9.5', 'τῳ', 'τῷ'), ('11.3', 'χωρῆν', 'χώρην'),
    ('13.1', 'ὕπερ', 'ὑπὲρ'), ('14.3', 'ἔτει', 'ἔτεϊ'), ('15.2', 'πὰρʼ', 'παρʼ'), ('15.4', 'ἔστηκε', 'ἕστηκε'),
    ('16.1', 'φας', 'φὰς'), ('17.1', 'Βορυσθενειτέων', 'Βορυσθενεϊτέων'), ('17.1', 'ὕπερ', 'ὑπὲρ'),
    ('17.2', 'ὕπερ', 'ὑπὲρ'), ('29.1', 'ἡ', 'ἢ'), ('44.2', 'Πακτυικῆς', 'Πακτυϊκῆς'), ('44.3', 'ὃμοια', 'ὅμοια'),
    ('45.2', 'Τάναιν', 'Τάναϊν'), ('46.2', 'γένει', 'γένεϊ'), ('50.1', 'πλήθει', 'πλήθεϊ'), ('50.2', 'θέρει', 'θέρεϊ'),
    ('50.4', 'τῶ', 'τῷ'), ('50.4', 'θέρει', 'θέρεϊ'), ('58.1', 'Σκυθικῆ', 'Σκυθικῇ'), ('60.1', 'ἔστηκε', 'ἕστηκε'),
    ('71.3', 'ἀμάξῃ', 'ἁμάξῃ'), ('73.1', 'ἀμάξῃσι', 'ἁμάξῃσι'), ('76.5', 'Σαυλίω', 'Σαυλίῳ'),
    ('78.3', 'Βορυσθενειτέων', 'Βορυσθενεϊτέων'), ('79.4', 'Βορυσθενειτέων', 'Βορυσθενεϊτέων'), ('80.3', 'εἶς', 'εἷς'),
    ('81.3', 'μεγάθει', 'μεγάθεϊ'), ('81.5', 'τῶ', 'τῷ'), ('88.1', 'τῆ', 'τῇ'), ('95.5', 'τετάρτω', 'τετάρτῳ'),
    ('97.4', 'ἁλλὰ', 'ἀλλὰ'), ('110.1', 'πὲρι', 'πέρι'), ('110.1', 'τοὐς', 'τοὺς'), ('110.1', 'πελάγει', 'πελάγεϊ'),
    ('116.1', 'νυν', 'νῦν'), ('116.2', 'χρὲωνται', 'χρέωνται'), ('117.1', 'γαμὲεται', 'γαμέεται'),
    ('119.4', 'γενομὲνους', 'γενομένους'), ('122.3', 'Τάναιν', 'Τάναϊν'), ('123.3', 'Τάναις', 'Τάναϊς'),
    ('125.5', 'Σκύθησι', 'Σκύθῃσι'), ('130.1', 'ἀνιῴατο', 'ἀνιῷατο'), ('135.1', 'στρατοπέδω', 'στρατοπέδῳ'),
    ('137.3', 'Ἰστιαίου', 'Ἱστιαίου'), ('143.3', 'Πέρσησι', 'Πέρσῃσι'), ('149.1', 'του', 'τοῦ'), ('150.3', 'Λιβύη', 'Λιβύῃ'),
    ('151.2', 'οὕνομα', 'οὔνομα'), ('152.4', 'πρόκροσσοί', 'πρόκροσσοι'), ('155.4', 'δε', 'δὲ'), ('158.1', 'ἔτει', 'ἔτεϊ'),
    ('159.4', 'αὑτῶν', 'αὐτῶν'), ('161.3', 'ἐποίησέ', 'ἐποίησε'), ('161.3', 'σφεας', 'σφέας'), ('162.5', 'δε', 'δὲ'),
    ('163.3', 'Βᾶττους', 'Βάττους'), ('184.3', 'οἶά', 'οἷά'), ('190.1', 'δε', 'δὲ'), ('192.3', 'ἔστι', 'ἐστί'),
    ('196.1', 'κυματωγήν', 'κυματώγην'), ('197.1', 'εἶσι', 'εἰσὶ'), ('198.3', 'τῆ', 'τῇ'),
]
PARTES4 = [((1, 12), 'Dario contra os citas; as origens dos citas'), ((13, 27), 'Aristeas e os povos do norte'),
           ((28, 36), 'O inverno da Cítia e os hiperbóreos'), ((37, 45), 'As partes da terra'),
           ((46, 58), 'Os rios da Cítia'), ((59, 66), 'Os deuses e a guerra dos citas'),
           ((67, 75), 'Adivinhos, juramentos e funerais dos citas'), ((76, 82), 'Anacársis e Cíles'),
           ((83, 92), 'A ponte do Bósforo e a marcha pela Trácia'), ((93, 98), 'Os getas e Zalmóxis; a ponte do Istro'),
           ((99, 109), 'A Cítia e os seus vizinhos'), ((110, 117), 'As amazonas e os saurômatas'),
           ((118, 125), 'Os citas recuam diante de Dario'), ((126, 135), 'Idantirso e os presentes dos citas'),
           ((136, 144), 'Os jônios na ponte e a volta de Dario'), ((145, 149), 'Os mínios e Tera'),
           ((150, 158), 'Bato e a fundação de Cirene'), ((159, 167), 'Os reis de Cirene e Feretima'),
           ((168, 180), 'Os povos da Líbia'), ((181, 190), 'As colinas de sal e os povos do deserto'),
           ((191, 199), 'A Líbia ocidental'), ((200, 205), 'O cerco de Barca e o fim de Feretima')]
# livro V (Terpsícore), no vol. III de Godley (1922)
CORR5 = [
    ('9.3', 'Δίγυες', 'Λίγυες'), ('15.2', 'τρέπονται', 'τράπονται'), ('17.2', 'Μακεδονίν', 'Μακεδονίῃ'),
    ('23.1', 'Ἑλλήποντον', 'Ἑλλήσποντον'), ('29.2', 'τούτους μὲν πόλιν', 'τούτους μὲν τὴν πόλιν'),
    ('41.1', 'ἔφεδρον', 'ἔπεδρον'), ('52.4', 'ἐς βάλλοντι', 'ἐσβάλλοντι'), ('61.2', 'τρέπονται', 'τράπονται'),
    ('79.2', 'οὐκ ὦν', 'οὐκῶν'), ('83.3', 'ἱροεργίαι', 'ἱρουργίαι'), ('106.3', 'ἀξιοῦμαι', 'ἀξιεῦμαι'),
    ('106.4', 'εἴ περ', 'εἴπερ'), ('59.1', 'ἀμφιτρύων', 'Ἀμφιτρύων'),
    ('5.1', 'πολλά,·', 'πολλάς·'), ('67.3', 'Κλεισθένης ʽ καὶ γὰρ τοῦτο δεῖ ἀπηγήσασθαἰ ὡς', 'Κλεισθένης (καὶ γὰρ τοῦτο δεῖ ἀπηγήσασθαι) ὡς'),
]
ACENTOS5 = [
    ('30.4', 'φερέγγυός', 'φερέγγυος'), ('30.4', 'εἰμι', 'εἰμὶ'), ('41.2', 'ἀληθεῖ', 'ἀληθέι'),
    ('49.8', 'ἐχόμενόν', 'ἐχόμενον'), ('49.8', 'ἐστι', 'ἐστὶ'), ('50.2', 'χρὲον', 'χρεὸν'), ('52.3', 'εἱσι', 'εἰσι'),
    ('80.1', 'χρῇσαι', 'χρῆσαι'), ('86.3', 'τραπέσθαι', 'τράπεσθαι'),
]
PARTES5 = [((1, 10), 'Os perintios, os peônios e os trácios'), ((11, 16), 'Histieu, Côes e os peônios levados para a Ásia'),
           ((17, 27), 'Os macedônios e os enviados persas; Histieu em Susa'),
           ((28, 38), 'Naxos e o começo da revolta jônica'), ((39, 48), 'Cleômenes e Dorieu'),
           ((49, 54), 'Aristágoras em Esparta'), ((55, 65), 'Hiparco, os gefireus e a queda dos Pisistrátidas'),
           ((66, 78), 'Clístenes, Iságoras e as vitórias de Atenas'),
           ((79, 89), 'Tebas, Egina e as estátuas de Dâmia e Auxésia'), ((90, 96), 'Hípias e o discurso de Sosícles'),
           ((97, 103), 'Aristágoras em Atenas e o incêndio de Sardes'), ((104, 115), 'A revolta de Chipre'),
           ((116, 126), 'A Cária, o Helesponto e a morte de Aristágoras')]
# livro VI (Érato), no vol. III de Godley (1922)
CORR6 = [
    ('12.1', 'ἐπιτρέπουσι', 'ἐπιτράπουσι'),
    ('33.2', 'τρέπονται', 'τράπονται'),
    ('34.2', 'ἐκτρέπονται', 'ἐκτράπονται'),
    ('42.1', 'δωσίδικοι', 'δοσίδικοι'),
    ('53.2', 'ὀρθῷ χρεωμένῳ', 'ὀρθῷ λόγῳ χρεωμένῳ'),
    ('61.2', 'προσέκειτο', 'προσεκέετο'),
    ('71.2', 'Δευτυχίδης', 'Λευτυχίδης'),
    ('73.2', 'Κάσαυβον', 'Κάσαμβον'),
    ('77.1', 'κεῖται', 'κέεται'),
    ('91.2', 'ἐπισπαστῆρσι', 'ἐπισπάστροισι'),
    ('98.3', 'ἐρξίης', 'ἐρξείης'),
    ('100.3', 'φράξει', 'φράζει'),
    ('119.3', 'τρέπεται', 'τράπεται'),
    ('119.4', 'φυλάσοντες', 'φυλάσσοντες'),
    ('138.2', 'αὐτῶν τινός', 'αὐτῶν ὑπʼ ἐκείνων τινός'),
    ('139.4', 'κεῖται', 'κέεται'),
    ('86C.2', 'γλαῦκʼ Ἐπικυδείδη', 'Γλαῦκʼ Ἐπικυδείδη'),
    ('69.4', 'ʽτὸν χρόνον γάρ, τοὺς δέκα μῆνας, οὐδέκω ἐξήκειν̓', '(τὸν χρόνον γάρ, τοὺς δέκα μῆνας, οὐδέκω ἐξήκειν)'),
    ('109.1', 'ʽὀλίγους γὰρ εἶναι στρατιῇ τῇ Μήδων συμβάλλειν’', '(ὀλίγους γὰρ εἶναι στρατιῇ τῇ Μήδων συμβάλλειν)'),
    ('109.2', 'ʽτὸ Παλαιὸν γὰρ Ἀθηναῖοι ὁμόψηφον τὸν πολέμαρχον ἐποιεῦντο τοῖσι στρατηγοῖσἰ', '(τὸ παλαιὸν γὰρ Ἀθηναῖοι ὁμόψηφον τὸν πολέμαρχον ἐποιεῦντο τοῖσι στρατηγοῖσι)'),
]
ACENTOS6 = [
    ('13.2', 'τοὺ', 'τοῦ'),
    ('28.2', 'Καϊκου', 'Καΐκου'),
    ('46.3', 'οὓτω', 'οὕτω'),
    ('46.3', 'ὣστε', 'ὥστε'),
    ('73.2', 'γένει', 'γένεϊ'),
    ('74.1', 'τῆ', 'τῇ'),
    ('91.1', 'οἶοί', 'οἷοί'),
    ('108.3', 'πλησιοχώροισί', 'πλησιοχώροισι'),
]
PARTES6 = [
    ((1, 10), 'Histieu e a frota jônica em Lade'),
    ((11, 21), 'A batalha de Lade e a queda de Mileto'),
    ((22, 33), 'Os sâmios em Zancle; a morte de Histieu'),
    ((34, 41), 'Os Milcíades no Quersoneso'),
    ((42, 50), 'Mardônio, Tasos e os arautos de Dario'),
    ((51, 60), 'Os reis de Esparta'),
    ((61, 72), 'Demarato e Leotíquides'),
    ((73, 84), 'A loucura e a morte de Cleômenes'),
    ((85, 93), 'Glauco e a guerra com Egina'),
    ((94, 101), 'Dátis e Artafernes; a tomada de Erétria'),
    ((102, 110), 'Antes de Maratona'),
    ((111, 120), 'A batalha de Maratona'),
    ((121, 131), 'Os alcmeônidas e o casamento de Agariste'),
    ((132, 140), 'Milcíades em Paros; os pelasgos de Lemnos'),
]
ED1 = ('A. D. Godley, Herodotus, vol. I (Loeb, Londres e Nova York, 1920); conferido com o fac-símile da impressão '
       'de 1921 (Internet Archive herodotud0000adgo); ver LEIAME.md')
ED2 = ('A. D. Godley, Herodotus, vol. II (Loeb, Londres e Nova York, 1921); conferido com o fac-símile da impressão '
       'de 1921 (Internet Archive herodotus0002adgo_j1l1); ver LEIAME.md')
ED3 = ('A. D. Godley, Herodotus, vol. III (Loeb, Londres e Nova York, 1922); conferido com o fac-símile da 1ª impressão, '
       '1922 (Internet Archive in.ernet.dli.2015.183370); ver LEIAME.md')
LIVROS = {1: dict(corr=CORR1, acentos=ACENTOS1, partes=PARTES1, aceitos='acentos-aceitos.tsv', letra='Α',
                  romano='I', titulo='Α · ΚΛΕΙΩ', ncaps=216, edicao=ED1),
          2: dict(corr=CORR2, acentos=ACENTOS2, partes=PARTES2, aceitos='acentos-aceitos-l2.tsv', letra='Β',
                  romano='II', titulo='Β · ΕΥΤΕΡΠΗ', ncaps=182, edicao=ED1),
          3: dict(corr=CORR3, acentos=ACENTOS3, partes=PARTES3, aceitos='acentos-aceitos-l3.tsv', letra='Γ',
                  romano='III', titulo='Γ · ΘΑΛΕΙΑ', ncaps=160, edicao=ED2),
          4: dict(corr=CORR4, acentos=ACENTOS4, partes=PARTES4, aceitos='acentos-aceitos-l4.tsv', letra='Δ',
                  romano='IV', titulo='Δ · ΜΕΛΠΟΜΕΝΗ', ncaps=205, edicao=ED2),
          5: dict(corr=CORR5, acentos=ACENTOS5, partes=PARTES5, aceitos='acentos-aceitos-l5.tsv', letra='Ε',
                  romano='V', titulo='Ε · ΤΕΡΨΙΧΟΡΗ', ncaps=126, edicao=ED3),
          6: dict(corr=CORR6, acentos=ACENTOS6, partes=PARTES6, aceitos='acentos-aceitos-l6.tsv', letra='Ζ',
                  romano='VI', titulo='Ζ · ΕΡΑΤΩ', ncaps=140, edicao=ED3)}
L = LIVROS[LIVRO]
CORR, ACENTOS, PARTES = L['corr'], list(L['acentos']), L['partes']
SUB = dict(zip('ABCDEFG', 'αβγδεζη'))   # 121A–F (II), 92A–G (V), 86A–D (VI)
def cap_marca(c):
    return c[:-1] + SUB[c[-1]] if c[-1] in SUB else c
def cap_num(c):
    return int(re.match(r'\d+', c).group())
N_MANUAIS = len(ACENTOS); CTX = {}
for l in open(os.path.join(AQUI, L['aceitos']), encoding='utf-8'):
    if not l.strip(): continue
    r = l.rstrip('\n').split('\t')
    novo = ('χώρη' if r[2] == 'χώρη' else 'χώρῃ') if r[1] == 'χωρῇ' else r[2].replace('᾽', 'ʼ').replace('’', 'ʼ')
    if novo[:1] != r[1][:1] and novo[:1].lower() == r[1][:1]: novo = novo[0].lower() + novo[1:]
    if novo == 'ἢ' and r[1] == 'ἡ': novo = 'ἣ'
    ACENTOS.append((r[0], r[1], novo)); CTX[len(ACENTOS) - 1] = r[4]
PAL = re.compile(r'[\ẁ-ͯʼ]+')
def _n(w):
    return ''.join(c for c in u.normalize('NFD', w.lower()) if not u.combining(c)).replace('ʼ', '').replace('’', '')
def troca_palavra(t, a, b, ctx=None):
    """troca a ocorrência de a; com ctx (as palavras em volta, da colação), a que tem a mesma palavra seguinte"""
    ms = [m for m in PAL.finditer(t)]
    cand = [k for k, m in enumerate(ms) if m.group() == a]
    if ctx and len(cand) > 1:
        cw = ctx.split(); i = next((j for j, w in enumerate(cw) if w == a), None)
        if i is not None and i + 1 < len(cw):
            boas = [k for k in cand if k + 1 < len(ms) and _n(ms[k + 1].group()) == _n(cw[i + 1])]
            if boas: cand = boas
    if not cand: return t, False
    m = ms[cand[0]]
    return t[:m.start()] + b + t[m.end():], True
def capitular(t):
    i = next(k for k, c in enumerate(t) if c.isalpha())
    return t[:i] + t[i].upper() + t[i + 1:]
d = json.load(open(os.path.join(B, f'l{LIVRO}.json'), encoding='utf-8'))
usadas, ac_usados, ngr, ndu = set(), set(), 0, 0
caps = {}
for c, secs in d['caps']:
    blocos, cur = [], ''
    for s, t in secs:
        ref = f'{c}.{s}'
        for k, (r, a, b) in enumerate(CORR):
            if r == ref:
                if t.count(a) != 1: sys.exit(f'correção {ref} «{a}» aparece {t.count(a)} vezes')
                t = t.replace(a, b); usadas.add(k)
        t, g1, g2 = corrigir(t); ngr += g1; ndu += g2
        for k, (r, a, b) in enumerate(ACENTOS):
            if r == ref:
                if a == 'ὁ' and b == 'ὃ' and k >= N_MANUAIS:
                    # ὃ pronome só antes de μέν/δέ; antes de nome ou particípio é o artigo, e o OCR errou
                    m_ = re.search(r'(?<![\w\u0300-\u036f])ὁ (\S+)', t)
                    if not m_ or m_.group(1).rstrip(',·.') not in ('μὲν', 'δὲ', 'δʼ', 'μέν', 'δέ'):
                        ac_usados.add(k); continue
                t, ok = troca_palavra(t, a, b, CTX.get(k))
                if not ok: sys.exit(f'acento {ref} «{a}» não achado')
                ac_usados.add(k)
        t = corrigir(t)[0]   # 2ª passada: um agudo do OCR antes de palavra que não é enclítica volta a grave
        t = t.replace('⟦n⟧', '')
        t = re.sub(r'\s*⟦gap⟧\s*', ' … ', t)
        t = t.replace('ʼ', '’')
        t = re.sub(r'\s*⟦l⟧\s*', '\n| ', t); t = re.sub(r'\s*⟦/l⟧\s*', '\n', t)
        t = re.sub(r' +([.,·;])', r'\1', t); t = re.sub(r'  +', ' ', t)
        if '⟦' in t: sys.exit(f'sobrou marca: {ref}')
        texto = f'[{cap_marca(c)}.{s}] '
        for p in t.split('\n'):
            p = p.strip()
            if not p: continue
            if p.startswith('| '):
                if texto:   # seção que começa no verso: a marca vai no começo do primeiro verso
                    p = '| ' + texto + p[2:]; texto = ''
                if cur.strip(): blocos.append(cur.strip()); cur = ''
                if blocos and blocos[-1].startswith('| ') and not cur: blocos[-1] += '\n' + p
                else: blocos.append(p)
            else:
                cur += (' ' if cur else '') + (texto + p if texto else p); texto = ''
        if texto:
            cur += (' ' if cur else '') + texto.strip()
    if cur.strip(): blocos.append(cur.strip())
    # maiúscula no começo do capítulo, como em Godley
    m = re.match(r'(\[\d+[α-η]?\.\d+\] )(.*)$', blocos[0], re.S)
    blocos[0] = m.group(1) + capitular(m.group(2))
    caps[c] = blocos
falta = [CORR[k] for k in range(len(CORR)) if k not in usadas] + [ACENTOS[k] for k in range(len(ACENTOS)) if k not in ac_usados]
if falta: sys.exit(f'não aplicadas: {falta}')
os.makedirs(os.path.join(OBRA, 'original'), exist_ok=True)
n1 = 'Α' if LIVRO == 1 else L['letra']
exemplo = '«[1.1]»'
for k, ((a, b), tit) in enumerate(PARTES):
    cab = [f'# titulo: Ἡροδότου Ἱστορίαι {L["letra"]}, {a}–{b}',
           '# fonte: Perseus Digital Library, tlg0016.tlg001.perseus-grc2 (CC BY-SA 4.0), https://github.com/PerseusDL/canonical-greekLit',
           '# edicao: ' + L['edicao'],
           f'# marcas: {exemplo} = capítulo.seção do livro {L["romano"]}, a numeração usual; um parágrafo por capítulo'
           + ('; 121α–121ζ: a história de Rampsinito, como em Hude' if LIVRO == 2 and a <= 121 <= b else ''), '']
    corpo = [L['titulo']] if k == 0 else []
    for c in caps:
        if a <= cap_num(c) <= b: corpo += caps[c]
    open(os.path.join(OBRA, 'original', f'livro{LIVRO}-{a}-{b}.txt'), 'w', encoding='utf-8').write('\n'.join(cab) + '\n' + '\n\n'.join(corpo) + '\n')
print('graves', ngr, 'acentos duplos', ndu, 'letras', len(usadas), 'acentos', len(ac_usados))
