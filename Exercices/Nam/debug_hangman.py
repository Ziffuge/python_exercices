
import random
import os
from file_manipulation import add
from file_manipulation import random_word_choice

game = True
start = False

while game == True:
    if start == False:
        choice = input("Voulez-vous choisir le mot ou jouer avec un mot aléatoire ? ")
        if choice == "mot choisi" or choice == "choisir" or choice == "choisir le mot":
            word = input("Choisissez le mot à faire deviner : ")
            add(word)
        elif choice == "aléatoire" or choice == "mot aléatoire":
            word = random_word_choice()
        word_to_guess = list(word)
        guess = []
        for letter in word_to_guess:
            guess.append("-")
        letters_tried = []
        remaining_errors = 6
        start = True
    print("Voici les lettres que vous avez déjà essayé :", letters_tried)
    print(guess)
    trial = input("Quelle lettre essayez-vous ? ")
    letters_tried.append(trial)
    good_trial = False
    i = 0
    for letter in word_to_guess:
        if letter == trial:
            guess.insert(i, trial)
            del guess[i+1]
            good_trial = True
        i += 1
    if good_trial == False:
        remaining_errors -= 1
    if remaining_errors == 0:
        print("Game Over")
        game = False
    elif guess == word_to_guess:
        print("Bien joué, vous avez gagné !!")
        print("Le mot à deviner était :", word_to_guess)
        game = False