class Recipe(object):
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = "Easy"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.calculate_difficulty()

    def get_cooking_time(self):
        return self.cooking_time

    def add_ingredients(self, *ingredients):
        for i in ingredients:
            if not (i in self.ingredients):
                self.ingredients.append(i)

        self.update_all_ingredients()
        self.calculate_difficulty()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)

        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"

        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"

        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"

        else:
            self.difficulty = "Hard"

    def get_difficulty(self):
        self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for i in self.ingredients:
            if not (i in Recipe.all_ingredients):
                Recipe.all_ingredients.append(i)

    def __str__(self):
        output = f"\nRecipe: {self.name} \nCooking Time (min): {self.cooking_time} \nIngredients: "
        for i in self.ingredients:
            output += f"\n{i}"

        output += f"\nDifficulty level: {self.difficulty}"
        return output

    def recipe_search(data, search_term):
        print(f"\nRecipes that contain {search_term}:")
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)


tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
print(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
print(coffee)

cake = Recipe("Cake")
cake.add_ingredients(
    "Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"
)
cake.set_cooking_time(50)
print(cake)

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"
)
banana_smoothie.set_cooking_time(5)
print(banana_smoothie)


recipes_list = [tea, coffee, cake, banana_smoothie]

Recipe.recipe_search(recipes_list, "Water")
Recipe.recipe_search(recipes_list, "Sugar")
Recipe.recipe_search(recipes_list, "Bananas")
