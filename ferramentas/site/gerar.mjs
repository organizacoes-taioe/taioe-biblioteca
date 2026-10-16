// Gera a Biblioteca Taioé estática em public/biblioteca/ (PLANO, etapa 4):
// uma página HTML pronta para cada área, autor, gênero, pasta de poemas, obra, parte e
// «Sobre esta edição», com endereço fixo, título e descrição próprios, sitemap e dados
// estruturados. Funciona sem JavaScript; o js/leitor.js só acrescenta as preferências,
// original e tradução, as setas do teclado e a posição de leitura.
//
//   node ferramentas/site/gerar.mjs
//
// Lê o mesmo conteudo/ do site antigo, na ordem do index.html antigo. A marcação do texto
// sai das mesmas funções do js/app.js antigo, só com os endereços trocados. Os endereços das
// partes ficam congelados em ferramentas/site/enderecos.json: uma parte nunca muda de endereço.
// Também grava ferramentas/sql/obras.sql (o catálogo, aplicado pelo workflow do taioe-infra).
// Sem dependências: Node 20+.

import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const SAIDA = path.join(RAIZ, 'public', 'biblioteca');
const BASE = '/biblioteca/';
const SITE = 'https://taioe.com.br';
const ARQ_ENDERECOS = path.join(RAIZ, 'ferramentas', 'site', 'enderecos.json');
const ARQ_SQL = path.join(RAIZ, 'ferramentas', 'sql', 'obras.sql');

// ------------------------------------------------------------------ carregar o conteúdo
const dados = { autores: [], obras: [], porId: {} };
function registrar(o) {
  if (dados.porId[o.id]) throw new Error('obra repetida: ' + o.id);
  dados.obras.push(o);
  dados.porId[o.id] = o;
}
const BIBLIOTECA = {
  autor(a) { dados.autores.push(a); },
  obra: registrar,
  poemas(pac) {
    pac.poemas.forEach((p, k) => {
      const l = p.livro >= 0 ? pac.livros[p.livro] : null;
      registrar({
        id: p.id, autor: pac.autor, titulo: p.titulo, genero: 'Poesia', poema: true,
        forma: p.forma, n: p.n || '', secao: p.secao || '', subtitulo: p.subtitulo || '',
        ano: p.ano || (l && l.ano) || null, versos: p.versos, lingua: p.lingua || '',
        traducao: p.traducao || null,
        coletanea: l ? { id: pac.autor + '/' + l.id, titulo: l.titulo, ano: l.ano || '', ordem: k, seq: p.livro } : null,
        ordem: k,
        divisao: { singular: 'parte', plural: 'partes' },
        partes: (p.partes || [{}]).map((x) => ({ n: '', titulo: x.titulo || '' })),
        arquivo: pac.arquivo
      });
    });
  },
  textos(mapa) {
    Object.keys(mapa).forEach((id) => {
      const o = dados.porId[id], e = mapa[id];
      if (!o) return;
      e.t.forEach((t, i) => {
        if (!o.partes[i]) o.partes[i] = { n: '', titulo: '' };
        o.partes[i].texto = t;
        if (e.o) o.partes[i].original = e.o[i];
      });
      if (e.e) o.edicao = e.e;
      o.carregada = true;
    });
  }
};
const ctx = vm.createContext({ BIBLIOTECA });
// Sempre com LF: no Windows o Git entrega CRLF, e o resultado tem de ser igual ao do GitHub.
const lerLf = (arq) => fs.readFileSync(arq, 'utf8').replace(/\r\n/g, '\n');
function rodar(rel) { vm.runInContext(lerLf(path.join(RAIZ, rel)), ctx, { filename: rel }); }

const indiceAntigo = lerLf(path.join(RAIZ, 'index.html'));
const scripts = [...indiceAntigo.matchAll(/<script[^>]*src="(conteudo\/[^"]+)"/g)].map((m) => m[1]);
scripts.forEach(rodar);
[...new Set(dados.obras.filter((o) => o.arquivo && !o.carregada).map((o) => o.arquivo))].forEach(rodar);
dados.obras.forEach((o) => {
  o.partes.forEach((p, i) => { if (p.texto === undefined) throw new Error(`sem texto: ${o.id} parte ${i + 1}`); });
});

// ------------------------------------------------------------------ marcação (do app.js antigo)
function esc(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function inline(s) {
  return esc(s)
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/_([^_]+)_/g, '<em>$1</em>')
    .replace(/\s*\{§ ([^}]+)\}\s*/g, (m, x) => ' <span class="folha-ms" title="capítulo e seção">' + x + '</span> ')
    .replace(/\s*\{Ms ([A-C]) (\d+)([rv]?)\}\s*/g, (m, ms, f, l) =>
      ' <span class="folha-ms" title="Manuscrito ' + ms + ', folha ' + f + (l === 'r' ? ' recto' : l === 'v' ? ' verso' : '') + '">' + ms + ' ' + f + l + '</span> ')
    .replace(/^ | $/g, '');
}
function textoPuro(s) { return String(s || '').replace(/\{[^}]*\}/g, '').replace(/[_*]/g, '').replace(/\s+/g, ' ').trim(); }

function blocos(texto) {
  const todos = String(texto).trim().split(/\n\s*\n/);
  const notas = todos.filter((b) => /^¤ /.test(b));
  let html = paragrafos(todos.filter((b) => !/^¤ /.test(b)));
  if (notas.length) {
    html += '\n<aside class="nota-do-autor"><p class="rotulo">' + (notas.length > 1 ? 'Notas do autor' : 'Nota do autor') + '</p>' +
      paragrafos(notas.map((b) => b.replace(/^¤ /, ''))) + '</aside>';
  }
  return html;
}
function paragrafos(lista) {
  return lista.map((b) => {
    if (/^## /.test(b)) return '<p class="cena">' + inline(b.slice(3).trim()) + '</p>';
    if (/^@ /.test(b)) return '<p class="fala">' + inline(b.slice(2).trim()) + '</p>';
    const linhas = b.split('\n');
    if (linhas.every((l) => /^\|\s?/.test(l))) {
      return '<p class="verso">' + linhas.map((l) => inline(l.replace(/^\|\s?/, ''))).join('<br>') + '</p>';
    }
    const p = b.replace(/\s*\n\s*/g, ' ').trim();
    const cls = /^[a-zà-ÿ]/.test(p) ? ' class="continua"' : '';
    return '<p' + cls + '>' + inline(p) + '</p>';
  }).join('\n');
}
function blocosPoema(texto) {
  const bl = []; let estrofe = null, branco = true;
  String(texto || '').split('\n').forEach((l) => {
    if (!l.trim()) { estrofe = null; branco = true; return; }
    const m = /^::(\w+)\s?(.*)$/.exec(l);
    if (m) { bl.push({ marca: m[1], valor: m[2].trim(), sep: branco }); estrofe = null; branco = false; return; }
    if (!estrofe) { estrofe = { versos: [], sep: branco }; bl.push(estrofe); }
    estrofe.versos.push(l);
    branco = false;
  });
  return bl;
}
const SEPARADORES = { 'filete': '<span class="fio"></span>', 'fio horizontal': '<span class="fio"></span>',
  'linha de pontos': '. . . . . . . . . . .' };
function htmlMarca(b) {
  const v = b.valor;
  switch (b.marca) {
    case 'epigrafe': return v.split(/\s+\/\s+/).map(inline).join('<br>');
    case 'separador': return SEPARADORES[v] || esc(v || '*');
    case 'lacuna': return '. . . . . . . . . . .';
    case 'pagina': return '';
    default: return inline(v);
  }
}
function linhasPoema(texto) {
  return blocosPoema(texto).map((b) => {
    if (b.marca) return { sep: b.sep, linhas: [{ cls: 'm m-' + b.marca, html: htmlMarca(b) }] };
    return { sep: b.sep, linhas: b.versos.map((v) => ({ cls: 'v', html: inline(v) })) };
  });
}
function linhasProsa(texto) {
  const todos = String(texto || '').trim().split(/\n\s*\n/).filter(Boolean);
  const corpo = todos.filter((b) => !/^¤ /.test(b));
  const notas = todos.filter((b) => /^¤ /.test(b));
  const linhas = corpo.map((b) => ({ sep: false, linhas: [{ cls: 'p', html: paragrafos([b]) }] }));
  if (notas.length) {
    linhas.push({ sep: false, linhas: [{ cls: 'p nota-do-autor', html: '<p class="rotulo">' + (notas.length > 1 ? 'Notas do autor' : 'Nota do autor') + '</p>' +
      paragrafos(notas.map((b) => b.replace(/^¤ /, ''))) }] });
  }
  return linhas;
}
function grade(ladoTrad, ladoOrig, lingua) {
  const n = Math.max(ladoTrad.length, ladoOrig ? ladoOrig.length : 0); let html = '', i = 0;
  for (let b = 0; b < n; b++) {
    const bt = ladoTrad[b] || { linhas: [] }, bo = ladoOrig ? ladoOrig[b] || { linhas: [] } : { linhas: [] };
    const m = Math.max(bt.linhas.length, bo.linhas.length);
    const sep = b > 0 && (bt.sep || bo.sep) ? ' ini' : '';
    for (let j = 0; j < m; j++, i++) {
      const ini = j === 0 ? sep : '';
      if (ladoOrig) html += celula('orig', bo.linhas[j], ini, i, lingua);
      html += celula('trad', bt.linhas[j], ini, i, '');
    }
  }
  return html;
}
function celula(lado, l, ini, i, lingua) {
  if (!l) return '<div class="' + lado + ' vazio' + ini + '" data-i="' + i + '"></div>';
  return '<div class="' + lado + ' ' + l.cls + ini + '" data-i="' + i + '"' + (lingua ? ' lang="' + lingua + '"' : '') + '>' + l.html + '</div>';
}
function textoParte(o, p) {
  const poema = !!o.poema;
  const linhas = poema ? linhasPoema : linhasProsa;
  const orig = p.original !== undefined && p.original !== null;
  const lingua = orig && o.traducao ? o.traducao.codigo || '' : '';
  const cls = 'paralelo ' + (poema ? 'poema' : 'prosa');
  const attr = o.lingua && !orig ? ' lang="' + esc(o.lingua) + '"' : '';
  if (!orig && !poema) return '<div class="texto">' + blocos(p.texto) + '</div>';
  return '<div class="texto"><div class="' + cls + '"' + attr + '>' +
    grade(linhas(p.texto), orig ? linhas(p.original) : null, lingua) + '</div></div>';
}
function incipit(texto, limite) {
  const t = String(texto).replace(/\{[^}]*\}/g, '').replace(/^\|\s?/gm, '').replace(/[_*]/g, '').replace(/\s+/g, ' ').trim();
  if (t.length <= limite) return esc(t);
  let corte = t.slice(0, limite);
  corte = corte.slice(0, corte.lastIndexOf(' '));
  return esc(corte) + '…';
}
const plural = (n, s, p) => n + ' ' + (n === 1 ? s : p);
const numeradas = (o) => o.partes.filter((p) => p.n).length || o.partes.length;
const rotuloPasso = (p) => [esc(p.n), p.titulo ? inline(p.titulo) : ''].filter(Boolean).join(' · ');

