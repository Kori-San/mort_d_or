# --|Import
# -|Import Classes
from Player.Player import Player


class Ranger(Player):
    def __init__(self, name, desc):
        super().__init__(name, desc, type="Ranger",  hp=130,
                         max_hp=130, armor=30, damage=80, score=0)
