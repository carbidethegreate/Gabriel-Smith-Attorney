<!--
File: prompts/5-meta.md
Version: 1.0.0
Created: 2025-07-12
Modified: 2025-07-12
-->

# 5. Meta Tags Prompt

For each page, generate:
- `<title>` around 50–60 characters including page focus and keywords.
- `<meta name="description">` ~150 characters summarizing page content and CTA.
- `<meta name="keywords">` a comma‑separated list of 5–7 relevant keywords.
- Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`).
- Twitter Card tags (`twitter:card`, `twitter:title`, `twitter:description`).

List them in blocks labeled by filename, e.g.:

```
--- about.html ---
<title>…</title>
<meta name="description" content="…">
...
```

