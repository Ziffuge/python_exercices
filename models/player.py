

class Player:
    
    def __init__(self, pseudo, health, attack_damage):
        self.pseudo = pseudo
        self.health = health
        self.attack_damage = attack_damage
        self.weapon = None
        print("Bienvenue au joueur", pseudo, "/ Points de vie maximum :", health, "/ Points d'attaque :", attack_damage)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health
    
    def get_attack_damage(self):
        return self.attack_damage

    def damage(self, damage):
        self.health -= damage
        print("Aie... vous avez subit {} dégâts".format(damage))

    def attack_player(self, target_player):
        damage = self.attack_damage

        if self.has_weapon():
            damage += self.weapon.get_bonus_attack()

        target_player.damage(damage)

    def set_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        return self.weapon is not None