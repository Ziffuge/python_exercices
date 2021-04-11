
import random
import os

def add(word):
    j = 0
    with open("word_list.txt", "r+") as file:
        word_list = file.readlines()
        for list_word in word_list:
            if list_word == word + "\n":
                j += 1
        file.close()
    if j == 0:
        with open("word_list.txt", "a+") as file:
            file.write(word + "\n")
            file.close()

def random_word_choice():
    with open("word_list.txt", "r+") as file:
        word_list = file.read().splitlines()
        random_word = random.choice(word_list)
        return random_word