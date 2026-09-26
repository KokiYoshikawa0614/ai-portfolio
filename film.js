const trailerButtons = document.querySelectorAll('[data-video]');
trailerButtons.forEach(button => button.addEventListener('click', () => {
  const label = button.dataset.label;
  const video = button.dataset.video;
  trailerButtons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  const player = document.getElementById('trailer-player');
  player.src = `https://www.youtube-nocookie.com/embed/${video}`;
  player.title = `HALUCINATION ${label}`;
  const link = document.getElementById('trailer-link');
  link.href = `https://youtu.be/${video}`;
  link.textContent = `${label}をYouTubeで見る ↗`;
}));
