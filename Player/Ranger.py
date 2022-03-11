from Player.Player import Player


class Ranger(Player):
    def __init__(self, name, desc):
        super().__init__(name, desc, type="Ranger",  hp=120, armor=30, damage=70, score=0)
