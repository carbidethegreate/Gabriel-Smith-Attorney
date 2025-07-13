<!--
File: prompts/6-jsonld.md
Version: 1.0.0
Created: 2025-07-12
Modified: 2025-07-12
-->

# 6. JSON-LD Prompt

Provide a JSON-LD `<script>` tag for Organization schema for the “Law Office of Gabriel Smith”:
- Use `"@context": "https://schema.org"`.
- Use `"@type": "Attorney"` or `"Organization"`.
- `name`: "Law Office of Gabriel Smith".
- `url`: "https://gabriel-smith-alabama-attorney.com".
- `logo`: "https://gabriel-smith-alabama-attorney.com/images/logo.png".
- `address` as a nested PostalAddress:
  - `streetAddress`: "123 Main Street".
  - `addressLocality`: "Opelika".
  - `addressRegion`: "AL".
  - `postalCode`: "36801".
- `telephone`: "(334) 750-1729".
- Include it as a `<script type="application/ld+json">` in the `<head>`.

