/* Biblioteca Taioé: o que o site estático faz no navegador (PLANO, etapa 4).
   - preferências (tema e tamanho da letra), original e tradução, setas do teclado;
   - posição de leitura: só neste navegador para quem não entrou; para quem entrou, também na
     conta, em qualquer aparelho (anexo banco.md, §2.7);
   - «Continuar a leitura» na capa e endereços antigos (#/o/<obra>/<n>) levados aos novos.
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
      titulo: D.tituloObra, rotulo: D.rotulo || '', url: location.pathname
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

  /* ---------------------------------------------------------------- sincronização (com conta) */
  var sync = { ativo: false, t: null, agendar: function () {} };
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
        return { obra: k, parte: x.parte, indice: x.i, paragrafo: x.par || 0, lida_em: new Date(x.t).toISOString(),
          max_parte: x.max || x.parte, max_indice: x.maxI || x.i, concluida: !!x.concluida };
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
        L[k] = r; mudou = true;
      });
      if (mudou) guardar(CHAVE_LEIT, JSON.stringify(L));
      return aviso;
    }

    /* puxa as leituras da conta e completa títulos e rótulos pelo índice das obras */
    var q = await sb.schema('biblioteca').from('leituras')
      .select('obra, parte, indice, paragrafo, lida_em, max_parte, max_indice, concluida');
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
