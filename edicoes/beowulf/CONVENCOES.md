# Beowulf — convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md` (regras gerais da Biblioteca). Este guia acrescenta o
específico e prevalece onde for mais preciso. Texto-fonte: `original/` (ver `original/LEIAME.md`).

## 1. O que se traduz

O poema inteiro, verso a verso, do inglês antigo da edição Harrison e Sharp (4.ª ed., 1894), e o
fragmento de Finnsburh que a edição traz em apêndice. **Um verso traduzido para cada verso do
original, na mesma ordem**: no site, cada verso português fica na altura do seu par em inglês antigo.
Não se traduzem os títulos ingleses das seções (o `# titulo-edicao`); cada arquivo traduzido leva o
título português da tabela do § 8.

## 2. O verso: verso livre, verso a verso

A tradução publicada (`traducao/`) é em **verso livre** (desde outubro de 2026; a tradução anterior,
que guardava a cesura e a aliteração do original, está em `traducao-aliterativa/`, fora do site).

1. **Sem cesura**: nenhuma tabulação nos arquivos traduzidos; o verso corre inteiro.
2. **Sem imitar a medida do original** (dois tempos por meio-verso, aliteração). O ritmo é o do bom
   verso livre português, conferido pelo Versificador (`Solar\Editora\Versificador`):
   `ferramentas/verso-livre.mjs` sem nenhum verso marcado (`ralo`, `vazio`, `choques`), de 2,4 a 2,8
   sílabas por acento forte, no máximo um verso em cinco com 4 átonas seguidas, nada de três vogais
   iguais seguidas, sem repetir o mesmo esqueleto em versos vizinhos; `ferramentas/molde.mjs`, em molde
   livre (`*`) com `# troca` para a pronúncia dos nomes, sem ✗, ≠ nem «leitura natural tem». Método e
   números: `traducao/notas.md`, § 4.
3. **Sem rima** (rima seria acréscimo).
4. **Sentido verso a verso.** O que está no verso N do original fica no verso N da tradução. A sintaxe
   portuguesa pode pedir que uma palavra passe ao verso vizinho, dentro da mesma frase: aceitável, mas
   raro, e nunca uma ideia inteira. As **aposições** ficam todas, no lugar delas: são a alma do estilo.
5. **Clareza**: sujeito explícito quando um pronome deixaria dúvida (às vezes o nome, que o original
   dá por subentendido); comparações completas; nenhuma aposição truncada.
6. **«dinamarqueses»** depois de preposição pode deixar cinco átonas seguidas: use o adjetivo
   («dinamarquesa», «dinamarquês») ou mude a ordem, sem trocar o termo.

Versos-modelo (I, 1–11):

```
Escutai! Dos dinamarqueses da lança, nos dias de outrora,
dos reis do povo ouvimos a glória,
e como os príncipes deram provas de bravura.
Muitas vezes Scyld Scefing, às hostes inimigas,
a muitas linhagens, tomou os bancos de hidromel;
aterrou os nobres, depois que no princípio
foi achado desamparado; disso teve consolo:
cresceu sob as nuvens, prosperou em honras,
até que cada um dos povos vizinhos,
além do caminho da baleia, teve de obedecer-lhe
e pagar-lhe tributo: aquele era um bom rei!
```

## 3. Registro

- Português do Brasil literário, sóbrio e forte; solene sem ser empolado. Vocabulário concreto
  (espada, escudo, salão, mar, sangue), frase que avança por aposições. Nada de arcaísmo de fantasia
  («vós sois mui valoroso»), nada de modernismo («ok», «gente»).
- **Kennings e compostos**: traduza a imagem, não a explicação: _hron-rād_ → caminho da baleia;
  _bān-hūs_ → casa dos ossos; _beado-lēoma_ → luz da batalha (a espada); _sǣ-wudu_ → madeira do mar
  (o navio); _hilde-lēoma_ → luz de combate; _word-hord_ → tesouro de palavras; _bēag-gyfa_ → doador
  de anéis. Se o composto pesar demais no meio-verso, use a forma com «de» mais curta possível, mas
  não troque por «navio», «espada».
