from character import Character

class Medic(Character):
    def __init__(self, health=10, power=5, name='hero', bounty=6):
        super().__init__(health, power, name, bounty)

    def regen(self):
        if self.chance_twenty() == True:
            self.health += 2
            print("the medic regned 2 health points!")
        else:
            pass
