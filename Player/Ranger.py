import Player


class Ranger(Player):
    def __init__(self, name, desc):
        super().__init__(name, desc, type = "Ranger",  hp= 60, armor =30, damage = 90)
        self.range = 90


    def attack(self):
       print(self.damage)

    def talk(self):
        print("Hello, I'm" + self.name + ", I'm a ranger, Here is what talk about me" + self.desc)

