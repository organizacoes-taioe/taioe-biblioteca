# Notas do tradutor: A arte de aproveitar as próprias faltas, Primeira parte

Arquivo: `traducao/01-primeira-parte.txt`. Texto-base: `original/01-primeira-parte.txt` (6e édition, 1894, estabelecida do scan; ver `original/LEIAME.md`).

A tradução foi escrita inteira por outro tradutor, cuja sessão caiu antes da conferência. Esta revisão a conferiu contra o original, parágrafo a parágrafo, e corrigiu o que vai listado em «Correções desta revisão».

## O que foi conferido

- **Blocos:** 212 no original e 212 na tradução, na mesma ordem: 110 parágrafos de texto, 3 títulos `## ` e 99 notas `¤ [n]`.
- **Títulos:** os três `## Chapitre N — ...` → `## Capítulo N — ...`, com os títulos traduzidos:
  - «Não se espantar com as próprias faltas»;
  - «Não se perturbar à vista das próprias faltas»;
  - «Não desanimar à vista das próprias faltas».
- **Marcas:** `[I.1]`, `[I.2]`, `[I.3]`, iguais e na mesma ordem, no começo do primeiro parágrafo de cada capítulo. Os números do autor («1. —» a «7. —») estão todos no lugar.
- **Chamadas e notas:** as 99 chamadas `[n]` e as 99 notas `¤ [n]` estão iguais, na mesma ordem, e cada chamada fica no mesmo bloco que no original.
- **Cabeçalho:** só o `# titulo:` foi traduzido («Primeira parte»). As linhas `# fonte:`, `# edicao:` e `# nota:` estão iguais às do original.
- **Tamanho:** nenhum parágrafo com menos da metade do tamanho do original. A razão vai de 0,83 a 1,17.
- **Itálicos:** o mesmo número de trechos em itálico em todos os blocos, salvo as notas 82 e 94, em que o latim, sem itálico no impresso, ficou em itálico, como manda o guia (§ 3).
- **Aspas:** angulares, com “...” dentro. Contagem diferente em dois blocos, explicados nos itens 1 e 7 de «Passagens difíceis».
- **Mesóclise:** o grep do CONVENCOES não achou nada. A varredura em Python com a mesma regex, terminada em `(?![A-Za-zÀ-ÿ])`, também não.
- **Versos:** não há.
- **Script de conferência:** `C:\Users\geren\AppData\Local\Temp\claude\arte-de-aproveitar-as-faltas-01\conf.py` (blocos, parágrafos, marcas, chamadas e notas por bloco, títulos, tamanho, itálicos, aspas, números do autor, mesóclise).

## Correções desta revisão

1. **«Il ne faut pas» lido como «não é preciso».** O erro mais frequente da primeira versão. Em francês, *il ne faut pas* proíbe («não se deve»); «não é preciso» diz que é dispensável, o que troca o sentido. Corrigido em cinco lugares:
   - cap. I, § 3 (nota 14): *Il ne faut pas s'y coucher ni vautrer* → «Não nos devemos deitar nela nem rebolcar» (antes «Não é preciso nos deitar nela...»). O fim do parágrafo do cap. I, § 6, que cita a frase («não “nos deitar nem rebolcar”»), continua a casar com ela.
   - cap. II, § 3 (nota 46): *il ne faut pas s'en affliger d'une affliction fâcheuse* → «não convém afligir-se com elas com uma aflição agastada».
   - cap. II, § 4 (nota 58): *Il ne faut pas se confondre tristement* → «Não convém confundir-se tristemente».
   - cap. III, § 3 (nota 80): *Il ne faut nullement que vous vous découragiez* → «É preciso que não desanimeis de modo algum» (antes «Não é de modo algum preciso que desanimeis»).
   - cap. III, § 4 (nota 86): *Il ne faut pas rompre les cordes* → «Não se devem romper as cordas».

   Ficou «não é preciso» onde o francês é pergunta afirmativa: cap. II, § 1, *Ne faut-il pas s'affliger...?* → «Não é preciso afligir-se...?».
