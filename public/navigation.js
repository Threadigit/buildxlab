// Navigation still works without JavaScript; this only marks the reading position.
(() => {
  const navigation = document.querySelector('.navigation');
  const links = [...document.querySelectorAll('.index a[href^="#"]')];
  const entries = links
    .map(link => ({ link, section: document.getElementById(link.hash.slice(1)) }))
    .filter(entry => entry.section);
  if (!navigation || !entries.length) return;

  let active = null;
  let pending = false;

  function update() {
    pending = false;
    const readingLine = navigation.offsetHeight + Math.min(120, innerHeight * 0.15);
    let current = null;
    for (const entry of entries) {
      if (entry.section.getBoundingClientRect().top <= readingLine) current = entry;
    }
    if (scrollY + innerHeight >= document.documentElement.scrollHeight - 2) {
      current = entries[entries.length - 1];
    }
    if (current === active) return;
    for (const entry of entries) {
      if (entry === current) entry.link.setAttribute('aria-current', 'location');
      else entry.link.removeAttribute('aria-current');
    }
    active = current;
  }

  function schedule() {
    if (pending) return;
    pending = true;
    requestAnimationFrame(update);
  }

  addEventListener('scroll', schedule, { passive: true });
  addEventListener('resize', schedule, { passive: true });
  addEventListener('hashchange', schedule);
  addEventListener('pageshow', schedule);
  document.fonts?.ready.then(schedule);
  schedule();
})();
