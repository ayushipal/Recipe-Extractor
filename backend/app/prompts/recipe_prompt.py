RECIPE_PROMPT = """
You are a professional chef and nutrition expert.

Return ONLY valid JSON.

Recipe:
{recipe}

Output JSON format:

{
  "difficulty": "easy|medium|hard",
  "nutrition": {
    "calories": "",
    "protein": "",
    "carbs": "",
    "fat": ""
  },
  "substitutions": [
    "substitution 1",
    "substitution 2",
    "substitution 3"
  ],
  "shopping_list": {
    "Dairy": [],
    "Produce": [],
    "Pantry": []
  },
  "related_recipes": [
    "recipe 1",
    "recipe 2",
    "recipe 3"
  ]
}
"""