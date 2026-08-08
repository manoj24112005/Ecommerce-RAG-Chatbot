import base64
from pathlib import Path

base_dir = Path(__file__).parent.parent
qr_img_path = base_dir / "src" / "api" / "static" / "gpay_qr.png"
index_html_path = base_dir / "src" / "api" / "static" / "index.html"

with open(qr_img_path, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode("utf-8")
    data_uri = f"data:image/png;base64,{b64_data}"

with open(index_html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace src="/static/gpay_qr.png" with embedded data_uri
content = content.replace('src="/static/gpay_qr.png"', f'src="{data_uri}"')
content = content.replace("document.getElementById('gpayQrImage').src = `/static/gpay_qr.png`;", f"document.getElementById('gpayQrImage').src = '{data_uri}';")

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully embedded base64 QR image into index.html (Length: {len(data_uri)})")
