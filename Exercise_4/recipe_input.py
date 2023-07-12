import pickle


def take_recipe():
    name = str(input("Enter the name of this recipe: "))
    cooking_time = int(input("Enter the cooking time: "))
    ingredients = str(input("Enter the list of ingredients:")).split(", ")

    difficulty = calc_difficulty(cooking_time, len(ingredients))

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }

    return recipe


def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"

    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"

    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"

    else:
        difficulty = "Hard"

    return difficulty


filename = str(input("Enter the name of the file where the recipes are stored: "))
recipes_list = []
all_ingredients = []

try:
    file = open(filename, "rb")
    data = pickle.load(file)

except FileNotFoundError:
    data = {"recipes_list": [], "all_ingredients": []}

except:
    data = {"recipes_list": [], "all_ingredients": []}

else:
    file.close()

finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


n = int(input("How many recipes would you like to enter? "))

for i in range(0, n):
    recipe = take_recipe()
    recipes_list.append(recipe)

    for ingredient in recipe["ingredients"]:
        if not (ingredient in all_ingredients):
            all_ingredients.append(ingredient)

data["recipes_list"] = recipes_list
data["all_ingredients"] = all_ingredients

recipe_file = open(filename, "wb")
pickle.dump(data, recipe_file)
recipe_file.close()
