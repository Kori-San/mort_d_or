# --|Import
# -|Import Func
from random import randrange

# -|Import Classes

from Player.Player import Player


class Monster(Player):
    def __init__(self, name):
        super().__init__(name, desc="Je suis un monstre",
                         type="Monster", hp=50, max_hp=50, armor=50, damage=50, score=1)
        self.sprite = ""

    def generate(self):
        Monster_Rand = randrange(0, 101)
        if Monster_Rand <= 10:
            self.sprite = "graphics/battle/monster/bat.png"
            self.name = "Bat"
            self.damage = 20
            health = 20
        elif 10 < Monster_Rand <= 20:
            self.sprite = "graphics/battle/monster/rat.png"
            self.name = "Rat"
            self.damage = 20
            health = 20
        elif 20 < Monster_Rand <= 30:
            self.sprite = "graphics/battle/monster/goblins.png"
            self.name = "Goblins"
            self.damage = 60
            health = 60
        elif 30 < Monster_Rand <= 40:
            self.sprite = "graphics/battle/monster/kobold.png"
            self.name = "Kobold"
            self.damage = 70
            health = 70
        elif 40 < Monster_Rand <= 50:
            self.sprite = "graphics/battle/monster/skeletton.png"
            self.name = "Skeletton"
            self.damage = 50
            health = 30
        elif 50 < Monster_Rand <= 60:
            self.sprite = "graphics/battle/monster/slime.png"
            self.name = "Slime"
            self.damage = 30
            health = 30
        elif 60 < Monster_Rand <= 70:
            self.sprite = "graphics/battle/monster/snake.png"
            self.name = "Snake"
            self.damage = 50
            health = 50
        elif 70 < Monster_Rand <= 80:
            self.sprite = "graphics/battle/monster/dracoy.png"
            self.name = "Dracoy"
            self.damage = 50
            health = 100
        elif 80 < Monster_Rand <= 90:
            self.sprite = "graphics/battle/monster/ghost.png"
            self.name = "Ghost"
            self.damage = 70
            health = 70
        elif 90 < Monster_Rand <= 100:
            self.sprite = "graphics/battle/monster/grenouille.png"
            self.name = "Grenouille"
            self.damage = 30
            health = 50
        self.hp = health
        self.max_hp = health
        self.score += (self.max_hp + self.damage)/10
