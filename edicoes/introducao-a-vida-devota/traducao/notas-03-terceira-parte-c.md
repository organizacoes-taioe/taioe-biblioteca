# Notas do tradutor: Terceira parte, capítulos XXVIII a XLI

Arquivo: `traducao/03-terceira-parte-c.txt`. Texto-base: `original/03-terceira-parte-c.txt` (Boulenger, 1909, texto de 1619, via Wikisource).
Texto de conferência: Annecy, t. III (1893), no OCR de `ferramentas/cache/filoteia/annecy3.txt`, consultado em todos os lugares em que o francês de Boulenger parecia errado, truncado ou mal pontuado (lista em «Emendas»).

## O que foi conferido

- **Parágrafos.** 115 blocos no francês e 115 na tradução, na mesma ordem (101 parágrafos de texto e 14 títulos, como no LEIAME), mais o cabeçalho.
- **Títulos.** Os 14 títulos `## ` traduzidos, de «Capítulo XXVIII — Dos juízos temerários» a «Capítulo XLI — Uma palavra às virgens», com os romanos como estão.
- **Marcas.** As 14 marcas, de `[III.28]` a `[III.41]`, iguais, na mesma ordem e no começo do primeiro parágrafo de cada capítulo.
- **Notas.** O arquivo não tem chamadas `[n]` nem notas `¤`, como diz o LEIAME.
- **Cabeçalho.** Só `# titulo: Terceira parte da Introdução, capítulos XXVIII a XLI`, como manda o CONVENCOES (§ 6).
- **Numeração do autor.** Os pontos «1.» a «5.» das considerações de III.33, «1.» a «7.» de III.39 e «1.» a «3.» de III.40 ficaram no começo dos mesmos parágrafos.
- **Pontuação.** «?» e «!» batem, parágrafo a parágrafo, com uma exceção de propósito: o «lobo!» de III.29 (ver Passagens). As aspas batem, menos em III.39 (último parágrafo numerado), onde corrigi aspas trocadas do francês (ver Emendas).
- **Itálicos.** Os três do original: _ophiusa_, _Confissões_, _Retratações_.
- **Tamanho.** Cada parágrafo traduzido tem entre 85% e 115% do tamanho do original. Nenhum abaixo da metade.
- **Mesóclise.** O `grep` do CONVENCOES e a varredura em Python com `(?![A-Za-zÀ-ÿ])` não acharam nada.
- **Versos.** Não há versos neste arquivo.

## Decisões gerais

- **Tratamento.**
  - Filoteia, por **vós**, do começo ao fim.
  - Os casados (III.38), os maridos, as mulheres e as virgens (III.41), a quem o autor se dirige no plural, também por **vós**.
  - São João e o caçador (III.31) se tratam por **tu**, como no francês («Por que não trazes o teu arco...?», «Não te admires»).
  - A rainha Branca fala a são Luís por **vós** («ver-vos morrer»), como no francês.
  - Deus, nas falas de Sara (III.32) e da viúva (III.40, «recebei-me»), por **vós**.
  - Timóteo, na citação de 1 Tm 5,3, por **tu** («Honra as viúvas»), que é o *Honore* do francês.
