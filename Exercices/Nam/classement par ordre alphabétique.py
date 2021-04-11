
words_list = input("Veuillez bien écrire votre liste de mot selon ce pattern (word1,word2,word3,...): ").split(",")

sorted_list = sorted(words_list)

print(sorted_list)
print("Attention, les mots commençant par une majuscule sont placés avant les autres mots.")