from Player import Player


class Wizard(Player):
    def __init__(self, name, desc):
        Player.__init__(self, name, desc, type="Wizard", hp=50, armor=20, damage=80)
