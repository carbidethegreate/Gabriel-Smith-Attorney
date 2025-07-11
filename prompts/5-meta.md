<!--
File: prompts/5-meta.md
Version: 1.0.0
Created: 2025-07-11
Modified: 2025-07-11
-->

# 5. Meta Tags Prompt

Use this prompt with GPT-4 (or Codex) to generate SEO-friendly `<title>`, `<meta name="description">`, `<meta name="keywords">`, and Open Graph / Twitter Card tags for a given page. Copy the entire block below into your AI call, replacing the placeholders.

Generate the head meta tags for a page on Gabriel Smith’s site with the following details:
•PAGE_TITLE: “About Gabriel Smith – Opelika Attorney”
•PAGE_DESCRIPTION: “Learn about Gabriel Smith, an Opelika attorney with over a decade of experience, UA Law cum laude grad, Alabama Bar admitted 2012.”
•PAGE_KEYWORDS: “Gabriel Smith, Opelika attorney, Alabama lawyer, attorney bio”

Output the following HTML snippet:
```html
<title>PAGE_TITLE</title>
<meta name="description" content="PAGE_DESCRIPTION">
<meta name="keywords" content="PAGE_KEYWORDS">

<meta property="og:title" content="PAGE_TITLE">
<meta property="og:description" content="PAGE_DESCRIPTION">
<meta property="og:image" content="https://gabriel-smith-alabama-attorney.com/images/social-preview.jpg">
<meta property="og:url" content="https://gabriel-smith-alabama-attorney.com/about.html">
<meta property="og:type" content="website">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="PAGE_TITLE">
<meta name="twitter:description" content="PAGE_DESCRIPTION">
<meta name="twitter:image" content="https://gabriel-smith-alabama-attorney.com/images/social-preview.jpg">
```

Replace PAGE_TITLE, PAGE_DESCRIPTION, PAGE_KEYWORDS, and the URLs with the actual values for each page. Use absolute URLs for og:image and og:url to ensure complete social sharing metadata.

<!-- End of prompts/5-meta.md -->
