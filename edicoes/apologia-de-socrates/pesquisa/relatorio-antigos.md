# Relatório: filósofos e escritores antigos não cristãos sobre a Apologia

Grupo: gregos e latinos não cristãos, até o fim da Antiguidade. Resultado em `achados.json`
(58 achados, ordenados por parte). Originais baixados em `textos/` (XML do Perseus e do
First1KGreek em `grc/` e `f1k/`, convertidos em `txt/`; páginas da Latin Library em `lat/` e
`lattxt/`; OCR do archive.org em `archive/`). Scripts em `scripts/` (`montar.py` gera o JSON a
partir de `dados1.py`, `dados2.py` e `dados3.py`).

## Como foi feito

- Grego: clone parcial dos repositórios PerseusDL/canonical-greekLit e OpenGreekAndLatin/First1KGreek;
  busca de «Σωκρ», «Ἄνυτ», «Μέλητ», «δαιμόνι», «Χαιρεφ», «ἀπολογ» etc. e leitura do contexto.
- Latim: The Latin Library (Cícero, Sêneca, Quintiliano, Valério Máximo, Gélio, Apuleio) e, para o
  *Lucullus* de Cícero, o canonical-latinLit do Perseus.
- Neoplatônicos: Proclo e Olimpiodoro, *In Alcibiadem*, ed. Creuzer (1820–21), e Hérmias, *In
  Phaedrum*, ed. Couvreur (1901), pelo OCR do archive.org.
- Links: todos testados. Os do Scaife (Perseus) foram conferidos passagem por passagem pela rota
  `library/passage/<urn>/json/` (ref inexistente devolve 303; todas deram 200).
- Tradução: minha, do original; varredura de mesóclise e de formas europeias sem ocorrências.

## Edições por trás dos textos digitais (para transparência)

Xenofonte, Apologia: Marchant (OCT, 1921). Aristóteles: Retórica, Ross (OCT, impressão de 1959);
Metafísica, Ross (1924); Ética a Nicômaco, Bywater (1894). Epicteto: Schenkl (Teubner, 1916).
Marco Aurélio: Leopold (Teubner, 1908). Dião: von Arnim (1893–96). Plutarco: Bernardakis (Teubner,
1891–95). Diógenes Laércio: Hicks (Loeb, 1925). Luciano: Jacobitz (Teubner, 1909). Eliano: Hercher
(Teubner, 1866). Máximo de Tiro: Hobein (Teubner, 1910). Musônio: Hense (Teubner, 1905). Latim: os
textos da Latin Library (edições antigas, não identificadas página a página). Todos os autores são
antigos; só a Retórica de Ross é impressão recente de edição de editor morto em 1971 (o texto é o
do Perseus, que o briefing admite).

## Contagem

Por autor: Xenofonte 9, Epicteto 8, Cícero 6, Plutarco 5, Sêneca 4, Aristóteles 4, Diógenes
Laércio 4 (para notas), Proclo 3, Máximo de Tiro 2, Dião Crisóstomo 2, Luciano 2, Apuleio 2,
Quintiliano 1, Eliano 1, Musônio 1, Élio Aristides 1, Olimpiodoro 1, Juliano 1, Marco Aurélio 1.

Por parte: 1 → 5; 2 → 3; 3 → 9; 4 → 5; 5 → 16; 6 → 3; 7 → 5; 8 → 6; 9 → 6.

## Núcleo forte (recomendação, se for preciso cortar)

Parte 1: `xenofonte-apol-1`, `quintiliano-instituicao-11-1-9-11`, `epicteto-diatribes-3-23-25-26`.
Parte 2: `seneca-vida-feliz-27` (e `eliano-historia-varia-2-13` para as notas).
Parte 3: `xenofonte-apol-14-15`, `cicero-academica-1-16`, `aristoteles-metafisica-1-6`,
`plutarco-contra-colotes-18` (crítica epicurista e resposta), `plutarco-contra-colotes-20`.
Parte 4: `aristoteles-retorica-3-18`, `aristoteles-etica-7-2` (crítica), `epicteto-diatribes-2-5-18-20`.
Parte 5: `epicteto-diatribes-1-9-22-24`, `epicteto-diatribes-1-29-16-18`, `seneca-constancia-7-3-4`,
`cicero-divinatione-1-122`, `apuleio-deus-socrates-19`, `plutarco-genio-socrates-20`,
`marco-aurelio-7-66` (crítica).
Parte 6: `xenofonte-mem-4-4-4`, `epicteto-diatribes-3-24-60-61`.
Parte 7: `cicero-de-oratore-1-231-233`, `xenofonte-apol-23`.
Parte 8: `epicteto-diatribes-2-2-8-12`, `maximo-tiro-3-8`.
Parte 9: `xenofonte-apol-4-5`, `cicero-divinatione-1-124`, `cicero-tusculanas-1-99`,
`plutarco-contradicoes-estoicos-37`.

