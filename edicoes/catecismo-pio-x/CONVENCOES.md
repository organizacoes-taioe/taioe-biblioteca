# Catecismo Maior de São Pio X — convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md` (regras gerais) e `edicoes/magisterio/CONVENCOES.md` (termos do
Magistério). Este guia prevalece onde for mais específico. Modelo do tom e do formato: `traducao/p0-licao-preliminare.txt`
e `traducao/p1-c01.txt` (perguntas 1–21), feitos pelo preparador.

## 1. O texto e os arquivos

- Original: `original/*.txt`, gerado por `montar.py` (não edite à mão; erro do italiano vai para as notas do
  tradutor, com o número da pergunta, e o principal confere no fac-símile e corrige em `CORRECOES`).
  Edição de Roma, Tipografia Vaticana, 1905. Não use o catecismo de 1912 (433 perguntas): é outro livro.
- Um arquivo por capítulo («Capo»): `p<parte>-c<capítulo>.txt`; a lição preliminar é `p0-licao-preliminare.txt`; o
  capítulo da Penitência (IV.6) está em dois arquivos, `p4-c06a.txt` (§§ 1–5) e `p4-c06b.txt` (§§ 6–10).
- A tradução: o mesmo arquivo em `traducao/`, **o mesmo número de blocos, na mesma ordem**, as mesmas marcas.
  Cabeçalho só com `# titulo:` traduzido (ex.: `# titulo: Parte I, Do Símbolo dos Apóstolos…; Capítulo II, Do primeiro artigo do Símbolo`).

## 2. O formato dos blocos (copie a estrutura do original, bloco por bloco)

| no original | na tradução |
|---|---|
| `## 2. Del primo articolo del Simbolo` (título do capítulo) | `## 2. Do primeiro artigo do Símbolo` (mesmo número) |
| `## § 1. Di Dio Padre e della creazione` | `## § 1. De Deus Pai e da criação` |
| `## Della dottrina cristiana…` (subtítulo, só na lição preliminar) | `## Da doutrina cristã e das suas partes principais` |
| `[I.2]` sozinho na linha, logo acima da 1ª pergunta do capítulo | igual, no mesmo lugar (é a marca que divide o site em páginas; não aparece) |
| `**22. Che cosa c’insegna il primo articolo: _Io credo…_?**` | `**22. O que nos ensina o primeiro artigo: _Creio em Deus…_?**` |
| a resposta, bloco seguinte, sem «R.» | a resposta, bloco seguinte |
| resposta em lista: linhas começando com `\| ` | o mesmo número de linhas `\| `, uma por item |

- A pergunta vai toda entre `**…**`, com o **mesmo número** na frente. O que a edição põe em redondo dentro da
  pergunta (citação de uma fórmula: «_Io credo in Dio…_», «_per grazia di Dio_») está em `_itálico_` dentro do
  negrito; faça o mesmo no mesmo trecho.
- Itálico na resposta: onde o original tem `_…_` (em geral a fórmula explicada ou o nome de uma oração).
- Ordinais como no original: «1.º», «2.º», «1.ª».
- Aspas «…» como no original (as falas e orações citadas). Abreviaturas: «S. Pietro» → «São Pedro»;
  «SSm̃a», «SS.» → «Santíssima», «Santíssimo»; «p. e.», «per es.» → «por exemplo».

## 3. Tom e tratamento

- Catecismo para o povo, de perguntas curtas e respostas que repetem a pergunta (é o método: a criança decora a
  resposta completa). **Mantenha a repetição**: a resposta retoma as palavras da pergunta, como no italiano.
  Português do Brasil simples, claro, **sem palavra rara** (nada de «outrossim», «mister», «cumpre»).
- **O catequista trata quem aprende por «você»** («Você é cristão?», «Por que você diz…?», «Recite-os.», «O que
  você fará antes de dormir?»). A resposta vem na 1ª pessoa quando o italiano a põe («Sim, sou cristão…»).
- **Deus, Nosso Senhor, Nossa Senhora e os santos, nas orações e jaculatórias: por «vós»**, como se reza no Brasil
  («Senhor, eu vos ofereço este trabalho: dai-me a vossa bênção»).
- Maiúsculas: como no original para os pronomes de Deus («Egli», «Lui» → «Ele»); «Papa», «Bispos», «Igreja»,
  «Sacramento» (o Santíssimo), «Missa» com maiúscula; os nomes dos sacramentos com maiúscula (Batismo, Crisma…).
- Italiano antigo e de catecismo: «Iddio» = «Deus»; «figliuolo» = «filho» («Figlio/Figliuolo di Dio» = «Filho de
  Deus»); «salute» (eterna) = **«salvação»**, nunca «saúde»; «roba» = «bens», «coisas»; «divozione» = «devoção»;
  «imagine» = «imagem»; «padroni e dipendenti» = «patrões e empregados»; «giovanetti» = «jovens».
