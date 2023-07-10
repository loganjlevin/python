# Introduction to Python

Career Foundry's Python for Web Developers Introduction to Python course.

## Table of Contents

[Exercise 1: Getting Started with Python](#getting-started-with-python)

[Exercise 2: Data Types in Python](#data-types-in-python)

# Getting Started with Python

## Table of Contents

[Install Python](#install-python)

[Set up a virtual environment](#set-up-a-virtual-environment)

[Install Visual Studio Code](#install-visual-studio-code)

[Set up an IPython shell](#set-up-an-ipython-shell)

[Export a requirements file](#export-a-requirements-file)

---

## Install Python

Install [Python 3.8.7](https://www.python.org/downloads/release/python-387/) on your system if you haven’t already. Make sure that you’re able to access the correct Python installation from your terminal and check that it’s running the correct version by using the python --version command.

![Step 1](./Exercise_1/Step1.PNG)

---

## Set up a virtual environment

Set up a new virtual environment and name it “cf-python-base”.

![Step 2](./Exercise_1/Step2.PNG)

---

## Install Visual Studio Code

Install [Visual Studio Code](https://code.visualstudio.com/download) or another text editor of your choice and make a script called “add.py” that adds two numbers that the user enters.

- Input from a user can be stored into a variable with the following syntax (don’t include < and > in your code): variable_name = int(input("<any prompt you'd like to give to the user>")).
- Store two values a and b from the user and add them to a variable c.
- Finally, print the value of c to the screen. The print() function can be used to print variable values with the following syntax: print(<variable name>).

![Step 3](./Exercise_1/Step3.PNG)

```python
# Prompt the user to enter the first number
a = int(input("Enter the first number: "))

# Prompt the use to enter the second number
b = int(input("Enter the second number: "))

# Add the two numbers and store them in variable c
c = a + b

# Print the value of c
print("The sum of ", a, "and", b, "is: ", c)

```

---

## Set up an IPython shell

Set up an IPython shell in the virtual environment “cf-python-base”. An IPython shell is similar to the regular Python REPL that you saw earlier but with additional features such as syntax highlighting, auto-indentation and robust auto-complete features. The name of the package to be installed is “ipython,” which is available for install via pip. Verify your installation by launching an IPython shell with the command ipython.

![Step 4](./Exercise_1/Step4.PNG)

---

## Export a requirements file

The requirements file is a text file that lists package requirements for any particular Python application. For example, it can specify that bcrypt 3.2.0 and ipython 7.20.0 need to be installed in order for your Python scripts to run. The requirements file also helps when you’d like to run your Python script on another system. Simply provide your scripts and the “requirements.txt” file, and pip can then automatically install the required packages in another environment by simply referring to your requirements file. Your script can then run in that environment without any unexpected errors.

- First, generate a “requirements.txt” file from your source environment. To do this, you use the pip freeze command and all packages (including version numbers) installed in the currently activated environment will be compiled: > pip freeze > requirements.txt.
- Next, create a new environment called “cf-python-copy”. In this new environment, install packages from the “requirements.txt” file that you generated earlier. To install the packages from this file in any other environment, you run the pip install command with the extra -r argument, followed by the name of your requirements file: > pip install -r requirements.txt.

![Step 5](./Exercise_1/Step5.PNG)

---

# Data Types in Python

## Table of Contents

[Create a Structure](#create-a-structure)

[First Recipe](#first-recipe)

[Create an Outer Structure](#create-an-outer-structure)

[Generate More Recipes](#generate-more-recipes)

[Print the Ingredients](#print-the-ingredients)

---

## Create a structure

Create a structure named recipe_1 that contains the following keys:

- name (str): Contains the name of the recipe
- cooking_time (int): Contains the cooking time in minutes
- ingredients (list): Contains a number of ingredients, each of the str data type

Decide what data structure you would use for this purpose, and in your README file in the repository for this task, describe in approx. 50-75 words why you’ve chosen to use it.

I would use the dictionary data type for creating a recipe because you can associate the keys name, cooking_time, ingredients, each with a different data type and the key names indicate what the values are meant to represent. When using the dictionary data structure the code will be more descriptive. For example if we used a list we would have recipe_1[0] to access the name instead of recipe_1['name']. It is much easier to understand what is going on in the code when using a dictionary.

## First Recipe

The recipe_1 structure that you create will be for a cup of tea, with the following attributes:

- Name: Tea
- Cooking time: 5 minutes
- Ingredients: Tea leaves, Sugar, Water

![Step2](./Exercise_2/Step2.PNG)

## Create an Outer Structure

Create an outer structure called all_recipes, and then add recipe_1 to it. Figure out what type of structure you would consider for all_recipes, and briefly note down your justification in the README file. Ideally, this outer structure should be sequential in nature, where multiple recipes can be stored and modified as required.

For the outer structure all_recipes I will use a list because it is sequential in nature and I can easily add, remove, and modify items as needed.

![Step3](./Exercise_2/Step3.PNG)

## Generate More Recipes

You can make your own recipes too! Generate 4 more recipes as recipe_2, recipe_3, recipe_4, and recipe_5, and then add them as well to all_recipes.

![Step4](./Exercise_2/Step4.PNG)

## Print the Ingredients

Once you’re done setting up all_recipes, print the ingredients of each recipe as five different lists, inside the IPython shell.

![Step5](./Exercise_2/Step5.PNG)
