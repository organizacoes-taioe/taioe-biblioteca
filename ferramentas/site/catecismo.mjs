// O Catecismo da Igreja Católica na Biblioteca Taioé (área Catolicismo).
//
// Os dados vêm de edicoes/catecismo/dados/, cópia fiel da pasta dados/ do site próprio do
// Catecismo (ver edicoes/catecismo/sincronizar.py): o manifesto (blocos, aberturas, subtítulos)
// e os pontos (trilha, corpo em HTML com as chamadas de nota, notas). O leitor é o mesmo do
// site antigo, em páginas estáticas:
//
//   .../catecismo-da-igreja-catolica/          rosto: o Prólogo e as quatro partes, «Ir ao ponto»
//   .../catecismo-da-igreja-catolica/parte-1/  as seções da parte (e .../prologo/, os tópicos do Prólogo)
//   .../parte-1/secao-2/                       os capítulos da seção
//   .../parte-1/secao-2/capitulo-1/            o que se lê: artigos, parágrafos e tópicos, até os pontos
//   .../catecismo-da-igreja-catolica/27/       o ponto 27: trilha, numeral, subtítulo, corpo, referências
//   .../catecismo-da-igreja-catolica/sobre/    a origem do texto
//
// A navegação vai de ponto em ponto: … 26 → 27 → 28 … O primeiro ponto de cada tópico traz no alto,
// em destaque, os níveis que começam ali (a «abertura»: parte, seção, capítulo, artigo, parágrafo,
// tópico). As antigas páginas de abertura (.../a27/) ficam só como redirecionamento para o ponto.
// Os endereços são o próprio número do ponto e não mudam: não entram em enderecos.json.
// Para a busca, as partes da obra são os pontos. O estado de
// leitura guarda só a posição («Continuar: Ponto N») e a escolha manual da obra (lendo, lida), sem
// marca por ponto: milhares de marcas estourariam o limite de leituras.partes no banco (64 KB).
// No obras.json, a obra vai com q = [primeiro, último, 'Ponto'] em vez da lista dos pontos.

import fs from 'node:fs';
import path from 'node:path';

export const ID = 'catecismo-da-igreja-catolica';
export const TOTAL = 2865;                         // pontos do Catecismo inteiro
const NIVEIS = ['parte', 'secao', 'capitulo', 'artigo', 'paragrafo', 'topico'];
const RODAPE = 'Catecismo da Igreja Católica © Libreria Editrice Vaticana.';
const VATICANO = 'https://www.vatican.va/archive/cathechism_po/index_new/prima-pagina-cic_po.html';
const VATICANO_INDICE = 'https://www.vatican.va/archive/cathechism_po/index_new/indice_po.html';
// as quatro partes, para o rosto mostrar também as que ainda não foram publicadas (sem link);
// as publicadas vêm do manifesto, com os títulos de lá
const PARTES = [
  { rotulo: 'Primeira parte', titulo: 'A profissão da fé', de: 26, ate: 1065 },
  { rotulo: 'Segunda parte', titulo: 'A celebração do mistério cristão', de: 1066, ate: 1690 },
  { rotulo: 'Terceira parte', titulo: 'A vida em Cristo', de: 1691, ate: 2557 },
  { rotulo: 'Quarta parte', titulo: 'A oração cristã', de: 2558, ate: 2865 }];

const semTags = (s) => String(s || '').replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ').replace(/&lt;/g, '<')
  .replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
