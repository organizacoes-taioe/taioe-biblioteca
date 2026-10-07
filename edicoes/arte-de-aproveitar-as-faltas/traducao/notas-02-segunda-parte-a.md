# Notas do tradutor: A arte de aproveitar as próprias faltas, Segunda parte, capítulos I a IV

Arquivo: `traducao/02-segunda-parte-a.txt`. Texto-base: `original/02-segunda-parte-a.txt` (6e édition, 1894, estabelecida do scan; ver `original/LEIAME.md`). Corresponde às págs. 49 a 113 do livro. Um tradutor anterior deixou blocos parciais numa pasta temporária, que não foram usados: a tradução foi feita de novo, inteira, e substitui qualquer versão anterior.

## O que foi conferido

- **Blocos:** 264 no original e 264 na tradução, na mesma ordem: 141 parágrafos de texto, 4 títulos `## ` e 119 notas `¤ [n]`. São as contagens do LEIAME. A sequência de tipos de bloco (título, parágrafo, nota) é idêntica nos dois arquivos.
- **Linhas:** 532 nos dois arquivos, com as linhas em branco nos mesmos lugares.
- **Títulos:** os quatro `## Chapitre I…IV` viraram `## Capítulo I…IV`, com o título traduzido.
- **Marcas `[X.n]`:** `[II.1]`, `[II.2]`, `[II.3]`, `[II.4]`, no começo do primeiro parágrafo de cada capítulo, iguais e na mesma ordem.
- **Números de parágrafo do autor:** os «1. —», «2. —»… estão iguais, nos mesmos parágrafos (cap. I: 1 a 8; cap. II: 1 a 7; cap. III: 1 a 5; cap. IV: 1 a 4).
- **Chamadas e notas:** as 119 chamadas `[1]`…`[119]` e as 119 notas `¤ [1]`…`¤ [119]` estão iguais, na mesma ordem e nos mesmos blocos (conferido bloco a bloco).
- **Cabeçalho:** só o `# titulo:` foi traduzido («Segunda parte, capítulos I a IV»). As linhas `# fonte:`, `# edicao:` e `# nota:` estão iguais às do original.
- **Tamanho:** nenhum bloco com menos da metade do tamanho do original. O menor é a nota 46 («C'était la pratique de M. l'abbé J. Allemand.» → «Era a prática do padre J. Allemand.»), com 0,81.
- **Pontuação, por bloco:** os «», os «!» e os «?» batem com o original em todos os blocos, salvo no 4.º parágrafo do n.º 4 do cap. I (Segneri), onde as aspas internas da citação de Jeremias passaram a “...”, como manda o guia (§ 6).
- **Itálicos:** os `_…_` batem com o original, salvo em cinco notas em latim que estão em redondo no impresso (notas 2, 15, 39, 40 e 83). Pus em itálico, pela regra geral (palavra estrangeira em itálico), como fizeram `01-primeira-parte.txt` e `02-segunda-parte-b.txt`.
- **Mesóclise:** o grep do CONVENCOES não achou nada. A varredura em Python com a mesma regex, terminada em `(?![A-Za-zÀ-ÿ])`, também não. Foram evitadas, entre outras: *je m'en repentirai* → «eu me arrependerei»; *nous nous bornerons* → «vamos limitar-nos»; *on dira* → «dirão»; *je me glorifierai* → «eu me gloriarei».
- **Versos:** não há versos em francês. A nota 2 traz seis versos latinos do *Pange lingua* da Paixão («Hoc opus nostræ salutis...»). Ficaram em latim, na mesma linha, com as barras, como no original.
- **Script de conferência:** `C:\Users\geren\AppData\Local\Temp\claude\arte-de-aproveitar-as-faltas-02-segunda-parte-a-r2\scripts\conf.py` (blocos, tipos, marcas, chamadas por bloco, números do autor, tamanho, itálicos, aspas e sinais, cabeçalho, mesóclise).

## Decisões gerais