- **Fórmulas** repetidas se traduzem sempre do mesmo modo:
  - _Bēowulf maþelode, bearn Ecgþēowes_ → `Beowulf falou,	o filho de Ecgtheow:`
  - _Hrōðgār maþelode, helm Scyldinga_ → `Hrothgar falou,	o elmo dos Scyldings:`
  - _Wīglāf maðelode_ … → `Wiglaf falou, …`; _maþelode_ em geral → «falou».
  - _Hwæt!_ no começo do poema → «Escutai!»; dentro de uma fala → «Ora!» ou «Vede!» (vós), «Vê!» (tu).
  - _Ic þæt gefrægn_, _mīne gefrǣge_ → «ouvi dizer», «pelo que ouvi».
  - _þā wæs_ … («então foi …») e _swā sceal_ … («assim deve …») sem enfeite.
  - _gōd cyning_ → bom rei; _frēawine folca_ → senhor amigo do povo; _wine Scyldinga_ → amigo dos
    Scyldings; _eodor Scyldinga_ → proteção dos Scyldings; _folces hyrde_ → pastor do povo;
    _helm Scyldinga_ → elmo dos Scyldings.
- **Tratamento**: _þū_ → **tu** (verbo na 2.ª do singular), também com o rei; _gē_ → **vós**; dual
  _wit_, _unc_, _incer_ → nós dois, a nós dois, de vós dois. **Nunca mesóclise.**
- **Deus**: o poeta é cristão e fala de Deus com muitos nomes; guarde a variedade e a maiúscula:
  _god_ (Deus) → Deus; _drihten/dryhten_ (Deus) → o Senhor; _metod_ → o Criador (_metodsceaft_ →
  decreto do Criador); _wealdend_ → o Soberano; _fæder_ → o Pai; _scyppend_ → o Criador (se _metod_
  e _scyppend_ estiverem juntos: _metod_ → o Ordenador); _ælmihtig_ → o Todo-Poderoso; _wuldor-cyning_
  → o Rei da glória; _līf-frēa_ → o Senhor da vida; _wuldres wealdend_ → o Soberano da glória. Pronome
  de Deus com minúscula (ele, seu), como no original. _wyrd_ → o destino (minúscula).
- Senhor humano: _dryhten, frēa, þēoden, hlāford_ → senhor (ou «rei», quando o verso pede).

## 4. Nomes

**Pessoas**: a forma do inglês antigo sem mácron, com **th** para _þ_ e _ð_, **æ** mantido; nominativo
sempre (sem as desinências de caso). Beowulf, Grendel, Scyld Scefing, Healfdene, Heorogar,
Hrothgar, Halga, Wealhtheow, Hrethric, Hrothmund, Hrothulf, Freawaru, Ingeld, Froda, Unferth
(filho de Ecglaf), Æschere, Yrmenlaf, Wulfgar, Ecgtheow, Hrethel, Herebeald, Hæthcyn, Hygelac, Hygd,
Hæreth, Heardred, Breca, Beanstan, Sigemund, Wæls, Fitela, Heremod, Finn, Folcwalda, Hildeburh,
Hnæf, Hengest, Guthlaf, Oslaf, Hunlafing, Eormenric, Hama, Offa, Eomer, Garmund, Hemming, Thryth,
Wiglaf, Weohstan, Ælfhere, Ongentheow, Onela, Ohthere, Eanmund, Eadgils, Eofor, Wulf, Wonred,
Dæghrefn, Withergyld, Ecgwela, Swerting, Cain → **Caim**, Abel.

