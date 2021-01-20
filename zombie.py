from character import Character

class Zombie(Character):
    def __init__(self, health=0, power=1, name="zombie"):
        super().__init__(health, power, name)
    
    def alive(self):
        if self.health <= 0:
            return True
        else:
            return True