- **Tratamento.** Segue o original, passagem por passagem:
  - **vós:** São Francisco às dirigidas, às filhas da Visitação e aos confessores; santa Chantal à Irmã de Fésigny; Madalena de Pazzi à noviça; Bernières ao amigo; Tissot ao leitor («Acrescentai a isso»); as orações a Deus e a Jesus (Davi, «Vós me perdoareis, Senhor»; Tissot, «Ó Sacerdote eterno... permiti-nos dizer-vos»; o padre de la Colombière; Margarida Maria, «Ó meu único amor, pagai»).
  - **tu:** o amor puro de Deus à alma («Miserável ou covarde que tu foste, humilha-te», cap. II, n.º 4); a alma a si mesma («Eia, meu coração! não queiras mais», cap. I, n.º 7; «ó minha alma... não temas», cap. III, n.º 4); a *Imitação* («tem-te pelo mais frágil de todos»); o *Connais-toi toi-même*.
  - **nós:** a voz de Tissot.
- **Maiúsculas.** As de reverência e de respeito do original ficaram: *Santo* (são Francisco), *Doutor*, *Bem-aventurado Pai*, *Bem-aventurado bispo*, *os Santos*, *os Apóstolos* (onde o impresso as tem), *Superiora*, *Diretora*, *Irmã* (cap. II, n.º 3), *Filha da Visitação*, *Coração* (de Jesus), *Sacramentos*, *Teologia*. *Celui qui* referido a Deus ficou «Aquele que», «Daquele que», «Àquele que». *Évêque*, *Religieuse*, *Directeur* passaram a minúscula, como em `00-avant-propos.txt`.
- **Títulos dos capítulos:** «Aproveitar as faltas para...», sem «próprias», como em `02-segunda-parte-b.txt`. No texto, *l'art d'utiliser ses fautes* → «a arte de aproveitar as próprias faltas» (ou «as nossas faltas», quando Tissot diz *nos fautes*).
- **Referências bíblicas:** abreviadas à portuguesa, sem ponto, como nos outros arquivos: Rm, Is, Sl, Dn, Ag, Lm, Nm, Pr, Eclo, Tg, Hb, Lc, Gl, Jó, 1 Jo, Mt, Jr, 1 Pd, Cl, 1 Cor. Capítulos e versículos como no impresso (numeração da Vulgata nos salmos).
- **Latim:** fica em latim, sem «[Trad.: …]», que o guia da obra não pede. Onde Tissot traduz o latim ao lado, a tradução dele foi traduzida.
- **Referências das cartas e obras de São Francisco:** «Lettre à une Dame, 614e ; collect. Blaise» → «Carta a uma senhora, 614.ª; coleção Blaise»; «coll. Blaise» (notas 109 e 110) → «coleção Blaise», uniformizado; «édit. Meyer» → «edição Meyer»; «Entretien IIIe, De la Fermeté» → «Colóquio III, Da firmeza»; «_Introd. à la vie dévote_, IIIe partie» → «_Introd. à vida devota_, III parte»; «1re partie» → «1.ª parte»; «_Avertissement aux confesseurs_» → «_Avisos aos confessores_» (como em `02-segunda-parte-b.txt`, nota 27).
- **Títulos de outras obras:** em francês, latim ou italiano, em itálico, como manda o guia: _Chrétien intérieur_, _Année sainte de la Visitation_, _Le cœur de Sainte Gertrude_, _Vie_ (de dom Rey), _Notice sur la Mère M.-Mélanie Pommeroy_, _Traité de l'Espérance chrétienne_, _De la vie et des vertus chrétiennes_, _Œuvres complètes_, _Physiologue_, _Esprit de S. François de Sales_, _Vie du Bienheureux François de Sales_, _Manna dell' anima_, _Cristiano istruito_, _Manuale Pauperum_, _Christus patiens_, _Catena aurea_, _De summo bono_, _De gradibus humilitatis_ etc. Exceções: «l'_Imitation_» → «a _Imitação_» (forma consagrada); «l'auteur de _Philothée_» → «o autor da _Filoteia_»; a _Suma de santo Tomás_ (o itálico do impresso cobre «de saint Thomas»).
  - Nas notas, o subtítulo francês depois do título da obra de dom Gay foi traduzido («Da esperança», nota 89), como em `01-primeira-parte.txt` (nota 71).
