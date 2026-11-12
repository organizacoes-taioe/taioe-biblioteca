# Heródoto, Histórias: texto grego

Base: A. D. Godley, *Herodotus*, vol. I, *Books I and II* (Loeb Classical Library, Londres, William Heinemann, e
Nova York, G. P. Putnam's Sons, 1920). Godley morreu em 1925: em domínio público. Godley marca entre colchetes o que
tem por acréscimo de copista e põe as variantes que pesaram nas notas de rodapé (que não reproduzimos).

O texto de Hude (Oxford, 1908; 3ª ed. 1927; Hude morreu em 1936) também é livre no Brasil, mas não há transcrição
dele conferível; ficamos com Godley, que tem transcrição e fac-símiles. Rosén (Teubner, 1987–1997) e Wilson (Oxford,
2015) são protegidos.

Por enquanto só o livro I (Clio). A obra cresce por livros, em pedidos seguintes; cada livro tem os seus arquivos
`livro<n>-<a>-<b>.txt` e é montado pelos mesmos scripts (`../ferramentas/`, trocando o número do livro).

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

## Numeração e divisão

Capítulos e seções (`[5.2]`) são os do Perseus, os usuais (livro I: 216 capítulos); o proêmio é `[1.0]`. Os grupos
de capítulos de cada arquivo e os títulos deles são desta edição (ver `../obra.py`).
