# --|Import
# -|Import Classes

class Player:
    def __init__(self, name, desc, type, hp, max_hp, armor, damage, score):
        self.name = name
        self.desc = desc
        self.type = type
        self.hp = hp
        self.max_hp = max_hp
        self.armor = armor
        self.damage = damage
        self.score = score

    def attack(self, enemy):
        mitigation = (self.damage - ((enemy.armor / 100) * self.damage))
        print(self.name, "-|===", enemy.name, "( -", mitigation, ")")
        enemy.hp -= mitigation
        if enemy.hp < 0:
            enemy.hp = 0
        print(enemy.name, ": [", enemy.hp, "HP ]")
        print(self.name, ": [", self.hp, "HP ]\n")

    def heal(self):
        if self.max_hp != self.hp:
            heal_val = (10/100)*self.max_hp
            self.hp += heal_val
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(">", self.name, ":", self.hp - heal_val,
                  "<3", self.hp, "( +", heal_val, ")\n")

    def talk(self):
        print("-| Name:", self.name, "\n   Class:", self.type)
        print("   Description:", self.desc, "\n")

    def isDead(self, enemy):
        if self.hp <= 0:
            print("[", self.name, "is dead ]")
            enemy.score = enemy.score + self.score
            print(enemy.name, "(X_x)", self.name, "( +", self.score, ")\n")
            return True
        else:
            return False