- **Datas:** «20 giugno» (nota 24), «8 avril 1602», «14 novembre», «1er novembre 1871» etc. → «20 de junho», «8 de abril de 1602», «14 de novembro», «1.º de novembro de 1871».
- **Citações da Filoteia** (notas 14, 51, 53, 55, 60, 74, 76: III.6, I.12, III.5, I.11, III.6). A nossa Filoteia só tem, por enquanto, a oração e o prefácio. As passagens foram traduzidas diretamente do texto que Tissot cita e devem ser harmonizadas quando aqueles capítulos existirem. A principal é a longa citação de III.5 (cap. I, n.º 7: «Certamente, nada nos pode humilhar tanto...»).
- **Vocabulário antigo de São Francisco** (guia da Filoteia, § 2): *ains* → «antes», «mas sim»; *voirement* → «verdadeiramente», «na verdade»; *iceux* → «eles»; *ès* → «nas»; *Or sus*, *Sus* → «Eia, pois», «Eia»; *marri* → «pesaroso»; *chopper* → «tropeçar»; *broncharde* → «tropeçona».

## Termos

| francês | tradução | observação |
|---|---|---|
| utiliser ses fautes | aproveitar as faltas | guia, § 5 |
| abjection; aimer son abjection | abjeção; amar a própria abjeção | guia, § 5 |
| agréer l'abjection; agrément | aceitar a abjeção; aceitação | cap. II, n.º 1 e 5 |
| néant; néantise | nada; o nosso nada | cap. I, n.º 3: «nadidade» seria raro demais |
| infirmité (moral) | fraqueza | guia, § 5; *infirmités spirituelles* (santa Gertrudes) → «fraquezas espirituais» |
| infirmité de l'enfant; un malade | enfermidade da criança; doente | físico |
| reconnaissance (envers Dieu) | gratidão | cap. I, n.º 6–7 |
| la connaissance engendre la reconnaissance | o conhecimento gera o reconhecimento | cap. I, n.º 7 (Filoteia III.5): «reconhecimento» guarda o jogo e o sentido de gratidão |
| bienfaits / méfaits | benefícios / malefícios | o par do Santo passa |
| par le menu | por miúdo | |
| superbe | soberba | |
| industries (do demônio; de Deus) | expedientes | cap. I, n.º 2; cap. III, n.º 3 |
| verge de correction, de probation, d'indignation | vara de correção, de provação, de indignação | Segneri |
| tenant des pécheurs; caution des pécheurs | fiador dos pecadores | cap. II, n.º 2: ver passagens difíceis |
| livrée du péché | libré do pecado | |
| chétiveté; chétif, chétive | pequenez; mesquinho, mesquinha; pobres (criaturas) | |
| promptitude (de Bernières) | arrebatamento | o acesso de cólera |
| froissement | mágoa | cap. II, n.º 5 |
| âmes douillettes | almas melindrosas | |
| pomme d'amour | pomo de amor | |
| pointilleuses fidélités | fidelidades minuciosas | |
| lâcheté | frouxidão | cap. II, n.º 1 (Madre Chappuis) |
| fonds (para a eternidade) / trame / ourdir | fundo / trama / urdir | a imagem é a do tecido; «fundo» guarda os dois sentidos de *fonds* |
| vertus mitoyennes | virtudes intermediárias | cap. IV, n.º 1 |
| actuellement miséricordieux | misericordioso em ato | cap. IV, n.º 1: «atualmente» se leria como «hoje» |
| coulpe | culpa | |
| le divin Samaritain | o divino Samaritano | |
| supériorité (cargo) | superiorato | |
| le chandelier | o candelabro | |
| prince de la chaire italienne | príncipe do púlpito italiano | Segneri |
| l'Ange de l'école | o Anjo da Escola | santo Tomás |
| publiciste | publicista | Louis Veuillot |
| Anoméens | anomeus | nota 41 |

