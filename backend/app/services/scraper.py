import requests
from bs4 import BeautifulSoup
import json

def find_recipe_schema(obj):
"""
Recursively find Recipe schema in JSON-LD
"""

if isinstance(obj, dict):

    if obj.get("@type") == "Recipe":
        return obj

    if "@graph" in obj:
        for item in obj["@graph"]:
            recipe = find_recipe_schema(item)
            if recipe:
                return recipe

    for value in obj.values():
        recipe = find_recipe_schema(value)
        if recipe:
            return recipe

elif isinstance(obj, list):
    for item in obj:
        recipe = find_recipe_schema(item)
        if recipe:
            return recipe

return None

def scrape_recipe_page(url: str):

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

try:

    response = requests.get(
        url,
        headers=headers,
        timeout=30,
        allow_redirects=True
    )

    print("URL:", url)
    print("STATUS:", response.status_code)

    if response.status_code != 200:
        raise Exception(f"HTTP {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")

    scripts = soup.find_all(
        "script",
        type="application/ld+json"
    )

    for script in scripts:

        if not script.string:
            continue

        try:
            data = json.loads(script.string)

            recipe = find_recipe_schema(data)

            if recipe:
                return recipe

        except Exception:
            continue

    return {
        "name": soup.title.get_text(strip=True)
        if soup.title
        else "Recipe",

        "recipeIngredient": [],

        "recipeInstructions": []
    }

except Exception as e:
    raise Exception(f"Scraping failed: {str(e)}")