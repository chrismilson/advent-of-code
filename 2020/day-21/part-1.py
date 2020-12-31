from collections import Counter
import re


def findSafe(recipes):
    """
    Returns a list of all ingredients that definitely do not contain any
    allergens, and then a count of how many of those.
    """
    allIngredients = Counter()
    avoid = {}

    for ingredients, allergens in recipes:
        allIngredients += Counter(ingredients)
        for allergen in allergens:
            if allergen not in avoid:
                avoid[allergen] = set(ingredients)
            else:
                # Take the intersection with the current possibily dangerous
                # ingredients.
                avoid[allergen] = set(
                    ingredient
                    for ingredient in ingredients
                    if ingredient in avoid[allergen]
                )

    possiblyDangerous = set(
        ingredient
        for allergen in avoid
        for ingredient in avoid[allergen]
    )

    definitelySafe = [
        ingredient
        for ingredient in allIngredients
        if ingredient not in possiblyDangerous
    ]

    return definitelySafe, sum(
        allIngredients[ingredient]
        for ingredient in definitelySafe
    )


recipeRegex = re.compile(r"^((?:\w+ )+)\(contains ((?:\w+(?:, )?)+)\)$")

if __name__ == "__main__":
    recipes = []

    with open('./recipe-book.txt') as f:
        # with open('./example.txt') as f:
        for line in f:
            ingredientStr, allergenStr = recipeRegex.match(line).groups()
            recipes.append((
                ingredientStr.strip().split(' '),
                allergenStr.strip().split(', ')
            ))

    safe, result = findSafe(recipes)
    print(result)
