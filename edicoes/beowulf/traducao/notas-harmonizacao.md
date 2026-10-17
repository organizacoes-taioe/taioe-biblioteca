# Harmonização do poema inteiro (cantos I–XLIII e Finnsburh)

Os cantos III–XLIII e o fragmento de Finnsburh foram traduzidos em nove lotes paralelos, pelo
`PROMPT-CONTINUACAO.md` (apagado depois de concluída a tradução; fica no histórico do git); cada lote tem as suas notas (`notas-03-07.md` … `notas-39-43.md`). Depois
dos lotes, o coordenador conferiu o conjunto e harmonizou o que os tradutores deixaram em aberto.

## Conferência geral

Para os 44 arquivos: número de versos igual ao do original, nenhuma linha em branco no meio,
nenhuma tabulação, nenhuma mesóclise, título do § 8 do guia no cabeçalho e aspas das falas
pareadas dentro de cada arquivo, com as falas que atravessam seções fechadas no fim de um arquivo e
reabertas no começo do seguinte (guia, § 6). Resultado: nenhum problema.

## Decisões

- **Aspas**: a fala de Beowulf (09 → 10) não fechava no fim do 09; fechada.
- **Javali do elmo**: _eofor_, _swȳn_, _swīn_ → «javali»; _ferh_ e, no par _swȳn … eofer_ de 1111–1112,
  a segunda palavra → «varrão» (para variar sem cair em «suíno», que se lê como porco).
- **_gold-wine_** → «amigo de ouro» em todo o poema (34 e 35 tinham «amigo do ouro»).
- **_Sige-Scyldingas_** → «Scyldings vitoriosos» (10 tinha «Scyldings da vitória»).
- **_on þǣm dæge þysses līfes_** (791 e 807) → «naquele dia, aqui nesta vida».
- **_þearf_, _nīed_** → «necessidade» ou «aperto», nunca «precisão», que no Brasil se lê como
  «exatidão» (23, 35, 36, 37).
- **_gār_ em 2441**: é a flecha de Hæthcyn (_flāne_, _horn-bogan_ nos versos anteriores) → «dardo»;
  a regra «gār → lança» do guia vale nos outros lugares.
- **Nomes de Deus** novos, aceitos: o Soberano de tudo (_al-wealda_, _anwealda_), o Pastor da glória
  (_wuldres hyrde_, com maiúscula, como os outros nomes de Deus), o Dono (_āgend_), o Rei verdadeiro
  (_sōð-cyning_). Em 666 (_kyninga wuldor_) → «Deus, a glória dos reis», para não parecer alegoria.
- **Guardas**: «o vigia» só para o vigia da costa (guia, § 9); _hȳð-weard_, _bāt-weard_ → «o guarda
  do porto», «o guarda do bote».

## Críticas aplicadas pelo coordenador

As críticas dos lotes 08–12 e 35–38 chegaram depois que os tradutores tinham entregado; o
coordenador as aplicou e mediu de novo cada verso mudado no `verso-livre.mjs` (nenhum marcado):

- **08–12**: 10 itens, 9 aceitos (sujeitos invertidos em 715–716, 762; regência em 474–476, 489–490,
  527–528, 594–595; comparação em 543; vigia em 668–669; «Glória dos reis» em 666; mais «famoso»
  por «famigerado» em 763 e «mas» por «pois» em 695). Recusado: «reino rico em joias» em 466, porque
  o glossário liga _gimme-rīce_ a _hord-burh_ («a cidadela … rica em joias»).
- **35–38**: 15 itens, 14 aceitos (ordem e sujeito em 2502–2505, 2525–2526, 2543, 2693, 2706,
  2721–2724, 2778–2780; «Hygelac» explícito em 2491; «fazer mal» por «perseguir» em 2467; «de modo
  que» em 2680; «muito perto» em 2729; «precisão» → «necessidade»). Recusado: 2618, onde «seu
  próprio parente» já remete a Onela, sujeito do verso anterior.

## Propostas para o guia (recolhidas das notas dos lotes)

- Antes de genitivo plural, «dinamarqueses» deixa cinco átonas seguidas: usar o adjetivo
  («dinamarquesa», «dinamarquês») ou mudar a ordem, sem trocar o termo (notas-03-07, § 7;
  notas-27-30).
- Acrescentar ao § 5: _sinces brytta_ → o doador de tesouro; _hlǣw_, _beorh_ → túmulo (monte);
  _hornas_ (do salão) → galhadas; _āgend_ → o Dono; _sōð-cyning_ → o Rei verdadeiro.
- Substituir o § 2 pela regra do verso livre (ver `notas.md`, § 6).

## Publicação

Em 16/10/2026 a tradução em verso livre substituiu no site a tradução aliterativa: a pasta
`teste-verso-livre/` passou a ser `traducao/` (a que o `ferramentas/traducoes.py` publica), e a
tradução anterior, com cesura e aliteração, foi guardada em `../traducao-aliterativa/`, com as suas
notas, fora do site.
