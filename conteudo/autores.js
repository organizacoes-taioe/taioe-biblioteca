/* Autores da biblioteca.
   Para acrescentar um autor, copie o modelo abaixo; o id é usado nas rotas (#/a/<id>)
   e no campo "autor" de cada obra. "ordem" (sobrenome, nome) não ordena mais a lista: desde 07/10/2026 ela segue o nome como está escrito. */

BIBLIOTECA.autor({
  id: 'machado-de-assis',
  nome: 'Machado de Assis',
  nomeCompleto: 'Joaquim Maria Machado de Assis',
  vida: '1839–1908',
  ordem: 'Assis, Machado de',
  nota: 'Romancista, contista, poeta e cronista carioca; fundador da Academia Brasileira de Letras.'
});

/* Catolicismo ("area": a pasta da capa; sem ela, o autor fica em Literatura) */

BIBLIOTECA.autor({
  id: 'santa-teresinha',
  area: 'catolicismo',
  nome: 'Santa Teresinha',
  nomeCompleto: 'Teresa do Menino Jesus e da Sagrada Face (Thérèse Martin)',
  vida: '1873–1897',
  ordem: 'Teresinha do Menino Jesus, Santa',
  nota: 'Carmelita de Lisieux, doutora da Igreja. Obras em tradução do francês, com o original ao lado.'
});

BIBLIOTECA.autor({
  id: 'santo-atanasio',
  area: 'catolicismo',
  nome: 'Santo Atanásio',
  nomeCompleto: 'Atanásio de Alexandria',
  vida: '~296–373',
  ordem: 'Atanásio, Santo',
  nota: 'Bispo de Alexandria, doutor da Igreja, defensor da fé de Niceia contra os arianos. Em tradução do grego.'
});

BIBLIOTECA.autor({
  id: 'santo-agostinho',
  area: 'catolicismo',
  nome: 'Santo Agostinho',
  nomeCompleto: 'Aurélio Agostinho de Hipona',
  vida: '354–430',
  ordem: 'Agostinho, Santo',
  nota: 'Bispo de Hipona, doutor da Igreja, convertido em Milão em 386. Em tradução do latim.'
});

BIBLIOTECA.autor({
  id: 'dom-chautard',
  area: 'catolicismo',
  nome: 'Dom Chautard',
  nomeCompleto: 'Jean-Baptiste Chautard',
  vida: '1858–1935',
  ordem: 'Chautard, Dom',
  nota: 'Monge trapista, abade de Sept-Fons. Em tradução do francês, com o original ao lado.'
});

BIBLIOTECA.autor({
  id: 'sao-francisco-de-sales',
  area: 'catolicismo',
  nome: 'São Francisco de Sales',
  nomeCompleto: 'Francisco de Sales (François de Sales)',
  vida: '1567–1622',
  ordem: 'Francisco de Sales, São',
  nota: 'Bispo de Genebra, com sede em Annecy, doutor da Igreja, fundador da Visitação com santa Joana de Chantal. Em tradução do francês, com o original ao lado.'
});

BIBLIOTECA.autor({
  id: 'joseph-tissot',
  area: 'catolicismo',
  nome: 'Joseph Tissot',
  nomeCompleto: 'Joseph Tissot',
  vida: '1840–1894',
  ordem: 'Tissot, Joseph',
  nota: 'Superior-geral dos Missionários de São Francisco de Sales, de Annecy. Em tradução do francês, com o original ao lado.'
});

BIBLIOTECA.autor({
  id: 'g-k-chesterton',
  area: 'catolicismo',
  nome: 'G. K. Chesterton',
  nomeCompleto: 'Gilbert Keith Chesterton',
  vida: '1874–1936',
  ordem: 'Chesterton, G. K.',
  nota: 'Escritor e jornalista inglês, convertido ao catolicismo em 1922. Em tradução do inglês.'
});

/* As orações em latim, na língua original, com nota em cada palavra (edicoes/lingua-original), sob o
   nome «Orações»; «nome» logo depois de «id», como os Cards o leem. */
BIBLIOTECA.autor({
  id: 'oracoes',
  nome: 'Orações',
  area: 'catolicismo',
  nomeCompleto: 'Orações tradicionais da Igreja',
  coletivo: true,   // não é uma pessoa: as páginas não o dão como autor (schema.org Person)
  nota: 'Em latim, no texto do Missal e do Breviário romanos, sem tradução.'
});