2. **Cap. I, § 4 (nota 24), São João Crisóstomo:** *sont les plus souvent frappés* estava «são os mais vezes atingidos», que não é português. Ficou «são os que mais vezes são atingidos».
3. **Cap. II, § 6 (nota 67), La Rivière:** *criant merci au doux Rédempteur* estava «pedindo mercê», que hoje se lê como «pedindo um favor». Ficou «implorando perdão ao doce Redentor». *Crier merci* é pedir misericórdia, perdão.

O resto da primeira versão foi conferido e mantido.

## Decisões gerais

- **Voz de Tissot.** Fala em *nous*: ficou «nós». O *on* geral das descrições (cap. II, § 1: «On avait commencé avec ferveur... On se relève cependant...»; cap. III, § 4) passou à 1.ª pessoa do plural («Tínhamos começado», «levantamo-nos», «desanimamos»), que inclui o leitor como o *on* francês. Onde o *on* é impessoal de verdade, ficou «se» («Vê-se pelas citações que precedem»).
- **Tratamento.** São Francisco às suas dirigidas, por *vous* → «vós», com o feminino do original («senhora da vossa alma», «convosco mesma», «certa de que», «cercada»). Onde o próprio original troca o gênero (cap. III, § 4, nota 89: *imparfait*, *craintive*, *environné*), a tradução troca também («imperfeito», «medrosa», «cercado»). Tissot à alma desanimada, por «vós» (cap. III, § 2). O santo ao próprio coração e o coração a si mesmo, por *tu* → «tu» (cap. II, § 5: «Por que é, então, que tropeças agora?»; «Não és miserável e abominável...»; cap. III, § 5: «meu coração, meu amigo, ... toma coragem»). O demônio à Madre de Chaugy, por *tu* (cap. III, § 7: «Não pronuncies esse nome»).
- **Sabor de São Francisco.** Os *car* → «pois»; os *ains* → «mas»; *icelui*, *icelle*, *iceux* → «dele», «nela», «deles»; *ès* → «nos», «nas»; *Or sus* → «Eia»; *Voire* → «Pois sim»; *tout bellement* → «devagarinho»; *prou* → «muito»; *si est-ce que* → «contudo». Ficaram as comparações e o encadeamento das frases longas.
- **Maiúsculas.** Como no original: «o nosso Santo», «o bom Santo», «o Bem-aventurado», «o santo Doutor», «os Santos», «Religiosas» (cap. I, § 4), «Daquele», «Naquele» (*Celui*), «meu Diretor». «Saint» com nome, em minúscula («são Paulo», «santa Teresa»), como manda o guia (§ 4).
- **Abreviaturas por extenso** (guia, § 6): *Mgr* → «dom» («Dom Gay», «Dom Mermillod», «dom Carlos Augusto de Sales»); *P.* → «padre» («o padre Grou», «Padre La Rivière» no começo das notas); *M.* → «o senhor» («O senhor de Bernières», «O senhor J.-J. Allemand»); *S. Aug.* → «Santo Agostinho»; *S. Joan. Chrysost.* → «São João Crisóstomo». *Vén.* ficou «Ven.» (nota 70), abreviado como no original.
- **Referências bibliográficas** (guia, § 1): *Lettre 793e ; collect. Blaise* → «Carta 793.ª; coleção Blaise»; *édit. Meyer* → «edição Meyer»; *Entretien XVIe. Des Aversions* → «Colóquio XVI. Das aversões» (abreviado *Entr.* → «Colóq.»); *Sermon pour le premier Dimanche de Carême* → «Sermão para o primeiro domingo da Quaresma»; *XVIIe partie, sect. 12e* → «XVII parte, seç. 12.ª»; *1re partie* → «1.ª parte»; *IIIe partie* → «III parte» (os números como o impresso os dá, romanos ou arábicos). «Colóquio» é a forma usada também em `02-segunda-parte-b.txt`.
- **Títulos de obras.** Em francês, em itálico: *Esprit du Saint*, *le Chrétien intérieur*, *Manuel des âmes intérieures*, *Opuscules spirituels*, *Vie du Bienheureux François de Sales*, *Vie écrite par elle-même*, *Progrès de l'âme*, *De la vie et des vertus chrétiennes*, *Année sainte de la Visitation*, *Discours à la réunion des Comités catholiques à Paris*, *Déposition touchant plusieurs miracles...*, *Pouvoir de saint François de Sales*. Em latim, como estão: *Ad Theod. Laps.*, *De Pœnit.*, *De Sermone Domini in monte*. As obras de São Francisco com forma consagrada, em português: *Introd. à vida devota*, *Vida devota*, *Tratado do amor de Deus*; no texto, «o autor da _Filoteia_» (*l'auteur de Philothée*) e «na _Introdução à vida devota_».
- **Escritura.** Traduzida do francês de Tissot e de São Francisco, não de uma Bíblia portuguesa. Livros com a abreviação portuguesa, sem ponto: Jz, Sl, 2 Cor / II Cor (como o impresso varia), Eclo, Ecl, 3 Rs, Gl, Is, Rm, Ef, Gn, Lc, Hb, Ez. Os capítulos e versículos ficaram como no impresso (numeração da Vulgata nos salmos). O latim que está em latim ficou em latim, em itálico: *non in commotione Dominus*, *operatur in filios diffidentiæ*, *quamdiu ponam consilia...*, *In justitia quam operatus est vivet*, *Omnis vallis implebitur*, a nota 94 inteira.
- **Citações da Filoteia** (guia, § 2). As passagens da *Introduction* citadas aqui (I, 5; III, 9; IV, 2; IV, 12) ainda não estão traduzidas na nossa Filoteia, de que só existe `00-oracao-e-prefacio.txt`. Ficaram traduzidas diretamente do texto de Tissot. Quando a Filoteia sair, convém harmonizar (ver as dúvidas).

