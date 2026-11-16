# Apologia pro Vita Sua, de John Henry Newman: texto inglês de trabalho

Arquivos `00-prefacio.txt` a `20-notas-adicionais.txt`, gerados por `montar.py` (`python3 -I montar.py <22088-0.txt>`).
UTF-8, cabeçalho `# chave: valor`, um parágrafo por bloco, linha em branco entre eles. O texto baixado não está no
repositório (ficou em `~/.cache/claude-pedidos-1611/tmp-apologia-newman/`, só neste PC).

## Fonte e edição

- Fonte: Project Gutenberg, eBook nº 22088 (lançado em 16/07/2007), arquivo `22088-0.txt` (revisão de 14/05/2024),
  baixado do espelho `mirrors.xmission.com/gutenberg/2/2/0/8/22088/` porque o gutenberg.org estava em manutenção.
  Produzido por Steven Giacomelli, David King e a equipe do Distributed Proofreaders, sobre imagens do Internet
  Archive (Canadian Libraries); as imagens das páginas estão no próprio Gutenberg (`22088-page-images/`, f001.png…),
  para conferência.
- Edição: _Apologia pro Vita Sua: being a History of his Religious Opinions_, Londres, Longmans, Green, and Co., 1890
  (folha de rosto reproduzida no Gutenberg). É a **forma final** da obra, e não a de 1864 (Gutenberg #19690, fora):
  - o prefácio, de 2 de maio de 1865, diz que esta edição tira as partes 1 e 2 de 1864 (a polêmica direta com
    Kingsley), salvo os trechos postos depois do prefácio, numera as partes 3 a 7 como capítulos I a V e reduz o
    apêndice às Notas A a G (A e D novas, B em parte nova);
  - o título com «Apologia pro Vita Sua» à frente é o de 1873 (em 1865 saiu como _History of my Religious Opinions_);
  - os acréscimos posteriores estão aí: a nota de rodapé sobre a volta a Oxford em 1878, as «Additional Notes» (de
    1873 a 1878) e a lista de obras «corrected up to 1890».
- Domínio público: Newman morreu em 1890.

## O que foi tirado

- As linhas `*** START` e `*** END` do Gutenberg (este arquivo não traz a licença longa nem notas do transcritor).
- A folha de rosto (título, epígrafe de Sl 36,5-6 em inglês, editora) e o sumário («Contents»), que passam para o
  `obra.py`, e o título «My Religious Opinions» que abre a narrativa.
- Os títulos de cada capítulo e de cada nota, que vão para o `# titulo:` do arquivo.
- Dos quatro suplementos («Supplemental Matter»), **ficam de fora o I e o II**: a lista cronológica das cartas e
  papéis citados, com as páginas da edição de 1890, e a lista das obras do autor (bibliografia de editora). Entram o
  III (carta do bispo Ullathorne) e o IV (as mensagens do clero e dos leigos). Ver `../FALTA.md`, dúvidas.

## Como ficou o texto

- Linhas quebradas a 72 colunas juntadas; espaços repetidos colapsados; recuo das citações em bloco descartado (a
  citação vira parágrafo próprio, como no impresso).
- Mantidos como no Gutenberg: aspas retas `"` e `'`, travessão `--`, itálico `_assim_` (o Gutenberg o marca), grafia
  britânica e a do autor (`shew`, `connexion`), referências bíblicas no formato do autor (`Matt. xxiv. 15.`), as
  remissões a páginas da edição de 1890 (títulos das notas: «Note A, on page 14»; «Vide supr. p. 219»).
- Únicas correções: «EXTRACT OF A LETTER **PROM** THE REV. E. SMEDLEY» → «FROM» (erro de digitação, nas notas adicionais), e a ligadura que o Gutenberg escreve `[oe]` virou `œ` (manœuvre, Syro-Phœnician, pomœria, Cœlestius).
- Quebras de seção do autor (cinco asteriscos) → parágrafo `* * *`. Títulos internos → `## ` («§ 1.» e «§ 2.» no
  capítulo IV; «Protest.» no III; nas mensagens do clero, cada diocese; nas notas adicionais, «Note on page …» e o
  título de cada uma, e os números das quatro cartas de Whately). Títulos em caixa alta passaram a caixa de título.
- **Notas de rodapé do autor** (21 no livro; no Gutenberg, numeradas de 1 a 21 e postas logo depois do parágrafo):
  renumeradas a partir de 1 em cada arquivo, a chamada `[n]` no lugar e o texto num parágrafo `¤ [n] …` no fim do
  arquivo (o site as mostra no fim da página como «Notas do autor», formato da _Democracia na América_).
- Versos: só dois trechos, ambos em latim, em `| ` linha a linha: «Victrix causa diis placuit…» (Lucano; cap. IV, 3ª
  parte) e a fala de Penteu e Baco (Horácio, Epístolas I,16; Nota A).
- **Nota D, o calendário dos santos ingleses** (1843): cada linha da lista vai em `| ` só para guardar as quebras (não
  é verso; os dias vazios ficam, como no impresso); os títulos dos meses, séculos e partes em `## `; as chaves do
  impresso, que agrupam santos («Daughters of King Penda», «Companions of St. Boniface»…), viram uma linha
  `| } rótulo` logo depois do grupo (seis grupos, listados em `CAL_GRUPOS` no `montar.py`).

## A divisão

Capítulo com mais de ~12 mil palavras foi cortado em partes, sempre numa quebra `* * *` do autor (a marca do corte sai):

| arquivo | conteúdo | corte |
|---|---|---|
| `00-prefacio.txt` | Prefácio (1865) e os trechos de 1864 | — |
| `01-capitulo-1.txt` | Cap. I, até 1833 | — |
| `02-capitulo-2a.txt`, `03-capitulo-2b.txt` | Cap. II, 1833–1839 | antes de «I suspect it was Dr. Pusey's influence…» (as obras de defesa do Movimento) |
| `04-capitulo-3a.txt`, `05-capitulo-3b.txt` | Cap. III, 1839–1841 | antes de «Now to trace the succession of thoughts…» (depois do abalo de 1839) |
| `06-…4a`, `07-…4b`, `08-capitulo-4c.txt` | Cap. IV, 1841–1845 | antes de «One calumny there was…» (a calúnia de estar a serviço de Roma; o «§ 2.» do autor fica no meio da 2ª parte) e antes de «Such was the object and the origin of the projected Series…» |
| `09-capitulo-5a.txt`, `10-capitulo-5b.txt` | Cap. V, desde 1845 | antes de «There is only one other subject…» (a reserva e a «economia») |
| `11-nota-a.txt` … `17-nota-g.txt` | Notas A a G | — |
| `18-carta-do-bispo.txt` | Suplemento III | — |
| `19-cartas-do-clero-e-leigos.txt` | Suplemento IV | — |
| `20-notas-adicionais.txt` | Notas adicionais 1–8 | — |

Contagem de palavras de cada arquivo: `../FALTA.md`.
