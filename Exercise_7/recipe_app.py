# import all the necessary packages and functions
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# Create the engine object that connects to the database
engine = create_engine("mysql://logan:logan@localhost/task_database")

# Create the session object to that will be used to make changes to the database
Session = sessionmaker(bind=engine)
session = Session()

# Store the declarative base class into a variable called Base
Base = declarative_base()


# Create the Recipe class model
class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"Recipe ID: {self.id} | Recipe Name: {self.name} | Recipe Difficulty: {self.difficulty}"

    def __str__(self):
        print(f"|      ID      | {self.id}")
        print(f"|     Name     | {self.name}")
        print(f"| Cooking Time | {self.cooking_time}")
        print(f"|  Difficulty  | {self.difficulty}")
        print(f"| Ingredients  | {self.ingredients}")

    def calc_difficulty(self):
        num_ingredients = len(self.ingredients.split(", "))

        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"

        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"

        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"

        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        else:
            return self.ingredients.split(", ")


# Create the Recipe table in the database
Base.metadata.create_all(engine)


# Define the create recipe function
def create_recipe():
    # Get recipe name from user with max 50 alphanumeric characters
    has_not_recieved_valid_input = True
    while has_not_recieved_valid_input:
        name = str(
            input("Enter the name of the recipe(max 50 alphanumeric characters): ")
        )
        if len(name) == 0:
            print("Nothing was entered. Please try again.")
        elif len(name) > 50:
            print("Name is too long. Max of 50 characters. Please try again.")
        elif not (name.isalnum()):
            print("Name must contain only alphanumeric characters. Please try again.")
        else:
            has_not_recieved_valid_input = False

    # Get recipe cooking time from user - must be a number greater than 0
    has_not_recieved_valid_input = True
    while has_not_recieved_valid_input:
        cooking_time = input("Enter the cooking time of the recipe in minutes: ")
        if int(cooking_time) <= 0:
            print("Cooking time must be greater than 0 minutes. Please try again.")
        elif not (cooking_time.isnumeric()):
            print("Cooking time must be a number. Please try again.")
        else:
            has_not_recieved_valid_input = False

    # Get recipe ingredients from user
    ingredients = []
    # Get the number of ingredients
    has_not_recieved_valid_input = True
    while has_not_recieved_valid_input:
        num_ingredients = input(
            "How many ingredients would you like to enter? Enter a number greater than 0: "
        )
        if int(num_ingredients) <= 0:
            print("You must enter more than 0 ingredients. Please try again.")
        elif not (num_ingredients.isnumeric()):
            print("You must enter a numer. Please try again.")
        else:
            has_not_recieved_valid_input = False
    # Get each ingredient
    for i in range(int(num_ingredients)):
        has_not_recieved_valid_input = True
        while has_not_recieved_valid_input:
            ingredient = str(
                input(
                    "Enter an ingredient (must contain only alphanumeric characters): "
                )
            )
            if len(ingredient) == 0:
                print("Nothing was entered. Please try again.")
            elif not (ingredient.isalnum()):
                print(
                    "Ingredient must contain only alphanumeric characters. Please try again."
                )
            else:
                has_not_recieved_valid_input = False
        ingredients.append(ingredient)
    # Convert ingredients list to a string where each ingredient is separated by a ,
    ingredients_string = ", ".join(ingredients)

    # Create a new Recipe object based on the input from the user
    recipe_entry = Recipe(
        name=name, cooking_time=int(cooking_time), ingredients=ingredients_string
    )

    # Calculate the difficulty
    recipe_entry.calc_difficulty()

    # Add this recipe entry to the database and commit the change
    session.add(recipe_entry)
    session.commit()


def view_all_recipes():
    all_recipes = session.query(Recipe).all()
    if len(all_recipes) > 0:
        for recipe in all_recipes:
            print(recipe)

    else:
        print("There are no recipes stored in the database.")


def search_by_ingredients():
    if session.query(Recipe).count() > 0:
        results = session.query(Recipe.ingredients).all()
        all_ingredients = []

        # for every recipe's ingredients...
        for entry in results:
            # split the string into a temp list
            temp_ingredients = entry.split(", ")
            # for each ingredient in the temp list...
            for ingredient in temp_ingredients:
                # if it's not already in all_ingredients list...
                if not (ingredient in all_ingredients):
                    # add it to all ingredients list
                    all_ingredients.append(ingredient)

        has_not_recieved_valid_input = True
        input_list = []
        while has_not_recieved_valid_input:
            # Display all the ingredients
            print("Ingredients Available Across All Recipes")
            print("----------------------------------------")
            for index, ingredient in enumerate(all_ingredients):
                print(f"{index + 1}. {ingredient}")

            print("By which ingredients would you like to search for recipes?")
            input_str = str(
                input(
                    "Enter numbers from the above list representing the ingredients to be searched separated by spaces: "
                )
            )
            input_list = input_str.split()
            num_ingredients = len(all_ingredients)
            has_not_recieved_valid_input = False
            for i in input_list:
                if i not in range(1, num_ingredients):
                    has_not_recieved_valid_input = True

            if has_not_recieved_valid_input:
                print("Invalid input. Please try again.")

        search_ingredients = []
        for i in input_list:
            search_ingredients.append(all_ingredients[i - 1])

        conditions = []
        for i in search_ingredients:
            like_term = f"%{i}%"
            conditions.append(Recipe.ingredients.like(like_term))

        searched_recipes = session.query(Recipe).filter(*conditions).all()
        for recipe in searched_recipes:
            print(recipe)

    else:
        print("There are no recipes stored in the database.")


