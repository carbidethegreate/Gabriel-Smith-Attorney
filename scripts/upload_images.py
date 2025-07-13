import os
import json
from io import BytesIO
import requests
from PIL import Image, ImageDraw, ImageFont

ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID")
API_TOKEN = os.environ.get("CF_API_TOKEN")

if not ACCOUNT_ID or not API_TOKEN:
    raise SystemExit("Missing Cloudflare credentials: set CF_ACCOUNT_ID and CF_API_TOKEN")

API_URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/images/v1"

raster_images = [
    ("headshot.jpg", (800, 800), "JPEG"),
    ("social-preview.png", (1200, 630), "PNG"),
    ("banner-courthouse.jpg", (1600, 400), "JPEG"),
    ("banner-library.jpg", (1600, 400), "JPEG"),
]

svg_icons = [
    "icon-criminal-defense.svg",
    "icon-personal-injury.svg",
    "icon-civil-litigation.svg",
    "icon-estate-planning.svg",
    "icon-crypto-recovery.svg",
]

IMAGES_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "images")

os.makedirs(IMAGES_DIR, exist_ok=True)

# create simple svg icons
svg_template = '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64"><rect width="64" height="64" fill="#00264D"/><text x="32" y="38" font-size="12" fill="white" text-anchor="middle">{}</text></svg>'
for name in svg_icons:
    path = os.path.join(IMAGES_DIR, name)
    if not os.path.exists(path):
        label = name.split("-")[1].split(".")[0].title()[0]
        with open(path, "w") as f:
            f.write(svg_template.format(label))

# upload raster images
def create_placeholder(size, fmt):
    img = Image.new("RGB", size, color=(220, 220, 220))
    return img

headers = {"Authorization": f"Bearer {API_TOKEN}"}
manifest = {}
for filename, size, fmt in raster_images:
    img = create_placeholder(size, fmt)
    buf = BytesIO()
    img.save(buf, format=fmt)
    buf.seek(0)
    files = {
        "file": (filename, buf, f"image/{'jpeg' if fmt == 'JPEG' else 'png'}")
    }
    data = {"requireSignedURLs": "false"}
    response = requests.post(API_URL, headers=headers, files=files, data=data)
    if response.status_code != 200:
        raise SystemExit(f"Upload failed for {filename}: {response.text}")
    result = response.json()
    if not result.get("success"):
        raise SystemExit(f"Upload failed for {filename}: {result}")
    variant_url = result["result"]["variants"][0]
    manifest[filename] = variant_url

manifest_path = os.path.join(IMAGES_DIR, "manifest.json")
with open(manifest_path, "w") as f:
    json.dump(manifest, f, indent=2)
print(json.dumps(manifest, indent=2))
