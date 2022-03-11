from Player.Player import Player


class Warrior(Player):
    def __init__(self, name, desc):
        super().__init__(name, desc,  type="Warrior", hp=100, armor=50, damage=50)