/* Poetas (poemas publicados a partir do Versificador; ver ferramentas/poesia.py) */

BIBLIOTECA.autor({
  id: 'alberto-de-oliveira',
  nome: 'Alberto de Oliveira',
  nomeCompleto: 'Antônio Mariano Alberto de Oliveira',
  vida: '1857–1937',
  ordem: 'Oliveira, Alberto de',
  nota: 'Poeta parnasiano fluminense, da tríade com Olavo Bilac e Raimundo Correia.'
});

BIBLIOTECA.autor({
  id: 'alphonsus-de-guimaraens',
  nome: 'Alphonsus de Guimaraens',
  nomeCompleto: 'Afonso Henriques da Costa Guimarães',
  vida: '1870–1921',
  ordem: 'Guimaraens, Alphonsus de',
  nota: 'Poeta simbolista mineiro, o poeta da morte da amada.'
});

BIBLIOTECA.autor({
  id: 'alvares-de-azevedo',
  nome: 'Álvares de Azevedo',
  nomeCompleto: 'Manuel Antônio Álvares de Azevedo',
  vida: '1831–1852',
  ordem: 'Azevedo, Álvares de',
  nota: 'Poeta da segunda geração romântica, morto aos vinte anos.'
});

BIBLIOTECA.autor({
  id: 'antero-de-quental',
  nome: 'Antero de Quental',
  nomeCompleto: 'Antero Tarquínio de Quental',
  vida: '1842–1891',
  ordem: 'Quental, Antero de',
  nota: 'Poeta e pensador açoriano, da Geração de 70; sonetista.'
});

BIBLIOTECA.autor({
  id: 'antonio-nobre',
  nome: 'António Nobre',
  nomeCompleto: 'António Pereira Nobre',
  vida: '1867–1900',
  ordem: 'Nobre, António',
  nota: 'Poeta portuense, autor de um só livro publicado em vida, _Só_.'
});

BIBLIOTECA.autor({
  id: 'augusto-dos-anjos',
  nome: 'Augusto dos Anjos',
  nomeCompleto: 'Augusto de Carvalho Rodrigues dos Anjos',
  vida: '1884–1914',
  ordem: 'Anjos, Augusto dos',
  nota: 'Poeta paraibano, autor de um livro único, _Eu_.'
});

BIBLIOTECA.autor({
  id: 'bocage',
  nome: 'Bocage',
  nomeCompleto: 'Manuel Maria Barbosa du Bocage',
  vida: '1765–1805',
  ordem: 'Bocage',
  nota: 'Poeta de Setúbal, o grande sonetista do arcadismo português.'
});

BIBLIOTECA.autor({
  id: 'camilo-pessanha',
  nome: 'Camilo Pessanha',
  nomeCompleto: 'Camilo de Almeida Pessanha',
  vida: '1867–1926',
  ordem: 'Pessanha, Camilo',
  nota: 'Poeta simbolista português, que viveu em Macau; autor da _Clepsidra_.'
});

BIBLIOTECA.autor({
  id: 'casimiro-de-abreu',
  nome: 'Casimiro de Abreu',
  nomeCompleto: 'Casimiro José Marques de Abreu',
  vida: '1839–1860',
  ordem: 'Abreu, Casimiro de',
  nota: 'Poeta romântico fluminense, autor de _As Primaveras_.'
});

BIBLIOTECA.autor({
  id: 'castro-alves',
  nome: 'Castro Alves',
  nomeCompleto: 'Antônio Frederico de Castro Alves',
  vida: '1847–1871',
  ordem: 'Alves, Castro',
  nota: 'Poeta romântico baiano, o poeta dos escravos.'
});

BIBLIOTECA.autor({
  id: 'cesario-verde',
  nome: 'Cesário Verde',
  nomeCompleto: 'José Joaquim Cesário Verde',
  vida: '1855–1886',
  ordem: 'Verde, Cesário',
  nota: 'Poeta lisboeta, pintor da cidade e do campo.'
});

BIBLIOTECA.autor({
  id: 'claudio-manuel-da-costa',
  nome: 'Cláudio Manuel da Costa',
  nomeCompleto: 'Cláudio Manuel da Costa',
  vida: '1729–1789',
  ordem: 'Costa, Cláudio Manuel da',
  nota: 'Poeta árcade mineiro, da Inconfidência.'
});