## Onde Xenofonte diverge de Platão (útil para as notas)

- Oráculo: «ninguém mais livre, mais justo, mais sensato» (Apol. 14), não «mais sábio» (21a).
- Sinal divino: «voz de deus que indica o que devo fazer» (Apol. 12; Mem. I 1, 4: manda fazer e não
  fazer); em Platão só desvia (31d). O sinal se opôs ao preparo da defesa (Apol. 4; Mem. IV 8, 5);
  em Platão o silêncio do sinal no dia do julgamento é o argumento (40a–c).
- Contraproposta: recusou-se a propor qualquer pena (Apol. 23); em Platão propõe o Pritaneu e,
  depois, trinta minas (36b–38b).
- Arginusas: Xenofonte faz de Sócrates o epistates, presidente da assembleia (Mem. I 1, 18 e IV 4,
  2); Platão diz só que sua tribo tinha a pritania (32b).
- Profecia final: dirigida a Ânito e ao filho dele (Apol. 29–31), não aos juízes em geral (39c–d).
- O próprio Xenofonte julga que a altivez de Sócrates no tribunal provocou a inveja e a condenação
  (Apol. 32); Platão não diz isso.

## O que não existe ou não rendeu

- **Não há comentário antigo corrido da Apologia.** Nos corpora consultados não aparece nenhum, e
  os neoplatônicos (Proclo, Olimpiodoro, Hérmias) só a citam de passagem, em comentários a outros
  diálogos. Pelo que se sabe do currículo neoplatônico (o cânon de doze diálogos de Jâmblico), a
  Apologia não era lida em aula; não conferi isso numa fonte antiga.
- Aulo Gélio: nada sobre a Apologia (só Xantipa, a resistência física de Sócrates, Fédon escravo, e
  uma «sentença» de Sócrates tirada do Górgias em XII, 9, 6).
- Valério Máximo: só anedotas que repetem outros (ver pistas).
- Marco Aurélio, VII, 44–46: transcreve 28b e 28d (e Górgias 512d–e) sem comentário: só citação.
- Máximo de Tiro, Dissertações 8–9 (sobre o *daimonion*): genéricas; ficaram de fora.
- Simplício, comentário ao Manual de Epicteto (cap. 53, «Ânito e Meleto podem matar-me»): as cópias
  do archive.org (Schweighäuser 1800) não têm o grego no OCR; não consultado.
- Plotino, Porfírio, Jâmblico, Damáscio: não procurei sistematicamente (não estão nos corpora
  baixados); nada encontrado por busca indireta.

## Pistas não usadas (todas lidas no original; podem virar achados)

