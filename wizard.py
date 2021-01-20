from character import Character

class Wizard(Character):
    def __init__(self, health=5, power=10, name='wizard', bounty=10):
        super().__init__(health, power, name)
    
    def attack(self, enemy):
        if self.chance_ten() == True:
            enemy.health -= self.power
            print("the wizard landed a spell.. for once")
        else:
            print("the wizard is new to combat.. he missed his attack")