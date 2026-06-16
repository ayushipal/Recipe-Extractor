import json
import re


def safe_json_parse(text: str):
    try:
        return json.loads(text)
    except Exception:
        pass

    try:
        cleaned = re.search(r"\{.*\}", text, re.S)
        if cleaned:
            return json.loads(cleaned.group(0))
    except Exception:
        pass

    return {
        "difficulty": "easy",
        "nutrition": {},
        "substitutions": [],
        "shopping_list": {"Dairy": [], "Produce": [], "Pantry": []},
        "related_recipes": []
    }