import Player


class Ranger(Player):
    def __init__(self, name, desc):
        super().__init__(name, desc, type = "Ranger",  hp= 60, armor =30, damage = 90)
        self.range = 90
