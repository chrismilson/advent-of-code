from collections import Counter
import re


def identifyAllergens(recipes):
    """
    Returns a list of all ingredients that definitely do not contain any
    allergens, and then a count of how many of those.
    """
    avoid = {}

    for ingredients, allergens in recipes:
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

    result = {}

    while len(avoid) > 0:
        # We want to find an allergen with only one possible cause.
        for allergen in avoid:
            if len(avoid[allergen]) == 1:
                result[allergen] = next(iter(avoid[allergen]))
                del avoid[allergen]
                for other in avoid:
                    if result[allergen] in avoid[other]:
                        avoid[other].remove(result[allergen])
                break
        else:
            print(avoid)
            raise ValueError("It is not possible to identify all allergens.")

    return result


recipeRegex = re.compile(r"^((?:\w+ )+)\(contains ((?:\w+(?:, )?)+)\)$")

if __name__ == "__main__":
    recipes = []

    # with open('./example.txt') as f:
    with open('./recipe-book.txt') as f:
        for line in f:
            ingredientStr, allergenStr = recipeRegex.match(line).groups()
            recipes.append((
                ingredientStr.strip().split(' '),
                allergenStr.strip().split(', ')
            ))

    allergens = identifyAllergens(recipes)
    result = ','.join(allergens[allergen] for allergen in sorted(allergens))
    print(result)
