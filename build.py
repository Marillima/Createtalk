"""Gera ceramica.html e prata.html a partir de um único template. Rode: python build.py"""
WA_ICON = ('<a class="wa-float" data-wa="{a}" aria-label="Falar no WhatsApp" target="_blank" rel="noopener">'
           '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.1-1.3A10 10 0 1 0 12 2zm4.9 14c-.2.6-1.2 1.1-1.7 1.2'
           '-.4.1-1 .1-3.1-.7-2.6-1.1-4.2-3.7-4.4-3.9-.1-.2-1-1.3-1-2.5s.6-1.8.9-2c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5'
           'l-.4.6c-.1.2-.3.3-.1.6.2.3.8 1.2 1.6 1.9 1.1.9 2 1.2 2.3 1.3.3.1.4.1.6-.1l.7-.9c.2-.2.4-.2.6-.1l1.9.9c.3.1.4.2.5.3.1.2.1.7-.1 1.3z"/></svg></a>')


def page(a):
    c = a == 'ceramica'
    nome = 'CREATE Ceramic Studio' if c else 'Alquimista Dourado'
    outra = 'prata.html' if c else 'ceramica.html'
    outran = 'Alquimista Dourado' if c else 'CREATE Ceramic Studio'
    logo = ('<img src="img/create-logo.webp" alt="CREATE Talk Ceramic Studio">' if c
            else '<img src="img/sol-logo.webp" alt=""><span>Alquimista Dourado</span>')
    title = ('CREATE Ceramic Studio · Cerâmica artesanal' if c
             else 'Alquimista Dourado · Joias esculpidas em prata e ouro')
    desc = ('Canecas, vasos e potes de cerâmica feitos à mão. Peça pelo WhatsApp.' if c
            else 'Joias autorais em prata e ouro. Coleção Ritual e alianças sob encomenda. Peça pelo WhatsApp.')
    eyebrow = 'Cerâmica artesanal' if c else 'Coleção Ritual'
    h1 = 'Barro que vira memória.' if c else 'Alquimista Dourado'
    lead = ('Peças de uso diário e sob encomenda, modeladas e queimadas à mão. Cada uma sai única do forno.' if c
            else 'Joias esculpidas à mão em prata e ouro. Formas orgânicas, símbolos ancestrais e acabamento polido ou oxidado.')
    hero = (('vaso-noite', 'Pratos de cerâmica com esmalte verde musgo') if c
            else ('anel-livro', 'Anel de prata sobre livro aberto, entre folhas de jiboia'))
    menu = ('<a href="#colecao">Peças</a>' if c else '<a href="#colecao">Coleção</a><a href="#aliancas">Alianças</a>')
    menu += '<a href="#como">Como comprar</a><a href="#encomenda">Encomenda</a><a href="#faq">Dúvidas</a>'
    perks = (['Feito à mão|Cada peça é única', 'Envio para todo o Brasil|Embalagem segura',
              'Pix ou cartão|Combinado no WhatsApp', 'Atendimento direto|Resposta rápida'] if c else
             ['Feito à mão|Prata 950 e ouro 18k', 'Envio para todo o Brasil|Embalagem para presente',
              'Pix ou cartão|Combinado no WhatsApp', 'Peças sob medida|Alianças e encomendas'])
    perks_html = ''.join('<li><b>%s</b>%s</li>' % tuple(x.split('|')) for x in perks)

    if c:
        story = '''<section class="band"><div class="wrap story">
  <div><p class="eyebrow">O ateliê</p><h2>Matéria viva, feita com as mãos.</h2>
  <p>Cada peça nasce do barro, passa pelo torno, pelo esmalte e pelo fogo. Nada é produzido em série: a marca do gesto fica na superfície.</p></div>
  <img src="img/torno.webp" alt="Mãos modelando uma peça de cerâmica no torno" loading="lazy">
</div></section>'''
        alianca = ''
        chips = [('peca', 'Tipo de peça', ['Caneca', 'Vaso', 'Pote / tigela', 'Outro']),
                 ('ocasiao', 'Ocasião', ['Presente', 'Casa / decoração', 'Evento']),
                 ('faixa', 'Faixa de investimento', ['Até R$ 300', 'R$ 300 – 700', 'Acima de R$ 700', 'Ainda a definir'])]
        tam = ('Tamanho (opcional)', 'Ex.: 12cm de altura')
        ph = 'Cores, texturas, história por trás da peça…'
        ig = '@seuperfil'
    else:
        story = '''<section class="band"><div class="wrap story">
  <div><p class="eyebrow">Quem faz</p><h2>Uma busca pela matéria-prima viva.</h2>
  <p>Cada joia nasce do desenho, passa pela serra de ourives e ganha forma no fogo. Nada é produzido em série: o metal guarda o gesto de quem o trabalhou.</p></div>
  <img src="img/serra.webp" alt="Serra de ourives sobre bancada de madeira" loading="lazy">
</div></section>'''
        alianca = '''<section id="aliancas" class="band"><div class="wrap story rev">
  <div><p class="eyebrow">Ouro 18k</p><h2>Alianças personalizadas</h2>
  <p>Desenhadas e trabalhadas para casamentos e rituais de compromisso. Cada par é único e feito sob consulta.</p>
  <div class="actions" style="margin-top:1.4rem"><a class="btn" href="#encomenda">Consultar alianças</a></div></div>
  <img src="img/aliancas.webp" alt="Par de alianças de ouro sobre carta manuscrita" loading="lazy">
</div></section>'''
        chips = [('peca', 'Tipo de peça', ['Anel', 'Colar / pingente', 'Brinco', 'Alianças']),
                 ('ocasiao', 'Ocasião', ['Presente', 'Casamento / noivado', 'Autopresente', 'Memória afetiva']),
                 ('faixa', 'Faixa de investimento', ['Até R$ 500', 'R$ 500 – 1.500', 'Acima de R$ 1.500', 'Ainda a definir'])]
        tam = ('Tamanho / aro (opcional)', 'Ex.: aro 14')
        ph = 'Símbolos, texturas, a história por trás da joia…'
        ig = '@alquimista.dourado'

    fs = ''.join(
        '<fieldset><legend>%s</legend><div class="chips">%s</div></fieldset>' % (
            l, ''.join('<label><input type="radio" name="%s" value="%s"><span>%s</span></label>' % (n, v, v) for v in vs))
        for n, l, vs in chips)
    faq = [('Como funciona a compra?', 'Você escolhe as peças, monta a sacola e envia o pedido pelo WhatsApp. Confirmamos disponibilidade, frete e forma de pagamento com você.'),
           ('Quais as formas de pagamento?', 'Pix e cartão de crédito (com link de pagamento), combinados na conversa.'),
           ('Como é o envio?', 'Enviamos para todo o Brasil com embalagem segura. Prazo e frete são calculados pelo seu CEP.'),
           ('Posso encomendar uma peça personalizada?', 'Sim. Use o formulário de encomenda: retornamos com orçamento e prazo.')]
    faq_html = ''.join('<details><summary>%s</summary><p>%s</p></details>' % f for f in faq)
    sec_eyebrow = 'Vitrine' if c else 'Prata e ouro'
    sec_h2 = 'Peças em destaque' if c else 'Joias esculpidas com a imperfeição da natureza'

    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="css/base.css"><link rel="stylesheet" href="css/{a}.css">