BIBLIOTECA.autor({
  id: 'cruz-e-sousa',
  nome: 'Cruz e Sousa',
  nomeCompleto: 'João da Cruz e Sousa',
  vida: '1861–1898',
  ordem: 'Sousa, Cruz e',
  nota: 'Poeta catarinense, o maior nome do simbolismo brasileiro.'
});

BIBLIOTECA.autor({
  id: 'fagundes-varela',
  nome: 'Fagundes Varela',
  nomeCompleto: 'Luís Nicolau Fagundes Varela',
  vida: '1841–1875',
  ordem: 'Varela, Fagundes',
  nota: 'Poeta romântico fluminense.'
});

BIBLIOTECA.autor({
  id: 'fernando-pessoa',
  nome: 'Fernando Pessoa',
  nomeCompleto: 'Fernando António Nogueira Pessoa',
  vida: '1888–1935',
  ordem: 'Pessoa, Fernando',
  nota: 'Poeta lisboeta; escreveu em seu nome e no de heterônimos, como Alberto Caeiro, Ricardo Reis e Álvaro de Campos.'
});

BIBLIOTECA.autor({
  id: 'florbela-espanca',
  nome: 'Florbela Espanca',
  nomeCompleto: 'Flor Bela de Alma da Conceição Espanca',
  vida: '1894–1930',
  ordem: 'Espanca, Florbela',
  nota: 'Poeta alentejana, sonetista.'
});

BIBLIOTECA.autor({
  id: 'francisca-julia',
  nome: 'Francisca Júlia',
  nomeCompleto: 'Francisca Júlia da Silva',
  vida: '1871–1920',
  ordem: 'Júlia, Francisca',
  nota: 'Poeta parnasiana paulista, autora de _Mármores_.'
});

BIBLIOTECA.autor({
  id: 'goncalves-dias',
  nome: 'Gonçalves Dias',
  nomeCompleto: 'Antônio Gonçalves Dias',
  vida: '1823–1864',
  ordem: 'Dias, Gonçalves',
  nota: 'Poeta romântico maranhense, da poesia indianista e da «Canção do exílio».'
});

BIBLIOTECA.autor({
  id: 'gregorio-de-matos',
  nome: 'Gregório de Matos',
  nomeCompleto: 'Gregório de Matos e Guerra',
  vida: '1636–1696',
  ordem: 'Matos, Gregório de',
  nota: 'Poeta barroco baiano, o Boca do Inferno; a obra chegou até nós em manuscritos.'
});

BIBLIOTECA.autor({
  id: 'junqueira-freire',
  nome: 'Junqueira Freire',
  nomeCompleto: 'Luís José Junqueira Freire',
  vida: '1832–1855',
  ordem: 'Freire, Junqueira',
  nota: 'Poeta romântico baiano, monge beneditino.'
});

BIBLIOTECA.autor({
  id: 'luis-de-camoes',
  nome: 'Luís de Camões',
  nomeCompleto: 'Luís Vaz de Camões',
  vida: '~1524–1580',
  ordem: 'Camões, Luís de',
  nota: 'Poeta de _Os Lusíadas_ e o maior lírico da língua.'
});

BIBLIOTECA.autor({
  id: 'mario-de-andrade',
  nome: 'Mário de Andrade',
  nomeCompleto: 'Mário Raul de Morais Andrade',
  vida: '1893–1945',
  ordem: 'Andrade, Mário de',
  nota: 'Poeta, romancista e musicólogo paulistano, figura central do modernismo.'
});

BIBLIOTECA.autor({
  id: 'olavo-bilac',
  nome: 'Olavo Bilac',
  nomeCompleto: 'Olavo Brás Martins dos Guimarães Bilac',
  vida: '1865–1918',
  ordem: 'Bilac, Olavo',
  nota: 'Poeta parnasiano carioca, o Príncipe dos Poetas Brasileiros.'
});

BIBLIOTECA.autor({
  id: 'raimundo-correia',
  nome: 'Raimundo Correia',
  nomeCompleto: 'Raimundo da Mota de Azevedo Correia',
  vida: '1859–1911',
  ordem: 'Correia, Raimundo',
  nota: 'Poeta parnasiano maranhense.'
});