const GENEROS = ['Romance', 'Novela', 'Contos', 'Autobiografia', 'Hagiografia', 'Ensaio', 'Poesia', 'Teatro',
  'Cartas', 'Orações', 'Crônica', 'Crítica', 'Tradução'];
const PLURAIS = { 'Romance': 'Romances', 'Novela': 'Novelas', 'Contos': 'Contos', 'Poesia': 'Poesia',
  'Teatro': 'Teatro', 'Crônica': 'Crônicas', 'Crítica': 'Crítica', 'Tradução': 'Traduções',
  'Autobiografia': 'Autobiografia', 'Cartas': 'Cartas', 'Orações': 'Orações',
  'Hagiografia': 'Hagiografia', 'Ensaio': 'Ensaios' };
const AREAS = [{ id: 'literatura', nome: 'Literatura' }, { id: 'catolicismo', nome: 'Catolicismo' }];
const areaDe = (a) => a.area || 'literatura';
const acharArea = (id) => AREAS.find((x) => x.id === id) || null;
const nomeGenero = (g) => PLURAIS[g] || g;
const slug = (s) => String(s).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
const slugGenero = (g) => slug(nomeGenero(g));

const PALAVRA = /[\p{L}\p{N}]+(?:[-'’][\p{L}\p{N}]+)*/gu;
function palavras(o) {
  if (o._palavras === undefined) {
    o._palavras = o.partes.reduce((n, p) => n + (String(p.texto).replace(/[_*|]/g, ' ').match(PALAVRA) || []).length, 0);
  }
  return o._palavras;
}
const milhar = (n) => n.toLocaleString('pt-BR');
function fichaObra(o) {
  const d = o.divisao || { singular: 'parte', plural: 'partes' };
  if (o.poema) {
    return [o.partes.length > 1 ? plural(o.partes.length, d.singular, d.plural) : '',
      o.versos === 1 ? '1 verso' : milhar(o.versos) + ' versos'].filter(Boolean).join(' · ');
  }
  if (o.coletanea) {
    return [o.partes.length > 1 ? plural(numeradas(o), d.singular, d.plural) : '', milhar(palavras(o)) + ' palavras'].filter(Boolean).join(' · ');
  }
  return [o.datas || (o.ano ? String(o.ano) : ''), plural(numeradas(o), d.singular, d.plural), milhar(palavras(o)) + ' palavras'].filter(Boolean).join(' · ');
}
const textoPublicacao = (o) => (o.publicacao ? 'Primeira publicação: ' + o.publicacao : '');
const daColetanea = (o) => dados.obras.filter((x) => x.coletanea && x.coletanea.id === o.coletanea.id)
  .sort((a, b) => a.coletanea.ordem - b.coletanea.ordem);
function livros(obras) {
  const vistos = {};
  obras.forEach((o) => { vistos[o.coletanea ? 'c:' + o.coletanea.id : o.id] = 1; });
  return Object.keys(vistos).length;
}
const TEXTOS = { 'Contos': ['conto', 'contos'], 'Poesia': ['poema', 'poemas'] };
function porColetanea(obras) {
  const grupos = [], idx = {};
  obras.forEach((o) => {
    const k = o.coletanea ? o.coletanea.id : '';
    if (!(k in idx)) {
      idx[k] = grupos.length;
      grupos.push({ titulo: o.coletanea ? o.coletanea.titulo : '', ano: o.coletanea ? o.coletanea.ano : o.ano,
        seq: o.poema ? (o.coletanea ? o.coletanea.seq : 1e6) : null, obras: [] });
    }
    grupos[idx[k]].obras.push(o);
  });
  grupos.forEach((g) => g.obras.sort((a, b) => {
    if (a.poema && b.poema) return a.ordem - b.ordem;
    return a.coletanea && b.coletanea ? a.coletanea.ordem - b.coletanea.ordem : 0;
  }));
  return grupos.sort((a, b) => (a.seq !== null && b.seq !== null ? a.seq - b.seq : (a.ano || 0) - (b.ano || 0)));
}
const FORMAS = [{ id: 'sonetos', nome: 'Sonetos' }, { id: 'apologos', nome: 'Apólogos' }, { id: 'liras', nome: 'Liras' },
  { id: 'odes', nome: 'Odes' }, { id: 'verso-livre', nome: 'Verso livre' }, { id: 'outras', nome: 'Outras formas' }];
const acharForma = (id) => FORMAS.find((f) => f.id === id) || null;
const pastasDe = (obras) => FORMAS.map((f) => ({ forma: f, obras: obras.filter((o) => (o.forma || 'outras') === f.id) })).filter((x) => x.obras.length);
const poesiaDe = (autorId) => dados.obras.filter((o) => o.autor === autorId && o.genero === 'Poesia');
const acharAutor = (id) => dados.autores.find((a) => a.id === id) || null;
const obrasDe = (autorId) => dados.obras.filter((o) => o.autor === autorId)
  .sort((a, b) => (a.ano || 0) - (b.ano || 0) || a.titulo.localeCompare(b.titulo, 'pt'));
function generosDe(autorId) {
  const grupos = {};
  obrasDe(autorId).forEach((o) => { const g = o.genero || 'Outros'; (grupos[g] = grupos[g] || []).push(o); });
  return GENEROS.filter((g) => grupos[g])
    .concat(Object.keys(grupos).filter((g) => GENEROS.indexOf(g) < 0).sort())
    .map((g) => ({ genero: g, obras: grupos[g] }));
}
function soPoesia(autorId) { const g = generosDe(autorId); return g.length === 1 && g[0].genero === 'Poesia'; }
// Ordem alfabética pelo nome como está escrito («Machado de Assis» no M), pedido do Gere, 07/10/2026.
const autoresOrdenados = () => dados.autores.slice().sort((a, b) => a.nome.localeCompare(b.nome, 'pt'));
const autoresDaArea = (id) => autoresOrdenados().filter((a) => areaDe(a) === id);
function vizinhosPoema(o) {
  let lista = [];
  porColetanea(poesiaDe(o.autor).filter((x) => (x.forma || 'outras') === (o.forma || 'outras'))).forEach((g) => { lista = lista.concat(g.obras); });
  return lista;
}
function rotuloParte(obra, parte) {
  if (!parte.n && !parte.titulo) return obra.titulo;
  if (!parte.n) return textoPuro(parte.titulo);
  if (obra.divisao && obra.divisao.rotulo === 'n') return parte.n;
  if (obra.divisao && obra.divisao.rotulo === 'nome') return textoPuro(parte.titulo || parte.n);
  if (obra.divisao && obra.divisao.rotulo === 'titulo') return textoPuro(parte.titulo) + ', ' + parte.n;
  const d = obra.divisao ? obra.divisao.singular : 'parte';
  return d.charAt(0).toUpperCase() + d.slice(1) + ' ' + parte.n;
}
const tituloSobre = (o) => (o.edicao && o.edicao.titulo) || 'Sobre esta edição';
const umaParte = (o) => (o.coletanea || o.poema) && o.partes.length === 1;

// ------------------------------------------------------------------ endereços (congelados)
const RESERVADOS = new Set(['css', 'js', 'vendor', 'sitemap.xml', '404.html', 'obras.json', 'favicon.svg', 'lendo', 'lidos', 'busca', ...AREAS.map((a) => a.id)]);
const congelados = fs.existsSync(ARQ_ENDERECOS) ? JSON.parse(lerLf(ARQ_ENDERECOS)) : {};
const enderecos = {};
function slugParte(o, p, i) {
  const ag = o.divisao && (o.divisao.agrupar || o.divisao.rotulo === 'titulo');
  let s = slug(ag ? `${p.n} ${textoPuro(p.titulo)}` : p.n ? p.n : textoPuro(p.titulo));
  if (s.length > 50) s = s.slice(0, 50).replace(/-[^-]*$/, '');
  return s || 'parte-' + (i + 1);
}
dados.obras.forEach((o) => {
  if (umaParte(o)) return;
  const antes = congelados[o.id] || {}, agora = {}, usados = new Set(Object.values(antes));
  const vistos = {};
  o.partes.forEach((p, i) => {
    let marca = `${p.n}|${textoPuro(p.titulo)}`;
    vistos[marca] = (vistos[marca] || 0) + 1;
    if (vistos[marca] > 1) marca += '#' + vistos[marca];
    let s = antes[marca];
    if (!s) {
      const base = slugParte(o, p, i);
      s = base;
      for (let k = 2; usados.has(s) || s === 'sobre'; k++) s = base + '-' + k;
      usados.add(s);
    }
    if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(s) || s.length > 60) throw new Error(`endereço inválido: ${o.id}/${s}`);
    agora[marca] = s;
    p.slug = s;
  });
  enderecos[o.id] = agora;
});

// O endereço da obra é o id sem o nome do autor repetido no começo
// ("machado-de-assis-americanas-lua-nova" → "americanas-lua-nova"), único dentro do autor.
dados.obras.forEach((o) => {
  const pref = o.autor + '-';
  o.url = o.id.startsWith(pref) && o.id.length > pref.length ? o.id.slice(pref.length) : o.id;
});
dados.autores.forEach((a) => {
  const vistos = {};
  dados.obras.filter((o) => o.autor === a.id).forEach((o) => {
    if (vistos[o.url]) o.url = o.id;                    // colisão: fica o id inteiro
    vistos[o.url] = true;
  });
});

const U = {
  capa: () => BASE,
  area: (id) => BASE + id + '/',
  autor: (a) => BASE + a.id + '/',
  genero: (a, g) => BASE + a.id + '/' + slugGenero(g) + '/',
  pasta: (a, f) => BASE + a.id + '/poesia/' + f + '/',
  obra: (o) => BASE + o.autor + '/' + o.url + '/',
  parte: (o, i) => (umaParte(o) ? U.obra(o) : U.obra(o) + o.partes[i - 1].slug + '/'),
  sobre: (o) => U.obra(o) + 'sobre/'
};
/* Categoria (gênero na página do autor, forma na poesia) só existe com MIN_CATEGORIA livros ou
   mais (pedido do Gere, 06/10/2026): entrar numa pasta e achar uma obra só é redundante. Abaixo
   disso, as obras ficam soltas na página de cima. */
const MIN_CATEGORIA = 3;
function generoEhPasta(a, g) {
  const obras = obrasDe(a.id).filter((o) => (o.genero || 'Outros') === g);
  return (g === 'Poesia' ? obras.length : livros(obras)) >= MIN_CATEGORIA;
}
const formasPasta = (autorId) => {
  const ps = pastasDe(poesiaDe(autorId));
  return ps.length > 1 ? ps.filter((x) => x.obras.length >= MIN_CATEGORIA) : [];
};
const formaEhPasta = (autorId, f) => formasPasta(autorId).some((x) => x.forma.id === f);
U.poesia = (a) => (soPoesia(a.id) || !generoEhPasta(a, 'Poesia') ? U.autor(a) : U.genero(a, 'Poesia'));
U.indicePoema = (a, o) => (formaEhPasta(a.id, o.forma || 'outras') ? U.pasta(a, o.forma || 'outras') : U.poesia(a));
const chaveObra = (o) => o.autor + '/' + o.url;

// ------------------------------------------------------------------ capítulos (páginas por nível)
/* Pedido do Gere, 08/10/2026: «coloque mais páginas intermediárias para eu avançar por níveis…
   Prefiro várias páginas, do que essas listas recolhíveis». Numa parte com capítulos (as marcas
   «{§ I.1}» no começo do parágrafo, todas da mesma parte, cada uma logo depois de um título «## »),
   a página da parte vira o índice dos capítulos, e cada capítulo, uma página de leitura, embaixo
   dela (…/i/capitulo-3/). Capítulo muito longo com seções tituladas («## I. …», «## a) …») vira,
   por sua vez, índice das seções; parte de capítulo único mostra direto as seções (nunca índice de
   um item só). As Confissões (marca «capítulo.seção», sem títulos) e a Vida de Santo Antão (números
   sem título) não se dividem: lá o livro e a parte já são a unidade de leitura.
   A ordem de leitura são as folhas: as partes sem divisão, os capítulos e as seções. Cada item tem
   chave própria no estado de leitura: as slugs do caminho unidas por hífen («i-capitulo-3»,
   «v-capitulo-3-ii»), no formato que o banco aceita (ver leitor.js). */
const MARCA_CAP = /^\{§ ([IVXLC]+)\.(\d+)\}/;
const TIT_CAP = /^## (?:(?:Cap[ií]tulo|Chapitre|Chapter)\s+([IVXLC]+|\d+)\s*[—–-]\s*|(\d+)\.\s+)(.+)$/;
const TIT_SECAO = [/^## ([IVXLC]+)\.\s+(.+)$/, /^## ([a-z])\)\s+(.+)$/];
const SECOES_ACIMA_DE = 8000;   // palavras: capítulo maior que isto, com seções tituladas, vira índice delas
const ehNota = (b) => /^¤ /.test(b);
const ehTitulo = (b) => /^## /.test(b);
const contarPalavras = (bl) => bl.filter((b) => !ehNota(b))
  .reduce((n, b) => n + (b.replace(/\{[^}]*\}/g, ' ').replace(/[_*|]/g, ' ').match(PALAVRA) || []).length, 0);

function cabecalho(b) {
  const cab = b.replace(/^## /, '').trim();
  let m = TIT_CAP.exec(b);
  if (m) return { n: m[1] || m[2], titulo: m[3].trim(), cab };
  m = TIT_SECAO[0].exec(b);
  if (m) return { n: m[1], titulo: m[2].trim(), cab };
  m = TIT_SECAO[1].exec(b);
  if (m) return { n: m[1] + ')', titulo: m[2].trim(), cab };
  return { n: '', titulo: cab, cab };
}
function dividirParte(o, p) {
  const bl = String(p.texto).trim().split(/\n\s*\n/), marcas = [];
  bl.forEach((b, i) => { const m = MARCA_CAP.exec(b); if (m) marcas.push({ i, p: m[1], c: +m[2] }); });
  if (!marcas.length || new Set(marcas.map((m) => m.p)).size > 1) return;
  const inis = [];
  for (const m of marcas) {
    const corrida = [];
    for (let j = m.i - 1; j >= 0 && (ehTitulo(bl[j]) || ehNota(bl[j])); j--) if (ehTitulo(bl[j])) corrida.unshift(j);
    if (!corrida.length) return;                       // marca sem título de capítulo: não é esta a divisão
    const t = corrida.find((k) => TIT_CAP.test(bl[k]));
    inis.push(t === undefined ? corrida[corrida.length - 1] : t);
  }
  const orig = p.original === undefined || p.original === null ? null : String(p.original).trim().split(/\n\s*\n/);
  const onde = `${o.id}, ${rotuloParte(o, p)}`;
  if (orig) {
    if (orig.length !== bl.length) throw new Error(`${onde}: original com ${orig.length} blocos e tradução com ${bl.length}`);
    marcas.forEach((m) => { if (!orig[m.i].startsWith(`{§ ${m.p}.${m.c}}`)) throw new Error(`${onde}: a marca ${m.p}.${m.c} não está no mesmo lugar no original`); });
    inis.forEach((a) => { if (!ehTitulo(orig[a])) throw new Error(`${onde}: falta no original o título «${bl[a]}»`); });
  }
  const linha = (i) => bl.slice(0, i).filter((b) => !ehNota(b)).length;   // a linha do bloco na página antiga da parte
  const fatia = (a, b, tipo, s) => {                  // do título (a) até antes de b
    const c = cabecalho(bl[a]);
    const x = { slug: s, tipo, n: c.n, titulo: c.titulo, cab: c.cab, linha: linha(a), a, b, texto: bl.slice(a + 1, b).join('\n\n') };
    if (orig) { x.cabOriginal = orig[a].replace(/^## /, '').trim(); x.original = orig.slice(a + 1, b).join('\n\n'); }
    return x;
  };
  const secoes = (cap, tipoAbertura, slugAbertura) => {
    for (const re of TIT_SECAO) {
      const idx = [];
      for (let j = cap.a + 1; j < cap.b; j++) if (re.test(bl[j])) idx.push(j);
      if (idx.length < 2) continue;
      const filhos = [];
      if (bl.slice(cap.a + 1, idx[0]).some((b) => !ehTitulo(b) && !ehNota(b))) filhos.push(fatia(cap.a, idx[0], tipoAbertura, slugAbertura));
      idx.forEach((j, k) => filhos.push(fatia(j, k + 1 < idx.length ? idx[k + 1] : cap.b, 'secao', slug(cabecalho(bl[j]).n))));
      return filhos;
    }
    return null;
  };
  let caps = inis.map((a, k) => fatia(a, k + 1 < inis.length ? inis[k + 1] : bl.length, 'capitulo', 'capitulo-' + marcas[k].c));
  if (caps.length === 1) {
    caps = secoes(caps[0], 'capitulo', caps[0].slug);  // capítulo único: as seções direto na parte
    if (!caps) return;
  } else {
    caps.forEach((c) => {
      if (contarPalavras(bl.slice(c.a, c.b)) > SECOES_ACIMA_DE) { const s = secoes(c, 'abertura', 'abertura'); if (s) c.filhos = s; }
    });
  }
  p.filhos = caps;
  p.preambulo = bl.slice(0, inis[0]).filter((b) => !ehTitulo(b)).join('\n\n');
}
dados.obras.forEach((o) => { if (!o.poema && !o.coletanea && !umaParte(o)) o.partes.forEach((p) => dividirParte(o, p)); });
const dividida = (o) => o.partes.some((p) => p.filhos);

const curto = (x) => (x.tipo === 'capitulo' ? 'Capítulo ' + x.n : x.tipo === 'abertura' ? 'Abertura' : x.n);
const minuscula = (s) => s.charAt(0).toLowerCase() + s.slice(1);
/* um item da obra: a parte i e o caminho até ele dentro dela (cadeia de capítulos e seções) */
function infoNo(o, i, cadeia) {
  const p = o.partes[i - 1], x = cadeia.length ? cadeia[cadeia.length - 1] : p;
  return { parte: p, i, cadeia, no: x,
    chave: cadeia.length ? [p.slug].concat(cadeia.map((y) => y.slug)).join('-') : umaParte(o) ? 'texto' : p.slug,
    url: U.parte(o, i) + cadeia.map((y) => y.slug + '/').join(''),
    rotulo: [rotuloParte(o, p)].concat(cadeia.map((y) => minuscula(curto(y)))).join(', '),
    acima: cadeia.slice(0, -1).reduce((l, y) => l.concat(l[l.length - 1] + '-' + y.slug), cadeia.length ? [p.slug] : []) };
}
/* as folhas (páginas de leitura), na ordem do livro, e os nós (páginas de índice dentro da obra) */
function percorrer(o, aoNo) {
  o.partes.forEach((p, i) => {
    const andar = (cadeia) => {
      const x = cadeia.length ? cadeia[cadeia.length - 1] : p;
      aoNo(infoNo(o, i + 1, cadeia), !!x.filhos);
      if (x.filhos) x.filhos.forEach((y) => andar(cadeia.concat(y)));
    };
    andar([]);
  });
}
function folhasDe(o) {
  if (!o._folhas) {
    o._folhas = [];
    percorrer(o, (x, temFilhos) => { if (!temFilhos) o._folhas.push(x); });
    o._folhas.forEach((f, k) => { f.k = k; });
  }
  return o._folhas;
}
function nosDe(o) { const l = []; percorrer(o, (x, temFilhos) => { if (temFilhos) l.push(x); }); return l; }
/* a estrutura para o leitor.js (obras.json): [[slug, rótulo, filhos?], …] */
function estrutura(o) {
  const sub = (i, lista, cadeia) => lista.map((y) => {
    const c = cadeia.concat(y), r = infoNo(o, i, c).rotulo;
    return y.filhos ? [y.slug, r, sub(i, y.filhos, c)] : [y.slug, r];
  });
  return o.partes.map((p, k) => (p.filhos ? [p.slug, rotuloParte(o, p), sub(k + 1, p.filhos, [])] : [p.slug, rotuloParte(o, p)]));
}
/* a mesma, sem os rótulos, nas páginas da obra e dos índices (data-estrutura): as slugs separadas
   por espaço, e os filhos entre parênteses: «prefacio i(capitulo-1 capitulo-2) ii(…)» */
function estruturaCurta(o) {
  const sub = (lista) => lista.map((y) => y.slug + (y.filhos ? '(' + sub(y.filhos) + ')' : '')).join(' ');
  return sub(o.partes);
}
dados.obras.filter(dividida).forEach((o) => {
  const vistas = new Set();
  folhasDe(o).concat(nosDe(o)).forEach((x) => {
    if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(x.chave) || x.chave.length > 60) throw new Error(`chave de leitura inválida para o banco: ${o.id}/${x.chave}`);
    if (vistas.has(x.chave)) throw new Error(`chave de leitura repetida: ${o.id}/${x.chave}`);
    vistas.add(x.chave);
  });
});

// colisões: dentro de cada autor, obras × gêneros × "poesia"; autores × reservados
dados.autores.forEach((a) => {
  if (RESERVADOS.has(a.id)) throw new Error('autor com nome reservado: ' + a.id);
  const nomes = new Set(generosDe(a.id).map((x) => slugGenero(x.genero)));
  obrasDe(a.id).forEach((o) => { if (nomes.has(o.url)) throw new Error(`obra com o nome de um gênero: ${a.id}/${o.url}`); });
});

// ------------------------------------------------------------------ moldura das páginas
const hash = (s) => crypto.createHash('sha256').update(s).digest('hex').slice(0, 8);
const CSS = lerLf(path.join(RAIZ, 'ferramentas', 'site', 'estilo.css'));
const LEITOR = lerLf(path.join(RAIZ, 'ferramentas', 'site', 'leitor.js'));
const V_CSS = hash(CSS), V_JS = hash(LEITOR);

function trilhaHtml(itens) {
  return itens.map((it) => (it.href ? '<a href="' + it.href + '">' + esc(it.txt) + '</a>' : '<span aria-current="page">' + esc(it.txt) + '</span>'))
    .join('<span class="sep">›</span>');
}
function comArea(a, itens) {
  const ar = a && acharArea(areaDe(a));
  return ar ? [{ txt: ar.nome, href: U.area(ar.id) }].concat(itens) : itens;
}
function descricaoDe(t) { const s = textoPuro(t); return s.length > 155 ? s.slice(0, 154).replace(/\s+\S*$/, '') + '…' : s; }

const sitemap = [];
let paginas = 0;
function gravar(url, html) {
  const dir = path.join(SAIDA, url.slice(BASE.length));
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'index.html'), html);
  paginas++;
}
function pagina(o) {
  const titulo = o.titulo ? o.titulo + ' · Biblioteca Taioé' : 'Biblioteca Taioé';
  const ds = o.dados ? Object.entries(o.dados).map(([k, v]) => ` data-${k}="${esc(v)}"`).join('') : '';
  const html = `<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(titulo)}</title>
<meta name="description" content="${esc(o.descricao || 'Biblioteca Taioé: clássicos em português, abertos a todos.')}">
<link rel="canonical" href="${SITE}${o.url}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="${BASE}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="${BASE}css/estilo.css?v=${V_CSS}">
${o.prev ? `<link rel="prev" href="${o.prev}">\n` : ''}${o.next ? `<link rel="next" href="${o.next}">\n` : ''}<script defer src="${BASE}js/leitor.js?v=${V_JS}"></script>
${o.jsonld ? `<script type="application/ld+json">${JSON.stringify(o.jsonld).replace(/</g, '\\u003c')}</script>\n` : ''}</head>
<body${ds}>
<a class="pular" href="#app">Ir para o texto</a>

<header class="topo">
  <div class="topo-int">
    ${o.dados && o.dados.pagina === 'capa' ? '<a class="marca" href="/">Taioé</a>' : `<a class="marca" href="${BASE}">Biblioteca</a>`}
    <nav class="topo-nav" id="trilha" aria-label="Trilha de navegação">${trilhaHtml(o.trilha || [])}</nav>
    <div class="ferramentas">
      <a class="btn" href="${BASE}busca/" aria-label="Buscar" title="Buscar"><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="8.5" cy="8.5" r="5.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12.6 12.6 17 17" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></a>
      <button type="button" id="fonte-menos" class="btn" aria-label="Diminuir a letra" title="Diminuir a letra" hidden>A−</button>
      <button type="button" id="fonte-mais" class="btn" aria-label="Aumentar a letra" title="Aumentar a letra" hidden>A+</button>
      <button type="button" id="tema" class="btn" aria-label="Alternar tema claro e escuro" title="Alternar tema" hidden>◐</button>
    </div>
  </div>
${o.bilingue ? `  <div class="idiomas" id="idiomas" hidden>
    <div class="idiomas-int" role="group" aria-label="Textos visíveis: original e tradução">
      <button type="button" class="idioma" data-lado="orig" aria-pressed="false" title="Mostrar ou esconder o original">${esc(o.bilingue)}</button>
      <button type="button" class="idioma" data-lado="trad" aria-pressed="true" title="Mostrar ou esconder a tradução">Português</button>
    </div>
  </div>
` : ''}${o.progresso !== undefined ? `  <div class="barra-progresso" id="progresso" data-frac="${o.progresso.toFixed(4)}" hidden><span></span></div>\n` : ''}</header>

<main id="app" tabindex="-1">
${o.corpo}
</main>

<footer class="rodape">
  <p>Textos em domínio público. <a href="/">Taioé</a> · <a href="/privacidade/">Privacidade</a> · <a href="/termos/">Termos de uso</a></p>
</footer>
</body>
</html>
`;
  gravar(o.url, html);
  if (!o.semSitemap) sitemap.push(o.url);
}

// ------------------------------------------------------------------ páginas
function paginaCapa() {
  let html = '<div class="folha capa"><h1>Biblioteca</h1><p class="subtitulo">Textos em domínio público</p></div><div class="folha">' +
    '<div id="retomar"></div>' +
    '<p class="atalhos"><a href="' + BASE + 'lendo/">Em leitura</a><a href="' + BASE + 'lidos/">Lidos</a><a href="' + BASE + 'busca/">Buscar</a></p>' +
    '<p class="aviso-conta" id="aviso-conta">Sua posição de leitura fica salva só neste navegador. ' +
    '<a href="/entrar/?voltar=%2Fbiblioteca%2F">Entre com seu email</a> para guardá-la em qualquer aparelho.</p>' +
    '<p class="secao-titulo">Acervo</p>';
  AREAS.forEach((ar) => {
    const autores = autoresDaArea(ar.id), generos = [];
    autores.forEach((a) => generosDe(a.id).forEach((x) => { if (generos.indexOf(x.genero) < 0) generos.push(x.genero); }));
    generos.sort((x, y) => GENEROS.indexOf(x) - GENEROS.indexOf(y));
    html += '<a class="cartao pasta area" href="' + U.area(ar.id) + '">' +
      '<span class="cartao-titulo">' + esc(ar.nome) + '</span>' +
      '<span class="cartao-meta">' + (autores.length ? plural(autores.length, 'autor', 'autores') : 'em preparação') + '</span>' +
      (generos.length ? '<span class="cartao-texto">' + generos.map((g) => esc(nomeGenero(g))).join(' · ') + '</span>' : '') + '</a>';
  });
  html += '</div>';
  pagina({ url: U.capa(), titulo: '', corpo: html, trilha: [], dados: { pagina: 'capa' },
    descricao: 'Biblioteca Taioé: romances, contos, poesia e obras católicas em português, abertos a todos, para ler capítulo por capítulo.',
    jsonld: { '@context': 'https://schema.org', '@type': 'WebSite', name: 'Biblioteca Taioé', url: SITE + BASE, inLanguage: 'pt-BR' } });
}

/* «1839–1908» ou «~296–373» (o til marca o ano estimado) → os dois anos, para ordenar */
function anosDe(vida) {
  const m = String(vida || '').match(/(~?)(\d{1,4})\s*[–-]\s*(~?)(\d{1,4})/);
  return m ? { nasc: +m[2], morte: +m[4] } : { nasc: 9999, morte: 9999 };
}
function paginaArea(ar) {
  let html = '<div class="folha"><header class="cabeca"><h1>' + esc(ar.nome) + '</h1></header>' +
    '<div class="secao-titulo linha-ordem"><span>Autores</span><span class="ordenar" id="ordenar" hidden>' +
    '<button type="button" data-ordem="alfa" aria-pressed="true">A–Z</button>' +
    '<button type="button" data-ordem="nasc" aria-pressed="false">nascimento</button>' +
    '<button type="button" data-ordem="morte" aria-pressed="false">falecimento</button></span></div><div id="lista-autores">';
  autoresDaArea(ar.id).forEach((a, k) => {
    const obras = obrasDe(a.id), prosa = obras.filter((o) => !o.poema), versos = obras.length - prosa.length;
    const conta = [prosa.length ? plural(livros(prosa), 'obra', 'obras') : '', versos ? plural(versos, 'poema', 'poemas') : ''].filter(Boolean).join(' · ') || '0 obras';
    const anos = anosDe(a.vida);
    html += '<a class="cartao" href="' + U.autor(a) + '" data-alfa="' + k + '" data-nasc="' + anos.nasc + '" data-morte="' + anos.morte + '"><span class="cartao-titulo">' + esc(a.nome) + '</span>' +
      '<span class="cartao-meta">' + esc(a.vida || '') + (a.vida ? ' · ' : '') + conta + '</span>' +
      (obras.length ? '<span class="cartao-texto">' + generosDe(a.id).map((x) => esc(nomeGenero(x.genero))).join(' · ') + '</span>' : '') + '</a>';
  });
  html += '</div></div>';
  pagina({ url: U.area(ar.id), titulo: ar.nome, corpo: html, trilha: [{ txt: ar.nome }],
    descricao: `${ar.nome} na Biblioteca Taioé: ${autoresDaArea(ar.id).map((a) => a.nome).join(', ')}.` });
}

function cabecaAutor(a) {
  return '<header class="cabeca"><h1>' + esc(a.nome) + '</h1>' +
    '<p class="meta">' + esc([a.nomeCompleto, a.vida].filter(Boolean).join(' · ')) + '</p>' +
    (a.nota ? '<p class="nota-autor">' + inline(a.nota) + '</p>' : '') + '</header>';
}
function htmlPastas(a, obras) {
  const pastas = formasPasta(a.id);
  if (!pastas.length) return htmlListaPoemas(obras);
  const soltos = obras.filter((o) => !formaEhPasta(a.id, o.forma || 'outras'));
  let html = '<p class="secao-titulo">Formas</p>';
  pastas.forEach((x) => {
    const titulos = [];
    porColetanea(x.obras).forEach((g) => { if (g.titulo && titulos.indexOf(g.titulo) < 0) titulos.push(g.titulo); });
    html += '<a class="cartao pasta" href="' + U.pasta(a, x.forma.id) + '"><span class="cartao-titulo">' + esc(x.forma.nome) + '</span>' +
      '<span class="cartao-meta">' + plural(x.obras.length, 'poema', 'poemas') + '</span>' +
      (titulos.length ? '<span class="cartao-texto">' + titulos.map((t) => '<em>' + esc(t) + '</em>').join(', ') + '</span>' : '') + '</a>';
  });
  if (soltos.length) html += '<p class="secao-titulo">Outros poemas</p>' + htmlListaPoemas(soltos);
  return html;
}
function htmlListaPoemas(obras) {
  const grupos = porColetanea(obras); let html = '';
  grupos.forEach((g) => {
    const titulo = g.titulo || (grupos.length > 1 ? 'Avulsos' : '');
    if (titulo) html += '<p class="secao-titulo">' + (g.titulo ? '<em>' + esc(titulo) + '</em>' : esc(titulo)) + (g.ano ? ' · ' + g.ano : '') + '</p>';
    const comNum = g.obras.some((o) => o.n);
    html += '<ol class="indice poemas' + (comNum ? '' : ' sem-num') + '">';
    g.obras.forEach((o) => {
      const extra = o.traducao ? '<span class="orig-tit" lang="' + esc(o.traducao.codigo || '') + '">' + esc(o.traducao.titulo) + '</span>'
        : o.partes.length > 1 ? '<span class="orig-tit">' + esc(fichaObra(o)) + '</span>' : '';
      html += '<li data-obra="' + esc(chaveObra(o)) + '"><a href="' + U.obra(o) + '">' + (comNum ? '<span class="num">' + esc(o.n) + '</span>' : '') +
        '<span class="tit"' + (o.lingua ? ' lang="' + esc(o.lingua) + '"' : '') + '>' + esc(o.titulo) + extra + '</span></a></li>';
    });
    html += '</ol>';
  });
  return html;
}
function trilhaPasta(a, o) {
  const f = acharForma(o.forma || 'outras'), itens = [{ txt: a.nome, href: U.autor(a) }];
  if (!soPoesia(a.id) && generoEhPasta(a, 'Poesia')) itens.push({ txt: 'Poesia', href: U.genero(a, 'Poesia') });
  if (formaEhPasta(a.id, f.id)) itens.push({ txt: f.nome, href: U.pasta(a, f.id) });
  return comArea(a, itens);
}
const trilhaGenero = (a, g) => (generoEhPasta(a, g) ? { txt: nomeGenero(g), href: U.genero(a, g) } : null);

function paginaPasta(a, f) {
  const obras = poesiaDe(a.id).filter((o) => (o.forma || 'outras') === f.id);
  const itens = [{ txt: a.nome, href: U.autor(a) }];
  if (!soPoesia(a.id) && generoEhPasta(a, 'Poesia')) itens.push({ txt: 'Poesia', href: U.genero(a, 'Poesia') });
  const html = '<div class="folha"><header class="cabeca"><h1>' + esc(f.nome) + '</h1><p class="meta">' + esc(a.nome) + ' · ' +
    plural(obras.length, 'poema', 'poemas') + '</p></header>' + htmlListaPoemas(obras) + '</div>';
  pagina({ url: U.pasta(a, f.id), titulo: f.nome + ' — ' + a.nome, corpo: html, trilha: comArea(a, itens.concat({ txt: f.nome })),
    descricao: `${f.nome} de ${a.nome}: ${plural(obras.length, 'poema', 'poemas')} na Biblioteca Taioé.` });
}

function paginaAutor(a) {
  const desc = `${a.nome}${a.vida ? ' (' + a.vida + ')' : ''} na Biblioteca Taioé.${a.nota ? ' ' + textoPuro(a.nota) : ''}`;
  if (soPoesia(a.id)) {
    pagina({ url: U.autor(a), titulo: a.nome, corpo: '<div class="folha">' + cabecaAutor(a) + htmlPastas(a, poesiaDe(a.id)) + '</div>',
      trilha: comArea(a, [{ txt: a.nome }]), descricao: descricaoDe(desc) });
    return;
  }
  const generos = generosDe(a.id), pastas = generos.filter((x) => generoEhPasta(a, x.genero));
  const soltos = generos.filter((x) => !generoEhPasta(a, x.genero));
  let html = '<div class="folha">' + cabecaAutor(a) + (pastas.length ? '<p class="secao-titulo">Gêneros</p>' : '');
  pastas.forEach((x) => {
    const grupos = porColetanea(x.obras), titulos = [];
    grupos.forEach((g) => { if (g.titulo) titulos.push(g.titulo); else g.obras.forEach((o) => titulos.push(o.titulo)); });
    let meta = plural(livros(x.obras), 'obra', 'obras');
    if (grupos.some((g) => g.titulo)) {
      const t = TEXTOS[x.genero] || ['texto', 'textos'];
      meta += ' · ' + plural(x.obras.filter((o) => !o.paratexto).length, t[0], t[1]);
    }
    html += '<a class="cartao" href="' + U.genero(a, x.genero) + '"><span class="cartao-titulo">' + esc(nomeGenero(x.genero)) + '</span>' +
      '<span class="cartao-meta">' + meta + '</span><span class="cartao-texto">' + titulos.map((t) => '<em>' + esc(t) + '</em>').join(', ') + '</span></a>';
  });
  if (soltos.length) {
    html += '<p class="secao-titulo">' + (pastas.length ? 'Outras obras' : 'Obras') + '</p>';
    soltos.forEach((x) => { html += x.genero === 'Poesia' ? htmlListaPoemas(x.obras) : htmlObrasDoGenero(x.obras); });
  }
  html += '</div>';
  pagina({ url: U.autor(a), titulo: a.nome, corpo: html, trilha: comArea(a, [{ txt: a.nome }]), descricao: descricaoDe(desc) });
}

/* As obras de um gênero, agrupadas por coletânea: o corpo da página do gênero, ou a lista solta
   na página do autor quando o gênero não chega a ser categoria. */
function htmlObrasDoGenero(obras) {
  let html = '';
  porColetanea(obras).forEach((g) => {
    if (g.titulo) html += '<p class="secao-titulo"><em>' + esc(g.titulo) + '</em>' + (g.ano ? ' · ' + g.ano : '') + '</p>';
    g.obras.forEach((o) => {
      const pub = textoPublicacao(o);
      html += '<a class="cartao' + (o.paratexto ? ' paratexto' : '') + '" href="' + U.obra(o) + '" data-obra="' + esc(chaveObra(o)) + '">' +
        '<span class="cartao-titulo">' + (o.coletanea ? esc(o.titulo) : '<em>' + esc(o.titulo) + '</em>') + '</span>' +
        '<span class="cartao-meta">' + esc(fichaObra(o)) + '</span>' + (pub ? '<span class="cartao-texto">' + inline(pub) + '</span>' : '') + '</a>';
    });
  });
  return html;
}

function paginaGenero(a, x) {
  let html = '<div class="folha"><header class="cabeca"><h1>' + esc(nomeGenero(x.genero)) + '</h1><p class="meta">' + esc(a.nome) + '</p></header>';
  const trilha = comArea(a, [{ txt: a.nome, href: U.autor(a) }, { txt: nomeGenero(x.genero) }]);
  if (x.genero === 'Poesia') {
    pagina({ url: U.genero(a, x.genero), titulo: 'Poesia — ' + a.nome, corpo: html + htmlPastas(a, x.obras) + '</div>', trilha,
      descricao: `Poesia de ${a.nome} na Biblioteca Taioé.` });
    return;
  }
  html += htmlObrasDoGenero(x.obras) + '</div>';
  pagina({ url: U.genero(a, x.genero), titulo: nomeGenero(x.genero) + ' — ' + a.nome, corpo: html, trilha,
    descricao: descricaoDe(`${nomeGenero(x.genero)} de ${a.nome} na Biblioteca Taioé: ${x.obras.map((o) => o.titulo).join(', ')}.`) });
}

function trilhaObra(a, o) {
  return o.poema ? trilhaPasta(a, o) : comArea(a, [{ txt: a.nome, href: U.autor(a) }, trilhaGenero(a, o.genero || 'Outros')].filter(Boolean));
}
function jsonObra(a, o) {
  return { '@context': 'https://schema.org', '@type': o.poema ? 'CreativeWork' : 'Book', name: o.titulo, inLanguage: 'pt-BR',
    author: { '@type': 'Person', name: a.nomeCompleto || a.nome }, url: SITE + U.obra(o),
    ...(o.ano ? { datePublished: String(o.ano) } : {}), isAccessibleForFree: true,
    ...(o.traducao ? { translationOfWork: { '@type': 'CreativeWork', name: o.traducao.titulo || o.titulo, inLanguage: o.traducao.codigo || undefined } } : {}),
    publisher: { '@type': 'Organization', name: 'Taioé', url: SITE + '/' } };
}

function paginaObra(a, o) {
  const d = o.divisao || { singular: 'parte', plural: 'partes' };
  let html = '<div class="folha"><header class="rosto"><p class="rosto-autor">' + esc(a.nome) + '</p><h1>' + esc(o.titulo) + '</h1>' +
    (o.subtitulo ? '<p class="subtitulo-obra">' + inline(o.subtitulo) + '</p>' : '') +
    '<p class="meta">' + (o.coletanea && o.coletanea.titulo !== o.titulo ? '<em>' + esc(o.coletanea.titulo) + '</em>' + (o.coletanea.ano ? ', ' + esc(o.coletanea.ano) : '') + ' · '
      : o.poema && o.ano ? esc(o.ano) + ' · ' : '') + esc(fichaObra(o)) + '</p>' +
    (o.publicacao ? '<p class="publicacao">' + inline(textoPublicacao(o)) + '</p>' : '') +
    (o.traducao && !o.poema ? '<p class="publicacao">Tradução do ' + esc(o.traducao.lingua) +
      (o.traducao.titulo ? ' (<em lang="' + esc(o.traducao.codigo || '') + '">' + esc(o.traducao.titulo) + '</em>)' : '') + '</p>' : '') +
    (o.descricao ? '<p class="descricao">' + inline(o.descricao) + '</p>' : '') +
    '<p class="aviso-outro" id="aviso-outro" hidden></p>' +
    '<p class="acoes"><a class="botao" id="comecar" href="' + folhasDe(o)[0].url + '">Começar a ler</a>' +
    (o.edicao ? ' <a class="botao secundario" href="' + U.sobre(o) + '">' + esc(tituloSobre(o)) + '</a>' : '') + '</p>' +
    '<div class="estado-leitura" id="estado-leitura" data-alvo="obra" hidden></div></header>' +
    '<p class="secao-titulo">' + esc(d.plural.charAt(0).toUpperCase() + d.plural.slice(1)) + '</p><ol class="indice">';
  const agrupa = o.divisao && (o.divisao.rotulo === 'titulo' || o.divisao.agrupar);
  o.partes.forEach((p, i) => {
    const num = agrupa && i && o.partes[i - 1].n === p.n ? '' : p.n;
    html += '<li data-parte="' + p.slug + '"><a href="' + U.parte(o, i + 1) + '"><span class="num">' + esc(num) + '</span>' +
      '<span class="tit">' + (p.titulo ? inline(p.titulo) : '<span class="inc">' + incipit(p.texto, 60) + '</span>') +
      (p.folhas ? '<span class="folhas">' + esc(p.folhas) + '</span>' : '') +
      (p.filhos ? '<span class="folhas">' + contaFilhos(p.filhos) + '</span>' : '') + '</span></a></li>';
  });
  html += '</ol></div>';
  pagina({ url: U.obra(o), titulo: o.titulo + ' — ' + a.nome, corpo: html, trilha: trilhaObra(a, o).concat({ txt: o.titulo }),
    descricao: descricaoDe(o.descricao || `${o.titulo}, de ${a.nome}${o.ano ? ' (' + (o.datas || o.ano) + ')' : ''}: ${fichaObra(o)}. Leia na Biblioteca Taioé.`),
    dados: { pagina: 'obra', obra: chaveObra(o), 'titulo-obra': o.titulo, total: o.partes.length,
      ...(dividida(o) ? { estrutura: estruturaCurta(o) } : {}) }, jsonld: jsonObra(a, o) });
}

const contaFilhos = (l) => (l.every((y) => y.tipo === 'capitulo') ? plural(l.length, 'capítulo', 'capítulos') : plural(l.length, 'seção', 'seções'));
/* rótulo de uma folha nos passos «Anterior»/«Seguinte»: a parte, como sempre; o capítulo ou a seção
   com o número e o título, e com a parte na frente quando é de outra parte */
function rotuloFolha(o, f, daqui) {
  if (!f.cadeia.length) return rotuloPasso(f.parte);
  const x = f.no, nome = x.tipo === 'capitulo' ? 'Capítulo ' + esc(x.n) + ' · ' + inline(x.titulo)
    : x.tipo === 'abertura' ? 'Abertura · ' + inline(x.titulo) : esc(x.n) + (/\)$/.test(x.n) ? ' ' : '. ') + inline(x.titulo);
  return (daqui && daqui.parte === f.parte ? '' : esc(rotuloParte(o, f.parte)) + ' · ') + nome;
}
/* a trilha até um item dentro da parte: Área › Autor › Obra › Parte › Capítulo (› Seção) */
function trilhaDentro(a, o, x) {
  const passos = [{ txt: a.nome, href: U.autor(a) }, { txt: o.titulo, href: U.obra(o) }, { txt: rotuloParte(o, x.parte), href: U.parte(o, x.i) }];
  x.cadeia.forEach((y, j) => passos.push({ txt: curto(y), href: U.parte(o, x.i) + x.cadeia.slice(0, j + 1).map((z) => z.slug + '/').join('') }));
  delete passos[passos.length - 1].href;
  return comArea(a, passos);
}
const passo = (cls, rel, dir, href, alvo) => '<a class="passo ' + cls + '" href="' + href + '" rel="' + rel + '"><span class="dir">' + dir + '</span><span class="alvo">' + alvo + '</span></a>';
function paginaParte(a, o, f) {
  const fs_ = folhasDe(o), i = f.k + 1, total = fs_.length, poema = !!o.poema, conto = !!o.coletanea || poema;
  const p = f.no, sub = f.cadeia.length > 0, partes = o.partes.length;
  const bilingue = p.original !== undefined && p.original !== null;
  let passos;
  if (poema) {
    passos = trilhaPasta(a, o).concat(total > 1 ? [{ txt: o.titulo, href: U.obra(o) }, { txt: rotuloParte(o, p) }] : [{ txt: o.titulo }]);
  } else if (sub) {
    passos = trilhaDentro(a, o, f);
  } else {
    passos = [{ txt: a.nome, href: U.autor(a) }, { txt: o.titulo, href: U.obra(o) }, { txt: rotuloParte(o, p) }];
    if (conto) {
      if (trilhaGenero(a, o.genero || 'Outros')) passos.splice(1, 0, trilhaGenero(a, o.genero || 'Outros'));
      if (total === 1) passos = passos.slice(0, 2).concat({ txt: o.titulo });
    }
    passos = comArea(a, passos);
  }
  const indice = (href, alvo) => '<a class="passo seg" href="' + href + '"><span class="dir">Índice</span><span class="alvo">' + esc(alvo) + '</span></a>';
  let navAnt = '<span class="passo vazio"></span>', navSeg, prev = null, next = null;
  const irmaos = poema ? vizinhosPoema(o) : conto ? daColetanea(o) : [], k = irmaos.indexOf(o);
  if (i > 1) { const x = fs_[i - 2]; prev = x.url; navAnt = passo('ant', 'prev', '← Anterior', prev, rotuloFolha(o, x, f)); }
  else if (k > 0) { const x = irmaos[k - 1]; prev = U.parte(x, x.partes.length); navAnt = passo('ant', 'prev', '← Anterior', prev, esc(x.titulo)); }
  if (i < total) { const x = fs_[i]; next = x.url; navSeg = passo('seg', 'next', 'Seguinte →', next, rotuloFolha(o, x, f)); }
  else if (k >= 0 && k < irmaos.length - 1) { const x = irmaos[k + 1]; next = U.parte(x, 1); navSeg = passo('seg', 'next', 'Seguinte →', next, esc(x.titulo)); }
  else if (poema) navSeg = indice(U.indicePoema(a, o), formaEhPasta(a.id, o.forma || 'outras') ? acharForma(o.forma || 'outras').nome
    : U.poesia(a) === U.autor(a) ? a.nome : 'Poesia');
  else if (conto) navSeg = generoEhPasta(a, o.genero) ? indice(U.genero(a, o.genero), nomeGenero(o.genero)) : indice(U.autor(a), a.nome);
  else navSeg = indice(U.obra(o), o.titulo);

  function titulo(tag, cls, trad, orig) {
    const h = '<' + tag + (cls ? ' class="' + cls + '"' : '') + '>';
    if (!bilingue || !orig) return h + inline(trad) + '</' + tag + '>';
    const lingua = o.traducao ? o.traducao.codigo || '' : '';
    return '<div class="paralelo titulos"><div class="orig" data-i="t"' + (lingua ? ' lang="' + esc(lingua) + '"' : '') + '>' + h + inline(orig) + '</' + tag + '></div>' +
      '<div class="trad" data-i="t">' + h + inline(trad) + '</' + tag + '></div></div>';
  }
  let cabeca;
  if (conto) {
    const livro = [o.coletanea ? '<em>' + esc(o.coletanea.titulo) + '</em>' : '', o.secao ? esc(o.secao) : ''].filter(Boolean).join(' · ');
    cabeca = (i === 1 ? (livro ? '<p class="coletanea-parte">' + livro + '</p>' : '') +
      (poema && o.n ? '<p class="num-parte">' + esc(o.n) + '</p>' : '') +
      titulo('h1', 'titulo-conto', o.titulo, o.traducao && o.traducao.titulo) +
      (o.subtitulo ? '<p class="subtitulo-obra">' + inline(o.subtitulo) + '</p>' : '') +
      (o.traducao ? '<p class="publicacao">Tradução do ' + esc(o.traducao.lingua) + '</p>' : '') +
      (o.publicacao ? '<p class="publicacao">' + inline(textoPublicacao(o)) + '</p>' : '') : '') +
      (total > 1 ? (p.n ? '<p class="num-parte">' + esc(p.n) + '</p>' : '') + (p.titulo ? titulo('h2', '', p.titulo, p.tituloOriginal) : '') : '');
  } else if (sub) {
    cabeca = '<p class="num-parte">' + esc([rotuloParte(o, f.parte)].concat(f.cadeia.slice(0, -1).map(curto)).join(' · ')) + '</p>' +
      titulo('h1', '', p.cab, p.cabOriginal);
  } else {
    cabeca = (p.n ? '<p class="num-parte">' + esc(p.n) + '</p>' : '') + (p.titulo ? titulo('h1', '', p.titulo, p.tituloOriginal) : '');
  }
  if (!/<h1/.test(cabeca)) cabeca = '<h1 class="visualmente-oculto">' + esc(rotuloParte(o, p) === o.titulo ? o.titulo : o.titulo + ' — ' + rotuloParte(o, p)) + '</h1>' + cabeca;
  /* onde se está: entre as partes, ou entre os irmãos do capítulo (ou da seção), com o índice de cima */
  let posicao = '';
  if (sub) {
    const pai = infoNo(o, f.i, f.cadeia.slice(0, -1)), lista = pai.no.filhos;
    posicao = '<p class="posicao">' + (lista.indexOf(p) + 1) + ' de ' + lista.length + ' · <a href="' + pai.url + '">' +
      esc(pai.cadeia.length ? curto(pai.no) : rotuloParte(o, pai.parte)) + '</a> · <a href="' + U.obra(o) + '">índice</a></p>';
  } else if (partes > 1) posicao = '<p class="posicao">' + f.i + ' de ' + partes + ' · <a href="' + U.obra(o) + '">índice</a></p>';
  const alvo = !sub ? 'parte' : p.tipo === 'capitulo' ? 'capitulo' : 'secao';
  const lingua = bilingue && o.traducao ? o.traducao.codigo || '' : '';
  const html = '<p class="aviso-outro" id="aviso-outro" hidden></p>' +
    '<article class="folha leitura' + (poema ? ' de-poema' : '') + (bilingue ? ' bilingue ver-trad' : '') + '"' + (lingua ? ' data-lingua="' + esc(lingua) + '"' : '') + '>' +
    '<header class="cabeca-parte' + (conto && i === 1 ? ' conto' : '') + '">' + cabeca + '</header>' + textoParte(o, p) +
    '<div id="fim-parte" aria-hidden="true"></div>' +
    (i < total || poema ? '' : '<p class="fim">Fim</p>') +
    '<div class="estado-leitura" id="estado-leitura" data-alvo="' + alvo + '" hidden></div>' +
    '<nav class="passos" aria-label="Navegação entre ' + esc(poema && total === 1 ? 'poemas' : dividida(o) ? 'capítulos' : o.divisao ? o.divisao.plural : 'partes') + '">' + navAnt + navSeg + '</nav>' +
    posicao +
    (conto && o.edicao && i === total ? '<p class="posicao"><a href="' + U.sobre(o) + '">' + esc(tituloSobre(o)) + '</a></p>' : '') + '</article>';
  const rot = sub ? f.rotulo : rotuloParte(o, p);
  const tituloPagina = sub ? rot + ': ' + textoPuro(p.titulo) + ' — ' + o.titulo + ' — ' + a.nome
    : (rot && rot !== o.titulo ? rot + (p.titulo && rot.indexOf(textoPuro(p.titulo)) < 0 ? ': ' + textoPuro(p.titulo) : '') + ' — ' : '') + o.titulo + ' — ' + a.nome;
  pagina({ url: f.url, titulo: tituloPagina, corpo: html, trilha: passos, prev, next,
    bilingue: bilingue ? (o.traducao && o.traducao.lingua ? o.traducao.lingua.charAt(0).toUpperCase() + o.traducao.lingua.slice(1) : 'Original') : null,
    progresso: total > 1 ? i / total : undefined,
    descricao: descricaoDe(p.texto),
    dados: { pagina: 'parte', obra: chaveObra(o), parte: f.chave, indice: i, total, ...(sub ? { cadeia: f.acima.join(' ') } : {}),
      rotulo: rot === o.titulo ? '' : rot, 'titulo-obra': o.titulo, 'url-obra': U.obra(o) },
    jsonld: umaParte(o) ? jsonObra(a, o) : { '@context': 'https://schema.org', '@type': 'Chapter', name: tituloPagina.replace(/ — [^—]+$/, ''),
      position: i, isPartOf: { '@type': 'Book', name: o.titulo, url: SITE + U.obra(o) }, author: { '@type': 'Person', name: a.nomeCompleto || a.nome }, inLanguage: 'pt-BR' } });
}

