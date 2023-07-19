import pickle


def display_recipe(recipe):
    print("Recipe:", recipe["name"])
    print("Cooking Time (min):", recipe["cooking_time"])
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty level: ", recipe["difficulty"], "\n")


def search_ingredient(data):
    print("Ingredients Available Across All Recipes")
    print("----------------------------------------")
    for index, ingredient in enumerate(data["all_ingredients"]):
        print(f"{index}. {ingredient}")

    try:
        print(
            "This script will display all recipes that include the choosen ingredient."
        )
        index = int(
            input(
                "Enter a number from the above list representing the ingredient to be searched: "
            )
        )
        ingredient_searched = data["all_ingredients"][index]

    except:
        print("This input is incorrect.")

    else:
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)


filename = str(input("Enter the name of the file where the recipe data is stored: "))

try:
    file = open(filename, "rb")
    data = pickle.load(file)

except FileNotFoundError:
    print("File does not exist.")

else:
    search_ingredient(data)
    file.close()
