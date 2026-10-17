# Teste em verso livre: cantos I e II (versos 1–114)

Tradução nova, do inglês antigo (Harrison e Sharp, 4.ª ed.), em verso livre: um verso português para cada
verso do original, na mesma ordem, sem tabulação de cesura e sem imitar a medida aliterativa. Nomes,
termos, fórmulas e tratamento seguem `../CONVENCOES.md` (§§ 3–9); o § 2 foi posto de lado, como pedido.

## 1. Método

1. Leitura do original com o glossário e as notas de Harrison e Sharp; conferência de cada verso com
   Hall (numeração por seção, a mesma dos nossos arquivos), Gummere e Morris e Wyatt. Nada foi copiado
   dessas versões: elas serviram para conferir a leitura e as passagens disputadas (§ 3).
2. Rascunho verso a verso, procurando a frase portuguesa natural dentro de cada verso.
3. Ritmo pelo Versificador: `ferramentas/molde.mjs` (molde livre, `*`, com `# troca` para a pronúncia
   dos nomes) e `ferramentas/verso-livre.mjs`, que mede o verso livre pelos indicadores do estudo
   (`estudo/metros/verso-livre.md` e `ESTUDO-DO-RITMO.md`, § 3.5 e § 5). Três passadas de reescrita
   (§ 4).
4. Crítica independente de sentido e de língua (manual, passo 8), e revisão dos pontos aceitos (§ 5).

## 2. Escolhas gerais

- **Verso a verso.** Cada verso guarda o que está no seu par em inglês antigo. Onde a sintaxe pediu,
  uma palavra passou ao verso vizinho dentro da mesma frase: v. 68–69 (_men gewyrcean_ → «aos homens»,
  no v. 68); v. 107–110 conservam a ordem do original, com o sujeito (_ēce drihten_, _metod_) no começo
  do verso seguinte, como lá.
- **Aposições** todas no lugar: «o Senhor da vida, / o Soberano da glória» (16–17); «o senhor amado, /
  o doador de anéis, … / o ilustre» (34–36); «os senhores dos salões, / os heróis sob os céus» (51–52);
  «caro rei do povo» (54); «o pai …, / o príncipe» (55–56).
- **Kennings**: _hron-rād_ → caminho da baleia (10); _hringed-stefna_ → a proa anelada (32, a imagem
  do original, sem acrescentar «navio»); _bēaga brytta_ → o doador de anéis (35); _sele-rǣdende_ → os
  senhores dos salões (51; glossário: _hall-ruler_); _ecg-hete_ → o ódio dos gumes (84); _heaðo-wylm_ →
  as ondas hostis do fogo (82–83); _mearc-stapa_ → andarilho das fronteiras (103); _horn-gēap_ → de
  amplas galhadas (82: os chifres de cervo nas empenas, glossário e nota aos vv. 78–83).
- **Nomes de Deus** segundo o guia: Deus (13, 72, 113), o Senhor da vida (16), o Soberano da glória
  (17), o Senhor (_frēan wǣre_, 27, que o glossário dá como «a guarda de Deus»), o Todo-Poderoso (92),
  o Criador (_scyppend_, 106), o Senhor eterno (108), o Ordenador (_metod_, 110, por estar perto de
  _scyppend_). Pronome de Deus em minúscula (114).
- **Termos do guia**: _gæst_ (102, vogal breve) → hóspede; _ellen-gǣst_ (86) → espírito; _eotenas_ e
  _gīgantas_ (112–113) → gigantes; _orcnēas_ → monstros marinhos; _segen_ → estandarte; _gōd cyning_ →
  bom rei; _mōd_ → ânimo; _sefa_ → coração; _middan-geard_ → terra-média; _bill_ → lâmina; _byrne_ →
  cota de malha; _cēol_ → quilha; _geogoð_ → os jovens.
- **Nomes**: Scyld Scefing, Scedeland, Healfdene, Heorogar, Hrothgar, Halga, Elan, Ongentheow,
  Heorot, Grendel, Caim, Abel; _Heaðo-Scilfing_ → o guerreiro Scylfing (63).
- **Hwæt!** → «Escutai!» (1). _Ic wīde gefrægn_ → «ouvi dizer» (74, como no guia); _ne hȳrde ic_ → «nunca ouvi falar» (38); _hȳrde ic_ → «ouvi» (62).

## 3. Passagens revistas (sentido)

