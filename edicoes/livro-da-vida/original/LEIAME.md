# Livro da Vida: o texto castelhano

**Edição-base:** Silverio de Santa Teresa (Julián Gómez Fernández, OCD, 1878–1954), *Obras de Santa Teresa
de Jesús*, t. I, *Libro de la Vida* (Burgos, El Monte Carmelo, 1915; Biblioteca Mística Carmelitana, 1),
feita sobre o autógrafo do Escorial. Silverio morreu em 1954: domínio público no Brasil; nos EUA, publicado
em 1915, também. Fac-símile: Internet Archive `BMC1ObrasDeSantaTeresaDeJessTomoILibroDeLaVida`.

**Testemunhos para corrigir a leitura** (só OCR, nenhum vai ao site):
- Vicente de la Fuente, *Escritos de Santa Teresa*, t. I (BAE 53; Madrid, 1861, reimpr. 1877), Internet
  Archive `bibliotecadeauto53madruoft`: também do autógrafo, com pontuação e algumas formas diferentes.
- *La vida de la Madre Teresa de Jesús escrita de su misma mano* (Estrasburgo, Heitz, Bibliotheca Romanica,
  s.d.), Internet Archive `lavidaesentadesu00tere`: transcrição na grafia do autógrafo (*an mandado*).
- (Não serve: o Wikisource es transcreve a Espasa-Calpe de 1927, sem revisão; o Gutenberg não tem a obra.)

**Como foi feito** (scripts em `../fonte/`, dados em `~/.cache/claude-pedidos-0511/livro-da-vida/`, só neste PC):
`hocr.py` (linhas com coordenadas do hOCR de 1915) → `extrair.py` (tira cabeços e notas de rodapé pelo passo
das linhas; parágrafo pelo recuo) → `montar.py` (prólogo, 40 capítulos, epílogo) → `corrigir.py` (erros de
OCR por regra, só quando a forma certa existe no próprio texto ou nos outros testemunhos: *g* → *y*, *rn* →
*m*, *fi* → *ñ*, *j* → *¡*…; registro em `correcoes.tsv`) → `titulos.py` (títulos dos capítulos pelo índice
de 1915, que os traz em caixa baixa) → `gravar_original.py`. As dúvidas que sobraram (`duvidas.tsv`) foram
decididas com o contexto dos três testemunhos (ver `FALTA.md`).

**Divisão e marcas:** prólogo (`00.txt`), capítulos 1–40 (`01.txt`…`40.txt`), epílogo, a carta a García de
Toledo (`41.txt`). `[c.p]` = capítulo.parágrafo: os parágrafos de 1915, numerados por nós. As notas de
Silverio ficaram de fora. As chamadas «Jhs.» ficam como linhas.
