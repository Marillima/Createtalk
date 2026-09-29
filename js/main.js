
const WHATSAPP = { ceramica: '+55 12 99717-5831', prata: '12 99647-9397' };
const NOMES = { ceramica: 'CREATE Ceramic Studio', prata: 'Alquimista Dourado' };

const form = document.getElementById('brief');
if (form) {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const ala = form.dataset.ala;
    const f = new FormData(form);
    const linhas = [
      `Olá! Quero fazer uma encomenda na ${NOMES[ala]}.`,
      f.get('peca') && `Peça: ${f.get('peca')}`,
      f.get('ocasiao') && `Ocasião: ${f.get('ocasiao')}`,
      f.get('faixa') && `Investimento: ${f.get('faixa')}`,
      f.get('tamanho') && `Tamanho: ${f.get('tamanho')}`,
      f.get('prazo') && `Prazo: ${f.get('prazo')}`,
      f.get('ideia') && `Minha ideia: ${f.get('ideia')}`,
    ].filter(Boolean).join('\n');
    window.open(`https://wa.me/${WHATSAPP[ala]}?text=${encodeURIComponent(linhas)}`, '_blank', 'noopener');
  });
}
document.querySelectorAll('[data-wa]').forEach(a => {
  const ala = a.dataset.wa;
  a.href = `https://wa.me/${WHATSAPP[ala]}?text=${encodeURIComponent('Olá! Vim pelo site da ' + NOMES[ala] + '.')}`;
});