| verso | original | leitura adotada | apoio |
|---|---|---|---|
| 6 | _Egsode eorl_ | «aterrou os nobres»: _egsian_ ativo, «aterrorizar» | H&S, nota ao v. 6. O glossário dá também o intransitivo («o nobre teve terror», como Hall); preferi o ativo, que Gummere segue e que liga melhor com os vv. 4–5. |
| 7 | _hē þæs frōfre gebād_ | «disso teve consolo»: consolo pelo desamparo do v. 7 | glossário; Hall, Gummere |
| 13 | _geong in geardum_ | «jovem no seu lar» | Hall _dwelling_, Gummere _halls_ |
| 14 | _fyren-þearfe ongeat_ | «pois vira a dura aflição»; sujeito: Deus, do v. 13 (o «pois» e o mais-que-perfeito tiram a dúvida sobre quem viu) | glossário: _misery through the malignity of enemies_; nota ao v. 15 (Sievers: _God had seen the dire need_) |
| 18–19 | _Bēowulf … Scede-landum in_ | «em Scedeland»; Beowulf é o filho de Scyld (o Beow das genealogias), não o herói | nota ao v. 18 |
| 20 | _gōde gewyrcean_ | «agir com largueza» (com bens, com dádivas); o v. 21 diz quais | Hall _by kindnesses rendered_ |
| 21 | _on fæder wine_ | «aos amigos do pai»: _wine_ plural | nota ao v. 21 |
| 22–24 | _þæt hine … gewunigen wil-gesīðas … lēode gelǣsten_ | «para que … o acompanhem / companheiros dispostos … / e o povo o sirva» | glossário (_gelǣstan_: prestar serviço na guerra) |
| 27 | _fela-hrōr_ | «cheio de vigor» | glossário: _very active_ |
| 30–31 | _þenden wordum wēold … lange āhte_ | «enquanto ainda dava ordens o amigo dos Scyldings, / o amado príncipe da terra, que longo tempo reinou» | nota ao v. 31 e glossário (_āgan_ com _geweald_ subentendido, tirado de _wordum wēold_); a passagem é disputada (Kluge: _lǣndagas_) |
| 33 | _īsig and ūtfūs_ | «coberta de gelo, pronta a partir» | glossário (_ūt-fūs_: _ready to go_) |
| 43–46 | _Nalas … lǣssan lācum … þonne þā dydon_ | «De modo algum o proveram de dádivas menores … do que os presentes daqueles / que no começo da vida o mandaram partir» | a comparação fica explícita (presentes de agora × presentes de antes); _æt frumsceafte_ = ao nascer (glossário) |
| 51 | _sele-rǣdende_ | «os senhores dos salões» | glossário; nota ao v. 51 (a outra lição, _sēle-rǣdenne_, daria «o decreto do destino») |
| 52 | _hlæste_ | «aquela carga» (o navio e o que levava) | glossário |
| 53 | _on burgum_ | «nas cidadelas» | glossário _burh_ |
| 57 | _hēold þenden lifde_ | «regeu, a vida inteira» | |
| 59–60 | _forð-gerīmed … weoroda rǣswan_ | «um após outro … ao chefe das hostes» (dativo: Healfdene) | glossário (_in unbroken succession_; _rǣswa_ dat. sg.); nota ao v. 60 (Heyne-Socin refere a Heorogar) |
| 62–63 | _Elan cwēn Ongenþēowes … heals-gebedde_ | «Elan foi a rainha de Ongentheow, / do guerreiro Scylfing, a querida esposa» | texto da edição; Bugge (nota ao v. 62) lê _[On]elan cwēn_, e as edições modernas fazem dela rainha de Onela. Não se emenda. |
| 64 | _here-spēd_ | «êxito na guerra» | glossário: _luck in war_ |
| 69–70 | _medo-ærn micel … þone yldo bearn ǣfre gefrūnon_ | «uma grande casa do hidromel, / como nunca os filhos dos homens tinham ouvido falar» | nota ao v. 70 (_þone_ = _þonne_, «do que», com sentido de comparativo); a frase portuguesa diz o superlativo sem forçar «maior do que». |
| 73 | _būton folc-scare and feorum gumena_ | «menos a terra do povo e as vidas humanas» | nota ao v. 73 (_folk-share_: a terra comum) |
| 79 | _sē þe his wordes geweald wīde hæfde_ | «aquele que tinha, por toda parte, o poder da palavra» | |
| 82 | _horn-gēap_ | «de amplas galhadas» | glossário; nota aos vv. 78–83 |
| 83–85 | _ne wæs hit lenge þā gēn, þæt …_ | «e não tardaria a hora / em que o ódio dos gumes entre genro e sogro … havia de despertar» | glossário de _gēn_: _it was not then long before_; _āðum-swerian_ = genro e sogro (nota ao v. 84) |
| 86 | _ellen-gǣst earfoðlīce_ | «o espírito valente, com rancor» | glossário: _ellen-gǣst_ = _demon with heroic strength_; _earfoðlīce_ no v. 86 = _with vexation, angrily_ |
| 88 | _drēam … hlūdne_ | «a festa / ruidosa» | nota ao v. 88 (_drēam_: o rumor da alegria, a música) |
| 95 | _lēoman tō lēohte_ | «luzeiros a dar luz» | |
| 101 | _fēond on helle_ | «um inimigo do inferno» | texto da edição; Bugge e Heyne-Socin leem _on healle_ («no salão», nota ao v. 101) |
| 102 | _se grimma gæst_ | «o hóspede cruel» | nota ao v. 102 (_gæst_ = _stranger_); guia § 9 |
| 104 | _fīfel-cynnes eard_ | «a terra da raça dos monstros» | glossário: _giant-race_; «monstros» para não confundir com _eotenas_ / _gīgantas_ (112–113), que são «gigantes» |
| 106 | _forscrifen hæfde_ | «lhe dera a sentença» | glossário: _to proscribe, condemn_ |
| 109 | _ne gefeah hē þǣre fǣhðe_ | «ele não se alegrou com a contenda»: «ele» é Caim, o mesmo «ele» do v. 108; o segundo _hē_ (_ac hē hine … forwræc_) é o Ordenador, que abre o v. 110, como no original | Gummere; Hall entende o primeiro _hē_ como Deus. |
| 111 | _untȳdras_ | «as crias malditas» | |

