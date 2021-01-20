import random

class Character:
    def __init__(self, health, power, name, bounty=5, armor=0):
        self.health = health
        self.power = power
        self.name = name
        self.bounty = bounty
        self.armor = armor
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        net_damage = self.power - enemy.armor
        enemy.health -= net_damage
        print(f"{self.name} did {net_damage} damage to {enemy.name}")
        if enemy.alive() == False:
            print(f"{enemy.name} is dead!")
    
    def print_status(self):
        return(print(f"""
        {self.name} has {self.health} health and {self.power}"""))

    def chance_twenty(self):
        num = random.randint(1, 5)
        if num == 1:
            return True
        else:
            return False
    
    def chance_ten(self):
        num = random.randint(1, 10)
        if num == 1:
            return True
        else:
            return False

