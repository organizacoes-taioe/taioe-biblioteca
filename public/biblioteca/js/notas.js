/* Notas da Taioé: o mesmo arquivo na Bíblia (public/biblia/js/notas.js) e na Biblioteca
   (ferramentas/site/comum/notas.js, que o gerar.mjs copia para public/biblioteca/js/). O workflow
   Cópias dos dois repositórios confere o sha256, anotado no README do taioe-hub. Pedido do Gere,
   31/10/2026: as notas da Bíblia e as da Biblioteca têm sempre a mesma dinâmica.

   Duas marcas abrem nota:
   - a letra (a.nota-ref[data-nota]), cujo texto está na lista do fim da página (#nota-<letra>, com
     .nota-v e .nota-texto); sem JavaScript, a letra é um link para essa lista;
   - a palavra (button.pal[data-g]), cujo verbete o gerador deixa escondido em #g-<id>.
   A nota abre logo abaixo da linha da marca (acima, se embaixo não couber), na largura da coluna do
   texto, em qualquer tela. Fecha com qualquer toque (dentro dela também), ao rolar, ao arrastar,
   com Esc e tocando de novo na mesma marca; tocar noutra marca abre a outra. */
(function () {
  'use strict';
  var painel = null, ref = null, texto = null;
  var ativa = null, y0 = 0, largura0 = 0, x0 = null, yToque = null;

  function montar() {
    painel = document.getElementById('nota-painel');
    if (!painel) {
      painel = document.createElement('div');
      painel.className = 'nota-painel';
      painel.id = 'nota-painel';
      painel.setAttribute('role', 'dialog');
      painel.setAttribute('aria-modal', 'false');
      painel.hidden = true;
      var p = document.createElement('p');
      p.className = 'nota-painel-ref';
      p.id = 'nota-painel-ref';
      var t = document.createElement('div');
      t.className = 'nota-painel-texto';
      t.id = 'nota-painel-texto';
      painel.appendChild(p);
      painel.appendChild(t);
      document.body.appendChild(painel);
    }
    ref = document.getElementById('nota-painel-ref');
    texto = document.getElementById('nota-painel-texto');
  }

  function fechar(focar) {
    if (!painel || painel.hidden) return;
    painel.hidden = true;
    if (ativa) {
      ativa.classList.remove('ativa');
      if (ativa.hasAttribute('aria-expanded')) ativa.setAttribute('aria-expanded', 'false');
      if (focar) ativa.focus({ preventScroll: true });
      ativa = null;
    }
  }

  // A linha em que está a marca: os retângulos do texto que cobrem a altura dela.
  function linha(marca) {
    var m = marca.getBoundingClientRect(), meio = (m.top + m.bottom) / 2, cima = m.top, pe = 0;
    var bloco = marca.closest('.txt, .par, p, li, .orig, .trad') || marca.parentNode;
    var r = document.createRange();
    r.selectNodeContents(bloco);
    var rs = r.getClientRects();
    for (var i = 0; i < rs.length; i++) {
      if (rs[i].top <= meio && rs[i].bottom >= meio) {
        if (rs[i].bottom > pe) pe = rs[i].bottom;
        if (rs[i].top < cima) cima = rs[i].top;
      }
    }
    return { cima: cima, pe: pe || m.bottom + 6 };
  }

  function posicionar(marca) {
    var col = (marca.closest('.trad, .orig, .folha') || document.body).getBoundingClientRect();
    var margem = 8, alto = window.innerHeight, largo = document.documentElement.clientWidth;
    var barra = document.querySelector('.topo');
    var teto = barra ? Math.max(0, barra.getBoundingClientRect().bottom) : 0;
    var larg = Math.min(Math.max(col.width + 24, 320), largo - 2 * margem);
    // coluna estreita (o verso de um poema): a nota fica centrada nela
    var esq = col.width + 24 >= larg ? col.left - 12 : col.left + col.width / 2 - larg / 2;
    esq = Math.min(Math.max(margem, esq), largo - margem - larg);
    painel.style.left = esq + 'px';
    painel.style.width = larg + 'px';
    painel.style.maxHeight = (alto - teto - 2 * margem) + 'px';
    var h = painel.offsetHeight, l = linha(marca);
    var y = l.pe + 4;
    if (y + h > alto - margem) {
      // embaixo não cabe: acima da linha, se couber; senão, o pé da nota no pé da tela
      y = l.cima - 4 - h >= teto + margem ? l.cima - 4 - h : alto - margem - h;
    }
    painel.style.top = Math.max(teto + margem, y) + 'px';
  }

  function conteudo(marca) {
    if (marca.classList.contains('nota-ref')) {
      var li = document.getElementById('nota-' + marca.getAttribute('data-nota'));
      if (!li || !li.querySelector('.nota-texto')) return null;
      var v = li.querySelector('.nota-v');
      return { ref: 'Nota ' + marca.getAttribute('data-nota') + (v ? ' · ' + v.textContent : ''), no: li.querySelector('.nota-texto') };
    }
    var vb = document.getElementById('g-' + marca.getAttribute('data-g'));
    return vb ? { ref: '', no: vb } : null;
  }

  function abrir(marca) {
    var c = conteudo(marca);
    if (!c) return false;
    if (ativa === marca) { fechar(); return true; }
    if (!painel) montar();
    if (ativa) {
      ativa.classList.remove('ativa');
      if (ativa.hasAttribute('aria-expanded')) ativa.setAttribute('aria-expanded', 'false');
    }
    ativa = marca;
    marca.classList.add('ativa');
    if (marca.tagName === 'BUTTON') marca.setAttribute('aria-expanded', 'true');
    ref.textContent = c.ref;
    ref.hidden = !c.ref;
    painel.setAttribute('aria-label', c.ref || 'Nota sobre «' + marca.textContent + '»');
    texto.innerHTML = '';
    var copia = c.no.cloneNode(true);
    copia.removeAttribute('id');
    copia.hidden = false;
    texto.appendChild(copia);
    painel.hidden = false;
    posicionar(marca);
    y0 = window.scrollY; largura0 = window.innerWidth;
    return true;
  }

  document.addEventListener('click', function (e) {
    var marca = e.target.closest && e.target.closest('a.nota-ref[data-nota], button.pal[data-g]');
    if (marca) { if (abrir(marca)) e.preventDefault(); return; }
    fechar();
  });
  window.addEventListener('scroll', function () { if (painel && !painel.hidden && Math.abs(window.scrollY - y0) > 3) fechar(); }, { passive: true });
  window.addEventListener('resize', function () { if (painel && !painel.hidden && window.innerWidth !== largura0) fechar(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fechar(true); });
  // Arrastar (o dedo ou o mouse apertado) também fecha, mesmo quando a página não rola.
  document.addEventListener('pointerdown', function (e) { x0 = e.clientX; yToque = e.clientY; });
  document.addEventListener('pointermove', function (e) {
    if (x0 === null || !painel || painel.hidden || (e.pointerType === 'mouse' && !e.buttons)) return;
    if (Math.abs(e.clientX - x0) + Math.abs(e.clientY - yToque) > 10) { x0 = null; fechar(); }
  }, { passive: true });
  document.addEventListener('pointerup', function () { x0 = null; });
  document.addEventListener('pointercancel', function () { x0 = null; });
})();
