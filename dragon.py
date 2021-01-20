from character import Character

class Dragon(Character):
    def __init__(self, health=50, power=5, name='dragon', bounty=50):
        super().__init__(health, power, name, bounty)
    
    def flames(self, enemy):
        enemy.health -= self.power
    
    def bite(self, enemy):
        enemy.health = 0
    
    def attack(self, enemy):
        if self.chance_ten == True:
            print("the dragon breathed fire on you!")
            self.flames(enemy)
        elif self.chance_twenty == True:
            print("you have been eaten")
            self.bite(enemy)
        else:
            print("the dragon circles above")
        
