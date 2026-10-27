# Carta a Diogneto: texto grego

Base: Kirsopp Lake, *The Apostolic Fathers*, vol. 2 (Loeb, 1913), p. 350–378, na digitalização do
First1KGreek (`tlg0646.tlg004.1st1K-grc1.xml`, CC BY-SA 4.0; baixado em 2026-10-26; o First1KGreek
cataloga a obra sob Pseudo-Justino, porque o manuscrito a trazia entre obras atribuídas a São
Justino). A digitalização é da reimpressão de 1917, que repete o texto de 1913. Edições críticas
modernas protegidas (Marrou, *Sources Chrétiennes* 33 bis, e outras) não foram usadas.

Como foi montado (`~/.cache/diogneto-tmp/scripts/`, fora do repositório): do XML saíram as notas e
as referências bíblicas de margem (`note`, `bibl`); os dois-pontos viraram o ponto alto grego (·),
que o XML troca; o apóstrofo, que o XML grava como sinal combinante (̓), virou ’, e as formas
estropiadas δἰ e παῤ voltaram a δι’ e παρ’; um parágrafo por capítulo, com os versículos marcados
`[1.1]`. O título de Lake abre a primeira parte.

A conferência foi feita com a Wikisource grega e, onde as duas divergem, com o fac-símile da
edição de Lake (Internet Archive, `TheApostolicFathersV2`, p. 350–378). A Wikisource tem muitos
erros de digitação e pulos de linha (até um «Ἐπιστολὴ ὁρῶ» no começo), e por isso só serviu de
alarme: toda correção abaixo foi confirmada no impresso.

Erros de digitalização corrigidos:
7.1 ἐπιγειον → ἐπίγειον; 7.2 «τὰ ἄστρα: τῷ» → «τὰ ἄστρα τῷ» (pontuação que o impresso não tem);
8.2 e 9.2 os parênteses de Lake, que o XML trocou por ʽ…̓ e ʽ…ὖ: «(οὗ μέλλουσι χωρήσειν αὐτοί,
τοῦτο καλοῦσι θεόν)» e «(ὢ τῆς ὑπερβαλλούσης φιλανθρωπίας καὶ ἀγάπης τοῦ θεοῦ)»; 10.3 τὸ → τὸν
(«τὸν οὕτως προαγαπήσαντά σε»); 10.4 «μιμη τὴς» → μιμητὴς, θαυμάσῃ → θαυμάσῃς, e o ponto depois
de θεοῦ, que faltava («…γενέσθαι θεοῦ. δύναται θέλοντος αὐτοῦ»); 10.5 três palavras estropiadas no
fim da linha: καταδυναστεύειν, βούλεσθαι, βιάζεσθαι; 11.6 ᾅδεται → ᾄδεται. As lacunas de 7.6–7.7
e 10.1, que Lake marca com pontos, ficam com reticências (…).

Lugares em que a Wikisource (ou outras edições) leem diferente e foi mantido Lake:
2.1 λόγου καινοῦ (Wikisource: λόγον); 11.5 ὅρκια πίστεως (Wikisource: ὅρια); 7.2 «τὴν θάλασσαν
ἰδίοις ἐνέκλεισεν», sem o ὅροις que outros editores acrescentam (a tradução diz «nos seus
limites», que o grego subentende).

Emendas antigas que Lake imprime e que mudam o sentido (o manuscrito único se perdeu em 1870; as
leituras dele vêm das cópias e colações feitas antes):
5.7 κοίτην («não o leito»), onde o manuscrito repetia κοινήν («põem a mesa em comum, mas não
comum»); 12.9 καιροί («os tempos»), onde o manuscrito trazia κηροί («os círios»; outros corrigem
para χοροί, «os coros»). As duas estão em `revisao.json`.