- **Maiúsculas.** Ficaram as de reverência: *Salvador*, *Senhor*, *Espírito de Deus*, *Bondade divina*, *divina Majestade*, *Esposo*, *Esposa* (do Cântico), *Cruz*, *Aquele* (III.40, *Celui*). Também *Apóstolo* (são Paulo), *Apóstolos*, *Profeta*, *Sábio*, *Antigos*, como no original. *saint*, *sainte* em minúscula: são Luís, santa Mônica.
- **«Mariage».** «Matrimônio» quando se fala do sacramento e do estado; «casamento» quando é o fato de casar-se ou a data («no começo do seu casamento», «aniversário dos seus casamentos», «pensamentos de casamento»). *Noces* → «bodas» (as festas) ou «núpcias» (*secondes noces*, *noces spirituelles*, *fin principale des noces*).
- **«Production des enfants».** «Geração dos filhos»; *procréation* → «procriação»; *production des corps* (III.38) → «produção dos corpos».
- **«Honnête», «honnêteté».** «Honesto», «honestidade», no sentido de decoro, como manda o guia (título de III.39: «Da honestidade do leito nupcial»). *Déshonnête* → «desonesto». Em III.33, *honnête conversation* → «honesta companhia».
- **«Conversation».** No sentido do século XVII, trato social: «conversações» (III.29 «peste das conversações»), «reuniões» (III.30), «companhia» (III.34), «convívio» (III.38–39 *mutuelle conversation* → «convívio mútuo»; III.40 *conversation des mondains* → «convívio dos mundanos»).
- **«Loisible», «loisiblement».** «Lícito», «licitamente» (títulos de III.31 e III.33).
- **Escritura.** Traduzida do francês do autor, sem referências, que ele não dá. As principais: Lc 6,37; 1 Cor 4,5; 1 Cor 11,31; Am 6,13 (o juízo em absinto); Lc 18,11; Jo 3,18; Mt 1,19; Lc 23,34; Sl 139,4 (as línguas afiadas e o veneno da áspide); Is 6,6–7; Sb 1,5; Pr 10,9; Sl 38,2 e 140,3; Tb 3,17 (Sara); Ct 4,9; Mt 10,42; Pr 31,13.19; Mt 25,21; 1 Cor 10,31; Ct 2,15; Sl 11,3; Pr 20,10; Ef 5,25.32; Hb 13,4; Gn 30 (as varas de Jacó); 1 Pd 3,7; 1 Ts 4,4; Gn 26,8; Ex 1,21; Pr 17,6; Tt 2,5; Gn 25,21; 1 Cor 7,14.29–31.40; Fl 3,19; Gn 38; 1 Tm 5,3–8; Ct 2,12; Rt 1,19–20; Ct 1,3.

## Termos

| francês | tradução | observação |
|---|---|---|
| *jugement téméraire* | juízo temerário | título e passim |
| *médisance*, *médisant*, *médire* | maledicência, maldizente, falar mal | |
| *meurtre* / *homicide spirituel* | assassínio / homicídio espiritual | III.29 «três assassínios ... com um homicídio espiritual» |
| *renommée* | fama | «a boa fama», «a vida civil, que consiste na fama» |
| *gentillesses et gausseries*; *gausserie* | graças e chalaças; chacota | III.29 |
| *agencements* | arranjos | como *agencement* no Prefácio |
| *privautés* | familiaridades | III.29; III.38 *privauté* → «familiaridade» |
| *muguetterie*, *muguetée*; *cajolerie*, *cajolée* | galanteio, galanteada; lisonja, lisonjeada | III.33, III.38, III.40 |
| *rondeur*; *rond* | lhaneza; lhano | III.30 |
| *esprit feint et double* | espírito fingido e dobre | Sb 1,5 |
| *loisir* | vagar | como no Prefácio |
| *empressement*, *s’empresser* | afã, afanar-se | III.31, III.32, III.37 |
| *habilité et industrie* | habilidade e engenho | III.31–32 |
| *prix* (do jogo) | prêmio | os dois sentidos, prêmio e aposta: «o prêmio, isto é, o que se joga» |
| *paume*, *ballon*, *paillemaille*, *courses à la bague*, *échecs*, *tables* | pela, balão, malha, corridas de argolinha, xadrez, gamão | III.31; em III.32 *les tables* → «os tabuleiros» |
| *potirons et champignons* | tortulhos e cogumelos | ver Passagens |
| *condescendance* | condescendência | III.34, como «rebento da caridade» (*surgeon*) |
| *dilection* | dileção | |
| *abjection*, *abject* | abjeção, abjeto | o termo do autor para a baixeza humilde |
| *ravissements* | arroubos | III.35 |
| *vacation* | vocação | III.35, III.38, III.39; o estado e ofício de cada um |
| *imbécillités* | fraquezas | III.38 |
| *jalousie* | ciúme | III.28, III.38; *jalousement*, *jalouse de* → «zelosamente», «ciosa de», «zelosa de» |
| *vantance* | jactância | III.38 |
| *commerce nuptial*, *commerce corporel* | trato nupcial, trato corporal | III.39; ver Dúvidas |
| *devoir* (conjugal) | dever; dever nupcial | III.39, com são Paulo |
| *supportable*; *vitupérable* | tolerável; repreensível | III.39 |
| *viduité*; *chasteté viduale* | viuvez; castidade vidual | III.40 |
| *retrancher*, *retranchement* | podar, poda | III.40, Ct 2,12 *tempus putationis* |
| *débonnaireté* | mansidão | III.40 |
| *force forcée* | força maior | III.40 |
| *tracas*; *brouilleries* | lida; complicações | III.40 |
| *simples souhaits* | simples veleidades | III.37 (os desejos passageiros, opostos aos que «entretêm o coração») |
| *purgée* | purificada | III.37, como *purgation* no guia |

