from fastapi import APIRouter, HTTPException
from app.schemas.recipe import RecipeRequest
from app.services.scraper import scrape_recipe_page
from app.services.gemini_service import generate_recipe_insights
from app.utils.safe_json import safe_json_parse

router = APIRouter()


def extract_instructions(recipe):
    instructions = recipe.get("recipeInstructions", [])

    if isinstance(instructions, str):
        return [instructions]

    if isinstance(instructions, list):
        steps = []
        for step in instructions:
            if isinstance(step, dict):
                steps.append(step.get("text", ""))
            else:
                steps.append(str(step))
        return steps

    return []


@router.post("/extract-recipe")
def extract_recipe(data: RecipeRequest):

    try:
        recipe = scrape_recipe_page(data.url)

        if recipe.get("error"):
            raise HTTPException(status_code=400, detail=f"Scraping failed: {recipe['error']}")

        raw_insights = generate_recipe_insights(recipe)
        insights = safe_json_parse(raw_insights)

        return {
            "recipe": {
                "name": recipe.get("name") or recipe.get("title"),
                "ingredients": recipe.get("recipeIngredient", []),
                "instructions": extract_instructions(recipe)
            },
            "generated": insights
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))