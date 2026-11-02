# Macunaíma: convenções do texto (proposta, 2026-11-02; a confirmar com o Gere)

Edição-base: a 1ª (São Paulo, 1928, edição do autor), fac-símile da Biblioteca Nacional
(Internet Archive `or182096`; o mesmo exemplar do índice do Wikisource «Macunaíma (1928).pdf»).
18 capítulos e o epílogo (ver FALTA.md, dúvida 1).

## O princípio
A grafia de Mário é parte da obra: ele escrevia «à brasileira» de propósito (a «Gramatiquinha da
Fala Brasileira» estava «em preparo», diz a lista «Do autor» do próprio livro). Modernizar só o que é
**ortografia de época sem valor de estilo**, isto é, o que qualquer texto de 1928 grafava assim e que
não muda a pronúncia nem a forma da palavra.

## Fica como Mário escreveu (escolha do autor, marca da fala)
- `si` (conjunção «se»: 84 vezes), `sinão`, `siquer`, `quasi` (pronúncia com i; forma que ele defendia).
- `pra`, `prá`, `pro`, `pros`, `prás`, `pras` e as contrações `nagua`, `dêle`→ver abaixo, `duma`, `numa`.
- Pronome átono no começo da frase («Me acocorei em riba destas folhas»), colocações e regências da fala.
- `mãi`, `mamãi` (40 vezes; Mário pronunciava e grafava assim; não é «mãe» antiga), `milhor`,
  `guspir`, `frexa` / `frexou` / `frexinhas`, `tribu`, `poude`, `enguliu`, `Ochum`, `Ochosse`,
  `macacheira`, `cachirí`, `piché`, `sussuarana`, `massaroca`, `dansarina`?: formas que o texto
  posterior (Wikisource nível 1) «corrigiu» e que são do impresso de 1928. **Dúvida**: parte delas
  (ch/x, s/ç, ss/ç) pode ser só ortografia de época (antes de 1931 não havia norma), e não estilo.
  Proposta prudente: manter todas as que mudam letra (x/ch, s/ç/ss, u/o, e/i), porque a grafia de
  Mário é programática e não há como separar com segurança; modernizar só acento gráfico.
- Palavras tupis e regionais com a grafia do livro (Uraricoera, cunhatã, curumim/culumi, paxiúba…).

## Modernizar (ortografia de época, sem valor de estilo)
- Acento gráfico pela norma de hoje: `tambem` → também, `ninguem` → ninguém, `heroi` → herói,
  `agua` → água, `porêm` → porém, `ha` → há, `familia` → família, `individuo` → indivíduo.
  O acento não muda a palavra (Mário acentuava pouco e sem sistema; o ABBYY do IA ainda inventa
  acentos, então o acento do OCR não conta).
- Circunflexo diferencial que caiu: `êle` → ele, `fôrça` → força, `chôro` → choro, `dêle` → dele.
- Letras dobradas e etimológicas, se houver (`theatro`, `paiz`): não apareceram até agora no texto
  revisado; `paiz` (1 vez) → país.
- `s` intervocálico de época com som de z (`gosados` → gozados)? **Dúvida** (é como «dansa»):
  proposta, modernizar, porque não marca fala nenhuma.
- Crase e maiúsculas: `Ás` (com agudo, uso de 1928) → Às.
- Hífen e aglutinação: manter os do livro (`talqualmente`, `boca-da-noite`, `mato-virgem`), salvo
  regra clara de hoje sem efeito de leitura.

## Feito em `config.modernizar` (2026-11-02)
Só o acento: a palavra fora do léxico (o do sistema + o Wikisource da edição posterior, na grafia de
hoje) com uma única forma igual sem acentos ganha a dela: heroi → herói (280), êle → ele, porêm →
porém, tambem → também, agua → água, fôrça → força, ninguem → ninguém. Protegidas: prá, prás, porquê,
mãi, mamãi. `á`/`ás` → à/às pelo MANUAL. Ficam: si, sinão, quasi, siquer, pra/pro/pros, mãi, milhor,
guspiu, enguliu, poude, tribu, frexa, nagua, dagua, inda, riba, adonde, desinfeliz.

**A decidir com o Gere** (letra trocada que parece só ortografia de época, sem marca de fala; hoje
ficam como em 1928, no `sem_par.tsv`): geito (10) → jeito, tezouro(s)/tezoura (11) → tesouro/tesoura,
gôso/gosar/gosados → gozo/gozar/gozados, dansa/dansando → dança/dançando, cincoenta → cinquenta,
milreis → mil-réis, guela → goela?. (flexa, 4 vezes, ao lado de frexa: conferida no impresso, é de
Mário; fica.) Recomendação: modernizar
essas (não marcam a fala) e manter as da lista acima (marcam).

## Itálico e pontuação
Pontuação do livro, sem vírgulas acrescentadas (Mário corta vírgulas de propósito: «foi crescendo foi
crescendo»). Aspas “ ” passam a « » como no resto da Biblioteca.

## Vocabulário (`edicoes/vocabulario/macunaima.json`)
Essencial nesta obra (tupi, termos afro-brasileiros, regionalismos), só com definição de fonte segura
(Houaiss/Aulete digital, Cascudo, *Dicionário histórico das palavras portuguesas de origem tupi* de
Antônio Geraldo da Cunha, o glossário de Cavalcanti Proença, *Roteiro de Macunaíma*). Ainda não feito.
