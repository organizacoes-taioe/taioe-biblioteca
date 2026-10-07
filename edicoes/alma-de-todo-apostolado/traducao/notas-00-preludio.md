# Notas do tradutor: A alma de todo apostolado, Prelúdio

Arquivo: `traducao/00-preludio.txt`. Texto-base: `original/00-preludio.txt` (12e édition, 1927, págs. 1–3
do livro). Conferido contra a imagem do scan: `ferramentas/cache/alma/rev/016.png` a `018.png`.

Conferência por script: 25 blocos no original e 25 na tradução (cabeçalho, 3 títulos `##`, 1 estrofe
de 3 versos `| `, 3 notas `¤ [n]` e 17 parágrafos de prosa; os 18 «parágrafos» do LEIAME contam a
estrofe). Chamadas `[1]`, `[2]`, `[3]` e notas `¤ [1]`, `¤ [2]`, `¤ [3]` iguais e nos mesmos lugares.
O Prelúdio não tem marca `[X.n]` (só aparecem, iguais, dentro da linha `# nota:` do cabeçalho).
Nenhum parágrafo traduzido com menos de 0,89 do tamanho do original; as notas 2 e 3 dobraram por causa
do `[Trad.: …]`. Linhas `# ` do topo copiadas; traduzido só o `# titulo:`. Grep de mesóclise do
CONVENCOES e varredura em Python com a mesma regex terminada em `(?![A-Za-zÀ-ÿ])`: nenhum resultado.

## Decisões gerais

- **Tratamento.** Deus, a Trindade, o Verbo, Jesus, o Espírito Santo e Maria por **Vós**, com maiúscula
  em *Vós*, *Vos*, *Vosso(s)*, *Vossa(s)*, como manda o guia para o Prelúdio (o autor escreve *Vous*,
  *Votre*). Os pronomes oblíquos e reflexivos que o português pede e o francês não tem também levam
  maiúscula: *Vous daignez* → «Vós Vos dignais»; *daignez bénir* (a Maria) → «dignai-Vos abençoar»;
  *Vous appeler* → «chamar-Vos».
