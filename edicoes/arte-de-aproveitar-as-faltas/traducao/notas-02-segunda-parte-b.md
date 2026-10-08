# Notas do tradutor: A arte de aproveitar as próprias faltas, Segunda parte, capítulos V a VIII

> Depois destas notas, as quatro partes foram harmonizadas. Onde houver divergência, valem `HARMONIZACAO.md` e a seção 8 do `CONVENCOES.md`.

Arquivo: `traducao/02-segunda-parte-b.txt`. Texto-base: `original/02-segunda-parte-b.txt` (6e édition, 1894, estabelecida do scan; ver `original/LEIAME.md`). A tradução foi escrita inteira por outro tradutor, que não chegou a conferi-la. Nesta revisão, ela foi conferida contra o original, parágrafo a parágrafo, e corrigida onde foi preciso (ver «Correções desta revisão», abaixo).

## O que foi conferido

- **Blocos:** 244 no original e 244 na tradução, na mesma ordem: 136 parágrafos de texto, 4 títulos `## ` e 104 notas `¤ [n]`. São as contagens do LEIAME.
- **Linhas:** 492 nos dois arquivos, com as linhas em branco nos mesmos lugares.
- **Títulos:** os quatro `## Chapitre V…VIII` viraram `## Capítulo V…VIII`, com o título traduzido.
- **Marcas `[X.n]`:** `[II.5]`, `[II.6]`, `[II.7]`, `[II.8]`, no começo do primeiro parágrafo de cada capítulo, iguais e na mesma ordem.
  - A conferência rápida que acusou diferença de marcas contava o arquivo inteiro, cabeçalho incluído. A linha `# nota:` do original menciona «[I.1]», e a tradução tinha perdido as linhas `# fonte:`, `# edicao:` e `# nota:`. Ver «Correções desta revisão», item 1.
  - Agora o arquivo inteiro dá a mesma sequência nos dois lados: `[I.1]` (no cabeçalho), `[II.5]`, `[II.6]`, `[II.7]`, `[II.8]`.
- **Números de parágrafo do autor:** os «1. —», «2. —»… estão iguais, nos mesmos parágrafos. No capítulo VIII o impresso numera 1, 2, 2, 3, 5, 6…, sem o 4. Ficou assim (ver as dúvidas).
- **Chamadas e notas:** as 104 chamadas `[1]`…`[104]` e as 104 notas `¤ [1]`…`¤ [104]` estão iguais, na mesma ordem e nos mesmos parágrafos.
- **Cabeçalho:** só o `# titulo:` foi traduzido («Segunda parte, capítulos V a VIII»). As outras três linhas estão iguais às do original, como em `00-avant-propos.txt` e `01-primeira-parte.txt`.
- **Tamanho:** nenhum bloco com menos da metade do tamanho do original. O menor é a nota 30 («II Macchab. I, 19» → «2 Mc I, 19»), com 0,72, por causa da abreviação.
- **Pontuação, por bloco:** os «», os «!», os «?» e as reticências batem com o original em todos os blocos.
  - Os casos de aspas desemparelhadas são do impresso e foram mantidos:
    - o «» final do 4.º bloco (Crisóstomo);
    - o «» final da citação de santo Tomás e são Gregório (n.º 4 do cap. VII), registrado no `emendas.txt`, p. 142.
- **Itálicos:** os `_…_` batem com o original, salvo em quatro notas em latim, onde a tradução pôs itálico (ver «Decisões gerais»).
- **Mesóclise:** o grep do CONVENCOES não achou nada, nem a varredura em Python com a mesma regex terminada em `(?![A-Za-zÀ-ÿ])`.
- **Versos:**
  - Não há versos em francês.
  - A nota 95 traz três versos latinos de uma prosa («Peccatores non exhorres / Sine quibus numquam fores / Tanto digna filio»). Ficaram em latim, como no original, na mesma linha, com as barras.

## Decisões gerais

