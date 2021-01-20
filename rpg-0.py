from hero import Hero
from goblin import Goblin
from zombie import Zombie

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    my_hero = Hero()
    my_goblin = Goblin()
    zombie = Zombie()

    while my_hero.alive() and my_goblin.alive():
        print(my_hero)
        print(my_goblin)
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            my_hero.attack(my_goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)
        if my_goblin.health > 0:
            my_goblin.attack(my_hero)

    print("Uh oh! A zombie has appeared!\n")

    while my_goblin.alive() == False and my_hero.alive() == True:
        print(my_hero)
        print(zombie)
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            my_hero.attack(zombie)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)
        if zombie.alive() == True:
            zombie.attack(my_hero)
main()
