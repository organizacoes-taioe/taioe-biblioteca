# Notas do tradutor: _Mit brennender Sorge_ (Pio XI, 14/3/1937)

Tradução nova, do alemão do vatican.va, conferido palavra a palavra com as AAS 29 (1937), n. 5,
pp. 145-167 (PDF `AAS-29-1937-ocr.pdf`; a página citada é a da edição impressa). O alemão é a língua
oficial da encíclica (nas AAS vem depois a versão italiana, pp. 168-188, que não se usou). 111 blocos
nos dois arquivos: 6 de cabeçalho, 53 parágrafos, 11 títulos de seção, 40 notas, data e assinatura.

Para o `obras.py` (não mexi nele): o original é alemão, como na _Tra le sollecitudini_ é italiano,
`'traducao': {'lingua': 'alemão', 'codigo': 'de', 'titulo': 'Mit brennender Sorge'}`; subtítulo
«Sobre a situação da Igreja Católica no Reich alemão»; fonte do texto, a página alemã do vatican.va;
texto oficial, AAS 29 (1937), pp. 145-167. O botão do original ao lado seria «Alemão».

## 1. O texto de base e a numeração

- **O texto do vatican.va não é a transcrição das AAS**: é outra edição, com os parágrafos numerados
  (1 a 53), as referências em notas no fim (as AAS as dão entre parênteses, no próprio texto), os
  títulos de seção sem parênteses e com «ß» (as AAS, compostas em Roma, escrevem «ss»: «dass»,
  «muss»). Ficou a base, como manda o § 1 das convenções, com a ortografia alemã de 1937 que ele tem
  («daß», «muß», «Mißtrauen»).
- **Numeração `{§ n}`**: a do próprio texto alemão do vatican.va (1 a 53), uma marca no começo de
  cada parágrafo, e não a da versão inglesa (1 a 43, que junta vários parágrafos alemães num só). As
  AAS não numeram. Ver a dúvida 1 no relatório.
- Títulos de seção: os 11 do original (nas AAS, entre parênteses, centrados), com «## ». Nas AAS há
  ainda um «* * *» antes do primeiro título («Reiner Gottesglaube»); o vatican.va não o tem, e não
  entrou.
- Cabeçalho: o do vatican.va («PIUS XI. / ENZYKLIKA / MIT BRENNENDER SORGE / destinatários e tema /
  VOM 14. MÄRZ 1937 / Ehrwürdige Brüder! Gruß und Apostolischen Segen!»). O das AAS é outro
  («RUNDSCHREIBEN AN DIE EHRWÜRDIGEN BRÜDER…», «PAPST PIUS XI»), sem a data.

## 2. Correções do texto de base (vatican.va → AAS)

Feitas no original e seguidas na tradução; todas conferidas nas AAS. As duas primeiras mudam o sentido.

- p. 159 (§ 35): **falta no vatican.va uma frase inteira**. O site lê «…„Recht ist, was dem Volke
  nützt“, gemessen werden, wenn man unterstellt, daß sittlich Unerlaubtes nie…», o que faz de uma
  concessão a condição da medida. As AAS: «…gemessen werden. **Zwar kann dem Satz ein rechter Sinn
  gegeben werden,** wenn man unterstellt…». Reposta (com «ß»/«ss» do site), traduzida «É verdade que
  se pode dar a esta frase um sentido correto, se se supõe…».
- p. 148 (§ 9): «wer das Wort **Gottes** rednerisch gebraucht» → «das Wort **Gott**» (quem usa
  retoricamente a palavra «Deus», e não «a palavra de Deus»).
- p. 148 (§ 10): «WeltalI gleich setzt» → «Weltall gleichsetzt».
- p. 153 (§ 22): «zur Kirche Christi zu zähle» → «zu zählen».
- p. 158 (§ 34): «ungenützt lassen oder ihnen den Weg … gar bewußt **zu** versperren» → «bewußt
  versperren» (os dois infinitivos são sujeito de «ist»; as AAS não têm «zu»).
- p. 165 (§ 49): «das Echo finden werden, **daß** der liebenden Sorge … entspricht» → «**das**».
- § 21: «[17],aus» → «[17], aus» (espaço).
- Nota 1: «3 _Joh_ 4,4» → «3 _Joh_ 4» (a 3ª carta de João tem um só capítulo; AAS p. 146: «3 Joh. 4»).
- Notas 11, 12, 14, 15, 16, 19, 27, 28, 36: espaços fora do lugar no itálico do site («1 _ Joh_»,
  «_Ps _2,4», «1 _ Tim _3,15») arrumados; nota 25, «Hebr» sem itálico → «_Hebr_», como as outras.

