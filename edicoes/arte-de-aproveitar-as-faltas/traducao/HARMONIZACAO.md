# Harmonização: A arte de aproveitar as próprias faltas, de Joseph Tissot

Harmonização das quatro partes traduzidas (`00-avant-propos.txt`, `01-primeira-parte.txt`, `02-segunda-parte-a.txt`, `02-segunda-parte-b.txt`), feitas por tradutores diferentes. Outubro de 2026.

Foram lidos o guia geral, o `CONVENCOES.md` da obra, o `original/LEIAME.md`, as quatro traduções inteiras, lado a lado com o original, e as quatro notas dos tradutores. Valeram as decisões do coordenador para esta obra.

Os termos e as regras que ficaram valendo estão no `CONVENCOES.md`, na nova seção «8. Termos fixados na harmonização». As notas dos tradutores (`notas-*.md`) ficam como registro do trabalho de cada parte. Onde divergem desta harmonização, vale esta.

## 1. Decisões do coordenador aplicadas

| decisão | como ficou | arquivos |
|---|---|---|
| Título do livro dentro do texto: em português, com «próprias», contraído | «da _Arte de aproveitar as próprias faltas_». Já estava assim em 00 e 02-b; fixado no CONVENCOES | — |
| Epígrafe do rosto antes da Advertência, em latim, com [Trad.] | `_Misericordias Domini in æternum cantabo._ (Sl LXXXVIII.) [Trad.: Cantarei eternamente as misericórdias do Senhor.]`, primeiro parágrafo de 00. No original também: `(Ps. LXXXVIII.)`, como no rosto do scan, por meio do `montar.py` | 00 (tradução e original) |
| Hb VI, 12 (é IV, 12) e «Eccl. XVII, 6» (é Eclo XVIII, 6): manter, usar «Eclo», registrar | «(Hb VI, 12)» mantido; «(Ecl XVII, 6)» → «(Eclo XVII, 6)»; os dois registrados no `emendas.txt` | 01 |
| «Puits-d'Ordre» (nota 79) → «Puits-d'Orbe» | Tradução: «Carta à abadessa do Puits-d'Orbe». Original emendado (*de Puits-d'Orbe*) e registrado | 01 (tradução e original) |
| Prenomes: forma portuguesa para os santos e figuras com forma corrente | Regra e lista no CONVENCOES, § 8. Os quatro arquivos já seguiam a regra (Frederico Ozanam, Cláudio de la Colombière, Carlos Augusto de Sales, Maria de Sales Chappuis, Angélica Arnaud, Margarida Maria, Benigna Gojos). Os religiosos obscuros ficam em francês (Alexandre de Saint-François, M.-Mélanie Pommeroy, Raoul d'Asti) | — |
| Citações da Filoteia: harmonizar com a nossa tradução | Ver a seção 3 | 01, 02-a, 02-b |
| Colóquio para *Entretien* | Já estava em todos (21 ocorrências, com «Colóq.» para *Entret.*, *Entr.*) | — |
| Nota 58 de 02-b: «Páginas 84 e 190» com [Trad.] | «¤ [58] Páginas 84 e 190. [Trad.: paginação da 3.ª edição; os lugares parecem ser I, cap. III, n.º 7, e II, cap. IV, n.º 2, em nota.]». A tradução tinha trocado a remissão por capítulos | 02-b |
| Numeração do cap. VIII (1, 2, 2, 3, 5...) mantida e registrada | Mantida; registrada no `emendas.txt` como não emendada | — |
| «pensa n'Ela» (cap. VIII, n.º 6) | Mantido | — |
| Mais referências erradas a registrar: Lc VII, 48 (47); Lc VII, 35 (37); Sl LXXXIII (LXXXIV) | Mantidas e registradas, com as que a tradutora de 02-a apontou (ver a seção 5) | — |
| Latim das notas em itálico | Mantido nos quatro arquivos | — |
| 02-a: *tenant des pécheurs* (entre aspas) → «o que responde pelos pecadores»; *caution* → «fiador dos pecadores» | «à sua qualidade de «o que responde pelos pecadores»»; «como fiador dos pecadores» já estava | 02-a |
| 02-a: são Bernardo, «la soutient» mantido | «quando é a humildade que a ampara», mantido | — |
| *M. l'abbé* → «o padre»; *M.* (leigo) → «o senhor»; «M. J.-J. Allemand» é o mesmo padre | 01, nota 55: «O senhor J.-J. Allemand» → «O padre J.-J. Allemand» | 01 |
| Corrigir no original «disentils» → «disent-ils» (cap. I, n.º 5) e registrar | A causa era a montagem: o impresso tem «disent-» no fim da pág. 58 e «ils» na 59, e o `montar.py` tirou o hífen como se fosse de fim de linha. Corrigido nos arquivos de revisão (`revisado/015.txt` e `016.txt`), original remontado, emenda registrada. Procurei o mesmo erro nas outras 23 viradas de página com hífen e não há outro caso | original 02-a |

## 2. Termos uniformizados

| termo (francês) | variantes encontradas | escolha | arquivos mudados |
|---|---|---|---|
| *avancement* | «adiantamento» (01: 4 vezes; 02-a: 2), «progresso» (02-b: 2) | «progresso», como na Filoteia; *avancé* continua «adiantado» | 01, 02-a |
| *reconnaissance* (para com Deus) | «gratidão» (02-a, 02-b), «reconhecimento» (02-b, cap. VIII, n.º 12) | «gratidão». Exceção: «o conhecimento gera o reconhecimento» (Filoteia III.5), por causa do jogo de palavras | 02-b |
| *« tenant des pécheurs »* | «fiador dos pecadores» | «o que responde pelos pecadores» (decisão) | 02-a |
| *M. J.-J. Allemand* / *M. l'abbé J. Allemand* | «o senhor» (01), «o padre» (02-a) | «o padre» | 01 |
| *Évêque* (na voz de Tissot) | «bispo» (00, 01, 02-a), «Bispo» (02-b) | «bispo», em minúscula | 02-b |
| *Religieuse(s)*, *Religieux* | «religiosa» (00, 02-a), «Religiosas» (01), «Religioso» (02-b) | minúscula | 01, 02-b |
| *Directeur* | «meu Diretor» (01, citação de III.9) | «meu diretor» | 01 |
| *P. La Rivière* / *P. la Rivière* | «Padre La Rivière», «Padre la Rivière» (01, nota 67) | «La Rivière» | 01 |
| *Puits-d'Orbe* / *Puits-d'Ordre* | as duas | «Puits-d'Orbe» | 01 |
| *Eccl.*, *Eccli.* | «Ecl» (01, nota 88), «Eclo» | «Eclo» | 01 |
| número do livro bíblico | «II Cor» (01), «2 Cor», «1 Cor», «1 Jo», «2 Mc» | algarismo arábico: «2 Cor XI, 14» | 01 |
| vírgula depois do livro | «Lc, III, 43» (01), «Lc XIV, 10» (02-a) | sem vírgula | 01 |
| *mouchons* (das abelhas) | «larvas» (01, IV.2) | «crias», como na Filoteia | 01 |
| pronomes combinados | «lhos», «no-la» (02-b) | evitados, como na Filoteia; «vo-lo», «no-lo», «no-los», «vo-los» ficaram | 02-b |
| *Entretien* | «Colóquio» em todos | «Colóquio» | — |
| *collect. Blaise*, *coll. Blaise*; *édit. Meyer* | «coleção Blaise»; «edição Meyer» em todos | idem | — |
| abreviaturas bíblicas | já portuguesas, sem ponto, em todos | lista fixada no CONVENCOES, § 8 | — |
| latim das notas | itálico nos quatro, contra o redondo do impresso | itálico | — |
| títulos dos capítulos | «## Capítulo N — ...»; na Segunda parte, «Aproveitar as faltas para...» | idem | — |
| aspas | angulares, com “...” dentro, em todos | idem | — |
| tratamento | vós (são Francisco às dirigidas, Tissot ao leitor, as orações, Tissot à Virgem); tu (Deus à alma, a alma a si mesma, o apelo ao pecador no cap. VIII) | idem, já coerente nos quatro | — |

Também conferidos e já coerentes: «o Bem-aventurado», «o nosso Santo», «o Doutor», «os Santos»; «Aquele», «Daquele» para *Celui* (Deus); «Ela» para Maria no cap. VIII; «são», «santa» em minúscula; *S.*, *Mgr*, *P.* por extenso; «Carta 793.ª»; «Sermão para o primeiro domingo da Quaresma»; «_Introd. à vida devota_, 1.ª parte» e «III parte»; «Nosso Senhor», «Nossa Senhora», «o bom Deus»; *chétif* → «mesquinho», como na Filoteia; *il ne faut pas* → «não se deve», «não convém».

## 3. Citações da Filoteia alinhadas com a nossa tradução

Base: a tradução atual da Filoteia (`edicoes/introducao-a-vida-devota/traducao/01-primeira-parte.txt`, `02-segunda-parte.txt`, `04-quarta-parte.txt`). As passagens foram achadas pelas notas de Tissot e por uma busca de sequências de 5 e 6 palavras iguais entre os dois originais franceses. A redação da Filoteia foi adotada; o que segue «ajuste» é onde o texto de Tissot difere do de são Francisco e a tradução acompanha Tissot.

| Tissot | Filoteia | ajuste ao texto de Tissot |
|---|---|---|
| I.1, n.º 3, nota 16 («São Paulo, num só momento...») | I.5 | Tissot omite «santa Madalena» e «e cura» (*La purification ordinaire*, no singular); tem *ils ne volent pourtant pas, ils montent* («mas, contudo, não voam; sobem»), *remonte* («torna a subir») e um ponto antes de «As doenças». A Filoteia trouxe «pretendê-la», «quer..., quer...», «por progressos», «a cavalo e a galope» (antes «pela posta») |
| I.2, n.º 1, nota 30 («A tristeza que é segundo Deus...») | IV.12 | Tissot tem *bonne ou mauvaise*, *selon les dispositions* (a Filoteia, *les diverses productions*) e as referências entre parênteses: ficou «boa ou má», «conforme as disposições», «mais más que boas». Da Filoteia: «porque só produz», «o que fez o Sábio dizer», «mata a muitos» |
| I.2, n.º 1, nota 32 («A má tristeza...») | IV.12 | Tissot intercala «retoma o nosso Santo» e começa frase nova em *Bref*. Da Filoteia: «a põe em inquietação», «tira o gosto da oração», «porque tira» |
| I.2, n.º 2, nota 36 («Não nos perturbemos com as nossas imperfeições») | I.5 | Já coincidia |
| I.3, n.º 4, nota 87 («Mas vedes que a montanha da perfeição...») | IV.2 | Tissot omite *chrétienne*, *extrêmement*, *voisines*, *à la quête* e o *ce* de *ce dites-vous*, e tem *sur les fleuves*, onde a Filoteia tem *sur les fleurs*: ficou «rios» (ver a seção 7). Da Filoteia: «crias» (antes «larvas»), «alimentando-se», «ganham asas», «paisagem», «cimo», «sair-nos», «entretanto», «para que» |
| I.3, n.º 4, nota 90 («É preciso, pois, ser corajosa e paciente...») | I.5 | Tissot salta de um parágrafo ao outro («...!...»), glosa «(a purificação da alma)», omite *de voir* («que pena dão as almas que...») e tem *nous ne sommes jamais tenus pour vaincus* («nunca somos tidos por vencidos») e *Délivrez-moi* sem aspas («Livrai-me»). Da Filoteia: «muitas imperfeições», «largar tudo», «para exercício», «os pecados veniais não nos podem tirar», «uma feliz condição... sermos sempre vencedores» |
| II.1, n.º 7, nota 51 («é um pecado geral...») | I.12 | Tissot tem *sur tous les autres* (a Filoteia, *par*): «que se derrama sobre todos os outros» |
| II.1, n.º 7, nota 55 («Dizei ao vosso coração: Eia, meu coração!...») | I.11 | Tissot introduz com «Dizei ao vosso coração» e corta «e por mim». Da Filoteia: «desleal para com este grande benfeitor», «como não há de a minha alma estar doravante sujeita» |
| II.6, n.º 1, nota 24 («O escorpião que nos picou...») | I.19 | A nota 24 de Tissot é só um paralelo latino; o texto é da Filoteia. Da Filoteia: «quando nos pica», «remédio», «quando o cometemos» |
| II.6, n.º 1, nota 25 («A contrição e a confissão...») | I.19 | Tissot tem *le mal qui nous tourmente* (a Filoteia, *ce qui*), *ce sang répandu* (a Filoteia, *son sang*) e *Passion* com maiúscula: «o mal que nos atormenta», «desse sangue», «Paixão». O resto, da Filoteia («fedor», «imaginai-vos no monte Calvário», «por todos os lados», «em volta dos confessionários») |
| II.6, n.º 1, nota 26 («Praticais (pela confissão)...») | II.19 | Tissot põe o verbo no presente e a glosa entre parênteses, e tem *vertus* no plural: «Praticais», «mais virtudes». Da Filoteia: «; e, nesta única ação da confissão,», «do que em nenhuma outra» |

**Atenção:** se a harmonização da própria Filoteia mudar estas passagens (por exemplo «a galope», «crias», «fedor»), convém repetir a mudança aqui.

## 4. Citações de capítulos da Filoteia ainda não traduzidos (III.1–13): conferir depois

_Feito no retoque final (seção 10)._

A Filoteia 03-a (III.1–13) ainda está em tradução. Estas passagens ficaram com a redação dos tradutores do Tissot e devem ser alinhadas quando ela estiver pronta:

| Tissot | arquivo | Filoteia | começo da citação |
|---|---|---|---|
| I.1, n.º 6, nota 29 | 01 | III.9 | «Levantai, pois, o vosso coração, quando ele cair, bem docemente...» (inclui «a miséria mísera»; a Filoteia 03-a, na primeira versão, tem «a miséria mesquinha») |
| I.2, n.º 4, nota 57 (dois parágrafos) | 01 | III.9 | «Uma das boas práticas que poderíamos fazer da doçura...»; «Pois, ainda que a razão queira que...» |
| I.2, n.º 5, nota 66 (três parágrafos) | 01 | III.9 | «É preciso, pois, ter das nossas faltas um desprazer...»; «Crede-me, Filoteia...» (com «meu diretor»); «Se, todavia, alguém achar...» |
| I.2, n.º 2, nota 41 | 01 | eco de III.9 | «Eu disse isto na _Introdução à vida devota_...» (é do _Tratado do amor de Deus_, IX, 7, mas repete III.9: conferir os termos) |
| II.1, n.º 3, nota 14 | 02-a | III.6 | «verdadeiro conhecimento e voluntário reconhecimento da nossa abjeção» |
| II.1, n.º 7, nota 53 | 02-a | III.5 | «Certamente, nada nos pode humilhar tanto diante da misericórdia de Deus...» (com o jogo «o conhecimento gera o reconhecimento») |
| II.2, n.º 1, nota 60 | 02-a | III.6 | «O alto ponto da humildade... está não só em reconhecer voluntariamente a nossa abjeção...» |
| II.2, n.º 5, nota 74 | 02-a | III.6 | «Se me desregrei por cólera ou por dissolução...» |
| II.2, n.º 5, nota 75 | 02-a | eco de III.6 | «Não obstante, minha filha... ainda que amemos a abjeção que se segue do mal...» (carta a santa Chantal, com frases de III.6) |
| II.2, n.º 5, nota 76 | 02-a | III.6 | «a nossa abjeção de diante dos seus olhos, é preciso guardá-la e escondê-la no nosso coração» |

## 5. Emendas ao original e registro no `emendas.txt`

Feitas em `ferramentas/cache/faltas/revisado/` e no `montar.py`, com o original remontado (a remontagem sem as mudanças reproduzia os quatro arquivos byte a byte). Tudo registrado no fim do `emendas.txt`, numa seção «Harmonização da tradução».

- **Emendados:**
  - epígrafe do rosto acrescentada no começo de `00-avant-propos.txt`;
  - nota 79 de 01 (pág. 36): *Puits-d'Ordre* → *Puits-d'Orbe*;
  - 02-a, cap. I, n.º 5 (págs. 58–59): *disentils* → *disent-ils*.
- **Mantidos e registrados** (referências erradas do impresso):
  - Hebr. VI, 12 (é IV, 12); Eccl. XVII, 6 (é Eclo XVIII, 6), pág. 41;
  - Prov. XXX, 13 (nota; o texto dá XXX, 23), pág. 57;
  - *Introd.*, 1re partie, chap. II (é o cap. 11), nota da pág. 67 (nota 55 de 02-a);
  - Ps. LXVI, 11 (é LXXVI, 11), pág. 91;
  - Rom. VIII, 24 (é VII, 24), pág. 105;
  - I Cor. XII, 9 (é II Cor. XII, 9), pág. 108;
  - Luc. VII, 48 (é 47), pág. 141; Luc, VII, 35 (é 37), pág. 145;
  - Ps. LXXXIII (é LXXXIV), nota da pág. 155;
  - a numeração 1, 2, 2, 3, 5 do cap. VIII;
  - *Roothan* (pág. 31), mantido no original; «Roothaan» na tradução;
  - *sur les fleuves* na citação de IV.2 (pág. 40), onde a Filoteia tem *fleurs*.
- O `original/LEIAME.md` foi atualizado: epígrafe, as duas emendas novas, as referências registradas, as contagens de 00 (12 parágrafos, 379 palavras; total 399 e 37.055), a remissão da nota 58 e as citações da Filoteia.

## 6. Correções de sentido e de português

A leitura integral não achou erro de sentido que as revisões das partes não tivessem corrigido. As correções miúdas desta harmonização:

- 01, I.1, n.º 5: «aplicar até ao pecado mortal» → «aplicar mesmo ao pecado mortal» (o «até ao» é lusitano).
- 02-b, II.7, n.º 8: «e nunca lhos teria perdoado» → «e nunca os teria perdoado».
- 02-b, II.8, n.º 8: «são Gregório Nazianzeno no-la apresenta, numa linguagem poética, dizendo...» → «são Gregório Nazianzeno, numa linguagem poética, apresenta-a dizendo...».
- 02-b, II.8, n.º 12: «O meu reconhecimento pelos vossos cuidados» → «A minha gratidão pelos vossos cuidados» (termo).
- As da seção 3, que também corrigem miudezas da primeira versão das citações («pretender a ela» → «pretendê-la»; «que lástima são as almas» → «que pena dão as almas»).

## 7. Apresentação da edição (`obra.py`)

- `PARTES` confere com os arquivos de `traducao/`: Advertência (00), Primeira parte (01), Segunda parte (02-a + 02-b).
- «Sobre esta tradução» acrescido do que foi feito: erros de impressão corrigidos e referências erradas mantidas; a epígrafe que abre o livro; as citações da _Filoteia_ pela nossa tradução; o tratamento por _vós_ e por _tu_. «São Francisco» passou a «são Francisco» no corpo do texto (fica «Missionários de São Francisco de Sales», nome da congregação).

## 8. Conferências

Script: `C:\Users\geren\AppData\Local\Temp\claude\arte-de-aproveitar-as-faltas-harmonizacao\conf.py`, arquivo a arquivo contra o original.

| arquivo | blocos | parágrafos | títulos `##` | notas | marcas | chamadas | números do autor | cabeçalho |
|---|---:|---:|---:|---:|---|---:|---|---|
| 00-avant-propos.txt | 13 | 12 | 1 | 0 | — | 0 | — | igual, só `# titulo:` traduzido |
| 01-primeira-parte.txt | 212 | 110 | 3 | 99 | I.1–I.3 | 99 | iguais | igual |
| 02-segunda-parte-a.txt | 264 | 141 | 4 | 119 | II.1–II.4 | 119 | iguais | igual |
| 02-segunda-parte-b.txt | 244 | 136 | 4 | 104 | II.5–II.8 | 104 | iguais | igual |

- Mesma sequência de tipos de bloco (título, parágrafo, nota), mesmas chamadas `[n]` nos mesmos blocos, mesmas notas `¤ [n]`.
- Tamanho: nenhum bloco abaixo de metade do original. Os dois acima do dobro são o [Trad.] da epígrafe (00) e o da nota 58 (02-b).
- Aspas: o saldo de «» por bloco é o do original em todos os blocos, salvo o da oração do Pai-nosso (01, I.1, n.º 2), onde a tradução fecha as aspas internas que o impresso não fecha (ver as notas de 01).
- **Mesóclise:** as duas varreduras (o grep do CONVENCOES e a mesma regex em Python, terminada em `(?![A-Za-zÀ-ÿ])`) não acham nada nas quatro traduções, no CONVENCOES, no `obra.py`, no LEIAME, nas notas e neste arquivo.

## 9. Para o Gere decidir

1. **Citações de III.1–13 (seção 4).** Até serem alinhadas, a frase do «Sobre esta tradução» («as que vêm da _Filoteia_ seguem a nossa tradução») vale só para as dos capítulos já prontos. Convém alinhá-las antes de publicar.
2. **«rios» em IV.2 (I.3, n.º 4).** Tissot dá *sur les fleuves*, provável erro dele ou da edição que usou; a Filoteia tem *sur les fleurs*. Ficou «rios», fiel ao texto de Tissot. A alternativa é «flores», com registro.
3. **Nota 55 de 02-a**, «_Introd. à vida devota_, 1.ª parte, cap. II»: a passagem é de I.11. Ficou como o impresso (talvez «II» por «11»). Pode virar «cap. 11» na tradução, com registro.
4. **Latim sem tradução nas notas** (01, notas 82 e 94; 02-a, notas 2, 15, 39, 40, 83; 02-b, notas 24, 42, 75, 81, 95, entre outras, e as frases latinas do texto). O guia da obra não pede «[Trad.: ...]», e só a epígrafe o recebeu. O Chautard usa [Trad.] nas notas inteiramente em latim; se for para igualar, são esses lugares.
5. **«vo-lo», «no-lo», «no-los», «vo-los»** (7 lugares) ficaram; só «lhos» e «no-la» saíram. Se a regra da Filoteia for para valer por inteiro, trocam-se também.

## 10. Retoque final

Outubro de 2026, depois da harmonização da Filoteia (`edicoes/introducao-a-vida-devota/traducao/HARMONIZACAO.md`). Resolve os itens 1, 4 e 5 da seção 9.

### 10.1 Citações de III.1–13 alinhadas (seção 4)

Base: a Filoteia definitiva (`03-terceira-parte-a.txt`). Cada passagem foi comparada palavra a palavra, em francês (Tissot × Filoteia) e em português (Tissot × Filoteia). Ficou a redação da Filoteia; os ajustes são só onde Tissot muda o texto.

| Tissot | Filoteia | ajuste ao texto de Tissot |
|---|---|---|
| I.1, n.º 6, nota 29 | III.9 | nenhum («da vossa queda», «a miséria mesquinha», «com uma grande coragem e confiança na sua misericórdia», da Filoteia) |
| I.2, n.º 2, nota 41 (eco, _Tratado_ IX, 7) | III.9 | «assentado» → «sereno», como *rassis* na Filoteia |
| I.2, n.º 4, nota 57 (dois parágrafos) | III.9 | Tissot divide o parágrafo em dois, começa frase nova em *Outre* («Além de que») e tem *d'autre origine* («não têm outra origem senão o amor-próprio») |
| I.2, n.º 5, nota 66 (três parágrafos) | III.9 | Tissot corta em *inclinations...*, antes do exemplo da castidade: o «cometida contra a castidade» da Filoteia emendada não entra. Tem *tout ainsi qu'un* («assim como um»), *dorénavant* e *désormais* («doravante», «agora»), *la censure et une répréhension* («a censura e uma repreensão»), as falas do coração sem aspas e com exclamações, *Directeur* («diretor») |
| II.1, n.º 3, nota 14 | III.6 | nenhum («o verdadeiro conhecimento e o voluntário reconhecimento») |
| II.1, n.º 7, nota 53 | III.5 | Tissot corta a frase final (a Virgem) e tem *Prince* com maiúscula («Príncipe»). Da Filoteia: «miudamente», «nos inche», «não vem de nós», «nos viesse fazer cócegas», «obra nossa nem fruto do nosso chão»; «o conhecimento gera o reconhecimento» mantido |
| II.2, n.º 1, nota 60, e o eco «esse ponto alto» | III.6 | nenhum («O ponto alto da humildade... consiste não somente...») |
| II.2, n.º 5, nota 74 | III.6 | Tissot tem *inconvenantes* («inconvenientes»), *sont offensés* e *m'efforcerai* («me esforçarei por»), onde a Filoteia tem *indécentes*, *est offensé*, *m'essaierai* |
| II.2, n.º 5, nota 75 (eco, carta a santa Chantal) | III.6 | as frases comuns pela Filoteia: «nem por isso se deve deixar de remediar o mal», «se um se pudesse separar do outro» |
| II.2, n.º 5, nota 76 | III.6 | nenhum («escondê-la dentro do nosso coração») |

**As onze da seção 3, reconferidas** contra a Filoteia harmonizada, do mesmo modo: as diferenças são só os ajustes já listados lá. Os termos que a harmonização da Filoteia mudou (*conducteur* → guia, *débonnaireté* → mansidão, *empressement* → afã, *avancement* → progresso, *affection* → afeição/afeto, «cara Filoteia», *dîner* → almoço) não caem dentro de nenhuma passagem citada; «a galope», «crias» e «fedor» continuam na Filoteia. Uma busca de sequências de 5 palavras iguais entre os dois originais franceses, com qualquer número de coincidências, não achou outra citação da Filoteia no Tissot. Fora das citações, «pressa» por *empressement* fica (nota 37 de 01, que é de uma carta).

### 10.2 Latim das notas: «[Trad.: ...]» (item 4 da seção 9)

Acrescentado, curto, depois do latim que vem sem tradução do autor: 01, notas 82 (Crisóstomo) e 94 (Eclo XI, 22-23); 02-a, notas 2 (hino *Pange lingua*, em prosa, como o [Trad.] dos versos *Ex quo omnia* no Chautard), 15 (Nm XXIV, 4), 39, 40, 49 (são Jerônimo, *Drachma periit*), 83 (Jó XI, 17) e 108 (ladainha e *Confiteor*); 02-b, notas 24 (Eclo IV, 24-25), 42 (Is XXXI, 6), 75, 81 e 95 (prosa antiga, três versos separados por « / »). Ficaram sem [Trad.]: a nota 26 de 02-a (Tissot traduz), as palavras latinas soltas dentro de frase portuguesa (*Felix culpa!*, nota 34 de 02-b; *Fiat! Fiat!*, nota 8 de 02-b), os títulos de obras e as referências. No corpo, nada. Regra fixada no CONVENCOES, § 8.

### 10.3 Pronomes combinados (item 5 da seção 9)

Os sete que restavam saíram:

| arquivo | antes | agora |
|---|---|---|
| 01, I.3 (Crisóstomo) | «eu vo-lo direi em todos os meus discursos» | «eu vos direi isto em todos os meus discursos» |
| 01, I.3 | «eu vo-lo ordeno por todo o poder» | «eu vos ordeno isto por todo o poder» |
| 02-a, II.1 | «tais como no-los revela a Igreja» | «tais como a Igreja nos revela» |
| 02-a, II.4 | «os seus confidentes no-lo dizem bastante» | «os seus confidentes nos dizem isso bastante» |
| 02-b, II.7 | «a sua misericórdia, que vo-los perdoou» | «que vos perdoou» |
| 02-b, II.7 | «como já no-lo insinuou o nosso Bem-aventurado Doutor» | «como já nos insinuou» |
| 02-b, II.8 | «são unânimes em no-lo afirmar» | «são unânimes em afirmá-lo» |

Varredura (*lho*, *lhos*, *lha*, *lhas*, *no-lo(s)*, *no-la(s)*, *vo-lo(s)*, *vo-la(s)*): nada nos quatro arquivos traduzidos.

### 10.4 `obra.py` e CONVENCOES

- «Sobre esta tradução»: a frase das citações da _Filoteia_ («seguem a nossa tradução») passa a valer para todas; acrescentado que o latim das notas sem tradução do autor vem com «[Trad.: ...]».
- CONVENCOES, § 8: a regra do latim, a das citações de III.1–13 e a dos pronomes combinados, atualizadas.

### 10.5 Conferências

O script da seção 8, de novo, contra o original: 00, 13 blocos; 01, 212; 02-a, 264; 02-b, 244. Mesma sequência de tipos de bloco, marcas `[I.1]`–`[II.8]`, chamadas `[n]` nos mesmos blocos (99, 119, 104), notas `¤ [n]` iguais, números do autor iguais, cabeçalhos iguais; 0 erros. O saldo de «» só difere no bloco do Pai-nosso (01), como antes. Os blocos mais longos que o dobro do original são as notas que receberam [Trad.]. **Mesóclise:** o `grep` do CONVENCOES e a regex em Python com `(?![A-Za-zÀ-ÿ])` não acham nada nas quatro traduções, no CONVENCOES, no `obra.py`, no LEIAME, nas notas e neste arquivo.
