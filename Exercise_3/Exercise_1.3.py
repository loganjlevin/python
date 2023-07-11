recipes_list = []
ingredients_list = []


def take_recipe():
    name = str(input("Enter the name of this recipe: "))
    cooking_time = int(input("Enter the cooking time: "))
    ingredients = str(input("Enter the list of ingredients:")).split(", ")
    print("\n")

    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    return recipe


n = int(input("How many recipes would you like to enter? "))

for i in range(0, n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if not (ingredient in ingredients_list):
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Easy"

    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        difficulty = "Medium"

    if recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Intermediate"

    if recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
        difficulty = "Hard"

    print("Recipe:", recipe["name"])
    print("Cooking Time (min):", recipe["cooking_time"])
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty level: ", difficulty, "\n")

ingredients_list.sort()
print("Ingredients Available Across All Recipes")
print("----------------------------------------")
for ingredient in ingredients_list:
    print(ingredient)
