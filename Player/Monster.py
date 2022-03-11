from Player.Player import Player


class Monster(Player):
    def __init__(self, name):
        super().__init__(name, desc="Je suis un monstre",  type="Monster", hp=100, armor=50, damage=50)