**Nomes:** santo Agostinho, são Bernardo, são João Crisóstomo, santo Tomás, santo Isidoro, santo Optato de Milevi, são Gregório de Nissa, são Gregório Magno, são Jerônimo, Boécio, santo Epifânio, são Vicente Ferrer, Longuinho; Sansão, os filisteus, Davi, Salomão, Jó, Jeremias, Elias, Jezabel, são Pedro, são Paulo, são Tiago, são João, são Mateus, Madalena; santa Gertrudes, santa Madalena de Pazzi / santa Maria Madalena de Pazzi (como o impresso varia), santa Catarina de Sena, a Madre Teresa, santa Teresa, a bem-aventurada Margarida Maria; santa Chantal; Pio IX; dom Gay, dom Pie, dom Rey, dom Camus; o padre Segneri, o padre Alvarez, o padre Varin, o padre La Rivière, o padre de la Colombière (o «V. Père C. de la Colombière» → «o venerável padre C. de la Colombière»; «Vén. P.» na nota 87 → «Ven. padre», como «Ven. Cl.» em `01`), o padre Gaut., o reverendo padre Cros, S. J., o cônego Ruffin, o padre J. Allemand; o senhor de Bernières (-Louvigny); Madre Maria de Sales Chappuis, Madre Angélica Arnaud, Madre de Soudeilles, Irmã C.-E. Cortelot, Irmã F.-A. de la Croix de Fésigny, Irmã M.-A. de Mayen, Irmã F.-G. de la Grave, a senhora d'Aix; Ven. Alexandre de Saint-François; Raoul d'Asti, Linée; Bossuet, Fénelon, Louis Veuillot; Paray-le-Monial, Troyes, Thonon, Annecy, Genebra, Constantinopla, Antioquia.

## Passagens difíceis

