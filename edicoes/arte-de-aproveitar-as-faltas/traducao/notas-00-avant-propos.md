# Notas do tradutor: A arte de aproveitar as próprias faltas, Advertência

Arquivo: `traducao/00-avant-propos.txt`. Texto-base: `original/00-avant-propos.txt` (6e édition, 1894, estabelecida do scan; ver `original/LEIAME.md`).

## O que foi conferido

- **Parágrafos:** 11 no original e 11 na tradução, na mesma ordem. São 12 blocos contando o título `## `.
- **Título:** um título `## ` nos dois arquivos: `## Avant-propos` → `## Advertência`, como manda o guia (§ 5).
- **Marcas, chamadas, notas:** nenhuma marca `[X.n]`, nenhuma chamada `[n]` e nenhuma nota `¤ [n]` no original; nenhuma na tradução. O Avant-propos não tem marca, como diz o LEIAME.
- **Cabeçalho:** só o `# titulo:` foi traduzido («Advertência»). As linhas `# fonte:`, `# edicao:` e `# nota:` estão iguais às do original.
- **Tamanho:** nenhum parágrafo com menos da metade do tamanho do original. O menor é o 6.º, com 0,81 do original.
- **Mesóclise:** o grep do CONVENCOES não achou nada. A varredura em Python com a mesma regex, terminada em `(?![A-Za-zÀ-ÿ])`, também não.
- **Versos e latim:** não há.

## Decisões gerais

