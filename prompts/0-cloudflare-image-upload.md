# 0. Cloudflare Image Upload Prompt

Use the following Cloudflare credentials and API to generate and upload all raster images, then record their delivery URLs. **Do not commit any binary files to the repo.** Instead, upload via the Cloudflare Images API and reference the returned URLs.

Cloudflare Credentials (provided via environment variables):
- `CF_ACCOUNT_ID`
- `CF_API_TOKEN`
- Image delivery URL pattern: `https://imagedelivery.net/MqlML99ManDWvfuYMb9PmQ/<image_id>/<variant_name>`

Test your API token with:
```
curl "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT_ID/tokens/verify" \
     -H "Authorization: Bearer $CF_API_TOKEN"
```

Required raster images:
- headshot.jpg (800×800 px, JPEG)
- social-preview.png (1200×630 px, PNG)
- banner-courthouse.jpg (1600×400 px, JPEG)
- banner-library.jpg (1600×400 px, JPEG)

Required SVG icons (save to images/):
- icon-criminal-defense.svg
- icon-personal-injury.svg
- icon-civil-litigation.svg
- icon-estate-planning.svg
- icon-crypto-recovery.svg

Instructions:
1. Generate SVG icons and save to images/.
2. Generate raster images in memory and upload via Cloudflare Images API:
   `POST https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT_ID/images/v1`
   Headers:
     `Authorization: Bearer $CF_API_TOKEN`
   Form fields:
     `file`: binary image bytes
     `requireSignedURLs`: false
3. Extract the first variant URL from response (`result.variants[0]`).
4. Create `images/manifest.json` mapping filenames to URLs.
5. Reference Cloudflare URLs in HTML `<img>` tags, CSS, and OG/Twitter meta tags.

If any upload fails, output a clear error and stop.
