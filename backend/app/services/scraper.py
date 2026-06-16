import requests
from bs4 import BeautifulSoup
import json


def scrape_recipe_page(url: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }

    try:
        print(f"SCRAPING URL: {url}")

        response = requests.get(
            url,
            headers=headers,
            timeout=30,
            allow_redirects=True
        )

        print("STATUS CODE:", response.status_code)
        print("FINAL URL:", response.url)

        if response.status_code != 200:
            raise Exception(f"HTTP {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")

        scripts = soup.find_all(
            "script",
            type="application/ld+json"
        )

        print("JSON-LD SCRIPTS FOUND:", len(scripts))

        for script in scripts:
            try:
                if not script.string:
                    continue

                data = json.loads(script.string)

                if isinstance(data, list):
                    for item in data:
                        if (
                            isinstance(item, dict)
                            and item.get("@type") == "Recipe"
                        ):
                            return item

                elif (
                    isinstance(data, dict)
                    and data.get("@type") == "Recipe"
                ):
                    return data

            except Exception:
                continue

        return {
            "name": soup.title.string if soup.title else "Recipe",
            "recipeIngredient": [],
            "recipeInstructions": []
        }

    except Exception as e:
        raise Exception(f"Scraping failed: {str(e)}")