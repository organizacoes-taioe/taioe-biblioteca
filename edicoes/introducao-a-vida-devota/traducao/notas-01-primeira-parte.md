# Notas do tradutor: Primeira parte (cap. I–XXIV)

Arquivo: `traducao/01-primeira-parte.txt`. Texto-base: `original/01-primeira-parte.txt` (Boulenger, 1909, texto de 1619, via Wikisource).
Texto de conferência: Annecy, t. III (1893), no OCR de `ferramentas/cache/filoteia/annecy3.txt`, consultado nos pontos em que o francês de Boulenger parecia errado (lista em «Emendas»).

## O que foi conferido

- **Parágrafos.** 232 blocos no francês e 232 na tradução, mais o cabeçalho, na mesma ordem. (O LEIAME conta 208 parágrafos porque não conta os 24 títulos.)
- **Títulos.** Os 24 títulos `## Chapitre N — ...` viraram `## Capítulo N — ...`, com os números romanos como estão.
- **Marcas.** As 24 marcas, de `[I.1]` a `[I.24]`, iguais e na mesma ordem, cada uma no começo do primeiro parágrafo do capítulo (nas meditações, antes de `_Preparação_`, como no original).
- **Chamadas e notas.** O arquivo não tem `[n]` nem `¤`, como diz o LEIAME.
- **Itálicos.** 90 sublinhados de cada lado: o sumário da Parte e todos os subtítulos das meditações (_Preparação_, _Considerações_, _Afetos e resoluções_, _Conclusão_, _Eleição_, _Fazei o pequeno ramalhete..._, _Pater noster, Ave._).
- **Numeração** «1.», «2.»... dos pontos das meditações: a mesma, parágrafo a parágrafo.
- **Pontuação.** «!» e «?» batem parágrafo a parágrafo, salvo as três emendas de Annecy (I.12, I.13, I.22; ver «Emendas»). Os «;» e «:» são um pouco mais numerosos na tradução (185 × 176; 80 × 73), por desdobramentos de frase em português; nenhum ponto do autor foi retirado.
- **Aspas.** «» do original; foram acrescentadas uma de abertura e três de fechamento que faltavam em Boulenger (ver «Emendas»), e retirada uma solta (I.15).
- **Tamanho.** Todos os parágrafos de mais de 40 caracteres ficaram entre 80% e 119% do original. Nenhum abaixo da metade.
- **Mesóclise.** O `grep` do CONVENCOES e a varredura em Python com `(?![A-Za-zÀ-ÿ])` não acharam nada. Os lugares em que o francês pedia futuro com pronome foram resolvidos com próclise ou outra construção: «Vós as fareis» (I.8), «eu me acusarei deles» (I.12), «se verá claramente» (I.14), «vou, pois, confessar-me» (I.14), «Eu me absterei» (I.16), «vós os vereis» (I.18). Também evitei «lho», «vo-lo», «vo-la»: «que lhe proibia fazê-lo» (I.4), «vos aconselho muito a fazê-la» (I.6), «a vós o dedico e consagro» (I.9), «antes de vos dar esses avisos» (I.21).
- **Versos.** Não há versos neste arquivo.

## Decisões gerais

- **Tratamento.**
  - Filoteia por **vós** do começo ao fim, com as concordâncias no feminino que o francês marca (*aliviada*, *exposta*, *colocada*, *atenta*; «vós mesma»).
  - Deus, Jesus, a Virgem e o anjo da guarda, nos colóquios, por **vós**.
  - **A própria alma e o coração:** por **tu** onde o francês tem *tu* (I.9 «tu estavas abismada»; I.11 «não queiras mais»; I.14 «Treme, ó minha alma»; I.15 «poderias tu bem»; I.16 «Vamos, ó minha querida alma»). Por **vós** onde o francês tem *vous*: I.13, «Ó minha alma, vós saireis um dia deste corpo... sereis assistida».
  - **O mundo e o inferno** (I.13, I.17, I.18): por *tu* («te hei de deixar, ó mundo»; «Ó inferno, eu te detesto»; «Rei do orgulho... renuncio a ti»), salvo em I.18, *Élection* 1, onde o francês trata o mundo por *vous* («jamais vous ne me verrez») e ficou «nunca me vereis».
  - Nas falas de Jesus e da Virgem à alma (I.17), *tu*, como no original («Vem, ó minha querida alma»; «Coragem, minha filha, não queiras»). Em I.18, o Rei crucificado fala por *vous*: «Vinde, ó minha bem-amada».
  - **Quem fala nas resoluções é Filoteia,** e o francês marca o feminino (*rendue*, *tirée*, *déloyale*, *jugée*, *soussignée*): «devedora», «tornei-me toda rebelde», «mesquinha de mim», «quero julgar-me a mim mesma... para não ser julgada», «Eu, abaixo assinada».
