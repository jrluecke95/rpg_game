from hero import Hero
from goblin import Goblin
from zombie import Zombie
from shadow import Shadow
from wizard import Wizard
from dragon import Dragon

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""

def main():
    my_hero = Hero()
    # goblin = Goblin()
    zombie = Zombie()
    shadow = Shadow()

    while my_hero.alive() and shadow.alive():
        print(my_hero)
        print(shadow)
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            my_hero.attack(shadow)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)
        if shadow.health > 0:
            shadow.attack(my_hero)

    print("Uh oh! A zombie has appeared!\n")

    while shadow.alive() == False and my_hero.alive() == True:
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
