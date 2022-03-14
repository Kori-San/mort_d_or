# --|Import
# -|Import Classes
from Player.Player import Player


class Wizard(Player):
    def __init__(self, name, desc):
        super().__init__(name, desc, type="Wizard", hp=115,
                         max_hp=115, armor=25, damage=125, score=0)
