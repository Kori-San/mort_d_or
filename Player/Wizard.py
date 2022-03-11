from Player.Player import Player


class Wizard(Player):
    def __init__(self, name, desc):
        super().__init__(name, desc, type="Wizard", hp=50, armor=20, damage=80)
