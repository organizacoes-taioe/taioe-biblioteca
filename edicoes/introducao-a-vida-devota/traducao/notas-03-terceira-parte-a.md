# Notas do tradutor: Terceira parte, capítulos I a XIII

Arquivo: `traducao/03-terceira-parte-a.txt`. Texto-base: `original/03-terceira-parte-a.txt` (Boulenger, 1909, texto de 1619, via Wikisource).
Texto de conferência: Annecy, t. III (1893), no OCR de `ferramentas/cache/filoteia/annecy3.txt`, consultado nos lugares duvidosos (ver «Emendas»).

## O que foi conferido

- **Parágrafos.** 103 blocos no francês e 103 na tradução, mais o bloco do cabeçalho, na mesma ordem: 90 parágrafos de texto (o sumário da parte e o dístico de III.1 incluídos) e 13 títulos.
- **Títulos.** Os 13 títulos `## Chapitre N — ...` viraram `## Capítulo N — ...`, com os romanos iguais.
- **Marcas.** As 13 marcas, de `[III.1]` a `[III.13]`, iguais e na mesma ordem, no começo do primeiro parágrafo de cada capítulo. O `[I.1]` que aparece na linha `# nota:` do original é do cabeçalho do arquivo, não do texto.
- **Notas.** O arquivo não tem chamadas `[n]` nem notas `¤`, como diz o LEIAME.
- **Cabeçalho.** Só `# titulo: Terceira parte da Introdução, capítulos I a XIII`, como manda o CONVENCOES.
- **Itálicos.** Os três do original: o sumário («_Contendo vários avisos acerca do exercício das virtudes._»), _Da pudicícia_ (título de Tertuliano, III.13) e _agnus castus_ (III.13). Os dois sublinhados soltos de III.4 («s_y amuser», «affectionne _ et») são restos de marcação e não abrem itálico nenhum; foram ignorados.
- **Pontuação.** Conferida parágrafo a parágrafo por script: «!», «?», «;», «:», ««» e «(» batem em todos os parágrafos, salvo o parêntese solto de III.7 (ver «Emendas»).
- **Tamanho.** Cada parágrafo traduzido tem entre 82% e 103% do tamanho do original, em caracteres. O de 82% é o curto fecho de III.6 («Eu vos disse muitas coisas...»), conferido: está inteiro.
- **Mesóclise.** O `grep` do CONVENCOES e a varredura em Python com `(?![A-Za-zÀ-ÿ])` não acharam nada. Também não há «lho», «no-lo», «vo-lo».
- **Versos.** O dístico de III.1, pelo método do Versificador; ver «Versos».

## Decisões gerais

- **Tratamento.**
  - Filoteia por **vós** do começo ao fim. Onde o francês põe o adjetivo no feminino, o português também: «Sede paciente», «acusada», «culpada», «cuidadosa e diligente», «teimosa nem rabugenta», «vil, abjeta ou louca», «acabrunhada».
  - Em III.7 o autor passa ao masculino genérico («vous êtes un hypocrite», «homme de bas courage»), e assim ficou.
  - Falas de terceiros seguem o original: a jovem a são João Esmoler, por *tu*; santo Antão aos dois, por *vós*; Eliseu à viúva, por *vós*; Isaías a Acaz, por *tu*; santo Agostinho a Auxílio, por *tu*.
  - O coração repreendido em III.9 é tratado por **tu**, como no francês («Não és tu miserável...»; «meu pobre coração... levantemo-nos»). O Sl 42 («Por que estás triste, ó minha alma») também por *tu*.
- **«Voyez-vous».** Ficou «Vedes», como o autor o emprega, de passagem: «Vedes, Filoteia, era o zelo...». Em III.10 ficou «Bem vedes que, se ela...», para a frase não se ler como «vedes se».
- **«Bien» de reforço** (*voudraient bien*, *s'empêchent bien*, *requiert bien*). O decalque «querer bem», «requerer bem» é galicismo. Ficou «bem gostariam», «guardam-se bem», «requer, sim», «escolhe-se, sim», «consente de bom grado».
- **Maiúsculas.** Ficaram as de reverência e as do autor: *Deus*, *Senhor*, *Salvador*, *divina Majestade*, *divina Bondade*, *Rei da glória*, *Rei dos santos*, *Apóstolo(s)*, *Esposa*, *Sábio*, *Profeta*, *Doutor Angélico*, *Pai celeste*. «Celui qui», referido a Cristo, ficou «Aquele que» (III.6) e «por amor Daquele que» (III.11). *saint*, *sainte* em minúscula.
- **Escritura.** Traduzida do francês do autor, sem Bíblia portuguesa por baixo, e sem referências acrescentadas (o texto não as dá). Exceção de forma: em III.8, Mt 11,29 ficou «manso e humilde de coração», a forma que todo leitor reconhece (ver «Passagens difíceis»).

## Termos

| francês | tradução | observação |
|---|---|---|
| *douceur*; *doux* | doçura; doce | é a virtude salesiana; «doçura para com o próximo», «doçura para conosco mesmos» |
| *débonnaireté*; *débonnaire* | mansidão; manso | sempre ao lado de *douceur*: «a doçura e a mansidão» |
| *ire* / *colère* / *courroux* | ira / cólera / irritação | III.8 enumera os três («a ira, a cólera e a irritação»); *se courroucer* → irritar-se |
| *abjection*; *abject* | abjeção; abjeto | III.6 |
| *vileté*; *bassesse*; *petitesse* | vileza; baixeza; pequenez | |
| *renommée*; *bonne renommée* | fama; boa fama | título de III.7: «Como se deve conservar a boa fama...» |
| *réputation* | reputação | |
| *prud'homie* | probidade | |
| *empressement*; *s'empresser* | afã; afanar-se | título de III.10: «sem afã nem preocupação»; também em III.4 («não se afanam pelas honras») |
| *souci* / *sollicitude* / *inquiétude* | preocupação / solicitude / inquietação | III.10 opõe os três a *soin* (cuidado) e *diligence* (diligência) |
| *affaires* | negócios | |
| *honnêteté*; *honnête*; *déshonnête* | honestidade; honesto; desonesto | sentido de decoro e pureza, como no guia |
| *lubricité* | luxúria | |
| *volupté*; *délectation* | volúpia; deleite | |
| *impudicité*; *lasciveté* | impudicícia; lascívia | |
| *privautés* | familiaridades | III.13 |
| *avis* | aviso; parecer | «aviso» para o conselho do autor e do Sábio; «parecer» para a opinião de um bispo, de são Gregório, do diretor, dos teólogos |
| *conducteurs*; *directeur* | condutores; diretor | |
| *vacation* | vocação | |
| *loisir* | vagar | III.8, como no Prefácio |
| *remontrances* | admoestações | III.9, como no Prefácio |
| *bizarres* | caprichosos | III.7, como no Prefácio |
| *naïvement*; *naïf* | com singeleza; singelo | |
| *damoiselle* | dama | III.1 e III.6; mulher de condição, não «donzela» |
| *gentilhomme* | fidalgo | |
| *maître, maîtresse* (superiores domésticos) | patrão, patroa | III.11 |
| *police* | governo civil; governo eclesiástico | III.11 |
| *amorces* | engodos | III.12–13 |
| *entamés* (frutos, castidade) | encetados | III.12 |

**Nomes:** santa Paula, são Jerônimo, santo Epifânio; são João (bispo de Alexandria), são João Esmoler; Eulógio de Alexandria; santo Antão; o rei são Luís; são Francisco, são Domingos; são Gregório Magno; Abraão; Tobias; santa Isabel; santa Catarina de Gênova; Cassiano (também «o antigo padre João Cassiano», III.13); santo Atanásio; Jó; são Gregório Nazianzeno; Raab; santo Agostinho; são Bernardo; Saul, Rebeca, Rute, Booz; são Carlos Borromeu; Eliseu; o Doutor Angélico; Acaz; Davi, Micol; Profuturo, Auxílio; José; são Tiago; santa Marta; Salomão; a madre Teresa, o padre Gracián; Alípio; santa Catarina de Sena; são João Crisóstomo; são Basílio; Tertuliano; as ilhas de Tilos (o Tylos de Plínio, no golfo Pérsico); o Peru.

## Versos

O único verso do arquivo é o dístico de III.1, que fecha a imagem dos bordadores (paráfrase do Sl 44, a rainha *in vestitu deaurato, circumdata varietate*).

- **Original.** «En son beau vêtement de drap d'or recamé, / Et d'ouvrages divers à l'aiguille semé.» Dois alexandrinos (6 + 6), 3-6-9-12 nos dois, com rima masculina emparelhada (*recamé / semé*).
- **Tradução.**

  ```
  Em seu belo vestido, em ouro recamado,
  E de vário lavor à agulha semeado.
  ```

- **Medida.** Alexandrino clássico, com lei do hemistíquio. O 1.º verso tem cesura grave com elisão (*vesti‿do‿em*), e o 2.º, cesura aguda (*lavor*).
- **Conferência.** `molde.mjs` com o molde `12: (3)-6-(8)-12 +1` nos dois versos dá 2 exatos (✓), sem ✗ nem ≠. O desenho é 3-6-8-12 nos dois, o 2.º mais frequente do corpus (5,7%). A única licença é a sinérese de *vário*, que é a leitura normal. Os arquivos de trabalho (original, moldes, tradução) ficaram em `C:\Users\geren\AppData\Local\Temp\claude\introducao-a-vida-devota-03a\`.
- **Sentido.**
  - *recamado* é o próprio cognato de *recamé* (bordado em relevo).
  - *vário lavor* traduz *ouvrages divers*.
  - *semeado à agulha* traduz *à l'aiguille semé*.
  - Perde-se só o *drap* (o tecido de ouro), que ficou «em ouro».
- **Rima.** Emparelhada, como no original, mas **grave** (*recamado / semeado*) onde o francês é masculino. O manual pede aguda para a rima masculina; tentei *bordou / semeou*, mas o 2.º verso só saía com hemistíquio grave sem fusão ou com o choque de vogais «que a agulha». O precedente da casa é *O albatroz*, que verte as masculinas de Baudelaire (*mers / amers*) em graves (*largo / amargo*). Ver «Dúvidas».

## Passagens difíceis

- **III.1, *Le roi des abeilles*.** Ficou «o rei das abelhas», como se cria no tempo do autor.
- **III.1, *dit le Proverbe*.** «Diz o Provérbio»: a sentença é de Eclo 22,6, e o autor a cita como provérbio.
- **III.1, *s'incommoder en ce saint exercice*.** «Se estorvar nesse santo exercício» (At 6,2).
- **III.1, *les plus braves*.** *Brave* é «vistoso», «bem-posto»: «as melhores e não as mais vistosas».
- **III.1, *comme par un prix fait*.** É a tarefa ajustada por preço fixo, feita com regularidade: «como por tarefa ajustada».
- **III.1, *caresser les pèlerins*.** «Acolher com carinho os peregrinos».
- **III.1, *alléguant Rahab*.** O sujeito é são Gregório Nazianzeno, que cita o exemplo: «citando Raab».
- **III.3, *c'est là où il y va du bon*.** Ficou «aí é que está o que vale». Ver «Emendas», n.º 5.
- **III.3, *plaindre* / *se plaindre*.** O francês joga com os dois verbos. Ficou «queixar-se» (do próprio mal) e «lamentar» (ter pena de alguém): «não se queixa do seu mal nem deseja que o lamentem».
- **III.3, *Ils ont de la gloire... mais non pas envers Dieu*.** Rm 4,2: «Têm glória, diz o Apóstolo, mas não diante de Deus».
- **III.3, *le travail*** (do parto). «As dores do parto».
- **III.3, *ennuis*.** No sentido forte do século XVII: «tormentos».
- **III.4, *crécerelle*.** «Peneireiro», o falcãozinho que paira no ar.
- **III.4, *goderon*.** A gola franzida em canudos, da moda da época: «uma gola de canudos».
- **III.4, *muguette*.** «Galantear».
- **III.4, *on fait l'essai du baume en le distillant dedans l'eau*.** *Distiller* é aqui «deixar cair gota a gota»: «deixando-o pingar na água».
- **III.5, *bienfaits / méfaits*.** «Benefícios / malefícios»: o eco passa.
- **III.5, *la connaissance engendre la reconnaissance*.** «O conhecimento gera o reconhecimento»: o jogo passa inteiro.
- **III.5, *de notre façon ni de notre crû*.** *Crû* é o que nasce no próprio terreno (como o vinho «do seu cru»): «obra nossa nem fruto do nosso chão».
- **III.5, *ou au fin moins*.** Annecy tem a mesma locução, que é antiga e quer dizer «pelo menos». Não é erro.
- **III.5, *présentions l'avantage*.** «Ofereçamos a precedência».
- **III.5, *il le faut admirer et non pas imiter*.** «É coisa de admirar e não de imitar»: o *le* é neutro.
- **III.6, *En latin abjection veut dire humilité*.** O autor joga com *humilitas* (baixeza, pequenez) do Magnificat. Ficou como está.
- **III.7, *La dissimulation ... de l'injure*.** Não é a hipocrisia, mas o fingir que não se percebe a ofensa: «O fingir que não se vê e o desprezo da injúria».
- **III.7, *une enseigne qui fait connaître où la vertu loge*.** A tabuleta da hospedaria: «uma tabuleta que dá a conhecer onde mora a virtude».
- **III.7, *débordements*.** Duas vezes, a dos rios e a «das línguas injuriosas»: «transbordamentos» nas duas, para a imagem continuar.
- **III.8, *Apprenez de moi que je suis doux et humble de cœur*.** Ficou «manso e humilde de coração», a forma consagrada de Mt 11,29. O leitor perde a ligação literal entre o *doux* de Cristo e a *douceur* do capítulo. Mas a frase seguinte junta logo «a doçura e a mansidão», e o «manso» se liga a essa mansidão. Ver «Dúvidas».
- **III.8, *la grâce de saint Paul*.** É a «terra de Malta», vendida como preservativo contra a mordida de cobra, em memória de At 28,3–6. Ficou «graça de são Paulo», nome que o autor diz ser o comum.
- **III.8, *le bon homme est foulé*.** *Bonhomme* é o homem simples, o camponês: «o homem do povo é pisado».
- **III.8, *sénats et parlements*.** «Senados e tribunais»: os *parlements* franceses eram cortes de justiça. Os *huissiers* são os «meirinhos», e *Paix là!* ficou «Silêncio aí!».
- **III.8, *la tranquillité se fera grande*.** Mt 8,26. A forma óbvia seria mesóclise; ficou «a tranquilidade se fará grande».
- **III.9, *se courroucent de s'être courroucés, entrent en chagrin..., ont dépit...*.** A tripla repetição ficou: «irritam-se de se terem irritado, amofinam-se de se terem amofinado e se despeitam de se terem despeitado».
- **III.9, *confit et détrempé en la colère*.** «Curtido e encharcado na cólera».
- **III.9, *compassion / passion*.** «Mais compaixão dele do que paixão contra ele»: o jogo passa.
- **III.9, *meshui*, *nous ferons prou*.** «Agora», «faremos muito».
- **III.10, *il faut dépêcher tout bellement*.** É o *festina lente* do provérbio: «despachar devagarinho».
- **III.10, *votre ménage*.** A administração da casa: «o vosso governo da casa».
- **III.11, *les trois branches de la croix*.** «Os três braços da cruz».
- **III.11, *C'est un abus de croire...*.** *Abus* é «engano», «ilusão»: «É ilusão crer que, sendo religioso ou religiosa, obedeceríamos facilmente...».
- **III.12, *déchet*; *messéance*.** «Detrimento»; «algo de impróprio».
- **III.12, *Courroucez-vous et ne péchez point* / *Ne vous courroucez point*.** Para guardar o paralelo das duas fórmulas, ficou «Irai-vos e não pequeis» / «Não vos ireis». No resto do arquivo, *se courroucer* é «irritar-se» (por exemplo, José em III.8: «Não vos irriteis pelo caminho»).
- **III.12, *petit papillon*.** É o inseto que voa em volta da chama: ficou «mariposa», que é o nome português dele nessa imagem.
- **III.12, *va brûletant çà et là*.** «Vai chamuscando aqui e ali».
- **III.13, *Je ne sais que c'est que des femmes*.** «Não sei o que são mulheres».
- **III.13, *ains alors*.** «Ou melhor, então...».
- **III.13, *agnus castus* / *le vrai agneau chaste*.** O latim ficou em itálico, e a comparação seguinte diz «o verdadeiro cordeiro casto». O leitor sem latim perde que *agnus castus* é, letra por letra, «cordeiro casto».

## Emendas pela edição de Annecy

Boulenger (no Wikisource) tem erros de transcrição evidentes. A tradução segue Annecy, conferido no OCR onde indicado:

1. **III.1, «Ains il est arrivé. comme dit»** → Annecy, «arrivé, comme»: vírgula.
2. **III.1, «alléguant ahab»** → Annecy, «alléguant Rahab»: «Raab».
3. **III.1, «Gassien raconte»** → Annecy, «Cassian»: «Cassiano».
4. **III.2, «les vertus des. autres»** → Annecy, «les vertus des autres».
5. **III.3, «c'est là où il y du bon»** (falta um verbo) → Annecy, «c'est la ou il y va du bon». Traduzido «aí é que está o que vale».
6. **III.3, «que de possède son âme»** → Annecy, «que de posséder son ame».
7. **III.3, «par ma faute », L'autre»** → ponto final antes de «L'autre».
8. **III.3, «vainquent le mal. vous»** → Annecy, «le mal, vous»: vírgula.
9. **III.3, «crucifié, nu, blasphème»** → Annecy, «blasphémé»: «blasfemado».
10. **III.5, «Qu'gavons-nous»** → «Qu'avons-nous».
11. **III.5, «c'est humilité d'obéir de suivre»** → Annecy, «d'obéir et suivre».
12. **III.5, «des motif»**; **«en son cœur Il est vrai»** → *motifs*; ponto antes de «Il est vrai».
13. **III.6, «plusieurs l'accommodent aux honorables»** → Annecy, «plusieurs s'accommodent»; **«chacun rappellera couardise»** → *appellera*.
14. **III.7, «où la venu loge»** → *vertu*.
15. **III.7, «contre la lune ; (car s'ils peuvent»** → Annecy não tem o parêntese, que nunca se fecha. Foi suprimido.
16. **III.9, «déplaisants jet marris»** → *et*; **«que non par les colères»** → *que non pas*; **«compassion de lui [que de passion»** → colchete solto suprimido.
17. **III.10, «pourvoir s'il a agréable»** → *pour voir*.
18. **III.11, «suivez il encore»** → *suivez encore*.
19. **III.12, «On [appelle»** → colchete solto suprimido; **«Mais quand à ceux»** → *quant*; **«l'infirmité ... passent»** → Annecy, *passe* (sem efeito na tradução); **«saint Ghrysostôme»** → *Chrysostome*.

Sem efeito na tradução: «popu- laire» (hífen de linha), «d abeilles», os sublinhados soltos de III.4.

## Remissões de página

Não há.

## Dúvidas para quem coordena

1. **Rima do dístico de III.1.** Ficou grave (*recamado / semeado*), contra a regra do manual (rima masculina vira aguda). O precedente é *O albatroz*. Se a casa quiser a aguda, é preciso refazer o 2.º verso; a família *-ou* (*bordou / semeou*) foi a única que achei, e rendeu versos piores.
2. ***Douceur* / *débonnaireté*.** Fixei «doçura» e «mansidão». Os outros arquivos da obra (há *douceur* por toda parte, e o capítulo «De la douceur» da Quarta Parte) devem seguir o mesmo par. **Proposta para o guia:** *douceur* → doçura; *débonnaireté* → mansidão.
3. **Mt 11,29.** Ficou «manso e humilde de coração». A alternativa literal, «doce e humilde de coração», guardaria o elo com a *douceur*, mas soa estranha a qualquer leitor católico.
4. ***Empressement*.** Fixei «afã» (e «afanar-se»), com «preocupação» para *souci* e «solicitude» para *sollicitude*. O termo volta muito na obra. **Proposta para o guia:** *empressement* → afã.
5. ***Renommée*.** Fixei «fama», «boa fama». «Bom nome» seria alternativa, mas não dá conta de «a raiz da fama» e de «os cabelos e a barba da nossa fama».
6. ***Ire*, *colère*, *courroux*.** Fixei «ira», «cólera», «irritação». A exceção é o par de III.12, que ficou «Irai-vos... / Não vos ireis».
7. **Nomes.** «Raab» (forma da Vulgata e de muitas Bíblias católicas; outras dão «Raabe»). E «padre Gracián», com a forma espanhola do sobrenome (Jerónimo Gracián).