def edit_recipe():
    if session.query(Recipe).count() > 0:
        results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()

        has_not_recieved_valid_input = True
        while has_not_recieved_valid_input:
            print("Recipes")
            print("-------")
            for i in results:
                print(f"{i[0]}. {i[1]}")

            print("Which recipe would you like to edit?")
            input_id = int(
                input(
                    "Enter a number from the above list corresponding to the recipe: "
                )
            )
            if input_id in range(1, len(results)):
                has_not_recieved_valid_input = False
            else:
                print("Invalid input. Please try again.")

        recipe_to_edit = session.query(Recipe).get(input_id)

        has_not_recieved_valid_input = True
        while has_not_recieved_valid_input:
            print("What attribute would you like to edit?")
            print(f"1. Name: {recipe_to_edit.name}")
            print(f"2. Ingredients: {recipe_to_edit.ingredients}")
            print(f"3. Cooking time: {recipe_to_edit.cooking_time}")
            input_num = int(input("Enter a number 1-3 corresponding to an attribute: "))

            if input_num in range(1, 3):
                has_not_recieved_valid_input = False
            else:
                print("Invalid input. Please try again.")

        if input_num == 1:
            # Get recipe name from user with max 50 alphanumeric characters
            has_not_recieved_valid_input = True
            while has_not_recieved_valid_input:
                name = str(
                    input(
                        "Enter the name of the recipe(max 50 alphanumeric characters): "
                    )
                )
                if len(name) == 0:
                    print("Nothing was entered. Please try again.")
                elif len(name) > 50:
                    print("Name is too long. Max of 50 characters. Please try again.")
                elif not (name.isalnum()):
                    print(
                        "Name must contain only alphanumeric characters. Please try again."
                    )
                else:
                    has_not_recieved_valid_input = False

            recipe_to_edit.name = name

        elif input_num == 2:
            # Get recipe ingredients from user
            ingredients = []
            # Get the number of ingredients
            has_not_recieved_valid_input = True
            while has_not_recieved_valid_input:
                num_ingredients = int(
                    input(
                        "How many ingredients would you like to enter? Enter a number greater than 0: "
                    )
                )
                if num_ingredients <= 0:
                    print("You must enter more than 0 ingredients. Please try again.")
                elif not (num_ingredients.isnumeric()):
                    print("You must enter a numer. Please try again.")
                else:
                    has_not_recieved_valid_input = False
            # Get each ingredient
            for i in range(num_ingredients):
                has_not_recieved_valid_input = True
                while has_not_recieved_valid_input:
                    ingredient = str(
                        input(
                            "Enter an ingredient (must contain only alphanumeric characters): "
                        )
                    )
                    if len(ingredient) == 0:
                        print("Nothing was entered. Please try again.")
                    elif not (ingredient.isalnum()):
                        print(
                            "Ingredient must contain only alphanumeric characters. Please try again."
                        )
                    else:
                        has_not_recieved_valid_input = False
                ingredients.append(ingredient)
            # Convert ingredients list to a string where each ingredient is separated by a ,
            ingredients_string = ingredients.join(", ")

            recipe_to_edit.ingredients = ingredients_string
            recipe_to_edit.calc_difficulty()

        elif input_num == 3:
            # Get recipe cooking time from user - must be a number greater than 0
            has_not_recieved_valid_input = True
            while has_not_recieved_valid_input:
                cooking_time = int(
                    input("Enter the cooking time of the recipe in minutes: ")
                )
                if cooking_time <= 0:
                    print(
                        "Cooking time must be greater than 0 minutes. Please try again."
                    )
                elif not (cooking_time.isnumeric()):
                    print("Cooking time must be a number. Please try again.")
                else:
                    has_not_recieved_valid_input = False

            recipe_to_edit.cooking_time = cooking_time
            recipe_to_edit.calc_difficulty()

        session.commit()
    else:
        print("There are no recipes stored in the database.")


def delete_recipe():
    if session.query(Recipe).count() > 0:
        results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()

        has_not_recieved_valid_input = True
        while has_not_recieved_valid_input:
            print("Recipes")
            print("-------")
            for i in results:
                print(f"{i[0]}. {i[1]}")

            print("Which recipe would you like to delete?")
            input_id = int(
                input(
                    "Enter a number from the above list corresponding to the recipe: "
                )
            )
            if input_id in range(1, len(results)):
                has_not_recieved_valid_input = False
            else:
                print("Invalid input. Please try again.")

        recipe_to_delete = session.query(Recipe).get(input_id)
        print(recipe_to_delete)
        print("Are you sure you would like to delete this recipe?")
        input_y = str(input("Enter 'y' for YES: "))

        if input_y == "y":
            session.delete(recipe_to_delete)
            session.commit()

    else:
        print("There are no recipes stored in the database.")


def main_menu():
    choice = 0
    while choice != "quit":
        print(
            "What would you like to do? Enter a number for the corresponding option. 1-5"
        )
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for a recipe by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit the program")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_recipe()

        elif choice == "2":
            view_all_recipes()

        elif choice == "3":
            search_by_ingredients()

        elif choice == "4":
            edit_recipe()

        elif choice == "5":
            delete_recipe()

        elif choice != "quit":
            print("Not a valid option. Please try again.")

    session.close()
    engine.dispose()


main_menu()