const PALAVRA = /[\p{L}\p{N}]+(?:[-'’][\p{L}\p{N}]+)*/gu;

export function carregarCatecismo(raiz) {
  const dir = path.join(raiz, 'edicoes', 'catecismo', 'dados');
  const ler = (arq) => JSON.parse(fs.readFileSync(path.join(dir, arq), 'utf8'));
  if (!fs.existsSync(path.join(dir, 'manifesto.json'))) return null;
  const man = ler('manifesto.json');
  // o endereço de cada ponto no vatican.va, com fragmento de texto (edicoes/catecismo/vaticano.py)
  const arqVat = path.join(raiz, 'edicoes', 'catecismo', 'vaticano.json');
  const vaticano = fs.existsSync(arqVat) ? JSON.parse(fs.readFileSync(arqVat, 'utf8')) : {};
  man.aberturas = man.aberturas || {};
  man.subtitulos = man.subtitulos || {};
  const pontos = {};
  man.blocos.forEach((b) => {
    const d = ler(b.file);
    for (let n = b.de; n <= b.ate; n++) {
      if (!d[n]) throw new Error(`catecismo: ponto ${n} anunciado em ${b.file}, mas ausente`);
      pontos[n] = d[n];
    }
  });
  const partes = [];
  let palavras = 0;
  for (let n = man.min; n <= man.max; n++) {
    const p = pontos[n];
    if (!p) throw new Error(`catecismo: falta o ponto ${n}`);
    const sub = man.subtitulos[n] || '';
    palavras += (semTags(sub + ' ' + p.body).match(PALAVRA) || []).length;
    // o texto da busca: subtítulo, corpo e notas (fonte e citação)
    const busca = [sub, p.body].concat(p.notes.map((x) => x.fonte + ' ' + (x.txt || ''))).map(semTags).join('\n\n');
    partes.push({ n: String(n), titulo: '', slug: String(n), texto: busca, ponto: p, num: n });
  }
  return {
    id: ID, autor: 'igreja-catolica', titulo: 'Catecismo da Igreja Católica', tituloCurto: 'Catecismo',
    ano: 1992, genero: 'Catecismo', divisao: { singular: 'ponto', plural: 'pontos' },
    descricao: 'A exposição da fé e da moral da Igreja, promulgada por São João Paulo II em 1992: ' +
      'a profissão da fé, os sacramentos, a vida em Cristo e a oração cristã.',
    rodape: RODAPE, _palavras: palavras, partes, catecismo: man, vaticano,
    edicao: {
      apresentacao: `O _Catecismo da Igreja Católica_ foi promulgado por São João Paulo II em 11 de outubro de 1992, com a constituição apostólica _Fidei depositum_. A edição típica latina, com as correções definitivas, saiu em 1997.

O texto desta edição é a tradução portuguesa publicada pela Santa Sé no sítio vatican.va, com ajustes de português de Portugal para o Brasil.

Os direitos do texto são da Libreria Editrice Vaticana (© Libreria Editrice Vaticana). Ao contrário das outras obras desta biblioteca, o _Catecismo_ não está em domínio público.

Cada um dos ${TOTAL} pontos (os parágrafos numerados do _Catecismo_) tem página própria, com as referências embaixo. Quando a nota traz um texto que não aparece no corpo do ponto, esse texto vem junto da fonte; quando a citação já foi transcrita no corpo, a nota mostra só a fonte e uma etiqueta que o diz. Tocar no número de uma nota abre a referência ali mesmo. O primeiro ponto de cada tópico anuncia no alto da página o que começa ali: parte, seção, capítulo, artigo, parágrafo ou tópico.

Por enquanto estão publicados os pontos ${man.min} a ${man.max}; os outros entram aos poucos.`,
      fontes: [{ nome: 'Catecismo da Igreja Católica, em vatican.va', url: VATICANO, nota: 'tradução portuguesa publicada pela Santa Sé' },
        { nome: 'Índice do Catecismo em vatican.va', url: VATICANO_INDICE, nota: 'em cada ponto desta edição há um link para o mesmo ponto lá' }]
    }
  };
}

/* As páginas da obra. h: as funções do gerar.mjs (pagina, esc, U, trilhaObra, jsonObra…). */
export function paginasCatecismo(a, o, h) {
  const { esc, U, SITE } = h;
  const man = o.catecismo, ab = man.aberturas, min = man.min, max = man.max;
  const chave = h.chaveObra(o), raiz = U.obra(o);
  const P = (n) => raiz + n + '/', A = (n) => raiz + 'a' + n + '/';
  const temAb = (n) => !!ab[n];
  const textoNivel = (x) => (x.rotulo ? x.rotulo + ': ' : '') + x.titulo;
    const autor = { '@type': 'Organization', name: a.nomeCompleto || a.nome };

  const passo = (cls, rel, dir, alvo) => (alvo
    ? '<a class="passo ' + cls + '" href="' + alvo.url + '" rel="' + rel + '"><span class="dir">' + dir + '</span><span class="alvo">' + esc(alvo.txt) + '</span></a>'
    : '<span class="passo vazio"></span>');
  const indice = () => '<a class="passo seg" href="' + raiz + '"><span class="dir">Índice</span><span class="alvo">' + esc(o.tituloCurto) + '</span></a>';
  // o campo é de texto com teclado numérico: sem as setinhas de subir e descer do type="number"
  const irAoPonto = () => '<form class="ir-ponto" id="ir-ponto" data-url="' + raiz + '" data-min="' + min + '" data-max="' + max + '"' +
    ' data-total="' + TOTAL + '" novalidate hidden>' +
    '<label for="ir-ponto-n">Ir ao ponto</label><input id="ir-ponto-n" type="text" inputmode="numeric" pattern="[0-9]*" maxlength="4"' +
    ' autocomplete="off" placeholder="' + min + '">' +
    '<button type="submit">Ir</button><span class="ir-aviso" id="ir-aviso" role="status"></span></form>';

  // ---------------------------------------------------------------- a árvore dos níveis
  // Cada nível que começa numa abertura (parte, seção, capítulo, artigo, parágrafo, tópico) vira
  // uma entrada, com a faixa de pontos e os filhos. Parte, seção e capítulo têm página própria
  // (.../parte-1/, .../parte-1/secao-2/, .../parte-1/secao-2/capitulo-1/; o Prólogo em .../prologo/):
  // escolhe-se a parte, depois a seção, depois o capítulo, e na página do capítulo está a lista do
  // que se lê. Nível que faltar na estrutura não ganha página; nível com um item só também não:
  // o link leva direto ao de baixo.
  const entradas = [];
  Object.keys(ab).map(Number).sort((x, y) => x - y).forEach((n) => {
    ab[n].novos.forEach((x) => entradas.push({ k: NIVEIS.indexOf(x.nivel), x, de: n, filhos: [], pai: null }));
  });
  entradas.forEach((e, i) => {
    const prox = entradas.slice(i + 1).find((f) => f.k <= e.k && f.de > e.de);
    e.ate = prox ? prox.de - 1 : max < TOTAL ? null : max;     // null: continua nos pontos ainda não publicados
  });
  const topo = [], pilha = [];
  entradas.forEach((e) => {
    while (pilha.length && pilha[pilha.length - 1].k >= e.k) pilha.pop();
    e.pai = pilha.length ? pilha[pilha.length - 1] : null;
    (e.pai ? e.pai.filhos : topo).push(e);
    pilha.push(e);
  });
  const ESTRUTURA = ['parte', 'secao', 'capitulo'];
  const estrutural = (e) => ESTRUTURA.includes(e.x.nivel);
  const prologo = (e) => e.x.nivel === 'parte' && !e.x.rotulo && /^pr[óo]logo$/i.test(e.x.titulo);
  const cheio = (e) => (e.x.rotulo ? e.x.rotulo + ' — ' : '') + e.x.titulo;     // como na trilha dos pontos
  const contem = (e, n) => n >= e.de && n <= (e.ate === null ? max : e.ate);
  // o endereço e o nome curto (o da trilha do topo): parte-1, secao-2, capitulo-1, pela ordem entre os irmãos
  entradas.filter(estrutural).forEach((e) => {
    const irmaos = (e.pai ? e.pai.filhos : topo).filter((f) => f.x.nivel === e.x.nivel && !prologo(f));
    const i = irmaos.indexOf(e) + 1;
    e.seg = prologo(e) ? 'prologo' : { parte: 'parte-', secao: 'secao-', capitulo: 'capitulo-' }[e.x.nivel] + i;
    e.curto = prologo(e) ? 'Prólogo' : e.x.nivel === 'capitulo' ? 'Capítulo ' + i : e.x.rotulo || e.x.titulo;
    e.url = (e.pai ? e.pai.url : raiz) + e.seg + '/';
  });
  // o que a página do nível lista: os pontos antes do primeiro filho («Início do capítulo») e os filhos
  const INICIO = { parte: 'Início da parte', secao: 'Início da seção', capitulo: 'Início do capítulo' };
  const itens = (e) => (e.filhos.length && e.filhos[0].de > e.de
    ? [{ inicio: true, de: e.de, ate: e.filhos[0].de - 1, nivel: e.x.nivel }] : []).concat(e.filhos);
  entradas.filter(estrutural).reverse().forEach((e) => {          // de baixo para cima: o filho decide antes do pai
    const it = itens(e);
    e.temPagina = it.length > 1 || (it.length === 1 && !it[0].inicio && !estrutural(it[0]) && it[0].filhos.length > 0);
    e.destino = e.temPagina ? e.url : it.length === 1 && estrutural(it[0]) ? it[0].destino : P(e.de);
  });
  // a cadeia de níveis que contém o ponto n, do mais alto ao mais baixo
  const cadeia = (n) => {
    const c = [];
    for (let nivel = topo, e; (e = nivel.find((f) => contem(f, n))); nivel = e.filhos) c.push(e);
    return c;
  };
  const ancora = (e) => e.x.nivel + '-' + e.de;
  // o link de um nível: parte, seção e capítulo levam à sua página; artigo, parágrafo e tópico, ao primeiro ponto
  const linkNivel = (e) => (estrutural(e) ? e.destino : P(e.de));
  const trilhaNiveis = (es) => es.filter(estrutural).map((e) => ({ txt: e.curto, href: e.destino }));
  // a trilha do topo nos pontos: Catecismo › Primeira parte › Segunda seção › Capítulo 1 › Ponto 27
  const trilha = (ultimo, n) => h.trilhaObra(a, o).concat({ txt: o.tituloCurto, href: raiz }, trilhaNiveis(cadeia(n)), { txt: ultimo });
  // «índice», embaixo dos pontos: a página de nível onde está o ponto n, no item dele
  const indiceDe = (n) => {
    const c = cadeia(n), ult = c[c.length - 1];
    for (let k = c.length - 1; k >= 0; k--) {
      if (estrutural(c[k]) && c[k].temPagina) return c[k].url + (ult && !estrutural(ult) ? '#' + ancora(ult) : '');
    }
    return raiz;
  };
  // a linha de contexto dos pontos e da abertura no primeiro ponto do tópico, com links: cada texto que for um nível da cadeia
  const ligarContexto = (textos, n, cls) => {
    const c = cadeia(n);
    return textos.map((t, k) => {
      const e = c.find((f) => [cheio(f), f.x.titulo].some((s) => t === s || t.startsWith(s + ' · ')));     // «III. … · subtítulo»
      const classe = cls && cls(k) ? ' class="' + cls(k) + '"' : '';
      return '<span' + classe + '>' + (e ? '<a href="' + linkNivel(e) + '">' + esc(t) + '</a>' : esc(t)) + '</span>';
    }).join('');
  };

  const numFaixa = (de, ate) => (ate === null ? de + '–…' : ate > de ? de + '–' + ate : String(de));
  const faixa = (de, ate) => '<span class="pontos">' + numFaixa(de, ate) + '</span>';
  const textoFaixa = (e) => (e.ate === null ? `Pontos ${e.de} em diante (publicados até o ${max})`
    : e.ate > e.de ? `Pontos ${e.de} a ${e.ate}` : `Ponto ${e.de}`);
  const rotulo = (r, t) => (r ? '<span class="rot">' + esc(r) + '</span> ' : '') + '<span class="tit">' + esc(t) + '</span>';
  // a lista aberta do que se lê (artigos, parágrafos, tópicos), indentada por nível
  const listaLeitura = (es) => (es.length ? '<ol>' + es.map((e) => '<li class="nivel-' + e.x.nivel + '" id="' + ancora(e) + '">' +
    '<a href="' + P(e.de) + '">' + rotulo(e.x.rotulo, e.x.titulo) + faixa(e.de, e.ate) + '</a>' + listaLeitura(e.filhos) + '</li>').join('') + '</ol>' : '');
  const item = (e) => (e.inicio
    ? '<li class="nivel-inicio"><a href="' + P(e.de) + '">' + rotulo(null, INICIO[e.nivel]) + faixa(e.de, e.ate) + '</a></li>'
    : estrutural(e)
      ? '<li class="nivel-' + e.x.nivel + ' passa"><a href="' + e.destino + '">' + rotulo(prologo(e) ? null : e.x.rotulo, e.x.titulo) + faixa(e.de, e.ate) + '</a></li>'
      : '<li class="nivel-' + e.x.nivel + '" id="' + ancora(e) + '"><a href="' + P(e.de) + '">' + rotulo(e.x.rotulo, e.x.titulo) + faixa(e.de, e.ate) + '</a>' +
        listaLeitura(e.filhos) + '</li>');

  // ---------------------------------------------------------------- rosto
  {
    // as quatro partes do Catecismo; as que ainda não foram publicadas aparecem sem link
    const linhas = topo.filter(prologo).map(item);
    PARTES.forEach((p) => {
      const e = topo.find((f) => f.x.nivel === 'parte' && f.x.rotulo === p.rotulo);
      linhas.push(e ? item(e) : '<li class="nivel-parte inedita"><span class="item">' + rotulo(p.rotulo, p.titulo) +
        '<span class="pontos">' + numFaixa(p.de, p.ate) + ' · ainda não publicada</span></span></li>');
    });
    topo.filter((f) => !prologo(f) && !PARTES.some((p) => p.rotulo === f.x.rotulo)).forEach((e) => linhas.push(item(e)));
    const publicados = min === 1 && max === TOTAL ? '' : 'Publicados até agora: pontos ' + min + ' a ' + max + ', de ' + TOTAL + '.';
    const html = '<div class="folha catecismo"><header class="rosto"><p class="rosto-autor">' + esc(a.nome) + '</p><h1>' + esc(o.titulo) + '</h1>' +
      '<p class="meta">' + esc(h.fichaObra(o)) + '</p>' +
      (publicados ? '<p class="publicacao">' + esc(publicados) + '</p>' : '') +
      '<p class="descricao">' + esc(o.descricao) + '</p>' +
      '<p class="aviso-outro" id="aviso-outro" hidden></p>' +
      '<p class="acoes"><a class="botao" id="comecar" href="' + P(min) + '">Começar a ler</a> ' +
      '<a class="botao secundario" href="' + U.sobre(o) + '">' + esc(h.tituloSobre(o)) + '</a></p>' + irAoPonto() +
      '<div class="estado-leitura" id="estado-leitura" data-alvo="obra" hidden></div></header>' +
      '<p class="secao-titulo">Índice</p><nav class="indice-cat" aria-label="Partes do Catecismo"><ol>' + linhas.join('') + '</ol></nav></div>';
    h.pagina({ url: raiz, titulo: o.titulo, corpo: html, trilha: h.trilhaObra(a, o).concat({ txt: o.tituloCurto }), rodape: o.rodape,
      descricao: h.descricaoDe(o.descricao),
      dados: { pagina: 'obra', obra: chave, 'titulo-obra': o.titulo, total: o.partes.length, 'so-posicao': 1, primeira: String(min) },
      jsonld: { ...h.jsonObra(a, o), author: autor, copyrightHolder: { '@type': 'Organization', name: 'Libreria Editrice Vaticana' } } });
  }

  // ---------------------------------------------------------------- páginas dos níveis
  {
    const comPagina = entradas.filter((e) => estrutural(e) && e.temPagina);
    comPagina.forEach((e) => {
      // anterior e seguinte: o nível vizinho do mesmo tipo (capítulo com capítulo), ainda que noutra seção
      const mesmos = comPagina.filter((f) => f.x.nivel === e.x.nivel), i = mesmos.indexOf(e);     // o Prólogo vai com as partes
      const viz = (f) => f && { url: f.url, txt: textoNivel(f.x) };
      const it = itens(e), leitura = !it.some((x) => !x.inicio && estrutural(x));
      const rot = prologo(e) ? null : e.x.rotulo;
      const html = '<div class="folha catecismo nivel-cat"><header class="cabeca">' +
        (rot ? '<p class="rotulo-nivel">' + esc(rot) + '</p>' : '') + '<h1>' + esc(e.x.titulo) + '</h1>' +
        '<p class="meta">' + esc(textoFaixa(e)) + '</p></header>' +
        '<nav class="indice-cat' + (leitura ? ' leitura-cat' : '') + '" aria-label="' + esc(leitura ? 'O que se lê em: ' + e.curto : 'Divisões de: ' + e.curto) + '">' +
        '<ol>' + it.map(item).join('') + '</ol></nav>' +
        (mesmos.length > 1 ? '<nav class="passos" aria-label="' + esc('Navegação entre ' + { parte: 'as partes', secao: 'as seções', capitulo: 'os capítulos' }[e.x.nivel]) + '">' +
          passo('ant', 'prev', '← Anterior', viz(mesmos[i - 1])) + passo('seg', 'next', 'Seguinte →', viz(mesmos[i + 1])) + '</nav>' : '') +
        irAoPonto() + '</div>';
      const dentro = it.map((x) => (x.inicio ? INICIO[x.nivel] : cheio(x))).join(' · ');
      h.pagina({ url: e.url, titulo: textoNivel(e.x) + ' — ' + o.titulo, corpo: html, rodape: o.rodape,
        trilha: h.trilhaObra(a, o).concat({ txt: o.tituloCurto, href: raiz }, trilhaNiveis(cadeia(e.de).slice(0, cadeia(e.de).indexOf(e))), { txt: e.curto }),
        descricao: h.descricaoDe(`${o.titulo}, ${textoNivel(e.x)} (pontos ${numFaixa(e.de, e.ate)}). ${dentro}.`),
        dados: { pagina: 'nivel', obra: chave, 'url-obra': raiz } });
    });
  }

  // ---------------------------------------------------------------- os antigos endereços das aberturas
  // .../a27/ era a página de abertura do tópico que começa no ponto 27; agora o próprio ponto 27 traz
  // a abertura no alto. O endereço antigo continua valendo: leva ao ponto (fora do sitemap e da contagem).
  Object.keys(ab).map(Number).forEach((n) => h.redirecionar(A(n), P(n), 'Ponto ' + n + ' — ' + o.titulo));

  // ---------------------------------------------------------------- pontos
  // o que muda no primeiro ponto de um tópico: o contexto (os níveis de cima, com links) e, grandes,
  // os níveis novos, cada um com rótulo e título — o que a página de abertura mostrava
  const abertura = (n) => {
    const x = ab[n];
    const contexto = x.contexto.length ? '<div class="contexto">' + ligarContexto(x.contexto, n) + '</div>' : '';
    const niveis = x.novos.map((v) => '<div class="nivel ' + v.nivel + '">' + (v.rotulo ? '<p class="rotulo">' + esc(v.rotulo) + '</p>' : '') +
      '<h2 class="titulo">' + esc(v.titulo) + '</h2></div>').join('<div class="elo"></div>');
    return '<div class="abertura-ponto">' + contexto + '<div class="ornato"></div>' + niveis + '</div>';
  };
  o.partes.forEach((p) => {
    const n = p.num, d = p.ponto, sub = man.subtitulos[n];
    const trilhaPonto = d.trail.length ? '<p class="trilha-ponto">' +
      ligarContexto(d.trail, n, (k) => (k === d.trail.length - 1 ? 'aqui' : '')) + '</p>' : '';
    const notas = d.notes.length ? '<section class="notas-ponto" aria-labelledby="ref-' + n + '"><h2 id="ref-' + n + '">Referências</h2>' +
      d.notes.map((x) => '<div class="nota-ponto" id="nota-' + x.n + '"><span class="n">' + x.n + '</span><div class="nota-corpo">' +
        '<p class="src">' + x.fonte + '</p>' + (x.txt ? '<div class="quoted">' + x.txt + '</div>' : '') +
        (x.tag ? '<span class="etiqueta">' + esc(x.tag) + '</span>' : '') + '</div></div>').join('') + '</section>' : '';
    const prev = n > min ? { url: P(n - 1), txt: 'Ponto ' + (n - 1) } : null;
    const next = n < max ? { url: P(n + 1), txt: 'Ponto ' + (n + 1) } : null;
    const html = '<p class="aviso-outro" id="aviso-outro" hidden></p>' +
      '<article class="folha leitura catecismo ponto">' +
      '<header class="cabeca-ponto' + (temAb(n) ? ' com-abertura' : '') + '">' + (temAb(n) ? abertura(n) : trilhaPonto) +
      '<h1 class="numeral"><span class="visualmente-oculto">Ponto </span>' + n + '</h1>' +
      '<div class="regua"></div>' + (sub ? '<h2 class="subtitulo-ponto">' + esc(sub) + '</h2>' : '') + '</header>' +
      '<div class="texto corpo-ponto">' + d.body + '</div>' + notas +
      (o.vaticano[n] ? '<p class="no-vaticano"><a href="' + esc(o.vaticano[n]) + '" target="_blank" rel="noopener">Ler este ponto no site do Vaticano ↗</a></p>' : '') +
      '<div id="fim-parte" aria-hidden="true"></div>' +
      (n === TOTAL ? '<p class="fim">Fim</p>' : '') +
      '<nav class="passos" aria-label="Navegação entre os pontos">' + passo('ant', 'prev', '← Anterior', prev) +
      (next ? passo('seg', 'next', 'Seguinte →', next) : indice()) + '</nav>' +
      '<p class="posicao">Ponto ' + n + ' de ' + TOTAL + ' · <a href="' + indiceDe(n) + '">índice</a></p>' + irAoPonto() + '</article>';
    h.pagina({ url: P(n), titulo: 'Ponto ' + n + ' — ' + o.titulo, corpo: html, trilha: trilha('Ponto ' + n, n), rodape: o.rodape,
      prev: prev && prev.url, next: next ? next.url : null, progresso: n / TOTAL,
      descricao: h.descricaoDe(`Catecismo, ${n}. ` + (temAb(n) ? ab[n].novos.map(textoNivel).join(' · ') + '. ' : '') + semTags(d.body)),
      dados: { pagina: 'parte', obra: chave, parte: p.slug, indice: n, total: TOTAL, ponto: n, 'so-posicao': 1,
        rotulo: 'Ponto ' + n, 'titulo-obra': o.titulo, 'url-obra': raiz },
      jsonld: { '@context': 'https://schema.org', '@type': 'Chapter', name: 'Ponto ' + n, position: n,
        isPartOf: { '@type': 'Book', name: o.titulo, url: SITE + raiz }, author: autor, inLanguage: 'pt-BR' } });
  });
}
