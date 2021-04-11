
import os
import random

if os.path.exists('meals.txt'):
    with open('meals.txt', "r+") as file:
        meals_list = file.readlines()
        random_meal_choice = random.choice(meals_list)
        print("Je vous propose aujourd'hui de manger :", random_meal_choice)
        file.close()
else:
    print("Le document n'existe pas ! Veuillez vérifier son nom")