- **Tratamento.** Segue o original, passagem por passagem:
  - **vós:** São Francisco às dirigidas e aos dirigidos; Tissot à Virgem (cap. VIII, n.º 12, e a oração final); a Madre de Chantal às filhas; Crisóstomo a Teodoro.
  - **tu:**
    - a alma falando a si mesma (cap. V, n.º 6: «Ó minha alma, lembra-te»);
    - o apelo ao pecador (cap. VIII: «Treme, pecador», «olha para Maria, pensa n'Ela»);
    - São Francisco ao «meu filho» do *Tratado* (cap. VII, n.º 2);
    - Nosso Senhor a são Pedro («por que duvidas?») e a santa Matilde (nota 53).
  - **nós:** a voz de Tissot.
- **Maiúsculas.** As de reverência do original ficaram: *Ela*, *Elle* (Maria), *Santos*, *Bem-aventurado Pai*, *Bem-aventurado Bispo*, *Doutor*, *Teólogo*, *Religioso*.
- **Título do livro dentro do texto.** *de l'Art d'utiliser ses fautes* → «da _Arte de aproveitar as próprias faltas_» (cap. V, n.º 6, e cap. VI, n.º 1). É a mesma solução de `00-avant-propos.txt`, que está nas dúvidas daquele arquivo.
- **Referências bíblicas:** abreviadas à portuguesa, como em `01-primeira-parte.txt`: Eclo, Sl, Lc, Mt, Rm, Tg, Jó, Is, Lm, Os, 1 Cor, 2 Mc, Lv, Ct, At, Ef. A numeração dos Salmos é a da Vulgata, como no original.
- **Latim:** fica em latim, como no original, sem «[Trad.: …]», que o guia da obra não pede.
  - Nas notas 24, 42, 75 e 95, o latim está em redondo no original. Pus em itálico, pela regra geral (palavra estrangeira em itálico). `01-primeira-parte.txt` fez o mesmo (nota 94).
- **Referências das cartas:** «Lettre à une Dame, 835e ; édit. Meyer» → «Carta a uma senhora, 835.ª; edição Meyer»; «collect. Blaise» → «coleção Blaise»; «Entretien XVIe» → «Colóquio XVI»; «Instruction XIIe» → «Instrução XII»; «_De l'amour de Dieu_» → «_Do amor de Deus_»; «_Traité de l'amour de Dieu_» → «_Tratado do amor de Deus_»; «_Introd. à la vie dévote_» → «_Introd. à vida devota_».
- **Títulos de outras obras:** ficaram em francês (ou latim, ou italiano), em itálico, como manda o guia: _Manuel des âmes intérieures_, _Il Direttore della perfezione cristiana_, _l'Art de la Perfection chrétienne_, _le Charme du divin amour_, _De la vie et des vertus chrétiennes_, _Mois de Marie de l'Immaculée Conception_, _Vie intérieure de la Très Sainte Vierge_, _Livre de la grâce spéciale_, _Physiologue_.
  - «Avis aux confesseurs» (nota 27), obra de São Francisco, virou _Avisos aos confessores_, pela exceção do guia.
- **Abreviaturas:** «S. Greg.» → «São Greg.»; «S. Thomas» → «Santo Tomás»; «Saint Thom.» → «Santo Tomás»; «Mgr Ch. Gay» → «Dom Ch. Gay»; «P. Gratry» → «Padre Gratry» (no começo da nota, com maiúscula); «M. Olier» → «o senhor Olier».
  - Os autores citados em latim ficaram como estão: «Laurent. a Ponte», «Borgius de Gubbio», «Philippus Abbas», «Idiota», «Cornel. a Lap.», «Guillelm. apud Delrio».
- **Citações da Filoteia** (notas 25 e 26: I.19 e II.19). A nossa tradução da Filoteia só tem, por enquanto, a oração e o prefácio. As duas passagens foram traduzidas diretamente do texto que Tissot cita e devem ser harmonizadas quando aqueles capítulos existirem.

## Termos

| francês | tradução | observação |
|---|---|---|
| utiliser ses fautes | aproveitar as faltas | guia, § 5; nos títulos dos capítulos, sem «próprias», como em `01` |
| s'affermir dans la persévérance | firmar-se na perseverança | título do cap. V |
| ressentiments (da febre) | achaques | cap. V, n.º 2: as sequelas que ficam depois da doença |
| occasions volontaires | ocasiões voluntárias | |
| les industries | os recursos; os expedientes; os recursos (do médico) | cap. V, n.º 6; cap. VII, n.º 1; cap. VIII, n.º 11 |
| accusation; aveu | acusação; confissão | cap. VI |
| _Actes du Pénitent_ | _Atos do penitente_ | |
| contrition; repentir; regret | contrição; arrependimento; pesar | guia, § 5 |
| satisfaction; satisfaire | satisfação; satisfazer | guia, § 5 |
| eau-de-vie; ardente | _água-da-vida_; _ardente_ | cap. VI, n.º 2: o jogo de São Francisco depende da forma literal |
| onctueux | suave | cap. VI, n.º 4 |
| dilection | dileção | |
| componction | compunção | |
| thériaque | teriaga | |
| archi-vierge | arquivirgem | |
| navrer (le cœur) | ferir | cap. VII, n.º 7 |
| élans | impulsos (cap. VII, n.º 1); arroubos (cap. VII, n.º 7, «élans amoureux») | |
| coulpe | culpa | |
| retardement | atraso | |
| Refuge des pécheurs; Mère de la miséricorde | Refúgio dos pecadores; Mãe da misericórdia | |
| médiatrice; avocate | medianeira; advogada | |
| département (de Marie) | pasta | cap. VIII, n.º 2: a imagem do ministério |
| _Pasce hædos meos, paissez mes boucs_ | _Pasce hædos meos, apascentai os meus bodes_ | segue o *vous* do francês de Tissot, não o *tu* do latim |
| _ses malades_; _suit_ ses malades | _seus doentes_; _acompanha_ os seus doentes | cap. VIII, n.º 11 |
| Secrète | Secreta | nota 91 |
| écu | escudo | a moeda |
| le Bienheureux Évêque; notre aimable Docteur; l'Apôtre du Chablais | o Bem-aventurado Bispo; o nosso amável Doutor; o Apóstolo do Chablais | |

**Nomes:**

- são João Crisóstomo, Teodoro, santo Epifânio, Vítor (bispo de Cartago);
- o padre Pinamonti, o padre Grou, o padre Du Pont;
- são Gregório, santo Agostinho, santo Anselmo, santo Tomás, santo Ambrósio, são Bernardo;
- o cura d'Ars;
- Benigna Gojos, santa Matilde (*Mecthilde*), santa Chantal;
- Simão, o Leproso; Madalena, santa Maria Madalena; Sedecias, Jeremias, Neemias; Absalão, no vale de Josafá;
- Nossa Senhora do Porto, em Clermont; Valência;
- são Germano de Constantinopla, santo Antonino, o cardeal Hailgrin, Ricardo e Hugo de São Vítor, Cristóvão de Vega;
- são Gregório Nazianzeno (guia da Filoteia), são Boaventura, são Pedro Damião;
- santa Brígida, santa Gertrudes;
- o senhor Olier, são Tomás de Vilanova;
- Ester, Rute, Jessé, Simeão;
- Estrasburgo.

## Passagens difíceis

- **Cap. V, n.º 1, *nos chutes nous doivent porter... à nous tenir mieux sur nos gardes*.** «Devem levar-nos... a estar mais de sobreaviso». A mesma locução volta no n.º 2 e no n.º 5 («estar tanto mais de sobreaviso»).
- **Cap. V, n.º 2, *ne nous retenaient en bride*.** «Não nos retivessem pela rédea». A primeira redação, «não nos tivessem de rédea», não é locução portuguesa (ver as correções).
- **Cap. V, n.º 3, a nota 8 (*un saint de premier calibre*).** «Um santo de primeira grandeza». O fim da nota, «Dieu le veut.», é emenda conjectural do texto-fonte (`emendas.txt`, p. 117 n3). Traduzi «Deus o quer.».
- **Cap. V, n.º 4, *se tenant fort assuré de la longueur de sa vertu*.** «Tendo-se por muito seguro pela longa duração da sua virtude». *Hors de ses escalades*: «a salvo de escaladas». A imagem é a da praça sitiada.
- **Cap. V, n.º 5, *vous donnant à lui sans déguisement*.** O gerúndio francês ficou gerúndio: «entregando-vos a ele... e dizendo-lhe». A primeira redação punha uma condição («se vos entregardes») que o francês não tem.
- **Cap. VI, n.º 2, os rubis da Etiópia.** A frase do Santo é anacolútica: «des rubis... qui ont... leur feu fort blafard, mais étant mis dans le vinaigre, il éclate». A tradução reproduz o anacoluto («mas que, postos no vinagre, ele resplandece»), em vez de arrumar a frase. *Aigreur de la pénitence* → «amargor da penitência». «Azedume» seria mais literal, mas soa pejorativo.
- **Cap. VII, n.º 6, *de tant plus belle que la contrition et l'amour avec lequel elle fit pénitence*.** O francês de São Francisco é elíptico. A tradução completa o segundo termo: «tanto mais bela quanto maiores foram a contrição e o amor com que fez penitência».
- **Cap. VII, n.º 3, *Que la pénitence confère...*, nous l'avons prouvé.** A oração com «que» anteposta pede subjuntivo em português: «Que a penitência confira... nós o provamos» (corrigido nesta revisão).
- **Cap. VIII, nota 59, *on sait ce que c'est qu'un navire désemparé*.** O jogo entre *desemparados* e *désemparé* (o navio sem mastros nem governo) passa: «sabe-se o que é um navio desamparado». «Desamparado» não é o termo náutico português, mas é o que guarda o jogo. O espanhol *Nostra Senora de los desemparados* ficou com a grafia do impresso (é *Nuestra Señora de los Desamparados*).
- **Cap. VIII, n.º 1, *les _tourner à profit_* (nota 61, At XXVII, 21).** «Convertê-las em ganho». O itálico marca a alusão ao *lucrique facere* da Vulgata, no naufrágio de são Paulo.
- **Cap. VIII, n.º 6, *pense à Elle*.** Ficou «pensa n'Ela», para guardar a maiúscula de reverência que Tissot dá a *Elle* em todo o capítulo (ver as dúvidas).
- **Cap. VIII, n.º 7, *le sang éteint*.** «O sangue apagado», literal. Logo depois, o mesmo autor diz *le sang mort*, «o sangue morto».
- **Cap. VIII, n.º 11, *le voulons-nous ? Marie nous adoptera*.** A pergunta retórica ficou («queremos? Maria nos adotará»), sem virar condicional.
- **Cap. VIII, n.º 12, *Plus je me rappellerai..., plus je vous rappellerai..., plus je me tiendrai assuré*.** «Quanto mais..., tanto mais..., tanto mais». *À moitié guérison*: «no meio da cura».
- **O fecho do livro.** O último parágrafo cita *Misericordias Domini in æternum cantabo* (nota 104, Sl LXXXVIII). É a epígrafe da página de rosto que o LEIAME deixou fora. Aqui ela está no texto e foi mantida em latim, em itálico, como no original.

## Remissões de página

- **Nota 58, «Pages 84 et 190».** Remete à paginação da 3.ª edição (`emendas.txt`, p. 149 n1). Foi trocada, como manda o guia (§ 1), por remissão aos lugares desta tradução: «Na primeira parte, capítulo III, n.º 7, e na segunda parte, capítulo IV, n.º 2, em nota.»
  - A identificação é por conteúdo, não por página. Tissot diz que «tocou o assunto» de Maria refúgio dos pecadores no correr da obra. São dois os lugares onde o faz:
    - o fim de I.3, n.º 7: a confissão do demônio («Je n'ai point de Marie») e o «Marie pour nous en obtenir la grâce : qui donc peut désespérer ?»;
    - a nota 108 de `02-segunda-parte-a.txt`, em II.4, n.º 2: a Igreja nos faz apresentar à Virgem «notre titre de pécheurs».
  - As proporções batem com 84 e 190 numa edição mais longa: a primeira passagem cai no fim da primeira parte; a segunda, perto do meio da segunda.
- **Outras remissões:** «_le Charme du divin amour_, page 128» (nota 36) e «_Vie intérieure de la Très Sainte Vierge_, p. 352» (nota 92) remetem a outros livros e ficaram, traduzidas só as palavras comuns («página 128», «p. 352»).

## Emendas

Nenhuma emenda nova. As do texto-fonte que caem neste arquivo (`emendas.txt`, págs. 117–165) foram seguidas:

- p. 117 n3: «Dieu le veut.» (nota 8), emenda conjectural;
- p. 121: *paternel*;
- p. 124–125: *en ce moment*, «O mon âme, souviens-toi», «ces peines, de ces»;
- p. 129: a chamada da nota 28, reposta depois de «Alexandre»;
- p. 152–153: *nécessaire*, *marine ou*;
- p. 165: *ils ont mis*, *mes*.

Referências erradas do impresso, mantidas como estão:

- **Já registradas no `emendas.txt`:**
  - Jó XXX, 33 (é XXXI, 33), cap. VI, n.º 1;
  - «Pages 84 et 190», trocada como se diz acima.
- **Não registradas no `emendas.txt`:**
  - Lc VII, 48, no cap. VII, n.º 3. *Celui à qui il est moins pardonné, aime moins* é VII, 47.
  - Lc VII, 35, no cap. VII, n.º 6. *Mulier erat in civitate peccatrix* é VII, 37.
  - Sl LXXXIII, na nota 74. *Justitia de cælo prospexit... Terra dedit fructum suum* é o Sl LXXXIV da Vulgata.

## Correções desta revisão

1. **Cabeçalho.** Faltavam as linhas `# fonte:`, `# edicao:` e `# nota:`, que o guia (§ 1) manda copiar iguais. Foram repostas, iguais às do original.
   - Era essa a causa da diferença de marcas acusada pela conferência rápida: a linha `# nota:` do original contém «[I.1]».
   - O texto já tinha as quatro marcas `[II.5]`…`[II.8]` no lugar certo.
2. **Cap. V, n.º 2:** «não nos tivessem de rédea» → «não nos retivessem pela rédea» (*ne nous retenaient en bride*).
3. **Cap. V, n.º 5:** «seremos logo furados e trespassados» → «perfurados e trespassados» (*percés et transpercés*). «Furados» era baixo demais para o tom.
4. **Cap. V, n.º 5:** «apreciará a vossa boa vontade, se vos entregardes a ele... dizendo-lhe» → «apreciará a vossa boa vontade, entregando-vos a ele... e dizendo-lhe». O francês tem gerúndio, não condição.
5. **Cap. VII, n.º 1:** «lhe faz dar os arroubos do fervor da devoção» → «lhe faz dar os impulsos do fervor de devoção» (*les élans de la ferveur de dévotion*). «Arroubo» é êxtase; *élan* é impulso.
6. **Cap. VII, n.º 3** (Madre de Chantal): «reparemos as nossas faltas e obtenhamos o seu perdão» → «e delas obtenhamos o perdão» (*et en obtenions le pardon*). «O seu perdão» ficava ambíguo, como se fosse o perdão de Deus, quando é o perdão das faltas.
7. **Cap. VII, n.º 3** (Crisóstomo): «Que a penitência confere» → «Que a penitência confira» (subjuntivo na oração anteposta).
8. **Cap. VIII, n.º 11:** «só deles depende... tornar-se _seus bodes_ e ser em breve convertidos» → «tornarem-se _seus bodes_ e serem em breve convertidos». O infinitivo pessoal concorda com «convertidos».
9. **Cap. VIII, n.º 12:** «a meio da cura» → «no meio da cura» (uso brasileiro).

O resto da tradução foi conferido e mantido: sentido, integridade, chamadas, notas, tratamento e termos estavam certos.

## Dúvidas para quem coordena

1. **Remissão da nota 58.** Confirmar a identificação dos dois lugares (I.3, n.º 7, e a nota 108 de II.4, n.º 2). Se a 3.ª edição for consultada, as páginas 84 e 190 resolvem a questão. Se não se quiser arriscar, a alternativa é manter «Páginas 84 e 190» com «[Trad.: paginação da 3.ª edição]».
2. **Numeração do capítulo VIII** (1, 2, 2, 3, 5, 6…, sem o 4). Está assim no impresso, conferido contra a imagem (`revisado/039.txt`, `040.txt`). Ficou como está. Corrigir (o segundo «2.» para «3.», o «3.» para «4.») seria emenda do autor e, se for feita, deve entrar no `emendas.txt` e no original também.
3. **«pensa n'Ela»** (cap. VIII, n.º 6). A contração com apóstrofo guarda a maiúscula de reverência, mas é de uso antigo ou devocional. As alternativas são «pensa nela», que perde a maiúscula, ou «pensa em Maria», que acrescenta o nome. Convém fixar a forma no CONVENCOES, se voltar.
4. **Referências erradas que não estão no `emendas.txt`:** Lc VII, 48; Lc VII, 35; Sl LXXXIII. Proponho acrescentá-las à lista, como as outras.
5. **Itálico no latim das notas** (24, 42, 75, 95), que o original dá em redondo. Segui a regra geral e `01-primeira-parte.txt`. Se o coordenador preferir a tipografia do impresso, é tirar quatro pares de `_`.
6. **Epígrafe *Misericordias Domini in æternum cantabo*.** O livro termina com ela (última frase antes de «Amém! Amém! Amém!»). Isso pesa a favor de pô-la também no rosto da edição, como o LEIAME e as notas da Advertência propõem.
