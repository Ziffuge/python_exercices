class Player:
    
    def __init__(self, pseudo, health, attack_damage):
        self.pseudo = pseudo
        self.health = health
        self.attack_damage = attack_damage
        print("Bienvenue au joueur", pseudo, "/ Points de vie maximum :", health, "/ Points d'attaque :", attack_damage)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health
    
    def get_attack_damage(self):
        return self.attack_damage

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.attack_damage)


class Warrior(Player):
    
    def __init__(self, pseudo, health, attack_damage):
        super().__init__(pseudo, health, attack_damage)
        self.armor = 3
        print("Bienvenue au guerrier", pseudo, "/ Points de vie maximum :", health, "/ Points d'attaque :", attack_damage)

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0

        super().damage(damage)

    def rest(self):
        self.armor = 3

    def get_armor_point(self):
        return self.armor


player1 = Player("Ziffuge", 20, 3)
player1.damage(3)

warrior = Warrior("DesArmory", 25, 3)
warrior.damage(12)
print("Points de vie :", warrior.get_health(), "Armure :", warrior.get_armor_point())

if issubclass(Warrior, Player):
    print("Guerrier est bien une spécialisation de Player")