- **Duas minúsculas do impresso.** O autor escreve, na imagem de 1927, *dont vous êtes la Plénitude*
  (fim do parágrafo «Pour faire descendre…», dito ao Espírito Santo) e *de vos suaves et puissants
  effluves* (parágrafo «O Charité infinie…»), em minúscula, no meio de dezenas de *Vous*/*Votre*
  maiúsculos. Seguindo o guia («siga o original, palavra a palavra») e o LEIAME (maiúsculas de
  reverência mantidas como no impresso), ficou **«de que vós sois a Plenitude»** e **«os vossos suaves
  e poderosos eflúvios»**, em minúscula. É quase certamente descuido do compositor; ver Dúvidas.
- **Terceira pessoa.** Onde o autor fala de Deus na terceira pessoa com maiúscula, mantida: *Il* (o
  Espírito, o Verbo) → «Ele»; *Celui à qui* → «Aquele a quem». Onde ele usa minúscula, minúscula: *son
  immense besoin* → «a sua imensa necessidade»; *sa Providence*, *ses biens* → «sua Providência», «seus
  bens». As maiúsculas de substantivos também seguem o original: *Foi*, *Vie intérieure*, *Vie intime*
  (mas *vie intime* no 1.º parágrafo), *Sein*, *Décret*, *Mains*, *Source*, *Apostolat*, *Chef*,
  *Œuvre*, *Sang divin*, *Acte divin*.
- **Itálico** (o texto-fonte não o marca; conferido nas três páginas do scan):
  - os versos latinos e as citações latinas das notas 2 e 3 (estas, no livro, estão em redondo; o
    guia manda pôr em itálico as citações latinas);
  - a obra citada na nota 2, *serm. 9 de Nativ.*, em itálico no livro;
  - as ênfases do autor, todas visíveis na imagem: *tressaille*, *jaillit* → «_estremece_», «_jorra_»;
    *notre divinisation* → «_nossa divinização_»; *déifiée* → «_deificado_»; *n'avez pas quitté* →
    «_não deixastes_»; « *transfuseurs* » → «_transfusores_»; a frase inteira *leur apostolat ne sera
    efficace … et Jésus-Christ la SOURCE*; *soif ardente*; *vrai bonheur*; *la Vôtre*; *Cœur de Jésus*;
    *comprendre*; *participer en quelque façon de la nature de l'Acte divin*.
- **Versalete.** *TRINITÉ ADORABLE*, *PRINCIPE*, *SOURCE* → «TRINDADE ADORÁVEL», «PRINCÍPIO», «FONTE», em
  maiúsculas.
- **Pontuação.** O espaço francês antes de «:» e «;» foi retirado. No 2.º parágrafo o autor usa vírgula
  e travessão (*le Verbe, — Votre Verbe … Beauté, — et*); ficou só o travessão, como se usa no Brasil:
  «o Verbo — o Vosso Verbo _estremece_, arrebatado pela Vossa Beleza — e…».
- **Versos latinos** (*Ex quo omnia, / per quem omnia, / in quo omnia*): ficam em latim, como manda o
  guia (§ 3), uma linha por verso, sem tradução e sem `[Trad.: …]` (que o guia reserva às notas
  inteiramente em latim). Não houve versos a traduzir, e por isso não se aplicou o Versificador.
  O livro os imprime em escada (recuo crescente); o formato `| ` não guarda o recuo.

## Termos

| francês | português | observação |
|---|---|---|
| *Prélude* | Prelúdio | título e `# titulo:` |
| *Dieu très grand et très bon* | Deus grandíssimo e boníssimo | exemplo do guia, seguido à letra |
| *Verbe* / *verbe* | Verbo / verbo | com maiúscula, a Pessoa; com minúscula (*le verbe qui éclaire*), a palavra pregada; o eco passa igual em português |
| *tressaille ravi de* | estremece, arrebatado por | *tressaillir*: estremecer (de alegria) |
| *embrasement d'amour*; *embrasés* | abrasamento de amor; abrasados | mesma raiz nas duas passagens, como no francês |
| *Esprit-Saint* | Espírito Santo | |
| *répandre au dehors* | derramar para fora | |
| *s'élancent du néant* | saltam do nada | |
| *poussière animée par Votre souffle* | pó animado pelo Vosso sopro | eco de Gn 2,7 |
| *combler* (o abismo) | preencher | |
| *besoin d'aimer* | necessidade de amar | |
| *provoque* | suscita | «provoca» tem em português um matiz de desafio ou de efeito ruim |
| *boue façonnée par Vos Mains* | barro modelado pelas Vossas Mãos | «barro» (e não «lama»), pelo eco do Gênesis |
| *fils d'adoption* | filhos de adoção | |
| *Chef* (do Corpo místico) | Cabeça | com maiúscula, como no original |
| *feux de la Pentecôte* | fogos de Pentecostes | |
| *transfuseurs* | «transfusores» | neologismo do autor, entre aspas no original; «transfusor» existe em português |
| *effluves* | eflúvios | |
| *ici-bas* | neste mundo | |
| *Obtenez à* | Alcançai a | verbo usual das orações a Maria |
| *amener quelque résultat* | produzir algum resultado | |
| *Jésus-Christ* | Jesus Cristo | sem hífen, como no uso brasileiro |
| *S. AUG.* (nota 2) | santo Agostinho | abreviatura do autor por extenso (guia, § 6); *serm. 9 de Nativ.* fica, como abreviatura de obra |
| *Liturgie* (notas 1 e 3) | Liturgia | |

## Passagens difíceis e leitura adotada

- **«Vous dites : et Vos œuvres s'élancent du néant».** *Vous dites* sem complemento é o *dixit et facta
  sunt* do Sl 32,9 (e o *dixitque Deus* do Gênesis): Deus fala, e as coisas existem. Ficou literal,
  «Vós dizeis: e as Vossas obras saltam do nada», guardando os dois-pontos que fazem as próprias obras
  serem a «palavra» dita. «Vós falais» seria mais corrente, mas perderia o eco.
- **«Un abîme existe entre Vous et la poussière …, Votre Esprit d'amour veut le combler ;».** O francês
  junta as duas orações só com vírgula. Em português a vírgula sozinha soava como erro; acrescentei
  «e»: «…pelo Vosso sopro, e o Vosso Espírito de amor quer preenchê-lo». Mantida a ordem «Um abismo
  existe», do autor.
- **«les heureux retraitants du Cénacle».** Os apóstolos reunidos no Cenáculo antes de Pentecostes,
  vistos como quem faz retiro. «Retirantes», que seria o decalque, no Brasil quer dizer o migrante que
  foge da seca; «exercitantes» é termo próprio dos Exercícios de santo Inácio. Ficou «os ditosos que
  fizeram retiro no Cenáculo».
- **«excitez … les ardeurs».** «Excitai» é correto, mas hoje tem conotação que destoa; ficou «despertai».
- **«Ils seront alors non plus de simples prédicateurs …».** «Então já não serão simples pregadores…»
  (o sujeito «eles» subentendido; o anterior é «todos os que participam do Vosso Apostolado»).
- **«dans leurs intelligences», «dans leurs volontés».** Para não deixar «suas» ambíguo numa oração em
  que Deus é tratado por *Vós* e os apóstolos estão na terceira pessoa, ficou «nas inteligências
  deles», «nas vontades deles»; depois, já sem risco, «os seus corações», «o seu apostolado».
- **«imitation et participation de la Vôtre et de celle du Cœur de Jésus».** «Imitação e participação
  _da Vossa_ e daquela do _Coração de Jesus_» («e da do» ficava duro).
- **«faites-leur sentir».** «Fazei-os sentir» (regência culta de *fazer* + infinitivo com objeto).
- **«Obtenez à tous ceux qui les liront de bien comprendre que…».** «Alcançai a todos os que as lerem
  que _compreendam_ bem que…»: o itálico do autor cai no verbo, como no francês.
- **«Celui à qui nous devons de pouvoir Vous appeler notre Mère».** «Aquele a quem devemos poder
  chamar-Vos nossa Mãe».
- **Nota 2.** *Factus est homo ut homo fieret deus*: a referência «serm. 9 de Nativ.» fica como no
  impresso (a sentença circula com várias atribuições a sermões de Natal de Agostinho; não a emendei).
  `[Trad.: Fez-se homem para que o homem se tornasse deus.]`, com *deus* em minúscula, como no latim.
- **Nota 3.** *Deus cujus Spiritu totum corpus sanctificatur et regitur*: é da oração da Sexta-feira
  Santa pela Igreja (*Omnipotens sempiterne Deus, cujus Spiritu totum corpus Ecclesiae…*); o autor cita
  sem *Ecclesiae*, e assim ficou. `[Trad.: Deus, por cujo Espírito todo o corpo é santificado e
  governado.]`

## Remissões de página

Nenhuma neste arquivo.

## Emendas

Nenhuma. O texto-base confere com a imagem nas três páginas.

## Dúvidas para quem coordena

1. **As duas minúsculas** (*dont vous êtes la Plénitude*; *de vos suaves … effluves*). Deixei
   «vós» e «vossos» em minúscula, como no impresso. Se se preferir a regra do guia para o Prelúdio
   (sempre maiúscula), basta trocar as duas palavras: «de que Vós sois a Plenitude», «os Vossos suaves e
   poderosos eflúvios».
2. **Tradução dos versos latinos do início.** O guia os deixa em latim sem tradução. Se se quiser dar
   o sentido ao leitor, a proposta é acrescentá-la à nota 1, como as outras: «Liturgia. [Trad.: De quem
   tudo, / por quem tudo, / em quem tudo.]» (a doxologia vem de Rm 11,36, *ex ipso et per ipsum et in
   ipso omnia*).
3. **Epígrafe de Mermillod** («Jésus doit être la Vie de mes œuvres. Sinon...»), da página de rosto,
   que o LEIAME deixou fora e sugere decidir se entra no começo do Prelúdio. Não a acrescentei, porque
   ela não está no arquivo-fonte. Proposta, se entrar: «Jesus deve ser a Vida das minhas obras. Senão...
   (Card. Mermillod)».
4. **Proposta para o guia (não alterado):** registrar que os oblíquos e reflexivos acrescentados pelo
   português nas falas a Deus e a Maria no Prelúdio também levam maiúscula («Vós Vos dignais»,
   «dignai-Vos», «chamar-Vos»), e que *Vous dites* se traduz «Vós dizeis:».
