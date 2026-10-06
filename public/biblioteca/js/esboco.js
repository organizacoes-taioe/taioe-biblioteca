/* Esboço da etapa 3 (PdC 2): a Biblioteca abre sem login, e o leitor anônimo não baixa o
   supabase-js. Só com a sessão guardada a página carrega o SDK e mostra quem está conectado.
   Sai na etapa 4, quando a Biblioteca de verdade entrar. */
(function () {
  'use strict';
  var tem = false;
  try { tem = !!localStorage.getItem('taioe-auth'); } catch (e) {}
  if (!tem) return;

  function carregar(src) {
    return new Promise(function (ok, falha) {
      var s = document.createElement('script');
      s.src = src; s.onload = ok; s.onerror = falha;
      document.body.appendChild(s);
    });
  }
  carregar('./vendor/supabase-js-2.117.2.js')
    .then(function () { return carregar('./js/taioe-sessao.js'); })
    .then(async function () {
      TaioeSessao.aoSair(function () { location.reload(); });
      var r = await TaioeSessao.cliente().auth.getSession();
      var s = r.data && r.data.session;
      if (!s) return;
      var p = await TaioeSessao.cliente().schema('conta').from('perfis').select('nome').maybeSingle();
      var linha = document.getElementById('logado');
      linha.textContent = 'Conectado como ' + (p.data ? p.data.nome : s.user.email)
        + '. Suas posições de leitura ficam guardadas na conta.';
      linha.hidden = false;
      document.getElementById('anonimo').hidden = true;
    })
    .catch(function () { /* sem SDK, a leitura continua normal */ });
})();
