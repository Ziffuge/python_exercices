
suite = input("Suite arithmétique ou géométrique ? ")
u1 = float(input("Quelle est la valeur du premier terme ? "))
r = float(input("Que vaut la raison de cette suite ? "))
n = int(input("Quel est l'indice du nième terme ? "))

if suite == "arithmétique" or suite == "suite arithmétique":
    un = u1 + (n - 1)*r
    somme = (n / 2) * (u1 + un)
    print("La somme des {} premiers termes de cette suite est {}".format(n, somme))
elif suite == "géométrique" or suite == "suite géométrique":
    un = u1 * r**(n - 1)
    somme = u1 * (1 - r**n)/(1 - r)
    print("La somme des {} premiers termes de cette suite est {}".format(n, somme))
else:
    print("Il y a eu une erreur avec le type de suite entré.")