**Povos e linhagens**: forma portuguesa quando há uma usual, com minúscula: Dene → **dinamarqueses**
(_Gār-Dene_ → dinamarqueses da lança; _Hring-Dene_ → dinamarqueses dos anéis; _Beorht-Dene_ →
dinamarqueses radiantes; _Ēast-Dene, West-Dene, Sūð-Dene, Norð-Dene_ → dinamarqueses do leste, do
oeste, do sul, do norte); Gēatas → **geatas** (_Gūð-Gēatas_ → geatas guerreiros; _Sǣ-Gēatas_ → geatas
do mar; _Weder-Gēatas_ → wedergeatas); Wederas → **wederas**;
Swēon → **suecos**; Frēsan → **frísios**; Francan → **francos**; Hūgas → **hugos**; Hetware →
**hetwaros**; Ēotenas (no episódio de Finnsburh) → **jutos**; Wendlas → **vândalos**; Gifðas →
**gépidas**; Heaðo-Beardan → **heatobardos**. Linhagens em _-ingas_, com maiúscula, na forma
inglesa usual: **Scyldings**, **Scylfings**, **Wylfings**, **Brondings**, **Wægmundings**,
**Hrethlings** (singular: um Scylding, o Wægmunding). _Ingwine_ → amigos de Ing.

**Lugares, coisas com nome**: Heorot (o salão); Hrunting e Nægling (as espadas); _Brōsinga mene_ → o
colar dos Brosings; Finnsburh; Frísia (_Frēsland_); Scedeland (_Scede-landum_, _Scedenig_);
Earnanæs; Hrefnesholt, Hrefnawudu; Hreosnabeorh; Hronesnæs; _Swīo-rīce_ → o reino dos suecos.

## 5. Termos

| inglês antigo | português |
|---|---|
| _heall, sele, reced, ærn_ | salão (casa, morada, quando o verso pede variação) |
| _medu, medo-_ | hidromel; _meodo-setl_ → banco de hidromel; _medu-heall_ → salão do hidromel |
| _bēor, ealu_ | cerveja; _bēor-sele_ → salão da cerveja |
| _hring, bēag_ | anel (bracelete, se for de braço) |
| _hord, gestrēon, mādm, sinc, frætwe_ | tesouro, riquezas, joias, ouro lavrado, adornos |
| _draca_ | dragão; _wyrm_ → serpe; _lyft-floga_ → voador do ar |
| _eoten, ent, þyrs, scucca, gǣst_ | gigante, gigante (obra de gigantes: _enta geweorc_), ogro, demônio, espírito (ou hóspede: _gæst/gǣst_ são ambíguos; siga o glossário da edição) |
| _āglǣca_ | o temível (o terror) — vale para Grendel, o dragão **e** Beowulf |
| _eorl, æðeling, hæleð, guma, rinc, secg, beorn, wer, cempa, wīgend_ | nobre, príncipe, herói, homem, guerreiro, varão, guerreiro, homem, campeão, combatente (varie) |
| _þegn_ | vassalo; _magu-þegn_ → jovem vassalo; _heorð-genēatas_ → companheiros da lareira |
| _dugoð / geogoð_ | os veteranos / os jovens |
| _gesīð, wine_ | companheiro, amigo |
| _scop, glēo-mann_ | poeta, menestrel; _hearpe_ → harpa; _gid, lēoð_ → canção, balada |
| _byrne, hring-net, searo_ | cota de malha, rede de anéis, arnês |
| _helm, eofor-līc_ | elmo, figura de javali |
| _bord, lind, scyld_ | escudo, escudo de tília |
| _gār, æsc, spere_ | lança, freixo (lança) |
| _sweord, mēce, bill, ecg, īren_ | espada, espada, lâmina, gume, ferro |
| _ceol, flota, naca, bāt_ | quilha, barco, nau, bote |
| _wergild, fǣhð_ | preço de sangue (_wergild_ em itálico, na primeira vez), contenda, vingança |
| _bēot, gylp_ | juramento de façanha, jactância |
| _dōm, lof, ellen_ | glória, fama, coragem |
| _sāwol, ferhð, mōd, sefa, hyge_ | alma, espírito, ânimo, coração, mente |
| _middan-geard_ | a terra-média |
| _hǣðen_ | pagão |

