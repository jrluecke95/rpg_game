from character import Character

class Hero(Character):
    def __init__(self, health=10, power=5, name='hero'):
        self.health = health
        self.power = power
        self.name = name
