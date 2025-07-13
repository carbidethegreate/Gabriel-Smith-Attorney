import os
import json
from io import BytesIO
import requests
from PIL import Image


def main():
    account_id = os.environ.get("CF_ACCOUNT_ID")
    api_token = os.environ.get("CF_API_TOKEN")
    if not account_id or not api_token:
        raise SystemExit(
            "Missing Cloudflare credentials: set CF_ACCOUNT_ID and CF_API_TOKEN"
        )

    api_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1"

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

    images_dir = os.path.join(os.path.dirname(__file__), os.pardir, "images")
    os.makedirs(images_dir, exist_ok=True)

    svg_template = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64">'
        '<rect width="64" height="64" fill="#00264D"/>'
        '<text x="32" y="38" font-size="12" fill="white" text-anchor="middle">{}'
        '</text></svg>'
    )
    for name in svg_icons:
        path = os.path.join(images_dir, name)
        if not os.path.exists(path):
            label = name.split("-")[1].split(".")[0].title()[0]
            with open(path, "w") as f:
                f.write(svg_template.format(label))

    def create_placeholder(size, fmt):
        img = Image.new("RGB", size, color=(220, 220, 220))
        return img

    headers = {"Authorization": f"Bearer {api_token}"}
    manifest = {}
    for filename, size, fmt in raster_images:
        img = create_placeholder(size, fmt)
        buf = BytesIO()
        img.save(buf, format=fmt)
        buf.seek(0)
        files = {"file": (filename, buf, f"image/{'jpeg' if fmt == 'JPEG' else 'png'}")}
        data = {"requireSignedURLs": "false"}
        response = requests.post(api_url, headers=headers, files=files, data=data)
        if response.status_code != 200:
            raise SystemExit(f"Upload failed for {filename}: {response.text}")
        result = response.json()
        if not result.get("success"):
            raise SystemExit(f"Upload failed for {filename}: {result}")
        variant_url = result["result"]["variants"][0]
        manifest[filename] = variant_url

    manifest_path = os.path.join(images_dir, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
