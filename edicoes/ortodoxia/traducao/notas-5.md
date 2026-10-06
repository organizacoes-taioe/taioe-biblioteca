# Ortodoxia — notas do tradutor, capítulo V (A bandeira do mundo)

Parágrafos: 26/26. Grep de mesóclise sem resultado.

## Variantes do texto-fonte (LEIAME)

- § 4: segui o scan, `throne of the mystic and the arbitrary` → «o trono do místico e do arbitrário» (o Gutenberg
  traz `throne or the mystic`, erro evidente).
- § 15: `liberal and humane` (PG) / `liberal and human` (scan) → «liberais e humanos». Em português, *humano* também
  quer dizer «compassivo» («tratamento humano»), de modo que a tradução serve às duas leituras e não precisei escolher.

## Os versos de Matthew Arnold (§ 12)

São os quatro versos de «Resignation» (*Enough, we live!...*), que o Gutenberg traz corridos num parágrafo próprio,
sem quebra de verso. Como manda o guia, ficaram nesse mesmo parágrafo, entre aspas, com « / » entre os versos.

- **Original:** tetrâmetro jâmbico, rimas emparelhadas AABB (*life/rife*, *worth/birth*), todas masculinas. Molde do
  original: `8: 2-4-6-8` nos quatro versos (o terceiro, *Though bearable, seem hardly worth*, tem a 4.ª fraca).
