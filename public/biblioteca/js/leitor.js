/* Biblioteca Taioé: o que o site estático faz no navegador (PLANO, etapa 4).
   - preferências (tema e tamanho da letra), original e tradução, setas do teclado;
   - posição de leitura: só neste navegador para quem não entrou; para quem entrou, também na
     conta, em qualquer aparelho (anexo banco.md, §2.7);
   - «Continuar a leitura» na capa e endereços antigos (#/o/<obra>/<n>) levados aos novos;
   - o estado de leitura de cada parte e de cada obra (lendo, lida), com as marcas nas listas,
     a escolha manual, as páginas «Em leitura» e «Lidos», a ordem dos autores e a busca.
   O leitor anônimo não baixa o supabase-js: só com a sessão guardada (taioe-auth) a página carrega
   o SDK e o módulo de sessão. Tudo o que vem de fora entra com textContent. */
(function () {
  'use strict';
  var B = '/biblioteca/';
  var CHAVE_TEMA = 'biblioteca:tema', CHAVE_FONTE = 'biblioteca:fonte';
  var CHAVE_LEIT = 'biblioteca:leituras', CHAVE_PEND = 'biblioteca:pendentes';
  var corpo = document.body, D = corpo.dataset;

  function guardar(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* modo privado */ } }
  function ler(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lerJson(k, padrao) { try { return JSON.parse(ler(k)) || padrao; } catch (e) { return padrao; } }
  function $(id) { return document.getElementById(id); }

  /* ---------------------------------------------------------------- preferências */
  function aplicarTema(t) {
    if (t === 'claro' || t === 'escuro') document.documentElement.setAttribute('data-tema', t);
    else document.documentElement.removeAttribute('data-tema');
  }
  var TAMANHOS = [0.9, 1, 1.1, 1.22, 1.35];
  function aplicarFonte(k) { document.documentElement.style.setProperty('--escala', TAMANHOS[k]); }
  aplicarTema(ler(CHAVE_TEMA));
  var kf = parseInt(ler(CHAVE_FONTE), 10);
  if (!isNaN(kf) && TAMANHOS[kf]) aplicarFonte(kf);

  function alternarTema() {
    var atual = document.documentElement.getAttribute('data-tema');
    var escuroSistema = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    var novo = (atual ? atual === 'escuro' : escuroSistema) ? 'claro' : 'escuro';
    aplicarTema(novo);
    guardar(CHAVE_TEMA, novo);
  }
  function mudarFonte(delta) {
    var k = parseInt(ler(CHAVE_FONTE), 10);
    if (isNaN(k)) k = 1;
    k = Math.max(0, Math.min(TAMANHOS.length - 1, k + delta));
    aplicarFonte(k);
    guardar(CHAVE_FONTE, String(k));
  }
  ['fonte-menos', 'fonte-mais', 'tema'].forEach(function (id) { var b = $(id); if (b) b.hidden = false; });
  if ($('tema')) $('tema').addEventListener('click', alternarTema);
  if ($('fonte-menos')) $('fonte-menos').addEventListener('click', function () { mudarFonte(-1); });
  if ($('fonte-mais')) $('fonte-mais').addEventListener('click', function () { mudarFonte(1); });

  var barra = $('progresso');
  if (barra) {
    barra.hidden = false;
    barra.firstElementChild.style.width = (Math.max(0, Math.min(1, parseFloat(barra.getAttribute('data-frac')) || 0)) * 100).toFixed(2) + '%';
  }

  document.addEventListener('keydown', function (ev) {
    if (ev.altKey || ev.ctrlKey || ev.metaKey || ev.shiftKey) return;
    var alvo = ev.target;
    if (alvo && (alvo.isContentEditable || /^(INPUT|TEXTAREA|SELECT|BUTTON)$/.test(alvo.tagName))) return;
    var link = ev.key === 'ArrowLeft' ? document.querySelector('a[rel="prev"]') : ev.key === 'ArrowRight' ? document.querySelector('a[rel="next"]') : null;
    if (link) { ev.preventDefault(); location.href = link.getAttribute('href'); }
  });

  /* ---------------------------------------------------------------- original e tradução */
  /* Todo texto abre só em português; a escolha segue de parte em parte da mesma obra (vale
     quando se chega pela navegação da própria obra) e volta ao português ao reabrir o texto. */
  var art = document.querySelector('.bilingue');
  if (art && $('idiomas')) {
    var ESTREITO = window.matchMedia ? window.matchMedia('(max-width: 760px)') : { matches: false };
    var idiomas = { obra: D.obra, orig: false, trad: true, ultimo: 'trad' };
    try {
      var s = JSON.parse(sessionStorage.getItem('biblioteca:idiomas'));
      var veioDaObra = document.referrer && new URL(document.referrer).pathname.indexOf(D.urlObra) === 0;
      if (s && s.obra === D.obra && veioDaObra) idiomas = s;
    } catch (e) {}
    var verAtual = function () {
      if (idiomas.orig && idiomas.trad) return ESTREITO.matches ? idiomas.ultimo : 'ambos';
      return idiomas.orig ? 'orig' : 'trad';
    };
    var alturaTopo = function () { var t = document.querySelector('.topo'); return t ? t.getBoundingClientRect().bottom : 0; };
    var pegarAncora = function () {
      if (window.scrollY < 4) return null;
      var topo = alturaTopo(), cels = art.querySelectorAll('[data-i]');
      for (var j = 0; j < cels.length; j++) {
        if (!cels[j].offsetParent) continue;
        var r = cels[j].getBoundingClientRect();
        if (r.bottom > topo + 2) return { i: cels[j].getAttribute('data-i'), dy: r.top - topo };
      }
      return null;
    };
    var soltarAncora = function (a) {
      var cels = art.querySelectorAll('[data-i="' + a.i + '"]');
      for (var j = 0; j < cels.length; j++) {
        if (!cels[j].offsetParent) continue;
        window.scrollBy(0, cels[j].getBoundingClientRect().top - alturaTopo() - a.dy);
        return;
      }
    };
    var aplicarIdiomas = function (manter) {
      var ancora = manter ? pegarAncora() : null, v = verAtual();
      art.classList.remove('ver-orig', 'ver-trad', 'ver-ambos', 'ultimo-orig', 'ultimo-trad');
      art.classList.add(idiomas.orig && idiomas.trad ? 'ver-ambos' : 'ver-' + v, 'ultimo-' + idiomas.ultimo);
      Array.prototype.forEach.call(document.querySelectorAll('#idiomas [data-lado]'), function (b) {
        b.setAttribute('aria-pressed', String(v === 'ambos' || v === b.getAttribute('data-lado')));
      });
      if (ancora) soltarAncora(ancora);
      try { sessionStorage.setItem('biblioteca:idiomas', JSON.stringify(idiomas)); } catch (e) {}
    };
    var clicarIdioma = function (lado) {
      var v = verAtual(), outro = lado === 'orig' ? 'trad' : 'orig';
      if (ESTREITO.matches) { if (v === lado) return; idiomas[lado] = true; idiomas[outro] = false; }
      else if (v === 'ambos') idiomas[lado] = false;
      else if (v === lado) return;                      /* é o único ligado: fica */
      else idiomas[lado] = true;
      idiomas.ultimo = idiomas[lado] ? lado : outro;
      aplicarIdiomas(true);
    };
    Array.prototype.forEach.call(document.querySelectorAll('#idiomas [data-lado]'), function (b) {
      b.addEventListener('click', function () { clicarIdioma(b.getAttribute('data-lado')); });
    });
    var eraEstreito = ESTREITO.matches;
    var mudouLargura = function () { if (ESTREITO.matches === eraEstreito) return; eraEstreito = ESTREITO.matches; aplicarIdiomas(true); };
    if (ESTREITO.addEventListener) ESTREITO.addEventListener('change', mudouLargura);
    window.addEventListener('resize', mudouLargura);
    $('idiomas').hidden = false;
    aplicarIdiomas(false);
  }

  /* ---------------------------------------------------------------- posição de leitura */
  /* biblioteca:leituras = { "autor/obra": { parte, i, par, t, max, maxI, concluida, titulo, rotulo, url } }
     t = momento da leitura (ms); max/maxI = a parte mais adiantada lida; pendentes = obras a enviar */
  function leituras() { return lerJson(CHAVE_LEIT, {}); }
  function pendentes() { return lerJson(CHAVE_PEND, []); }
  function marcarPendente(obra) {
    var p = pendentes();
    if (p.indexOf(obra) < 0) { p.push(obra); guardar(CHAVE_PEND, JSON.stringify(p)); }
  }
  function urlDe(obra, parte, url) {
    if (url) return url;
    return parte === 'texto' ? B + obra + '/' : B + obra + '/' + parte + '/';
  }

  function paragrafoVisivel() {
    var cels = document.querySelectorAll('.leitura .texto [data-i], .leitura .texto > p');
    var topo = 80;
    for (var j = 0; j < cels.length; j++) {
      if (cels[j].getBoundingClientRect().bottom > topo) return Math.min(j, 32000);
    }
    return 0;
  }

  var contou = false;
  function registrarLeitura() {
    var L = leituras(), atual = L[D.obra] || {}, i = parseInt(D.indice, 10), total = parseInt(D.total, 10);
    var maisAdiante = !atual.maxI || i > atual.maxI;
    L[D.obra] = {
      parte: D.parte, i: i, par: paragrafoVisivel(), t: Date.now(),
      max: maisAdiante ? D.parte : atual.max, maxI: maisAdiante ? i : atual.maxI,
      concluida: !!atual.concluida || i === total,
      titulo: D.tituloObra, rotulo: D.rotulo || '', url: location.pathname,
      partes: atual.partes || {}
    };
    guardar(CHAVE_LEIT, JSON.stringify(L));
    marcarPendente(D.obra);
    contou = true;
    if (sync.ativo) sync.agendar(3000);
  }
  if (D.pagina === 'parte') {
    /* conta como leitura depois de 12 s na parte ou de alguma rolagem: espiar o índice não conta */
    var relogio = setTimeout(registrarLeitura, 12000);
    var aoRolar = function () {
      if (!contou) { clearTimeout(relogio); registrarLeitura(); return; }
      clearTimeout(aoRolar.t);
      aoRolar.t = setTimeout(function () {
        var L = leituras(), r = L[D.obra];
        if (!r || r.parte !== D.parte) return;
        r.par = paragrafoVisivel(); r.t = Date.now();
        guardar(CHAVE_LEIT, JSON.stringify(L));
        marcarPendente(D.obra);
        if (sync.ativo) sync.agendar(5000);
      }, 1200);
    };
    window.addEventListener('scroll', function () { if (window.scrollY > 40) aoRolar(); }, { passive: true });
  }

  function textoRetomar(r) {
    return r.titulo + (r.rotulo ? ' — ' + r.rotulo : '');
  }
  if (D.pagina === 'obra') {
    var r0 = leituras()[D.obra];
    if (r0 && r0.parte) {
      var b = $('comecar');
      if (b && (r0.i > 1 || r0.rotulo)) { b.textContent = 'Continuar: ' + (r0.rotulo || ('parte ' + r0.i)); b.href = urlDe(D.obra, r0.parte, r0.url); }
      var li = document.querySelector('.indice li[data-parte="' + r0.parte + '"]');
      if (li) li.classList.add('atual');
    }
  }
  function mostrarRetomar() {
    var caixa = $('retomar');
    if (!caixa) return;
    var L = leituras(), ultima = null;
    Object.keys(L).forEach(function (k) { if (L[k].t && (!ultima || L[k].t > ultima.r.t)) ultima = { k: k, r: L[k] }; });
    caixa.textContent = '';
    if (!ultima || !ultima.r.titulo) return;
    var a = document.createElement('a');
    a.className = 'retomar';
    a.href = urlDe(ultima.k, ultima.r.parte, ultima.r.url);
    var s1 = document.createElement('span'); s1.className = 'rot'; s1.textContent = 'Continuar a leitura';
    var s2 = document.createElement('span'); s2.className = 'alvo'; s2.textContent = textoRetomar(ultima.r);
    a.appendChild(s1); a.appendChild(s2);
    caixa.appendChild(a);
  }
  mostrarRetomar();

  /* índice compacto das obras (títulos e partes), baixado só quando preciso */
  var obrasJson = null;
  function indiceObras() {
    if (!obrasJson) obrasJson = fetch(B + 'obras.json').then(function (r) { return r.json(); }).catch(function () { return {}; });
    return obrasJson;
  }

  /* endereços do site antigo: #/o/<obra>/<n>, #/o/<obra>/sobre, #/a/<autor>..., #/s/<area> */
  if (D.pagina === 'capa' && /^#\/./.test(location.hash)) {
    var p = decodeURIComponent(location.hash.slice(2)).split('/').filter(Boolean);
    if (p[0] === 's' && p[1]) location.replace(B + p[1] + '/');
    else if (p[0] === 'a' && p[1]) location.replace(B + p.slice(1).join('/') + '/');
    else if (p[0] === 'o' && p[1]) {
      indiceObras().then(function (idx) {
        var chave = Object.keys(idx).filter(function (k) { return idx[k].i === p[1]; })[0];
        if (!chave) return;
        var o = idx[chave], destino = o.u;
        if (p[2] === 'sobre') destino = o.u + 'sobre/';
        else if (p[2] && o.p[parseInt(p[2], 10) - 1]) destino = urlDe(chave, o.p[parseInt(p[2], 10) - 1][0]);
        location.replace(destino);
      });
    }
  }

  /* ---------------------------------------------------------------- estado de leitura */
  /* r.partes = { "<parte>": [estado, t], "*": [estado, t] }: 0 não iniciada, 1 lendo (aberta),
     2 lida por inteiro (desceu até o fim); "*" é a escolha manual para a obra inteira. Parte a
     parte vale a marca mais recente (a mesma regra do servidor); sozinho, o aparelho só sobe. */
  function juntarPartes(a, b) {
    var saida = {};
    [a || {}, b || {}].forEach(function (m) {
      Object.keys(m).forEach(function (k) {
        var v = m[k], x = saida[k];
        if (!Array.isArray(v) || v.length !== 2) return;
        if (!x || v[1] > x[1] || (v[1] === x[1] && v[0] > x[0])) saida[k] = [v[0], v[1]];
      });
    });
    return saida;
  }
  function estadoParte(r, slug) { var v = r && r.partes && r.partes[slug]; return v ? v[0] : 0; }
  /* a obra: a escolha manual, se for mais nova que todas as marcas das partes; senão, lida com
     todas as partes lidas, lendo com pelo menos uma parte lida por inteiro */
  function estadoObra(r, n) {
    if (!r) return 0;
    var p = r.partes || {}, inteiras = 0, maisNova = 0, chaves = Object.keys(p);
    chaves.forEach(function (k) { if (k === '*') return; if (p[k][0] === 2) inteiras++; maisNova = Math.max(maisNova, p[k][1]); });
    if (p['*'] && p['*'][1] >= maisNova) return p['*'][0];
    if (n && inteiras >= n) return 2;
    if (inteiras > 0) return 1;
    if (r.concluida && !chaves.length) return 2;                  /* conclusão de antes das marcas */
    return 0;
  }
  /* começada: em leitura pela regra acima, ou com alguma parte aberta (e sem «não iniciada» depois) */
  function comecada(r, n) {
    var e = estadoObra(r, n);
    if (e !== 0) return e === 1;
    var p = (r && r.partes) || {}, m = p['*'];
    return Object.keys(p).some(function (k) { return k !== '*' && p[k][0] >= 1 && (!m || p[k][1] > m[1]); });
  }
  function recencia(r) {
    var t = r.t || 0, p = r.partes || {};
    Object.keys(p).forEach(function (k) { t = Math.max(t, p[k][1]); });
    return t;
  }
  /* grava uma marca; «manual» pode baixar, a automática só sobe */
  function marcar(obra, slugs, estado, manual, extra) {
    var L = leituras(), r = L[obra] || {}, t = Date.now(), mudou = false;
    r.partes = r.partes || {};
    slugs.forEach(function (k) {
      var atual = r.partes[k];
      if (!manual && atual && atual[0] >= estado) return;
      r.partes[k] = [estado, t]; mudou = true;
    });
    if (extra) Object.keys(extra).forEach(function (k) { if (r[k] === undefined || r[k] === null) r[k] = extra[k]; });
    if (!mudou && !extra) return;
    L[obra] = r;
    guardar(CHAVE_LEIT, JSON.stringify(L));
    marcarPendente(obra);
    if (sync && sync.ativo) sync.agendar(3000);              /* «sync» ainda não existe na abertura da página */
  }
  var ROTULOS = [['0', 'Não iniciada'], ['1', 'Lendo'], ['2', 'Lida']];
  function controleEstado(caixa, atual, aoEscolher) {
    caixa.textContent = '';
    var rot = document.createElement('span'); rot.className = 'rot'; rot.textContent = caixa.getAttribute('data-alvo') === 'obra' ? 'Esta obra:' : 'Esta parte:';
    caixa.appendChild(rot);
    ROTULOS.forEach(function (x) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = x[1];
      b.setAttribute('aria-pressed', String(String(atual) === x[0]));
      b.className = 'estado-' + x[0];
      b.addEventListener('click', function () { aoEscolher(+x[0]); });
      caixa.appendChild(b);
    });
    caixa.hidden = false;
  }
  function classeDe(e) { return e === 2 ? 'lido-inteiro' : e === 1 ? 'lido-parte' : ''; }
  function pintar(el, e) {
    el.classList.remove('lido-parte', 'lido-inteiro');
    if (classeDe(e)) el.classList.add(classeDe(e));
  }

  function pintarTudo() {
    var L = leituras();
    /* índice da obra: cada parte; e a escolha manual da obra */
    if (D.pagina === 'obra') {
      var lis = Array.prototype.slice.call(document.querySelectorAll('.indice li[data-parte]'));
      var slugs = lis.map(function (li) { return li.getAttribute('data-parte'); });
      lis.forEach(function (li) { pintar(li, estadoParte(L[D.obra], li.getAttribute('data-parte'))); });
      var cx = $('estado-leitura');
      if (cx) controleEstado(cx, estadoObra(L[D.obra], slugs.length), function (e) {
        var extra = slugs.length ? { parte: slugs[0], i: 1, max: slugs[0], maxI: 1, t: 1, titulo: D.tituloObra, rotulo: '' } : null;
        marcar(D.obra, ['*'], e, true, extra);
        if (e !== 1) marcar(D.obra, slugs, e, true);             /* lida ou não iniciada vale para todas as partes */
        pintarTudo();
      });
    }
    /* a parte aberta */
    if (D.pagina === 'parte') {
      var cp = $('estado-leitura');
      if (cp) controleEstado(cp, estadoParte(L[D.obra], D.parte), function (e) { marcar(D.obra, [D.parte], e, true); pintarTudo(); });
    }
    /* listas de obras e de poemas: precisam do número de partes de cada obra */
    var itens = document.querySelectorAll('li[data-obra], a[data-obra]');
    if (!itens.length || !Object.keys(L).length) return;
    indiceObras().then(function (idx) {
      var L2 = leituras();
      Array.prototype.forEach.call(itens, function (el) {
        var k = el.getAttribute('data-obra'), o = idx[k];
        pintar(el, o ? estadoObra(L2[k], o.p.length) : 0);
      });
    });
  }

  /* abrir a parte já é «lendo»; chegar ao fim do texto (depois de uns segundos na página) é «lida» */
  if (D.pagina === 'parte' && D.obra && D.parte) {
    marcar(D.obra, [D.parte], 1, false, { parte: D.parte, i: parseInt(D.indice, 10), max: D.parte, maxI: parseInt(D.indice, 10),
      t: Date.now(), titulo: D.tituloObra, rotulo: D.rotulo || '', url: location.pathname });
    var fim = $('fim-parte'), abertaEm = Date.now(), checar = null;
    if (fim) {
      var verFim = function () {
        if (Date.now() - abertaEm < 4000) return;
        if (fim.getBoundingClientRect().top > window.innerHeight) return;
        clearInterval(checar);
        window.removeEventListener('scroll', verFim);
        marcar(D.obra, [D.parte], 2, false);
        pintarTudo();
      };
      checar = setInterval(verFim, 1500);
      window.addEventListener('scroll', verFim, { passive: true });
    }
  }

  /* ---------------------------------------------------------------- ordem dos autores */
  var ordenar = $('ordenar'), listaAutores = $('lista-autores');
  if (ordenar && listaAutores) {
    var CHAVE_ORDEM = 'biblioteca:ordem-autores';
    var aplicarOrdem = function (modo) {
      var els = Array.prototype.slice.call(listaAutores.children);
      els.sort(function (a, b) {
        var x = +a.getAttribute('data-' + modo), y = +b.getAttribute('data-' + modo);
        return x - y || (+a.getAttribute('data-alfa')) - (+b.getAttribute('data-alfa'));
      });
      els.forEach(function (el) { listaAutores.appendChild(el); });
      Array.prototype.forEach.call(ordenar.querySelectorAll('button'), function (b) {
        b.setAttribute('aria-pressed', String(b.getAttribute('data-ordem') === modo));
      });
    };
    Array.prototype.forEach.call(ordenar.querySelectorAll('button'), function (b) {
      b.addEventListener('click', function () { var m = b.getAttribute('data-ordem'); aplicarOrdem(m); guardar(CHAVE_ORDEM, m); });
    });
    ordenar.hidden = false;
    var salva = ler(CHAVE_ORDEM);
    if (salva === 'nasc' || salva === 'morte') aplicarOrdem(salva);
  }

  /* ---------------------------------------------------------------- «Em leitura» e «Lidos» */
  function item(href, titulo, linha1, linha2) {
    var a = document.createElement('a'); a.className = 'cartao'; a.href = href;
    var t = document.createElement('span'); t.className = 'cartao-titulo'; t.textContent = titulo; a.appendChild(t);
    if (linha1) { var m = document.createElement('span'); m.className = 'cartao-meta'; m.textContent = linha1; a.appendChild(m); }
    if (linha2) { var x = document.createElement('span'); x.className = 'cartao-texto'; x.textContent = linha2; a.appendChild(x); }
    return a;
  }
  function montarListaLeitor() {
    var caixa = $('lista-leitor');
    if (!caixa) return;
    indiceObras().then(function (idx) {
      var L = leituras(), lidos = D.pagina === 'lidos';
      var ks = Object.keys(L).filter(function (k) {
        var o = idx[k]; if (!o) return false;
        return lidos ? estadoObra(L[k], o.p.length) === 2 : comecada(L[k], o.p.length);
      }).sort(function (a, b) { return recencia(L[b]) - recencia(L[a]); });
      caixa.textContent = '';
      if (!ks.length) {
        var vazio = document.createElement('p'); vazio.className = 'explica';
        vazio.textContent = lidos ? 'Nenhum livro lido por inteiro ainda. Quando você chega ao fim de todas as partes de um livro, ou o marca como lido, ele aparece aqui.'
          : 'Nenhum livro começado ainda. Abra uma parte de qualquer livro e ele aparece aqui.';
        caixa.appendChild(vazio);
        return;
      }
      ks.forEach(function (k) {
        var o = idx[k], r = L[k], n = o.p.length, inteiras = 0;
        o.p.forEach(function (x) { if (estadoParte(r, x[0]) === 2) inteiras++; });
        var par = r.parte && o.p.filter(function (x) { return x[0] === r.parte; })[0];
        var onde = lidos ? '' : (par && par[1] ? 'Parou em: ' + par[1] : '');
        var conta = n > 1 ? inteiras + ' de ' + n + ' partes lidas' : '';
        var href = lidos || !r.parte ? o.u : urlDe(k, r.parte, r.url);
        caixa.appendChild(item(href, o.t, o.a, [onde, conta].filter(Boolean).join(' · ')));
      });
    });
  }
  if (D.pagina === 'lendo' || D.pagina === 'lidos') montarListaLeitor();

  /* ---------------------------------------------------------------- busca */
  function normal(t) {
    return String(t).toLowerCase().replace(/ß/g, 'ss').replace(/æ/g, 'ae').replace(/œ/g, 'oe')
      .normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  }
  /* o texto normalizado e, para cada caractere dele, a posição no original (para destacar) */
  function mapaNormal(t) {
    var n = '', pos = [];
    for (var i = 0; i < t.length; i++) { var c = normal(t[i]); for (var j = 0; j < c.length; j++) { n += c[j]; pos.push(i); } }
    return { n: n, pos: pos };
  }
  var STOP = {};
  ('de da do das dos a o as os e e em um uma uns umas no na nos nas ao aos a as que se por para com nao mas ou como mais ' +
   'lhe lhes me te vos seu sua seus suas meu minha meus minhas teu tua ele ela eles elas eu tu isso isto este esta estes ' +
   'estas esse essa esses essas aquele aquela era foi ser ha ja so the and of to in that is it le la les et des un une du ' +
   'en est qui der die das und den dem ist ein eine nicht zu mit sich non ad cum').split(' ').forEach(function (w) { STOP[w] = 1; });

  var formBusca = $('busca');
  if (formBusca) {
    var campo = $('busca-q'), saida = $('busca-resultados'), modo = 'titulos', ultima = 0;
    var cache = {}, titulosJson = null, docsJson = null;
    var pegar = function (url) {
      if (!cache[url]) cache[url] = fetch(url).then(function (r) { if (!r.ok) throw r.status; return r.json(); }).catch(function () { return null; });
      return cache[url];
    };
    var linha = function (txt, cls) { var p = document.createElement('p'); p.className = cls || 'explica'; p.textContent = txt; return p; };

    var buscarTitulos = function (q, vez) {
      if (!titulosJson) titulosJson = pegar(B + 'busca/titulos.json');
      return titulosJson.then(function (lista) {
        if (vez !== ultima || !lista) return;
        var nq = normal(q), comeco = [], meio = [];
        lista.forEach(function (x) {
          var nomes = [x[0], x[1]].concat(x[4] ? [x[4]] : []).map(normal);
          if (nomes.some(function (s) { return s.indexOf(nq) === 0; })) comeco.push(x);
          else if (nomes.some(function (s) { return s.indexOf(nq) > 0; })) meio.push(x);
        });
        var porNome = function (a, b) { return (a[3] === 'autor' ? 0 : 1) - (b[3] === 'autor' ? 0 : 1) || a[0].localeCompare(b[0], 'pt'); };
        var todos = comeco.sort(porNome).concat(meio.sort(porNome));
        saida.textContent = '';
        if (!todos.length) { saida.appendChild(linha('Nada com «' + q + '» no título nem no nome do autor. Experimente buscar dentro dos textos.')); return; }
        saida.appendChild(linha(todos.length + (todos.length === 1 ? ' resultado' : ' resultados') + (todos.length > 120 ? ' (mostrando os 120 primeiros)' : ''), 'contagem'));
        todos.slice(0, 120).forEach(function (x) {
          var tipo = x[3] === 'autor' ? 'Autor' : x[3] === 'poema' ? 'Poema' : 'Obra';
          saida.appendChild(item(x[2], x[0], [tipo, x[1]].filter(Boolean).join(' · '), x[4] && x[4] !== x[0] ? x[4] : ''));
        });
      });
    };

    var lerLista = function (s) {
      var ids = [], v = 0;
      s.split(',').forEach(function (p) { v += parseInt(p, 36); ids.push(v); });
      return ids;
    };
    var buscarTextos = function (q, vez) {
      var palavras = (normal(q).match(/[a-z0-9]+/g) || []).filter(function (w) { return w.length >= 2 && !STOP[w]; });
      if (!palavras.length) { saida.textContent = ''; saida.appendChild(linha('Use ao menos uma palavra de duas letras que não seja das mais comuns (de, que, para…).')); return Promise.resolve(); }
      if (!docsJson) docsJson = pegar(B + 'busca/docs.json');
      var ultimaPalavra = palavras.length - 1;
      return Promise.all([docsJson, pegar(B + 'obras.json')].concat(palavras.map(function (w, i) {
        return pegar(B + 'busca/i/' + w.slice(0, 2) + '.json').then(function (m) {
          if (!m) return [];
          if (m[w]) return lerLista(m[w]);
          /* a última palavra vale também como começo de palavra: «capit» acha «capitu» */
          if (i !== ultimaPalavra || w.length < 3) return [];
          var junto = {};
          Object.keys(m).forEach(function (k) { if (k.indexOf(w) === 0) lerLista(m[k]).forEach(function (d) { junto[d] = 1; }); });
          return Object.keys(junto).map(Number);
        });
      }))).then(function (res) {
        if (vez !== ultima) return;
        var docs = res[0], idx = res[1], listas = res.slice(2);
        saida.textContent = '';
        if (!docs || !idx) { saida.appendChild(linha('Não consegui carregar o índice da busca. Confira a conexão.')); return; }
        listas.sort(function (a, b) { return a.length - b.length; });
        var achados = listas[0].filter(function (d) { return listas.every(function (l) { return l.indexOf(d) >= 0; }); });
        if (!achados.length) { saida.appendChild(linha('Nenhum texto tem ' + (palavras.length > 1 ? 'todas estas palavras' : '«' + q + '»') + '.')); return; }
        saida.appendChild(linha(achados.length + (achados.length === 1 ? ' trecho' : ' trechos') + ' com ' + (palavras.length > 1 ? 'todas as palavras' : '«' + q + '»') +
          (achados.length > 60 ? ' (mostrando os 60 primeiros)' : ''), 'contagem'));
        achados.slice(0, 60).forEach(function (d, n) {
          var par = docs.d[d], k = docs.o[par[0]], o = idx[k];
          if (!o) return;
          var p = o.p[par[1]], href = p[0] === 'texto' ? o.u : o.u + p[0] + '/';
          var el = item(href, o.t + (p[1] ? ' — ' + p[1] : ''), o.a, '');
          saida.appendChild(el);
          if (n < 12) trecho(el, href, palavras, vez, normal(q).replace(/[^a-z0-9]+/g, ' ').trim());
        });
      });
    };
    /* o trecho, tirado da própria página (só nos primeiros resultados): o parágrafo com a frase
       exata, ou com mais palavras da busca; todas as palavras destacadas */
    var trecho = function (el, href, palavras, vez, frase) {
      fetch(href).then(function (r) { return r.text(); }).then(function (html) {
        if (vez !== ultima) return;
        var doc = new DOMParser().parseFromString(html, 'text/html');
        var ps = doc.querySelectorAll('.leitura .texto p, .leitura .texto .trad, .leitura .texto .orig');
        var melhor = null;
        for (var i = 0; i < ps.length; i++) {
          var t = ps[i].textContent.replace(/\s+/g, ' ').trim(), m = mapaNormal(t), achou = [], nota = 0;
          palavras.forEach(function (w) {
            var re = new RegExp('(^|[^a-z0-9])(' + w + ')', 'g'), x, uma = false;
            while ((x = re.exec(m.n))) { achou.push([x.index + x[1].length, w.length]); uma = true; }
            if (uma) nota++;
          });
          if (frase && m.n.indexOf(frase) >= 0) nota += 10;
          if (nota && (!melhor || nota > melhor.nota)) melhor = { t: t, m: m, achou: achou, nota: nota };
        }
        if (!melhor) return;
        var t2 = melhor.t, pos = melhor.m.pos, ac = melhor.achou.sort(function (a, b) { return a[0] - b[0]; });
        var centro = pos[ac[0][0]], de = Math.max(0, centro - 90), ate = Math.min(t2.length, centro + 200);
        var s2 = document.createElement('span'), cursor = de;
        s2.className = 'cartao-texto';
        if (de > 0) s2.appendChild(document.createTextNode('…'));
        ac.forEach(function (a) {
          var ini = pos[a[0]], fimP = pos[Math.min(pos.length - 1, a[0] + a[1] - 1)] + 1;
          if (ini < cursor || fimP > ate) return;
          s2.appendChild(document.createTextNode(t2.slice(cursor, ini)));
          var mk = document.createElement('mark'); mk.textContent = t2.slice(ini, fimP); s2.appendChild(mk);
          cursor = fimP;
        });
        s2.appendChild(document.createTextNode(t2.slice(cursor, ate) + (ate < t2.length ? '…' : '')));
        el.appendChild(s2);
      }).catch(function () {});
    };

    var buscar = function () {
      var q = campo.value.trim(), vez = ++ultima;
      try { history.replaceState(null, '', q ? '?q=' + encodeURIComponent(q) + (modo === 'textos' ? '&em=textos' : '') : location.pathname); } catch (e) {}
      if (q.length < 2) { saida.textContent = ''; return; }
      saida.textContent = '';
      saida.appendChild(linha('Buscando…'));
      (modo === 'titulos' ? buscarTitulos : buscarTextos)(q, vez);
    };
    var espera = null;
    campo.addEventListener('input', function () { clearTimeout(espera); espera = setTimeout(buscar, modo === 'titulos' ? 120 : 350); });
    formBusca.addEventListener('submit', function (ev) { ev.preventDefault(); buscar(); });
    Array.prototype.forEach.call(document.querySelectorAll('.modos [data-modo]'), function (b) {
      b.addEventListener('click', function () {
        modo = b.getAttribute('data-modo');
        Array.prototype.forEach.call(document.querySelectorAll('.modos [data-modo]'), function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        buscar(); campo.focus();
      });
    });
    var params = new URLSearchParams(location.search);
    if (params.get('em') === 'textos') {
      modo = 'textos';
      Array.prototype.forEach.call(document.querySelectorAll('.modos [data-modo]'), function (x) { x.setAttribute('aria-pressed', String(x.getAttribute('data-modo') === 'textos')); });
    }
    if (params.get('q')) { campo.value = params.get('q'); buscar(); }
    campo.focus();
  }

  /* ---------------------------------------------------------------- sincronização (com conta) */
  var sync = { ativo: false, t: null, agendar: function () {} };
  pintarTudo();
  var temSessao = !!ler('taioe-auth');
  if (!temSessao) return;

  function carregar(src) {
    return new Promise(function (ok, falha) {
      var s = document.createElement('script');
      s.src = src; s.onload = ok; s.onerror = falha;
      document.head.appendChild(s);
    });
  }

  carregar(B + 'vendor/supabase-js-2.117.2.js')
    .then(function () { return carregar(B + 'js/taioe-sessao.js'); })
    .then(iniciarSync)
    .catch(function () { /* sem SDK, a leitura continua só neste navegador */ });

  async function iniciarSync() {
    var sb = TaioeSessao.cliente();
    var r = await sb.auth.getSession(), sessao = r.data && r.data.session;
    if (!sessao) return;
    var uid = sessao.user.id, email = sessao.user.email;
    if ($('aviso-conta')) $('aviso-conta').hidden = true;
    TaioeSessao.aoSair(function () { sync.ativo = false; if ($('aviso-conta')) $('aviso-conta').hidden = false; });

    /* primeira vez nesta conta, neste aparelho: perguntar antes de enviar o que já está aqui
       (defesa contra login CSRF: o link de outra pessoa não leva as leituras desta) */
    var CHAVE_CONTA = 'biblioteca:conta:' + uid;
    if (!ler(CHAVE_CONTA)) {
      var locais = Object.keys(leituras());
      if (!locais.length) guardar(CHAVE_CONTA, 'ok');
      else {
        var resp = await perguntarEnvio(email, locais.length);
        if (resp) { locais.forEach(marcarPendente); guardar(CHAVE_CONTA, 'enviado'); }
        else { guardar(CHAVE_PEND, '[]'); guardar(CHAVE_CONTA, 'recusado'); }
      }
    }

    sync.ativo = true;
    sync.agendar = function (ms) { clearTimeout(sync.t); sync.t = setTimeout(enviar, ms || 3000); };

    function lote() {
      var L = leituras();
      return pendentes().map(function (k) {
        var x = L[k];
        if (!x || !x.parte) return null;
        return { obra: k, parte: x.parte, indice: x.i, paragrafo: x.par || 0, lida_em: new Date(x.t || 1).toISOString(),
          max_parte: x.max || x.parte, max_indice: x.maxI || x.i, concluida: !!x.concluida, partes: x.partes || {} };
      }).filter(Boolean).slice(0, 100);
    }
    /* A fila local é a fonte da verdade até a resposta chegar: o que não for enviado agora
       (sem rede, aba fechada no meio) vai na próxima vez. */
    var enviando = false;
    async function enviar() {
      if (!sync.ativo || enviando) return;
      var itens = lote();
      if (!itens.length) return;
      enviando = true;
      try {
        var resp = await sb.schema('biblioteca').rpc('registrar_leituras', { lote: itens });
        if (resp.error) {
          if (resp.status === 403) { sync.ativo = false; return; }       /* sem cadastro: fica só local */
          sync.agendar(60000);
          return;
        }
        var enviados = itens.map(function (x) { return x.obra; });
        guardar(CHAVE_PEND, JSON.stringify(pendentes().filter(function (k) { return enviados.indexOf(k) < 0; })));
        adotar(resp.data, false);
      } catch (e) { sync.agendar(60000); }
      finally { enviando = false; }
    }

    /* junta o que veio do servidor: posição pela leitura mais recente; máximo e conclusão só sobem */
    function adotar(linhas, avisar) {
      var L = leituras(), mudou = false, aviso = null;
      (linhas || []).forEach(function (s) {
        var k = s.obra, local = L[k], t = Date.parse(s.lida_em);
        var r = local || {};
        if (!local || t > (local.t || 0)) {
          if (avisar && k === D.obra && D.pagina && local && s.parte !== (D.parte || r.parte)) aviso = s;
          if (!(k === D.obra && D.pagina === 'parte' && contou)) {
            r.parte = s.parte; r.i = s.indice; r.par = s.paragrafo; r.t = t; r.url = null;
            r.rotulo = null;
          }
        }
        if (!r.maxI || s.max_indice > r.maxI) { r.max = s.max_parte; r.maxI = s.max_indice; }
        r.concluida = !!r.concluida || !!s.concluida;
        r.partes = juntarPartes(r.partes, s.partes);
        L[k] = r; mudou = true;
      });
      if (mudou) guardar(CHAVE_LEIT, JSON.stringify(L));
      return aviso;
    }

    /* puxa as leituras da conta e completa títulos e rótulos pelo índice das obras */
    var q = await sb.schema('biblioteca').from('leituras')
      .select('obra, parte, indice, paragrafo, lida_em, max_parte, max_indice, concluida, partes');
    if (!q.error) {
      var aviso = adotar(q.data, true);
      var idx = await indiceObras(), L = leituras(), mudou = false;
      Object.keys(L).forEach(function (k) {
        var o = idx[k], x = L[k];
        if (!o || !x.parte) return;
        if (!x.titulo) { x.titulo = o.t; mudou = true; }
        if (x.rotulo === null || x.rotulo === undefined) {
          var par = o.p.filter(function (y) { return y[0] === x.parte; })[0];
          x.rotulo = par ? par[1] : ''; mudou = true;
        }
      });
      if (mudou) guardar(CHAVE_LEIT, JSON.stringify(L));
      mostrarRetomar();
      pintarTudo();
      if (aviso && $('aviso-outro')) {
        var o = idx[aviso.obra], par = o && o.p.filter(function (y) { return y[0] === aviso.parte; })[0];
        var rot = par && par[1] ? par[1] : 'parte ' + aviso.indice;
        var caixa = $('aviso-outro');
        caixa.textContent = 'Em outro aparelho, você parou em: ' + rot + '. ';
        var ir = document.createElement('a');
        ir.href = urlDe(aviso.obra, aviso.parte);
        ir.textContent = 'Ir para lá';
        caixa.appendChild(ir);
        caixa.hidden = false;
      }
    }

    if (pendentes().length) sync.agendar(1500);
    setInterval(function () { if (pendentes().length) enviar(); }, 60000);
    document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') enviar(); });
  }

  function perguntarEnvio(email, n) {
    return new Promise(function (ok) {
      var caixa = document.createElement('div');
      caixa.className = 'pergunta-envio';
      caixa.setAttribute('role', 'dialog');
      caixa.setAttribute('aria-label', 'Enviar as leituras deste aparelho');
      var p = document.createElement('p');
      p.textContent = 'Enviar as leituras deste aparelho (' + n + (n === 1 ? ' obra' : ' obras') + ') para a conta ' + email + '?';
      var sim = document.createElement('button'); sim.type = 'button'; sim.textContent = 'Enviar';
      var nao = document.createElement('button'); nao.type = 'button'; nao.className = 'secundario'; nao.textContent = 'Não enviar';
      sim.addEventListener('click', function () { caixa.remove(); ok(true); });
      nao.addEventListener('click', function () { caixa.remove(); ok(false); });
      caixa.appendChild(p); caixa.appendChild(sim); caixa.appendChild(nao);
      var app = $('app');
      app.insertBefore(caixa, app.firstChild);
    });
  }
})();