BIBLIOTECA.autor({
  id: 'raul-de-leoni',
  nome: 'Raul de Leoni',
  nomeCompleto: 'Raul de Leoni Ramos',
  vida: '1895–1926',
  ordem: 'Leoni, Raul de',
  nota: 'Poeta fluminense, autor de _Luz Mediterrânea_.'
});

BIBLIOTECA.autor({
  id: 'tomas-antonio-gonzaga',
  nome: 'Tomás Antônio Gonzaga',
  nomeCompleto: 'Tomás Antônio Gonzaga',
  vida: '1744–1810',
  ordem: 'Gonzaga, Tomás Antônio',
  nota: 'Poeta árcade, o Dirceu de _Marília de Dirceu_; inconfidente.'
});

BIBLIOTECA.autor({
  id: 'vicente-de-carvalho',
  nome: 'Vicente de Carvalho',
  nomeCompleto: 'Vicente Augusto de Carvalho',
  vida: '1866–1924',
  ordem: 'Carvalho, Vicente de',
  nota: 'Poeta parnasiano santista, o poeta do mar.'
});

/* Literatura em tradução: nenhuma. O Beowulf (tradução por IA) saiu em 23/10/2026: o Gere não põe
   tradução de IA na Literatura e combina a do Beowulf com um tradutor. Os poemas traduzidos pelo
   Versificador saíram em 20/10/2026 (PUBLICAR_TRADUCOES em ferramentas/poesia.py). */

/* Na língua original, sem tradução nossa ("lingua": a língua em que o autor aparece na Literatura;
   cada palavra dos poemas abre uma nota, ver edicoes/lingua-original/README.md). Poe, Baudelaire
   e Verlaine voltaram assim em 20/10/2026; uma tradução em domínio público, quando há, fica ao lado. */
BIBLIOTECA.autor({
  id: 'garcilaso-de-la-vega',
  nome: 'Garcilaso de la Vega',
  nomeCompleto: 'Garcilaso de la Vega',
  vida: '~1500–1536',
  lingua: 'es',
  nota: 'Poeta do Renascimento espanhol, que aclimatou no castelhano o soneto e o verso italiano.'
});

BIBLIOTECA.autor({
  id: 'francisco-de-quevedo',
  nome: 'Francisco de Quevedo',
  nomeCompleto: 'Francisco Gómez de Quevedo y Santibáñez Villegas',
  vida: '1580–1645',
  lingua: 'es',
  nota: 'Poeta e prosador do Século de Ouro espanhol.'
});

BIBLIOTECA.autor({
  id: 'sao-joao-da-cruz',
  nome: 'São João da Cruz',
  nomeCompleto: 'Juan de Yepes Álvarez (San Juan de la Cruz)',
  vida: '1542–1591',
  lingua: 'es',
  nota: 'Carmelita, doutor da Igreja e poeta místico do Século de Ouro espanhol.'
});

BIBLIOTECA.autor({
  id: 'william-shakespeare',
  nome: 'William Shakespeare',
  nomeCompleto: 'William Shakespeare',
  vida: '1564–1616',
  lingua: 'en',
  nota: 'Dramaturgo e poeta inglês.'
});

BIBLIOTECA.autor({
  id: 'john-donne',
  nome: 'John Donne',
  nomeCompleto: 'John Donne',
  vida: '1572–1631',
  lingua: 'en',
  nota: 'Poeta e pregador inglês, o maior dos poetas metafísicos.'
});

BIBLIOTECA.autor({
  id: 'john-keats',
  nome: 'John Keats',
  nomeCompleto: 'John Keats',
  vida: '1795–1821',
  lingua: 'en',
  nota: 'Poeta romântico inglês.'
});

BIBLIOTECA.autor({
  id: 'edgar-allan-poe',
  nome: 'Edgar Allan Poe',
  nomeCompleto: 'Edgar Allan Poe',
  vida: '1809–1849',
  lingua: 'en',
  nota: 'Poeta e contista norte-americano.'
});

BIBLIOTECA.autor({
  id: 'pierre-de-ronsard',
  nome: 'Pierre de Ronsard',
  nomeCompleto: 'Pierre de Ronsard',
  vida: '1524–1585',
  lingua: 'fr',
  nota: 'Poeta do Renascimento francês, o principal da Plêiade.'
});

