class Player:
    def __init__(self, name, desc, type, hp, armor, damage, score):
        self.name = name
        self.desc = desc
        self.type = type
        self.hp = hp
        self.armor = armor
        self.damage = damage
        self.score = score

    def attack(self, enemy):
        mitigation = (self.damage - ((enemy.armor / 100) * self.damage))
        print(self.name, "-|== attack -|==", enemy.name, "(-", mitigation, ")")
        enemy.hp -= mitigation

    def talk(self):
        return self.desc

    def isDead(self):
        return self.hp <= 0