- **Cap. I, n.º 1, *Ne pas nous décourager, ne pas même nous étonner...*** O infinitivo de abertura ficou flexionado («Não nos desanimarmos, nem sequer nos espantarmos...: são essas disposições...»), para guardar o movimento da frase.
- **Cap. I, n.º 1, *nous croirons mieux et nous nous associerons plus activement aux desseins de Dieu*.** Um só complemento para dois verbos; em português, «quanto mais firmemente crermos nos desígnios de Deus... e mais ativamente nos associarmos a eles».
- **Cap. I, n.º 2, *quand elle semblerait devoir germer*.** «Quando pareceria que devesse germinar»: a concessiva irônica (era de esperar que brotasse por si; ao contrário, encontra o orgulho).
- **Cap. I, n.º 3, *elles éclairent et convainquent de néant les forces vives*.** «Iluminam as forças vivas mais íntimas da alma e as convencem do seu nada»: *convaincre de* no sentido jurídico (provar contra alguém).
- **Cap. I, n.º 3, *nous sommes de pauvres gens, qui ne pouvons guère bien faire*.** «Somos pobre gente, que pouco bem podemos fazer»: guardei a concordância do Santo com «nós» depois de «gente».
- **Cap. I, n.º 4, *nous demeurions court*.** «Fiquemos aquém»: ficar sem recurso, falhar.
- **Cap. I, n.º 5, *C'est une grâce à la misère de l'homme qu'il glisse*.** «É uma graça concedida à miséria do homem que ele escorregue».
- **Cap. I, n.º 5, *la leur montrant éphémère*.** Desfiz o pronome duplo: «mostrando-lhes que ela é efêmera». «Mostrando-lha» seria correto, mas pesado.
- **Cap. I, n.º 6, a aspa solta depois da nota 47.** O impresso fecha uma aspa («...le ver de mon orgueil[47]. »») que não foi aberta. Mantida, como nos outros arquivos se mantiveram as aspas desemparelhadas do impresso. A citação de dom Rey parece começar em «A exemplo de...» ou em «farei».
- **Cap. I, n.º 6, *il regarde l'humilité de ses serviteurs*.** Eco do *respexit humilitatem* do Magnificat; «ele põe os olhos na humildade dos seus servos».
- **Cap. I, n.º 6, *la reconnaissance*** (santa Gertrudes) e **n.º 7, *La reconnaissance envers Dieu... faire germer*.** «Gratidão» nos dois lugares, para não perder o elo que Tissot faz com o itálico de *faire germer*. Na citação da Filoteia, *la connaissance engendre la reconnaissance* ficou «o conhecimento gera o reconhecimento», que é jogo e é gratidão.
- **Cap. I, n.º 7, *quelque sorte de vanité venait nous chatouiller*.** «Viesse fazer-nos cócegas»: a imagem do Santo fica.
- **Cap. I, n.º 8, *de peur que... ils n'appelassent la foudre*.** «Por receio de que... chamassem o raio sobre os pecadores».
- **Cap. II, n.º 1, *nous devons tous être capables de défauts des uns des autres*.** *Capable de* no sentido antigo de «capaz de conter, de comportar». Traduzi «devemos todos saber suportar os defeitos uns dos outros». O literal («ser capazes dos defeitos uns dos outros») não se entende em português de hoje. É o único lugar em que o verbo foi explicitado.
- **Cap. II, n.º 1, *de la suite desquelles il faut profiter*.** «De cujas consequências é preciso tirar proveito».
- **Cap. II, n.º 1 (Madre Chappuis), *en coupant court*.** «Atalhando»: cortar logo a falta, sem voltas.
- **Cap. II, n.º 2, *tenant des pécheurs*.** Entre aspas no impresso. *Tenant* é o que responde por outro, o que toma a causa de outro. Logo adiante Tissot diz *comme caution des pécheurs*. Pus «fiador dos pecadores» nos dois lugares. Ver as dúvidas.
- **Cap. II, n.º 2, *notre invincible orgueil ne nous tiendra que trop au-dessus de Celui...*.** «O nosso invencível orgulho não deixará de nos manter muito acima Daquele...». O *ne... que trop* («só demasiado») não tem forma direta em português.
- **Cap. II, n.º 3, *précipué*.** Latinismo raro (*præcipuus*): «distinguido e avantajado».
- **Cap. II, n.º 4, *si nous sommes braves*.** «Se somos valentes», pelo contraste com *misérable ou couard*, que vem logo depois.
- **Cap. II, n.º 4, *passe outre à la poursuite de ton avancement*.** «Segue em frente na busca do teu adiantamento».
- **Cap. II, n.º 5, *Je donne du nez en terre*.** «Dou com o nariz no chão», a expressão do Santo.
- **Cap. II, n.º 5, *il faut être bien aises que nous soyons reconnues*.** O Santo fala às irmãs: «é preciso ficarmos bem contentes de sermos reconhecidas tais como somos», no feminino.
- **Cap. II, n.º 6, *de crainte de fâcher la pauvre sœur qui l'est déjà assez*.** «Com receio de afligir a pobre irmã, que já está bastante aflita».
- **Cap. II, n.º 6, *Si bien font les paons*.** «Assim fazem também os pavões».
- **Cap. II, n.º 7, *La main de Dieu ne soutient-elle pas celui qui tombe, quand c'est l'humilité qui la soutient ?*** O *la* parece referir-se à mão, o que faz pouco sentido. Talvez seja *le* (o que cai). O latim de são Bernardo (*In Ps. Qui habitat*, sermão 2) diz, mais ou menos, que cai sob a mão do Senhor aquele a quem a humildade ampara. Traduzi como está: «quando é a humildade que a ampara». Ver as dúvidas.
- **Cap. III, n.º 1 (dom Gay), *Dieu est l'amour*.** «Deus é o amor», com artigo, porque dom Gay retoma logo «il nous aime parce qu'il est l'amour».
- **Cap. III, n.º 1, *régulièrement*.** «Por regra»: segundo a ordem das coisas.
- **Cap. III, n.º 2, *les lèvres de l'agneau... ses mamelles*.** «O úbere».
- **Cap. III, n.º 2, *quel objet plus pitoyable pour une infinie pitié*.** O jogo *pitoyable* / *pitié*, com os dois itálicos, ficou «que objeto mais _digno de piedade_ para uma infinita _piedade!_». «Lastimável» perderia a repetição.
- **Cap. III, n.º 2, *trop peu connu*.** «Que merecia ser mais conhecido».
- **Cap. III, n.º 3, *anéantir celui-là en sauvant celui-ci*.** «Aniquilar aquele salvando este»: *celui-là* é o pecado, *celui-ci* o pecador, e o par «aquele/este» do português tem o mesmo valor.
- **Cap. III, n.º 3, *s'humilie avec tant d'avances amoureuses*.** «Humilha-se com tantas aproximações amorosas»: *avances* são os primeiros passos de quem procura a reconciliação.
- **Cap. III, n.º 4 (Bossuet), o anacoluto *Jésus-Christ... étant la sainteté essentielle, quoiqu'il se plaise..., il aime*.** Ficou o anacoluto, que em português também se lê: «Jesus Cristo, como Filho de Deus, sendo a santidade essencial, embora se compraza..., ama todavia...».
- **Cap. III, n.º 4, *Si le Dieu a été offensé par la coulpe, le Sauveur est glorifié*.** «Se o Deus foi ofendido pela culpa, o Salvador é glorificado»: o artigo diante de «Deus» marca a oposição Deus / Salvador, como no francês.
- **Cap. III, n.º 4, *comme le pélican, ses petits, de ses flancs par eux déchirés*.** Elipse do verbo; ficou «como o pelicano aos seus filhotes, com os flancos por eles dilacerados».
- **Cap. III, n.º 5 (Colombière), *il me fera tout perdre plutôt que l'espérance*.** «Há de fazer-me perder tudo antes de me fazer perder a esperança».
- **Cap. III, n.º 5 (Madre Chappuis), *elles n'affaiblissent pas sa volonté*.** O *sa* é ambíguo (a vontade de Deus ou a da alma). «A sua vontade» guarda a ambiguidade.
- **Cap. IV, n.º 2, *la faiblesse et infirmité de l'enfant déplaît*.** Sujeito duplo com verbo no singular, como no Santo: «a fraqueza e enfermidade da criança desagrada à mãe».
- **Cap. IV, n.º 2, *Ps. VI, 3*.** «Tende misericórdia, Senhor, porque sou fraco», como em `01-primeira-parte.txt` traduziu o mesmo versículo.
- **Cap. IV, n.º 2, *il aura un soin de votre âme... que jamais vous ne sauriez penser*.** «Ele terá um cuidado da vossa alma... tal, que jamais o poderíeis imaginar».
- **Cap. IV, n.º 2, *faisant le sujet de sa gloire sur leur abjection*.** «Fazendo da abjeção deles o motivo da sua glória».
- **Cap. IV, n.º 3, a carta à Madre Angélica.** *Une jeune fille... la pauvre fille... fille de bons désirs* → «uma moça... a pobre moça... moça de bons desejos». *Tout bellement, mon enfant* → «Devagarinho, meu filho». *Il a sauté, il est bien sage, ne pleurez point* → «Deu um pulo, é muito ajuizado, não choreis»: o pai disfarça a queda de pulo; o *vous* do pai ao filho ficou «vós», como no francês. *Elle ne tombera pas aussi d'en haut* → «também não cairá de muito alto».
- **Cap. IV, n.º 4, *une vraie bonne besogne pour la miséricorde de Dieu*.** «Uma verdadeira boa matéria para a misericórdia de Deus»: aquilo em que a misericórdia tem o que trabalhar. «Boa obra» se leria como obra de caridade.
- **Cap. IV, n.º 4 (La Rivière), *qui les détruit jusqu'à une*.** «Que as destrói até a última».

