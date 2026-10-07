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
- **Remissões de página:** «Pages 84 et 190» (nota 58 de `02-segunda-parte-b.txt`) remete a uma edição antiga. Troque por remissão ao capítulo correspondente desta tradução, se der para identificá-lo, ou mantenha e registre nas notas. As remissões a outros livros («le _Pouvoir de saint François de Sales_, page 284») ficam.

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
  - Referências no formato do autor, com os livros em português («Judic. XVI» → «Juízes XVI», ou a abreviação «Jz XVI»; escolha uma forma e mantenha). Os erros de referência do impresso ficam como estão; estão listados em `ferramentas/cache/faltas/revisado/emendas.txt`.
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