/* Página de índice dentro da obra: a parte com capítulos (no endereço que a parte sempre teve) ou o
   capítulo com seções. Lista aberta, sem recolher; «Começar a ler» vai à primeira folha, e as setas
   e os passos seguem a ordem de leitura (a folha antes deste índice e a primeira dele). Cada item
   leva a linha em que começava na página antiga da parte (data-linha), para o leitor.js levar ao
   capítulo certo quem tinha parado no meio da parte inteira. */
function paginaIndice(a, o, x) {
  const fs_ = folhasDe(o), p = x.no, ehParte = !x.cadeia.length;
  const primeira = fs_.find((f) => f.parte === x.parte && x.cadeia.every((y, j) => f.cadeia[j] === y)), antes = fs_[primeira.k - 1];
  const prev = antes ? antes.url : null, next = primeira.url;
  const navAnt = antes ? passo('ant', 'prev', '← Anterior', prev, rotuloFolha(o, antes, x)) : '<span class="passo vazio"></span>';
  const navSeg = passo('seg', 'next', 'Seguinte →', next, rotuloFolha(o, primeira, x));
  const cabeca = ehParte ? (p.n ? '<p class="num-parte">' + esc(p.n) + '</p>' : '') + '<h1>' + inline(p.titulo || rotuloParte(o, p)) + '</h1>'
    : '<p class="num-parte">' + esc([rotuloParte(o, x.parte)].concat(x.cadeia.slice(0, -1).map(curto)).join(' · ')) + '</p><h1>' + inline(p.cab) + '</h1>';
  const pre = ehParte && p.preambulo ? '<div class="preambulo">' + blocos(p.preambulo) + '</div>' : '';
  const nome = contaFilhos(p.filhos).replace(/^\d+ /, '');
  let html = '<p class="aviso-outro" id="aviso-outro" hidden></p><div class="folha indice-parte"><header class="cabeca-parte">' + cabeca + pre + '</header>' +
    '<p class="acoes"><a class="botao" id="comecar" href="' + primeira.url + '">Começar a ler</a></p>' +
    '<div class="estado-leitura" id="estado-leitura" data-alvo="' + (ehParte ? 'parte' : 'capitulo') + '" hidden></div>' +
    '<p class="secao-titulo">' + esc(nome.charAt(0).toUpperCase() + nome.slice(1)) + '</p>' +
    '<ol class="indice" id="indice-no"' + (ehParte ? ' data-celulas="' + (p.original !== undefined && p.original !== null ? 2 : 1) + '"' : '') + '>';
  p.filhos.forEach((y) => {
    const z = infoNo(o, x.i, x.cadeia.concat(y));
    html += '<li data-no="' + z.chave + '"' + (ehParte ? ' data-linha="' + y.linha + '"' : '') + ' data-rotulo="' + esc(z.rotulo) + '"><a href="' + z.url + '">' +
      '<span class="num">' + esc(y.tipo === 'abertura' ? '' : y.n) + '</span><span class="tit">' + (y.tipo === 'abertura' ? 'Abertura' : inline(y.titulo)) +
      (y.filhos ? '<span class="folhas">' + contaFilhos(y.filhos) + '</span>' : '') + '</span></a></li>';
  });
  const pai = ehParte ? null : infoNo(o, x.i, x.cadeia.slice(0, -1)), irmaos = pai ? pai.no.filhos : o.partes;
  html += '</ol><nav class="passos" aria-label="Navegação entre capítulos">' + navAnt + navSeg + '</nav>' +
    '<p class="posicao">' + (irmaos.indexOf(p) + 1) + ' de ' + irmaos.length +
    (pai ? ' · <a href="' + pai.url + '">' + esc(pai.cadeia.length ? curto(pai.no) : rotuloParte(o, pai.parte)) + '</a>' : '') +
    ' · <a href="' + U.obra(o) + '">índice</a></p></div>';
  const rot = x.rotulo, tit = p.titulo;
  const tituloPagina = (tit && rot.indexOf(textoPuro(tit)) < 0 ? rot + ': ' + textoPuro(tit) : rot) + ' — ' + o.titulo + ' — ' + a.nome;
  pagina({ url: x.url, titulo: tituloPagina, corpo: html, trilha: trilhaDentro(a, o, x), prev, next,
    descricao: descricaoDe(`${rot}${tit ? ': ' + tit : ''}, de ${o.titulo}, de ${a.nome}: ${contaFilhos(p.filhos)}. ${p.preambulo || ''}`),
    dados: { pagina: 'no', obra: chaveObra(o), no: x.chave, ...(x.acima.length ? { cadeia: x.acima.join(' ') } : {}),
      estrutura: estruturaCurta(o), rotulo: rot, 'titulo-obra': o.titulo, 'url-obra': U.obra(o) } });
}

