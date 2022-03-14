# --|Import
# -|Import Classes
from Player.Player import Player


class Warrior(Player):
    def __init__(self, name, desc):
        super().__init__(name, desc, type="Warrior", hp=155,
                         max_hp=155, armor=50, damage=35, score=0)
