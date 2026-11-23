/* O Uraguai — Basílio da Gama
   Gerado por edicoes/o-uraguai/montar.py --publicar. Não edite à mão:
   corrija texto.txt (montar.py), notas1769.txt (notas.py), abertura.txt ou fecho.txt e rode de novo.

   Os versos de cada canto num bloco («| »); {v N} põe o número do verso à margem; «¤ » as notas do autor.
*/
BIBLIOTECA.obra({
  id: "o-uraguai",
  autor: "basilio-da-gama",
  titulo: "O Uraguai",
  ano: 1769,
  genero: "Epopeia",
  divisao: {"singular": "canto", "plural": "cantos"},
  edicao: {
    secoes: {"erros": {"titulo": "Erros da 1ª edição corrigidos", "explica": "À esquerda, a 1ª edição na grafia original."}, "mantidas": {"titulo": "Lições da 1ª edição contra o texto corrente", "explica": "À esquerda, o verso como está aqui (1ª edição); à direita, o que se lê no texto que circula na internet (Wikisource, Domínio Público). O lugar é canto e verso."}},
    apresentacao: `**Texto-base.** Este texto reproduz a primeira edição de _O Uraguai_ (Lisboa, na Régia Oficina Tipográfica, 1769), na grafia brasileira de hoje, com tudo o que ela traz: a dedicatória, o soneto ao Conde de Oeiras, as notas do autor e os dois sonetos «Ao Autor» do fim do livro, de Joaquim Inácio de Seixas Brandão e Inácio José de Alvarenga Peixoto.

**Como foi estabelecido.** Foram confrontados palavra por palavra, por programa, dois exemplares da 1ª edição digitalizados no Internet Archive (o da Biblioteca Pública de Boston e o da Biblioteca Fisher, da Universidade de Toronto), em quatro leituras por OCR, a transcrição da 1ª edição no Wikisource e o texto em grafia atualizada que circula na internet (Wikisource e Domínio Público). Cada diferença de palavra ou de pontuação entre as leituras foi decidida nas imagens dos dois exemplares. O texto corrente tem erros que a 1ª edição corrige («Ninfas do amor» por «Ninfas do mar», «Podres choupanas» por «Pobres choupanas», «Quando pode o temor» por «Quanto pode o temor», entre outros; lista abaixo), perde palavras («nem os caudalosos», «princípio à guerra») e mete entre os versos três linhas das notas. O poema tem 1.377 versos: 244, 365, 329, 289 e 150 nos cinco cantos.

**Grafia.** Mudou só a maneira de escrever (ſ, y, ph, letras dobradas, acentos, _he_ → _é_, _hum_ → _um_), e as formas antigas que não pesam no verso passaram à forma de hoje (_cousa_ → _coisa_, _dous_ → _dois_, _cuberto_ → _coberto_, _frecha_ → _flecha_, _artilheria_ → _artilharia_). Ficam as que mudam o número de sílabas do decassílabo: _inda_, _mui_, _exprimentada_, _galopear_, _até li_ (até ali) e as contrações de «com» com o artigo (_co'o_, _co'a_, _co'os_, _co'as_). Os nomes ficam na forma do autor (_Cepé_, _Gerardo_, _Catâneo_), com a grafia de hoje (_Lindoia_, _Cobé_). A pontuação é a de 1769.

**Notas.** As notas do autor, que na 1ª edição estão no pé das páginas, vêm no fim de cada canto, cada uma com as palavras do verso a que se refere. As citações em latim e em francês ficam como no impresso.

**Divisão.** Cinco cantos, com o número do verso à margem de dez em dez.`,
    fontes: [
      {"nome": "O Uraguay, 1ª edição, 1769, exemplar da Boston Public Library (Internet Archive)", "url": "https://archive.org/details/ouruaguaypoema00gama", "nota": "fac-símile; texto-base"},
      {"nome": "O Uraguay, 1ª edição, 1769, exemplar da Biblioteca Fisher, Universidade de Toronto (Internet Archive)", "url": "https://archive.org/details/ouraguaypoema00gama", "nota": "fac-símile; segundo exemplar, para as passagens gastas ou manchadas"},
      {"nome": "Wikisource, O Uraguay (transcrição da 1ª edição)", "url": "https://pt.wikisource.org/wiki/O_Uraguay", "nota": "revisada em parte; conferida palavra por palavra"},
      {"nome": "Wikisource, O Uraguai (grafia atualizada)", "url": "https://pt.wikisource.org/wiki/O_Uraguai", "nota": "base da grafia de hoje; corrigida pela 1ª edição"}
    ],
    erros: [
      {"cap": "V, nota «As brancas velas»", "de": "a virtude ao todo O Author", "para": "a virtude ao todo. O Autor"}
    ],
    mantidas: [
      {"cap": "I, 56", "texto": "Porque visse o espanhol em campo largo", "variante": "Por que"},
      {"cap": "I, 73", "texto": "Fonte de crimes, militar tesouro,", "variante": "- Fontes de crimes - militar tesouro,"},
      {"cap": "I, 85", "texto": "Quem é este, Catâneo perguntava,", "variante": "Que"},
      {"cap": "I, 89", "texto": "Gerardo, que os conhece, lhe responde:", "variante": "Geraldo"},
      {"cap": "I, 110", "texto": "Ninfas do mar, que vistes, se é que vistes,", "variante": "amor"},
      {"cap": "I, 121", "texto": "Honra da Toga, e glória do Senado.", "variante": "de"},
      {"cap": "II, 70", "texto": "Porém não pode dar-lhe os nossos povos.", "variante": "dar-lhes"},
      {"cap": "II, 89", "texto": "Nem altas minas, nem os caudalosos", "variante": "Nem altas minas, nem caudalosos"},
      {"cap": "II, depois de 89", "texto": "(nada)", "variante": "duas linhas da nota a «Aqui não temos» entre os versos"},
      {"cap": "II, 99", "texto": "Pobres choupanas, e algodões tecidos,", "variante": "Podres"},
      {"cap": "II, 109", "texto": "O teu está mui longe; e nós os índios", "variante": "muito"},
      {"cap": "II, 191", "texto": "Que tendes livre o passo. Assim dizendo,", "variante": "livres"},
      {"cap": "II, 210", "texto": "Entre nuvens de pó no ardor da guerra.", "variante": "pós"},
      {"cap": "II, 230", "texto": "Se do terreno os bárbaros nasciam.", "variante": "o"},
      {"cap": "II, 236", "texto": "Mil vezes, e mil vezes solta o arco", "variante": "sota"},
      {"cap": "II, 305", "texto": "Por seu braço ele só pôr termo à guerra.", "variante": "ermo"},
      {"cap": "II, 311", "texto": "Mostrava descoberto o rosto, e o peito,", "variante": "Mostrava descoberto o peito e o rosto"},
      {"cap": "II, 315", "texto": "Quantas setas da mão voar fazia,", "variante": "na"},
      {"cap": "II, 318", "texto": "Para dar outra vez princípio à guerra.", "variante": "Para dar outra vez princípio"},
      {"cap": "IV, 34", "texto": "Purpúreo encosto do dourado assento,", "variante": "de"},
      {"cap": "IV, depois de 56", "texto": "(nada)", "variante": "«O bom padre. Balda.», a nota, entre os versos"},
      {"cap": "IV, 81", "texto": "Vão com ele os seus tapes, que se afrontam,", "variante": "eles"},
      {"cap": "IV, 82", "texto": "E que têm por injúria morrer velhos.", "variante": "É"},
      {"cap": "IV, 202", "texto": "Quanto pode o temor! Secou-se a um tempo", "variante": "Quando"},
      {"cap": "IV, 220", "texto": "Dizem que Tanajura lhe pintara", "variante": "lhes"},
      {"cap": "V, 20", "texto": "Seus tortos sulcos o luzente arado", "variante": "sucos"},
      {"cap": "V, 72", "texto": "Todos os grandes, e a famosa fala.", "variante": "sala"},
      {"cap": "V, 97", "texto": "Em si revolve o General famoso.", "variante": "resolve"},
      {"cap": "V, 120", "texto": "Pendem-lhe dos arções de um lado, e de outro", "variante": "Pendem-se"}
    ]
  },
  partes: [
    { n: "", titulo: "Dedicatória", texto: `_Dedicado ao Ilustríssimo e Excelentíssimo Senhor Francisco Xavier de Mendonça Furtado, Secretário de Estado de S. Majestade Fidelíssima, &c. &c. &c._

| _At specus, & Caci detecta apparuit ingens_
| _Regia, & umbrosae penitus patuere cavernae._

Virg. _Æneid._ Lib. VIII.

## Ao Ilustríssimo e Excelentíssimo Senhor Conde de Oeiras

## Soneto

| Ergue de jaspe um globo alvo, e rotundo,
| E em cima a estátua de um Herói perfeito;
| Mas não lhe lavres nome em campo estreito,
| Que o seu nome enche a terra, e o mar profundo.

| Mostra no jaspe, Artífice facundo,
| Em muda história tanto ilustre feito,
| Paz, Justiça, Abundância, e firme peito,
| Isto nos basta a nós, e ao nosso Mundo.

| Mas porque pode em século futuro,
| Peregrino, que o mar de nós afasta,
| Duvidar quem anima o jaspe duro,

| Mostra-lhe mais Lisboa rica, e vasta,
| E o Comércio, e em lugar remoto, e escuro,
| Chorando a Hipocrisia. Isto lhe basta.

Do Autor.

| - - - - - _saevis_ - - - - _periclis_
| _Servati facimus._

Virg. _Æn._ VIII.` },
    { n: 1, titulo: "Canto Primeiro", texto: `| Fumam ainda nas desertas praias
| Lagos de sangue tépidos, e impuros,
| Em que ondeiam cadáveres despidos,
| Pasto de corvos. Dura inda nos vales
| O rouco som da irada artilharia.
| Musa, honremos o Herói, que o povo rude
| Subjugou do Uraguai, e no seu sangue
| Dos decretos reais lavou a afronta.
| Ai tanto custas, ambição de império!
| {v 10} E Vós, por quem o Maranhão pendura
| Rotas cadeias, e grilhões pesados,
| Herói, e irmão de heróis, saudosa, e triste,
| Se ao longe a vossa América vos lembra,
| Protegei os meus versos. Possa entanto
| Acostumar ao voo as novas asas,
| Em que um dia vos leve. Desta sorte
| Medrosa deixa o ninho a vez primeira
| Águia, que depois foge à humilde terra
| E vai ver de mais perto no ar vazio
| {v 20} O espaço azul, onde não chega o raio.
| Já dos olhos o véu tinha rasgado
| A enganada Madri, e ao Novo Mundo
| Da vontade do Rei núncio severo
| Aportava Catâneo: e ao grande Andrade
| Avisa que tem prontos os socorros,
| E que em breve saía ao campo armado.
| Não podia marchar por um deserto
| O nosso General, sem que chegassem
| As conduções, que há muito tempo espera.
| {v 30} Já por dilatadíssimos caminhos
| Tinha mandado de remotas partes
| Conduzir os petrechos para a guerra.
| Mas entretanto cuidadoso, e triste
| Muitas coisas a um tempo revolvia
| No inquieto agitado pensamento.
| Quando pelos seus guardas conduzido
| Um índio, com insígnias de correio,
| Com cerimônia estranha lhe apresenta
| Humilde as cartas, que primeiro toca
| {v 40} Levemente na boca, e na cabeça.
| Conhece a fiel mão, e já descansa
| O ilustre General, que viu, rasgando,
| Que na cera encarnada impressa vinha
| A águia real do generoso Almeida.
| Diz-lhe, que está vizinho, e traz consigo
| Prontos para o caminho, e para a guerra
| Os fogosos cavalos, e os robustos,
| E tardos bois, que hão de sofrer o jugo
| No pesado exercício das carretas.
| {v 50} Não tem mais que esperar, e sem demora
| Responde ao castelhano, que partia,
| E lhe determinou lugar, e tempo
| Para unir os socorros ao seu campo.
| Juntos enfim, e um corpo do outro à vista,
| Fez desfilar as tropas pelo plano,
| Porque visse o espanhol em campo largo
| A nobre gente, e as armas, que trazia.
| Vão passando as esquadras: ele entanto
| Tudo nota de parte, e tudo observa
| {v 60} Encostado ao bastão. Ligeira, e leve
| Passou primeiro a guarda, que na guerra
| É primeira a marchar, e que a seu cargo
| Tem descobrir, e segurar o campo.
| Depois desta se segue a que descreve,
| E dá ao campo a ordem, e a figura,
| E transporta, e edifica em um momento
| O leve teto, e as movediças casas,
| E a praça, e as ruas da cidade errante.
| Atrás dos forçosíssimos cavalos
| {v 70} Quentes sonoros eixos vão gemendo
| Co'o peso da funesta artilharia.
| Vinha logo de guardas rodeado,
| Fonte de crimes, militar tesouro,
| Por quem deixa no rego o curvo arado
| O lavrador, que não conhece a glória;
| E vendendo a vil preço o sangue, e a vida,
| Move, e nem sabe por que move a guerra.
| Intrépidos, e imóveis nas fileiras,
| Com grandes passos, firme a testa, e os olhos
| {v 80} Vão marchando os mitrados granadeiros,
| Sobre ligeiras rodas conduzindo
| Novas espécies de fundidos bronzes,
| Que amiúdam de prontas mãos servidos,
| E multiplicam pelo campo a morte.
| Quem é este, Catâneo perguntava,
| Das brancas plumas, e de azul, e branco
| Vestido, e de galões coberto, e cheio,
| Que traz a rica cruz no largo peito?
| Gerardo, que os conhece, lhe responde:
| {v 90} É o ilustre Meneses, mais que todos
| Forte de braço, e forte de conselho.
| Toda essa guerreira infantaria,
| A flor da mocidade, e da nobreza,
| Como ele, azul, e branco, e ouro vestem.
| Quem é, continuava o castelhano,
| Aquele velho vigoroso, e forte,
| Que de branco, e amarelo, e de ouro ornado
| Vem os seus artilheiros conduzindo?
| Vês o grande Alpoim. Este o primeiro
| {v 100} Ensinou entre nós, por que caminho
| Se eleva aos céus a curva, e grave bomba
| Prenhe de fogo: e com que força do alto
| Abate os tetos da cidade, e lança
| Do roto seio envolta em fumo a morte.
| Seguiam juntos o paterno exemplo
| Dignos do grande pai ambos os filhos.
| Justos céus! E é forçoso, ilustre Vasco,
| Que te preparem as soberbas ondas,
| Longe de mim, a morte, e a sepultura?
| {v 110} Ninfas do mar, que vistes, se é que vistes,
| O rosto esmorecido, e os frios braços,
| Sobre os olhos soltai as verdes tranças.
| Triste objeto de mágoa, e de saudade,
| Como em meu coração, vive em meus versos.
| Com os teus encarnados granadeiros
| Também te viu naquele dia o campo,
| Famoso Mascarenhas, tu, que agora
| Em doce paz, nos menos firmes anos,
| Igualmente servindo ao rei, e à pátria,
| {v 120} Ditas as leis ao público sossego,
| Honra da Toga, e glória do Senado.
| Nem tu, Castro fortíssimo, escolheste
| O descanso da pátria: o campo, e as armas
| Fizeram renovar no ínclito peito
| Todo o heroico valor dos teus passados.
| Os últimos, que em campo se mostraram,
| Foram fortes dragões de duros peitos,
| Prontos para dois gêneros de guerra,
| Que pelejam a pé sobre as montanhas,
| {v 130} Quando o pede o terreno; e quando o pede,
| Erguem nuvens de pó por todo o campo
| Co'o tropel dos magnânimos cavalos.
| Convida o General depois da mostra,
| Pago da militar guerreira imagem
| Os seus, e os espanhóis, e já recebe
| No pavilhão purpúreo, em largo giro,
| Os capitães a alegre, e rica mesa.
| Desterram-se os cuidados, derramando
| Os vinhos europeus nas taças de ouro.
| {v 140} Ao som da ebúrnea cítara sonora
| Arrebatado de furor divino
| Do seu herói Matúsio celebrava
| Altas empresas dignas de memória.
| Honras futuras lhe promete, e canta
| Os seus brasões, e sobre o forte escudo
| Já de então lhe afigura, e lhe descreve
| As pérolas, e o título de Grande.
| Levantadas as mesas, entretinham
| O congresso de heróis discursos vários.
| {v 150} Ali Catâneo ao General pedia,
| Que do princípio lhe dissesse as causas
| Da nova guerra, e do fatal tumulto.
| Se aos Padres seguem os rebeldes povos?
| Quem os governa em paz, e na peleja?
| Que do premeditado oculto Império
| Vagamente na Europa se falava.
| Nos seus lugares cada qual imóvel
| Pende da sua boca: atende em roda
| Tudo em silêncio, e dá princípio Andrade.
| {v 160} O nosso último rei, e o rei de Espanha
| Determinaram, por cortar de um golpe,
| Como sabeis, neste ângulo da terra,
| As desordens de povos confinantes,
| Que mais certos sinais nos dividissem.
| Tirando a linha, de onde a estéril costa,
| E o cerro de Castilhos o mar lava
| Ao monte mais vizinho, e que as vertentes
| Os termos do domínio assinalassem.
| Vossa fica a Colônia, e ficam nossos
| {v 170} Sete povos, que os Bárbaros habitam
| Naquela oriental vasta campina,
| Que o fértil Uraguai discorre, e banha.
| Quem podia esperar que uns índios rudes,
| Sem disciplina, sem valor, sem armas,
| Se atravessassem no caminho aos nossos,
| E que lhes disputassem o terreno!
| Enfim não lhes dei ordens para a guerra:
| Frustrada a expedição, enfim voltaram.
| Co'o vosso general me determino
| {v 180} A entrar no campo juntos, em chegando
| A doce volta da estação das flores.
| Não sofrem tanto os índios atrevidos:
| Juntos um nosso forte entanto assaltam:
| E os padres os incitam, e acompanham.
| Que, à sua discrição, só eles podem
| Aqui mover, ou sossegar a guerra.
| Os índios, que ficaram prisioneiros,
| Ainda os podeis ver neste meu campo.
| Deixados os quartéis, enfim partimos
| {v 190} Por diversas estradas, procurando
| Tomar no meio os rebelados povos.
| Por muitas léguas de áspero caminho,
| Por lagos, bosques, vales, e montanhas,
| Chegamos onde nos impede o passo
| Arrebatado, e caudaloso rio.
| Por toda a oposta margem se descobre
| De bárbaros o número infinito,
| Que ao longe nos insulta, e nos espera.
| Preparo curvas balsas, e pelotas,
| {v 200} E em uma parte de passar aceno,
| Enquanto em outra passo oculto as tropas.
| Quase tocava o fim da empresa, quando
| Do vosso general um mensageiro
| Me afirma, que se havia retirado.
| A disciplina militar dos índios
| Tinha esterilizado aqueles campos.
| Que eu também me retire me aconselha,
| Até que o tempo mostre outro caminho.
| Irado, não o nego, lhe respondo:
| {v 210} Que para trás não sei mover um passo.
| Venha quando puder, que eu firme o espero.
| Porém o rio, e a forma do terreno
| Nos faz não vista, e nunca usada guerra.
| Sai furioso do seu seio, e toda
| Vai alagando com o desmedido
| Peso das águas a planície imensa.
| As tendas levantei, primeiro aos troncos,
| Depois aos altos ramos: pouco a pouco
| Fomos tomar na região do vento
| {v 220} A habitação aos leves passarinhos.
| Tece o emaranhadíssimo arvoredo
| Verdes, irregulares, e torcidas
| Ruas, e praças de uma, e de outra banda
| Cruzadas de canoas. Tais podemos
| Co'a mistura das luzes, e das sombras
| Ver por meio de um vidro transplantados
| Ao seio de Ádria os nobres edifícios,
| E os jardins, que produz outro elemento.
| E batidas do remo, e navegáveis
| {v 230} As ruas da marítima Veneza.
| Duas vezes a lua prateada
| Curvou no céu sereno os alvos cornos,
| E inda continuava a grossa enchente.
| Tudo nos falta no país deserto.
| Tardar devia o espanhol socorro.
| E de si nos lançava o rio, e o tempo.
| Cedi, e retirei-me às nossas terras.
| Deu fim à narração o invicto Andrade,
| E antes de se soltar o ajuntamento,
| {v 240} Com os régios poderes, que ocultara,
| Surpreende os seus, e os ânimos alegra,
| Enchendo os postos todos do seu campo.
| O corpo de dragões a Almeida entrega,
| E Campo das Mercês o lugar chama.

¤ _E Vós._ O Ilustríssimo, e Excelentíssimo Senhor Francisco Xavier de Mendonça Furtado foi Governador, e Capitão General das Capitanias do Grão Pará, e Maranhão; e fez ao Norte do Brasil o que o Conde de Bobadela fez da parte do Sul: encontrou nos jesuítas a mesma resistência, e venceu-a da mesma sorte.

¤ _Rotas cadeias._ Os índios lhe devem inteiramente a sua liberdade. Os jesuítas nunca declamaram contra o cativeiro destes miseráveis racionais, senão porque pretendiam ser só eles os seus Senhores. Ultimamente foram, nos nossos dias, nobilitados, e admitidos aos cargos da República. Este procedimento honra a humanidade.

¤ _Irmão de Heróis._ Em uma só Família achou o Rei três Irmãos dignos de repartirem entre si todo o peso do Governo. Com quanto maior glória nossa podem os estranhos dizer da Corte de Lisboa, o que já se disse de Roma, ao vê-la nas mãos dos três famosos Horácios, _Corneil. Horac._:

¤ | _E son illustre ardeur d' oser plus que les autres_
| _D' une seule maison brave toutes les notres._
| _Ce choix pouvoit combler trois familles de gloire._

¤ _A enganada Madri._ Os jesuítas por si, e pelos seus fautores tinham feito na Corte de Madri o último esforço para impedir a execução do Tratado de Limites.

¤ _Andrade._ O Ilustríssimo, e Excelentíssimo Senhor Gomes Freire de Andrade.

¤ _Almeida._ O Coronel José Inácio de Almeida.

¤ _Lugar, e tempo._ O dia 16 de janeiro de 1756 em Santo Antônio o Velho.

¤ _Novas espécies._ As Companhias de Granadeiros levaram a esta expedição peças de amiudar, que foram as primeiras, que passaram ao Brasil.

¤ _Meneses._ O Coronel Francisco Antônio Cardoso de Meneses, hoje Governador da Colônia.

¤ _Alpoim._ O Brigadeiro.

¤ _Vasco_ Fernandes Pinto Alpoim, filho do Brigadeiro, e particular amigo do Autor, morreu Tenente-Coronel na flor dos seus anos em uma embarcação, que se perdeu, vindo da Colônia para o Rio de Janeiro.

¤ _Mascarenhas._ Fernando Mascarenhas, Capitão de Granadeiros, depois Sargento-mor, atualmente serve no Senado.

¤ _Castro._ O Tenente-Coronel Gregório de Castro Morais de ilustríssima Família, que teve o governo do Rio de Janeiro no tempo da invasão do famoso Du Guay Trouin.

¤ _Vagamente._ Os jesuítas têm tido a animosidade de negar por toda Europa o que se acabou de passar na América nos nossos dias à vista de dois Exércitos. O Autor o experimentou em Roma, onde muitas pessoas o buscavam só para saberem com fundamento as notícias do Uraguai; testemunhando um estranho contentamento de encontrarem um americano, que os podia informar miudamente de tudo o sucedido. A admiração, que causava a estranheza de fatos entre nós tão conhecidos, fez nascer as primeiras ideias deste Poema.

¤ _Mais certos sinais._ O Tratado de Limites das Conquistas celebrou-se a 16 de janeiro de 1750 entre os Senhores Reis D. João o V de Portugal, e D. Fernando o VI de Espanha. Este Tratado feria os jesuítas na alma, porque por elle se entregavam aos portugueses as terras, que a Companhia depois de muito tempo possuía como suas da parte Oriental do Rio Uraguai.

¤ _Sem disciplina._ Como naquele tempo se imaginava.

¤ _Lhes disputassem._ Os Oficiais Militares, que foram fazer a demarcação, chegaram ao posto de Santa Tecla, e nele acharam fortificados os índios, que lhes impediram os passos.

¤ _Prisioneiros._ Foram cinquenta estes prisioneiros; alguns dos principais vieram remetidos ao Rio de Janeiro, onde o Autor os viu, e falou com eles. Confessavam ingenuamente, que os Padres tinham vindo em sua companhia até o Rio Pardo, e se tinham deixado ficar da outra banda. Mostravam-se surpreendidos da doçura, que encontravam no trato dos portugueses. Diziam que os Padres não cessavam de lhes intimar nas suas pregações, que os portugueses tinham o diabo no corpo, e que eram todos feiticeiros. Que em matando algum, para que não tornasse a viver, era necessário pôr-lhe a cabeça um palmo longe do corpo; o que eles religiosamente observavam.

¤ _Partimos._ Saiu o General português do Rio Grande de S. Pedro a 28 de julho de 1754.

¤ _Caudaloso rio._ Jacuí. Chegaram a elle aos 7 de setembro.

¤ _Balsas, e pelotas._ Espécie de barcos, em que os nossos passam naquele país os maiores, e mais profundos rios. Fazem-se de couros de boi. Levam no fundo as cargas, e em cima os homens com os cavalos nadando à mão. Os índios, que são robustíssimos, e grandes nadadores, tiram toda esta máquina por uma corda, cuja ponta tomam nos dentes. Quem vai dentro leva na mão a outra ponta, largando-a mais, ou menos, conforme julga ser necessário.

¤ _Se havia retirado._ Retiraram-se as Tropas Castelhanas, enfraquecida a Cavalaria. Tinham-se metido muito pela margem do rio, que estava rapada dos gados Jesuíticos. Finalmente não tinham vontade de entrar em Missões; nem até então estavam inteiramente persuadidos da intenção do Rei. A maior razão de duvidar nascia das cartas, que vinham da Corte de Madri por uma oculta cabala; os jesuítas tudo revolviam, e maquinavam mais que nunca.

¤ _Forma do terreno._ Todos aqueles bosques, e várzeas por muitas, e muitas léguas são alagadiços, e sujeitos a estas enchentes. Há Nações inteiras de índios, que fazem as suas choupanas, e vivem sobre as árvores. São destríssimos em subir, e descer sem cordas, nem gênero algum de escada. As árvores são altíssimas, e têm a maior parte do ano as raízes na água.

¤ _As tendas._ Talvez não se achará na História outro sucesso semelhante. Foi necessária toda a constância do Conde de Bobadela para ter dois meses um Exército abarracado sobre as árvores.

¤ _Canoas._ Pequenas embarcações dos índios feitas de um só tronco: nelas vinham ocultamente fazer comércio com os portugueses, e espanhóis.

¤ Tardar devia. _Post bellum auxilium._` },
    { n: 2, titulo: "Canto Segundo", texto: `| Depois de haver marchado muitos dias,
| Enfim junto a um ribeiro, que atravessa
| Sereno, e manso um curvo, e fresco vale,
| Acharam, os que o campo descobriram,
| Um cavalo anelante, e o peito, e as ancas
| Coberto de suor, e branca escuma.
| Temos perto o inimigo: aos seus dizia
| O esperto General: Sei que costumam
| Trazer os índios um volúvel laço,
| {v 10} Com o qual tomam no espaçoso campo
| Os cavalos, que encontram; e rendidos
| Aqui, e ali com o continuado
| Galopear, a quem primeiro os segue
| Deixam os seus, que entanto se restauram.
| Nem se enganou; porque ao terceiro dia
| Formados os achou sobre uma larga
| Vantajosa colina, que de um lado
| É coberta de um bosque, e do outro lado
| Corre escarpada, e sobranceira a um rio.
| {v 20} Notava o General o sítio forte,
| Quando Meneses, que vizinho estava,
| Lhe diz: Nestes desertos encontramos
| Mais do que se esperava, e me parece
| Que só por força de armas poderemos
| Inteiramente sujeitar os povos.
| Torna-lhe o General: Tentem-se os meios
| De brandura, e de amor; se isto não basta,
| Farei a meu pesar o último esforço.
| Mandou, dizendo assim, que os índios todos,
| {v 30} Que tinha prisioneiros no seu campo,
| Fossem vestidos das formosas cores,
| Que a inculta gente simples tanto adora.
| Abraçou-os a todos, como filhos,
| E deu a todos liberdade. Alegres
| Vão buscar os parentes, e os amigos,
| E a uns, e a outros contam a grandeza
| Do excelso coração, e peito nobre
| Do General famoso, invicto Andrade.
| Já para o nosso campo vêm descendo,
| {v 40} Por mandado dos seus, dois dos mais nobres,
| Sem arcos, sem aljavas; mas as testas
| De várias, e altas penas coroadas,
| E cercadas de penas as cinturas,
| E os pés, e os braços, e o pescoço. Entrara
| Sem mostras, nem sinal de cortesia,
| Cepé no pavilhão. Porém Cacambo
| Fez, ao seu modo, cortesia estranha,
| E começou: Ó General famoso,
| Tu tens à vista quanta gente bebe
| {v 50} Do soberbo Uraguai a esquerda margem.
| Bem que os nossos avôs fossem despojo
| Da perfídia de Europa, e daqui mesmo
| Co'os não vingados ossos dos parentes
| Se vejam branquejar ao longe os vales,
| Eu desarmado, e só buscar-te venho.
| Tanto espero de ti. E enquanto as armas
| Dão lugar à razão, senhor, vejamos
| Se se pode salvar a vida, e o sangue
| De tantos desgraçados. Muito tempo
| {v 60} Pode ainda tardar-nos o recurso
| Com o largo oceano de permeio,
| Em que os suspiros dos vexados povos
| Perdem o alento. O dilatar-se a entrega
| Está nas nossas mãos, até que um dia
| Informados os reis nos restituam
| A doce antiga paz. Se o rei de Espanha
| Ao teu rei quer dar terras com mão larga,
| Que lhe dê Buenos Aires, e Correntes,
| E outras, que tem por estes vastos climas;
| {v 70} Porém não pode dar-lhe os nossos povos.
| E inda no caso que pudesse dá-los,
| Eu não sei se o teu rei sabe o que troca;
| Porém tenho receio que o não saiba.
| Eu já vi a Colônia portuguesa
| Na tenra idade dos primeiros anos,
| Quando o meu velho pai co'os nossos arcos
| Às sitiadoras tropas castelhanas
| Deu socorro, e mediu convosco as armas.
| E quererão deixar os portugueses
| {v 80} A praça, que avassala, e que domina
| O gigante das águas, e com ela
| Toda a navegação do largo rio,
| Que parece que pôs a natureza
| Para servir-vos de limite, e raia?
| Será; mas não o creio. E depois disto,
| As campinas, que vês, e a nossa terra,
| Sem o nosso suor, e os nossos braços,
| De que serve ao teu rei? Aqui não temos
| Nem altas minas, nem os caudalosos
| {v 90} Rios de areias de ouro. Essa riqueza,
| Que cobre os templos dos benditos padres,
| Fruto da sua indústria, e do comércio
| Da folha, e peles, é riqueza sua.
| Com o arbítrio dos corpos, e das almas
| O céu lha deu em sorte. A nós somente
| Nos toca arar, e cultivar a terra,
| Sem outra paga mais que o repartido
| Por mãos escassas mísero sustento.
| Pobres choupanas, e algodões tecidos,
| {v 100} E o arco, e as setas, e as vistosas penas
| São as nossas fantásticas riquezas.
| Muito suor, e pouco, ou nenhum fasto.
| Volta, senhor, não passes adiante.
| Que mais queres de nós? Não nos obrigues
| A resistir-te em campo aberto. Pode
| Custar-te muito sangue o dar um passo.
| Não queiras ver se cortam nossas flechas.
| Vê que o nome dos reis não nos assusta.
| O teu está mui longe; e nós os índios
| {v 110} Não temos outro rei mais do que os padres.
| Acabou de falar; e assim responde
| O ilustre General: Ó alma grande,
| Digna de combater por melhor causa,
| Vê que te enganam: risca da memória
| Vãs, funestas imagens, que alimentam
| Envelhecidos mal fundados ódios.
| Por mim te fala o rei: ouve-me, atende,
| E verás uma vez nua a verdade.
| Fez-vos livres o céu; mas se o ser livres
| {v 120} Era viver errantes, e dispersos,
| Sem companheiros, sem amigos, sempre
| Com as armas na mão em dura guerra,
| Ter por justiça a força, e pelos bosques
| Viver do acaso, eu julgo que inda fora
| Melhor a escravidão, que a liberdade.
| Mas nem a escravidão, nem a miséria
| Quer o benigno rei que o fruto seja
| Da sua proteção. Esse absoluto
| Império ilimitado, que exercitam
| {v 130} Em vós os padres, como vós, vassalos,
| É império tirânico, que usurpam.
| Nem são senhores, nem vós sois escravos.
| O rei é vosso pai: quer-vos felizes.
| Sois livres, como eu sou; e sereis livres,
| Não sendo aqui, em outra qualquer parte.
| Mas deveis entregar-nos estas terras.
| Ao bem público cede o bem privado.
| O sossego de Europa assim o pede.
| Assim o manda o rei. Vós sois rebeldes,
| {v 140} Se não obedeceis; mas os rebeldes,
| Eu sei que não sois vós; são os bons padres,
| Que vos dizem a todos, que sois livres,
| E se servem de vós, como de escravos.
| Armados de orações vos põem no campo
| Contra o fero trovão da artilharia,
| Que os muros arrebata, e se contentam
| De ver de longe a guerra: sacrificam
| Avarentos do seu o vosso sangue.
| Eu quero à vossa vista despojá-los
| {v 150} Do tirano domínio destes climas,
| De que a vossa inocência os fez senhores.
| Dizem-vos que não tendes rei? Cacique,
| E o juramento de fidelidade?
| Porque está longe, julgas que não pode
| Castigar-vos a vós, e castigá-los?
| Generoso inimigo, é tudo engano.
| Os reis estão na Europa; mas adverte
| Que estes braços que vês, são os seus braços.
| Dentro de pouco tempo um meu aceno
| {v 160} Vai cobrir este monte, e essas campinas
| De semivivos palpitantes corpos
| De míseros mortais, que inda não sabem
| Por que causa o seu sangue vai agora
| Lavar a terra, e recolher-se em lagos.
| Não me chames cruel: enquanto é tempo
| Pensa, e resolve; e pela mão tomando
| Ao nobre embaixador o ilustre Andrade,
| Intenta reduzi-lo por brandura.
| E o índio, um pouco pensativo, o braço,
| {v 170} E a mão retira; e suspirando, disse:
| Gentes de Europa, nunca vos trouxera
| O mar, e o vento a nós. Ah! não debalde
| Estendeu entre nós a natureza
| Todo esse plano espaço imenso de águas.
| Prosseguia talvez; mas o interrompe
| Cepé, que entra no meio, e diz: Cacambo
| Fez mais do que devia; e todos sabem
| Que estas terras, que pisas, o céu livres
| Deu aos nossos avôs; nós também livres
| {v 180} As recebemos dos antepassados.
| Livres as hão de herdar os nossos filhos.
| Desconhecemos, detestamos jugo,
| Que não seja o do céu, por mão dos padres.
| As flechas partirão nossas contendas
| Dentro de pouco tempo; e o vosso Mundo,
| Se nele um resto houver de humanidade,
| Julgará entre nós; se defendemos
| Tu a injustiça, e nós o Deus, e a Pátria.
| Enfim quereis a guerra, e tereis guerra,
| {v 190} Lhe torna o General: Podeis partir-vos,
| Que tendes livre o passo. Assim dizendo,
| Manda dar a Cacambo rica espada
| De tortas guarnições de prata, e ouro,
| A que inda mais valor dera o trabalho.
| Um bordado chapéu, e larga cinta
| Verde, e capa de verde, e fino pano,
| Com bandas amarelas, e encarnadas.
| E mandou que a Cepé se desse um arco
| De pontas de marfim: e ornada, e cheia
| {v 200} De novas setas a famosa aljava:
| A mesma aljava, que deixara um dia,
| Quando envolto em seu sangue, e vivo apenas,
| Sem arco, e sem cavalo, foi trazido
| Prisioneiro de guerra ao nosso campo.
| Lembrou-se o índio da passada injúria,
| E sobraçando a conhecida aljava,
| Lhe disse: Ó General, eu te agradeço
| As setas, que me dás, e te prometo
| Mandar-tas bem depressa uma por uma
| {v 210} Entre nuvens de pó no ardor da guerra.
| Tu as conhecerás pelas feridas,
| Ou porque rompem com mais força os ares.
| Despediram-se os índios, e as esquadras
| Se vão dispondo em ordem de peleja,
| Como mandava o General. Os lados
| Cobrem as tropas de cavalaria,
| E estão no centro firmes os infantes.
| Qual fera boca de libréu raivoso
| De lisos, e alvos dentes guarnecida,
| {v 220} Os índios ameaça a nossa frente
| De agudas baionetas rodeada.
| Fez a trombeta o som da guerra. Ouviram
| Aqueles montes pela vez primeira
| O som da caixa portuguesa; e viram
| Pela primeira vez aqueles ares
| Desenroladas as reais bandeiras.
| Saem das grutas pelo chão cavadas,
| Em que até li de indústria se escondiam,
| Nuvens de índios, e a vista duvidava
| {v 230} Se do terreno os bárbaros nasciam.
| Qual já no tempo antigo o errante Cadmo
| Dizem que vira da fecunda terra
| Brotar a cruelíssima seara.
| Erguem todos um bárbaro alarido,
| E sobre os nossos cada qual encurva
| Mil vezes, e mil vezes solta o arco
| Um chuveiro de setas despedindo.
| Gentil mancebo presumido, e néscio,
| A quem a popular lisonja engana,
| {v 240} Vaidoso pelo campo discorria,
| Fazendo ostentação dos seus penachos.
| Impertinente, e de família escura,
| Mas que tinha o favor dos santos padres.
| Contam, não sei se é certo, que o tivera
| A estéril mãe por orações de Balda.
| Chamaram-no Baldetta por memória.
| Tinha um cavalo de manchada pele
| Mais vistoso que forte: a natureza
| Um ameno jardim por todo o corpo
| {v 250} Lhe debuxou, e era Jardim chamado.
| O padre na saudosa despedida
| Deu-lho em sinal de amor; e nele agora
| Girando ao largo com incertos tiros
| Muitos feria, e a todos inquietava.
| Mas se então se cobriu de eterna infâmia,
| A glória tua foi, nobre Gerardo.
| Tornava o índio jactancioso, quando
| Lhe sai Gerardo ao meio da carreira:
| Disparou-lhe a pistola, e fez-lhe a um tempo
| {v 260} Co'o reflexo do sol luzir a espada.
| Só de vê-lo se assusta o índio, e fica
| Qual quem ouve o trovão, e espera o raio.
| Treme, e o cavalo aos seus volta, e pendente
| A um lado, e a outro de cair acena.
| Deixando aqui, e ali por todo o campo
| Entornadas as setas; pelas costas,
| Flutuavam as penas; e fugindo
| Soltas da mão as rédeas ondeavam.
| Insta Gerardo, e quase o ferro o alcança,
| {v 270} Quando Tatu-Guaçu, o mais valente
| De quantos índios viu a nossa idade,
| Armado o peito da escamosa pele
| De um jacaré disforme, que matara,
| Se atravessa diante. Intenta o nosso
| Com a outra pistola abrir caminho,
| E em vão o intenta: a verde-negra pele,
| Que ao índio o largo peito orna, e defende,
| Formou a natureza impenetrável.
| Co'a espada o fere no ombro, e na cabeça,
| {v 280} E as penas corta, de que o campo espalha.
| Separa os dois fortíssimos guerreiros
| A multidão dos nossos, que atropela
| Os índios fugitivos: tão depressa
| Cobrem o campo os mortos, e os feridos,
| E por nós a vitória se declara.
| Precipitadamente as armas deixam,
| Nem resistem mais tempo às espingardas.
| Vale-lhe a costumada ligeireza,
| Debaixo lhe desaparece a terra,
| {v 290} E voam, que o temor aos pés põe asas,
| Clamando ao céu, e encomendando a vida
| Às orações dos padres. Desta sorte,
| Talvez, em outro clima, quando soltam
| A branca neve eterna os velhos Alpes,
| Arrebata a corrente impetuosa
| Co'as choupanas o gado. Aflito, e triste
| Se salva o lavrador nos altos ramos,
| E vê levar-lhe a cheia os bois, e o arado.
| Poucos índios no campo mais famosos,
| {v 300} Servindo de reparo aos fugitivos,
| Sustentam todo o peso da batalha,
| Apesar da fortuna. De uma parte
| Tatu-Guaçu mais forte na desgraça
| Já banhado em seu sangue pretendia
| Por seu braço ele só pôr termo à guerra.
| Caitutu de outra parte altivo, forte
| Opunha o peito à fúria do inimigo,
| E servia de muro à sua gente.
| Fez proezas Cepé naquele dia.
| {v 310} Conhecido de todos, no perigo
| Mostrava descoberto o rosto, e o peito,
| Forçando os seus co'o exemplo, e co'as palavras.
| Já tinha despejado a aljava toda,
| E destro em atirar, e irado, e forte
| Quantas setas da mão voar fazia,
| Tantas na nossa gente ensanguentava.
| Setas de novo agora recebia,
| Para dar outra vez princípio à guerra.
| Quando o ilustre espanhol, que governava
| {v 320} Montevidio alegre, airoso, e pronto
| As rédeas volta ao rápido cavalo,
| E por cima de mortos, e feridos,
| Que lutavam co'a morte, o índio afronta.
| Cepé, que o viu, tinha tomado a lança,
| E atrás deitando a um tempo o corpo, e o braço,
| A despediu. Por entre o braço, e o corpo
| Ao ligeiro espanhol o ferro passa:
| Rompe, sem fazer dano, a terra dura,
| E treme fora muito tempo a hástea.
| {v 330} Mas de um golpe a Cepé na testa, e peito
| Fere o governador, e as rédeas corta
| Ao cavalo feroz. Foge o cavalo,
| E leva involuntário, e ardendo em ira
| Por todo o campo a seu senhor; e ou fosse
| Que regada de sangue aos pés cedia
| A terra, ou que pusesse as mãos em falso,
| Rodou sobre si mesmo, e na caída
| Lançou longe a Cepé. Rende-te, ou morre,
| Grita o governador; e o tape altivo,
| {v 340} Sem responder, encurva o arco, e a seta
| Despede, e nela lhe prepara a morte.
| Enganou-se esta vez. A seta um pouco
| Declina, e açouta o rosto a leve pluma.
| Não quis deixar o vencimento incerto
| Por mais tempo o espanhol, e arrebatado
| Com a pistola lhe fez tiro aos peitos.
| Era pequeno o espaço, e fez o tiro
| No corpo desarmado estrago horrendo.
| Viam-se dentro pelas rotas costas
| {v 350} Palpitar as entranhas. Quis três vezes
| Levantar-se do chão: caiu três vezes,
| E os olhos já nadando em fria morte
| Lhe cobriu sombra escura, e férreo sono.
| Morto o grande Cepé, já não resistem
| As tímidas esquadras. Não conhece
| Leis o temor. Debalde está diante,
| E anima os seus o rápido Cacambo.
| Tinha-se retirado da peleja
| Caitutu mal ferido; e do seu corpo
| {v 360} Deixa Tatu-Guaçu por onde passa
| Rios de sangue. Os outros mais valentes
| Ou eram mortos, ou feridos. Pende
| O ferro vencedor sobre os vencidos.
| Ao número, ao valor cede Cacambo:
| Salva os índios, que pode, e se retira.

¤ _Ao terceiro dia._ Aos 10 de fevereiro de 1756.

¤ _E começou._ Todos os Padres aprendiam a língua dos índios, e proibiam a estes, contra a intenção do Rei, usar de outra língua, que não fosse a sua nacional. Desta sorte ficava impossibilitada a comunicação com os portugueses, e castelhanos, e impenetrável o segredo do que se passava naqueles sertões. E o que é mais, é que os mesmos jesuítas se jactavam desta espécie de tirania na face de toda Europa:

¤ | _Nescia gens nostri vivit - - - - - - -_
| _- - - - - ad interiora venire_
| _Regna vetent homines cupidos audita videndi._

¤ Vanier. Praed. rust. Lib. XIV.

¤ Nossos Avôs. _Por estes portugueses se nos trazem a casa todos os presentes prejuízos. Lembrai-vos que nos tempos passados mataram a vossos defuntos Avôs. Mataram mais milhares deles por todas as partes, sem reservar as inocentes criaturas._ Instruções, &c.

¤ _Buscar-te venho._ Tinham positiva ordem dos Padres para o não fazerem. _Os que nos aborrecem,_ (por estas expressões caracterizavam os europeus) _quando nos pretendam falar, havemos de escusar sua conversação, fugindo muito da dos espanhóis, e muito mais dos portugueses .... Se acaso nos quiserem falar, hão de ser cinco castelhanos, nada mais. Não sejam portugueses; porque se viessem alguns dos portugueses, não lhes há de ir bem. O Padre, que é o dos índios, e sabe a sua língua, há de ser o que sirva de intérprete, e então se fará tudo, porque deste modo se fará tudo como Deus manda; e senão, irão as coisas por onde o Diabo quiser._ Instruções, &c.

¤ Tanto espero de ti. _Não queremos ir aonde vós estais, porque não temos confiança de vós-outros._ Instruções.

¤ _Aqui não temos._ Os Padres faziam crer aos índios que os portugueses eram gente sem lei, que adoravam o ouro.

¤ _Essa riqueza._ As suas riquezas eram imensas: as suas Casas, e os seus Templos magníficos, fora de quanto se pode imaginar em Europa. Nem é necessário ir tão longe: mesmo no Rio de Janeiro tinham os Padres, entre outras imensas terras, a fazenda de Santa Cruz; tão grande, que nenhuma daquelas opulentíssimas famílias se achou até hoje com fundo para comprá-la. Tinham só nesta mais de mil escravos. O gado era sem número. Com tudo isto, é coisa certa que se lhes não achou dinheiro de consideração no seu sequestro. Poucos dias depois de partirem daquele Porto se apresentou ao Conde de Bobadela um Leigo pedreiro, dizendo, que vinha descobrir o lugar, onde por ordem dos Padres tinha escondido o dinheiro. Com efeito já se não achou mais que o lugar nos alicerces da Igreja nova. Eles assim que viram que o Leigo despia a roupeta, fizeram-lhe uma ligeireza das suas.

¤ _Da folha, e peles._ Os índios, e os espanhóis fazem do _Mate_ o uso, que os chineses fazem do seu _The_. Este importantíssimo comércio era todo dos jesuítas do Paraguai. Cultivavam as árvores, que dão a tal folha, e fabricavam-na, e a faziam girar em surrões de pele por toda a América Espanhola. Só este negócio rendia em cada um ano muitos milhões. Tudo suor dos miseráveis índios.

¤ Riqueza sua. _Semina nos colimus faustis, quae jecimus agris,_

¤ Vanier. Praed. rust. Lib. XIV.

¤ Sem outra paga. - - - _proprium, qui nil potiuntur, & usu_

¤ | _Cuncta tenent_ - - - -

¤ Ibid.

¤ _Muito suor._ Também não é necessário ir ao Uraguai para ter provas do excessivo trabalho dos índios no serviço dos Padres. Entre a Vila de Santos, e a Cidade de S. Paulo há uma serra muito íngreme, e dilatada: não se pode subir a cavalo. O Conde de Bobadela, o melhor cavaleiro do seu tempo, caiu duas vezes logo à entrada, em cavalos, que tinha escolhido para isso entre muitos. Todos a sobem a pé com o seu cavalo pela mão. Os Padres como faziam voto de pobreza, contentavam-se de a subir, e descer recostados em redes às costas dos miseráveis índios; nem jamais passaram por ali de outra sorte. Este fato na Europa parece incrível; mas o Autor o atesta.

¤ _O nome dos Reis._ Estas expressões não são ornato da Poesia, passou na realidade tudo o que o Autor aqui faz dizer a este índio.

¤ Estas terras. _Estas terras no-las deu Deus, e a nossos Avôs, e por isso só as possuímos em amor de Deus._ Carta sediciosa, &c.

¤ _O do Céu._ Esta mistura do sagrado com o profano, ou para melhor dizer, aquele fazer servir a Religião aos seus fins particulares, foi sempre o caráter dos jesuítas. Considere-se atentamente este verso:

¤ | _Non gentem imperio, sed relligione tenemus._

¤ Vanier. sup.

¤ _Balda._ O P. Lourenço Balda foi uma das cabeças mais tenazes, e que mais animava os índios à rebelião.

¤ _Por memória._ Os jesuítas da América não eram tão escrupulosos como afetavam ser os da Europa. Era bem fácil distinguir nas Aldeãs as índias, que gozavam do favor dos Padres. Da mesma sorte se distinguiam muito bem, entre os outros, os rapazes da família. Na Ásia era o mesmo. Leia-se a Carta do Bispo de Nankim a Benedito XIV.

¤ Sinal de amor. - - - - - _quem cândida Dido_

¤ | _Esse sui dederat monumentum, & pignus amoris._

¤ Virg. Æn. Lib. V.

¤ _Tatu Guaçu._ _Guasú_ na língua dos índios quer dizer _grande._ Alguns índios mais soberbos ajuntam esta palavra ao seu nome, que fica soando desta sorte, entre eles, como soa, entre nós, Carlos Magno, Alexandre Magno, &c.

¤ _Jacaré._ Com este nome o traz Marcgr. Bras. 242. Veja-se Linae. System. Natur. Amphibia, Reptilia, Draco. 1.

¤ _Tão de pressa._ Ainda que os Padres tinham armado os índios, e feito quanto podiam para os disciplinar, contudo estavam bem longe de poder resistir às Tropas regulares. Era necessária muita crueldade para entregar aqueles miseráveis à morte só por ambição, e por capricho.` },
    { n: 3, titulo: "Canto Terceiro", texto: `| Já a nossa do mundo última Parte
| Tinha voltado a ensanguentada fronte
| Ao centro luminar; quando a campanha
| Semeada de mortos, e insepultos
| Viu desfazer-se a um tempo a vila errante
| Ao som das caixas. Descontente, e triste
| Marchava o General: não sofre o peito
| Compadecido, e generoso a vista
| Daqueles frios, e sangrados corpos,
| {v 10} Vítimas da ambição de injusto império.
| Foram ganhando, e descobrindo terra
| Inimiga, e infiel; até que um dia
| Fizeram alto, e se acamparam, onde
| Incultas várzeas, por espaço imenso,
| Enfadonhas, e estéreis acompanham
| Ambas as margens de um profundo rio.
| Todas estas vastíssimas campinas
| Cobrem palustres, e tecidas canas,
| E leves juncos do calor tostados,
| {v 20} Pronta matéria de voraz incêndio.
| O índio habitador de quando em quando
| Com estranha cultura entrega ao fogo
| Muitas léguas de campo: o incêndio dura,
| Enquanto dura, e o favorece o vento.
| Da erva, que renasce, se apascenta
| O imenso gado, que dos montes desce;
| E renovando incêndios desta sorte
| A Arte emenda a Natureza, e podem
| Ter sempre nédio o gado, e o campo verde.
| {v 30} Mas agora sabendo por espias
| As nossas marchas, conservavam sempre
| Secas as torradíssimas campinas,
| Nem consentiam, por fazer-nos guerra,
| Que a chama benfeitora, e a cinza fria
| Fertilizasse o árido terreno.
| O cavalo até li forte, e brioso,
| E costumado a não ter mais sustento,
| Naqueles climas, do que a verde relva
| Da mimosa campina, desfalece.
| {v 40} Nem mais, se o seu senhor o afaga, encurva
| Os pés, e cava o chão co'as mãos, e o vale
| Rinchando atroa, e açouta o ar co'as crinas.
| Era alta noite, e carrancudo, e triste
| Negava o céu envolto em pobre manto
| A luz ao mundo, e murmurar se ouvia
| Ao longe o rio, e menear-se o vento.
| Respirava descanso a natureza.
| Só na outra margem não podia entanto
| O inquieto Cacambo achar sossego.
| {v 50} No perturbado interrompido sono,
| Talvez fosse ilusão, se lhe apresenta
| A triste imagem de Cepé despido,
| Pintado o rosto do temor da morte,
| Banhado em negro sangue, que corria
| Do peito aberto, e nos pisados braços
| Inda os sinais da mísera caída.
| Sem adorno a cabeça, e aos pés calcada
| A rota aljava, e as descompostas penas.
| Quanto diverso do Cepé valente,
| {v 60} Que no meio dos nossos espalhava,
| De pó, de sangue, e de suor coberto,
| O espanto, a morte! E diz-lhe em tristes vozes:
| Foge, foge, Cacambo. E tu descansas,
| Tendo tão perto os inimigos? Torna,
| Torna aos teus bosques, e nas pátrias grutas
| Tua fraqueza, e desventura encobre.
| Ou se acaso inda vivem no teu peito
| Os desejos de glória, ao duro passo
| Resiste valoroso; ah tu, que podes!
| {v 70} E tu, que podes, põe a mão nos peitos
| À fortuna de Europa: agora é tempo,
| Que descuidados da outra parte dormem.
| Envolve em fogo, e fumo o campo, e paguem
| O teu sangue, e o meu sangue. Assim dizendo
| Se perdeu entre as nuvens, sacudindo
| Sobre as tendas no ar fumante tocha;
| E assinala com chamas o caminho.
| Acorda o índio valoroso, e salta
| Longe da curva rede, e sem demora
| {v 80} O arco, e as setas arrebata, e fere
| O chão com o pé: quer sobre o largo rio
| Ir peito a peito a contrastar co'a morte.
| Tem diante dos olhos a figura
| Do caro amigo, e inda lhe escuta as vozes.
| Pendura a um verde tronco as várias penas,
| E o arco, e as setas, e a sonora aljava;
| E onde mais manso, e mais quieto o rio
| Se estende, e espraia sobre a ruiva areia,
| Pensativo, e turbado entra; e com água
| {v 90} Já por cima do peito as mãos, e os olhos
| Levanta ao céu, que ele não via, e às ondas
| O corpo entrega. Já sabia entanto
| A nova empresa na limosa gruta
| O pátrio rio; e dando um jeito à urna,
| Fez que as águas corressem mais serenas;
| E o índio afortunado a praia oposta
| Tocou sem ser sentido. Aqui se aparta
| Da margem guarnecida, e mansamente
| Pelo silêncio vai da noite escura
| {v 100} Buscando a parte, donde vinha o vento.
| Lá, como é uso do país, roçando
| Dois lenhos entre si, desperta a chama,
| Que já se ateia nas ligeiras palhas,
| E velozmente se propaga. Ao vento
| Deixa Cacambo o resto, e foge a tempo
| Da perigosa luz; porém na margem
| Do rio, quando a chama abrasadora
| Começa a alumiar a noite escura,
| Já sentido dos guardas não se assusta,
| {v 110} E temerária, e venturosamente,
| Fiando a vida aos animosos braços,
| De um alto precipício às negras ondas
| Outra vez se lançou, e foi de um salto
| Ao fundo rio a visitar a areia.
| Debalde gritam, e debalde às margens
| Corre a gente apressada. Ele entretanto
| Sacode as pernas, e os nervosos braços:
| Rompe as escumas assoprando, e a um tempo
| Suspendido nas mãos, voltando o rosto,
| {v 120} Via nas águas trêmulas a imagem
| Do arrebatado incêndio, e se alegrava.
| Não de outra sorte o cauteloso Ulisses,
| Vaidoso da ruína, que causara,
| Viu abrasar de Troia os altos muros,
| E a perjura cidade envolta em fumo
| Encostar-se no chão, e pouco a pouco
| Desmaiar sobre as cinzas. Cresce entanto
| O incêndio furioso, e o irado vento
| Arrebata às mãos cheias vivas chamas,
| {v 130} Que aqui, e ali pela campina espalha.
| Comunica-se a um tempo ao largo campo
| A chama abrasadora, e em breve espaço
| Cerca as barracas da confusa gente.
| Armado o General, como se achava,
| Saiu do pavilhão, e pronto atalha,
| Que não prossiga o voador incêndio.
| Poucas tendas entrega ao fogo, e manda,
| Sem mais demora, abrir largo caminho,
| Que os separe das chamas. Uns já cortam
| {v 140} As combustíveis palhas, outros trazem
| Nos prontos vasos as vizinhas ondas.
| Mas não espera o bárbaro atrevido.
| A todos se adianta; e desejoso
| De levar a notícia ao grande Balda,
| Naquela mesma noite o passo estende.
| Tanto se apressa, que na quarta aurora
| Por veredas ocultas viu de longe
| A doce pátria, e os conhecidos montes,
| E o templo, que tocava o céu co'as grimpas.
| {v 150} Mas não sabia que a fortuna entanto
| Lhe preparava a última ruína.
| Quanto seria mais ditoso! Quanto
| Melhor lhe fora o acabar a vida
| Na frente do inimigo, em campo aberto,
| Ou sobre os restos de abrasadas tendas,
| Obra do seu valor! Tinha Cacambo
| Real esposa a senhoril Lindoia,
| De costumes suavíssimos, e honestos
| Em verdes anos: com ditosos laços
| {v 160} Amor os tinha unido; mas apenas
| Os tinha unido, quando ao som primeiro
| Das trombetas lho arrebatou dos braços
| A glória enganadora. Ou foi que Balda
| Engenhoso, e sutil quis desfazer-se
| Da presença importuna, e perigosa
| Do índio generoso; e desde aquela
| Saudosa manhã, que a despedida
| Presenciou dos dois amantes, nunca
| Consentiu que outra vez tornasse aos braços
| {v 170} Da formosa Lindoia, e descobria
| Sempre novos pretextos da demora.
| Tornar não esperado, e vitorioso
| Foi todo o seu delito. Não consente
| O cauteloso Balda que Lindoia
| Chegue a falar ao seu esposo; e manda
| Que uma escura prisão o esconda, e aparte
| Da luz do sol. Nem os reais parentes,
| Nem dos amigos a piedade, e o pranto
| Da enternecida esposa abranda o peito
| {v 180} Do obstinado juiz: até que à força
| De desgostos, de mágoa, e de saudade,
| Por meio de um licor desconhecido,
| Que lhe deu compassivo o santo padre,
| Jaz o ilustre Cacambo: entre os gentios
| Único, que na paz, e em dura guerra
| De virtude, e valor deu claro exemplo.
| Chorado ocultamente, e sem as honras
| De régio funeral, desconhecida
| Pouca terra os honrados ossos cobre.
| {v 190} Se é que os seus ossos cobre alguma terra.
| Cruéis ministros, encobri ao menos
| A funesta notícia. Ai que já sabe
| A assustada amantíssima Lindoia
| O sucesso infeliz. Quem a socorre!
| Que aborrecida de viver procura
| Todos os meios de encontrar a morte.
| Nem quer que o esposo longamente a espere
| No reino escuro, aonde se não ama.
| Mas a enrugada Tanajura, que era
| {v 200} Prudente, e exprimentada, e que a seus peitos
| Tinha criado em mais ditosa idade
| A mãe da mãe da mísera Lindoia,
| E lia pela história do futuro,
| Visionária, supersticiosa,
| Que de abertos sepulcros recolhia
| Nuas caveiras, e esburgados ossos,
| A uma medonha gruta, onde ardem sempre
| Verdes candeias, conduziu chorando
| Lindoia, a quem amava como filha;
| {v 210} E em ferrugento vaso licor puro
| De viva fonte recolheu. Três vezes
| Girou em roda, e murmurou três vezes
| Co'a carcomida boca ímpias palavras,
| E as águas assoprou: depois com o dedo
| Lhe impõe silêncio, e faz que as águas note.
| Como no mar azul, quando recolhe
| A lisonjeira viração as asas,
| Adormecem as ondas, e retratam
| Ao natural as debruçadas penhas,
| {v 220} O copado arvoredo, e as nuvens altas:
| Não de outra sorte à tímida Lindoia
| Aquelas águas fielmente pintam
| O rio, a praia, o vale, e os montes, onde
| Tinha sido Lisboa; e viu Lisboa
| Entre despedaçados edifícios,
| Com o solto cabelo descomposto,
| Tropeçando em ruínas encostar-se.
| Desamparada dos habitadores
| A Rainha do Tejo, e solitária,
| {v 230} No meio de sepulcros procurava
| Com seus olhos socorro; e com seus olhos
| Só descobria de um, e de outro lado
| Pendentes muros, e inclinadas torres.
| Vê mais o Luso Atlante, que forceja
| Por sustentar o peso desmedido
| Nos roxos ombros. Mas do céu sereno,
| Em branca nuvem Próvida Donzela
| Rapidamente desce, e lhe apresenta
| De sua mão, Espírito Constante,
| {v 240} Gênio de Alcides, que de negros monstros
| Despeja o mundo, e enxuga o pranto à pátria.
| Tem por despojos cabeludas peles
| De ensanguentados, e famintos lobos,
| E fingidas raposas. Manda, e logo
| O incêndio lhe obedece; e de repente
| Por onde quer que ele encaminha os passos
| Dão lugar as ruínas. Viu Lindoia
| Do meio delas, só a um seu aceno,
| Sair da terra feitos, e acabados
| {v 250} Vistosos edifícios. Já mais bela
| Nasce Lisboa de entre as cinzas: glória
| Do grande conde, que co'a mão robusta
| Lhe firmou na alta testa os vacilantes
| Mal seguros castelos. Mais ao longe
| Prontas no Tejo, e ao curvo ferro atadas
| Aos olhos dão de si terrível mostra,
| Ameaçando o mar, as poderosas
| Soberbas naus. Por entre as cordas negras
| Alvejam as bandeiras: geme atado
| {v 260} Na popa o vento; e alegres, e vistosas
| Descem das nuvens a beijar os mares
| As flâmulas guerreiras. No horizonte
| Já sobre o mar azul aparecia
| A pintada Serpente; obra, e trabalho
| Do Novo Mundo: que de longe vinha
| Buscar as nadadoras companheiras;
| E já de longe a fresca Sintra, e os montes
| Que inda não conhecia, saudava.
| Impacientes da fatal demora
| {v 270} Os lenhos mercenários junto à terra
| Recebem no seu seio, e a outros climas,
| Longe dos doces ares de Lisboa,
| Transportam a Ignorância, e a magra Inveja,
| E envolta em negros, e compridos panos
| A Discórdia, o Furor. A torpe, e velha
| Hipocrisia vagarosamente
| Atrás deles caminha; e inda duvida
| Que houvesse mão, que se atrevesse a tanto.
| O povo a mostra com o dedo; e ela
| {v 280} Com os olhos no chão da luz do dia
| Foge, e cobrir o rosto inda procura
| Com os pedaços do rasgado manto.
| Vai, filha da ambição, onde te levam
| O vento, e os mares: possam teus alunos
| Andar errando sobre as águas: possa
| Negar-lhe a bela Europa abrigo, e porto.
| Alegre deixarei a luz do dia,
| Se chegarem a ver meus olhos, que Ádria
| Da alta injúria se lembra, e do seu seio
| {v 290} Te lança: e que te lançam do seu seio
| Gália, Ibéria, e o país belo, que parte
| O Apenino, e cinge o mar, e os Alpes.
| Pareceu a Lindoia, que a partida
| Destes monstros deixava mais serenos,
| E mais puros os ares. Já se mostra
| Mais distinta a seus olhos a cidade.
| Mas viu, ai vista lastimosa! a um lado
| Ir a fidelidade portuguesa
| Manchados os puríssimos vestidos
| {v 300} De roxas nódoas. Mais ao longe estava
| Com os olhos vendados, e escondido
| Nas roupas um punhal banhado em sangue,
| O Fanatismo, pela mão guiando
| Um curvo, e branco velho ao fogo, e ao laço.
| Geme ofendida a Natureza; e geme
| Ai! muito tarde, a crédula cidade.
| Os olhos põe no chão a Igreja irada,
| E desconhece, e desaprova, e vinga
| O delito cruel, e a mão bastarda.
| {v 310} Embebida na mágica pintura
| Goza as imagens vãs, e não se atreve
| Lindoia a perguntar. Vê destruída
| A República infame, e bem vingada
| A morte de Cacambo; e atenta, e imóvel
| Apascentava os olhos, e o desejo,
| E nem tudo entendia; quando a velha
| Bateu co'a mão, e fez tremer as águas.
| Desaparecem as fingidas torres,
| E os verdes campos; nem já deles resta
| {v 320} Leve sinal. Debalde os olhos buscam
| As naus: já não são naus; nem mar, nem montes,
| Nem o lugar, onde estiveram. Torna
| Ao pranto a saudosíssima Lindoia,
| E de novo outra vez suspira, e geme.
| Até que a noite compassiva, e atenta,
| Que as magoadas lástimas lhe ouvira,
| Ao partir sacudiu das fuscas asas,
| Envolto em frio orvalho, um leve sono,
| Suave esquecimento de seus males.

¤ _Voltado._ É dito por hipótese.

¤ _Por meio._ Quanto a miúdo os jesuítas se sirvam de semelhante expediente nos casos mais apertados, só o pode ignorar quem nunca leu a História. A morte improvisa de Inocêncio XIII, quando estava de todo resoluto a pôr cobro nas desordens dos jesuítas, ainda não houve quem pusesse em dúvida ser obra dos mesmos. A mesma sorte teve o Cardeal Archinto. Em Roma é coisa pública, que o Cardeal Passionei morreu de um _acidente Jesuítico._ Este incomparável Purpurado dissera algumas vezes, que esperava ter o gosto de ver, antes da sua morte, a total extinção da Companhia. Os jesuítas tiveram o orgulho de fazer-lhe este Epitáfio: _Dominico S. R. E. Card. Passion. S. J. superstes._

¤ _Visionária._ Os índios davam-se inteiramente a superstições, e tinham não só por verossímil, senão por certa quanta extravagância se pode imaginar nesta matéria: viviam na mais crassa ignorância. Não lhes era lícito saber mais do que aquilo, que podia servir de utilidade à Companhia. Toda a doutrina, que lhes ensinavam, se reduzia a atemorizá-los com o Inferno, se não obedecessem em tudo, e por tudo aos seus _santos Padres._

¤ _Tinha sido Lisboa._ É notório quanto os jesuítas abusaram, e pretenderam servir-se da calamidade pública para consternar os povos, e reduzi-los aos seus perniciosíssimos interesses. De sorte, que a não ser a serenidade de ânimo do nosso amabilíssimo Monarca, verdadeiramente imperturbável, e a constância do seu iluminadíssimo Ministério, ficava para sempre Portugal sepultado nas ruínas de Lisboa.

¤ _Manda._ Providências sobre o Terremoto.

¤ _Dão lugar._ Desentulho da Cidade.

¤ _Sair da terra._ Reedificação de Lisboa devida inteiramente à grandeza de coração de S. Majestade, e ao incansável espírito do Ilustríssimo, e Excelentíssimo Senhor Conde de Oeiras.

¤ _Prontas no Tejo._ A Marinha Real no florentíssimo estado, em que a vemos, não é a última glória deste felicíssimo Reinado; glória, que se deve principalmente ao zelo do Ilustríssimo, e Excelentíssimo Senhor Francisco Xavier de Mendonça Furtado.

¤ _Serpente._ Nau feita no Rio de Janeiro, governando o Ilustríssimo, e Excelentíssimo Senhor Conde de Cunha, embutida de peregrinas madeiras de diversas cores, obra muito rara, e admirável no seu gênero.

¤ _Transportam._ Só a posteridade poderá justamente avaliar esta ação, que será sempre a mais brilhante entre todas as do nosso tão aplaudido Ministério. Sem se fazer este passo, jamais poderia o Reino sair da ignorância, em que o tinham.

¤ _Que Ádria._ Por aquele famoso interdito de Paulo V os jesuítas, que em umas escabrosas circunstâncias queriam ter da sua parte a Cúria, saíram de Veneza, onde finalmente depois de meio Século tornaram a entrar. Parece incrível que os Senhores Venezianos se tenham esquecido totalmente desta ação.

¤ _Gália, Ibéria._ Quando o Autor escreveu estes versos estava bem longe de imaginar que a maior parte do que neles se contém se havia de cumprir em seus dias. Temos agora de mais a mais boas esperanças de ver cumprido brevemente o resto.

¤ _Um curvo._ Gabriel de Malagrida, diabólico mártir, que cá deixou a Companhia para última prova do seu sedicioso, e fanático espírito. Os jesuítas espalharam pelos seus devotos em Roma uma estampa com esta letra: _V. P. Gabr. Malagr. in Portugall, pro fide occisus._

¤ _A Igreja._ Foi relaxado ao braço secular, &c.` },
    { n: 4, titulo: "Canto Quarto", texto: `| Salvas as tropas do noturno incêndio,
| Aos povos se avizinha o grande Andrade,
| Depois de afugentar os índios fortes,
| Que a subida dos montes defendiam,
| E rotos muitas vezes, e espalhados
| Os tapes cavaleiros, que arremessam
| Duas causas de morte em uma lança,
| E em largo giro todo o campo escrevem.
| Que negue agora a pérfida calúnia,
| {v 10} Que se ensinava aos bárbaros gentios
| A disciplina militar, e negue
| Que mãos traidoras a distantes povos
| Por ásperos desertos conduziam
| O pó sulfúreo, e as sibilantes balas,
| E o bronze, que rugia nos seus muros.
| Tu que viste, e pisaste, ó Blasco insigne,
| Todo aquele país, tu só pudeste,
| Co'a mão, que dirigia o ataque horrendo,
| E aplanava os caminhos à vitória,
| {v 20} Descrever ao teu rei o sítio, e as armas,
| E os ódios, e o furor, e a incrível guerra.
| Pisaram finalmente os altos riscos
| De escalvada montanha, que os infernos
| Co'o peso oprime, e a testa altiva esconde
| Na região, que não perturba o vento.
| Qual vê quem foge à terra pouco a pouco
| Ir crescendo o horizonte, que se encurva,
| Até que com os céus o mar confina,
| Nem tem à vista mais que o ar, e as ondas:
| {v 30} Assim quem olha do escarpado cume
| Não vê mais do que o céu, que o mais lhe encobre
| A tarda, e fria névoa, escura, e densa.
| Mas quando o Sol de lá do eterno, e fixo
| Purpúreo encosto do dourado assento,
| Co'a criadora mão desfaz, e corre
| O véu cinzento de ondeadas nuvens,
| Que alegre cena para os olhos! Podem
| Daquela altura, por espaço imenso,
| Ver as longas campinas retalhadas
| {v 40} De trêmulos ribeiros; claras fontes,
| E lagos cristalinos, onde molha
| As leves asas o lascivo vento.
| Engraçados outeiros, fundos vales,
| E arvoredos copados, e confusos,
| Verde teatro, onde se admira quanto
| Produziu a supérflua Natureza.
| A terra sofredora de cultura
| Mostra o rasgado seio; e as várias plantas
| Dando as mãos entre si, tecem compridas
| {v 50} Ruas, por onde a vista saudosa
| Se estende, e perde. O vagaroso gado
| Mal se move no campo, e se divisam
| Por entre as sombras da verdura, ao longe,
| As casas branquejando, e os altos templos.
| Ajuntavam-se os índios entretanto
| No lugar mais vizinho, onde o bom padre
| Queria dar Lindoia por esposa
| Ao seu Baldetta, e segurar-lhe o posto,
| E a régia autoridade de Cacambo.
| {v 60} Estão patentes as douradas portas
| Do grande templo, e na vizinha praça
| Se vão dispondo de uma, e de outra banda
| As vistosas esquadras diferentes.
| Co'a chata frente de urucu tingida,
| Vinha o índio Cobé disforme, e feio,
| Que sustenta nas mãos pesada maça,
| Com que abate no campo os inimigos,
| Como abate a seara o rijo vento.
| Traz consigo os selvagens da montanha,
| {v 70} Que comem os seus mortos; nem consentem
| Que jamais lhes esconda a dura terra
| No seu avaro seio o frio corpo
| Do doce pai, ou suspirado amigo.
| Foi o segundo, que de si fez mostra,
| O mancebo Pindó, que sucedera
| A Cepé no lugar: inda em memória
| Do não vingado irmão, que tanto amava,
| Leva negros penachos na cabeça.
| São vermelhas as outras penas todas,
| {v 80} Cor, que Cepé usara sempre em guerra.
| Vão com ele os seus tapes, que se afrontam,
| E que têm por injúria morrer velhos.
| Segue-se Caitutu de régio sangue,
| E de Lindoia irmão. Não muito fortes
| São os que ele conduz; mas são tão destros
| No exercício da flecha, que arrebatam
| Ao verde papagaio o curvo bico,
| Voando pelo ar. Nem dos seus tiros
| O peixe prateado está seguro
| {v 90} No fundo do ribeiro. Vinham logo
| Alegres guaranis de amável gesto.
| Esta foi de Cacambo a esquadra antiga.
| Penas da cor do céu trazem vestidas,
| Com cintas amarelas: e Baldetta
| Desvanecido a bela esquadra ordena
| No seu Jardim: até o meio a lança
| Pintada de vermelho, e a testa, e o corpo
| Todo coberto de amarelas plumas.
| Pendente a rica espada de Cacambo;
| {v 100} E pelos peitos ao través lançada
| Por cima do ombro esquerdo a verde faixa,
| De donde ao lado oposto a aljava desce.
| Num cavalo da cor da noite escura
| Entrou na grande praça derradeiro
| Tatu-Guaçu feroz, e vem guiando
| Tropel confuso de cavalaria,
| Que combate desordenadamente.
| Trazem lanças nas mãos, e lhes defendem
| Peles de monstros os seguros peitos.
| {v 110} Revia-se em Baldetta o santo padre;
| E fazendo profunda reverência,
| Fora da grande porta, recebia
| O esperado Tedeu ativo, e pronto,
| A quem acompanhava vagaroso
| Com as chaves no cinto o Irmão Patusca,
| De pesada, enormíssima barriga.
| Jamais a este o som da dura guerra
| Tinha tirado as horas do descanso.
| De indulgente moral, e brando peito,
| {v 120} Que penetrado da fraqueza humana
| Sofre em paz as delícias desta vida,
| Tais, e quais no-las dão. Gosta das coisas,
| Porque gosta, e contenta-se do efeito,
| E nem sabe, nem quer saber as causas.
| Ainda que talvez, em falta de outro,
| Com grosseiras ações o povo exorte,
| Gritando sempre, e sempre repetindo,
| Que do bom Pai Adão a triste raça
| Por degraus degenera, e que este mundo
| {v 130} Piorando envelhece. Não faltava,
| Para se dar princípio à estranha festa,
| Mais que Lindoia. Há muito lhe preparam
| Todas de brancas penas revestidas
| Festões de flores as gentis donzelas.
| Cansados de esperar, ao seu retiro
| Vão muitos impacientes a buscá-la.
| Estes de crespa Tanajura aprendem
| Que entrara no jardim triste, e chorosa,
| Sem consentir que alguém a acompanhasse.
| {v 140} Um frio susto corre pelas veias
| De Caitutu, que deixa os seus no campo;
| E a irmã por entre as sombras do arvoredo
| Busca co'a vista, e teme de encontrá-la.
| Entram enfim na mais remota, e interna
| Parte de antigo bosque, escuro, e negro,
| Onde ao pé de uma lapa cavernosa
| Cobre uma rouca fonte, que murmura,
| Curva latada de jasmins, e rosas.
| Este lugar delicioso, e triste,
| {v 150} Cansada de viver, tinha escolhido
| Para morrer a mísera Lindoia.
| Lá reclinada, como que dormia,
| Na branda relva, e nas mimosas flores,
| Tinha a face na mão, e a mão no tronco
| De um fúnebre cipreste, que espalhava
| Melancólica sombra. Mais de perto
| Descobrem que se enrola no seu corpo
| Verde serpente, e lhe passeia, e cinge
| Pescoço, e braços, e lhe lambe o seio.
| {v 160} Fogem de a ver assim sobressaltados,
| E param cheios de temor ao longe;
| E nem se atrevem a chamá-la, e temem
| Que desperte assustada, e irrite o monstro,
| E fuja, e apresse no fugir a morte.
| Porém o destro Caitutu, que treme
| Do perigo da irmã, sem mais demora
| Dobrou as pontas do arco, e quis três vezes
| Soltar o tiro, e vacilou três vezes
| Entre a ira, e o temor. Enfim sacode
| {v 170} O arco, e faz voar a aguda seta,
| Que toca o peito de Lindoia, e fere
| A serpente na testa, e a boca, e os dentes
| Deixou cravados no vizinho tronco.
| Açouta o campo co'a ligeira cauda
| O irado monstro, e em tortuosos giros
| Se enrosca no cipreste, e verte envolto
| Em negro sangue o lívido veneno.
| Leva nos braços a infeliz Lindoia
| O desgraçado irmão, que ao despertá-la
| {v 180} Conhece, com que dor! no frio rosto
| Os sinais do veneno, e vê ferido
| Pelo dente sutil o brando peito.
| Os olhos, em que Amor reinava, um dia,
| Cheios de morte; e muda aquela língua,
| Que ao surdo vento, e aos ecos tantas vezes
| Contou a larga história de seus males.
| Nos olhos Caitutu não sofre o pranto,
| E rompe em profundíssimos suspiros,
| Lendo na testa da fronteira gruta
| {v 190} De sua mão já trêmula gravado
| O alheio crime, e a voluntária morte.
| E por todas as partes repetido
| O suspirado nome de Cacambo.
| Inda conserva o pálido semblante
| Um não sei quê de magoado, e triste,
| Que os corações mais duros enternece.
| Tanto era bela no seu rosto a morte!
| Indiferente admira o caso acerbo
| Da estranha novidade ali trazido
| {v 200} O duro Balda; e os índios, que se achavam,
| Corre co'a vista, e os ânimos observa.
| Quanto pode o temor! Secou-se a um tempo
| Em mais de um rosto o pranto; e em mais de um peito
| Morreram sufocados os suspiros.
| Ficou desamparada na espessura,
| E exposta às feras, e às famintas aves,
| Sem que alguém se atrevesse a honrar seu corpo
| De poucas flores, e piedosa terra.
| Fastosa egípcia, que o maior triunfo
| {v 210} Temeste honrar do vencedor Latino,
| Se desceste inda livre ao escuro reino,
| Foi vaidosa talvez da imaginada
| Bárbara pompa do real sepulcro.
| Amável indiana, eu te prometo
| Que em breve a iníqua pátria envolta em chamas
| Te sirva de urna, e que misture, e leve
| A tua, e a sua cinza o irado vento.
| Confusamente murmurava entanto
| Do caso atroz a lastimada gente.
| {v 220} Dizem que Tanajura lhe pintara
| Suave aquele gênero de morte,
| E talvez lhe mostrasse o sítio, e os meios.
| Balda, que há muito espera o tempo, e o modo
| De alta vingança, e encobre a dor no peito,
| Excita os povos a exemplar castigo
| Na desgraçada velha. Alegre em roda
| Se ajunta a petulante mocidade
| Co'as armas, que o acaso lhe oferece.
| Mas neste tempo um índio pelas ruas
| {v 230} Com gesto espavorido vem gritando,
| Soltos, e arrepiados os cabelos:
| Fugi, fugi da mal segura terra,
| Que estão já sobre nós os inimigos.
| Eu mesmo os vi, que descem do alto monte,
| E vêm cobrindo os campos; e se ainda
| Vivo chego a trazer-vos a notícia,
| Aos meus ligeiros pés a vida eu devo.
| Debalde nos expomos neste sítio,
| Diz o ativo Tedeu: melhor conselho
| {v 240} É ajuntar as tropas no outro povo:
| Perca-se o mais, salvemos a cabeça.
| Embora seja assim: faça-se em tudo
| A vontade do céu; mas entretanto
| Vejam os contumazes inimigos
| Que não têm que esperar de nós despojos.
| Falte-lhe a melhor parte ao seu triunfo.
| Assim discorre Balda; e entanto ordena,
| Que todas as esquadras se retirem,
| Dando as casas primeiro ao fogo, e o templo.
| {v 250} Parte, deixando atada a triste velha
| Dentro de uma choupana, e vingativo
| Quis que por ela começasse o incêndio.
| Ouviam-se de longe os altos gritos
| Da miserável Tanajura. Aos ares
| Vão globos espessíssimos de fumo,
| Que deixa ensanguentada a luz do dia.
| Com as grossas camáldulas à porta,
| Devoto, e penitente os esperava
| O Irmão Patusca, que ao rumor primeiro
| {v 260} Tinha sido o mais pronto a pôr-se em salvo,
| E a desertar da perigosa terra.
| Por mais que o nosso General se apresse,
| Não acha mais que as cinzas inda quentes,
| E um deserto, onde há pouco era a cidade.
| Tinham ardido as míseras choupanas
| Dos pobres índios, e no chão caídos
| Fumegavam os nobres edifícios,
| Deliciosa habitação dos padres.
| Entram no grande templo, e veem por terra
| {v 270} As imagens sagradas. O áureo trono,
| O trono, em que se adora um Deus imenso,
| Que o sofre, e não castiga os temerários,
| Em pedaços no chão. Voltava os olhos
| Turbado o General: aquela vista
| Lhe encheu o peito de ira, e os olhos de água.
| Em roda os seus fortíssimos guerreiros
| Admiram espalhados a grandeza
| Do rico templo, e os desmedidos arcos,
| As bases das firmíssimas colunas,
| {v 280} E os vultos animados, que respiram.
| Na abóbada o artífice famoso
| Pintara... mas que intento! as roucas vozes
| Seguir não podem do pincel os rasgos.
| Gênio da inculta América, que inspiras
| A meu peito o furor, que me transporta,
| Tu me levanta nas seguras asas.
| Serás em paga ouvido no meu canto.
| E te prometo, que pendente um dia
| Adorne a minha lira os teus altares.

¤ _Que negue._ Os jesuítas, que hoje negam altamente a verdade de fatos tão evidentes, faziam em outro tempo ostentação disto mesmo. Os versos seguintes são do já citado jesuíta _Vanier_ na digressão a respeito dos índios do Paraguai. _Praed. rust. Lib. xiv._

¤ | _- - - - - - arma, ducesque paratos_
| _Semper habent, Martisque truces formantur in usus._
| _Haec operum requies, sacris jam ritè peractis,_
| _Timpanaque, & lituos festis audire diebus,_
| _Et peditum turmas, equitumque videre sub armis._

¤ _Blasco._ O Marechal D. Michel Ângelo de Blasco Engenheiro-mor do Reino.

¤ _O bom Padre._ Balda.

¤ _Urucu._ Rheed. Ericú mal. 2. p. 53. t. 31. Veja-se Linae. _Species plantarum._ Pentandr. Monog.

¤ _A quem acompanhava._ Este retrato é tirado ao natural de um Leigo da Companhia, que o Autor conheceu.

¤ _No jardim._ Os índios viviam na maior miséria, e apenas tinham as coisas necessárias absolutamente para a vida. Os Padres porém viviam todos na abundância, e tinham jardins deliciosos, onde recolhiam os espíritos cansados de trabalhar na vinha do Senhor.

¤ _Fastosa Egípcia._ Cleópatra.

¤ _Entram._ Os nossos ainda conseguiram salvar o Templo, do qual se remeteu a planta, e o prospecto a S. Majestade. Os Padres tinham mandado despedaçar as Imagens, e reduzir a pequenas partes o Sacrário.

¤ _Admiram._ O General não se podia persuadir, que os riquíssimos ornamentos tivessem sido bordados naquele País, até que se lhe mostrou um, que foi achado junto à Sacristia ainda imperfeito no tear.` },
    { n: 5, titulo: "Canto Quinto", texto: `| Na vasta, e curva abóbada pintara
| A destra mão de artífice famoso,
| Em breve espaço, e Vilas, e Cidades,
| E Províncias, e Reinos. No alto sólio
| Estava dando leis ao mundo inteiro
| A Companhia. Os Cetros, e as Coroas,
| E as Tiaras, e as Púrpuras em torno
| Semeadas no chão. Tinha de um lado
| Dádivas corruptoras: do outro lado
| {v 10} Sobre os brancos altares suspendidos
| Agudos ferros, que gotejam sangue.
| Por esta mão ao pé dos altos muros
| Um dos Henriques perde a vida, e o Reino.
| E cai por esta mão, oh céus! debalde
| Rodeado dos seus o outro Henrique.
| Delícia do seu povo, e dos humanos.
| Príncipes, o seu sangue é vossa ofensa.
| Novos crimes prepara o horrendo monstro.
| Armai o braço vingador: descreva
| {v 20} Seus tortos sulcos o luzente arado
| Sobre o seu trono; nem aos tardos netos
| O lugar, em que foi, mostrar-se possa.
| Viam-se ao longe errantes, e espalhados
| Pelo mundo os seus filhos ir lançando
| Os fundamentos do esperado Império,
| De dois em dois: ou sobre os coroados
| Montes do Tejo; ou nas remotas praias,
| Que habitam as pintadas Amazonas,
| Por onde o rei das águas escumando
| {v 30} Foge da estreita terra, e insulta os mares.
| Ou no Ganges sagrado; ou nas escuras
| Nunca de humanos pés trilhadas serras,
| Aonde o Nilo tem, se é que tem fonte.
| Com um gesto inocente aos pés do trono
| Via-se a Liberdade Americana,
| Que arrastando enormíssimas cadeias,
| Suspira, e os olhos, e a inclinada testa
| Nem levanta, de humilde, e de medrosa.
| Tem diante riquíssimo tributo,
| {v 40} Brilhante pedraria, e prata, e ouro,
| Funesto preço, por que compra os ferros.
| Ao longe o mar azul, e as brancas velas,
| Com estranhas divisas nas bandeiras,
| Denotam que aspirava ao senhorio,
| E da navegação, e do comércio.
| Outro tempo, outro clima, outros costumes.
| Mais além tão diversa de si mesma
| Vestida em larga roupa flutuante,
| Que distinguem barbáricos lavores,
| {v 50} Respira no ar chinês o mole fasto
| De asiática pompa; e grave, e lenta
| Permite aos bonzos, apesar de Roma,
| Do seu Legislador o indigno culto.
| Aqui entrando no Japão fomenta
| Domésticas discórdias. Lá passeia
| No meio dos estragos, ostentando
| Orvalhadas de sangue as negras roupas.
| Cá desterrada enfim dos ricos portos,
| Voltando a vista às terras, que perdera,
| {v 60} Quer pisar temerária, e criminosa...
| Oh céus! Que negro horror! Tinha ficado
| Imperfeita a pintura, e envolta em sombras.
| Tremeu a mão do artífice ao fingi-la,
| E desmaiaram no pincel as cores.
| Da parte oposta, nas soberbas praias
| Da rica Londres trágica, e funesta,
| Ensanguentado o Tâmega esmorece,
| Vendo a conjuração pérfida, e negra,
| Que se prepara ao crime; e intenta, e espera
| {v 70} Erguer aos céus nos inflamados ombros,
| E espalhar pelas nuvens denegridos
| Todos os grandes, e a famosa fala.
| Por entre os troncos de umas plantas negras,
| Por obra sua, viam-se arrastados
| Às ardentes areias africanas
| O valor, e alta glória portuguesa.
| Ai mal aconselhado, quanto forte,
| Generoso Mancebo! eternos lutos
| Preparas à chorosa Lusitânia.
| {v 80} Desejado dos teus, a incertos climas
| Vás mendigar a morte, e a sepultura.
| Já satisfeitos do fatal desígnio,
| Por mão de um dos Filipes, afogavam
| Nos abismos do mar, e emudeciam
| Queixosas línguas, e sagradas bocas,
| Em que ainda se ouvia a voz da pátria.
| Crescia o seu poder, e se firmava
| Entre surdas vinganças. Ao mar largo
| Lança do profanado oculto seio
| {v 90} O irado Tejo os frios nadadores.
| E deixa o barco, e foge para a praia
| O pescador, que atônito recolhe
| Na longa rede o pálido cadáver
| Privado de sepulcro. Enquanto os nossos
| Apascentam a vista na pintura,
| Nova empresa, e outro gênero de guerra
| Em si revolve o General famoso.
| Apenas esperou que ao sol brilhante
| Desse as costas de todo a opaca terra;
| {v 100} Precipitou a marcha, e no outro povo
| Foi surpreender os índios. O Cruzeiro,
| Constelação dos europeus não vista,
| As horas declinando lhe assinala.
| A corada manhã serena, e pura
| Começava a bordar nos horizontes
| O céu de brancas nuvens povoado,
| Quando, abertas as portas, se descobrem
| Em trajes de caminho ambos os padres,
| Que mansamente do lugar fugiam,
| {v 110} Desamparando os miseráveis índios,
| Depois de expostos ao furor das armas.
| Lobo voraz, que vai na sombra escura
| Meditando traições ao manso gado,
| Perseguido dos cães, e descoberto
| Não arde em tanta cólera, como ardem
| Balda, e Tedeu. A soldadesca alegre
| Cerca em roda o fleumático Patusca,
| Que próvido de longe os acompanha,
| E mal se move no jumento tardo.
| {v 120} Pendem-lhe dos arções de um lado, e de outro
| Os paios saborosos, e os vermelhos
| Presuntos europeus; e a tiracolo
| Inseparável companheira antiga
| De seus caminhos a borracha pende.
| Entra no povo, e ao templo se encaminha
| O invicto Andrade; e generoso entanto
| Reprime a militar licença, e a todos
| Co'a grande sombra ampara: alegre, e brando
| No meio da vitória. Em roda o cercam,
| {v 130} (Nem se enganaram) procurando abrigo
| Chorosas mães, e filhos inocentes,
| E curvos pais, e tímidas donzelas.
| Sossegado o tumulto, e conhecidas
| As vis astúcias de Tedeu, e Balda,
| Cai a infame República por terra.
| Aos pés do General as toscas armas
| Já tem deposto o rude Americano,
| Que reconhece as ordens, e se humilha,
| E a imagem do seu rei prostrado adora.
| {v 140} Serás lido Uraguai. Cubra os meus olhos
| Embora um dia a escura noite eterna.
| Tu vive, e goza a luz serena, e pura.
| Vai aos bosques de Arcádia: e não receies
| Chegar desconhecido àquela areia.
| Ali de fresco entre as sombrias murtas
| Urna triste a Mireo não todo encerra.
| Leva de estranho céu, sobre ela espalha
| Co'a peregrina mão bárbaras flores.
| E busca o sucessor, que te encaminhe
| {v 150} Ao teu lugar, que há muito que te espera.

¤ _Na vasta._ As façanhas dos jesuítas não estavam sepultadas só no Uraguai. Quem se admirar da pintura deste Templo, considere atentamente a que eles têm na Igreja do seu Colégio Romano, e na da Casa Professa, que com estar cobertas da máscara da Religião, não deixam de ser ainda mais soberbas, e insultantes.

¤ _Um dos Henriques._ Henrique III assassinado por Fr. Jacques Clemente. Quem há que ignore quanta parte tiveram nisto os jesuítas? É público o processo do P. Guignard, e quanto a Companhia defende ainda hoje este seu digno filho. Vejam-se os seus Autores, e por todos o Jovency.

¤ _O outro Henrique._ Na morte de Henrique IV soube-se esconder melhor a mão Jesuítica; mas não se soube esconder nas duas ocasiões antecedentes, em que se tinha intentado o mesmo parricídio. O Padre Varade, Superior da Companhia em Paris, foi quem desencaminhou ao miserável Barriere: levou-o ao seu cubículo, deitou-lhe a sua bênção, confessou-o, deu-lhe depois a comunhão, &c. Os jesuítas no Colégio de Clermont, e na sua Igreja de Santo Antônio, por meio de práticas, conferências, meditações, e exercícios espirituais corromperão o espírito de Chatel.

¤ _Novos crimes._ Tragam-se à memória a tarde de 5 de janeiro, e a noite de 3 de setembro tão funestas para França, e Portugal, e que podiam cobrir de luto estas duas Monarquias.

¤ _O seu trono._ O trono da Companhia está em Roma. Lá é o centro do seu poder. Ali recebe o seu Geral os avisos do que se passa em todas as partes do Mundo: e dali com o maior despotismo envia as suas ordens ao fim da terra. Exterminá-la das outras Províncias é fazer-lhe guerra pela rama: é necessário cortar-lhe a raiz. Ora os tesouros das duas índias ajudavam muito a sustentar o crédito dos jesuítas em Roma. Afortunadamente as presentes disposições todas anunciam a próxima total extinção daquele Corpo.

¤ _De dois em dois._ Os jesuítas em Portugal eram chamados os Apóstolos: e escrupulosamente observavam a exterioridade do _misit illos binos._

¤ _Rei das águas._ O Rio das Amazonas por uma boca de oitenta léguas sai encanado com tal força, que lança por muitas léguas ao mar água doce.

¤ _Aonde o Nilo tem._ Os jesuítas até se jactam nas suas Histórias de ter descoberto a origem do Nilo.

¤ _Nem levanta._ Não há palavras, que expliquem bastantemente a sujeição, em que viviam aqueles índios. Vejam-se os fragmentos das Cartas do Conde de Bobadela citadas na _República_, &c.

¤ _As brancas velas._ Os jesuítas do Brasil tinham uma fragata magnífica, em que o Provincial saía todos os anos a título de visitar a Província; porém na realidade era a que fazia a maior parte do comércio, que aqueles portos têm entre si. Enquanto a fragata recebia carga, estavam ociosas todas as outras embarcações; sendo os fretes daquela mais caros, a título de ir a fazenda mais segura. Ora os jesuítas nas Alfândegas nunca pagaram direitos. O seu lucro era imenso. Para se conseguir melhor este fim, espalharam pelo povo uma profecia do seu Padre Anchieta, que aquela fragata nunca se perderia. Encalharam-na finalmente, e fizeram outra, que custou cinquenta mil cruzados. E sendo-lhes necessário perpetuar aquela santa impostura, mandaram pregar na nova algumas tábuas da velha: e persuadiram àqueles bons negociantes, que bastava aquela parte para comunicar a virtude ao todo. O Autor viu muitas vezes esta fragata, e entrou nela. Trazia flâmula, e bandeira com a insígnia da Companhia; e tinha de mais a mais excelente artilharia. Ao entrar, e sair dos portos recebia todas as honras, que se fazem às naus do Rei.

¤ _Mais além._ Os jesuítas da China no ano de 1645 aproveitaram-se da divisão daquele grande Império, entre os dois pretendentes, para o entregarem ao Kam dos tártaros. Foram em prêmio elevados à dignidade de Mandarins, e ornados com os ricos vestidos, e colares, que se podem ver na estampa, que nos deixou o P. Bonani no _Catálogo dos Religiosos, &c._

¤ _Permite._ E de mais a mais o servirem-se, para nomear o verdadeiro Deus, das vozes _Tien_ Céu, e _Xamti_ supremo Imperador: e fazerem certas oblações aos seus defuntos.

¤ _Bonzos._ Sacerdotes da China.

¤ _A pesar de Roma._ E bem a pesar dela, que enfim cansou de lutar por mais de um século com a animosidade dos jesuítas. O fruto, que se tirou dos Decretos das Sagradas Congregações publicados em 1645, foi o que tirou Monsig. Maigrot em 1693, o Cardeal de Tournon em 1704, Clemente XI em 1710, Benedito XIII em 1727, Clemente XII em 1734, Benedito XIV em 1742. Com tudo isto ainda hoje não cessam de repetir que são a guarda pretoriana do Papa; e o mais é que falam verdade:

¤ | _En ses Pretoriens Rome eut autant destraitres,_
| _Ils marchandaient l' Empire, e lui donnaient des maitres._

¤ Le Philosophe de Sans-souci dans l' Epitre a Darget.

¤ _Legislador._ Confúcio.

¤ Que perdera. _Qualia forte dolent dites Orientis ad oras_

¤ | _- - - - erepta - - - sibi regna. - - -_

¤ Vanier. supr.

¤ _Quer pisar._ Os jesuítas com as suas restrições mentais não duvidaram ao princípio calcar o crucifixo, por não perderem aquele riquíssimo comércio. Quem quiser fazer conceito da extensão deste, e de outras curiosidades nesta matéria, leia as viagens de Mr. Duquesne mandado por Luís XIV às índias Orientais. Tom. 3. pag. 81.

¤ _A conjuração._ Os Padres Garnet, e Oldecorne réus convictos, e confessos da conjuração da pólvora.

¤ _Nos abismos do mar._ Veja-se a _Dedução Cronológica_; Obra, que servirá de Época à restauração das Letras em Portugal; monumento de zelo, e de fidelidade.` },
    { n: "", titulo: "Ao Autor", texto: `## Soneto

| Parece-me que vejo a grossa enchente,
| E a vila errante, que nas águas boia:
| Detesto os crimes da infernal tramoia:
| Choro a Cacambo, e a Cepé valente.

| Não é presságio vão: lerá a gente
| A guerra do Uraguai, como a de Troia;
| E o lagrimoso caso de Lindoia
| Fará sentir o peito, que não sente.

| Ao longe, a Inveja um país ermo, e bronco
| Infecte com seu hálito perverso,
| Que a ti só chega o mal distinto ronco.

| Ah! consente que o meu junto ao teu verso,
| Qual fraca vide, que se arrima a um tronco,
| Também vá discorrer pelo Universo.

De Joaquim Inácio de Seixas Brandão, Doutor em Medicina pela Universidade de Montpellier.

## Soneto

| Entro pelo Uraguai: vejo a cultura
| Das novas terras por engenho claro;
| Mas chego ao Templo majestoso, e paro
| Embebido nos rasgos da pintura.

| Vejo erguer-se a República perjura
| Sobre alicerces de um domínio avaro:
| Vejo distintamente, se reparo,
| De Caco usurpador a cova escura.

| Famoso Alcides, ao teu braço forte
| Toca vingar os cetros, e os altares:
| Arranca a espada, descarrega o corte.

| E tu, Termindo, leva pelos ares
| A grande ação; já que te coube em sorte
| A gloriosa parte de a cantares.

Do Doutor Inácio José de Alvarenga Peixoto, graduado na faculdade de Leis pela Universidade de Coimbra.` }
  ]
});
