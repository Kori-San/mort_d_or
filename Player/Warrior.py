from Player import Player


class Warrior:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.type = "Warrior"
        self.hp = 100
        self.armor = 50
        self.damage = 50
    def attack(self, monster):
        monster.hp -= self.damage

    def talk(self):
        return self.desc

    def is_dead(self):
        return self.hp <= 0