Xenofonte: Apol. 26 (Palamedes, 41b); Apol. 27–28 (Apolodoro: «queria me ver morrer justamente?»);
Apol. 32 (a altivez atraiu a inveja); Mem. I 1, 1–2 (o texto da acusação e o *daimonion* como origem
das «novas divindades», 24b–c e 31d); I 1, 11–16 (não discutia a natureza, 19c–d); I 1, 18 e IV 4,
2 (Arginusas, 32b); IV 4, 3 (os Trinta, 32c–d); I 2, 32–38 (Crítias e Cáricles proíbem-no de falar
com os jovens; o mau vaqueiro, cf. 25a–b); I 2, 62–64 (merecia honra, não morte, cf. 36d); IV 8,
4–10 (repete Apol. 2–9).
Aristóteles: Retórica II 23, 8 (1398a15: o *daimonion* é deus ou obra de deus, 27c–e); II 23, 13
(«o Sócrates de Teodectes»: em que templo foi ímpio?); Metafísica XIII 4, 1078b17–30;
Ética III 8, 1116b4 e VI 13, 1144b17–30 (virtude como ciência).
Cícero: Tusc. I 97–98 (tradução de 40c–41c); Tusc. V 10–11 (Sócrates trouxe a filosofia do céu,
19c); De or. I 233 (condenado «por não saber falar», crítica de Crasso aos filósofos);
Acad. I 44–45 (Arcesilau nega até o «sei que nada sei», crítica); Lucullus 15 (Luculo/Antíoco: a
ignorância socrática é ironia) e 74 (Cícero: é sincera; ironia perpétua não se sustenta) — par muito
bom para 21d, só não entrou por excesso na parte 3.
Quintiliano: II 15, 29–30 (Lísias; Platão escreveu a defesa de Sócrates); V 11, 42 (o oráculo como
testemunho divino); IX 2, 46 (a vida de Sócrates como ironia contínua, «agens imperitum et
admiratorem aliorum tamquam sapientium», bom para 21b–22e).
Valério Máximo: 3, 4, ext. 1 (oráculo, filosofia moral); 3, 8, ext. 3 (Arginusas); 6, 4, ext. 2
(Lísias: «maluit Socrates extingui quam Lysias superesse»).
Sêneca: Ep. 71, 7 (paráfrase de 41d); Ad Helviam 13, 4 (entrou na prisão com o rosto com que
enfrentou os Trinta); De tranq. 5, 1–3 (Sócrates livre entre os Trinta; a liberdade não suportou a
sua liberdade); De const. 18, 6 (riu da comédia); Ep. 24, 4; 28, 8; 70, 9; De prov. 3, 12 (mais
Críton e Fédon).
Epicteto: III 1, 19–20 (o posto dado pelo *daimonion*; parecido com I 9); IV 1, 123 (quem se saiu
mal foram os juízes e acusadores, 41d); IV 1, 159–169 (Leão de Salamina, recusa de fugir; «salva-se
morrendo»); IV 7, 30–31 (Leão: «procure outro»); III 23, 22 e IV 8, 22–23 (nunca disse «sei e
ensino», 33a–b); I 26, 18 e III 12, 15 (só citam 38a); Manual 53 (só citação de 30c–d).
Musônio: entrou só a diatribe 10.
Dião: Discurso 13, 14–16 (a exortação de Sócrates, do Clitofonte, perto de 29d–30b).
Plutarco: De tranquillitate 17, 475e (Sócrates disse a Ânito e Meleto o que na verdade dizia à
fortuna, 30c–d); De genio 11, 580f–581c (teoria megárica do espirro, rejeitada) e 12, 582b–c (por
que o chamava *daimonion*); Quomodo adulator 72a (refutava os jovens como quem não está livre
da ignorância); [Plutarco], Consolação a Apolônio 12–13, 107d–108e (paráfrase de 40c–e com uma
terceira hipótese, a destruição da alma, e citação de 29a; obra de autoria duvidosa).
Diógenes Laércio: II 37–39 (o oráculo em trímetro, «de todos os homens Sócrates é o mais sábio»; os
três acusadores, cada um por um grupo, cf. 23e; o discurso de Polícrates); II 40–41 (recusa do
discurso de Lísias); II 35 (à mulher: «queria que eu morresse justamente?»); II 46 (epigrama).
Luciano: Diálogos dos mortos 20, 4–6 (Sócrates no Hades com Nestor e Palamedes; «eu dizia que nada
sabia, e eles achavam que era ironia», 38a e 41b).
Juliano: Aos cínicos incultos 181a (Sócrates julgava não saber se a morte é um mal, 29a) e 191a–b
(«serviço ao deus» no exame do oráculo, 23b–c: usa a mesma palavra, λατρεία).
Libânio: Apologia de Sócrates (Declamação 1, ed. Foerster): declamação inteira em defesa de
Sócrates, posta na boca de um amigo; só pista, como pedia o briefing.
Apuleio, Apologia 27: o *daimonion* de Sócrates entre as coisas tidas por magia; só eco.
Proclo, In Alc., Creuzer t. 1, p. 79 (aprox.): por que Sócrates chama o seu daimon de deus.
Hérmias, In Phaedrum (sobre 242b), ed. Couvreur: por que o sinal só detém («para que Sócrates não
fosse como um ser sem razão, movido por outro») e citação de Plotino («no primeiro livro Das dificuldades sobre a
alma», isto é, Enéadas IV, 3) sobre as vozes dos daimones. O OCR está ruim demais para transcrever com segurança; vale conferir na imagem.

## Dúvidas e cuidados

- **Proclo e Olimpiodoro** (`proclo-*`, `olimpiodoro-*`): transcritos do OCR do archive.org, com
  correções minhas onde o OCR errou (marcadas no original entre colchetes). A paginação de Creuzer
  foi inferida dos números de página no OCR e pode estar uma página fora. Em Olimpiodoro, a primeira
  citação da Apologia (30d) vem alterada (Creuzer já nota que ele cita de memória), e a palavra que
  li como ἄρχεσθαι é incerta. Conferir na imagem antes de publicar.
- Diógenes Laércio II, 41: «281 votos a mais» é a lição dos manuscritos, tida por corrupta.
- Eliano, II, 13: a encomenda das Nuvens por Ânito não tem valor histórico; serve para as notas.
- Epicteto, II, 5, 18, troca Meleto por Ânito no interrogatório de 27b–d.
- Máximo de Tiro: numeração de Hobein (Dübner entre parênteses no `passagem`). Na Dissertação 3, 8 a
  primeira palavra da «acusação» falta no texto digital; supri ‹Ἡ›.
- Élio Aristides, Discurso 45 Dindorf (= 2 Behr): o Perseus divide pelas páginas de Jebb (21–22).
- Luciano, Diálogos dos mortos: numeração do Perseus (Jacobitz); outras edições numeram diferente.
- Cícero: no De oratore fala Crasso; no De divinatione I fala o irmão Quinto (Cícero rebate a
  adivinhação no livro II); nos Academica fala Varrão. Está anotado no campo `sobre`.
- Marco Aurélio VII, 66 é crítico no sentido de relativizar os feitos famosos, não de condenar
  Sócrates.
