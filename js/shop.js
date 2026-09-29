(() => {
  const ala = document.body.dataset.ala;
  const catalogo = PRODUTOS[ala];
  const $ = (s, r = document) => r.querySelector(s);
  const brl = n => n.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
  const KEY = 'sacola-' + ala;

  const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch { return []; } };
  const persist = () => { try { localStorage.setItem(KEY, JSON.stringify(cart)); } catch {} };
  let cart = load().filter(i => catalogo.some(p => p.id === i.id));

  const byId = id => catalogo.find(p => p.id === id);
  const waLink = texto => `https://wa.me/${WHATSAPP[ala]}?text=${encodeURIComponent(texto)}`;
  const linha = (p, opt, qtd) =>
    `• ${qtd}x ${p.nome}${opt ? ` (${opt})` : ''}${p.preco ? ' — ' + brl(p.preco * qtd) : ' — sob consulta'}`;

  function mensagem(itens, nome) {
    const total = itens.reduce((s, i) => s + (byId(i.id).preco || 0) * i.qtd, 0);
    const consulta = itens.some(i => !byId(i.id).preco);
    return [
      `Olá! Quero fazer um pedido na ${NOMES[ala]}.`,
      nome && `Meu nome: ${nome}`,
      '',
      ...itens.map(i => linha(byId(i.id), i.opt, i.qtd)),
      '',
      total ? `Total (peças com preço): ${brl(total)}` : '',
      consulta ? 'Há peça sob consulta: pode me passar o orçamento?' : '',
      'Pode me passar as formas de pagamento, frete e prazo?'
    ].filter(l => l !== false && l !== undefined).join('\n').replace(/\n{3,}/g, '\n\n');
  }

  /* ---------- Catálogo + filtros ---------- */
  const grid = $('#produtos');
  const filtros = $('#filtros');
  const cats = ['Todos', ...new Set(catalogo.map(p => p.cat))];
  let filtro = 'Todos';

  function cardHTML(p) {
    const preco = p.preco ? `<p class="price">${brl(p.preco)}</p>` : `<p class="price"><small>Sob consulta</small></p>`;
    const acoes = p.preco
      ? `<button class="btn sm ghost" data-add="${p.id}">+ Sacola</button>
         <button class="btn sm wa" data-buy="${p.id}">Comprar</button>`
      : `<button class="btn sm wa" style="grid-column:1/-1" data-open="${p.id}">Consultar pelo WhatsApp</button>`;
    return `<article class="card">
      <button class="thumb" data-open="${p.id}" aria-label="Ver detalhes de ${p.nome}">
        <img src="img/${p.img}.webp" alt="${p.nome}" loading="lazy">
        ${p.badge ? `<span class="badge">${p.badge}</span>` : ''}
      </button>
      <div class="info"><span class="cat">${p.cat}</span><h3>${p.nome}</h3>${preco}</div>
      <div class="actions">${acoes}</div>
    </article>`;
  }

  function renderGrid() {
    const lista = catalogo.filter(p => filtro === 'Todos' || p.cat === filtro);
    grid.innerHTML = lista.length ? lista.map(cardHTML).join('') : '<p class="empty">Nenhuma peça nesta categoria.</p>';
  }
  function renderFiltros() {
    filtros.innerHTML = cats.map(c => `<button type="button" aria-pressed="${c === filtro}" data-cat="${c}">${c}</button>`).join('');
  }
  filtros.addEventListener('click', e => {
    const b = e.target.closest('[data-cat]'); if (!b) return;
    filtro = b.dataset.cat; renderFiltros(); renderGrid();
  });

  /* ---------- Sacola ---------- */
  const drawer = $('#sacola'), overlay = $('#overlay'), lista = $('#sacola-lista');
  const badge = $('#cart-count');

  function abrirSacola(on) {
    drawer.classList.toggle('on', on);
    overlay.classList.toggle('on', on);
    drawer.setAttribute('aria-hidden', String(!on));
    document.body.style.overflow = on ? 'hidden' : '';
    if (on) $('#sacola-fechar').focus();
  }

  function renderSacola() {
    const qtd = cart.reduce((s, i) => s + i.qtd, 0);
    badge.textContent = qtd; badge.hidden = !qtd;
    if (!cart.length) {
      lista.innerHTML = '<li class="empty" style="padding:24px 0">Sua sacola está vazia.</li>';
    } else {
      lista.innerHTML = cart.map((i, idx) => {
        const p = byId(i.id);
        return `<li class="line-item">
          <img src="img/${p.img}.webp" alt="">
          <div><strong>${p.nome}</strong>${i.opt ? `<small>${p.opcoes.label}: ${i.opt}</small>` : ''}
            <small>${brl(p.preco)}</small>
            <div class="qty"><button data-dec="${idx}" aria-label="Diminuir">−</button><span>${i.qtd}</span><button data-inc="${idx}" aria-label="Aumentar">+</button></div></div>
          <button class="rm" data-rm="${idx}">Remover</button>
        </li>`;
      }).join('');
    }
    const total = cart.reduce((s, i) => s + byId(i.id).preco * i.qtd, 0);
    $('#sacola-total').textContent = brl(total);
    $('#sacola-enviar').disabled = !cart.length;
    persist();
  }

  function adicionar(id, opt = '', qtd = 1) {
    const ex = cart.find(i => i.id === id && i.opt === opt);
    ex ? ex.qtd += qtd : cart.push({ id, opt, qtd });
    renderSacola();
  }

  lista.addEventListener('click', e => {
    const t = e.target, n = k => Number(t.dataset[k]);
    if (t.dataset.inc != null) cart[n('inc')].qtd++;
    else if (t.dataset.dec != null) { const i = cart[n('dec')]; i.qtd > 1 ? i.qtd-- : cart.splice(n('dec'), 1); }
    else if (t.dataset.rm != null) cart.splice(n('rm'), 1);
    else return;
    renderSacola();
  });

  $('#cart-open').addEventListener('click', () => abrirSacola(true));
  $('#sacola-fechar').addEventListener('click', () => abrirSacola(false));
  overlay.addEventListener('click', () => abrirSacola(false));
  $('#sacola-enviar').addEventListener('click', () => {
    if (!cart.length) return;
    window.open(waLink(mensagem(cart, $('#cliente-nome').value.trim())), '_blank', 'noopener');
  });

  /* ---------- Modal do produto ---------- */
  const dlg = $('#produto');
  function abrirProduto(id) {
    const p = byId(id);
    const opc = p.opcoes ? `<div><label class="l" for="pd-opt">${p.opcoes.label}</label>
      <select id="pd-opt">${p.opcoes.valores.map(v => `<option>${v}</option>`).join('')}</select></div>` : '';
    const spec = Object.entries(p.spec || {}).map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join('');
    const acoes = p.preco
      ? `<button class="btn ghost" id="pd-add">Adicionar à sacola</button><button class="btn wa" id="pd-buy">Comprar pelo WhatsApp</button>`
      : `<a class="btn wa" id="pd-ask" target="_blank" rel="noopener">Consultar pelo WhatsApp</a>`;
    dlg.innerHTML = `<div class="pd">
      <img src="img/${p.img}.webp" alt="${p.nome}">
      <div class="body">
        <button class="icon-btn close" aria-label="Fechar" id="pd-close"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
        <span class="eyebrow" style="margin:0">${p.cat}</span>
        <h2 style="margin:0">${p.nome}</h2>
        <p class="price" style="font-size:1.3rem;margin:0">${p.preco ? brl(p.preco) : 'Sob consulta'}</p>
        <p>${p.desc}</p>
        <dl class="spec">${spec}</dl>
        ${opc}
        <div class="actions">${acoes}</div>
        <p class="note">Pagamento e frete combinados pelo WhatsApp (Pix ou cartão).</p>
      </div></div>`;
    const opt = () => (p.opcoes ? $('#pd-opt', dlg).value : '');
    $('#pd-close', dlg).onclick = () => dlg.close();
    if (p.preco) {
      $('#pd-add', dlg).onclick = () => { adicionar(p.id, opt()); dlg.close(); abrirSacola(true); };
      $('#pd-buy', dlg).onclick = () => window.open(waLink(mensagem([{ id: p.id, opt: opt(), qtd: 1 }])), '_blank', 'noopener');
    } else {
      $('#pd-ask', dlg).href = waLink(`Olá! Quero um orçamento: ${p.nome} (${NOMES[ala]}).`);
    }
    dlg.showModal();
  }
  dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });

  /* ---------- Delegação nos cards ---------- */
  grid.addEventListener('click', e => {
    const b = e.target.closest('[data-open],[data-add],[data-buy]'); if (!b) return;
    const d = b.dataset;
    if (d.open) return abrirProduto(d.open);
    const p = byId(d.add || d.buy);
    if (p.opcoes) return abrirProduto(p.id);            // precisa escolher tamanho/aro primeiro
    if (d.add) { adicionar(p.id); abrirSacola(true); }
    else window.open(waLink(mensagem([{ id: p.id, opt: '', qtd: 1 }])), '_blank', 'noopener');
  });

  document.addEventListener('keydown', e => { if (e.key === 'Escape') abrirSacola(false); });

  /* ---------- Menu mobile ---------- */
  const nav = $('.nav'), tg = $('#menu-toggle');
  tg.addEventListener('click', () => { const on = nav.classList.toggle('open'); tg.setAttribute('aria-expanded', on); });
  nav.querySelectorAll('.menu a').forEach(a => a.addEventListener('click', () => { nav.classList.remove('open'); tg.setAttribute('aria-expanded', false); }));

  renderFiltros(); renderGrid(); renderSacola();
})();
