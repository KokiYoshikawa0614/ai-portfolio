const filters = document.querySelectorAll('[data-filter]');
const projects = document.querySelectorAll('[data-category]');
filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  let count = 0;
  projects.forEach(project => {
    const visible = button.dataset.filter === 'all' || project.dataset.category === button.dataset.filter;
    project.hidden = !visible;
    if (visible) count++;
  });
  document.getElementById('filter-status').textContent = `${count}件の実績を表示`;
}));
