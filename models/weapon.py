
class Weapon:

    def __init__(self, name, bonus_attack):
        self.name = name
        self.bonus_attack = bonus_attack

    def get_name(self):
        return self.name
    
    def get_bonus_attack(self):
        return self.bonus_attack