</head>
<body data-ala="{a}">
<div class="topbar">Envio para todo o Brasil · Pedido finalizado pelo WhatsApp</div>
<header class="nav"><div class="wrap">
  <a class="brand" href="{a}.html" aria-label="{nome}">{logo}</a>
  <nav class="menu" id="menu" aria-label="Principal">{menu}<a href="{outra}">{outran} ↗</a></nav>
  <div class="tools">
    <button class="icon-btn" id="cart-open" aria-label="Abrir sacola"><svg viewBox="0 0 24 24"><path d="M5 8h14l-1 12H6L5 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg><span class="count" id="cart-count" hidden>0</span></button>
    <button class="icon-btn" id="menu-toggle" aria-label="Menu" aria-expanded="false" aria-controls="menu"><svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  </div>
</div></header>
<main>
<section class="hero"><div class="wrap row">
  <div>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="actions"><a class="btn" href="#colecao">Ver peças</a><a class="btn ghost" href="#encomenda">Encomenda personalizada</a></div>
  </div>
  <img src="img/{hero[0]}.webp" alt="{hero[1]}" fetchpriority="high">
</div></section>

<section class="perks" aria-label="Diferenciais"><div class="wrap"><ul>{perks_html}</ul></div></section>

<section id="colecao"><div class="wrap">
  <div class="cat-head">
    <div><p class="eyebrow">{sec_eyebrow}</p><h2>{sec_h2}</h2></div>
    <div class="filters" id="filtros" role="group" aria-label="Filtrar por categoria"></div>
  </div>
  <div class="products" id="produtos" aria-live="polite"></div>