## 4. Ritmo: o que o Versificador mostrou e o que mudou

Meta (estudo do verso livre, «Lições para quem traduz»): um acento forte a cada 2,4–2,8 sílabas;
intervalos misturando o binário e o ternário (mestres: 1 → ~15%, 2 → ~30%, 3 → ~29%, 4 → ~16%,
5+ → ~5%); poucos versos com 4 átonas seguidas; a frase fechando junto do verso; nenhuma leitura
natural forçada; não repetir o mesmo esqueleto em versos seguidos.

**Primeiro rascunho** (canto I): 2,77 sílabas por acento, mas 25% dos versos com vãos de 4 átonas ou
mais e três versos marcados como prosa (`ralo`/`vazio`): 3, 20 e 30. Canto II: cinco versos marcados
(56, 57, 64 com choques empilhados, 79, 110).

Reescritas principais (antes → depois):

| verso | antes | depois | por quê |
|---|---|---|---|
| 3 | e como aqueles príncipes provaram o seu valor. | e como os príncipes deram provas de bravura. | 3 acentos em 15 sílabas (prosa) |
| 20–23 | Assim deve o jovem, com generosidade, / … / alcançar que, na velhice, fiquem a seu lado / companheiros de bom grado, quando vier a guerra, | Assim deve o jovem agir com largueza, / … / para que, mais tarde, já velho, o acompanhem / companheiros dispostos, quando a guerra vier, | vão de 7 átonas; frase arrastada |
| 30 | enquanto governava com a palavra o amigo dos Scyldings, | enquanto ainda dava ordens o amigo dos Scyldings, | 4 acentos em 17 sílabas; e o sentido fica mais claro |
| 40 | … no seu regaço jaziam | … no colo dele jaziam | vão; «dele» desfaz a dúvida sobre de quem é o colo |
| 44 | do que fizeram aqueles | do que os presentes daqueles | a comparação fica explícita (o vão de 4 átonas continua, em «do que os pre-», mas a frase o carrega) |
| 46 | quando ainda era criança | criança ainda | verso mais curto, fecho em choque suave |
| 48 | bem alto sobre a cabeça | no alto, sobre a cabeça | choque inútil no começo |
| 56–57 | o príncipe, da sua terra), … / o alto Healfdene; enquanto viveu, governou, | o príncipe deixara a pátria), … / o alto Healfdene; regeu, a vida inteira, | vãos de 5 e 6 átonas; a aposição sem verbo ficava truncada (crítica) |
| 64 | Então foi dado a Hrothgar o êxito na guerra, | Então a Hrothgar foi dado êxito na guerra, | três choques seguidos |
| 79 | aquele cuja palavra mandava por toda parte. | aquele que tinha, por toda parte, o poder da palavra. | 4 acentos em 15 sílabas |
| 86–88 | Então o espírito valente com amargura / … / ouvir a cada dia a alegria | Então o espírito valente, com rancor, / … / ouvir a cada dia a festa | vão de 5 átonas; três vogais seguidas (_dia a alegria_) |
| 91 | contar desde longe a origem dos homens, | contar a origem dos homens, desde longe, | quebra uma série de 2-5-8-11 |
| 106 | depois que o Criador o havia proscrito. | depois que o Criador lhe dera a sentença. | 3 acentos em 12 sílabas; termo mais claro |
| 110 | o Ordenador, por aquele crime, do meio dos homens. | o Ordenador, por causa do crime, do convívio humano. | `ralo` |