BIBLIOTECA.autor({
  id: 'victor-hugo',
  nome: 'Victor Hugo',
  nomeCompleto: 'Victor-Marie Hugo',
  vida: '1802–1885',
  lingua: 'fr',
  nota: 'Poeta, romancista e dramaturgo francês.'
});

BIBLIOTECA.autor({
  id: 'arthur-rimbaud',
  nome: 'Arthur Rimbaud',
  nomeCompleto: 'Jean Nicolas Arthur Rimbaud',
  vida: '1854–1891',
  lingua: 'fr',
  nota: 'Poeta francês; escreveu toda a sua obra antes dos 21 anos.'
});

BIBLIOTECA.autor({
  id: 'charles-baudelaire',
  nome: 'Charles Baudelaire',
  nomeCompleto: 'Charles-Pierre Baudelaire',
  vida: '1821–1867',
  lingua: 'fr',
  nota: 'Poeta francês, autor de _As Flores do Mal_.'
});

BIBLIOTECA.autor({
  id: 'paul-verlaine',
  nome: 'Paul Verlaine',
  nomeCompleto: 'Paul-Marie Verlaine',
  vida: '1844–1896',
  lingua: 'fr',
  nota: 'Poeta simbolista francês.'
});

BIBLIOTECA.autor({
  id: 'gustavo-adolfo-becquer',
  nome: 'Gustavo Adolfo Bécquer',
  nomeCompleto: 'Gustavo Adolfo Claudio Domínguez Bastida',
  vida: '1836–1870',
  lingua: 'es',
  nota: 'Poeta e prosador do romantismo espanhol, autor das _Rimas_ e das _Leyendas_.'
});

BIBLIOTECA.autor({
  id: 'antonio-machado',
  nome: 'Antonio Machado',
  nomeCompleto: 'Antonio Cipriano José María y Francisco de Santa Ana Machado Ruiz',
  vida: '1875–1939',
  lingua: 'es',
  nota: 'Poeta espanhol da Geração de 98, autor de _Soledades_ e _Campos de Castilla_.'
});

BIBLIOTECA.autor({
  id: 'emily-dickinson',
  nome: 'Emily Dickinson',
  nomeCompleto: 'Emily Elizabeth Dickinson',
  vida: '1830–1886',
  lingua: 'en',
  nota: 'Poeta norte-americana; quase toda a obra saiu depois da morte dela.'
});

BIBLIOTECA.autor({
  id: 'robert-louis-stevenson',
  nome: 'Robert Louis Stevenson',
  nomeCompleto: 'Robert Louis Balfour Stevenson',
  vida: '1850–1894',
  lingua: 'en',
  nota: 'Escritor escocês, autor de _A Ilha do Tesouro_ e de poemas.'
});

BIBLIOTECA.autor({
  id: 'marcial',
  nome: 'Marcial',
  nomeCompleto: 'Marco Valério Marcial',
  vida: '~40–~104',
  lingua: 'la',
  nota: 'Poeta latino nascido na Hispânia, que viveu em Roma; mestre do epigrama.'
});

BIBLIOTECA.autor({
  id: 'catulo',
  nome: 'Catulo',
  nomeCompleto: 'Caio Valério Catulo',
  vida: '~84–~54 a.C.',
  lingua: 'la',
  nota: 'Poeta latino de Verona; os seus poemas a Lésbia estão entre os mais pessoais da poesia antiga.'
});

BIBLIOTECA.autor({
  id: 'fedro',
  nome: 'Fedro',
  nomeCompleto: 'Fedro',
  vida: '~15 a.C.–~50',
  lingua: 'la',
  nota: 'Escravo liberto de Augusto, pôs em verso latino as fábulas de Esopo.'
});

/* Não-ficção (área ainda sem link na capa, até o Gere aprovar a primeira obra) */
BIBLIOTECA.autor({
  id: 'platao',
  nome: 'Platão',
  nomeCompleto: 'Platão de Atenas',
  vida: '~428–348 a.C.',
  ordem: 'Platão',
  area: 'nao-ficcao',
  nota: 'Filósofo ateniense, discípulo de Sócrates e mestre de Aristóteles.'
});

BIBLIOTECA.autor({
  id: 'vergilio',
  nome: 'Vergílio',
  nomeCompleto: 'Públio Vergílio Marão',
  vida: '70–19 a.C.',
  lingua: 'la',
  nota: 'Poeta latino de Mântua, autor das Bucólicas, das Geórgicas e da Eneida.'
});