## Remissões de página

- **Não há remissão a páginas deste livro.** As remissões internas são a capítulos e ficaram: «no capítulo terceiro da primeira parte deste livro» (cap. III, n.º 1); «como veremos no capítulo seguinte» (cap. II, n.º 2).
- **Remissões a outros livros**, mantidas como manda o guia (§ 1):
  - nota 47: «Ver a sua _Vie_, pelo cônego Ruffin, pág. 86»;
  - nota 102: «_Œuvres complètes_, t. II, p. 173».
- **Remissão vinda de outro arquivo:** a nota 58 de `02-segunda-parte-b.txt` remete a «na segunda parte, capítulo IV, n.º 2, em nota». O lugar é a nota 108 deste arquivo (a Igreja nos faz apresentar a Deus e à Virgem «o nosso título de pecadores»), e ele está no cap. IV, n.º 2, como diz aquela nota.

## Emendas

O texto-fonte já traz as emendas registradas em `ferramentas/cache/faltas/revisado/emendas.txt` para as págs. 49 a 113. A tradução segue o texto emendado. As que pesam:

- **p. 50, nota 2:** «(Hymn. Passion.)» é leitura incerta do impresso («Passicr.»). Traduzi «(Hino da Paixão.)». Os versos são do *Pange lingua gloriosi... certaminis*, o hino da Paixão, o que confirma a leitura.
- **p. 53:** «dérouler... ses anneaux» por «découler» (emenda conjectural). Traduzi «desenrolar... os seus anéis», que é o que a imagem da serpente pede.
- **p. 60, nota 41 (aqui):** «Anoméens» (incerto no impresso) → «anomeus». É a série de homilias de Crisóstomo *contra os anomeus*; a leitura é segura pelo sentido.
- **p. 70, nota 60:** o número do capítulo está em branco no impresso («IIIe partie, chap.»). Mantido em branco («III parte, cap.»). O lugar é a Filoteia III.6, a mesma das notas 14, 74 e 76.
- As demais emendas do trecho são de grafia e pontuação (*Francios*, *virgnité*, *fortifié*, *ivin*, *acceplait*, *somme*, *innombrabes*, *imperfcetions*, *ustice*, *but : exterminer*, *se dépile* → *se dépite*, *on été*, *résolulions* etc.) e não afetam a tradução.