- **Imperativos das meditações.** *Mettez-vous* → «Ponde-vos»; *Suppliez-le qu'il* → «Suplicai-lhe que»; *Priez-le qu'il* → «Pedi-lhe que»; *Priez.* (sozinho) e *Priez Dieu* → «Orai»; *Remerciez* → «Agradecei»; *Offrez* → «Oferecei»; *Confondez-vous* → «Confundi-vos»; *Faites le petit bouquet* → «Fazei o pequeno ramalhete». O refrão *Remerciez, offrez, priez* → «Agradecei, oferecei, orai».
- **Latim.** *Pater noster, Ave* e *Pater, Ave Maria* ficaram em latim e em itálico, como no original.
- **Maiúsculas.** As de reverência ficaram (*Majestade*, *Salvador*, *Criador*, *Esposo*, *Rei Jesus*, *Juiz*, *Nome*, *Cruz*, *Santos* em I.11, *Mãe* da Igreja). Onde Boulenger põe minúscula, ficou minúscula (I.14.3 «o soberano juiz»; «o juiz» em I.14 *Afetos* 3). *Saint* com nome, em minúscula: são Paulo, santa Paula. *Partie* → «Parte», com maiúscula, como no Prefácio («na segunda Parte», I.8). *Ancien testament* (minúscula em Boulenger) ficou «Antigo Testamento», com a maiúscula de uso em português.
- **«Vive Jésus».** «Viva Jesus» (I.18, I.20), em caixa normal, como no original (aqui não há versalete).
- **Citações da Escritura.** Traduzidas do francês do autor, sem referência acrescentada: Gn 1 («segundo o seu gênero»), Nm 13 (os exploradores), 1 Sm 19 (Micol), Sl 118 («no caminho dos mandamentos»), Tb 5, Eclo 6 (o amigo fiel), Ct 2 (as flores), Dt 21 (a cativa), Ef 4/Cl 3 (homem velho), Sl 126 (levantar-se), Sl 54 (covardia), Sl 38, 99 e 102 (I.9), Is 33 (I.15), Mt 25 (I.14), 1 Sm 3 (I.19), Lc 10 (I.19), Ecl 10 (as moscas, I.22), Nm 6 (os nazireus, I.23). Onde o autor parafraseia, ficou a paráfrase.

## Termos

