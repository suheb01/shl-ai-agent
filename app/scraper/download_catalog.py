import requests
from pathlib import Path

CATALOG_URL = (
    "https://tcp-us-prod-rnd.shl.com/voiceRater/"
    "shl-ai-hiring/shl_product_catalog.json"
)

OUTPUT_FILE = Path("app/data/raw_catalog.json")


def download_catalog():

    print("Downloading SHL catalog...")

    response = requests.get(CATALOG_URL, timeout=30)
    response.raise_for_status()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(
        response.text,
        encoding="utf-8"
    )

    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    download_catalog()