
conversion_type = input("Voulez-vous conertir vers un nombre binaire ou un nombre décimal ? ")
result = 0
i = 0

if conversion_type == "décimal" or conversion_type == "nombre décimal":
    number = list(input("Veuillez insérer votre nombre : "))
    number.reverse()
    for figure in number:
        figure = int(number[i]) * 2**i
        result += figure
        i += 1
    print("Le résultat est :", result)
elif conversion_type == "binaire" or conversion_type == "nombre binaire":
    number = int(input("Veuillez insérer votre nombre : "))
    result = []
    while number != 0:
        q = number//2
        r = number%2
        number = q
        result.append(r)
    result.reverse()
    print("Le résultat est :", result)
else:
    print("Il y a une erreur lors du choix de la conversion, réessayez en écrivant (décimal ou binaire)")
