from character import Character

# class Hero(Character):
#     def __init__(self, health=10, power=5, name='hero'):
#         self.health = health
#         self.power = power
#         self.name = name

class Hero(Character):
    def __init__(self, health=10, power=5, name='hero', bounty=0, coins=0, evade=0):
        super().__init__(health, power, name)
        self.coins = coins
        self.evade = evade

    def attack(self, enemy):
        if enemy.name == 'shadow' and self.chance_ten() == False:
            print("shadow dodged your attack!")
        elif self.chance_twenty() == True:
            enemy.health -= (self.power * 2)
            print(f"{self.name} did {self.power * 2} damage(double) to {enemy.name}")
        else:
            enemy.health -= self.power
            print(f"{self.name} did {self.power} damage to {enemy.name}")
    
    def collect_bounty(self, enemy):
        if enemy.health <= 0:
            self.coins += enemy.bounty
            print(f"you have {self.coins} coins now!")
    
    def get_armor(self):
        self.armor += 2
    
    def get_evade(self):
        self.evade += 2
    
    # def evasion(self):
    #     for number in range(self.evade - 1):
    #         if self.chance_ten() == True:
    #             "somehow evade atack"