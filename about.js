document.addEventListener('DOMContentLoaded', () => {
  // Highlight active nav link
  const navLinks = document.querySelectorAll('header nav a');
  navLinks.forEach(link => {
    if (link.href === window.location.href) link.classList.add('active');
  });

  // Smooth scroll for any anchor links on the page
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
    });
  });

  // Fade-in animation on scroll
  const sections = document.querySelectorAll('main section');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.1 });
  sections.forEach(sec => {
    sec.classList.add('hidden-section');
    observer.observe(sec);
  });
});
