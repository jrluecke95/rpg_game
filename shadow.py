from character import Character
import random

class Shadow(Character):
    def __init__(self, health=10, power=1, name='shadow', bounty=15):
        super().__init__(health, power, name, bounty)