function colunaLugar(itens, rotParte) {
  const tem = itens.some((v) => v.cap);
  return { th: tem ? '<th>' + esc(rotParte) + '</th>' : '', td: (v) => (tem ? '<td class="cap">' + esc(v.cap || 'Texto') + '</td>' : '') };
}
function listaVariantes(itens, rotDe, rotPara, rotParte) {
  const c = colunaLugar(itens, rotParte);
  return '<table class="variantes"><thead><tr>' + c.th + '<th>' + esc(rotDe) + '</th><th>' + esc(rotPara) + '</th></tr></thead><tbody>' +
    itens.map((v) => '<tr>' + c.td(v) + '<td>' + esc(v.de) + '</td><td>' + esc(v.para) + '</td></tr>').join('') + '</tbody></table>';
}
function paginaSobre(a, o) {
  const e = o.edicao, d = o.divisao || { singular: 'parte' };
  const rotParte = o.coletanea && o.partes.length === 1 ? 'Onde' : d.singular.charAt(0).toUpperCase() + d.singular.slice(1);
  const rotBase = e.base || '1ª edição', tit = tituloSobre(o);
  let html = '<article class="folha sobre"><header class="cabeca"><h1>' + esc(tit) + '</h1><p class="meta">' +
    (o.coletanea ? esc(o.titulo) + ' · <em>' + esc(o.coletanea.titulo) + '</em>' : '<em>' + esc(o.titulo) + '</em>') + ' · ' + esc(a.nome) + '</p></header>' +
    '<div class="texto">' + blocos(e.apresentacao || '') + '</div>';
  const S = e.secoes || {};
  const secao = (nome, padrao) => { const s = S[nome] || {}; return { titulo: s.titulo || padrao.titulo, explica: s.explica || padrao.explica, de: s.de || padrao.de || rotBase, para: s.para || padrao.para }; };
  let s;
  if (e.erros && e.erros.length) {
    s = secao('erros', { titulo: 'Erros tipográficos da 1ª edição corrigidos', explica: 'Grafia da 1ª edição nas duas colunas.', para: 'Corrigido' });
    html += '<h2>' + esc(s.titulo) + '</h2><p class="explica">' + esc(s.explica) + ' ' + e.erros.length + ' correções.</p>' + listaVariantes(e.erros, s.de, s.para, rotParte);
  }
  if (e.tradicao && e.tradicao.length) {
    s = secao('tradicao', { titulo: 'Lições da 2ª edição adotadas', explica: 'Leituras em que todas as edições posteriores concordam contra a 1ª. Grafia da 1ª edição.', para: 'Adotado' });
    html += '<h2>' + esc(s.titulo) + '</h2><p class="explica">' + esc(s.explica) + '</p>' + listaVariantes(e.tradicao, s.de, s.para, rotParte);
  }
  if (e.pontuacao && e.pontuacao.length) {
    s = secao('pontuacao', { titulo: 'Pontuação da 2ª edição adotada', explica: 'Mesmo critério: só onde toda a tradição posterior concorda. Grafia atualizada.', para: 'Adotado' });
    html += '<h2>' + esc(s.titulo) + '</h2><p class="explica">' + esc(s.explica) + '</p>' + listaVariantes(e.pontuacao, s.de, s.para, rotParte);
  }
  if (e.mantidas && e.mantidas.length) {
    s = secao('mantidas', { titulo: 'Leituras da 1ª edição mantidas', explica: 'Pontos em que parte das edições modernas lê diferente.' });
    const cm = colunaLugar(e.mantidas, rotParte);
    html += '<h2>' + esc(s.titulo) + '</h2><p class="explica">' + esc(s.explica) + '</p><table class="variantes"><thead><tr>' + cm.th +
      '<th>Este texto</th><th>Outras edições</th></tr></thead><tbody>' +
      e.mantidas.map((v) => '<tr>' + cm.td(v) + '<td>' + esc(v.texto) + '</td><td>' + esc(v.variante) + (v.obs ? '<span class="obs">' + esc(v.obs) + '</span>' : '') + '</td></tr>').join('') + '</tbody></table>';
  }
  if (e.fontes && e.fontes.length) {
    html += '<h2>Fontes consultadas</h2><ul class="fontes">' + e.fontes.map((f) => {
      const nome = f.url ? '<a href="' + esc(f.url) + '" target="_blank" rel="noopener">' + esc(f.nome) + '</a>' : esc(f.nome);
      return '<li>' + nome + (f.nota ? ' — <span class="obs-inline">' + esc(f.nota) + '</span>' : '') + '</li>';
    }).join('') + '</ul>';
  }
  html += '<p class="posicao"><a href="' + U.obra(o) + '">' + (umaParte(o) ? 'Voltar ao texto' : 'Voltar ao índice') + '</a></p></article>';
  pagina({ url: U.sobre(o), titulo: tit + ' — ' + o.titulo, corpo: html, trilha: trilhaObra(a, o).concat({ txt: o.titulo, href: U.obra(o) }, { txt: tit }),
    descricao: descricaoDe(`${tit}: ${o.titulo}, de ${a.nome}. ${e.apresentacao || ''}`) });
}

