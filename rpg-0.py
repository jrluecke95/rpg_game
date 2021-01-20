from hero import Hero
from goblin import Goblin

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    my_hero = Hero()
    my_goblin = Goblin()

    # while my_goblin.health > 0 and my_hero.health > 0:
    while my_hero.alive() and my_goblin.alive():
        # print("You have %d health and %d power." % (my_hero.health, my_hero.power))
        # print("The goblin has %d health and %d power." % (my_goblin.health, my_goblin.power))
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
            # Hero attacks goblin
            my_hero.attack(my_goblin)
            # my_goblin.health -= my_hero.power
            print("You do %d damage to the goblin." % my_hero.power)
            if my_goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if my_goblin.health > 0:
            # Goblin attacks hero
            # my_hero.health -= my_goblin.power
            my_goblin.attack(my_hero)
            print("The goblin does %d damage to you." % my_goblin.power)
            if my_hero.health <= 0:
                print("You are dead.")

main()