## 6. Tipografia

- Aspas: as do português, “...”, com ‘...’ dentro. **Uma fala abre as aspas no verso em que começa e
  fecha no verso em que acaba**; os versos do meio não levam aspas (o `"` no começo de cada linha
  do original é uso tipográfico antigo, ver `original/LEIAME.md`).
- **Fala que atravessa duas seções** (o canto de Finnsburh, o discurso de Hrothgar, o relato de Beowulf a
  Hygelac, a fala do mensageiro): as aspas fecham no último verso de
  um arquivo e reabrem no primeiro do seguinte (cada página do site é lida por si).
- Parênteses do original (incisos dos editores) → parênteses na tradução, no mesmo verso.
- Lacunas `. . .` → `. . .` na tradução, no mesmo lugar do verso; traduza só as palavras legíveis, sem
  completar o que o manuscrito perdeu. `(?)` → `(?)`.
- Maiúscula no começo de frase, não no começo de verso.
- Itálico só para palavra que fica em outra língua (_wergild_).

## 7. Formato

`traducao/01.txt` ... `traducao/43.txt` e `traducao/finnsburh.txt`, cada um com:

```
# canto: I
# titulo: A partida de Scyld

Escutai! Dos dinamarqueses da lança, nos dias de outrora,
...
```

Depois do cabeçalho, uma linha em branco e os versos, **um por linha, sem linhas em branco no meio**,
o mesmo número de linhas do original. Conferência (tem de sair «ok»):

```
python edicoes/beowulf/conferir.py 01 02 03
```

O `conferir.py` confere o título, o número de versos, linhas em branco, tabulação, aspas (as falas que
atravessam seções fecham no fim de um arquivo e reabrem no seguinte) e mesóclise. O ritmo se confere
com o Versificador (§ 2).

## 8. Títulos das seções

Os títulos ingleses são de Harrison e Sharp; os portugueses os traduzem.

| | arquivo | título |
|---|---|---|
| I | 01 | A partida de Scyld |
| II | 02 | O salão Heorot |
| III | 03 | As visitas de Grendel |
| IV | 04 | O vassalo de Hygelac |
| V | 05 | A missão |
| VI | 06 | A fala de Beowulf |
| VII | 07 | As boas-vindas de Hrothgar |
| VIII | 08 | Hrothgar fala de Grendel |
| IX | 09 | Unferth provoca Beowulf |
| X | 10 | A disputa de Beowulf com Breca. O banquete |
| XI | 11 | A vigília à espera de Grendel |
| XII | 12 | O ataque de Grendel |
| XIII | 13 | Beowulf arranca o braço de Grendel |
| XIV | 14 | A alegria em Heorot |
| XV | 15 | O louvor de Hrothgar |
| XVI | 16 | O banquete e os presentes |
| XVII | 17 | O canto do poeta de Hrothgar: a balada de Hnæf e Hengest |
| XVIII | 18 | Termina a história do menestrel |
| XIX | 19 | O colar de Beowulf. Os heróis repousam |
| XX | 20 | A mãe de Grendel ataca os dinamarqueses dos anéis |
| XXI | 21 | Luto em Heorot: a morte de Æschere |
| XXII | 22 | Beowulf busca o monstro no covil das feras das águas |
| XXIII | 23 | A batalha com o dragão das águas |
| XXIV | 24 | Beowulf mata o espectro |
| XXV | 25 | A gratidão de Hrothgar. O discurso do rei |
| XXVI | 26 | Fim do discurso. Beowulf se prepara para partir |
| XXVII | 27 | As palavras de despedida |
| XXVIII | 28 | Beowulf volta à terra dos geatas. As rainhas Hygd e Thryth |
| XXIX | 29 | A chegada. Hygelac recebe Beowulf |
| XXX | 30 | Beowulf conta os combates |
| XXXI | 31 | Os presentes a Hygelac. A recompensa. A morte de Hygelac. Beowulf reina |
| XXXII | 32 | O dragão de fogo. O tesouro |
| XXXIII | 33 | Beowulf decide matar o dragão de fogo |
| XXXIV | 34 | Beowulf relembra. A guerra entre suecos e geatas |
| XXXV | 35 | Memórias do passado. O combate com o dragão de fogo |
| XXXVI | 36 | Wiglaf socorre Beowulf no combate |
| XXXVII | 37 | Beowulf ferido de morte |
| XXXVIII | 38 | O tesouro de joias. A partida de Beowulf |
| XXXIX | 39 | Os vassalos covardes |
| XL | 40 | O lamento e a profecia do mensageiro |
| XLI | 41 | O relato dos suecos e dos geatas |
| XLII | 42 | Wiglaf fala. A construção da pira |
| XLIII | 43 | A pira de Beowulf |
| Apêndice | finnsburh | O combate em Finnsburh (fragmento) |

