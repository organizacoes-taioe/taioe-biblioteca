# A democracia na América (Tocqueville), seleção: convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md`. Texto-fonte e conferência: `original/LEIAME.md`.
Traduz-se o francês da 12ª edição (Pagnerre, 1848), que está ao lado. As decisões em aberto estão no
`revisao.json` (a recomendação já aplicada); quando o Gere responder, a escolha sai de lá e vem para cá.

## Princípio e tom

- Português do Brasil culto e claro, fiel ao movimento da prosa de Tocqueville: períodos amplos e
  equilibrados, antíteses, enumerações em ponto e vírgula, frases curtas de efeito no fim do parágrafo.
  Não partir os períodos sem necessidade; não acrescentar nada.
- Tocqueville fala de si na 1ª pessoa do singular («eu», «penso», «parece-me»); o «nous» de autor e de
  francês («chez nous», «parmi nous») → **«entre nós»**, «em nossos dias».
- O «vous» dirigido ao leitor → **você** (3ª pessoa do singular: «Volte atrás; examine a criança…»;
  decisão `vous`). Nas falas citadas, o tratamento natural do diálogo.
- **Nunca mesóclise** (grep do guia antes de cada commit). Nada de palavra rara quando há uma comum
  de mesmo sentido.

## Termos fixos

- *égalité des conditions* → **igualdade de condições**; *conditions* → condições;
  *inégalité* → desigualdade.
- *état social* → **estado social**; *point de départ* → ponto de partida.
- *mœurs* → **costumes** (no sentido largo que Tocqueville define na nota do cap. «Da influência dos
  costumes»: hábitos do coração, noções, opiniões; decisão `moeurs`); *habitudes* → hábitos;
  *coutumes* → costumes também, quando vem sozinho; quando vêm juntos, *les mœurs et les coutumes* →
  «os costumes e os usos».
- *lumières* → **luzes** (instrução, saber difundido; decisão `lumieres`); *éclairé* → esclarecido,
  instruído.
- *intérêt bien entendu* → **interesse bem compreendido** (decisão `interesse`); *la doctrine de
  l'intérêt bien entendu* → a doutrina do interesse bem compreendido; *intérêt personnel* → interesse
  pessoal.
- *omnipotence de la majorité* → **onipotência da maioria**; *tyrannie de la majorité* → **tirania da
  maioria**; *empire de la majorité* → império da maioria.
- *despotisme administratif* → **despotismo administrativo**; *centralisation administrative /
  gouvernementale* → centralização administrativa / governamental; *pouvoir tutélaire* → poder
  tutelar; *servitude* → servidão.
- *individualisme* → individualismo; *égoïsme* → egoísmo.
- *souveraineté du peuple* → soberania do povo; *pouvoir social* → poder social; *puissance* →
  poder, potência (conforme o caso); *pouvoir* → poder.
- *siècles démocratiques / aristocratiques* → **séculos democráticos / aristocráticos** (decisão
  `seculos`); *dans les siècles d'égalité* → nos séculos de igualdade.
- *peuples démocratiques* → povos democráticos; *nations* → nações; *société politique / civile* →
  sociedade política / civil.
- *commune* (a da Nova Inglaterra) → comuna; *institutions communales* → instituições comunais;
  *township* fica em itálico se aparecer.
- *État* → Estado; *les États* (da União) → os Estados; *l'Union* → a União; *gouvernement fédéral* →
  governo federal; *législature* → legislatura; *juges, jurés* → juízes, jurados.
- *Anglo-Américains* → anglo-americanos; *Américains* → americanos; *Nouveau-Monde* → Novo Mundo;
  *Nouvelle-Angleterre* → Nova Inglaterra; *émigrants* → emigrantes.
- *puritains, puritanisme* → puritanos, puritanismo; *sectes* → seitas; *croyances (dogmatiques)* →
  crenças (dogmáticas); *culte* → culto; *prêtres* → sacerdotes (no geral) ou padres (católicos);
  *clergé* → clero; *ministres* (protestantes) → ministros.
- *esprit de religion / esprit de liberté* → espírito de religião / espírito de liberdade.
- *la Providence* → a Providência; *providentiel* → providencial.
- *honnêtes gens* → gente de bem; *hommes d'État* → estadistas; *publicistes* → publicistas.
- *droit d'aînesse* → direito de primogenitura; *substitutions* → substituições (fideicomissos, na
  nota); *propriété foncière* → propriedade territorial.

## Formato

- Um arquivo traduzido por arquivo do original, mesmo nome, **mesmo número de blocos** (parágrafos,
  títulos `## `, sumários em itálico e notas `¤ [n]`), na mesma ordem.
- Títulos de seção (`## …`): só a primeira letra maiúscula (e os nomes próprios).
- Sumários (o resumo em itálico no começo do capítulo e das seções, do próprio Tocqueville): em
  itálico, com os travessões « — » como no original.
- Notas do autor: a chamada `[n]` fica no mesmo ponto da frase; o texto da nota no bloco `¤ [n] …`.
  Títulos de livros e jornais em itálico, como estão (_History of Virginia_, _Code of 1650_), sem
  traduzir; «Voyez» → «Ver»; «Id.» → «Id.»; «vol.», «p.», «art.», «§» como estão.
- **Citações em inglês nas notas** (leis, jornais, discursos): traduzidas para o português, e o título
  da fonte fica em inglês (decisão `ingles`). O inglês fica no original ao lado.
- Números: «161,000» → «161.000»; datas como no original.
- «M.» → «o sr.»; «MM.» → «os srs.».
- Aspas: “…”, com ‘…’ dentro. Itálico: `_assim_`.

## Escolhas registradas

- Introdução, § 1: «le fait générateur dont chaque fait particulier semblait descendre» → «o fato
  gerador do qual cada fato particular parecia descender».
- I,2,9 (religião): «qui changent le siége de l'État tous les quatre ans» → «que trocam o chefe do
  Estado a cada quatro anos», pela emenda das _Œuvres complètes_ (1864–66), com o original ao lado
  como em 1848 (decisão `siege`).
- Fixados na tradução (ver `traducao/notas-tradutor.md`): *hiérarchie des rangs* → hierarquia das
  classes; *charte* → carta (*charte royale* → carta régia); *cautionnement / caution* → fiança /
  fiador; *l'arbitraire* → o arbítrio; *idées arrêtées* → ideias assentadas; *libre arbitre* →
  livre-arbítrio; *pouvoir tutélaire* → poder tutelar (tutores, tutela); *canton* (nos Estados Unidos)
  → distrito; *prêtre* → sacerdote no geral, padre quando é o clero católico ou o americano.
- Nomes: Spinosa → Espinosa; «Madisson» como no impresso; nomes de lugar na forma corrente no Brasil
  (Nova York, Pensilvânia, Rhode Island); nomes estropiados das notas como no impresso.
- II,4,6: «il aime que les citoyens se réjouissent, pourvu qu'ils ne songent qu'à se réjouir» →
  «gosta de que os cidadãos se divirtam, contanto que só pensem em divertir-se».