**Nomes:**

- Abimeleque, Isaac, Rebeca, Jacó, Raquel, Eliézer, Josué, Noé, Ló, Simão, o leproso, Madalena, Onã, Noemi, Mara, Moab, Belém, Caná, Adão, Eva, Samuel, Salomão, Timóteo, Davi, Isaías.
- Cassiano (João Cassiano), são João Evangelista.
- São Luís; o conde de Anjou (Carlos, irmão do rei); «o senhor Gautier de Nemours» (*messire*); a rainha Branca (de Castela).
- São Carlos Borromeu; o bem-aventurado Inácio de Loyola (beatificado em 1609, daí «bem-aventurado»); santa Isabel da Hungria; santa Catarina de Sena; santa Marta.
- Santa Mônica, santo Agostinho; santo Tomás de Aquino; santo André de Fiesole (André Corsini); a mãe de são Bernardo (não nomeada).
- São Gregório Nazianzeno; são Gregório (Magno); são Jerônimo; Orígenes; Trajano; Plínio; Aristóteles.
- Fúria e Sálvia (ver Dúvidas); os cínicos.
- Adônis, Vênus.
- Lugares: Etiópia, África, Paflagônia, Egito, lago de Rieti (ver Dúvidas).

## Passagens difíceis

- **III.28, *convertissent ... le jugement en absinthe*.** Am 6,13. «Convertem ... o juízo em absinto».
- **III.28, *si on ne la leur montre*.** «Se não lhes é mostrada», para evitar «lha».
- **III.28, *ophiusa*.** Erva de Plínio (XXIV, 102), em itálico como no original.
- **III.28, *éclère*.** É a *éclaire*, a celidônia (Annecy, *esclere*). Ficou «celidônia».
- **III.28, *jaunisse*, *ictériques*.** «Ictéricos», «icterícia»; a «icterícia espiritual» fecha a imagem.
- **III.28, *sa garce*.** No século XVII, *garce* já tinha o sentido pejorativo de amante ilegítima. Ficou «concubina».
- **III.28, *qu’il eût été un inceste*.** *Inceste* designa a pessoa (como em III.29, *il est inceste*): «que ele era um incestuoso».
- **III.28, *l’argument fût violent*.** «O indício fosse forte»: *argument* é aqui a prova, o indício.
- **III.28, *ric-à-ric*.** «À justa, só tanto quanto»: com exatidão, sem passar da medida.
- **III.28, *brouillard*, *embrouillés*, *nubileux*.** O autor joga com a névoa: «a névoa ou o tempo nublado ... objetos enevoados ... ações nubladas». O jogo passa.
- **III.28, *truchements et interprètes*.** «Porta-vozes e intérpretes» («trugimão» seria arcaísmo forçado).
- **III.29, *Je proteste, disent-ils*.** «Asseguro, dizem eles». «Protesto» se leria como objeção (ver a dúvida sobre *protestation* nas notas do Prefácio).
- **III.29, *favoriser, flatter ou nourrir les autres*.** *Les autres* são os outros vícios (o que se quer evitar é «louvar o vício»). Em português, «os outros» sozinho se leria como «as outras pessoas»; pus «os outros vícios». É a única palavra acrescentada.
- **III.29, *c’est charité de crier au loup*.** «É caridade gritar “lobo!”»: a exclamação, com aspas, é o grito de alarme, que o português precisa marcar. Por isso há um «!» e um par de aspas a mais nesse parágrafo.
- **III.29, *Rappelez à soi le médisant*.** «Fazei o maldizente cair em si».
- **III.29, *cervelle*.** «Cabeça»: a maledicência «fixa-se firmemente na cabeça dos que escutam».
- **III.30, *naïf*.** No século XVII, «natural, sem artifício»: «simples».
- **III.30, *……*.** As reticências duplas do original, que marcam o salto entre os dois salmos (Sl 38,2 e 140,3), ficaram.
- **III.30, *faire trop l’entendu*.** «Fazer-se demasiado de entendido». Reorganizei o início da frase («quando alguém se faz...»), porque o infinitivo solto do francês (*de faire ... il semble*) não se sustenta em português.
- **III.31, *chanter en musique*.** Cantar música composta, a várias vozes: «cantar a vozes».
- **III.31, *arc toujours tendu*.** «Arco sempre retesado»; *courbé* → «curvado»; *s’étendre* → «distender-se».
- **III.32, *les voilà à dépiter*.** «Ei-los despeitados».
- **III.33, *potirons et champignons*.** *Potiron*, no francês do tempo, era um cogumelo grande, não a abóbora. Pus «tortulhos e cogumelos», que é o par português. Nas frases seguintes o autor alterna as duas palavras; segui a alternância.
- **III.33, *accommodée*.** Termo de cozinha: «temperada».
- **III.33, ponto 5, *passage* / *passetemps*.** O autor joga com o passo da dança e o passatempo. Os dois passam: «onde não dareis senão um só passo, da vida para a morte. Esta dança é o verdadeiro passatempo dos mortais, pois nela se passa, num momento, do tempo para a eternidade». *Violon* → «violino».
- **III.34, *surgeon*.** «Rebento».
- **III.35, *artifice*.** A feitura do olho, o trabalho do Criador: «quer pela feitura, quer pela atividade».
- **III.35, *qu’il ne requiert pas de vous vos yeux*.** O sujeito muda de *la Providence* para *il* (Deus): «e ele não vos pede os vossos olhos».
- **III.35, *cette moue*.** «Essa cara feia».
- **III.35, *se communier*.** «Comungar».
- **III.35, *un seul verre d’eau*.** «Um só copo de água», para ecoar a «quebra de um copo» do mesmo parágrafo (o *verre* do francês).
- **III.36, *détraque*.** «Desencaminha».
- **III.36, *mis la dent*.** «Em quem tenhamos uma vez cravado o dente».
- **III.36, *contrerolons*.** «Censuramos».
- **III.36, *calanger*.** «Repreender» (é a glosa de Boulenger no seu léxico: «accuser, blâmer»).
- **III.36, *grâce sensuelle*.** «Graça sensual»: o encanto que agrada aos sentidos, sem sentido erótico.
- **III.36, *nous lui savons mauvais gré*.** «Ficamos sentidos com ele».
- **III.36, *au bout de là, ce ne sont que tricheries*.** «Afinal de contas, não passam de trapaças»: as pequenas injustiças, que não obrigam à restituição, são mesquinharias, pois nada se perde em viver com generosidade.
- **III.36, *Oui da !*** «Pois sim!», a interjeição afirmativa da época.
- **III.37, *désirs des femmes grosses*.** «Desejos de mulheres grávidas»: o português tem a mesma expressão.
- **III.37, *simples souhaits*.** «Simples veleidades». «Votos» se confundiria com o voto religioso.
- **III.38, *pépinière du christianisme*.** «Viveiro do cristianismo».
- **III.38, *pour parier*.** «Para acasalar» (*s’apparier*); o mesmo verbo em III.39, a propósito do elefante.
- **III.38, *sapin*.** «Abeto».
- **III.38, *cachets*, *scelle et cachette*.** «Sinetes»; «sela e lacra».
- **III.38, *grilloter*, *grillotis*.** «Tilintar» (verbo e substantivo).
- **III.38, *l’oreille*.** O mesmo *oreille* dá os brincos e o ouvir. Ficou «orelhas» para as pérolas e «o ouvido» para o que a mulher deve guardar, porque a frase segue com «nenhuma linguagem ou rumor nele possa entrar» e «se envenenam as almas pelo ouvido». Perda pequena da imagem.
- **III.38, *confitures*, *confits*.** Três vezes o mesmo radical: «em conserva», «postos em conserva», «conservados no açúcar da devoção». O eco passa.
- **III.38, *ternir*.** «Empanar-se».
- **III.38, *support mutuel*.** «A paciência de um para com o outro».
- **III.38, *J’aimerais trop mieux*.** «Antes queria eu».
- **III.38, *maisons*, *édification de maison*.** «Casas», «edificação de casa»: o português também chama «casa» à linhagem.
- **III.39, *esprit truand*.** *Truand* é o mendigo vagabundo, o vadio: «espírito vadio, vilão, abjeto e infame».
- **III.39, *vautrant son esprit*.** «Chafurdando o espírito».
- **III.39, *tiennent leur esprit en broche*.** «Têm o espírito no espeto».
- **III.39, *souillards de cuisine*.** «Moços de cozinha».
- **III.39, *humeurs*** (do elefante). «Costumes».
- **III.39, *Ne sont-ce pas de belles et honnêtes humeurs ... relevées.*** Tem forma de pergunta, mas termina com ponto. O ponto ficou, como nas notas do Prefácio (P9).
- **III.39, *prétentions spirituelles*.** «Intentos espirituais»; em III.39 (ponto 2) *capricieuses prétentions de vertu* ficou «caprichosas pretensões de virtude», onde o sentido é pejorativo.
- **III.39, Agostinho.** *De diversis quaestionibus 83*, q. 30. Sem referência no texto, como no original.
- **III.40, *volupté du corps* / *volonté du cœur*.** Jogo de som. Ficou «volúpia do corpo» / «vontade do coração», que guarda a aliteração.
- **III.40, *l’enseigne du logis d’Adonis*.** «A tabuleta da hospedaria de Adônis»; *aigrettes blanches* → «penas de garça brancas».
- **III.40, *ains souvent le noir...*** *Ains* com o valor de «mais ainda, antes»: «Antes, muitas vezes o negro é posto sobre o branco...».
- **III.40, *vivante est morte*.** «Viva está morta», com o quiasmo do autor.
- **III.40, o ferro, o ímã e o diamante.** A crença antiga (Plínio) de que o diamante impede o ímã de atrair o ferro. Traduzido literalmente.
- **III.40, *un rang d’amour*.** «Um grau de amor».
- **III.41, *frelaté et tracassé d’amour*.** «Adulterado e maltratado pelo amor».

