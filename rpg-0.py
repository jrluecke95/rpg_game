from hero import Hero
from goblin import Goblin
from zombie import Zombie
from shadow import Shadow
from wizard import Wizard
from dragon import Dragon
import random

def main():
    my_hero = Hero()
    goblin = Goblin()
    zombie = Zombie()
    shadow = Shadow()
    wizard = Wizard()
    dragon = Dragon()
    enemies = [goblin, zombie, shadow, wizard, dragon]

    print("Welcome to the game - good luck fighting your way through the enemies")

    while len(enemies) > 0:
        enemy_num = random.randint(0, len(enemies) - 1)
        enemy = enemies[enemy_num]
        if my_hero.alive() == False:
            break

        while my_hero.alive() and enemy.alive():
            print(my_hero.print_status())
            print(enemy.print_status())
            print()
            print("What do you want to do?")
            print(f"1. fight {enemy.name}")
            print("2. do nothing")
            print("3. flee")
            print("4. run away and enter the shop")
            print("> ",)
            user_input = input()
            if user_input == "1":
                my_hero.attack(enemy)
            elif user_input == "2":
                pass
            elif user_input == "3":
                print(f"Good call. the {enemy.name} is a tough one")
                break
            elif user_input == "4":
                print("welcome to the store! here is our inventory")
                shop = ["Super Tonic", "Armor", "Evade"]
                for item in shop:
                    print(f"{shop.index(item) + 1}: {item}")
                choice = int(input("Enter choice here: "))
                if choice == 1:
                    my_hero.coins -= 5
                    my_hero.health == 10
                elif choice == 2:
                    my_hero.coins -= 3
                    my_hero.get_armor()
                elif choice == 3:
                    my_hero.coins -= 3
                    my_hero.get_evade()

            else:
                print("Invalid input %r" % user_input)
            if enemy.health > 0:
                enemy.attack(my_hero)
            elif enemy.alive() == False:
                print(f"you killed {enemy.name}")
                my_hero.collect_bounty(enemy)
                enemies.pop(enemy_num)



main()
