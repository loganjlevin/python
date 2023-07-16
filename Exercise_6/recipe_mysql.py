import mysql.connector

conn = mysql.connector.connect(host="localhost", user="logan", passwd="logan")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Recipes(
    id              INT PRIMARY KEY AUTO_INCREMENT, 
    name            VARCHAR(50),
    ingredients     VARCHAR(255),
    cooking_time    INT,
    difficulty      VARCHAR(20)
    )"""
)


def calc_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients.split(", "))
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"

    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"

    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"

    else:
        difficulty = "Hard"

    return difficulty


def create_recipe(conn, cursor):
    name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = str(input("Enter the ingredients separated by ', ': "))
    difficulty = calc_difficulty(cooking_time, ingredients)

    sql = f"""INSERT INTO Recipes (
            name, ingredients, cooking_time, difficulty
    ) VALUES (
        '{name}', '{ingredients}', {cooking_time}, '{difficulty}'
    )"""

    cursor.execute(sql)
    conn.commit()


def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    all_ingredients = []

    for row in results:
        ingredients = row[0].split(", ")
        for i in ingredients:
            if not (i in all_ingredients):
                all_ingredients.append(i)

    print("Ingredients Available Across All Recipes")
    print("----------------------------------------")

    for index, ingredient in enumerate(all_ingredients):
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
        search_ingredient = all_ingredients[index]

    except:
        print("This input is invalid.")

    else:
        sql = f"""SELECT name, ingredients, cooking_time, difficulty
             FROM Recipes WHERE ingredients LIKE '%{search_ingredient}%'"""
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print("Recipe:", row[0])
            print("Cooking Time (min):", row[2])
            print("Ingredients:")
            ingredients = row[1].split(", ")
            for ingredient in ingredients:
                print(ingredient)
            print("Difficulty level: ", row[3], "\n")


def update_recipe(conn, cursor):
    sql = "SELECT id, name FROM Recipes"

    cursor.execute(sql)
    results = cursor.fetchall()
    print("Names of all Recipes in the Database")
    print("------------------------------------")
    for row in results:
        print(f"{row[0]}. {row[1]}")

    id = 0
    while not (id > 0 and id <= len(results)):
        id = int(
            input(
                "Enter a number from the above list representing the recipe to be updated: "
            )
        )

    column = 0
    while not (column > 0 and column <= 3):
        column = int(
            input(
                "What would you like to modify? \n1. Name \n2. Cooking Time \n3. Ingredients\nEnter a number 1-3: "
            )
        )

    value = 0
    if column == 1:
        value = str(input("Enter the new name of the recipe: "))
        column = "name"
    elif column == 2:
        value = int(input("Enter the new cooking time in minutes: "))
        column = "cooking_time"
    elif column == 3:
        value = str(input("Enter the new list of ingredients separated by ', ': "))
        column = "ingredients"

    if column == "cooking_time":
        sql = f"UPDATE Recipes SET {column} = {value} WHERE id = {id}"
    else:
        sql = f"UPDATE Recipes SET {column} = '{value}' WHERE id = {id}"
    cursor.execute(sql)

    if column != "name":
        sql = f"SELECT cooking_time, ingredients FROM Recipes WHERE id = {id}"
        cursor.execute(sql)
        results = cursor.fetchall()

        cooking_time = int(results[0][0])
        ingredients = results[0][1]
        difficulty = calc_difficulty(cooking_time, ingredients)

        sql = f"UPDATE Recipes SET difficulty = '{difficulty}' WHERE id = {id}"
        cursor.execute(sql)

    conn.commit()


def delete_recipe(conn, cursor):
    sql = "SELECT id, name FROM Recipes"

    cursor.execute(sql)
    results = cursor.fetchall()
    print("Names of all Recipes in the Database")
    print("------------------------------------")
    for row in results:
        print(f"{row[0]}. {row[1]}")

    id = 0
    while not (id > 0 and id <= len(results)):
        id = int(
            input(
                "Enter a number from the above list representing the recipe to be deleted: "
            )
        )

    sql = f"DELETE FROM Recipes WHERE id = {id}"
    cursor.execute(sql)
    conn.commit()


def main_menu(conn, cursor):
    choice = 0
    while choice != "quit":
        print("What would you like to do? Enter a number for the corresponding option.")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)

        elif choice == "2":
            search_recipe(conn, cursor)

        elif choice == "3":
            update_recipe(conn, cursor)

        elif choice == "4":
            delete_recipe(conn, cursor)

        elif choice != "quit":
            print("Not a valid option. Please choose again")

    conn.commit()

    conn.close()


main_menu(conn, cursor)