## Emendas pela edição de Annecy

Boulenger, no Wikisource, tem os erros abaixo. A tradução segue Annecy.

1. **III.38, omissão.** Boulenger: «c’est pourquoi plusieurs ont cette véritable famille que celle des maris qui, ne faisant pas...», frase sem sentido. Annecy: «c’est pourquoy plusieurs ont cette véritable **opinion, que leur dévotion est plus fructueuse a la** famille que celle des maris qui, ne faisans pas...». É um salto de linha (do *véritable* para o *famille*), que a colação do LEIAME não apanhou. Traduzi Annecy: «muitos têm esta opinião verdadeira, de que a devoção delas é mais frutuosa para a família do que a dos maridos». **Ver Dúvidas.**
2. **III.39, «celui a une femme comme n’en ayant point qui rend tellement les consolations»** → Annecy, «qui **prend** tellement»: «que de tal modo toma com ela as consolações corporais».
3. **III.39, «capricieuses prétentions vertu»** → Annecy, «prétentions **de** vertu».
4. **III.39, aspas.** Boulenger fecha a citação de Agostinho com «» C’est le grand mal...», isto é, com aspas de fechar onde deviam ser de abrir. Annecy: «« C’est le grand mal de l’homme, » dit saint Augustin, « de vouloir...». Abri as aspas antes de «É o grande mal».
5. **III.29, «je ne dirai rien de cela»** → Annecy, «je ne diray rien **que** cela»: «não direi senão isso». A lição de Boulenger diria o contrário do que pede a gradação (fraca aparência → só isso; imprudência → nada além disso).
6. **III.28, «elle en détourne sa face elle dissimule»** → Annecy, «elle en destourne sa face **et le** dissimule»: «desvia dele o rosto e o dissimula».
7. **III.28, «où qu’il eût vu Rébecca»** → Annecy, «**ou** qu’il eust veu»: «ou tivesse visto».
8. **III.28, «jugés », Mais, O Dieu»** → Annecy, «jugés. Mais, o Dieu»: ponto final antes de «Mas, ó Deus».
9. **III.34, «s’enflamment auvent»** → Annecy, «au vent»: «se inflamam ao vento».
10. **III.37, «puisqu’on ce temps-là»** → «puisqu’en ce temps-là»: «pois nesse tempo»; **«quand elle arriveront»** → Annecy, «quand **elles** arriveront».
11. **III.31, «il passait ; le temps»** → Annecy, «il passoit le tems», sem ponto e vírgula.
12. Erros de digitação, sem efeito no sentido: III.28 «d autrui»; III.29 «au ; prochain», «la I médisance», «maindu»; III.30 «simplicité, Les» (ponto final) e «langage « J’ai dit» (pus ponto antes das aspas); III.38 «con- solations», «lamitié», «parla bouche»; III.39 «son emmiellées»; III.40 «quant l’âme» (Annecy «quant a l’ame»), «a toutes ces autres dames».

