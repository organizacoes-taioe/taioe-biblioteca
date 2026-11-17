# Heródoto, Histórias: texto grego

Base: A. D. Godley, *Herodotus*, vol. I, *Books I and II* (Loeb Classical Library, Londres, William Heinemann, e
Nova York, G. P. Putnam's Sons, 1920). Godley morreu em 1925: em domínio público. Godley marca entre colchetes o que
tem por acréscimo de copista e põe as variantes que pesaram nas notas de rodapé (que não reproduzimos).

O texto de Hude (Oxford, 1908; 3ª ed. 1927; Hude morreu em 1936) também é livre no Brasil, mas não há transcrição
dele conferível; ficamos com Godley, que tem transcrição e fac-símiles. Rosén (Teubner, 1987–1997) e Wilson (Oxford,
2015) são protegidos.

Por enquanto os livros I (Clio) e II (Euterpe), os dois do vol. I de Godley, o III (Tália) e o IV (Melpômene), do vol. II, e o V (Terpsícore), do vol. III. A obra cresce por livros, em pedidos
seguintes; cada livro tem os seus arquivos `livro<n>-<a>-<b>.txt` e é montado pelos mesmos scripts (`../ferramentas/`,
com o número do livro no fim: `extrair.py dl/her-grc2.xml 2 l2.json`, `colacao.py . 2`, `acentos.py . 2`,
`montar.py . <obra> 2`; o bloco de cada livro fica em `LIVROS`, no `montar.py`).

## De onde vem

- Transcrição: Perseus Digital Library, `tlg0016.tlg001.perseus-grc2`, em https://github.com/PerseusDL/canonical-greekLit
  (CC BY-SA 4.0), baixado em 2026-11-12. O cabeçalho diz que é o texto de Godley (Loeb, 1920–1925), escaneado em
  Chicago em 1988–1989.
- Fac-símile principal: Internet Archive, `herodotud0000adgo`, a impressão de 1921 do vol. I (Londres, Heinemann, e
  Nova York, Putnam, «MCMXXI»), a mais antiga digitalizada; páginas gregas do livro I = p. 28–296 do PDF. O OCR do
  Internet Archive nesse exemplar não lê grego: fizemos um OCR próprio (Tesseract 5, modelo `grc`, 300 dpi).
- Segunda leitura: o OCR do próprio Internet Archive em `historiesvolumei00hero_249`, reimpressão de 1975 (as mesmas
  chapas: «Revised and reprinted 1926, 1931, 1946, 1960, 1966, 1975»; as revisões tocam a tradução inglesa).

## Como foi conferido

`ferramentas/extrair.py` lê o XML do livro (capítulos, seções, falas, versos, colchetes, lacunas; das notas de Godley
o Perseus só guarda o número); `ferramentas/graves.py` aplica a regra do acento grave, que o Perseus ignora em
centenas de lugares; `ferramentas/colacao.py` alinha, palavra por palavra, o Perseus com as duas leituras do
fac-símile e lista os pontos em que as duas leituras concordam entre si e não com o Perseus; `ferramentas/acentos.py`
separa os pontos de acento em aceitos (classes em que o OCR acerta), recusados (classes em que o OCR erra em série:
o espírito das maiúsculas, ὦν/ὧν, ἦν/ἣν) e a conferir; `ferramentas/pranchas.py` recorta as linhas do fac-símile
para ver os pontos; `ferramentas/montar.py` aplica tudo e grava estes arquivos.

Correções ao Perseus (o fac-símile de Godley tem a forma da direita):
- regra do grave: 120 agudos finais no meio da frase viraram grave (σχεδόν πάντων → σχεδὸν πάντων); 19 acentos
  duplos que não vêm antes de enclítica saíram, ou o segundo virou agudo antes de enclítica (Ἕλληνές λέγουσι →
  Ἕλληνες λέγουσι; ἐντειλάμενὸς οἱ → ἐντειλάμενός οἱ); o agudo da enclítica na palavra anterior (πείθεσθαί μοι,
  γάρ σε). A palavra elidida guarda o acento (οὔτ’). A regra não mexe antes de pontuação nem antes de forma ambígua (οἱ artigo × pronome);
- 141 acentos e espíritos pelo fac-símile (lista em `ferramentas/acentos-aceitos.tsv` e `ACENTOS` em
  `ferramentas/montar.py`), entre eles ὃ δὲ (pronome) onde o Perseus tem ὁ δὲ, os particípios εἴπας, δεύτερα
  advérbio, χώρῃ e χώρη, ἱππεύειν, ἄπαις;
- letras (`CORR` em `ferramentas/montar.py`, todas vistas nas imagens): 32.7 τελευτήσῃ → τελευτήσει; 46.2 e 55.1
  μαντείων, μαντείου → μαντηίων, μαντηίου; 50.2 μὰν → μὲν; 60.5 Ἀηθναίη → Ἀθηναίη; 63.1 τρέπουσι → τράπουσι, 117.2
  τρέπεται → τράπεται; 68.5 Λακεδαιμονίοσσι → Λακεδαιμονίοισι; 74.2 τῇ ἡμέρης → τῆς ἡμέρης; 80.5 ὤσφροντο →
  ὤσφραντο; 82.3 ἀπαμύνοιεν → ἐπαμύνοιεν; 116.3 ὁ Ἀστυάγεος → ὁ Ἀστυάγης; 119.2 ἐκπέμπεν → ἐκπέμπει; 134.3 ἀρχὸν
  τῶν → ἀρχόντων; 164.3 τὰ ἐν τῶν → τὰ ἐκ τῶν, εἰσβάντες → ἐσβάντες; 165.1 Φωκαίες → Φωκαιέες; 170.3 κατά περ ἐς δῆμοι
  → κατά περ εἰ δῆμοι; 172.2 χέασθαι → χρᾶσθαι; 173.3 καὶ νυν ἔτι → καὶ νῦν ἔτι; 176.3 ἐκδημέουσι → ἐκδημέουσαι;
  179.2 τάφου → τάφρου; 193.5 τὸν φοινίκων → τῶν φοινίκων; 199.1 ἀξιούμεναι → ἀξιεύμεναι; 199.5 ὅσσαι → ὅσαι; 202.2
  ὀσμῇ → ὀδμῇ; 205.1 Μασαγετέων → Μασσαγετέων; 216.3 ἀλλ’ γῇ → ἀλλὰ γῇ; 42.2 χρηστοῖσἰ → χρηστοῖσι; 145.1 Αἴγίον → Αἴγιον; 149.1 τῆ → τῇ; 163.2 «μὲν ἦν,
  Ἀργανθώνιος» sem a vírgula; 166.1 ἑξήκόντα → ἑξήκοντα; 171.6 ἀποδείκνῦσι → ἀποδεικνῦσι; 97.1 δίκαν → δικᾶν; 120.1 Ἁστυάγης → Ἀστυάγης; 128.3 Πέρῃσι →
  Πέρσῃσι; 133.4 δὲμὴ → δὲ μὴ; e em 153.1 uma oração
  repetida («χῶρος ἐν μέσῃ ἑωυτῷ προαγορεύουσι· τῇ πόλι», onde Godley tem «χῶρος ἐν μέσῃ τῇ πόλι»: as duas palavras
  do meio vêm da frase anterior), achada na tradução.

A colação não achou palavras perdidas no livro I; a repetição de 153.1 apareceu na lista de «buracos», no meio do
ruído do OCR, e foi confirmada na tradução. Pontos que ficaram como no Perseus, porque o fac-símile não decide (o espírito é ilegível na impressão): ὦν
(«então», jônico) e ᾔδεε.

Apresentação (não muda o texto): a elisão com ’; maiúscula no começo de cada capítulo, como em Godley; as falas
entre “ ”, como o Perseus as marca (Godley também usa aspas); os versos dos oráculos em linhas `| `; o que Godley
imprime entre colchetes vai entre colchetes (1.148.2, 167.1, 180.4, 196.5); as lacunas que ele marca com pontos,
«…» (1.92.2, 180.4, 193.2); ficaram de fora as notas críticas de Godley, a paginação e os títulos correntes. O título
do livro, «Α · ΚΛΕΙΩ», junta a letra de Godley ao nome da Musa, que os livros têm desde a Antiguidade.

## Livro II (2026-11-16)

Mesmo método e mesmas fontes (o vol. I de Godley tem os livros I e II): o fac-símile de 1921 nas p. 300–522 do PDF
(páginas pares), lido pelo Tesseract; a 2ª leitura, o OCR do Internet Archive da reimpressão de 1975, do título «BOOK
II» até o índice. A colação deu 72 pontos de letras, 406 de acentos (21 aceitos pela regra, 57 a ver), 123 fracos e
7 buracos; 28 pontos vistos nas imagens. O Perseus do livro II já traz quase todos os graves (a regra mudou 5).

Correções ao Perseus (o fac-símile tem a forma da direita): 17.4 τρέπεται → τράπεται, 80.1 ἐκτρέπονται → ἐκτράπονται,
92.5 τρέπουσι → τράπουσι, 120.4 ἐπιτρέπειν → ἐπιτράπειν (as formas jônicas, como no livro I); 29.4 λίμνην → λίμνη;
45.3 εὐμένεια → εὐμενείη; 47.2 δικαιοῦσι → δικαιεῦσι; 67.1 ἀποφανόντες → ἀποθανόντες; 69.2 ταριχεύσαντες →
ταριχεύοντες; 93.1 ἐκπλέουσι → ἐκπλώουσι; 93.2 ἡγεμονία → ἡγεμονίη; 96.4 ῥιπὶ → ῥίπεϊ; 116.3 ἀριστείῃ → ἀριστηίῃ;
121ζ.1 διανέμοντα → διαπέμποντα; 158.3 ὑπώρεαν → ὑπωρέην; 169.2 βασιληία → βασιλήια (o palácio); duas palavras que o
Perseus perdeu: 47.1 ὑός (no começo da página do fac-símile) e 113.3 τὸν τοῦ στόματος. Acentos: 28.4 ἄβυσσοι εἰσὶ
(Godley não trata εἰσί como enclítica aqui), 41.6 τἄλλα, 59.3 Ἡλίῳ, 61.1 πρότερόν μοι, 149.4 ἔστι, 149.5 ὕδωρ e 14
aceitos pela regra (`ferramentas/acentos-aceitos-l2.tsv`; os 6 ἡ → ἣ da leitura ficaram de fora: são o artigo, ἡ δὲ
τρίτη, e o OCR inventa o acento). Em 90.2 Godley imprime αἱ ἱρέες, erro tipográfico; o Perseus o corrige (οἱ), e
ficamos com a correção. As referências que o Perseus acrescenta às citações de Homero (116.3–5) saem.

Os capítulos 121α–121ζ (a história de Rampsinito e do ladrão) têm a numeração de Hude, que o Perseus escreve 121A–121F;
a marca é `[121α.1]`. Colchetes de Godley no livro II: 116.2, 143.4, 148.4; lacunas, «…»: 40.1, 86.2, 175.4.

## Livro III (2026-11-16)

Base: A. D. Godley, *Herodotus*, vol. II, *Books III and IV* (Loeb, Londres, Heinemann, e Nova York, Putnam, 1921).
Godley morreu em 1925: em domínio público no Brasil; nos EUA também (publicado antes de 1931). Mesmo método:
- fac-símile principal: Internet Archive `herodotus0002adgo_j1l1`, a impressão de 1921 do vol. II («MCMXXI», a 1ª);
  páginas gregas do livro III = p. 26–218 do PDF (pares), lidas pelo Tesseract (`grc`, 300 dpi; OCR em `ocr3/`,
  páginas em `pag3/`, na pasta de trabalho);
- segunda leitura: o OCR do Internet Archive em `herodotus0000hero` (Harvard, reimpressão de 2000 da edição
  «revised and reprinted 1938»; mesmas chapas), da 2ª ocorrência de «BOOK III» até «BOOK IV». As outras cópias do
  vol. II no Internet Archive (a de Toronto é de 1928) têm OCR sem grego.

A colação deu 47 pontos de letras (quase todos ζ lido como ξ e maiúsculas), 390 de acentos (43 aceitos pela regra,
36 a ver), 89 fracos e 6 buracos; 31 pontos vistos nas imagens. Correções ao Perseus (o fac-símile tem a forma da
direita): 2.2 παρατρέπουσι → παρατράπουσι, 21.3 τρέπουσι → τράπουσι, 65.3 ἀποτρέπειν → ἀποτράπειν, 81.1 ἐπιτρέπειν →
ἐπιτράπειν, 157.1 ἐπιτρέπεσθαι → ἐπιτράπεσθαι (as formas jônicas, como nos livros I e II); 12.1 ἔκειτο → ἐκέετο,
22.4 προκεῖσθαι → προκέεσθαι, 34.2 προσκεῖσθαι → προσκέεσθαι, 100.1 κεῖται → κέεται (jônico; em 57.2 Godley
imprime ἀνάκειται, e fica); 14.11 Αἴγυπτους → Αἴγυπτον; 21.2 a palavra que o Perseus perdeu, «ἀνήρ ἐστι δίκαιος»;
34.5 «οἷον σὲ ἐκεῖνος» (Godley acentua o pronome). Ficaram como no Perseus, conferidos: 16.1 τἆλλα, 52.3 ἆσσον, 82.3
γνώμῃσί τε. Os 43 acentos aceitos: `ferramentas/acentos-aceitos-l3.tsv` (quase todos ὃ pronome antes de δέ).

Colchetes de Godley no livro III: 14.11, 51.2, 59.2, 91.3, 97.2, 149.1; lacunas, «…»: 39.2, 49.1. O oráculo dos
sifnios (57.4) em três versos. Título: «Γ · ΘΑΛΕΙΑ».

## Livro IV (2026-11-16)

Mesmo volume (vol. II de Godley, 1921) e mesmas fontes do livro III: o fac-símile `herodotus0002adgo_j1l1` nas p. 222–430
do PDF (páginas pares; OCR em `ocr4/`, páginas em `pag4/`, na pasta de trabalho) e a 2ª leitura `herodotus0000hero`, da
2ª ocorrência de «BOOK IV» até o índice. A colação deu 68 pontos de letras (quase todos ζ lido como ξ e maiúsculas),
473 de acentos (48 aceitos pela regra, 108 a ver), 108 fracos e 11 buracos; 44 pontos vistos nas imagens.

Correções ao Perseus (o fac-símile tem a forma da direita): 3.2 μετά γε → μετὰ δὲ; 4.1 Δαρεῖυς → Δαρεῖος; 20.2 κατʼ
ὅσον → κατόσον (Godley imprime numa palavra só); 48.3 Ὀρδησσὸς καὶ μέσου → Ὀρδησσὸς διὰ μέσου; 54.1 Ὑβλαίην →
Ὑλαίην; 57.1 λίμνην καλεόμενον → καλεομένην; 60.2 τρέπεται → τράπεται (jônico, como nos livros I a III); 64.3
ἀποδερμάτων → ἀποδαρμάτων; 73.2 Σκύψαι → Σκύθαι, 101.2 Σκυψέων → Σκυθέων; 78.4 ἐγκλῄσειε → ἐγκληίσειε; 119.4 a
palavra que o Perseus perdeu, «ἐπίῃ καὶ ἐπὶ τὴν ἡμετέρην»; 148.1 οἰκηιούμενος → οἰκηιεύμενος; 148.3 Μεμβιάρου →
Μεμβλιάρου; 156.3 Βλατέα → Πλατέα; 160.1 κλέεται → καλέεται; 163.3 ἐξοπτήσεις → ἐξοπτήσῃς; 186.2 δικαιοῦσι →
δικαιεῦσι (como no livro II); 201.1 Βορκαίους → Βαρκαίους; 201.3 ἐξῄσαν → ἐξήισαν; 203.3 Ἀρυνάνδεω → Ἀρυάνδεω.
Acentos: 69 conferidos à mão (`ACENTOS4` no `montar.py`: o trema de Godley nos dativos jônicos, ἔτεϊ, πλήθεϊ, θέρεϊ,
μεγάθεϊ, e em Τάναϊς, Βορυσθενεϊτέων, Κολάξαϊς; τῷ por τῳ em 5.1, 8.3 e 9.5; ὑπὲρ por ὕπερ; αὐτή em 9.4; ἦρξαν,
ἁμάξῃ, ἕστηκε, εἷς, οἷά, κυματώγην) e 47 aceitos pela regra (`ferramentas/acentos-aceitos-l4.tsv`). Ficaram como no
Perseus, conferidos: 27.1 ἓν, 80.2 δι’, 114.4 ἐποίησαν, 144.1 ἐλίπετο, 149.1 τοιγαρῶν, 148.2 Τηΰγετον, 165.1 τἆλλα,
5.4 τούτου, 71.1 σελίνου; e os espíritos que o OCR troca (εὖρος, ὤμους, αὖτις, ἕψομαι, ἓξ, ἦ μέν, o dórico αἰ).

Sem colchetes de Godley no livro IV; lacunas, «…»: 47.2 e 149.2. Versos: o de Homero em 29.1 (_Odisseia_ 4.85), o
epigrama de Mandrocles (88.2, quatro versos) e os oráculos de Bato e de Cirene (155.3, 157.2, 159.3). Título:
«Δ · ΜΕΛΠΟΜΕΝΗ».

## Livro V (2026-11-17)

Base: A. D. Godley, *Herodotus*, vol. III, *Books V–VII* (Loeb, Londres, Heinemann, e Nova York, Putnam, 1922).
Godley morreu em 1925: em domínio público no Brasil; nos EUA também (publicado antes de 1931). Mesmo método:
- fac-símile principal: Internet Archive `in.ernet.dli.2015.183370`, a 1ª impressão do vol. III («MCMXXII», Londres e
  Nova York; digitalização da Digital Library of India, 600 dpi, preto e branco); páginas gregas do livro V = p. 18–160
  do PDF (pares), lidas pelo Tesseract (`grc`, 300 dpi; OCR em `ocr5/`, páginas em `pag5/`, PDF em `dl5/`, na pasta de
  trabalho, com o roteiro `scripts/ocr1922-l5.sh`);
- segunda leitura: o OCR do Internet Archive em `herodotus19203hero` (reimpressão de 1982: «First printed 1922;
  reprinted 1928, 1938, 1950, 1957, 1963, 1971, 1982»; mesmas chapas), da linha «BOOK V» até «BOOK VI». Das outras
  cópias do vol. III, a de Toronto (`herodotuswitheng03herouoft`) tem OCR sem grego, e as da Digital Library of India
  (`in.ernet.dli.2015.30897`, `…69771`) leem pior (93 % das palavras iguais ao Perseus, contra 95 %).

A colação deu 39 pontos de letras (quase todos ζ lido como ξ e maiúsculas), 488 de acentos (17 aceitos pela regra, 24 a
ver), 45 fracos e 14 buracos; 34 pontos vistos nas imagens. Dois «aceitos pela regra» o fac-símile desmentiu (1.3
πολλόν τε e 78.1 ἓν: as duas leituras erraram igual) e saíram da lista. Correções ao Perseus (o fac-símile tem a forma da
direita): 9.3 Δίγυες → Λίγυες; 15.2 e 61.2 τρέπονται → τράπονται, 86.3 τραπέσθαι → τράπεσθαι (jônico, como nos
livros I a IV); 17.2 Μακεδονίν → Μακεδονίῃ; 23.1 Ἑλλήποντον → Ἑλλήσποντον; 29.2 a palavra que o Perseus perdeu,
«τούτους μὲν τὴν πόλιν»; 41.1 ἔφεδρον → ἔπεδρον (jônico); 52.4 ἐς βάλλοντι → ἐσβάλλοντι; 59.1 ἀμφιτρύων →
Ἀμφιτρύων (o verso da trípode); 79.2 οὐκ ὦν → οὐκῶν; 83.3 ἱροεργίαι → ἱρουργίαι; 106.3 ἀξιοῦμαι → ἀξιεῦμαι; 106.4
εἴ περ → εἴπερ; 67.3 os parênteses de Godley, «(καὶ γὰρ τοῦτο δεῖ ἀπηγήσασθαι)», que o Perseus perdeu (sobrou um
sinal solto). Em 5.1 Godley imprime «πολλά,·», erro tipográfico (o Perseus o copia): fica πολλάς·. Acentos: 30.4 «φερέγγυος εἰμὶ» e 49.8 «ἐχόμενον ἐστὶ» (Godley não trata εἰμί como enclítica aqui,
como em 2.28.4), 41.2 ἀληθέι, 50.2 χρεὸν, 52.3 εἰσι, 80.1 χρῆσαι, e os 17 aceitos pela regra
(`ferramentas/acentos-aceitos-l5.tsv`, quase todos ὃ pronome antes de δέ). Ficaram como no Perseus, conferidos: 24.3
ὅτι, 52.4 νηυσιπέρητοι, 100.1 Καΰστριον, 50.2 τἆλλα, 60.1 e 61.1 τεῒν, 41.2 ὤχλεον; e 121.1 ἐμπεσόντες, onde Godley
imprime ἐμπεσύντες, erro tipográfico. Os dois «buracos» de 73.2 e 89.3 são notas de rodapé de Godley.

Os capítulos 92α–92η (o discurso de Sosícles, com a história de Cípselo e Periandro) têm a numeração de Hude, que o
Perseus escreve 92A–92G; a marca é `[92α.1]`, como `[121α.1]` no livro II. Sem colchetes de Godley e sem lacunas no
livro V. Versos: as três inscrições das trípodes de Tebas (59–61), o oráculo a Hiparco (56.1), o epigrama da
quadriga de Atenas (77.4) e os oráculos de Cípselo (92β.2–3, 92ε.2). Título: «Ε · ΤΕΡΨΙΧΟΡΗ».

## Numeração e divisão

Capítulos e seções (`[5.2]`) são os do Perseus, os usuais (livro I: 216 capítulos); o proêmio é `[1.0]`. Os grupos
de capítulos de cada arquivo e os títulos deles são desta edição (ver `../obra.py`).
