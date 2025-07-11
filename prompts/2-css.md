<!--
File: prompts/2-css.md
Version: 1.0.0
Created: 2025-07-11
Modified: 2025-07-11
-->

# 2. Main Stylesheet Prompt

Use this prompt with OpenAI Codex to generate a professional, responsive CSS stylesheet for Gabriel Smith’s website. Copy the entire block below (including the numbered section comments) into your Codex call.

Generate a CSS file at css/style.css that implements the following:

/* 1. Reset & Base Styles */
*,
*::before,
*::after {
margin: 0;
padding: 0;
box-sizing: border-box;
}
html {
font-size: 16px;
}
body {
font-family: "Helvetica Neue", Arial, sans-serif;
line-height: 1.6;
color: #333;
background-color: #fff;
}

/* 2. Typography */
h1, h2, h3, h4, h5, h6 {
color: #00264D;
font-weight: 700;
margin-bottom: 0.5em;
}
p {
margin-bottom: 1em;
}
a {
color: #00264D;
text-decoration: none;
}
a:hover {
text-decoration: underline;
}

/* 3. Layout & Header */
header {
background-color: #00264D;
color: #fff;
padding: 1rem 2rem;
}
header h1 {
font-size: 1.75rem;
}
main {
max-width: 960px;
margin: 2rem auto;
padding: 0 1rem;
}

/* 4. Navigation */
nav ul {
list-style: none;
display: flex;
gap: 1rem;
}
nav a {
color: #fff;
padding: 0.5rem;
}
nav a:hover,
nav a.active {
background-color: #004080;
border-radius: 4px;
}

/* 5. Buttons & CTAs */
.btn {
display: inline-block;
background-color: #00264D;
color: #fff;
padding: 0.75rem 1.5rem;
border-radius: 4px;
text-align: center;
}
.btn:hover {
background-color: #004080;
}

/* 6. Footer */
footer {
background-color: #00264D;
color: #fff;
text-align: center;
padding: 1rem 2rem;
font-size: 0.875rem;
}

/* 7. Responsive Media Queries */
@media (max-width: 768px) {
nav ul {
flex-direction: column;
display: none;
}
nav ul.open {
 display: flex;
}
.menu-toggle {
 display: block;
 background: none;
 border: none;
 color: #fff;
 font-size: 1.25rem;
 cursor: pointer;
}
}

This stylesheet:
- Resets margins and paddings for consistency
- Sets base typography and color scheme (navy `#00264D` + white/`#fff`)
- Styles header, navigation, buttons, and footer
- Includes a mobile breakpoint at 768px to stack the nav and support a `.menu-toggle` control

<!-- End of prompts/2-css.md -->