## 9. Decisões da tradução (harmonização)

Tomadas pelos tradutores e conferidas no poema inteiro:

- _gæst_ (vogal breve, «estranho») → hóspede (_gryre-gæst_ → hóspede do horror; _inwit-gæst_ → hóspede
  hostil); _gāst/gǣst_ (espírito) → espírito (_ellor-gǣst_ → espírito estranho); _wæl-gǣst_ → espírito
  da matança.
- _nicor_ → monstros das águas; _orcnēas_ → monstros marinhos; _gīgantas_ → gigantes. _eotenas_ fora do
  episódio de Finnsburh (903) → gigantes, como na edição; no episódio, com maiúscula na edição → jutos.
- _beorh, hlǣw_ → túmulo (monte, quando é o lugar da pira); _segn_ → estandarte; _bǣr_ → esquife.
- _hlēo_ (de pessoa) → amparo; _þyle_ (Unferth) → o orador; _weard_ (da costa) → o vigia.
- _gifeðe_ → fado; _wyrd_ → destino; _dōm_ → glória, mas juízo em _dōm godes_ (2859).
- Fórmulas: «Wiglaf falou, o filho de Weohstan»; «O vigia falou».
- Nomes novos: Elan, Hoc, Hondscio, Heoroweard, Hereric, Sigeferth, Eaha, Ordlaf, Garulf, Guthere;
  _Merewīoing_ → o merovíngio; _Secgan_ → secgas; Weohstan numa forma só (a edição varia).
- _Hwæt!_ dentro de fala → «Vê!» a quem se trata por tu, «Ora!» quando é exclamação geral.
- Da tradução em verso livre (`traducao/notas-harmonizacao.md`): _eofor_, _swȳn_, _swīn_ (do elmo) →
  javali, e _ferh_ → varrão; _gold-wine_ → amigo de ouro; _Sige-Scyldingas_ → Scyldings vitoriosos;
  _on þǣm dæge þysses līfes_ → naquele dia, aqui nesta vida; _þearf_, _nīed_ → necessidade, aperto
  (nunca «precisão»); _gār_ da flecha de Hæthcyn (2441) → dardo; _sinces brytta_ → o doador de tesouro;
  _hornas_ (do salão) → galhadas; _hȳð-weard_, _bāt-weard_ → o guarda do porto, o guarda do bote.
  Nomes de Deus: o Soberano de tudo (_al-wealda_), o Pastor da glória (_wuldres hyrde_), o Dono
  (_āgend_), o Rei verdadeiro (_sōð-cyning_); _kyninga wuldor_ → Deus, a glória dos reis.

## 10. Notas do tradutor

Cada tarefa grava `traducao/notas-<arquivos>.md` (ex.: `notas-01-05.md`): leituras difíceis e a
interpretação adotada (com o verso); compostos e kennings novos e como ficaram; nomes e termos que
não estão neste guia; lacunas; e o resultado do `conferir.py`. Não altere este guia: proponha
mudanças nas notas.
