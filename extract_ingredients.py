import re

def extract_ingredients(recipe_text):
    """
    Extracts the list of ingredients from the recipe text.

    Args:
        recipe_text (str): The full recipe text output from the model.

    Returns:
        list: A list of ingredients extracted from the recipe.
    """
    # Regular expression to extract ingredients section
    ingredients_pattern = r"(?<=\*\*Ingredients:\*\*\n)([\s\S]*?)(?=\*\*Recipe:)"
    match = re.search(ingredients_pattern, recipe_text)

    if match:
        # Extract the ingredients section
        ingredients_text = match.group(1)

        # Clean and split the ingredients into a list by bullet points
        ingredients_list = [ingredient.strip("* ").strip() for ingredient in ingredients_text.split("\n") if ingredient.strip()]

        return ingredients_list
    else:
        raise ValueError("Ingredients section not found in the recipe text.")

