# São João Clímaco, Escada do Paraíso: convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md` (vale tudo de lá: nunca mesóclise, um bloco traduzido para cada bloco
do original, as marcas no mesmo lugar). Texto-fonte e correções: `original/LEIAME.md`. Traduz-se o grego da
_Patrologia Graeca_ 88 (Migne, 1860, col. 624–1164), que reproduz a edição de Mateus Rader (Paris, 1633) e vai ao
lado. A tradução latina de Rader, impressa na coluna ao lado do grego na PG, serve só para conferir o sentido; as
traduções modernas (Moore 1959, Luibheid–Russell 1982 etc.) são protegidas: não usar.

## Princípio e tom

Português do Brasil culto e simples. Clímaco escreve em sentenças curtas, densas, cheias de definições («A
obediência é…»), imagens, antíteses, jogos de palavras e pequenos casos dos monges que ele conheceu. Manter a
concisão e o ritmo da sentença, a ordem das ideias, as imagens ao pé da letra (a escada, o fogo, a água, o cavalo, o
médico), e as repetições de propósito. Nada de acréscimo explicativo. Sem palavra rara (o Gere não quer «medrou»,
«hoste», «ledo»): vocabulário comum, mesmo nos termos técnicos da vida monástica, que ficam fixos (tabela abaixo).

Tratamento: Clímaco fala ao leitor por _tu_ (ou por _nós_, incluindo-se); a João de Raitu, na carta, por _tu_; os
plurais, por _vós_. Deus e Cristo: _tu_ nas orações. Pronomes de Deus em minúscula (ele, seu).

## Formato

- Uma parte por degrau: `original/degrau-NN.txt` e `traducao/degrau-NN.txt`; as cartas e o prólogo em
  `original/inicio.txt`. Cabeçalho `# titulo: <título da parte>`.
- Primeiro bloco: o título do degrau, como na PG («ΛΟΓΟΣ Α΄. Περὶ ἀποταγῆς βίου.» → «PRIMEIRO DEGRAU. A renúncia
  da vida»). Ver `revisao.json`, «Degrau ou discurso».
- Os parágrafos são os de Rader, divididos por nós em blocos menores nos fins de frase, para a leitura e a
  citação; cada bloco tem a marca `[N.k]` no começo (degrau.parágrafo, numeração desta edição). Não mexer nas marcas.
- `{PG 88.633}` marca a coluna da PG onde ela começa (sai do texto publicado da tradução; fica no grego).
- Colchetes do grego: Rader põe entre colchetes a lição que ele prefere ou a de outro manuscrito, logo depois da
  palavra impressa (περὶ Θεοῦ [θεὸν]). A tradução lê a forma que dá sentido (em geral a dos colchetes) e não
  reproduz o colchete; anotar nas notas do tradutor quando a escolha pesa.
- Os números entre parênteses do grego da PG remetem aos escólios de Elias de Creta: já saíram do texto; os
  escólios não são traduzidos.
- Falas e citações entre “ ”, com ‘ ’ dentro. Itálico `_assim_` só para título de livro e palavra que fica em
  grego. Versos citados (raros): verso livre, linha por linha `| `.

## Escritura

Traduzir como Clímaco cita (a Septuaginta, de memória, muitas vezes adaptando), do grego dele, sem copiar Bíblia
portuguesa. Nomes na forma da liturgia do Brasil (Moisés, Elias, Ló, Davi, Faraó, Amalec, Lázaro, Jacó,
Esaú). Não acrescentar referências. Salmos: se for preciso citar número em nota, na numeração grega.

## Termos fixos

