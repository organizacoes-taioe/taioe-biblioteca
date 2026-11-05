# Vidas paralelas, Alexandre e César: texto grego

Base: Bernadotte Perrin, *Plutarch's Lives*, vol. VII, *Demosthenes and Cicero, Alexander and Caesar*
(Loeb Classical Library, Londres, William Heinemann, e Cambridge, Mass., Harvard University Press, 1919),
p. 224–439 (Alexandre) e 440–609 (César). Perrin morreu em 1920: em domínio público. Perrin não faz edição
crítica própria: parte de Sintenis (Teubner, 2ª ed., 1873–1875) e o compara com Coraës e Bekker, nas notas.

Não usamos o texto de Ziegler (Teubner, 1935 em diante), que é protegido.

## De onde vem

- Transcrição: Perseus Digital Library, `tlg0007.tlg047.perseus-grc2` (Alexandre) e `tlg0007.tlg048.perseus-grc2`
  (César), em https://github.com/PerseusDL/canonical-greekLit (CC BY-SA 4.0). O cabeçalho dos arquivos diz que é o
  texto de Perrin, 1919, vol. 7 (baixado em 2026-11-05).
- Fac-símile: Internet Archive, `plutarchslives07plut` (exemplar da New York Public Library; PDF de 652 páginas,
  Alexandre a partir da p. 240 do PDF, César a partir da p. 458), com OCR do próprio Internet Archive (Tesseract 5).

## Como foi conferido

`ferramentas/extrair.py` lê o XML (capítulos, seções, versos, notas de Perrin); `ferramentas/colacao.py` alinha,
palavra por palavra, o Perseus com o OCR do fac-símile (sem acentos, para achar as palavras diferentes; com acentos,
nas palavras iguais) e grava as listas; `ferramentas/montar.py` aplica as correções e grava estes arquivos.
O OCR é ruim nos espíritos e confunde ζ/ξ, ο/υ, α/ω: só serviu para apontar os pontos, que foram vistos nas imagens
(pranchas de recortes do PDF) quando não eram evidentes.

Correções ao Perseus (o fac-símile de Perrin tem a forma da direita):
- 355 acentos agudos no fim da palavra, no meio da frase, onde Perrin imprime grave (καί → καὶ, τόν → τὸν), só
  onde o OCR do fac-símile mostra o grave (lista em `ferramentas/acentos.tsv`); os outros agudos do Perseus ficaram;
- palavras: Alex. 2.1 ἐν θρᾴκῃ → ἐν Σαμοθρᾴκῃ (o Perseus perdeu a sílaba do fim da linha); 6.1 Φιλονίκου →
  Φιλονείκου; 10.1–2 Πιξόδαρος → Πιξώδαρος; 14.5 ποχὺν → πολὺν; 16.2 βασιλεῖ → βασιλεῖς; 23.4 κόλαζι → κόλαξι;
  33.3 συμμεμῖξαι → συμμῖξαι; 35.1 τὸν πυρὸς → τοῦ πυρὸς; 35.6 πυριγονοῦντα → πυριμανοῦντα, ἢ γένεσις → ἡ γένεσις;
  42.3 ἀνυδρίον → ἀνυδρίαν; 47.2 μαρτνράμενος → μαρτυράμενος, προσαχθῆναι → προαχθῆναι; 49.4 ὑπεροψίαν →
  ὑποψίαν, Λίμνου → Λίμνον; 53.4 τῆς παλινῳδίαν → τὴν παλινῳδίαν; 54.1 Καλλισθένη → Καλλισθένην; 55.1
  ὑπογινομένης → ὑπογενομένης; 63.2 τ ὁ → τὸ; 68.4 τρισχίλαι → τρισχίλια; 70.3 εἶτ’ → εἶτα; 76.4 Σεραπεῖον →
  Σαραπεῖον; Caes. 8.3 οἶ δα → οἶδα; 10.4 τοῦ Κλώδιον → τοῦ Κλωδίου; 12.1 Καλαϊκοὺς → Καλλαϊκοὺς; 15.2 Μετέλλονς
  → Μετέλλους, τ?ε → τε; 41.2 Διὰ → διὰ (duas vezes), «ἐπαρχίας, ἐκ» → «ἐπαρχίας. ἐκ»; 66.3 ἐντυχάνοντι →
  ἐντυγχάνοντι; 68.4 Βροῦτον → Βρούτου; 69.7 ὂψομαι → ὄψομαι;
- os parênteses de Perrin, que o Perseus marca com ʽ…ʼ e às vezes sem fechar (Alex. 14.5, Caes. 2.4, 41.2), voltaram
  a ser ( ).

Lacunas: Perrin imprime «…» onde o texto dos manuscritos se perdeu (Alex. 35.6, Caes. 42.1); aqui também.

Apresentação (não muda o texto): a elisão com ’; maiúscula só no começo de cada capítulo, como em Perrin; as
falas entre “ ”, como o Perseus as marca; os versos citados em linhas `| `; ficaram de fora as notas críticas de
Perrin, a paginação e os títulos correntes.

Pontos que ficaram como no Perseus sem conferir na imagem (o alinhamento não os achou): Caes. 26.3 προσγενόμενοι.

## Numeração e divisão

Capítulos e seções (`[1.1]`) são os do Perseus, os usuais (Alexandre 1–77, César 1–69). Os grupos de capítulos de
cada arquivo e os títulos deles são desta edição (ver `../obra.py`).

O proêmio de Alexandre 1 serve às duas vidas. A *Vida de César* começa abrupta, já no casamento com Cornélia,
sem a infância nem a família: muitos estudiosos acham que o começo dela se perdeu. Perdeu-se também a comparação
(*synkrisis*) que Plutarco costuma pôr no fim de cada par.

## Notas críticas de Perrin que tocam a tradução

Alex. 10.2 ἰὼν … δωμάτιον (correção anônima, depois de Amyot); 39.2 ἑαυτῷ; 47.2 ἐφῆκε (correção de Coraës);
58.2 ἀπότομον (Coraës); 68.2 ἀδικίαν (Bekker: ἀκηδίαν, «indiferença»); 70.2 ἄλλον (Bekker, depois de Coraës; os
manuscritos têm καλὸν); 74.3 οἰμωξομένων; 75.2 ἥ, καταρρέοντος, ἀνεπλήρου, κατάφοβον (Coraës, Bekker).
Caes. 2.3 Ἴουγκον (Sintenis); 21.1 Καῖσαρ δ’ αὐτὸς (Sintenis²); 28.4 ναῦν (acréscimo de Reiske); 42.1 lacuna
(o conteúdo perdido está no *Pompeu*, 67.2; Sintenis exclui a frase como glosa); 57.3 ἀνέγκλητον ἑαυτόν.
A tradução segue o texto de Perrin em todos.