</div></section>

{story}
{alianca}
<section id="como"><div class="wrap">
  <p class="eyebrow">Compra simples</p><h2>Como comprar pelo WhatsApp</h2>
  <ol class="steps">
    <li><b>Escolha</b>Navegue pelas peças e adicione à sacola.</li>
    <li><b>Envie o pedido</b>Um clique abre a conversa com o pedido pronto.</li>
    <li><b>Combine</b>Confirmamos estoque, frete e pagamento (Pix ou cartão).</li>
    <li><b>Receba</b>Embalamos com cuidado e enviamos para você.</li>
  </ol>
</div></section>

<section id="encomenda" class="band"><div class="wrap">
  <p class="eyebrow">Encomenda personalizada</p><h2>Conte sua ideia.</h2>
  <p class="lead" style="margin-bottom:1.6rem">Quanto mais contexto, mais próximo o resultado fica do que você imagina.</p>
  <form class="brief" id="brief" data-ala="{a}">
    {fs}
    <div class="two">
      <div><label class="l" for="t">{tam[0]}</label><input id="t" type="text" name="tamanho" placeholder="{tam[1]}"></div>
      <div><label class="l" for="pz">Prazo (opcional)</label><input id="pz" type="text" name="prazo" placeholder="Ex.: até 30/11"></div></div>
    <div><label class="l" for="i">Sua ideia</label><textarea id="i" name="ideia" placeholder="{ph}"></textarea></div>
    <div class="actions"><button class="btn wa" type="submit">Enviar pelo WhatsApp</button></div>
  </form>
</div></section>

<section id="faq"><div class="wrap">
  <p class="eyebrow">Dúvidas</p><h2>Perguntas frequentes</h2>
  <div class="faq">{faq_html}</div>
</div></section>
</main>

<footer class="site"><div class="wrap">
  <div class="cols">
    <div><h3>{nome}</h3><p>Peças feitas à mão, uma de cada vez.</p></div>
    <div><h3>Navegue</h3><ul><li><a href="#colecao">Peças</a></li><li><a href="#encomenda">Encomenda</a></li><li><a href="#faq">Dúvidas</a></li><li><a href="{outra}">{outran}</a></li></ul></div>
    <div><h3>Contato</h3><ul><li><a href="#" data-wa="{a}">WhatsApp</a></li><li>Instagram {ig}</li></ul></div>
  </div>
  <p class="copy">© {nome}. Todos os direitos reservados.</p>
</div></footer>

<div class="overlay" id="overlay"></div>
<aside class="drawer" id="sacola" aria-hidden="true" aria-label="Sacola">
  <header><h3>Sua sacola</h3><button class="icon-btn" id="sacola-fechar" aria-label="Fechar sacola"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button></header>
  <ul class="list" id="sacola-lista"></ul>
  <footer>
    <div><label class="l" for="cliente-nome">Seu nome (opcional)</label><input id="cliente-nome" type="text" autocomplete="name"></div>
    <div class="total"><span>Total</span><span id="sacola-total">R$ 0,00</span></div>
    <button class="btn wa block" id="sacola-enviar" disabled>Finalizar pelo WhatsApp</button>
    <p class="note">Frete e forma de pagamento combinados na conversa.</p>
  </footer>
</aside>
<dialog id="produto" aria-label="Detalhes da peça"></dialog>
{WA_ICON.format(a=a)}
<script src="js/main.js"></script>
<script src="js/produtos.js"></script>
<script src="js/shop.js"></script>
</body>
</html>
'''


for a in ('ceramica', 'prata'):
    with open(f'{a}.html', 'w', encoding='utf-8') as f:
        f.write(page(a))