function paginasDoLeitor() {
  const casca = (url, titulo, explica, id) => pagina({ url, titulo, semSitemap: true, trilha: [{ txt: titulo }], dados: { pagina: id },
    descricao: titulo + ' na Biblioteca Taioé.',
    corpo: '<div class="folha"><header class="cabeca"><h1>' + esc(titulo) + '</h1><p class="meta">' + esc(explica) + '</p></header>' +
      '<div id="lista-leitor" class="lista-leitor"><p class="explica">Carregando…</p></div></div>' });
  casca(BASE + 'lendo/', 'Em leitura', 'Os livros que você começou, o aberto mais recentemente primeiro.', 'lendo');
  casca(BASE + 'lidos/', 'Lidos', 'Os livros que você leu por inteiro.', 'lidos');
  pagina({ url: BASE + 'busca/', titulo: 'Buscar', trilha: [{ txt: 'Buscar' }], dados: { pagina: 'busca' },
    descricao: 'Busque livros, poemas e autores na Biblioteca Taioé, ou palavras dentro dos textos.',
    corpo: '<div class="folha"><header class="cabeca"><h1>Buscar</h1></header>' +
      '<form class="busca" id="busca" role="search"><input type="search" id="busca-q" name="q" autocomplete="off" ' +
      'placeholder="título, autor ou palavra do texto" aria-label="Buscar"></form>' +
      '<p class="modos" role="group" aria-label="Onde buscar"><button type="button" data-modo="titulos" aria-pressed="true">Títulos e autores</button>' +
      '<button type="button" data-modo="textos" aria-pressed="false">Dentro dos textos</button></p>' +
      '<div id="busca-resultados" class="busca-resultados" aria-live="polite"><noscript><p class="explica">A busca precisa de JavaScript.</p></noscript></div></div>' });
}

