<!--
File: prompts/3-nav.md
Version: 1.0.0
Created: 2025-07-11
Modified: 2025-07-11
-->

# 3. Responsive Navigation Prompt

Use this prompt with OpenAI Codex to generate a mobile-friendly navigation bar and the accompanying JavaScript toggle. Copy the block below (including numbered section comments) into your Codex call.

Generate the updated header markup and a JS file as follows:
```html
/* 1. Header & Navigation HTML */
/* — insert inside <header> just before </header> — */
<button class="menu-toggle">☰</button>

<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
    <li class="has-children">
      <a href="#">Practice Areas</a>
      <ul class="dropdown">
        <li><a href="criminal-defense.html">Criminal Defense</a></li>
        <li><a href="personal-injury.html">Personal Injury</a></li>
        <li><a href="civil-litigation.html">Civil Litigation</a></li>
        <li><a href="estate-planning.html">Estate Planning</a></li>
        <li><a href="cryptocurrency-recovery.html">Cryptocurrency Recovery</a></li>
      </ul>
    </li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>


/* 2. JavaScript for menu toggle (save as js/menu.js) */
document.addEventListener('DOMContentLoaded', function() {
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('header nav ul');

  toggle.addEventListener('click', () => {
    menu.classList.toggle('open');
  });

  // Optional: close menu when a link is clicked (mobile)
  menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      if (menu.classList.contains('open')) {
        menu.classList.remove('open');
      }
    });
  });
});
```

This will add a hamburger button on small screens that toggles the navigation's `.open` class (which your CSS will show/hide via the media query).

<!-- End of prompts/3-nav.md -->