| francês | tradução | onde / observação |
|---|---|---|
| *avis* | avisos | sumário, I.4, I.6, I.14, I.21, I.24 (proposta da nota 00) |
| *exercices* | exercícios | sumário, I.24 |
| *conducteur*; *guide*; *conduite* | guia; guia; conduta | título de I.4 («Da necessidade de um guia»); «condutor» soaria a motorista |
| *purgation*; *purger* | purificação; purificar | conforme o guia. Exceção: «sermos purgados dos nossos humores pecantes» (I.5), onde a imagem é médica (*humeurs peccantes*, médico, aforismo); ver «Passagens difíceis» |
| *humeurs peccantes* | humores pecantes | I.5, I.6 (termo da medicina antiga) |
| *affection(s) du/au péché* | afeição(ões) ao pecado | títulos de I.7, I.22, I.23 |
| *délectations* | deleites | I.7 |
| *loisir* | vagar | I.5 («com trabalho e vagar»), I.11, I.13 |
| *entreprise* | empresa | I.5, I.6 (como no Prefácio) |
| *protestation*; *protester* | protestação; protestar | I.19, I.20, I.21 (proposta da nota 00). O verbo, em I.2 e I.8 (*protestaient*, *protestait*), ficou «afirmavam», «declarava»; em I.20, «protestando», «protesto desde agora», que no contexto jurídico do ato se lê bem |
| *avouer* (ato jurídico) | ratificar | I.17 «ratifico a aquisição», I.20 «ratifico de novo e renovo», «que ratifico e confirmo»: *avouer* é aqui aprovar como próprio, termo de direito |
| *atteinte et convaincue* | arguida e convicta | I.20 (fórmula de processo) |
| *merci* | mercê | I.20 «graça, perdão e mercê» (misericórdia) |
| *conversation* | trato; convívio | I.2 «um santo e amável trato» (como «trato do mundo» no Prefácio); I.8 «o convívio dos seus aliados» |
| *débonnaireté*, *débonnaire* | benignidade, benigno | I.10, I.11, I.17, I.20 |
| *vacation* | vocação | I.3 |
| *la fille* | a donzela | I.3 (moça solteira, ao lado da viúva e da casada) |
| *boutique* | oficina | I.3 (de artesãos; são José, são Crispim) |
| *ménage* | lar | I.3 (como «nos lares» do Prefácio); I.22 *faire leur ménage* (das abelhas) → «fazer a sua lida» |
| *serpe* | podadeira | I.5 |
| *émonder* | podar | I.5, I.7 |
| *contrecœur* | repugnância; a contragosto | I.7, I.8 |
| *ressentiment* | saudade; vivo sentimento | I.7 «falam do pecado com saudade e gosto» (o gosto lembrado); I.19 «com o mais vivo sentimento» |
| *muguetée* | galanteada | I.7 |
| *contenance* | semblante; compostura; atitude | I.18 |
| *endiablés* | endemoninhados | I.18 («endiabrados» seria «travessos» no Brasil) |
| *troupe* | multidão; hoste; bando | I.16 «hoste de apóstolos»; I.18 «multidão de mundanos/devotos/virgens», «o seu triste bando», «ó bando abominável»; I.21 «multidão dos bem-aventurados» |
| *forceneries* | desvarios | I.18 |
| *venaison* | gordura | I.23 «tendo criado gordura demais» (é a gordura de estação do veado) |
| *verjus* | agraço | I.23 |
| *jolivetés* | enfeites | I.22 |
| *rébarbatifs*; *revêche* | ríspidos; rebelde | I.24 |
| *naturel* (subst.) | índole; natureza | I.24 |
| *gratifications ingrates* | obséquios ingratos | I.10 (favores feitos ao mundo, sem paga) |
| *considérable* (da morte) | digna de consideração | I.13 (no sentido de «que se deve considerar», ligado à meditação) |
| *impiteuse* | impiedosa | I.13 |
| *bouquet de myrrhe* | ramalhete de mirra | I.13 |
| *Nazariens* | nazireus | I.23 (os do voto de Nm 6) |

**Nomes:**

- Arélio (pintor citado por Plínio).
- Saul, Davi, Micol; Josué, Caleb; Jacó; Tobias, Ragés; Ló, Sodoma; Absalão; Madalena; Simão, o leproso; Isaías; Jó.
- Abraão, Isaac, Jacó, Jó, Tobias, Sara, Rebeca, Judite; são José, Lídia, são Crispim; santa Ana, santa Marta, santa Mônica, Áquila, Priscila; Cornélio, são Sebastião, são Maurício; Constantino, Helena, são Luís, o bem-aventurado Amadeu (Amadeu IX de Saboia), santo Eduardo; são Gregório.
- O devoto Ávila (são João de Ávila); a bem-aventurada madre Teresa; a senhora Catarina de Cardona (ver «Emendas»); santa Catarina de Sena e os seus *Diálogos*; santa Isabel (da Hungria) e o mestre Conrado (de Marburgo); são Luís e o filho.
- Santa Catarina de Gênova, santa Pelágia.
- Os autores de livros de confissão (I.6): Granada, Bruno, Arias, Auger (Luís de Granada, Vincenzo Bruno, Francisco Arias, Edmond Auger), deixados como o autor os nomeia, pelo sobrenome.
- Santa Paula, são Jerônimo.
- Aristóteles (I.3).

## Passagens difíceis