- **Voz.** Tissot fala em *nous*, como autor. Ficou «nós»: «vemos», «quisemos», «acrescentamos», «Resta-nos».
- **O *on* do 4.º parágrafo** («on s'affectionne... on éprouve... l'on répète») tem valor geral: é quem lê o livro. Ficou na 1.ª pessoa do plural: «afeiçoamo-nos», «sentimos», «repetimos». É mais natural em português do que o «se» impessoal repetido três vezes. Inclui o leitor, como o *on* francês.
- **Título da obra no texto.** O guia (§ 1) manda deixar em francês os títulos de obras em francês. Aqui, porém, Tissot fala do próprio livro que se está traduzindo. Pus o título português da nossa edição, em itálico, com o artigo contraído, como o francês faz («de _l'Art_»):
  - «a sexta edição da _Arte de aproveitar as próprias faltas_»;
  - «a _Arte de aproveitar as próprias faltas_ contribui».

  Ver as dúvidas, abaixo.
- **Aspas:** angulares, como manda o guia (§ 6). A citação da religiosa está entre «...», com o ponto fora, como no original. Tirei os espaços franceses antes dos dois-pontos e dentro das aspas.
- **Maiúsculas:**
  - *Evêques* (com maiúscula no impresso) → «bispos», em minúscula, como no uso brasileiro.
  - «Coração de Jesus» com maiúscula e «este coração adorado» em minúscula, como Tissot escreve («au Cœur de Jésus» / «ce cœur adoré»).
  - O «Que» maiúsculo depois dos dois-pontos, no começo da prece, segue o original.
- **Data e assinatura:** «1er vendredi d'avril 1894» → «primeira sexta-feira de abril de 1894», por extenso. «JOSEPH TISSOT,» em versal, como no original. «_Missionnaire de saint François de Sales._» → «_Missionário de são Francisco de Sales._», em itálico, com «são» em minúscula (guia, § 4).

## Termos

| francês | tradução | observação |
|---|---|---|
| Avant-propos | Advertência | guia, § 5 |
| l'Art d'utiliser ses fautes | a _Arte de aproveitar as próprias faltas_ | título da nossa edição (ver as dúvidas) |
| opuscule | opúsculo | |
| fervents | fervorosos | guia, § 5 |
| le _Docteur de la piété_ | o _Doutor da piedade_ | guia, § 5; o itálico do original foi mantido |
| les inventions de la miséricorde divine | as invenções da misericórdia divina | «invenções» no sentido antigo de «engenhos, achados» |
| les prodigues | os pródigos | |
| le Père de famille | o Pai de família | |
| une grâce de relèvement | uma graça para se reerguer | |
| le bon Dieu | o bom Deus | guia, § 5 |
| contrister | contristar | |
| lettres approbatives | cartas de aprovação | |
| exactitude théologique | exatidão teológica | |
| les justes | os justos | |

## Passagens difíceis

- **1.º parágrafo, *voir paraître dans un format à prix réduit*.** Traduzi por «vemos sair, num formato de preço reduzido». «Sair» é o verbo corrente para livro publicado. *Nous sommes heureux de* virou «É com alegria que», para não ficar «Estamos felizes de ver».
- **2.º parágrafo, *ceux qui veulent le devenir*.** «Os que querem vir a sê-lo», com o *le* retomando «fervorosos».
- **2.º parágrafo, *leur dire les inventions*.** «Contar-lhes as invenções»: *dire* tem quatro objetos aqui («as invenções», «o amor», «o acolhimento», «os favores»), e «contar» os aceita melhor que «dizer».
- **2.º parágrafo, *l'amour compatissant qui poursuit les prodigues*.** «O amor compassivo que vai em busca dos pródigos». «Persegue» teria em português um tom hostil, que o francês não tem aqui: é o pai que sai atrás do filho para trazê-lo de volta.
- **3.º parágrafo, *le Sauveur aidant*.** O particípio absoluto ficou «com a ajuda do Salvador».
- **3.º parágrafo, *médite quelques lignes*.** «Medita algumas linhas desta obra», com o verbo transitivo, como no francês.
- **4.º parágrafo, *à les faire détester et éviter*.** «Para fazê-las detestar e evitar», com o causativo. O *les* (as faltas) fica claro pelo título que vem logo antes.
- **4.º parágrafo, *si libéralement*.** Ficou «com tanta liberalidade», para fazer par com «com tanta munificência».
- **4.º parágrafo, *un regret plus amoureux*.** «Um pesar mais amoroso». «Pesar» e não «arrependimento», porque *regret* não é aqui o termo técnico (*repentir*, *contrition*).
- **6.º parágrafo, *Afin de moins grossir ce volume*.** «Para engrossar menos este volume». *garantir l'exactitude* → «garantir-lhe a exatidão teológica» (*en* = do livro).
- **7.º parágrafo, *en lui consacrant pour la première fois ce travail, il y a seize ans*.** «Quando lhe consagramos pela primeira vez este trabalho, há dezesseis anos». É a primeira edição, de 1878.

## Remissões de página

Não há.

## Emendas

Nenhuma. O LEIAME não registra emenda neste trecho.

## Dúvidas para quem coordena

1. **Título do livro dentro do texto.** Pus o título português da edição, *A arte de aproveitar as próprias faltas*, em itálico. A alternativa seria seguir à letra o guia, § 1, e deixar *l'Art d'utiliser ses fautes* em francês. Convém fixar a forma no CONVENCOES, porque o título volta nos outros arquivos. Duas perguntas:
   - Com «próprias», como no título da edição, ou sem?
   - Contraído («da _Arte..._»), como pus, ou «de _A arte..._»?
2. **«Advertência» para *Avant-propos*.** Segui o guia. «Prefácio» ou «Ao leitor» também serviriam, mas «Advertência» é o termo tradicional para esse texto curto do autor sobre a edição.
3. **Epígrafe da página de rosto.** A epígrafe *Misericordias Domini in æternum cantabo* (Ps. LXXXVIII) ficou fora do texto-fonte, e o LEIAME pede uma decisão. Se entrar, o lugar natural é antes desta Advertência ou no rosto da edição. Ficaria em latim, em itálico, com «[Trad.: Cantarei eternamente as misericórdias do Senhor]» se o guia pedir.
