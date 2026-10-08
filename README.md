# Biblioteca

Sítio de leitura de textos em domínio público. Escolhe-se o autor, depois a obra, e lê-se
parte por parte, seguindo a divisão interna do próprio livro (capítulos, cantos, atos...).

Primeira obra: **Machado de Assis — _Dom Casmurro_**, em texto estabelecido para esta
biblioteca (ver abaixo). Depois, a prosa de Machado e a **poesia** do corpus do Versificador:
cerca de 2.100 poemas de 28 poetas de língua portuguesa e poemas estrangeiros traduzidos, com
o original ao lado.

## Como funciona

Site estático puro: HTML, CSS e um arquivo de JavaScript. Sem build, sem dependências,
sem npm. Basta abrir o `index.html` no navegador; funciona até sem servidor.

```
index.html                              página única; lista os arquivos de conteúdo
css/estilo.css                          toda a aparência
js/app.js                               roteador e renderização
conteudo/autores.js                     cadastro dos autores
conteudo/<autor>/<obra>.js              uma obra por arquivo (gerado pelas ferramentas)
conteudo/poesia.js                      índice de todos os poemas (gerado por ferramentas/poesia.py)
conteudo/<autor>/poesia.js              texto dos poemas do autor, carregado sob demanda
edicoes/<obra>/                         fontes e decisões editoriais de cada obra
ferramentas/                            estabelecimento dos textos (Python)
PLANO.md                                bibliografia de Machado de Assis e andamento
netlify.toml                            configuração de publicação (opcional)
```

As rotas usam `#`, de modo que qualquer hospedagem estática serve:

| Rota                     | Página                                  |
| ------------------------ | --------------------------------------- |
| `#/`                     | capa: autores e "continuar a leitura"   |
| `#/a/machado-de-assis`   | gêneros do autor                        |
| `#/a/machado-de-assis/romances` | obras do gênero: ano, capítulos, palavras |
| `#/a/machado-de-assis/contos` | contos, agrupados por livro, com a 1ª publicação |
| `#/o/dom-casmurro`       | folha de rosto e índice                 |
| `#/o/dom-casmurro/12`    | 12ª parte (aqui, o capítulo XII)        |
| `#/o/dom-casmurro/sobre` | notas sobre o texto desta edição        |
| `#/o/o-alienista/1`      | um conto (cada conto é uma obra; o livro vai em `coletanea`) |
| `#/a/olavo-bilac`        | num poeta, direto as pastas por forma   |
| `#/a/olavo-bilac/poesia/sonetos` | os sonetos do autor, livro a livro |
| `#/o/o-corvo/1`          | um poema (aqui, traduzido: original ao lado) |

Na leitura, as setas ← e → do teclado passam de uma parte para outra. O site guarda no
navegador a última parte lida de cada obra, o tema (claro ou escuro) e o tamanho da letra.

Para ver no computador com um servidor local:

```bash
python -m http.server 8765
```

e abrir `http://localhost:8765`.

## Acrescentar um autor

Em `conteudo/autores.js`:

```js
BIBLIOTECA.autor({
  id: 'eca-de-queiros',              // usado nas rotas e no campo "autor" das obras
  nome: 'Eça de Queirós',
  nomeCompleto: 'José Maria de Eça de Queirós',
  vida: '1845–1900',
  ordem: 'Queirós, Eça de',          // posição na lista de autores
  nota: 'Uma linha de apresentação (opcional).'
});
```

## Acrescentar uma obra

As obras desta biblioteca são geradas por `ferramentas/texto.py` a partir das decisões
registradas em `edicoes/<obra>/` (ver `ferramentas/README.md`). Para um texto que não passe
por esse processo, também dá para escrever o arquivo à mão:

1. Crie `conteudo/<autor>/<obra>.js`:

```js
BIBLIOTECA.obra({
  id: 'o-primo-basilio',             // único no site inteiro
  autor: 'eca-de-queiros',
  titulo: 'O Primo Basílio',
  ano: 1878,
  genero: 'Romance',
  divisao: { singular: 'capítulo', plural: 'capítulos' },
  descricao: 'Uma frase sobre o livro, na folha de rosto (opcional).',
  edicao: { apresentacao: `Notas sobre o texto (opcional).` },
  partes: [
    { n: 'I', titulo: '', texto: `Primeiro parágrafo.

Segundo parágrafo.` },
    { n: 'II', titulo: '', texto: `...` }
  ]
});
```

2. Acrescente a linha no `index.html`, junto das outras (sempre depois do `app.js`):