O extrator corrigido (`<solto>`) foi rodado de novo na página: os blocos soltos são só menu e título
da página, e nenhum falta no corpo, o que confere com a comparação palavra a palavra com as AAS.

**Variantes não corrigidas** (o site tem outra lição, mas não erro evidente; a tradução segue o site).
Ficam aqui para quem quiser conferir com o texto oficial: § 2 «Episkopates» (AAS «Episkopats»);
§ 8 «so wenden Wir Uns an Euch» (AAS «… Uns **heute** an Euch»), «liebevoll Besuch» (AAS
«liebevollen»); § 11 «von einem Ende der Welt zum anderen» (AAS «bis zum andern»); § 13 «Einer» (AAS
«einer»); § 14 «seinsgemäß» (AAS «seinsmässig»); § 15 «in die Grenze» (AAS «Grenzen»); § 16
«beachtet und befolgt» (AAS «geachtet»); § 17 «angrifflüsternes» (AAS «angriffslüsternes»); § 19
«Verheißungen» (AAS «Verheissung»), «über alle **Fehde** und Sünde» (o PDF lê «Fehle», as faltas; não
pude ver a imagem), «ihre Augen» (AAS «ihr Auge»), «in dem Neuen Bunde» (AAS «im»); § 22 «den Balken»
(AAS «dem»), «in deren Händen» (AAS «Hände»), «Vorstellung» (AAS «Vorstellungen»); § 35 «Grundlagen
des Rechtslebens» (AAS «Grundlegung»); § 41 «allein» em outro lugar; § 43 «ihre unsterbliche Seele»
(AAS «ihrer unsterblichen Seele»), «Siegeskranz» (AAS «Siegerkranz»), «begleiten» (AAS
«begleiteten»); § 44 «haßverzehrten» (AAS «hassverzerrten»: deformado, e não consumido, pelo ódio),
«Die apostolische Liebe» (AAS «Diese»), «Sünde an der Wohlfahrt» (AAS «an der wahren Wohlfahrt»);
§ 45 «liebgewordener» (AAS «liebgewonnener»), «bemüht waren» (AAS «war»); § 47 «ein feierliches
Abkommen der Kirche ihnen» (AAS «der Kirche und ihnen»); § 48 «Kinderseele» (AAS «Kindesseele»),
«geliebte katholische **Christen**» (AAS «**Eltern**»), «vergeßt es nicht» (AAS «vergesst eines
nicht»); § 51 «Verinnerlichung durch Buße» (AAS «und Buße»), «das sind Wir gewiß» (AAS «des»).
Diferenças só de grafia (Ä/Ae, maiúscula do pronome, hífen, «Knien/Knieen») não se listam.

## 3. Termos (para a tabela do § 3)

| original | tradução |
|---|---|
| Ehrwürdige Brüder | Veneráveis Irmãos |
| Gruß und Apostolischen Segen | Saúde e bênção apostólica |
| Wir, Uns, Unser (o papa; também onde o site põe minúscula: «uns», «unsere Schuld», «senden wir») | Nós, Nos, Nosso |
| Ihr, Euch, Euer (aos bispos, com maiúscula de carta) | vós, vosso, com minúscula, como para os fiéis |
| Er, Seine (Deus, Cristo) | ele, seu, com minúscula |
| Enzyklika; Schreiben, Sendschreiben | Encíclica; carta |
| Oberhirten (no cabeçalho) | Ordinários («aos demais Ordinários») |
| Episkopat (hochwürdigster) | episcopado (reverendíssimo) |
| Reich; Deutsches Reich; Reichsregierung | Reich; Reich alemão; governo do Reich (sem itálico: nome próprio corrente em português) |
| Reich Gottes, Gottesreich | Reino de Deus |
| Konkordat, Vereinbarung, Abkommen, Vertrag | Concordata (a de 1933, com maiúscula); acordo; acordo; tratado |
| Vertragstreue, Vereinbarungstreue | fidelidade ao tratado; fidelidade ao acordo |
| Volk; Volksgemeinschaft; Volkserziehung | povo; comunidade do povo (no § 21, plural: comunidades dos povos); educação do povo |
| Rasse; Blut und Rasse; Mythus von Blut und Rasse | raça; o sangue e a raça; mito do sangue e da raça |
| Gottesglaube; gottgläubig, die Gottgläubigen | fé em Deus; crente em Deus, os crentes em Deus |
| Christusglaube; Kirchenglaube | fé em Cristo; fé na Igreja |
| gläubig (o cristão), Gläubige | crente; fiéis |
| Neuheidentum | neopaganismo |
| Nationalkirche; Weltkirche | Igreja nacional; Igreja universal |
| Kirchenaustritt | saída da Igreja |
| Bekenntnisschule | escola confessional |
| Staatsjugend; Pflichtorganisation | juventude do Estado; organização obrigatória |
| Bekenner | confessores |
| Heiland; Erlöser | Salvador; Redentor |
| Weltanschauung | visão do mundo |
| Ertüchtigung (sittliche, körperliche, des Leibes) | fortalecimento (moral, físico, do corpo) |
| heldisch, Heldentum | heroico, heroísmo |
| Naturrecht; positives Recht | direito natural; direito positivo |
| Katholische Aktion; Laienapostolat | Ação Católica; apostolado dos leigos |
| Ordensleute; Orden; Ordensgenossenschaften | religiosos; ordens religiosas; congregações religiosas |
| Gegeben im Vatikan, am Passionssonntag | Dado no Vaticano, no Domingo da Paixão |
| PIUS PP. XI. | PIO PP. XI. |