// ------------------------------------------------------------------ gerar
fs.rmSync(SAIDA, { recursive: true, force: true });
fs.mkdirSync(SAIDA, { recursive: true });

paginaCapa();
AREAS.forEach(paginaArea);
paginasDoLeitor();
dados.autores.forEach((a) => {
  if (!obrasDe(a.id).length) return;
  paginaAutor(a);
  generosDe(a.id).forEach((x) => { if (!(x.genero === 'Poesia' && soPoesia(a.id)) && generoEhPasta(a, x.genero)) paginaGenero(a, x); });
  formasPasta(a.id).forEach((x) => paginaPasta(a, x.forma));
});
dados.obras.forEach((o) => {
  const a = acharAutor(o.autor) || { nome: o.autor, id: o.autor };
  if (!umaParte(o)) paginaObra(a, o);
  folhasDe(o).forEach((f) => paginaParte(a, o, f));
  nosDe(o).forEach((x) => paginaIndice(a, o, x));
  if (o.edicao) paginaSobre(a, o);
});

// 404, estilo, leitor, ícone, cópias do login
const html404 = `<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Página não encontrada · Biblioteca Taioé</title>
<meta name="color-scheme" content="light dark">
<link rel="icon" href="${BASE}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="${BASE}css/estilo.css?v=${V_CSS}">
<script defer src="${BASE}js/leitor.js?v=${V_JS}"></script>
</head>
<body data-pagina="404">
<header class="topo"><div class="topo-int"><a class="marca" href="${BASE}">Biblioteca</a><nav class="topo-nav" id="trilha"></nav></div></header>
<main id="app" tabindex="-1"><div class="folha cabeca"><h1>Página não encontrada</h1><p><a href="${BASE}">Voltar à capa da Biblioteca</a></p></div></main>
<footer class="rodape"><p>Textos em domínio público. <a href="/">Taioé</a></p></footer>
</body>
</html>
`;
fs.writeFileSync(path.join(SAIDA, '404.html'), html404);
fs.mkdirSync(path.join(SAIDA, 'css'), { recursive: true });
fs.mkdirSync(path.join(SAIDA, 'js'), { recursive: true });
fs.writeFileSync(path.join(SAIDA, 'css', 'estilo.css'), CSS);
fs.writeFileSync(path.join(SAIDA, 'js', 'leitor.js'), LEITOR);
fs.copyFileSync(path.join(RAIZ, 'favicon.svg'), path.join(SAIDA, 'favicon.svg'));
// cópias idênticas do taioe-hub (o workflow Cópias confere o sha256)
fs.mkdirSync(path.join(SAIDA, 'vendor'), { recursive: true });
fs.writeFileSync(path.join(SAIDA, 'vendor', 'supabase-js-2.117.2.js'), lerLf(path.join(RAIZ, 'ferramentas', 'site', 'comum', 'supabase-js-2.117.2.js')));
fs.writeFileSync(path.join(SAIDA, 'js', 'taioe-sessao.js'), lerLf(path.join(RAIZ, 'ferramentas', 'site', 'comum', 'taioe-sessao.js')));