- Frase longa da resposta: pode partir em duas, sem perder a repetição da pergunta nem as ligações (perché,
  dunque, cioè → porque, portanto, isto é). Nunca mesóclise.

## 4. Termos fixos

| italiano | tradução |
|---|---|
| dottrina cristiana | doutrina cristã |
| Simbolo degli Apostoli; il _Credo_ | Símbolo dos Apóstolos; o _Credo_ |
| articolo (do Credo) | artigo |
| mistero; misteri principali della fede | mistério; mistérios principais da fé |
| Unità e Trinità di Dio; Incarnazione, Passione e Morte | Unidade e Trindade de Deus; Encarnação, Paixão e Morte |
| Santissima Trinità; Persona (divina) | Santíssima Trindade; Pessoa |
| Spirito Santo | Espírito Santo |
| Gesù Cristo; Signor nostro; il divin Salvatore; il Redentore | Jesus Cristo; nosso Senhor; o divino Salvador; o Redentor |
| la Madonna; la santissima Vergine; Maria SSm̃a | Nossa Senhora; a Santíssima Virgem; Maria Santíssima |
| Angelo custode; demonio | Anjo da guarda; demônio |
| paradiso; inferno; purgatorio; Limbo dei santi Padri | paraíso; inferno; purgatório; limbo dos santos Padres |
| Novissimi | Novíssimos |
| grazia santificante; grazia attuale | graça santificante; graça atual |
| in istato di grazia | em estado de graça |
| peccato originale, attuale, mortale, veniale | pecado original, atual, mortal, venial |
| vizi capitali | vícios capitais (a lista: «pecados capitais» se o italiano diz «peccati capitali») |
| virtù teologali, cardinali, morali | virtudes teologais, cardeais, morais |
| doni dello Spirito Santo | dons do Espírito Santo |
| opere di misericordia corporali, spirituali | obras de misericórdia corporais, espirituais |
| Beatitudini evangeliche | bem-aventuranças evangélicas |
| consigli evangelici | conselhos evangélicos |
| Chiesa cattolica, apostolica, romana | Igreja Católica, Apostólica, Romana |
| Chiesa militante, purgante, trionfante | Igreja militante, padecente, triunfante |
| Chiesa docente, discente | Igreja docente, discente (o catecismo explica as palavras) |
| comunione dei santi | comunhão dos santos |
| il Papa; Sommo Pontefice; Romano Pontefice | o Papa; Sumo Pontífice; Romano Pontífice |
| Vicario di Gesù Cristo; Vescovi; parroco; sacerdote; i Pastori | Vigário de Jesus Cristo; Bispos; pároco; sacerdote; os Pastores |
| infallibile, infallibilità | infalível, infalibilidade |
| eretici, scismatici, apostati, infedeli, ebrei | hereges, cismáticos, apóstatas, infiéis, judeus |
| scomunica, scomunicati | excomunhão, excomungados |
| orazione; orazione mentale, vocale | oração; oração mental, vocal |
| orazione domenicale; il _Pater noster_, il Pater | oração dominical; o _Pai-Nosso_ (com itálico onde o original tem) |
| petizione; domanda (do Pai-Nosso) | pedido |
| salutazione angelica; l’_Ave Maria_ | saudação angélica; a _Ave-Maria_ |
| comandamenti di Dio; della prima/seconda tavola | mandamentos de Deus (ou da lei de Deus); da primeira/segunda tábua |
| precetti della Chiesa | **preceitos da Igreja** («precetto o comandamento» = «preceito ou mandamento») |
| feste comandate; di precetto | festas de guarda; de preceito |
| culto interno, esterno; adorazione | culto interno, externo; adoração |
| bestemmia; giuramento; spergiuro; voto | blasfêmia; juramento; perjúrio; voto |
| digiuno; astinenza; quattro tempora; vigilie | jejum; abstinência; Quatro Têmporas; vigílias |
| decime | dízimos |
| sacramenti; segno sensibile ed efficace | sacramentos; sinal sensível e eficaz |
| materia; forma; ministro | matéria; forma; ministro |
| carattere (sacramental) | caráter |
| Battesimo; padrini | Batismo; padrinhos |
| Cresima o Confermazione | Crisma ou Confirmação |
| Eucaristia; il santissimo Sacramento; Corpo e Sangue | Eucaristia; o Santíssimo Sacramento; Corpo e Sangue (de Cristo, com maiúscula) |
| specie (del pane e del vino); transustanziazione | espécies; transubstanciação |
| Comunione; comunicarsi; Comunione spirituale | Comunhão; comungar; Comunhão espiritual |
| digiuno naturale | jejum natural |
| Messa; santo sacrificio della Messa; ascoltare / assistere alla Messa | Missa; santo sacrifício da Missa; ouvir Missa / assistir à Missa |
| Penitenza (sacramento); penitente; confessore | Penitência; penitente; confessor |
| esame (di coscienza); dolore; contrizione; attrizione | exame (de consciência); dor; contrição; atrição |
| proponimento; accusa; assoluzione; soddisfazione | propósito; acusação; absolvição; satisfação |
| peccati riservati; censure; sigillo sacramentale | pecados reservados; censuras; sigilo sacramental |
| indulgenza plenaria, parziale; giubileo | indulgência plenária, parcial; jubileu |
| Estrema Unzione; Ordine sacro | Extrema-Unção; Ordem (o sacramento da Ordem) |
| Matrimonio; impedimenti; nozze | Matrimônio; impedimentos; casamento («celebrare le nozze» = «celebrar o casamento») |
| Sacra Scrittura; Tradizione; Bibbia; Vecchio e Nuovo Testamento | Sagrada Escritura; Tradição; Bíblia; Antigo e Novo Testamento |
| giaculatoria | jaculatória |
| mortificazione; mortificarsi | mortificação; mortificar-se |
| tentazione; occasioni (prossime) | tentação; ocasiões (próximas) |
| il prossimo | o próximo |

