# Convenções do Magistério (documentos da Igreja, sob o autor «Igreja Católica»)

Valem para todo documento de `edicoes/magisterio/<documento>/`, junto com as gerais de
`edicoes/CONVENCOES-TRADUCAO.md` (que valem onde estas não dizem nada). Decididas em 2026-10-26, com o
Gere: tradução nova, do original (as do vatican.va são protegidas), com o original ao lado, só as
notas do próprio documento, sem comentários. Os termos se fixam aqui, sem fila de revisão para ele.

## 1. O texto de base

- Base de trabalho: o texto na língua original da página do vatican.va (latim; italiano na *Tra le
  sollecitudini*). Ele vem do texto das *Acta* (ASS até 1908, AAS desde 1909), que é a referência e
  vai citado na página «Sobre».
- A página do vatican.va tem erros de digitalização («f.. r.», «A. A. 5.», «Eneycl.»). Corrija só o
  erro evidente, no original e na tradução, e liste cada correção nas notas do tradutor. Na dúvida,
  confira no PDF das *Acta* (o link está no `obra.py`) e não corrija o que não puder conferir.
- Nada se acrescenta ao texto: nem títulos de seção que o original não tem, nem explicações.

## 2. Os arquivos (original e tradução, iguais em estrutura)

- `original/<documento>.txt` e `traducao/<documento>.txt`: cabeçalho de linhas `# chave: valor`
  (`# titulo:`, e no original `# fonte:` e `# nota:`), depois os blocos separados por linha em branco,
  **o mesmo número de blocos e na mesma ordem nos dois arquivos**.
- O cabeçalho do documento (papa, «Carta encíclica», o nome, os destinatários, o tema e a saudação)
  fica no começo, como parágrafos, na ordem do original.
- Título de seção do original («I», «II»…, ou com título): bloco próprio começando por `## `
  (`## I`, `## II`). Se o original não titula, não há `## `.
- Chamada de nota: «(1)» do vatican.va vira `[1]`, colada à palavra ou à pontuação, como no
  original. A nota: um bloco `¤ [1] texto da nota`, **logo depois do parágrafo que a chama**.
- Numeração: o vatican.va em inglês numera os parágrafos (é a numeração mais citada). Marque
  `{§ n}` no ponto do original onde começa o parágrafo *n* da versão inglesa: no começo do bloco,
  ou no meio dele, antes da frase em que o parágrafo inglês começa. A tradução leva a mesma marca no
  mesmo lugar. Se o documento tem numeração própria no original (como a *Tra le sollecitudini*), vale
  a dele, que já está no texto, e não se marca a do inglês. A versão inglesa serve só para achar os
  pontos; nada dela se copia.
- O fecho («Datum Romae…») e a assinatura são blocos como os outros.

## 3. Termos fixos

| original | tradução |
|---|---|
| Venerabiles Fratres | Veneráveis Irmãos |
| salutem et apostolicam benedictionem | saúde e bênção apostólica |
| Nos, Noster (plural do papa) | Nós, Nosso (com maiúscula, como o latim) |
| Decessor Noster; f. r. (felicis recordationis); s. m. | Nosso Predecessor; de feliz memória; de santa memória |
| Apostolica Sedes; Romanus Pontifex | Sé Apostólica; Romano Pontífice |
| Ecclesia; catholica Ecclesia | Igreja; Igreja Católica |
| christifideles; Ordinarii | fiéis; Ordinários |
| civitas (a comunidade política) | Estado (ou «cidade», quando o texto fala da cidade) |
| civilis societas, societas civilis | sociedade civil |
| res publica | Estado; «coisa pública» só quando o texto joga com a expressão |
| principes, qui praesunt (os governantes) | governantes (ou «príncipes», se o texto fala de reis) |
| potestas; auctoritas; imperium | poder; autoridade; poder ou mando, conforme o caso |
| opifices, operarii; proletarii | operários; proletários |
| merces | salário |
| communismus, socialismus, liberalismus | comunismo, socialismo, liberalismo |
| modernistae | modernistas |
| secta (a maçonaria) | seita |
| Datum Romae apud S. Petrum, die… | Dado em Roma, junto de São Pedro, no dia… |
| Pontificatus Nostri anno… | do Nosso Pontificado, o ano… (ex.: «no ano décimo sexto do Nosso Pontificado») |
| PIUS PP. XI, LEO PP. XIII | PIO PP. XI, LEÃO PP. XIII |

Termo novo que se repete: registre-o nas notas do tradutor, com a solução, para entrar nesta tabela.

## 4. Citações e referências

- Escritura: traduza como o documento cita (em geral a Vulgata), sem copiar uma Bíblia portuguesa.
  Salmos com a numeração da Vulgata, como o documento.
- Outros documentos e Padres citados: traduza do latim do próprio documento (não copie traduções
  existentes).
- Nas notas: abreviaturas portuguesas dos livros (Gn, Ex, Mt, Mc, Lc, Jo, At, Rm, 1Cor, 2Cor, Gl, Ef,
  Fl, Cl, 1Ts, 2Ts, 1Tm, 2Tm, Tt, Hb, Tg, 1Pd, 2Pd, 1Jo, Ap; Sl, Pr, Ecl, Sb, Eclo, Is, Jr, Ez, Dn…),
  com a numeração como o autor a dá (romanos e arábicos); «Litt. Encycl.» → «Carta encíclica»;
  «Epist.» → «Carta»; «A. A. S.» → «AAS»; «Acta Leonis XIII» e semelhantes ficam; «vol.», «p.», «pp.»
  ficam; títulos de documentos em itálico.

## 5. O estilo

Português do Brasil culto, claro, com o registro solene do documento, sem arcaísmo artificial. O
período latino longo pode virar duas ou três frases quando, inteiro, ficaria confuso em português;
a ordem das ideias e as ligações lógicas (portanto, com efeito, todavia) ficam. Nunca mesóclise.
