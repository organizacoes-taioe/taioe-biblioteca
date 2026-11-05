# Conferência das *Poesias Completas* (Machado de Assis, 1901) nas imagens

Responda e escreva em português do Brasil. Você estabelece o texto de 1901 de alguns poemas, olhando as
imagens do fac-símile. Worktree: `~/.cache/claude-wt5-poesias-machado` (trabalhe só nela; caminhos abaixo
relativos a ela, salvo os do cache).

## O que você tem
- `edicoes/poesias-completas-machado/rascunho/<id>.txt`: o texto do poema como está no Wikisource (a 1ª edição,
  1864/1870/1875, ou, nas *Ocidentais*, o próprio volume de 1901), com as divergências do OCR de 1901 marcadas:
  - `⟦ws‖ocr⟧`: a palavra ou o sinal difere; o 1º lado é o Wikisource, o 2º o OCR de 1901;
  - `⟦+ ...⟧`: só o OCR de 1901 tem (verso novo de 1901, título, epígrafe, número de seção, cabeço, sujeira);
  - `⟦- ...⟧`: só o Wikisource tem (verso cortado em 1901, ou o OCR perdeu).
- As imagens de 1901: `~/.cache/claude-pedidos-0511/poesias-completas-machado/pag/p-NNN.png` (NNN = página do PDF,
  3 algarismos; a 1ª linha do rascunho diz quais). Abra-as com a ferramenta Read. Página do PDF = página do livro + 16.
- O OCR cru de cada página: `~/.cache/claude-pedidos-0511/poesias-completas-machado/tess/NNN.txt`.

## O que fazer
Para cada poema seu, grave `edicoes/poesias-completas-machado/1901/<id>.txt` com o texto **como está em 1901**:
1. Abra as páginas do poema, uma a uma, e leia-as junto com o rascunho, verso a verso.
2. Resolva **toda** marca ⟦…⟧ pela imagem: escreva o que 1901 imprime (às vezes o Wikisource, às vezes o OCR, às
   vezes outra coisa). Machado revisou os poemas para 1901: palavra, pontuação, verso ou estrofe inteira podem ter
   mudado, e vale sempre 1901. Sujeira do OCR (cabeço «CHRYSALIDAS 31», número de página, letras soltas) some.
3. Corrija também o que não estiver marcado e você vir diferente na imagem (palavra, pontuação, verso faltando ou
   sobrando, quebra de estrofe). Confira a quebra de estrofe na virada da página: na imagem, veja se a página
   seguinte começa com espaço de estrofe nova; na dúvida, fica a do rascunho.
4. **Grafia**: não perca tempo com diferenças só de grafia entre o rascunho e a imagem (h, acentos, y/i, ph/f,
   consoantes dobradas, -ão/-am, céo/céu): podem ficar como no rascunho; depois um script põe tudo na grafia de hoje.
   Mas as formas que mudam o som ou o metro seguem a imagem: *inda/ainda*, *co'as/com as*, *n'outra/noutra*,
   *dous/dois*, *cousa*, *p'ra*, *té/até*, *vae/vai*, apóstrofos, *á/a* (crase). O que você escrever de novo
   (cabeçalhos, versos novos), escreva como está na imagem, sem modernizar.
5. Itálico entre sublinhados: `_assim_` (palavras estrangeiras, títulos, epígrafes). Sem recuos no começo dos versos.
6. Erro evidente de composição em 1901 (letra trocada, palavra que não existe) se corrige, com uma linha
   `# nota: «x» (1901) corrigido para «y»: erro de composição; a 1ª ed. tem «y»`. Leitura duvidosa fica como
   impressa, com `# nota: dúvida: ...`. Nada de emenda por gosto.

## Formato de `1901/<id>.txt`
Cabeçalho (linhas `# chave: valor`), depois os versos, um por linha, linha em branco entre estrofes:
```
# titulo: Musa consolatrix          (caixa normal, como no índice; a grafia de 1901)
# subtitulo: (Edgar Poe)            (linha logo abaixo do título: autor traduzido, dedicatória entre parênteses, «fragmento», «história guaycurú»)
# epigrafe: Oh! la fleur de l'Eden, pourquoi l'as-tu fanée, / Insouciant enfant, belle Eve aux blonds cheveux? (Alfred de Musset)
# nota: ...                         (comentário de conferência; não vai ao site)

Que a mão do tempo e o halito dos homens
Murchem a flor das illusões da vida,
...
```
No meio do poema, linhas de marca, sozinhas e entre linhas em branco:
- `# parte: I` — número ou título de seção (centralizado no livro); `# subtitulo: ...` logo depois, para o título da
  seção (na *Lyra chineza*: `# parte: I`, `# subtitulo: O poeta a rir`, `# subtitulo: (Han-Tiê)`);
- `# epigrafe: ...` — epígrafe de uma seção;
- teatro (*Uma ode de Anacreonte*): `# personagens: Lysias / Cleon / Myrto / Tres escravos`, `# lugar: A scena é em
  Samos...` (a indicação geral), `# cena: Scena I`, `# rubrica: (Estão no fim de um banquete...)` (indicação de
  cena; pode vir também no meio de uma fala), `# fala: LYSIAS` (o nome de quem fala, antes dos versos dele);
- `# data: ...` — data ou lugar no pé do poema; `# lacuna` — linha de pontos ou de asteriscos;
- prosa (só a Advertência): cada parágrafo numa linha comum, e `# assinatura: Machado de Assis.`.

## Notas do autor (só quem receber a tarefa das notas)
As notas do volume estão no fim (PDF 381–390). Grave `edicoes/poesias-completas-machado/1901/notas.txt`, na
ordem do livro; cada nota assim:
```
@ <id do poema a que a nota se refere>          (ids em edicoes/poesias-completas-machado/poemas.json)
= A                                             (a letra da nota em 1901; nota sem letra: = -)
> Flor da mocidade                              (o lema: o título ou os versos citados, versos separados por " / ", SEM o «pag. NN»)
Os poetas classicos francezes usavão muito esta fórma ...   (cada parágrafo numa linha)
| É um velho paiz, de luz e sombras,            (versos citados dentro da nota: um por linha, com "| "; estrofe = linha "|")
```
Para achar o poema de cada nota, procure os versos do lema nos rascunhos (`grep`). Testemunho para o confronto:
as notas das primeiras edições no Wikisource, `~/.cache/claude-pedidos-0511/poesias-completas-machado/ws-Phalenas/215.txt`
a `221.txt` e `ws-Americanas/209.txt` a `224.txt` (texto de 1870 e 1875; vale 1901, mas elas ajudam a ler).

## Commit (obrigatório, a cada 1–3 poemas prontos)
Na raiz da worktree: `bash edicoes/poesias-completas-machado/commitar.sh "Poesias Completas: <ids> conferidos nas imagens" edicoes/poesias-completas-machado/1901/<id>.txt ...`
(várias conversas commitam ao mesmo tempo nesta worktree; o script espera a vez). Commite só os seus arquivos.
Não mexa em nenhum outro arquivo do repositório, nem no corpus do Versificador.

## Relatório final (curto)
Para cada poema: quantas marcas, quantas mudanças de 1901 sobre a 1ª edição (palavras/versos), notas de dúvida e de
erro de composição; e qualquer coisa estranha (página faltando no fac-símile, poema cortado, estrutura incomum).
