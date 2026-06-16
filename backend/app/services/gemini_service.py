import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from app.prompts.recipe_prompt import RECIPE_PROMPT

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)


def generate_recipe_insights(recipe_data):
    try:
        prompt = RECIPE_PROMPT.format(
            recipe=json.dumps(recipe_data)
        )

        response = llm.invoke(prompt)

        if not response or not response.content:
            return {}

        content = response.content.strip()

        # SAFE JSON EXTRACTION
        try:
            return json.loads(content)
        except:
            import re
            match = re.search(r"\{.*\}", content, re.S)
            if match:
                return json.loads(match.group())

        # LAST FALLBACK (NEVER FAIL)
        return {
            "difficulty": "easy",
            "nutrition": {},
            "substitutions": [],
            "shopping_list": {},
            "related_recipes": []
        }

    except Exception as e:
        return {
            "difficulty": "easy",
            "nutrition": {},
            "substitutions": [],
            "shopping_list": {},
            "related_recipes": [],
            "error": str(e)
        }