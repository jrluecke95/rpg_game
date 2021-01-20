from character import Character

# class Goblin(Character):
#     def __init__(self, health=6, power=2, name='goblin'):
#         self.health = health
#         self.power = power
#         self.name = name

class Goblin(Character):
    def __init__(self, health=6, power=2, name='goblin'):
        super().__init__(health, power, name)