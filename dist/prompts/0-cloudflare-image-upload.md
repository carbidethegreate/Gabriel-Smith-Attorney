# 0. Cloudflare Image Upload Prompt

Use the following Cloudflare credentials and API to generate and upload all raster images, then record their delivery URLs. **Do not commit any binary files to the repo.** Instead, upload via the Cloudflare Images API and reference the returned URLs.

Cloudflare Credentials:
- Account ID: 9748736d8674bad21f5e685fa96db7cd
- Image delivery URL pattern: https://imagedelivery.net/MqlML99ManDWvfuYMb9PmQ/<image_id>/<variant_name>
- Account hash: MqlML99ManDWvfuYMb9PmQ
- Global API Token: v1.0-f40987f9239e5cc2d81dee0a-ca3725e52e8abc99e31dd99f24ea706e25e67aff35f0c53b93e71840c5c7981015c0a53678db61fddc828f98820789b8adde25c050e341468dce92e8865c334794278157b2c5de3dfb
- Origin CA Key: v1.0-f40987f9239e5cc2d81dee0a-ca3725e52e8abc99e31dd99f24ea706e25e67aff35f0c53b93e71840c5c7981015c0a53678db61fddc828f98820789b8adde25c050e341468dce92e8865c334794278157b2c5de3dfb
- API Token: Y0HLGcRrOROlxc-bqqwP2iZsk80jt_GDUlwhR2si

Test your API token with:
```
curl "https://api.cloudflare.com/client/v4/accounts/9748736d8674bad21f5e685fa96db7cd/tokens/verify" \
     -H "Authorization: Bearer Y0HLGcRrOROlxc-bqqwP2iZsk80jt_GDUlwhR2si"
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
   `POST https://api.cloudflare.com/client/v4/accounts/9748736d8674bad21f5e685fa96db7cd/images/v1`
   Headers:
     `Authorization: Bearer Y0HLGcRrOROlxc-bqqwP2iZsk80jt_GDUlwhR2si`
   Form fields:
     `file`: binary image bytes
     `requireSignedURLs`: false
3. Extract the first variant URL from response (`result.variants[0]`).
4. Create `images/manifest.json` mapping filenames to URLs.
5. Reference Cloudflare URLs in HTML `<img>` tags, CSS, and OG/Twitter meta tags.

If any upload fails, output a clear error and stop.