Termo novo que se repete: anote-o nas notas do tradutor com a solução, para entrar aqui.

## 5. As fórmulas (iguais em todo o livro)

Use estas formas sempre que a fórmula, ou um pedaço dela, aparecer (na lista, na pergunta que a cita, na resposta
que a explica). São as rezadas no Brasil, **menos onde o catecismo explica as palavras da sua forma** (anotado
abaixo); aí vale a palavra do catecismo.

**Credo** (Q 18; 12 linhas, como o original; artigo 5: «desceu aos infernos», porque a Q 116 explica a palavra «inferno»)
| 1.º Creio em Deus Pai todo-poderoso, Criador do céu e da terra.
| 2.º E em Jesus Cristo, seu único Filho, nosso Senhor,
| 3.º que foi concebido pelo poder do Espírito Santo; nasceu da Virgem Maria;
| 4.º padeceu sob Pôncio Pilatos, foi crucificado, morto e sepultado;
| 5.º desceu aos infernos; ao terceiro dia ressuscitou dos mortos;
| 6.º subiu aos céus; está sentado à direita de Deus Pai todo-poderoso,
| 7.º donde há de vir a julgar os vivos e os mortos.
| 8.º Creio no Espírito Santo,
| 9.º na santa Igreja Católica, na comunhão dos santos,
| 10.º na remissão dos pecados,
| 11.º na ressurreição da carne,
| 12.º na vida eterna. Amém.

A palavra «Credo» como nome da oração fica «Credo»; mas a Q 19 explica a primeira palavra da oração: «Que quer
dizer a palavra _Creio_…». Nas perguntas sobre cada artigo, o artigo citado vai na mesma forma («_Creio no Espírito Santo_»), adaptando só a
pontuação. Q 115: «_Desceu aos infernos; ao terceiro dia ressuscitou dos mortos_».

**Pai-Nosso** (Q 284; 8 linhas; «dívidas» e «devedores», porque a Q 310 explica por que os pecados se chamam «dívidas»)
| Pai nosso, que estais nos céus:
| 1.ª Santificado seja o vosso nome.
| 2.ª Venha a nós o vosso reino.
| 3.ª Seja feita a vossa vontade, assim na terra como no céu.
| 4.ª O pão nosso de cada dia nos dai hoje.
| 5.ª Perdoai-nos as nossas dívidas, assim como nós perdoamos aos nossos devedores.
| 6.ª E não nos deixeis cair em tentação.
| 7.ª Mas livrai-nos do mal. Amém.

Q 288: «_que estais nos céus_». Q 318: «_livrai-nos do mal_» e não «_dos males_». (O italiano «come in cielo, così in
terra» fica na ordem brasileira, «assim na terra como no céu».)

**Ave-Maria** (forma rezada no Brasil: «Ave, Maria, cheia de graça, o Senhor é convosco. Bendita sois vós entre as
mulheres, e bendito é o fruto do vosso ventre, Jesus. Santa Maria, Mãe de Deus, rogai por nós, pecadores, agora e na
hora de nossa morte. Amém.»). As palavras do anjo (Q 327): «Ave, cheia de graça, o Senhor é convosco; bendita sois
vós entre as mulheres». As de Santa Isabel (Q 330): «Bendita sois vós entre as mulheres, e bendito é o fruto do
vosso ventre».

