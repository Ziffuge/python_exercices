
sentence = list(input("Entrez votre phrase/texte : "))
uppercase_counter = 0
lowercase_counter = 0

for letters in sentence:
    if letters.isupper() == True:
        uppercase_counter += 1
    elif letters.islower() == True:
        lowercase_counter += 1

print("Majuscules :", uppercase_counter, "| Minuscules :", lowercase_counter)