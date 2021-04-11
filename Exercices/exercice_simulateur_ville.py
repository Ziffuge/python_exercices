
class Building:

    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors
        print("Un nouveau batîment a été construit à l'adresse :", address, "/ Nom :", name)

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_num_floors(self):
        return self.floors

    def rename(self, new_name):
        self.name = new_name
        print("Ce batîment se nomme maintenant :", new_name)


class Block_of_flat(Building):

    def __init__(self, name, address, floors):
        super().__init__(name, address, floors)
        self.number_flats = floors * 4
        self.free_apartements = self.number_flats
        print("Sa fonction : Immeuble à appartements", "/ Son nombre d'appartements :", self.number_flats)
    
    def get_num_flats(self):
        return self.number_flats

    def get_num_free_apartements(self):
        return self.free_apartements

    def move_in(self):
        if self.free_apartements <= 0:
            print("Vous ne pouvez pas emménager, il n'y a plus d'appartements disponnibles.")
        else:
            self.free_apartements -= 1
            print("Vous avez bien emménagé dans cet immeuble.")


class Supermarket(Building):

    def __init__(self, name, address, floors, type_of_products):
        super().__init__(name, address, floors)
        self.floors = 1
        self.type_of_products = type_of_products
        print("Sa fonction : Magasin de", type_of_products)

    def get_type_of_products(self):
        return self.type_of_products

    def buy_something(self, product, number):
        print("Vous avez acheté", number, product)


class Bank(Building):

    def __init__(self, name, address, floors, level_of_security):
        super().__init__(name, address, floors)
        self.level_of_security = level_of_security

    def get_level_of_security(self):
        if self.level_of_security < 1:
            print("Erreur")
        elif 1 <= self.level_of_security < 10:
            print("Cette banque est peu sécurisée")
        elif 10 <= self.level_of_security < 20:
            print("Cette banque est relativement bien sécurisée")
        elif self.level_of_security >= 20:
            print("Cette banque est parfaitement sécurisée !")


immeuble1 = Block_of_flat("Miami's Sun", "Avenue de la Plage, 13, Miami", 7)
immeuble1.move_in()

immeubble2 = Block_of_flat("Le vent d'Est", "Rue du moulin, 2, Miami", 3)

immeuble3 = Block_of_flat("Chez Roger", "Avenue du Centre, 45, Miami", 5)

immeuble4 = Block_of_flat("Miami's Hotel", "Avenue du Centre, 29, Miami", 8)

supermarché1 = Supermarket("Delhaize", "Rue du Moulin, 7, Miami", 1, "Achats quotidiens")

supermarché2 = Supermarket("Carrefour", "Avenue de la Plage, 67, Miami", 2, "Achats quotidiens")
supermarché2.buy_something("Pain", 3)

banque1 = Bank("Banque centrale", "Rue du Couvent, 3", 2, 14)
banque1.get_level_of_security()