Fora do `emendas.txt`, notei no texto-fonte:

- **cap. I, n.º 5:** «disentils», por «disent-ils». O hífen se perdeu na retirada da hifenização de fim de linha. Traduzi «dizem eles». Convém corrigir no original.
- **nota 43:** «_De gradibus humilitatis._ Cap.», sem número, como no impresso. Mantido.
- **cap. IV, n.º 2:** os parágrafos das notas 110 e 111 abrem aspas e não as fecham. É o uso do impresso para citações seguidas; mantido.

Referências erradas do impresso, mantidas como estão (guia, § 3):

- nota 29: «Prov. XXX, 13», quando o texto, logo antes, dá «Prov. XXX, 23», que é o lugar certo;
- cap. III, n.º 2: «Ps. LXVI, 11» para *hæc mutatio dexteræ Excelsi*, que é o Sl LXXVI, 11;
- cap. IV, n.º 2: «Rom. VIII, 24» para *Ó miserável de mim!*, que é Rm VII, 24;
- cap. IV, n.º 2: «I Cor. XII, 9» para *Eu me gloriarei nas minhas fraquezas*, que é 2 Cor XII, 9;
- notas 15 e 26: o mesmo texto de Nm XXIV, 4, duas vezes, como no impresso.

## Dúvidas para quem coordena

1. **«Fiador dos pecadores»** para *tenant des pécheurs* (cap. II, n.º 2) e *caution des pécheurs* (n.º 2, adiante). A palavra entre aspas no impresso parece ser citação (talvez de são Francisco). Se se quiser marcar a diferença, *tenant* poderia ser «o que responde pelos pecadores».
2. **A mão de Deus em são Bernardo** (cap. II, n.º 7): «quando é a humildade que *a* ampara». Se o *la* do impresso for erro por *le*, a frase fica «que *o* ampara», com sentido mais claro. Mantive o impresso.
3. **Nomes próprios de religiosos.** Pus em português os prenomes que têm forma corrente (*Maria de Sales Chappuis*, *Angélica Arnaud*, *Margarida Maria*, *Maria Madalena de Pazzi*), como `01` fez com *dom Carlos Augusto de Sales* e `02-b` com *Cláudio de la Colombière*. Deixei em francês os nomes de religião pouco conhecidos ou ligados a título de obra (*Alexandre de Saint-François*, *M.-Mélanie Pommeroy*, *Raoul d'Asti*). Convém fixar a regra no CONVENCOES.
4. **«M. l'abbé J. Allemand»** (nota 46) → «o padre J. Allemand». O guia manda *M.* → «o senhor»; mas *abbé* aqui é o padre secular, e «o senhor abade» faria pensar num abade de mosteiro. Em `01`, nota 55, *M. J.-J. Allemand* ficou «O senhor J.-J. Allemand».
5. **Latim em itálico nas notas** (2, 15, 39, 40, 83), contra o redondo do impresso, para seguir `01` e `02-b`. Se o editor preferir o redondo do impresso, são esses cinco lugares.
6. **Citações da Filoteia** (III.5, III.6, I.11, I.12): traduzidas diretamente. Harmonizar quando a nossa Filoteia tiver esses capítulos.