- **I.1, *vous amuser à suivre quelque dévotion impertinente*.** *S'amuser* é, no século XVII, deter-se, perder o tempo; *impertinente*, «que não vem a propósito». Ficou «perder o tempo em seguir alguma devoção descabida e supersticiosa». «Impertinente», em português, se leria como «insolente».
- **I.1, P2, *ne se feindra point de la plonger*.** *Se feindre de* = hesitar. «Não terá escrúpulo de mergulhá-la no sangue do próximo».
- **I.1, P2, *mais de tenir raison à ses créanciers, jamais qu'à vive força de justice*.** «mas, quanto a pagar aos seus credores o que lhes deve, nunca, senão à viva força da justiça».
- **I.1, P3, *voler en Dieu*.** «Voar para Deus»: é o movimento em direção a Deus, oposto a «correr na terra e para a terra».
- **I.2, *des gens si prodigieux*.** «Gente tão descomunal»: os gigantes de Nm 13. A comparação «como gafanhotos» está no francês assim, aplicada aos homens devorados, e assim ficou.
- **I.2, P4, *l'odeur de suavité*.** «O odor de suavidade», a fórmula bíblica, e não «perfume», para guardar o eco do sacrifício (que volta em I.20).
- **I.3, P3, *dit saint Grégoire*.** Ló «se souilla en la solitude»: «manchou-se na solidão».
- **I.4, *prud'homme*.** Na citação de são Luís (Joinville), «que seja homem prudente e reto»: *prud'homme* reúne o juízo e a probidade.
- **I.4, a obediência de Teresa.** *elle en voua une toute particulière* → «fez voto de uma obediência toda particular», com o substantivo repetido para a frase se ler sem esforço.
- **I.5, *purge* / *purgation*.** O capítulo inteiro joga com a medicina (*humeurs peccantes*, *médecin*, *aphorisme*, *guérison*). Mantive «purificação» para *purgation*, como manda o guia, e «purgados dos nossos humores pecantes» só na frase propriamente médica. A perda é pequena: em português «purificar» não evoca o purgante.
- **I.5, *viennent à cheval et en poste*.** «Vêm a cavalo e a galope»: *en poste* é com cavalos de muda, isto é, à pressa.
- **I.5, P3, *se tenant pour parfaites avant presque d'être faites*.** O jogo *parfaites* / *faites* passa: «tendo-se por perfeitas quase antes de estarem feitas».
- **I.5, P3, a citação do Profeta.** Ficou com a pontuação do original: «antes que a luz tenha chegado, diz o Profeta, levantai-vos depois de terdes estado sentados» (Sl 126,2 na Vulgata).
- **I.7, *marchandent s'il se pourrait faire*.** «Regateiam se não se poderia fazer»: o doente negocia com o médico.
- **I.7, *les pâles couleurs*.** É a clorose das moças. Ficou «as pálidas cores», que é também o nome antigo da doença em português, sem glosa.
- **I.8, *Une haine ... nous fait avoir à contrecœur celui que nous haïssons*.** A frase longa foi um pouco recomposta para a regência: «não somente fugimos daquele a quem o temos e o abominamos, mas também temos repugnância ao convívio dos seus aliados... e não o podemos suportar».
- **I.10, *Je vous renonce*.** «Renuncio a vós»: em português culto *renunciar* pede «a». O *je vous abjure* ficou «eu vos abjuro» (transitivo direto).
- **I.11, *connaître et reconnaître*.** «Conhecê-lo e reconhecê-lo»: o jogo (conhecer e ser grato) passa igual.
- **I.12, *Je tels et de tels*.** É erro de transcrição por *de tels et de tels*. «Particularmente de tais e tais que me são mais penosos» (*ennuyeux*, no sentido forte da época).
- **I.13, *il renversera sans dessus dessous*.** «Ele se revirará de pernas para o ar diante dos vossos olhos».
- **I.13, *Ah chétive*.** «Ah, mesquinha de mim»: *chétive* é a miserável, a coitada, no feminino.
- **I.13, *quelle voie tiendra-t-elle ? non autre que celle qu'elle aura commencée*.** «que caminho seguirá? nenhum outro senão aquele que tiver começado neste mundo».
- **I.16, *pour ces plaisirs si déplaisants*.** O jogo *plaisirs* / *déplaisants* ficou «prazeres tão desaprazíveis»; o de *désirables* / *désirs* e *mépriser* / *méprisables*, «bens tão desejáveis por desejos tão vãos e desprezíveis», passa inteiro.
- **I.16, *chacun à qui mieux mieux*.** «Cada um à porfia».
- **I.17, *ni tant de soupirs que je jette pour toi, respirant avec lui ton salut éternel*.** *Respirer* é aqui «aspirar a». «Nem tantos suspiros que dou por ti, aspirando com ele à tua salvação eterna»: a cadeia *soupirs* / *respirant* se perde em parte, mas «suspiros» / «aspirando» guarda o fôlego.
- **I.17, *le chemin du ciel n'est point si malaisé que le monde le fait*.** «Como o mundo o pinta».
- **I.18, *ces dévotes âmes marient le soin de leur maison extérieure*.** O jogo com as «pessoas casadas» passa: «essas almas devotas casam o cuidado da sua casa exterior com o cuidado da interior».
- **I.18, *voyez les yeux du Sauveur qui les console*.** O *qui* se refere ao Salvador (verbo no singular): «vede os olhos do Salvador, que os consola».
- **I.19, *Notre Seigneur dit que non*.** «Nosso Senhor diz que não, e já não fala senão dos perfumes»: presente, como no francês, que segue Lc 7.
- **I.20, a protestação.** Tem a forma de um ato notarial («Je soussignée, constituée et établie...»), e assim ficou: «Eu, abaixo assinada, constituída e estabelecida...»; «legitimamente arguida e convicta do crime de lesa-majestade divina». O «N.» (o ano da idade, a preencher) ficou: «até este ano N. da minha idade».
- **I.20, *lui donnant à ces fins, dédiant et consacrant mon esprit*.** «Dando-lhe para esses fins, dedicando-lhe e consagrando-lhe o meu espírito»: o «lhe» foi repetido para o português não deixar os gerúndios sem complemento.
- **I.21, *le baiser de paix et de société*.** «O beijo de paz e de sociedade»: *société* é a comunhão dos bem-aventurados, a mesma palavra de I.16 («indissolúvel sociedade»).
- **I.21, *vous la gagnez et vous-même aussi*.** «A ganhais, e a vós mesma também».
- **I.22, *de gaîté de cœur*.** «De ânimo leve», isto é, sem necessidade, por leviandade.
- **I.22, *tout à notre escient*.** «De caso pensado».
- **I.22, *les mouches mourantes ... le mettent à dédain*.** «Tiram-lhe o valor e o tornam desprezível».
- **I.22, *nous les en rechassions et bannissions*.** «As expulsemos e as lancemos fora dela»: *banir* não tem as formas do presente do subjuntivo.
- **I.23, *ouïr des honnêtes comédies*.** «Assistir a comédias honestas»: *honnête* no sentido de decente, como prevê o guia.
- **I.23, *qui est le vrai point de la dévotion*.** «Que é o verdadeiro ponto da devoção»: o ponto essencial.
- **I.24, *s'en délivrer et purger*.** «Livrar-se e purificar-se delas».
- **I.24, *et si assurerez de plus en plus votre conscience*.** *Si* = assim. «E assim tornareis cada vez mais segura a vossa consciência».

