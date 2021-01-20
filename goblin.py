from character import Character

class Goblin(Character):
    def __init__(self, health=6, power=2, name='goblin'):
        self.health = health
        self.power = power
        self.name = name