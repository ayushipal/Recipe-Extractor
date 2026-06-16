import requests
from bs4 import BeautifulSoup
import json


def scrape_recipe_page(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122 Safari/537.36"
    }

    try:
        r = requests.get(url, headers=headers, timeout=20)

        if r.status_code != 200:
            raise Exception(f"HTTP {r.status_code}")

        soup = BeautifulSoup(r.text, "html.parser")

        # TRY JSON-LD FIRST
        scripts = soup.find_all("script", type="application/ld+json")

        for s in scripts:
            try:
                data = json.loads(s.string)

                if isinstance(data, list):
                    data = data[0]

                if isinstance(data, dict) and data.get("@type") == "Recipe":
                    return data

            except:
                continue

        # FALLBACK EXTRACTION
        return {
            "name": soup.title.string if soup.title else "Recipe",
            "recipeIngredient": [],
            "recipeInstructions": []
        }

    except Exception as e:
        raise Exception(f"Scraping failed: {str(e)}")