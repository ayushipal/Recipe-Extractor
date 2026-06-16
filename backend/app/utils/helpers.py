def extract_instructions(recipe):
    """
    Normalize instructions from different websites
    """

    instructions = []

    try:
        steps = recipe.get("recipeInstructions", [])

        if isinstance(steps, list):
            for step in steps:
                if isinstance(step, str):
                    instructions.append(step)
                elif isinstance(step, dict):
                    instructions.append(step.get("text", ""))

        elif isinstance(steps, str):
            instructions = [steps]

    except:
        instructions = []

    return instructions