# Gabriel-Smith-Attorney
Gabriel Smith Alabama Attorney

## Image Upload

To update Cloudflare-hosted images, set the following environment variables before
running the upload script:

```
export CF_ACCOUNT_ID=YOUR_ACCOUNT_ID
export CF_API_TOKEN=YOUR_TOKEN
```

Then execute:

```
python3 scripts/upload_images.py
```

The script uploads placeholder images to Cloudflare and writes their delivery URLs
to `images/manifest.json`.
