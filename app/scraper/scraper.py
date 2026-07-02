import json
from pathlib import Path

import requests


CATALOG_URL = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

OUTPUT_FILE = Path("app/data/assessments.json")


def download_catalog():
    print("Downloading SHL Product Catalog...")

    response = requests.get(CATALOG_URL, timeout=30)
    response.raise_for_status()

    # Save the raw response so we can inspect it
    with open("app/data/raw_catalog.json", "w", encoding="utf-8") as f:
        f.write(response.text)

    print("Raw catalog saved.")

    return response.text

def save_catalog(data):
    """
    Save catalog locally.
    """

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Catalog saved to {OUTPUT_FILE}")


def main():

    catalog = download_catalog()

    print(f"Total assessments: {len(catalog)}")

    save_catalog(catalog)


if __name__ == "__main__":
    main()