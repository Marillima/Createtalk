# CREATE Ceramic Studio + Alquimista Dourado

Portal com duas lojas de peças feitas à mão

- **CREATE Ceramic Studio**: canecas, vasos e potes de cerâmica.
- **Alquimista Dourado**: joias esculpidas em prata e ouro.

## Páginas

| Arquivo | Descrição |
|---|---|
| `index.html` | Portal de entrada, com duas portas (cerâmica / prata). |
| `ceramica.html` | Loja CREATE Ceramic Studio. **Gerada** por `build.py`. |
| `prata.html` | Loja Alquimista Dourado. **Gerada** por `build.py`. |

## Estrutura

```
lp/
├── index.html
├── ceramica.html      # gerado
├── prata.html         # gerado
├── build.py           # template único das duas lojas
├── css/
│   ├── base.css       # estilos compartilhados
│   ├── ceramica.css   # tema cerâmica
│   └── prata.css      # tema prata
├── js/
│   ├── main.js        # WhatsApp, NOMES, formulário de encomenda
│   ├── produtos.js    # catálogo
│   └── shop.js        # filtros, sacola, modal de produto
└── img/               # imagens em .webp
```

## Funcionalidades

- Catálogo com filtro por categoria e modal de detalhes.
- Sacola persistida em `localStorage` (uma por marca).
- Finalização do pedido por mensagem pronta no WhatsApp (`wa.me`).
- Formulário de encomenda personalizada que também envia pelo WhatsApp.
- Peças sem preço aparecem como "Sob consulta".
- Mobile-first, HTML/CSS/JS puros, sem dependências ou build de front-end.

### Visual

- Estilos comuns: `css/base.css`
- Tema de cada marca: `css/ceramica.css` e `css/prata.css`
- A página inicial (`index.html`) tem o CSS embutido.
