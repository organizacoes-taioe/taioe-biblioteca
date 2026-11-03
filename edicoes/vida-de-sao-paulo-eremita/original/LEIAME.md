# Vida de São Paulo, primeiro eremita: texto latino

Base: *Patrologia Latina* 23 (Migne), col. 17–30, que reproduz a edição de Domenico Vallarsi
(Verona, 1734–1742), em domínio público; fac-símile do Google no Internet Archive,
`patrologiaecurs01goog` (p. 16–22 do PDF), e, para a conferência, outro exemplar,
`bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1845_23` (só a camada de texto).

**Por que não a The Latin Library.** O texto do pedido (`thelatinlibrary.com/jerome/vitapauli.html`,
o mesmo da Wikisource latina) não é o do PL: o rodapé da página diz que vem da edição de Vincent
Hunink (Lovaina, 2002), sobre a tese de Degórski (1987), protegida, com umas 300 diferenças do PL.
Serviu só como ajuda para ler o OCR; nenhuma leitura dele entrou onde o PL diz outra coisa.

Como foi montado (2026-11-02; scripts em `~/.cache/claude-pedidos-0211b/martires/scripts/`, fora
do repositório): as camadas de texto de três exemplares do PL 23 (Internet Archive:
`patrologiaecurs01goog`, `patrologiaecurs256unkngoog` e o `bim_…_1845_23`) foram alinhadas palavra por
palavra com a The Latin Library, para achar as leituras do PL; depois o texto inteiro foi
transcrito à mão das imagens das páginas (220 dpi; os pontos duvidosos a 500 dpi), coluna por
coluna, e conferido de novo contra as três camadas de texto. Sobraram só erros de OCR e as notas.

O que ficou de fora do texto do PL, por ser do editor e não de Jerônimo: os títulos «Prologus» e
«Incipit vita» e os títulos de capítulo em itálico (*Decius et Valerianus Christianorum
persecutores*, *Duo martyres insignes* etc.); as variantes entre colchetes no meio do texto
(«[*Veron.* eo]», «[*Al.* adduci]», «[*ms. Ver.* cogis]» e outras umas 30), ficando a leitura que
Vallarsi imprime fora dos colchetes; as referências entre parênteses («(Virgil. *Aeneid.* II)»,
«(I *Joan.* IV, 18)», «(*Eccle.* III, 7)»); os números das notas e as letras das colunas.

Defeitos de impressão do exemplar, corrigidos: 3 «milies» → «miles»; 4 «ambrorum» → «amborum»;
7 «quescienti» → «quiescenti», «servebat» → «fervebat» (o outro exemplar, `256`, tem «fervebat»);
8 «uiverso» → «universo»; 12 «comitem tale itineris» → «talis», «utram tectum» → «utrum»; 16
«effosam» → «effossam» (a nota de Vallarsi explica *effossam, scilicet humum*).

Mantidos como o PL: a grafia (*j* e *v*, *coelum*, *coepit*, *lacrymae*, *charitas*, *haereditate*,
*pene*, *quicunque*, *genubus*; o *æ* do PL vai como *ae*), «Nonnulli haec et alia» (1), «Gubbam»
(6, em versalete no PL), «cum Antonio» (10), e o fim, «cum poenis suis» (18; outros manuscritos e a
edição de Hunink têm «cum regnis suis»: decisão no `revisao.json`). No cap. 9 os dois versos que
Jerônimo adapta da *Eneida* (II,650 e VI,672) vão em linhas próprias, como no PL.

Os capítulos (1–18) são os do PL, marcados «[1]».
