<!--
File: prompts/2-css.md
Version: 1.0.0
Created: 2025-07-12
Modified: 2025-07-12
-->

# 2. CSS Stylesheet Prompt

Create a CSS stylesheet for the Gabriel Smith Attorney website with these requirements:
- Color scheme:
  - Background: #ffffff (white).
  - Header and footer background: #00264D (dark blue).
  - Primary text color: #000000 (black).
- Typography:
  - Body font: a clean sans-serif (e.g., system-ui, Arial, sans-serif).
  - Headings (h1, h2, h3): serif or bold sans-serif, color #00264D.
  - Line-height: 1.6 for body text.
- Header styling:
  - Display: flex, aligned center vertically and spaced between.
  - Site title (<h1>) in white.
  - Navigation list items in horizontal row with no bullets.
  - Nav links in white; on hover or active state, change to a lighter blue or underline.
- Footer styling:
  - Text-center alignment.
  - Footer text in white on #00264D.
- Button styling:
  - Class .btn: background #00264D, color white, padding 10px 20px, border-radius 4px, text-decoration none.
  - .btn:hover: background #004080.
- Responsive images:
  - img { max-width: 100%; height: auto; display: block; }
- Utility classes:
  - .container: max-width 1200px, margin: 0 auto, padding: 0 1rem.
- Media queries:
  - @media (max-width: 600px):
    - Stack header nav items vertically.
    - Show .menu-toggle button.
    - Hide nav ul by default; display when .open class is applied.
- No external frameworks—pure CSS3.

