# Castelo interior (As moradas), de Santa Teresa de Jesus: convenções da tradução

Prevalece sobre `edicoes/CONVENCOES-TRADUCAO.md` onde for mais específico. Texto de base: Silverio de
Santa Teresa, *Obras de Santa Teresa de Jesús*, t. IV (Burgos, 1917), que transcreve o autógrafo de
Sevilha com a ortografia atualizada (ver `original/LEIAME.md`).

## 1. Princípio e registro

- Fiel ao sentido e ao movimento da prosa de Teresa: oral, de conversa com as irmãs, cheia de
  parênteses, retomadas («tornando ao que dizia»), desculpas («não sei se me entendo»), exclamações
  e frases longas que mudam de rumo. **Não arrumar** a sintaxe dela para ficar elegante: só o
  necessário para o português ficar claro. As repetições e os anacolutos de propósito ficam.
- Português do Brasil culto e simples, sem arcaísmo artificial. As formas antigas do castelhano dela
  (*ansí*, *mesmo*, *agora*, *dinidad*, *inorancia*, *terná*, *mirá*, *entendé*) saem em português de
  hoje (assim, mesmo, agora, dignidade, ignorância, terá, vede, entendei).
- Palavra rara, nunca (regra do Gere): se o português comum tem a palavra, é ela.
- **Nunca mesóclise** (grep do guia antes de cada commit; `trechos.py conferir` acusa).

## 2. Tratamento

- **As irmãs**: Teresa fala às monjas por *vosotras*: em português, **vós** (*mirad* → «vede»,
  *entended* → «entendei», *os parecerá* → «vos parecerá»). *Hermanas* → «irmãs»; *hijas* → «filhas».
- **Deus**: quando Teresa fala com Deus (*Vos*, *vuestro*), «**Vós**», «Vosso», «Vos», com maiúscula
  («ó Senhor, que todo o dano nos vem de não ter postos os olhos em Vós»).
- Maiúsculas de reverência onde a edição as põe: *Su Majestad* → «Sua Majestade», *Él* → «Ele»,
  *Sí* → «Si», *Esposo* → «Esposo». Onde a edição não as põe, minúscula.
- *Nuestro Señor* → «Nosso Senhor»; *el Señor* → «o Senhor»; *Su Majestad* → «Sua Majestade»
  (nunca «Sua Majestade divina» se ela não disser).

## 3. Termos fixos

| castelhano | português |
|---|---|
| castillo interior; moradas; aposentos; piezas | castelo interior; moradas; aposentos; cômodos (*piezas*, quando não é «aposentos») |
| primeras moradas … séptimas (sétimas) moradas | primeiras moradas … sétimas moradas |
| oración mental / vocal | oração mental / vocal |
| oración de recogimiento | oração de recolhimento |
| oración de quietud | oração de quietude |
| unión; oración de unión | união; oração de união |
| desposorio (espiritual) | desposório (espiritual) |
| matrimonio espiritual | matrimônio espiritual |
| contentos / gustos (IV.1–2: os que vêm do nosso esforço / os que vêm de Deus) | contentamentos / gostos |
| arrobamiento; éxtasis; rapto; arrebatamiento | arroubamento; êxtase; rapto; arrebatamento |
| vuelo del espíritu | voo do espírito |
| ímpetus | ímpetos |
| hablas (que Dios dice al alma) | falas |
| visión imaginaria / intelectual | visão imaginária / intelectual |
| suspensión (de las potencias) | suspensão (das potências) |
| potencias: entendimiento, memoria, voluntad | potências: entendimento, memória, vontade |
| imaginación; pensamiento | imaginação; pensamento (em IV.1, Teresa os faz a mesma coisa) |
| propio conocimiento | conhecimento próprio |
| humildad; determinación (determinada determinación) | humildade; determinação («determinada determinação») |
| letrados | letrados (os homens de estudo, teólogos; termo dela, ver `revisao.json`) |
| confesor; prelado | confessor; prelado |
| sabandijas; cosas emponzoñosas | bichos; coisas peçonhentas (ver `revisao.json`) |
| gusano de seda; mariposica (blanca) | bicho-da-seda; borboletinha (branca) |
| cosa / cosas | coisa / coisas (nunca «cousa») |
| mercedes (que Dios hace) | mercês |
| regalos (de Dios) | regalos (os mimos, as delícias que Deus dá; ver `revisao.json`) |
| sequedad | secura |
| ¡Oh, válame Dios! | Oh, valha-me Deus! |
| pila, pilón (as fontes de IV.2; retomadas em VI.5) | tanque |
| trabajos (os sofrimentos que Deus manda) | trabalhos (ver `revisao.json`) |
| silbo (do pastor, do Esposo) | assobio |
| embebecimiento; embebidas | embevecimento; absortas |
| letras (estudo) | estudos |
| expiriencia; nengún; luego | experiência; nenhum; logo / em seguida (pelo contexto) |
| harto | bastante, muito (pelo contexto) |

## 4. Escritura e latim

- Teresa cita de memória, quase sempre em castelhano e às vezes em latim. Traduzir **o que ela
  diz**, não copiar uma Bíblia portuguesa; referência só se a edição a dá no texto (as notas de
  Silverio ficaram de fora).
- Latim do texto fica em latim, em itálico, como ela o escreve (*Mihi vivere Christus est*); se ela
  não dá o sentido logo depois, acrescenta-se «[Trad.: …]» em colchetes (registrar nas notas).

## 5. Formato

- Arquivos: `00-prologo.txt` (dedicatória e prólogo), `01-primeiras-moradas.txt` … `07-setimas-moradas.txt`,
  `08-epilogo.txt`, em `original/` e `traducao/`, um parágrafo traduzido para cada parágrafo do original.
- Cada capítulo: `## Capítulo 1 — <ementa de Teresa>` (o gerador faz do título a página do capítulo, com a
  ementa no índice), depois o texto, o primeiro parágrafo com a marca `[I.1]` (morada em romano, capítulo em
  arábico). As segundas moradas têm um capítulo só: `## Capítulo único`, a ementa num parágrafo em itálico com a
  marca `[II.1]` (a parte fica numa página só).
- No começo de cada arquivo de morada, antes do primeiro capítulo, a linha de Teresa sobre o número
  de capítulos (`_Há nelas dois capítulos._`), em itálico.
- Aspas: «…», como na edição (prevalece sobre o guia geral).
- Os colchetes de Silverio (letra ou palavra que falta no autógrafo: *quita[r]*) ficam no original; na
  tradução, nada (traduz-se o sentido completo).
- Trabalho por capítulo em `traducao/trechos/<morada>-<nn>.txt` (`trechos.py mostrar|conferir|juntar`).

## 6. Versos

Versos citados (há poucos) vão pelo método do Versificador (`edicoes/santa-teresinha/CONVENCOES.md`,
§ 7), conferidos no `molde.mjs` sem ✗ nem ≠.