// índice compacto das obras: títulos e partes, para «Continuar a leitura» de outro aparelho
// e para converter os endereços antigos (#/o/<id>/<n>). Parte dividida: [slug, rótulo, capítulos],
// e cada capítulo [slug, rótulo] ou [slug, rótulo, seções] (ver arvore() no leitor.js).
const indiceObras = {};
dados.obras.forEach((o) => {
  const a = acharAutor(o.autor);
  indiceObras[chaveObra(o)] = { i: o.id, t: o.titulo, a: a ? a.nome : o.autor, u: U.obra(o), p: umaParte(o) ? [['texto', '']] : estrutura(o) };
});
fs.writeFileSync(path.join(SAIDA, 'obras.json'), JSON.stringify(indiceObras));

/* ── a busca ──
   busca/titulos.json: obras e autores, para a busca por nome (no navegador: começo do nome
   primeiro, depois qualquer parte). busca/docs.json: as partes (obra, parte), na ordem dos
   números do índice. busca/i/<xy>.json: o índice invertido dos textos, partido pelas duas
   primeiras letras da palavra: { palavra: "números das partes, em base 36, por diferença" }.
   Nas partes divididas, cada capítulo (ou seção) é um documento: [obra, parte, capítulo(, seção)];
   o preâmbulo da parte, quando há, fica no documento [obra, parte], o índice dela. */
