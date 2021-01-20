class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} did {self.power} damage to {enemy.name}")
        if enemy.alive() == False:
            print(f"{enemy.name} is dead!")
    
    def __str__(self):
        return f"""
        {self.name} has {self.health} health and {self.power}"""

