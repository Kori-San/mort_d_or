import random

from Player import Player


class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.armor = 50
        self.damage = 30

    def attack(self, player):
        if self.is_doge():
            return False
        player.hp -= self.damage

    def is_doge(self):
        roll = random.randint(1, 100)
        if roll <= 5:
            return True
        return False
