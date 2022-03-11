from Player.Player import Player
from random import randrange, randint


class Monster(Player):
    def __init__(self, name):
        super().__init__(name, desc="Je suis un monstre",
                         type="Monster", hp=50, armor=50, damage=50, score=1)
        self.sprite = ""

    def generate(self):
        Monster_Rand = randrange(0, 101)
        if Monster_Rand <= 10:
            self.sprite = "graphics/battle/monster/bat.png"
            self.name = "Bat"
            self.hp = 40
            self.damage = 20
            self.score += 2
        elif 10 < Monster_Rand <= 20:
            self.sprite = "graphics/battle/monster/rat.png"
            self.name = "Rat"
            self.hp = 30
            self.damage = 20
            self.score += 2
        elif 20 < Monster_Rand <= 30:
            self.sprite = "graphics/battle/monster/goblins.png"
            self.name = "Goblins"
            self.hp = 50
            self.damage = 40
        elif 30 < Monster_Rand <= 40:
            self.sprite = "graphics/battle/monster/kobold.png"
            self.name = "Kobold"
            self.hp = 60
            self.damage = 50
            self.score += 4
        elif 40 < Monster_Rand <= 50:
            self.sprite = "graphics/battle/monster/skeletton.png"
            self.name = "Skeletton"
            self.hp = 30
            self.damage = 40
            self.score += 4
        elif 50 < Monster_Rand <= 60:
            self.sprite = "graphics/battle/monster/slime.png"
            self.name = "Slime"
            self.hp = 30
            self.damage = 30
            self.score += 2
        elif 60 < Monster_Rand <= 70:
            self.sprite = "graphics/battle/monster/snake.png"
            self.name = "Snake"
            self.hp = 60
            self.score += 2
        elif 70 < Monster_Rand <= 80:
            self.sprite = "graphics/battle/monster/dracoy.png"
            self.name = "Dracoy"
            self.hp = 100
            self.damage = 50
            self.score += 9
        elif 80 < Monster_Rand <= 90:
            self.sprite = "graphics/battle/monster/ghost.png"
            self.name = "Ghost"
            self.hp = 70
            self.damage = 70
            self.score += 6
        elif 90 < Monster_Rand <= 100:
            self.sprite = "graphics/battle/monster/grenouille.png"
            self.name = "Grenouille"
            self.hp = 40
            self.damage = 20
            self.score += 2