```html
<script defer src="conteudo/eca-de-queiros/o-primo-basilio.js"></script>
```

### Formato do texto

- Use crases (`` ` ``) para abrir e fechar o texto de cada parte.
- Parágrafos separados por uma linha em branco.
- `_itálico_` entre sublinhados; `**negrito**` só nas notas de edição.
- Versos, inscrições e citações compostas à parte: uma linha por verso, começando com `| `.
- Um parágrafo que começa com minúscula (continuação da frase depois de uma citação em
  verso) aparece sem recuo.
- Partes sem título mostram no índice o começo do texto.
- Parágrafos que começam com `¤ ` são notas do autor: aparecem juntos, no fim da parte.

### Contos

Cada conto é uma obra própria (`BIBLIOTECA.obra`), com três campos a mais:

```js
  subtitulo: 'Diálogo',                                   // opcional
  coletanea: { id: 'papeis-avulsos', titulo: 'Papéis Avulsos', ano: 1882, ordem: 3 },
  publicacao: '_Gazeta de Notícias_, 18 de dezembro de 1881',
  paratexto: true,                                        // advertência, prefácio (opcional)
```

A página do gênero agrupa os contos pelo livro, na ordem de `ordem`; um conto sem capítulos
(uma só parte, sem número nem título) abre direto no texto, e as setas levam ao conto
anterior ou seguinte do mesmo livro.

## Poesia

Os poemas vêm do corpus do Versificador (`Solar/Editora/Versificador`): o texto em ortografia
atualizada de `corpus/<autor>/` e as traduções de `traducao/<poema>/`. Os poemas infantis
ficam de fora, assim como os trechos de teste de `poemas/` (os poemas completos de lá já estão
no corpus). Para publicar de novo depois de mudar o corpus:

```bash
python ferramentas/poesia.py
```

A ferramenta grava `conteudo/poesia.js` (o índice, que chega com o site) e um
`conteudo/<autor>/poesia.js` por autor (o texto, que só é baixado quando um poema do autor é
aberto). Ela também:

- põe cada poema numa **pasta por forma**, pelo campo `# forma` do corpus: Sonetos, Apólogos,
  Liras, Odes, Verso livre e Outras formas; o autor só mostra as pastas que tem, e com uma
  pasta só mostra direto a lista;
- agrupa os poemas de cada pasta **por livro**, na ordem de publicação (tabela `LIVROS`);
- junta num só os poemas longos que o corpus divide em arquivos (`JUNTAR`: _Os Timbiras_,
  _Alma em Flor_, _Gulnare e Mustafá_, _Lira Paulistana_);
- tira os textos repetidos (poema «avulso» que também está no livro);
- leva para a página «Sobre esta edição» a publicação, a ortografia, a forma, a fonte e as
  notas do corpus.

Poetas novos no corpus precisam de cadastro em `AUTORES` e `LIVROS` (na ferramenta) e em
`conteudo/autores.js`.

### Formato do texto de um poema

Um verso por linha; estrofes separadas por uma linha em branco. Linhas começadas por `::`
são marcas: `::parte II` (seção do poema), `::subtitulo`, `::fala ROMEU.`, `::voz`,
`::epigrafe` (linhas separadas por ` / `), `::dedicatoria`, `::data`, `::fecho`,
`::separador` (`*`, `* * *`, `filete`, `linha de pontos`), `::lacuna` e `::pagina` (espaço).

## Traduções: original e tradução

Uma parte que traga `original` além de `texto` é lida em modo bilíngue. No alto da página, sob
a barra do topo, dois botões independentes: o original (com o nome da língua) à esquerda e
«Português» à direita.

- O texto abre só em português. A escolha vale de parte em parte da mesma obra; ao reabrir o
  texto, volta o português.
- Pelo menos um fica ligado: o botão do único texto visível não desliga.
- Com os dois ligados, os textos ficam lado a lado. No poema, cada verso fica na altura do seu
  par; na prosa, cada parágrafo começa na altura do seu par.
- Em tela estreita (até 760 px), um texto de cada vez: tocar num botão mostra aquele texto. Na
  troca, o verso (ou parágrafo) que estava no alto da tela continua no mesmo lugar.

Para uma obra traduzida escrita à mão, basta acrescentar à obra
`traducao: { lingua: 'francês', codigo: 'fr', titulo: 'Titre original' }` e, em cada parte,
`original` (e, se houver, `tituloOriginal`), no mesmo formato de `texto`.

## O texto de _Dom Casmurro_

Base: a 1ª edição (H. Garnier, 1899), estabelecida palavra por palavra a partir de três
transcrições independentes (Projeto Gutenberg, Wikisource e J. Stolfi/Unicamp), com o
fac-símile como árbitro. Foram corrigidos os erros tipográficos evidentes e adotadas as
lições da 2ª edição (1900, a última em vida do autor) atestadas por toda a tradição
posterior. A ortografia foi atualizada pelo Acordo de 1990 sem tocar no vocabulário, nas
formas e na sintaxe do autor (mesóclises, colocação pronominal, pontuação); só as formas
antigas de palavras atuais passaram à de hoje (_cousa_ → coisa, _dous_ → dois). A lista completa das intervenções está na página
**Sobre esta edição** do próprio site (`#/o/dom-casmurro/sobre`).

## Publicar

Qualquer hospedagem estática serve, com a raiz do repositório como pasta publicada:

- **GitHub Pages**: Settings → Pages → *Deploy from a branch* → `main` / raiz.
- **Netlify**: importar o repositório, sem comando de build, *publish directory* `.`
  (o `netlify.toml` já traz isso).

## Taioé: o site estático (etapa 4 do PLANO da plataforma)

Em taioe.com.br/biblioteca/, a Biblioteca deixa de ser uma página única com rotas `#` e vira um
site estático: **uma página HTML pronta para cada área, autor, gênero, pasta de poemas, obra,
parte e «Sobre esta edição»**, com endereço fixo (`/biblioteca/machado-de-assis/dom-casmurro/xii/`),
título e descrição próprios, `sitemap.xml` e dados estruturados. Funciona até sem JavaScript.

```bash
node ferramentas/site/gerar.mjs      # grava public/biblioteca/, enderecos.json e sql/obras.sql
node ferramentas/site/conferir.mjs   # links internos, títulos, CSP (nada inline)
```

- **Rode o gerador e commite o resultado sempre que mudar `conteudo/`.** O workflow *Site* recusa
  o push se `public/biblioteca/` não estiver em dia.
- O gerador lê o `conteudo/` na ordem do `index.html` antigo e usa as mesmas funções de marcação
  do `js/app.js` antigo; só os endereços mudam.
- **Endereços congelados:** `ferramentas/site/enderecos.json` guarda o endereço de cada parte. Uma
  parte nunca muda de endereço; parte nova ganha um endereço novo. Nunca apague linhas desse arquivo.
- O endereço da obra é o `id` sem o nome do autor repetido no começo.
- `ferramentas/sql/obras.sql` é o catálogo (`biblioteca.obras`), aplicado pelo workflow *Catálogo*
  do `taioe-infra`, primeiro no teste e depois na produção, **antes** de publicar obra nova.
- `ferramentas/site/leitor.js`: tema, letra, original e tradução, setas, e a posição de leitura —
  só no navegador para quem não entrou; na conta, em qualquer aparelho, para quem entrou.
- `ferramentas/site/comum/`: cópias do supabase-js e do módulo de sessão do `taioe-hub`
  (o workflow *Cópias* confere o sha256).

### O _Catecismo da Igreja Católica_

Vem do site próprio do Catecismo (pasta `catecismo`, vizinha de `taioe`), onde o texto é
preparado. `edicoes/catecismo/dados/` é cópia fiel da pasta `dados/` de lá; o gerador lê essa
cópia (`ferramentas/site/catecismo.mjs`). Quando entrarem pontos novos no Catecismo:

```bash
python estrutura.py                            # na pasta do Catecismo: aberturas e subtítulos
python edicoes/catecismo/sincronizar.py        # aqui: confere e copia (aceita a pasta como argumento)
node ferramentas/site/gerar.mjs && node ferramentas/site/conferir.mjs
```

Endereços: `/biblioteca/igreja-catolica/catecismo-da-igreja-catolica/` (índice e «Ir ao ponto»),
`.../27/` (o ponto 27), `.../a27/` (a abertura do tópico que começa no 27) e `.../sobre/`. A
navegação passa pelas aberturas (… 26 → a27 → 27 …). O número da nota no corpo abre um popup
(o mesmo funcionamento dos popups da Bíblia); sem JavaScript, é um link para a nota embaixo.
O texto não está em domínio público: nessas páginas o rodapé diz «© Libreria Editrice Vaticana».

Cada ponto traz também «Ler este ponto no site do Vaticano», que vai à página do vatican.va com
um fragmento de texto (`#:~:text=`) apontando para o começo do ponto. Os endereços dos 2865
pontos ficam em `edicoes/catecismo/vaticano.json`, gravado uma vez por
`python edicoes/catecismo/vaticano.py` (o gerador não acessa o Vaticano).
