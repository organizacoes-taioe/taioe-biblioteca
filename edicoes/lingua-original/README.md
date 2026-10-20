# Poemas na língua original

Textos em outras línguas na Literatura, **sem tradução** (pedido do Gere, 2026-10-19): toda palavra
do poema é clicável e abre uma nota com a definição do sentido que ela tem ali, traduzida ao
português do Wiktionary, com o link para o verbete original, e, quando é preciso, uma explicação
nossa do uso no verso.

- `obras.json`: autor, título, livro, ano, forma e fontes de cada poema.
- `<pasta>/poema.txt`: o texto, no formato dos poemas da Biblioteca (um verso por linha, estrofes
  separadas por linha em branco, marcas `::subtitulo`, `::data`…). Ortografia atual da língua,
  pelas edições correntes; a fonte de cada um está em `obras.json`.
- `<pasta>/glossario.json`: as notas.
- `<pasta>/traducao.txt` (opcional): uma tradução **em domínio público**, boa e com o nome do tradutor
  (pedido de 2026-10-20; nunca uma tradução nossa). Vai no botão «Português», ao lado do original, que
  continua a abrir primeiro. Ortografia atualizada (AO1990, com os acentos de Portugal nos portugueses).
  Em `obras.json`, o campo `traducao`: `tradutor`, `titulo`, `ano`, `publicacao` (frase da página «Sobre»)
  e `fonte`. Hoje: Fernando Pessoa (*O Corvo*, *Annabel Lee*) e Alphonsus de Guimaraens (*Canção do Outono*).

```bash
python ferramentas/lingua_original.py palavras <pasta>         # as palavras, com a posição e a chave
python ferramentas/lingua_original.py wiki <es|fr|en> <página> [<língua>]   # o verbete, só definições
python ferramentas/lingua_original.py conferir [<pasta>]       # cobre todas as palavras? campos certos?
python ferramentas/lingua_original.py publicar                 # grava conteudo/ (depois, o gerador do site)
```

## Licença

O Wiktionary é CC BY-SA 4.0: pode ser usado por terceiros, com atribuição (o link para o verbete
em cada nota e a página «Sobre este texto») e com as notas sob a mesma licença. A tradução da
definição é obra derivada e segue a mesma licença.

## Como fazer o glossário de um poema

1. `palavras <pasta>` lista cada palavra com a posição (`linha.posição`; a linha 0 é o título) e a
   chave (a palavra em minúsculas). Em francês, a elisão e o pronome depois do hífen já vêm
   separados (`l’` + `aube`, `vois` + `tu`).
2. Para cada chave, um verbete. A mesma chave vale para todas as ocorrências; se a palavra tem outro
   sentido noutro verso, crie outra chave (`fair#2`) e aponte a ocorrência em `ocorrencias`.
3. Consulte o Wiktionary pela ferramenta: na forma flexionada, primeiro a página da forma (ela diz
   de que lema é), depois a do lema. Ordem das fontes: o Wiktionary da própria língua (`es`, `fr`,
   `en`); se ele não tiver a palavra ou o sentido (arcaísmo, uso poético), o en.wiktionary na seção
   da língua (`"wiki": "en:Spanish"`, `"en:French"`); se nenhum tiver, `"wiki": null` e só a nota.
4. Campos (tudo em português do Brasil, **nunca mesóclise**):
   - `lema`: o título exato da página do Wiktionary de onde vem a definição;
   - `wiki`: só quando não é o Wiktionary da língua do poema (`"en:Spanish"`, `null`);
   - `classe`: «substantivo feminino», «verbo», «adjetivo», «advérbio», «preposição», «conjunção»,
     «artigo definido», «pronome pessoal», «pronome relativo», «interjeição»…;
   - `forma`: quando a palavra do poema não é o próprio lema: «plural», «feminino plural»,
     «futuro do indicativo, 3ª pessoa do singular», «particípio passado»…;
   - `def`: a definição do sentido usado no poema, **traduzida fielmente** da do Wiktionary (uma;
     duas no máximo, se o verso joga com as duas). Sem exemplos, sem enfeite, sem inventar sentido
     que o verbete não tem;
   - `nota`: só quando a definição sozinha não basta para entender a palavra no verso: sentido
     antigo ou figurado, tempo verbal fora de uso, sintaxe invertida, alusão, jogo de palavras.
     Uma a três frases. Explica a palavra; não traduz o verso inteiro;
   - palavra composta (inglês com hífen): `partes`, uma por elemento, cada uma com lema, classe,
     def (e wiki, forma), e a nota no verbete.
5. Palavras gramaticais (artigo, preposição, conjunção) levam definição curta e, em geral, nada de
   nota. Nome próprio: o verbete do Wiktionary, se houver; senão, `wiki: null` e a nota.
6. `conferir <pasta>` até dar «tudo certo».

Exemplo:

```json
{
  "verbetes": {
    "gesto": {"lema": "gesto", "classe": "substantivo masculino",
              "def": ["Expressão do rosto, ou o próprio rosto."],
              "nota": "Aqui, o rosto da dama: o sentido antigo, ainda vivo no século XVI."},
    "llevare": {"lema": "llevar", "classe": "verbo", "forma": "futuro do subjuntivo, 3ª pessoa do singular",
                "def": ["Transportar algo ou alguém de um lugar a outro."],
                "nota": "O futuro do subjuntivo quase sumiu do espanhol de hoje; o português ainda o usa: «a sombra que me levar»."},
    "thatch-eves": {"partes": [
        {"lema": "thatch", "classe": "substantivo", "def": ["Telhado de palha, junco ou material semelhante."]},
        {"lema": "eaves", "classe": "substantivo", "def": ["A borda inferior do telhado, que se projeta além da parede."]}],
      "nota": "«Eves» é a grafia da 1ª edição para «eaves»: o beiral dos telhados de palha das casas de campo."}
  },
  "ocorrencias": {"7.2": "fair#2"}
}
```
