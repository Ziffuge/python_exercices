
from models.player import Player
from models.weapon import Weapon

player1 = Player("Ziffuge", 20, 2)
player2 = Player("GobUlysse", 15, 6)

knife = Weapon("Couteau", 5)

player1.attack_player(player2)

print(player1.get_pseudo(), "attaque", player2.get_pseudo())
print(player2.get_pseudo(), "a encore", player2.get_health(), "points de vie")

player1.set_weapon(knife)

player1.attack_player(player2)

print(player1.get_pseudo(), "attaque", player2.get_pseudo())
print(player2.get_pseudo(), "a encore", player2.get_health(), "points de vie")