**Mandamentos de Deus** (Q 343; nas palavras do catecismo, que explica cada um; onde a forma brasileira diz o mesmo,
ela fica)
| Os mandamentos da lei de Deus são dez:
| Eu sou o Senhor teu Deus:
| 1.º Não terás outro Deus diante de mim.
| 2.º Não tomar o nome de Deus em vão.
| 3.º Lembra-te de santificar as festas.
| 4.º Honra pai e mãe.
| 5.º Não matar.
| 6.º Não pecar contra a castidade.
| 7.º Não furtar.
| 8.º Não levantar falso testemunho.
| 9.º Não desejar a mulher do próximo.
| 10.º Não cobiçar as coisas alheias.

(«Non fornicare» → «Não pecar contra a castidade», a forma brasileira, que a resposta da Q 423 explica bem; «Non
nominare il nome di Dio invano» → «Não tomar o nome de Deus em vão», e «nominare il nome di Dio senza rispetto»
→ «tomar o nome de Deus sem respeito».)

**Preceitos da Igreja** (Q 474; os cinco do catecismo, traduzidos)
| Os preceitos da Igreja são cinco:
| 1.º Ouvir Missa todos os domingos e nas outras festas de guarda.
| 2.º Jejuar na Quaresma, nas Quatro Têmporas e nas vigílias mandadas; não comer carne nos dias proibidos.
| 3.º Confessar-se ao menos uma vez por ano, e comungar pela Páscoa da Ressurreição, cada um na sua paróquia.
| 4.º Pagar os dízimos devidos à Igreja, segundo os costumes.
| 5.º Não celebrar o casamento nos tempos proibidos, isto é, do primeiro domingo do Advento até a Epifania, e do primeiro dia da Quaresma até a oitava da Páscoa.

**Sacramentos**: Batismo, Crisma (ou Confirmação), Eucaristia, Penitência, Extrema-Unção, Ordem e Matrimônio.
**Virtudes teologais**: fé, esperança e caridade. **Cardeais**: prudência, justiça, fortaleza e temperança.
**Dons do Espírito Santo**: sabedoria, entendimento, conselho, fortaleza, ciência, piedade e temor de Deus.
**Vícios capitais** (Q 961): soberba, avareza, luxúria, ira, gula, inveja e preguiça.
**Obras de misericórdia corporais**: dar de comer a quem tem fome; dar de beber a quem tem sede; vestir os nus; dar
pousada aos peregrinos; visitar os enfermos; visitar os presos; enterrar os mortos.
**Espirituais**: dar bom conselho a quem está em dúvida; ensinar os ignorantes; corrigir os pecadores; consolar os
aflitos; perdoar as ofensas; suportar com paciência as pessoas importunas; rezar a Deus pelos vivos e pelos mortos.
**Bem-aventuranças** (Q 926): «Bem-aventurados os pobres de espírito, porque deles é o reino dos céus», «…os
mansos, porque possuirão a terra», «…os que choram, porque serão consolados», «…os que têm fome e sede de justiça,
porque serão saciados», «…os misericordiosos, porque alcançarão misericórdia», «…os puros de coração, porque verão
a Deus», «…os pacíficos, porque serão chamados filhos de Deus», «…os que sofrem perseguição por amor da justiça,
porque deles é o reino dos céus».
**Jaculatórias e orações curtas do cap. V.8** (traduza do italiano, por «vós»); as conhecidas no Brasil ficam na forma
de lá: «Graças e louvores se deem a todo momento ao Santíssimo e Diviníssimo Sacramento»; «Doce Coração do meu
Jesus, fazei que eu vos ame cada vez mais». Nomes de orações: «Pater noster» → «Pai-Nosso»; «Ave Maria» → «Ave-Maria»;
«Credo» fica; as que no Brasil se dizem pelo nome latino ficam em latim e itálico: _Angelus Domini_ (ou _Angelus_),
_De profundis_, _Requiem_.

## 6. Citações da Escritura e de Cristo

Traduza do italiano do catecismo, sem copiar Bíblia moderna (ex.: Q 153, «Tu és Pedro, e sobre esta pedra
edificarei a minha Igreja…»). O catecismo não dá referências; não as acrescente.

## 7. Antes de entregar

1. Mesmo número de blocos que o original, arquivo por arquivo; cada pergunta com o mesmo número; as linhas `| ` em
   igual número; a marca `[parte.n]` no mesmo bloco; os `## ` nos mesmos lugares. Script de conferência:
   `python3 edicoes/catecismo-pio-x/conferir.py [arquivo …]` (tem de dizer «ok»).
2. Grep de mesóclise sem resultado.
3. As fórmulas do § 5 iguais, letra por letra.
4. Releitura: sentido trocado, falso amigo («salute», «roba», «divozione», «parroco»), concordância, crase.
5. Notas do tradutor em `traducao/notas-<lote>.md`: termos novos, passagens difíceis, erros do italiano (com o
   número da pergunta), decisões que o Gere deveria ver.
