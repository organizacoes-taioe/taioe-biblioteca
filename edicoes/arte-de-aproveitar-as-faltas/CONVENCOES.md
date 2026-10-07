# A arte de aproveitar as próprias faltas, de Joseph Tissot — convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md`, com as regras gerais. Este guia acrescenta o que é próprio desta obra e prevalece onde for mais específico. Os modelos são `edicoes/santa-teresinha/CONVENCOES.md` e o guia da Filoteia (`edicoes/introducao-a-vida-devota/CONVENCOES.md`); este livro cita a Filoteia a toda hora.

## 1. Texto-fonte

- Os arquivos são `original/00-avant-propos.txt` a `02-segunda-parte-b.txt`. É a 6e édition (1894), estabelecida do scan (ver `original/LEIAME.md`).
- As linhas `# ` do topo são do arquivo. Traduza só o `# titulo:`.
- Marcas:
  - `## Chapitre N — Título` → `## Capítulo N — Título traduzido`.
  - `[I.1]` fica igual, no começo do primeiro parágrafo do capítulo.
  - Os números «1. —», «2. —» no começo de parágrafos são do autor e ficam como estão.
- **Notas do autor:**
  - `[n]` no texto é a chamada; fica igual, no ponto correspondente da frase traduzida.
  - `¤ [n] ...` é a nota. Traduza o conteúdo e mantenha o prefixo `¤ [n] `, no mesmo lugar (logo depois do parágrafo).
  - Referências bibliográficas: traduza só as palavras comuns («Lettre 793e ; collect. Blaise» → «Carta 793.ª; coleção Blaise»; «Sermon pour le premier Dimanche de Carême» → «Sermão para o primeiro domingo da Quaresma»).
  - Títulos de obras em francês ficam em francês, em itálico (*Esprit du Saint*, *Chrétien intérieur*). Exceção: as obras do próprio São Francisco com forma portuguesa consagrada (*Introd. à la vie dévote* → *Introd. à vida devota*; *Traité de l'amour de Dieu* → *Tratado do amor de Deus*).
- **Remissões de página:** «Pages 84 et 190» (nota 58 de `02-segunda-parte-b.txt`) remete a uma edição antiga. Fica «Páginas 84 e 190», com nota «[Trad.: ...]» (ver § 8). As remissões a outros livros («le _Pouvoir de saint François de Sales_, page 284») ficam.

## 2. Registro e tratamento

- **Tom:** Tissot escreve com unção e clareza, em francês oitocentista correto, com exclamações e apelos ao leitor. Quase metade do livro são citações de São Francisco de Sales, na língua do século XVII.
  - O que é de Tissot vai em português culto atual.
  - O que é de São Francisco guarda o sabor da frase dele (os *car*, os *ains*, as comparações), sem arcaísmo artificial. As regras do vocabulário antigo são as do guia da Filoteia, § 2.
- **Tratamento:** siga o original, passagem por passagem.
  - *vous* → **vós** (*vós*, *vos*, *vosso*, verbo na 2.ª pessoa do plural): São Francisco às suas dirigidas («Vous vivez, écrivait-il à une dame...» → «Viveis, escrevia ele a uma senhora...»), Tissot ao leitor, as orações a Deus e a Maria.
  - *tu* → **tu**: Deus ou Jesus falando à alma, a alma falando a si mesma («O mon âme, souviens-toi» → «Ó minha alma, lembra-te»).
  - Tissot fala quase sempre em *nous*: mantenha o «nós».
- **Citações da Filoteia:** quando Tissot cita a *Introduction*, e se a nossa tradução da Filoteia já existir, use a redação dela, ajustada ao texto que Tissot cita, que às vezes difere. Registre nas notas.
- **Nunca mesóclise.** Antes de entregar, rode:

  ```
  grep -n -E -o "[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)\b" traducao/*.txt
  ```

  Não pode sair nada.

## 3. Escritura e citações

- **Escritura:** traduza do francês ou do latim como Tissot e São Francisco a dão, não de uma Bíblia portuguesa.
  - Latim que fique em latim no original fica em latim, em itálico.
  - Se o autor traduz, traduza a tradução dele.
  - Referências no formato do autor, com os livros em português, abreviados («Judic. XVI» → «Jz XVI»; ver § 8). Os erros de referência do impresso ficam como estão; estão listados em `ferramentas/cache/faltas/revisado/emendas.txt`.
- **Versos:** não há versos no livro. Se aparecer algum na revisão, use o método do Versificador (guia da Filoteia, § 3).

## 4. Nomes

| francês | português |
|---|---|
| saint François de Sales; le saint évêque; le Bienheureux (em citações antigas) | são Francisco de Sales; o santo bispo; o Bem-aventurado |
| sainte Jeanne-Françoise de Chantal; la Mère de Chantal | santa Joana Francisca de Chantal; a Madre de Chantal |
| la Visitation; visitandines | a Visitação; visitandinas |
| Mgr Camus (évêque de Belley) | dom Camus (bispo de Belley) |
| M. de Bernières (-Louvigny) | o senhor de Bernières (-Louvigny) |
| saint Augustin, saint Ambroise, saint Grégoire, saint Bernard | santo Agostinho, santo Ambrósio, são Gregório, são Bernardo |
| sainte Thérèse; saint Louis de Gonzague; saint Vincent de Paul | santa Teresa; são Luís Gonzaga; são Vicente de Paulo |
| Ozanam; le P. Roothaan | Ozanam; o padre Roothaan |
| Samson, les Philistins, David, saint Pierre, Madeleine | Sansão, os filisteus, Davi, são Pedro, Madalena |
| Annecy, Genève, Chablais, Turin | Annecy, Genebra, Chablais, Turim |

«Saint», com nome, vai em minúscula. Sobrenomes ficam em francês.

## 5. Vocabulário

| francês | português |
|---|---|
| utiliser ses fautes | aproveitar as (próprias) faltas |
| faute; chute; tomber | falta; queda; cair |
| imperfection; infirmité; misère | imperfeição; fraqueza (*infirmité* moral), enfermidade (física); miséria |
| s'étonner; se troubler; se décourager | espantar-se; perturbar-se; desanimar |
| trouble; inquiétude; découragement | perturbação; inquietação; desânimo |
| abjection; aimer son abjection | abjeção; amar a própria abjeção |
| humilité; s'humilier | humildade; humilhar-se |
| confiance; miséricorde | confiança; misericórdia |
| persévérance; ferveur, fervent | perseverança; fervor, fervoroso |
| satisfaction (pela pena devida) | satisfação |
| contrition; repentir | contrição; arrependimento |
| amour-propre | amor-próprio |
| le Docteur de la piété | o Doutor da piedade |
| la bienheureuse Vierge Marie | a bem-aventurada Virgem Maria |
| le bon Dieu | o bom Deus |
| Notre-Seigneur | Nosso Senhor |
| Avant-propos | Advertência |

## 6. Tipografia

- **Aspas:** as angulares do original, «...»; dentro delas, “...”.
- **Itálico:** `_assim_`, como no texto-fonte.
- **Abreviaturas por extenso:** *S.* → *são*; *Mgr* → *dom*; *P.* → *padre*; *M.* → *o senhor*.

## 7. Formato de saída

- Cada arquivo vai para `traducao/<mesmo nome>.txt`, com `# titulo:` traduzido («Advertência», «Primeira parte», «Segunda parte, capítulos I a IV»...).
- Um parágrafo traduzido para cada parágrafo do original, na mesma ordem, com `## `, `[I.1]`, `[n]` e `¤ [n]` no mesmo lugar.
- As notas do tradutor vão em `traducao/notas-<arquivo>.md`.

## 8. Termos fixados na harmonização

Fixados ao harmonizar as quatro partes (outubro de 2026). Prevalecem sobre o que vai acima e sobre as notas dos tradutores. O relatório está em `traducao/HARMONIZACAO.md`.

### Texto e edição

- **Epígrafe do rosto:** entra antes da Advertência, como primeiro parágrafo de `00-avant-propos.txt` (no original também): `_Misericordias Domini in æternum cantabo._ (Sl LXXXVIII.) [Trad.: Cantarei eternamente as misericórdias do Senhor.]`.
- **Título do livro dentro do texto:** em português, com «próprias», em itálico e contraído: «a sexta edição da _Arte de aproveitar as próprias faltas_». Quando Tissot fala da arte e não do livro (*l'art d'utiliser ses fautes*), vai sem itálico: «a arte de aproveitar as próprias faltas» (ou «as nossas faltas», se ele diz *nos fautes*). Nos títulos dos capítulos: «Aproveitar as faltas para...».
- **Nota 58 de `02-segunda-parte-b.txt`:** «Páginas 84 e 190. [Trad.: paginação da 3.ª edição; os lugares parecem ser I, cap. III, n.º 7, e II, cap. IV, n.º 2, em nota.]».
- **Erros do impresso:** os de grafia se emendam no original e se registram no `emendas.txt`; as referências erradas ficam como estão, no original e na tradução, e se registram lá. Única adaptação: *Eccl.* (cap. I.3, nota 88), que é o Eclesiástico, vai como «Eclo».
- **Numeração do cap. VIII** (1, 2, 2, 3, 5...): fica como no impresso.

### Escritura e latim

- Livros com a abreviação portuguesa, sem ponto e sem vírgula depois do livro; número do livro em algarismo arábico: Gn, Lv, Nm, Jz, 3 Rs, 2 Mc, Jó, Sl, Pr, Ct, Eclo, Is, Jr, Lm, Ez, Dn, Os, Ag, Mt, Lc, At, Rm, 1 Cor, 2 Cor, Gl, Ef, Cl, Hb, Tg, 1 Pd, 1 Jo. Capítulo em romano e versículo em arábico, como o impresso dá («Sl XC, 6»); salmos pela Vulgata; os poucos números arábicos do impresso ficam («Sl 85, 11»).
- Latim fica em latim e em itálico, também nas notas em que o impresso o dá em redondo. Sem «[Trad.: ...]», salvo na epígrafe; onde Tissot traduz o latim, traduz-se a tradução dele.

### Referências das obras

| francês | português |
|---|---|
| Lettre 793e ; collect. Blaise / coll. Blaise | Carta 793.ª; coleção Blaise |
| édit. Meyer / édition Meyer | edição Meyer |
| Lettre à une Dame / à une Demoiselle / à une Religieuse | Carta a uma senhora / a uma senhorita / a uma religiosa |
| Entretien XVIe. Des Aversions; Entret., Entr. | Colóquio XVI. Das aversões; Colóq. |
| Sermon pour le premier Dimanche de Carême | Sermão para o primeiro domingo da Quaresma |
| Avis, Avis spirituels | Avisos, Avisos espirituais |
| _Introd. à la vie dévote_, 1re partie, chap. 5 / IIIe partie | _Introd. à vida devota_, 1.ª parte, cap. 5 / III parte |
| _Traité de l'amour de Dieu_ / _De l'amour de Dieu_ | _Tratado do amor de Deus_ / _Do amor de Deus_ |
| _Avertissement_ (_Avis_) _aux confesseurs_ | _Avisos aos confessores_ |
| l'auteur de _Philothée_ / de _Théotime_ | o autor da _Filoteia_ / do _Teótimo_ |
| l'_Imitation_ | a _Imitação_ |

Os demais títulos de obras ficam na língua do impresso, em itálico (*Esprit du Saint*, *Chrétien intérieur*, *Manna dell' anima*).

### Abreviaturas, tratamentos e maiúsculas

- *S.* → «são», «santo» («Santo Agostinho», «São João Crisóstomo» no começo de nota); *Mgr*, *Monseigneur* → «dom» («Dom» no começo de nota); *P.*, *Père* → «padre» («Padre» no começo de nota); *R. P.* → «reverendo padre»; *V. Père* → «venerável padre»; *Vén.* → «Ven.».
- *M.* diante de leigo → «o senhor» («o senhor de Bernières», «o senhor Olier»); *M. l'abbé* e *M. J.-J. Allemand* (o mesmo sacerdote) → «o padre».
- Minúscula em *Évêque*, *Religieuse*, *Religieux*, *Directeur*, *Supérieure* quando é Tissot quem fala: «o Bem-aventurado bispo de Genebra», «uma religiosa», «um religioso», «o meu diretor», «uma superiora da Visitação». Nos colóquios do Santo, «a Superiora», «a Diretora», «uma Irmã», onde o impresso tem maiúscula.
- Maiúsculas de reverência do impresso, mantidas: o Santo, o nosso Santo (são Francisco), o Doutor, o Bem-aventurado, o Bem-aventurado Pai, os Santos, os Apóstolos (onde o impresso tem maiúscula), o Coração (de Jesus), Aquele / Daquele (*Celui*, Deus), Ela (Maria, cap. VIII), «pensa n'Ela».
- «Saint», com nome, em minúscula: são Francisco de Sales, santa Chantal.

### Nomes e prenomes

- **Regra dos prenomes:** santos e figuras com forma portuguesa corrente levam o prenome em português, com o sobrenome em francês; religiosos obscuros, nomes ligados a título de obra e escritores leigos ficam em francês.
- Em português: Frederico Ozanam; o venerável padre Cláudio de la Colombière (C. de la Colombière, Cl. de la Colombière, quando o impresso abrevia); dom Carlos Augusto de Sales; santa Joana Francisca de Chantal (santa Chantal; a Madre de Chantal); a Madre Maria de Sales Chappuis; a Madre Angélica Arnaud; a bem-aventurada Margarida Maria; santa Maria Madalena de Pazzi (santa Madalena de Pazzi, onde o impresso encurta); Benigna Gojos; santa Matilde (*Mecthilde*); santa Brígida; santa Gertrudes; são Luís Gonzaga; são Vicente Ferrer; são Tomás de Vilanova; são Gregório Nazianzeno; são Gregório de Nissa; santo Optato de Milevi; Ricardo de São Vítor; Hugo de São Vítor; Cristóvão de Vega; Longuinho; Teodoro; Vítor (bispo de Cartago); Simão, o Leproso.
- Em francês: Alexandre de Saint-François; M.-Mélanie Pommeroy; Raoul d'Asti; Linée; Louis Veuillot; J. de Maistre; as Irmãs citadas pelas iniciais (Irmã C.-E. Cortelot, Irmã M.-A. Fichet...); a senhora de Cornillon; a presidente Brulart; a senhora d'Aix.
- **Puits-d'Orbe** (a abadessa do Puits-d'Orbe), também na nota 79 de `01-primeira-parte.txt`, onde o impresso tem *Puits-d'Ordre* (emendado).
- O padre **La Rivière** (maiúscula sempre); o padre **Roothaan** (o impresso tem *Roothan*); o padre Grou, o padre Faber, o padre Segneri, o padre Pinamonti, o padre Du Pont, o padre Varin, o padre Gratry; o cura d'Ars.

### Vocabulário

| francês | português | observação |
|---|---|---|
| avancement | progresso | era «adiantamento» em 01 e 02-a; como na Filoteia |
| avancé (na perfeição) | adiantado | |
| reconnaissance (para com Deus) | gratidão | exceção: «o conhecimento gera o reconhecimento» (Filoteia III.5, jogo de palavras) |
| « tenant des pécheurs » | «o que responde pelos pecadores» | II.2, n.º 2 |
| caution des pécheurs | fiador dos pecadores | II.2, n.º 2 |
| Entretien | Colóquio | |
| mouchons (des abeilles) | crias | como na Filoteia, IV.2 |
| il ne faut pas (proibição) | não se deve, não convém | nunca «não é preciso», que diz o contrário |
| empressement | pressa | fora das citações da Filoteia, que seguem a redação dela |
| industries | expedientes; recursos | pelo contexto |
| chétif, chétive; chétiveté | mesquinho; pobre; pequenez | como na Filoteia |
| abjection; agréer l'abjection | abjeção; aceitar a abjeção | |
| marri; marrissement | pesaroso; _amofinamento_ | |
| Or sus; Sus | Eia; Eia, pois | |
| tout bellement | devagarinho | fora das citações da Filoteia |
| Notre-Dame; la Sainte Vierge; la Très Sainte Vierge | Nossa Senhora; a Santa Virgem; a Santíssima Virgem | maiúsculas do impresso |

### Citações da Filoteia

- Seguem a redação da nossa tradução da Filoteia, ajustada só onde o texto de Tissot difere do de são Francisco (palavra trocada, trecho cortado, glosa entre parênteses).
- As passagens dos capítulos III.1–13, que ainda estavam em tradução, ficaram com a redação dos tradutores do Tissot e estão listadas em `traducao/HARMONIZACAO.md` para conferir quando a Filoteia 03-a estiver pronta.

### Pronomes combinados

- Evitar «lho(s)», «lha(s)», «no-la», «vo-la», como na Filoteia; «vo-lo», «no-lo», «no-los», «vo-los» ficam onde soam naturais.
