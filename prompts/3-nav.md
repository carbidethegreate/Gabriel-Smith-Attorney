<!--
File: prompts/3-nav.md
Version: 1.0.0
Created: 2025-07-12
Modified: 2025-07-12
-->

# 3. Mobile Navigation Prompt

Enhance the navigation bar for mobile responsiveness:
- In the `<header>`, add a `<button>` with class `"menu-toggle"` and text `"☰ Menu"` that is hidden on desktop and visible on screens under 600px.
- Write a `<script>` that defines function `toggleMenu()`:
  - Selects the `<nav> ul` element.
  - Toggles a CSS class `"open"` on it.
- Ensure CSS rules:
  - `nav ul { display: flex; list-style: none; }`
  - `nav ul.open { display: flex; flex-direction: column; }`
  - `.menu-toggle { display: none; }`
  - `@media (max-width: 600px) {`
      `nav ul { display: none; }`
      `.menu-toggle { display: block; }`
      `nav ul.open { display: flex; }`
    `}`

