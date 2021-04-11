
def get_vowels_number():
    vowels_counter = 0
    word = list(input("Choisissez un mot : "))
    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
            vowels_counter += 1
        else:
            vowels_counter += 0
    print("Il y a {} voyelle(s) dans ce mot".format(vowels_counter))
    


get_vowels_number()