- **Tradução:** octossílabo com 4.ª e 8.ª obrigatórias, molde `8: (1)-(2)-4-(6)-8`, AABB. O `molde.mjs` deu 4 ✓, sem
  ✗ nem ≠ e sem leitura forçada:

  | verso | desenho | corpus |
  |---|---|---|
  | Basta: vivemos — e se a vida, | 1-4-8 | 13,35% (#2) |
  | De grandes frutos desprovida, | 2-4-8 | 15,82% (#1) |
  | Mesmo aceitável, paga mal | 1-4-6-8 | 7,11% (#5) |
  | A pompa astral e a dor natal. | 2-4-6-8 | 8,79% (#4) |

- **Escolhas.** *This pomp of worlds, this pain of birth* → «A pompa astral e a dor natal»: guarda a pompa, os astros
  (os «mundos») e a dor do nascimento, e a rima interna *astral/natal* faz o papel da aliteração *pomp/pain*.
  *Seem hardly worth* → «paga mal», isto é, a vida mal compensa o que custou; *though bearable* → «mesmo aceitável».
  *So little rife* → «desprovida».
- **Perdas.** O *seem* (a hesitação de «parecer») e a nuance de *so little rife* («tão pouco farta»), que
  «desprovida» endurece um pouco. O par *vida/provida* é grave; as rimas de Arnold são todas agudas. Só o segundo par
  (*mal/natal*) ficou agudo, porque não achei rima aguda para *vida* que não forçasse o sentido. Rejeitei «Embora
  suportável, mal», que é mais literal, porque não tem a 4.ª (desenho 6-8, 0,39% do corpus).
- O travessão de *Enough we live:--and* ficou («Basta: vivemos — e se a vida»). O parágrafo anterior termina, como no
  original, em travessão («...os gritos de Schopenhauer —»).

## Trocadilhos, paradoxos e soluções

- **right / left** (§ 1): «achasse tudo direito e nada errado... é como dizer que tudo é direito e nada é esquerdo».
  *Direito* também quer dizer «correto», o que deixa passar a piada inteira.
- **looks after your eyes / your feet** (§ 1): «cuida dos seus olhos... cuida dos seus pés».
- **jingo** (§§ 3, 8, 9): «patrioteiro» em todas as ocorrências («literatura belicosa e até patrioteira», «o
  patrioteiro do universo», «autossatisfação patrioteira», «os piores patrioteiros»). Evitei *jingoísta*, que pouca
  gente conhece.
- **penny dreadfuls** (§ 3): «folhetins de tostão».
- **holy day / holiday** (§ 5): «um dia santo para Deus... um feriado para os homens». No Brasil, o dia santo é também
  feriado, então o jogo passa sem perda.
- **candid friend / uncandid candid friend** (§§ 6 e 7): «o amigo franco», «o amigo franco sem franqueza».
- **My cosmos, right or wrong** (§ 8): «Meu cosmo, certo ou errado» (eco de *My country, right or wrong*).
- **wash / whitewash** (§ 8): «Não vai lavar o mundo, mas caiar o mundo»; no § 9, *the whitewashing* → «a
  caiação». *Caiar* é o *whitewash* literal, pintar de branco sem limpar, e é essa a imagem dele.
- **through thick and thin / the thinness of his excuses or the thickness of his head** (§ 10): sem trocadilho
  equivalente. Ficou «defender os seus homens com unhas e dentes... quanto ao esfarrapado das desculpas dele ou ao duro
  da sua cabeça» (*desculpa esfarrapada* e *cabeça-dura* traduzem bem *thin excuse* e *thick head*). **Perda:** o eco
  *thick/thin* com a expressão inicial.
- **Love is not blind... Love is bound** (§ 10): «O amor não é cego... O amor é preso; e, quanto mais preso, menos
  cego.»
- **interested / disinterested** (§ 11): «se interesse pela vida... desinteressado nas suas opiniões».
- **fixed heart / free hand** (§ 11): «o coração fixo, temos as mãos livres».
- **fills / freezes** (§ 13): «enche a nossa época... enregela a nossa época» (a aliteração passou para o *en-*).
- **get on with it / get it on** (§ 14): «ir levando a vida neste mundo... força bastante para ir levando, e sim força
  bastante para levar o mundo adiante».
- **die for the world / die to it** (§ 14): «morrer pelo mundo... morrer para o mundo».
- **Not only is suicide a sin, it is the sin** (§ 15): «não é só um pecado; é o pecado». O Gutenberg não marca
  ênfase e não acrescentei itálico; a frase se sustenta sem ele.
- **he flung away his life / another flung away life** (§ 17): «jogava fora a sua vida» / «jogava fora a vida»; mantive
  a diferença do possessivo.
- **piety or pity** (§ 20): «piedade nem compaixão» (o par vem da mesma raiz nas duas línguas; o som se perde).
- **Its peculiarity was that it was peculiar** (§ 20): «A sua peculiaridade era ser peculiar».
- **unselfish egoist** (§ 20): «um egocêntrico abnegado». *Egoísta altruísta* seria só contradição em português;
  *egoist* aqui é quem se centra em si, e não quem é avarento com os outros (cf. *egotistical* → «egocêntrico», cap. I).
- **Christian Scientist / Christian** (§ 19): «um adepto da Ciência Cristã... um cristão». Perde-se um pouco o choque
  de *Scientist*.
- **Pantheism / Pan; the cloven hoof** (§ 21): «o panteísmo vai muito bem enquanto é o culto de Pã... logo mostrou o pé
  de cabra». Pã tem pés de bode e, no folclore português, o diabo é o Pé-de-Cabra; a expressão serve às duas coisas.
- **Natural Religion / unnatural** (§ 21): «Religião Natural... antinatural».
- **evolutionist / unrolled** (§ 23): «o evolucionista tem, no próprio nome, a ideia de ser desenrolado como um tapete»
  (*evolução* vem do mesmo *evolvere* latino).
- **thrown off / flung it away** (§ 23): «uma coisinha que “jogou no papel”. Mesmo ao dá-lo ao mundo, já o arremessou
  para longe». *Jogar no papel* é escrever de improviso e, ao pé da letra, atirar.
- **breaking off / branching out** (§ 23): «um desprender-se... um ramificar-se».
- **right / rectitude** (§ 25): «Acertada uma peça, todas as outras iam repetindo aquele acerto, como relógio após
  relógio bate o meio-dia» (*acertar* também se diz dos relógios).
- **vast and void** (§ 25): «vasto e vazio», aliteração conservada.
- **good / goods from Crusoe's ship** (§ 25): «o bem... como os bens do navio de Crusoé».
- **the crazy thread of a condition** (§ 25): «o fio bambo de uma condição»; *crazy* aqui é o velho sentido de
  «frágil, rachado». **Perda:** o eco com a loucura.
- **homesick at home** (§ 26): «sentir saudade de casa estando em casa».

## Citações e alusões

- «My son give me thy heart» (Pr 23,26) → «Meu filho, dá-me o teu coração», com o *tu* bíblico.
- «fair as the sun, clear as the moon, terrible as an army with banners» (Ct 6,10, com sol e lua trocados por
  Chesterton) → «formosa como o sol, clara como a lua, terrível como um exército com bandeiras». Traduzi o que ele
  escreveu, sem destrocar. O feminino concorda com «luz»; mantive «com bandeiras» (e não «em ordem de batalha») por
  causa do título do capítulo.
- «sought its meat from God» (Sl 104,21) → «buscava de Deus o seu alimento».
- «the everlasting hills» (Gn 49,26) → «as colinas eternas».
- «the blazing stones of the Celestial City» (Bunyan) → «as pedras flamejantes da Cidade Celestial».
- «small things done or undone» → «pequenas coisas feitas ou deixadas por fazer» (eco do *Book of Common Prayer*).
- «in the fourth chapter» → «no quarto capítulo»; «In the last chapter» (§ 3) → «No capítulo anterior».

## Termos e nomes

| inglês | tradução |
|---|---|
| optimist / pessimist | otimista / pessimista |
| jingo, jingoes | patrioteiro(s) |
| cosmic patriot / anti-patriot | patriota cósmico / antipatriota cósmico |
| candid friend | amigo franco |
| oath of allegiance / of loyalty | juramento de fidelidade / de lealdade |
| the suicide (pessoa) / suicide (ato) | o suicida / o suicídio |
| martyr, martyrdom | mártir, martírio |
| the Inner Light | a Luz Interior |
| the god within | o deus interior |
| the Simple Life | a Vida Simples |
| the Higher Thought Centre | o Centro do Pensamento Superior |
| Christian Scientist | adepto da Ciência Cristã |
| Natural Religion, nature worship | Religião Natural, culto da natureza |
| latitudinarian | latitudinário |
| penny dreadfuls | folhetins de tostão |
| penny-in-the-slot machines | máquinas automáticas de moeda (por um pêni) |
| front-bench official answer | resposta oficial, de bancada do governo |
| whitewash / whitewashing | caiar / caiação |
| Pimlico, Chelsea, Tottenham, Brighton | sem mudança |
| the Boer War | a Guerra dos Bôeres |
| the Norman Conquest | a Conquista Normanda |
| Hindoos | hindus |
| Marcus Aurelius; Julian the Apostate | Marco Aurélio; Juliano, o Apóstata |
| the Wise Man of the Stoics | o Sábio dos estoicos |
| Pendennis, Thackeray, Carlyle, Freeman, Mr. William Archer | sem mudança («o sr. William Archer») |
| St. George | São Jorge |
| the Fall | a Queda |
| Crusoe | Crusoé |
| the New Jerusalem | a Nova Jerusalém |

## Outras decisões

- Maiúsculas de ênfase do Gutenberg → itálico: «because it is THEIRS» → «porque é _deles_»; «There IS a trace» →
  «_Há_ vestígio»; «as THE answer» → «como _a_ resposta»; «a distinct IDEA» → «uma _ideia_ distinta»; «we do NOT fit»
  → «nós _não_ nos encaixamos»; «the WRONG place» → «no lugar _errado_». Não acrescentei outras.
- «He set it free» com maiúscula no original → «Ele o libertou»; «separate from Himself» → «separado de Si». Onde
  Chesterton usa *he* minúsculo para Deus (a peça que «planejara perfeita»), o pronome sumiu na conjugação.
- Pimlico é tratado no feminino por ele quando se enfeita («attire herself»): «Pimlico se enfeitaria... mais bela que
  Florença»; nos outros lugares (*it*), «o próprio Pimlico».
- «eighteenth-century theories» → «as teorias setecentistas».
- «an idea of content and co-operation» → «uma ideia de contentamento e cooperação» (*content* = contentamento,
  aquiescência, e não «conteúdo»).
- «Let me explain» → «Permita-me explicar» (o *você* do leitor, no singular, como no resto do livro).
