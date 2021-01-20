from character import Character

# class Hero(Character):
#     def __init__(self, health=10, power=5, name='hero'):
#         self.health = health
#         self.power = power
#         self.name = name

class Hero(Character):
    def __init__(self, health=10, power=5, name='hero', bounty=0, coins=0):
        super().__init__(health, power, name)
        self.coins = coins

    def attack(self, enemy):
        if enemy.name == 'shadow' and self.chance_ten() == False:
            print("shadow dodged your attack!")
        elif self.chance_twenty() == True:
            enemy.health -= (self.power * 2)
            print(f"{self.name} did {self.power * 2} damage(double) to {enemy.name}")
        else:
            enemy.health -= self.power
            print(f"{self.name} did {self.power} damage to {enemy.name}")
        