**Resultado final** (`verso-livre.mjs`, com a pronúncia dos nomes dada por `# troca`):

| | canto I | canto II | meta |
|---|---|---|---|
| versos | 52 | 62 | = original |
| média de sílabas | 12,4 | 12,3 | |
| sílabas por acento | 2,66 | 2,60 | 2,4–2,8 |
| intervalos 1 / 2 / 3 / 4 / 5+ (%) | 6,8 / 32,6 / 38,9 / 17,9 / 3,7 | 6,5 / 35,9 / 37,2 / 19,0 / 1,3 | ~15 / 30 / 29 / 16 / 5 |
| versos com 4+ átonas seguidas | 13,5% | 4,8% | até 22% |
| versos que terminam em pontuação | 71,2% | 71,0% | 65–100% |
| âncoras métricas (versos que caem num metro) | 9 | 17 | uma ou duas a cada 6–8 versos |
| versos marcados (`ralo`, `vazio`, `choques`) | 0 | 0 | 0 |

`molde.mjs` (molde livre, `*`, com as `# troca`): nenhum ✗, nenhum ≠, nenhuma «leitura natural»
diferente da leitura usada; as fusões que ele faz são as da fala (_vo‿ou_, _to‿a_, _de‿ou_).

O que fica fora da meta, de propósito: o choque (intervalo 1) está abaixo da média dos mestres, e o
ternário acima. O choque é recurso de estrondo em Campos; aqui, num relato solene, ficou só onde a fala
o pede («bom rei», «um após outro», «não sabem»). O ternário alto vem do vocabulário (paroxítonas de
três sílabas: _linhagens_, _companheiros_, _cidadelas_); quebrei as séries de 2-5-8-11 iguais em
versos vizinhos (vv. 91, 106; 63 deixou de ser 2-5-8-11) e deixei o ternário puro em versos de
enumeração («gigantes e elfos e monstros marinhos»), onde ele soa como lista de saga.

## 5. Crítica

Um crítico (Sonnet, esforço médio) conferiu os 114 versos com o original, Hall, Gummere, Morris e Wyatt
e o glossário. Apontou 8 itens; aceitos 6, cada um conferido de novo no `verso-livre.mjs`:

- v. 14, sujeito de «viu» incerto → «pois vira a dura aflição».
- v. 19, «nas terras de Scedeland» redundante → «em Scedeland».
- v. 44, comparação difícil de seguir → «do que os presentes daqueles».
- v. 56, aposição truncada → «o príncipe deixara a pátria)».
- v. 62, «foi de Ongentheow» forçado → «Elan foi a rainha de Ongentheow».
- v. 109, «não lhe deu alegria a contenda» deixava dúvida sobre quem não se alegrou → «ele não se
  alegrou com a contenda».

Recusados:

- v. 86, «com rancor» por _earfoðlīce_: o crítico propôs «a custo», mas o glossário da edição dá, para
  este verso, _with vexation, angrily_ (Hall: _bore it bitterly_; Gummere: _with envy and anger_).
- v. 113, «gigantes» duas vezes (_eotenas_, 112; _gīgantas_, 113): é a regra do guia (§ 9), e o
  original também tem duas palavras para a mesma raça. «Titãs» seria uma glosa.

## 6. Proposta para o guia

Se o verso livre for adotado, o § 2 do guia precisa de um substituto. Sugestão: «um verso para cada
verso; verso livre, sem cesura; conferir com `verso-livre.mjs` (sem verso marcado; 2,4–2,8 sílabas por
acento; no máximo um verso em cinco com 4 átonas seguidas) e com `molde.mjs` em molde livre, com
`# troca` para a pronúncia dos nomes».

## 7. Conferência

- Versos: 52 (1–52) e 62 (53–114), como o original; sem tabulação.
- Grep de mesóclise: nada.
- Cabeçalho igual ao de `traducao-aliterativa/` (`# canto`, `# titulo`).