## Remissões de página

Não há. Há uma remissão interna do autor, sem página, em III.39 (ponto 2): «a palavra que pus a esse respeito no capítulo da santa comunhão» (é II.20, «Da comunhão frequente», no parágrafo «Il faut que je dise ce mot pour les gens mariés»). Ficou como está.

## Dúvidas para quem coordena

1. **A omissão de III.38.** A frase de Boulenger/Wikisource está truncada (ver Emendas, 1). Completei por Annecy. O LEIAME diz que «não há omissões» do lado de Boulenger; esta escapou à colação (talvez pelo limite de 8 palavras, depois da normalização). **Proposta:** corrigir `original/03-terceira-parte-c.txt` (lista `CORRECOES` de `preparar.py`) e registrar no LEIAME; e talvez repassar a colação com limite menor, porque podem existir outras.
2. ***Commerce nuptial*.** Usei «trato nupcial» e «trato corporal». «Comércio» é o termo clássico («comércio carnal»), mas hoje se lê como negócio. Se a casa preferir o termo antigo, são três ocorrências em III.39.
3. ***Potirons*.** «Tortulhos» é a palavra exata, mas pouco usada no Brasil. A alternativa seria «fungos e cogumelos». Proponho manter «tortulhos».
4. ***Empressement*.** Usei «afã» / «afanar-se». É termo-chave da obra (III.10 trata dele); convém fixá-lo no CONVENCOES para que as outras partes usem o mesmo. **Proposta:** *empressement* → afã.
5. ***Vacation*.** Usei «vocação». Convém fixá-lo também (volta em várias partes).
6. ***Conversation*.** Variei conforme o contexto («conversações», «reuniões», «companhia», «convívio»). Se a casa quiser uma palavra só, «convívio» é a que melhor serve.
7. **«Sálvia».** O autor (e Annecy) escreve *Salvia*; a destinatária da carta 79 de são Jerônimo é Salvina. Mantive a forma do autor, «Sálvia». Se a regra for corrigir os nomes, como se fez com Campaspe no Prefácio, troca-se por «Salvina».
8. **«Lago de Rieti».** O francês diz *lac de Riette*. Usei a forma italiana atual da cidade, Rieti, que é a usual em português.
9. **«Os outros vícios»** (III.29): a única palavra acrescentada, para desfazer a ambiguidade de «os outros». Se se preferir a letra, fica «os outros».
