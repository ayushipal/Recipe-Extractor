import requests
import json
from bs4 import BeautifulSoup


def scrape_recipe_page(url: str):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=20,
            allow_redirects=True
        )

        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        return {"error": f"HTTP {str(e)}"}

    soup = BeautifulSoup(response.text, "html.parser")

    scripts = soup.find_all("script", type="application/ld+json")

    for script in scripts:
        if not script.string:
            continue

        try:
            data = json.loads(script.string)

            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and "Recipe" in str(item.get("@type", "")):
                        return item

            elif isinstance(data, dict):
                if "Recipe" in str(data.get("@type", "")):
                    return data

        except json.JSONDecodeError:
            continue

    return {
        "error": "Recipe schema not found",
        "title": soup.title.string if soup.title else "Unknown"
    }