## Termos

| francês | tradução | onde / observação |
|---|---|---|
| faute; chute; tomber | falta; queda; cair | passim (guia, § 5) |
| s'étonner; étonnement | espantar-se; espanto | título do cap. I e passim |
| se troubler; trouble | perturbar-se; perturbação | título do cap. II e passim |
| se décourager; découragement | desanimar; desânimo | título do cap. III e passim |
| inquiétude; s'inquiéter | inquietação; inquietar-se | passim |
| infirmité | fraqueza; enfermidade | «fraqueza» no sentido moral (guia, § 5); «enfermidade» em cap. I, § 6 (*que l'infirmité soit infirme* → «que a enfermidade seja enferma») e cap. II, § 5 (*par infirmité*, oposto a *infidélité*), para guardar o jogo |
| misère | miséria | *la misère chétive* → «a miséria mísera» |
| manquements | falhas | |
| imperfection | imperfeição | |
| abjection | abjeção | cap. I, § 6 |
| amour-propre | amor-próprio | |
| empressement(s) | pressa(s) | cap. II, §§ 1, 2, 4 |
| dépit, se dépiter, dépiteux | despeito, despeitar-se, despeitado | |
| chagrin (adj. e subst.) | amargurado; amargura | *douleur chagrine* → «dor amargurada»; *sans chagrin ni dépit* → «sem amargura nem despeito» |
| fâcher, fâcheux | agastar; agastado, importuno | |
| marri; marrissement | pesaroso; _amofinamento_ | cap. II, § 4: o itálico de Tissot ficou na palavra portuguesa |
| repentance; repentir | arrependimento | |
| regret | pesar | cap. II, § 5 |
| saillies (de l'amour-propre) | assomos | cap. II, § 3; cap. III, § 4 |
| rassis | assentado | *repentance rassise*, *propos bien rassis* |
| se relever | levantar-se, reerguer-se | |
| Philothée; Théotime | Filoteia; Teótimo | |
| Monsieur l'abbé | Senhor padre | cap. III, § 1 |
| Jésuite; Général de sa Compagnie | jesuíta; Geral da sua Companhia | cap. III, § 1 |
| mouchons des abeilles; nymphes | larvas das abelhas; ninfas | cap. III, § 4 |
| tirer des armes | esgrimir | cap. III, § 3 |
| luth; détraquement | alaúde; desarranjo | cap. III, § 4 |

Nomes: Sansão, os filisteus, Teresa, Catarina de Sena, Catarina de Gênova, Pelágia, Jacó, Teótimo, Anteu, Hércules, Caim, Davi, Satanás, Frederico Ozanam, o padre Grou, o padre Roothaan, o padre Faber, Cláudio de la Colombière, J. de Maistre, dom Camus, dom Gay, dom Mermillod, dom Carlos Augusto de Sales, a Madre de Chaugy, a Madre C.-A. Joly de la Roche, a Irmã M.-A. Fichet, a Irmã E.-G. de la Tour, a senhora de Cornillon, a presidente Brulart, a presidente de Herco, a abadessa do Puits-d'Orbe, o senhor J.-J. Allemand, o Chablais, Genebra, Annecy, Roma, Paris.

## Passagens difíceis

1. **Cap. I, § 2 (nota 6), a oração do Pai-nosso.** O impresso abre «« _Pardonnez-nous..._» dentro da citação e não fecha essas aspas internas. A tradução as fecha depois da oração: “_Perdoai-nos as nossas ofensas, assim como nós perdoamos aos que nos ofenderam_.” É a única leitura possível: a frase seguinte («E não há exceção nesta ordem») já é de São Francisco.
2. **Cap. I, § 2 (nota 7), *il n'en bouge*.** «Ele não sai de lá». *Si n'est-il pas déraciné* → «nem por isso foi desarraigado».
3. **Cap. I, § 3 (nota 16), *viennent à cheval et en poste, mais elles s'en revont à pied et au petit pas*.** «Vêm a cavalo e pela posta, mas vão-se embora a pé e a passo miúdo». *En poste* é a muda de cavalos do correio, a toda a pressa; «pela posta» guarda a imagem de época, como o guia admite («um ou outro torneio de época»).
4. **Cap. I, § 3 (nota 12), *En avez-vous déjà beaucoup gâté, de ces ennemis-là?*** *Gâter* é aqui «arruinar, desbaratar» o inimigo: «Já desbaratastes muitos desses inimigos?».
5. **Cap. I, § 5 (nota 25), o tonel.** *de laquelle chacun ne sait pas la raison* → «da qual nem todos sabem a razão» (*chacun ne* = «nem todos»). *Décevoir* → «enganar» (sentido antigo).
6. **Cap. II, § 2 (nota 34), *Vous couriez bien : qui vous a arrêtées?*** Gálatas V, 7, sem aspas no original e sem aspas na tradução: «Corríeis bem: quem vos deteve?».
7. **Cap. II, § 6 (nota 67), as aspas do biógrafo.** O impresso abre a citação de La Rivière com «, abre outra vez « na fala do santo e fecha uma só vez no fim do parágrafo; o parágrafo seguinte reabre com « e fecha. A tradução fecha a fala do santo com ” e deixa a citação do biógrafo aberta, retomada pelo « do parágrafo seguinte, como no uso francês da continuação. Por isso a contagem de aspas difere nesse bloco.
8. **Cap. II, § 6, *oui bien en devons-nous avoir du déplaisir*.** «Mas devemos, sim, ter desprazer deles». O jogo final *nous déplaire de ce que nous avons déplu au divin plaisir* passou inteiro: «a desprazer-nos de termos desprazido ao divino prazer do nosso Criador».
9. **Cap. II, § 6, *à bon escient*.** «Deveras», isto é, a sério, de verdade.
10. **Cap. III, § 6 (nota 97), *quant et soi (_avec soi_)*.** São Francisco usa uma locução já antiga, e Tissot (ou o editor) a glosa entre parênteses. Para que o parêntese continue a explicar alguma coisa, a locução ficou também antiga em português, «a par de si», com a glosa «(_consigo_)».
11. **Cap. III, § 3 (nota 82), *Non est grave certantem cadere, sed in lapsu manere*.** Latim, fica em latim, agora em itálico. Sem «[Trad.: ...]», porque o guia da obra não o pede. Sentido: «Não é grave cair quem combate, mas permanecer na queda».
12. **Cap. III, § 5 (nota 94).** A nota é o versículo latino de que o texto dá a tradução francesa. Ficou em latim, em itálico.
13. **Cap. III, § 7, *le Pouvoir de saint François de Sales, page 284*** (nota 98). Remissão a outra obra de Tissot: fica, como manda o guia (§ 1).

## Remissões de página

Uma só, a outro livro: nota 98, «Ver o _Pouvoir de saint François de Sales_, página 284». Mantida, como manda o guia. Não há remissões a páginas deste livro.

Remissão interna, sem página: cap. I, § 6, «na IIe partie de cet ouvrage» → «na segunda parte desta obra»; cap. III, § 6, «dans la deuxième partie de notre livre» → «na segunda parte do nosso livro». Ficam como estão.

## Emendas e referências erradas do impresso

O texto-base já traz as emendas do `ferramentas/cache/faltas/revisado/emendas.txt` (págs. 2 a 46 para este arquivo: *pesque* → *presque*, *Osannam* → *Ozanam*, *certanten* → *certantem*, *ils les conjurait* → *il les conjurait*, *mane*, *pauperem* etc.). A tradução não fez emenda própria. Ficaram como no impresso, conforme o guia (§ 3):

- **Gn VI, 13** (cap. III, § 1): é Gn IV, 13 (registrado no `emendas.txt`).
- **Lc, III, 43** (cap. III, § 6, nota 97): Lucas III não tem versículo 43; o lugar provável é Lc 3,4-6 (registrado no `emendas.txt`). A vírgula depois de «Lc» também é do impresso.
- **Hb VI, 12** (cap. III, § 4, nota 88): *jusques à la division de l'âme et de l'esprit* é Hb IV, 12. Não está no `emendas.txt`.
- **Ecl XVII, 6** (cap. III, § 4, nota 88): o impresso tem *Eccl.*, que na abreviação francesa é o Eclesiastes (que só tem doze capítulos). A frase (*Cum consummaverit homo, tunc incipiet*) é do Eclesiástico, XVIII, 6 na Vulgata. Mantive «Ecl», do impresso. Não está no `emendas.txt`.
- **Roothan / Roothaan** (cap. III, § 1): o impresso tem *Roothan*; a tradução segue a forma do guia (§ 4), «Roothaan», que é a grafia correta do nome do padre Jan Roothaan.
- **Puits-d'Orbe / Puits-d'Ordre**: as notas 47 e 61 têm *Puits-d'Orbe*; a nota 79 tem *l'Abbesse de Puits-d'Ordre*, que parece erro do impresso (o mosteiro é o Puits-d'Orbe). Mantido como está («abadessa de Puits-d'Ordre»). Não está no `emendas.txt`.

## Dúvidas para quem coordena

1. **«Ecl XVII, 6» e «Hb VI, 12».** Mantidos como no impresso, por regra do guia. Convém acrescentá-los ao `emendas.txt` (são do mesmo tipo que Gen. VI, 13 e Luc III, 43). Se se preferir corrigir a abreviação do livro, «Eclo XVII, 6» evitaria mandar o leitor a um capítulo que não existe no Eclesiastes.
2. **«Puits-d'Ordre» (nota 79).** Mantido. Pode ser uniformizado como «Puits-d'Orbe», com registro.
3. **Citações da Filoteia.** Quando sair a nossa tradução da *Introdução à vida devota*, as passagens I, 5 (notas 16, 36, 90), III, 9 (notas 29, 57, 66), IV, 2 (nota 87) e IV, 12 (nota 30) devem ser ajustadas à redação dela.
4. **Nomes próprios com prenome traduzido.** Ficaram «Frederico Ozanam», «Cláudio de la Colombière» e «dom Carlos Augusto de Sales» (prenome na forma portuguesa usual, sobrenome em francês). O guia só dá «Ozanam». Convém fixar no CONVENCOES se os prenomes se traduzem.
5. **O latim sem tradução.** As notas 82 e 94 e as frases latinas do texto ficaram sem «[Trad.: ...]», porque o guia desta obra não o pede. Na nota 94, a tradução está no próprio texto (cap. III, § 5); na 82, não.