## Remissões de página

Não há. A única remissão interna é «vede o que se dirá disso na segunda Parte» (I.8), que remete à Parte, não a página.

## Emendas

Erros de transcrição de Boulenger/Wikisource, corrigidos sem efeito no sentido:

1. **I.1, P2, *actions extérieure*** → *extérieures*: «ações exteriores».
2. **I.1, P4, *encore quelles ne soient*** → *encore qu'elles*.
3. **I.5, *d'être purge*** → *purgé*.
4. **I.9, *teétais*** → *tu étais* (Annecy: *tu estois abismee*).
5. **I.12, *Je tels et de tels*** → *de tels et de tels*.
6. **I.16, *innumérable, Oh !*** → ponto depois de «inumerável».
7. **I.17, *Élection* 1, *tes belles et sacrées, maisons, et en les saints*** → *tes belles et sacrées maisons, et en tes saints* (Annecy).
8. **I.18, P2, *qui les console, y et que*** → *qui les console, et que* (Annecy). O «y» é sobra.
9. **I.20, *]’ai*, *[leurs*, *|et*, *[irrévocablement*** → sobras de OCR retiradas.
10. **I.20, P3, *Dieu de mon cœur. Dieu de mon âme*** → vírgula (Annecy).
11. **I.21, P3, *affecions*** → *affections*.
12. **I.22, P2, *n'avoiraucune*** → *n'avoir aucune*.
13. **I.24, *défauts Et manquements*, *couRut*** → caixa corrigida.

Emendas pela edição de Annecy, com efeito no texto:

14. **I.4, *Dialogues, La dévote princesse*** → *Dialogues. La dévote princesse* (Annecy): ponto final, frase nova.
15. **I.4, aspas.** Boulenger fecha com «» a fala de Ávila sem a abrir; Annecy marca a citação a partir de *vous ne trouverez*. Ficou: «Por mais que procureis, diz o devoto Ávila, «nunca encontrareis...». Também a citação de são Luís, no fim do mesmo parágrafo, não fechava; Annecy a encerra em *nécessaires*, onde pus o «»».
16. **I.4, *madame Catherine de Cordoue*** → **Catarina de Cardona.** Annecy imprime *Catherine de Cardone* e explica em nota que *Cordoue* é o que trazem os textos anteriores, «une erreur facile à constater», porque o episódio está nas *Adições* à Vida de santa Teresa e se trata de Catalina de Cardona. Decisão a confirmar (ver «Dúvidas»).
17. **I.12, P3, *vous ! avez toujours fui*** → *vous avez* (Annecy). O «!» solto foi retirado.
18. **I.13, P1, *père spirituel !*** → «?» (Annecy): é a última de uma série de perguntas.
19. **I.14, P1, *ains qu'aucune des choses*** → *sans qu'aucune* (Annecy): «sem que nenhuma das coisas que vemos sobre ela fique isenta». Com *ains* a frase não tem sentido.
20. **I.14, P3, *étant devant soi sa croix*** → *ayant devant soy sa Croix* (Annecy): «tendo diante de si a sua cruz».
21. **I.14, P4, *séparera les bons de mauvais*** → *des mauvais* (Annecy).
22. **I.14, P7, *« Venez ! dit le Juge*** → as aspas não fechavam. Ficou «Vinde!», diz o Juiz.
23. **I.15, *Afetos* 1, *« O jmon âme, pourrais-tu bien « vivre éternellement...* ** → «Ó minha alma, poderias tu bem viver eternamente...?», com uma só abertura de aspas.
24. **I.15, *Afetos* 1, *les paroles de Job*** → **Isaías.** Annecy, no texto de 1619, imprime *par les paroles d'Isaïe*, com a referência na margem (Is 33,14: *quis poterit habitare ... cum ardoribus sempiternis?*); *Job* é a lição do manuscrito, que Annecy reproduz no apêndice. A citação é de fato de Isaías. Decisão a confirmar (ver «Dúvidas»).
25. **I.17, P4, fim.** A fala das «santas almas» não fechava aspas; fechei-as no fim do parágrafo, onde acaba a citação em Annecy.
26. **I.22, P1, *ces lares et déchets*** → *ces tares et déchets* (Annecy): «essas nódoas e falhas».
27. **I.22, P5, último período.** *quelle apparence y a-t-il ... lui être ennuyeux.* Boulenger fecha com ponto uma pergunta; Annecy tem «?». Ficou «?».

Diferenças de Annecy sem efeito na tradução, não seguidas: I.14.6 *ces paroles si pesantes* (Annecy) × *ces paroles pesantes* (Boulenger), ficou «estas palavras pesadas»; I.13.2 «!» × «?» depois de *offensé mon Dieu*, ficou o «?» de Boulenger.

## Dúvidas para quem coordena

1. **Catarina de Cardona × de Córdova (I.4).** Adotei «Cardona», a forma correta, com Annecy, como o tradutor do Prefácio adotou «Campaspe». Se a regra for seguir o texto de 1619 até nos nomes errados, fica «Catarina de Córdova» (uma ocorrência). Convém decidir junto com Campaspe.
2. **Isaías × Jó (I.15).** Segui Annecy, que dá «Isaías» no texto de 1619. Se Boulenger tiver razão em ler *Job* na edição de 1619 (não consegui conferir o fac-símile), a tradução deve voltar a «Jó». Uma ocorrência.
3. ***Conducteur* (título de I.4).** Usei «guia» e não «condutor», que no Brasil soa a motorista ou a fio elétrico. O guia da obra dá os dois («guia, condutor»). **Proposta para o CONVENCOES:** *conducteur* → guia.
4. ***Purgation* × «purgar».** O guia manda «purificação», e assim fiz em todo o arquivo, mas no capítulo V a imagem é médica. Usei «purgados» uma só vez, com *humeurs peccantes*. Se a casa preferir «purificados» também aí, é uma troca.
5. ***Protestation*.** Usei «protestação», conforme a proposta da nota 00 (I.19, I.20, I.21). Reforço a proposta de fixar o termo no CONVENCOES, porque volta nas outras partes (V.1–V.8, renovação da protestação).
6. ***Avouer* = «ratificar»** (I.17, I.20). Proposta para o guia, se o termo voltar na Quinta Parte (renovação dos votos).
7. **Imperativos da meditação.** Fixei «Ponde-vos na presença de Deus», «Suplicai-lhe que vos inspire», «Agradecei, oferecei, orai». Convém que os tradutores da Segunda Parte (método da meditação) e da Quinta (meditações de renovação) usem as mesmas fórmulas.