const STOP = new Set(('de da do das dos a o as os e é em um uma uns umas no na nos nas ao aos à às que se por para com ' +
  'não mas ou como mais lhe lhes me te vos seu sua seus suas meu minha meus minhas teu tua ele ela eles elas eu tu ' +
  'isso isto este esta estes estas esse essa esses essas aquele aquela era foi ser há já só the and of to in that is it ' +
  'le la les et des un une du en est qui der die das und den dem ist ein eine nicht zu mit sich non ad cum').split(' ')
  .map((w) => w.normalize('NFD').replace(/[\u0300-\u036f]/g, '')));
const normal = (t) => String(t).toLowerCase().replace(/ß/g, 'ss').replace(/æ/g, 'ae').replace(/œ/g, 'oe')
  .normalize('NFD').replace(/[\u0300-\u036f]/g, '');
const limpo = (t) => String(t || '').replace(/\{[^}]*\}/g, ' ').replace(/^::.*$/gm, ' ').replace(/[_*|]/g, ' ');
const titulos = [];
dados.autores.forEach((a) => { if (obrasDe(a.id).length) titulos.push([a.nome, '', U.autor(a), 'autor']); });
dados.obras.filter((o) => !o.paratexto).forEach((o) => {
  const a = acharAutor(o.autor);
  titulos.push([o.titulo, a ? a.nome : o.autor, U.obra(o), o.poema ? 'poema' : 'obra',
    ...(o.traducao && o.traducao.titulo ? [o.traducao.titulo] : [])]);
});
fs.mkdirSync(path.join(SAIDA, 'busca', 'i'), { recursive: true });
fs.writeFileSync(path.join(SAIDA, 'busca', 'titulos.json'), JSON.stringify(titulos));
const chaves = [], docs = [], postings = new Map();
dados.obras.forEach((o) => {
  const oi = chaves.push(chaveObra(o)) - 1;
  const indexar = (caminho, texto) => {
    const d = docs.push([oi, ...caminho]) - 1;
    const vistas = new Set((normal(texto).match(/[a-z0-9]+/g) || [])
      .filter((w) => w.length >= 2 && w.length <= 30 && !STOP.has(w)));
    vistas.forEach((w) => { let l = postings.get(w); if (!l) postings.set(w, (l = [])); l.push(d); });
  };
  const andar = (lista, caminho) => lista.forEach((y, yi) => {
    if (y.filhos) andar(y.filhos, caminho.concat(yi));
    else indexar(caminho.concat(yi), limpo(y.cab) + ' ' + limpo(y.texto) + ' ' + limpo(y.cabOriginal) + ' ' + limpo(y.original));
  });
  o.partes.forEach((p, pi) => {
    if (!p.filhos) { indexar([pi], limpo(p.texto) + ' ' + limpo(p.original)); return; }
    if (p.preambulo) indexar([pi], limpo(p.preambulo));
    andar(p.filhos, [pi]);
  });
});
fs.writeFileSync(path.join(SAIDA, 'busca', 'docs.json'), JSON.stringify({ o: chaves, d: docs }));
const shards = {};
[...postings.keys()].sort().forEach((w) => {
  const k = w.slice(0, 2), ids = postings.get(w);
  let ant = 0;
  (shards[k] = shards[k] || {})[w] = ids.map((x) => { const v = (x - ant).toString(36); ant = x; return v; }).join(',');
});
Object.entries(shards).forEach(([k, m]) => fs.writeFileSync(path.join(SAIDA, 'busca', 'i', k + '.json'), JSON.stringify(m)));

fs.writeFileSync(path.join(SAIDA, 'sitemap.xml'), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  sitemap.map((u) => `<url><loc>${SITE}${u}</loc></url>`).join('\n') + '\n</urlset>\n');  // sem data: gerar de novo dá o mesmo arquivo

// endereços congelados (só acrescenta; nunca muda um que já existe)
const juntos = { ...congelados };
Object.entries(enderecos).forEach(([id, mapa]) => { juntos[id] = { ...(congelados[id] || {}), ...mapa }; });
fs.writeFileSync(ARQ_ENDERECOS, '{\n' + Object.keys(juntos).sort().map((k) => JSON.stringify(k) + ': ' + JSON.stringify(juntos[k])).join(',\n') + '\n}\n');

// catálogo para o banco (biblioteca.obras), idempotente
const linhas = dados.obras.slice().sort((a, b) => chaveObra(a).localeCompare(chaveObra(b)))
  .map((o) => `  (${sql(chaveObra(o))}, ${sql(o.titulo.length > 200 ? o.titulo.slice(0, 199).replace(/\s+\S*$/, '') + '…' : o.titulo)})`);  // o banco aceita até 200
function sql(s) { return "'" + String(s).replace(/'/g, "''") + "'"; }
fs.mkdirSync(path.dirname(ARQ_SQL), { recursive: true });
fs.writeFileSync(ARQ_SQL, `-- Catálogo da Biblioteca Taioé (biblioteca.obras). Gerado por ferramentas/site/gerar.mjs; não edite à mão.
-- Aplicado pelo workflow Catálogo do taioe-infra, primeiro no teste e depois na produção.
-- Obra que sai do site continua no catálogo: as posições de leitura guardadas dependem dela.
insert into biblioteca.obras (obra, titulo) values
${linhas.join(',\n')}
on conflict (obra) do update set titulo = excluded.titulo, atualizado_em = now()
  where biblioteca.obras.titulo is distinct from excluded.titulo;
`);

console.log(`${paginas} páginas, ${sitemap.length} no sitemap, ${dados.obras.length} obras, ${dados.autores.length} autores.`);
