import random

from Player import Player


class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.armor = 50
        self.damage = 30

    def attack(self, player):
        player.hp -= self.damage

    def is_dead(self):
        return self.hp <= 0
