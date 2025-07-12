function toggleMenu() {
  const menu = document.querySelector('header nav ul');
  if (menu) {
    menu.classList.toggle('open');
  }
}

document.addEventListener('DOMContentLoaded', function() {
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('header nav ul');
  if (toggle && menu) {
    toggle.addEventListener('click', toggleMenu);
    menu.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        if (menu.classList.contains('open')) {
          menu.classList.remove('open');
        }
      });
    });
  }
});