Escolhas que pesam:

- **gottgläubig**: era o rótulo oficial do regime para quem saía das Igrejas mas se dizia «crente em
  Deus». O documento o desmonta nos §§ 9-12 («Não é crente em Deus quem…»). «Crente em Deus», sempre
  igual, guarda a palavra e a ironia; e no § 28 «gläubig» entre aspas («crente») retoma o jogo.
- **Volksgemeinschaft**: termo da propaganda; «comunidade do povo», literal, em vez de «comunidade
  nacional», para que o leitor reconheça a palavra quando o papa a devolve (§ 43: «verdadeira
  comunidade do povo»).
- **Reich** fica Reich (o título dado pelo pedido); «Reiche Gottes», no § 1, é «Reino de Deus».
- **Totalität** (§ 14): «totalidade», de propósito (o eco do Estado total).
- «Recht ist, was dem Volke nützt» (§ 35), lema jurídico do regime: «Direito é o que é útil ao povo».
- «Mutterkirche» (§ 4): «Igreja Mãe».

## 4. Passagens e soluções

- Título e subtítulo ficam em alemão no cabeçalho («_MIT BRENNENDER SORGE_», como «_DIVINI
  REDEMPTORIS_»); o incipit, na tradução, é «Com ardente preocupação».
- § 2: «Apostel der Liebe» (São João): «Apóstolo do amor».
- § 5: «inimicus homo» fica em latim, em itálico e entre aspas, como o original o cita; «Oberhaupt»
  (da Igreja): «Chefe»; «Anschauungsunterricht»: «lição prática»; «Schildhalter»: «escudeiros».
- § 6: «Gewährenlassen oder gar … Begünstigung»: «tolerância … ou até o favor que se lhes concedesse».
- § 7: «katholischen Erziehungsberechtigten»: «católicos a quem cabe o direito de educar»;
  «verbrieftes Recht»: «direito garantido por escrito».
- § 13: «dreipersönlich»: «tripessoal».
- § 14: «Menschensatzung / Gottessatzung»: «ordenação humana / ordenação divina».
- § 19: «Heilsführung»: «condução salvadora»; «Meintat»: «crime».
- § 20: «Wahnprophet»: «profeta insensato» («Wahnversuch», § 15: «tentativa insensata»).
- § 22: «zur Kirche Christi zu zählen»: «figurar na Igreja de Cristo»; «über den Splitter … den
  Balken übersehen»: «por causa do cisco no olho do irmão não veem a trave no próprio olho».
- § 24: «mir soll die Zunge am Gaumen kleben»: «que a minha língua se pegue ao paladar» (evitei
  «pegue-se-me»).
- § 31: «In seinem Kusse sterben wir»: «Beijando-a morremos».
- § 34: «das Können und Vollbringen»: «o poder e o realizar».
- § 36: «unverlierbares Recht»: «direito imprescritível» («inalienável» ficou para «unveräußerlich»,
  §§ 30 e 42).
- § 42: «der sei ausgeschlossen» (o anátema de Gl 1,9 na tradução alemã): «seja excluído».
- § 44: «Nachkriegszeit»: «desde o fim da guerra»; o período final («folgt … der Dank») virou passiva
  («são acompanhados … pela gratidão»).
- § 48: «Ersatzglauben»: «fé substituta»; «von Unberufenen»: «por quem não tem autoridade para isso».
- § 51: «Te Deum» em itálico na tradução (o original não o destaca); «Dulder»: «sofredor paciente».
- § 53: «erteilen … den Apostolischen Segen»: «concedemos … a Bênção Apostólica».
- Citações bíblicas traduzidas do alemão do documento (Sl na numeração da Vulgata, como ele: 13,1;
  42,4); nas notas, as abreviaturas portuguesas (3Jo, 2Pd, Sb, Is, Hb, Tt, At, Gl, Cl…), «Vgl.» →
  «Cf.», «Cicero de officiis» → «Cícero, _De officiis_».
