<!--
File: prompts/7-sitemap.md
Version: 1.0.0
Created: 2025-07-12
Modified: 2025-07-12
-->

# 7. Sitemap Prompt

Generate a simple XML sitemap listing these URLs (use absolute paths without domain):
- /index.html
- /about.html
- /criminal-defense.html
- /personal-injury.html
- /civil-litigation.html
- /estate-planning.html
- /cryptocurrency-recovery.html
- /contact.html
- Include any resource pages, blog listing page, and any subpages under /cryptocurrency-recovery/ or /blog/.
Wrap in:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://gabriel‑smith‑alabama‑attorney.com/index.html</loc>
  </url>
  ...
</urlset>
```