| grego | tradução |
|---|---|
| κλῖμαξ; βαθμός; ἀνάβασις | escada; degrau; subida |
| λόγος (cada uma das 30 partes) | degrau (no título); «discurso» se o próprio texto fala do λόγος como fala |
| ἀπάθεια; ἀπαθής | impassibilidade; impassível |
| ἡσυχία; ἡσυχαστής; ἡσυχάζω | hesíquia; hesicasta; viver na hesíquia (quietude: «quietude» só onde ἡσυχία é o simples sossego exterior) |
| πένθος; πενθέω | pranto; chorar (o pranto «que alegra», χαροποιὸν πένθος: «pranto que traz alegria») |
| κατάνυξις | compunção |
| διάκρισις | discernimento |
| λογισμός, λογισμοί | pensamento, pensamentos (os que assaltam a alma) |
| πάθος, πάθη | paixão, paixões |
| ἀρετή; κακία | virtude; vício (κακία = maldade, só onde é a qualidade moral) |
| ἀποταγή; ἀποτάσσομαι | renúncia; renunciar |
| ἀπροσπάθεια; προσπάθεια | desapego; apego |
| ξενιτεία; ξένος | exílio (voluntário); estrangeiro |
| ὑπακοή; ὑποτακτικός | obediência; o que obedece, o súdito (monge sob um pai) |
| μετάνοια | penitência (arrependimento só onde é o sentimento) |
| μνήμη θανάτου | lembrança da morte |
| ἀοργησία; πραότης | mansidão (ἀοργησία = «ausência de ira» onde o texto contrasta com ὀργή); doçura |
| μνησικακία | rancor |
| καταλαλιά | maledicência |
| πολυλογία; σιωπή | falar muito; silêncio |
| ψεῦδος | mentira |
| ἀκηδία | acédia |
| γαστριμαργία; γαστήρ | gula; ventre |
| ἁγνεία; σωφροσύνη; πορνεία | castidade; temperança (castidade onde o contexto é o corpo); fornicação |
| φιλαργυρία; ἀκτημοσύνη | avareza; pobreza (= não possuir) |
| ἀναισθησία | insensibilidade |
| ἀγρυπνία | vigília |
| δειλία | covardia |
| κενοδοξία; ὑπερηφανία | vanglória; soberba |
| ταπεινοφροσύνη; ταπείνωσις | humildade; humilhação (= abaixamento) |
| βλασφημία (pensamentos de) | blasfêmia |
| ἁπλότης; πονηρία | simplicidade; malícia |
| προσευχή; εὐχή | oração; oração, prece |
| ἀγάπη; πίστις; ἐλπίς | caridade (amor onde é o amor humano); fé; esperança |
| προσβολή, συνδυασμός, συγκατάθεσις, αἰχμαλωσία, πάλη (degrau 15) | sugestão, diálogo, consentimento, cativeiro, luta |
| νοῦς; ψυχή; καρδία | mente; alma; coração |
| ἡγούμενος; ποιμήν; πατήρ; γέρων | superior; pastor; pai; ancião |
| κοινόβιον; μονή; ἀσκητήριον | cenóbio; mosteiro; mosteiro (ascetério só se for preciso distinguir) |
| μοναχός; μονάζων | monge |
| ἀσκητής; ἄσκησις; ἀγών; ἀγωνιστής | asceta; ascese; luta, combate; lutador |
| δαίμονες; δαίμων; διάβολος | demônios; demônio; diabo |
| κοσμικός, κοσμικοί | do mundo, os do mundo (os leigos) |
| θεωρία; πρᾶξις | contemplação; prática |
| θεολογία; θεολόγος | teologia; teólogo |
| φωτισμός | iluminação |

Acrescentar aqui o que for fixado na tradução de cada degrau (nas notas do tradutor primeiro).

## Nomes

João (Clímaco, o Sinaíta, o Escolástico); João, superior de Raitu (Ῥαϊθοῦ: **Raitu**); o monte Sinai; Menas;
Isidoro (o de Alexandria); João Sabaíta; Acácio; Mena; Lourenço; Macedônio; Abacir; Jorge Arsilaíta; Arsênio;
Antíoco; Moisés; Elias; Hilarião; Basílio; Gregório (o Teólogo). Lugares: Alexandria, o Egito, a Tebaida, o
«Cárcere» (φυλακή, o mosteiro dos penitentes do degrau 5: «o Cárcere»). Acrescentar aqui os nomes de cada degrau.

## Notas do tradutor

Cada tradutor grava `traducao/notas-degrau-NN.md`: termos novos e a solução; passagens difíceis e a leitura
adotada; colchetes e erros da PG que pesaram; e 1 ou 2 candidatas a decisão para o Gere (termo-chave, frase
célebre, jogo de palavras), com o grego, a tradução adotada e uma ou duas alternativas.
