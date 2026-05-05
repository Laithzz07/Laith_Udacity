import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def get_input(prompt, valid):
    while True:
        choice = input(prompt)
        if choice in valid:
            return choice
        options = " or ".join(valid)
        print("(Please enter " + options + ".)")


def intro(enemy):
    print_pause("You wake up in a dark forest with no memory"
                " of how you got here.")
    print_pause("The trees are tall and the air smells like danger.")
    print_pause("In front of you: an old wooden cabin.")
    print_pause("To your right: a narrow path leading into the fog.")
    print_pause("Somewhere out there, a " + enemy + " is hunting you.")


def cabin(has_sword, enemy):
    print_pause("You push the cabin door open. It creaks loudly.")
    print_pause("Inside: a dusty table, broken chairs, and a fireplace.")

    if not has_sword:
        print_pause("On the table you spot a rusty sword.")
        choice = get_input(
            "Do you take it?\n1) Yes\n2) Leave it\n> ",
            ["1", "2"]
        )
        if choice == "1":
            print_pause("You grab the sword. It feels heavy but reliable.")
            has_sword = True
        else:
            print_pause("You leave it. Hopefully you won't regret that.")
    else:
        print_pause("Nothing useful here anymore.")

    print_pause("You hear footsteps outside. The " + enemy + " found you!")
    return fight(has_sword, enemy)


def path(has_sword, enemy):
    print_pause("You step into the fog. The path twists and turns.")
    print_pause("After a few minutes, you reach a river.")

    choice = get_input(
        "What do you do?\n1) Cross the river\n2) Follow it upstream\n> ",
        ["1", "2"]
    )

    if choice == "1":
        print_pause("The current is strong. You barely make it across.")
        print_pause("On the other side: a bridge. And under it...")
        print_pause("The " + enemy + " was waiting for you all along.")
        return fight(has_sword, enemy)
    else:
        print_pause("You follow the river and find an old boat.")
        print_pause("You row downstream and escape into the open valley.")
        print_pause("But in the valley, the " + enemy + " blocks your path!")
        return fight(has_sword, enemy)


def fight(has_sword, enemy):
    print_pause("The " + enemy + " roars and charges at you!")

    if has_sword:
        print_pause("You raise your sword and stand your ground.")
        victory_chance = random.randint(1, 10)
        if victory_chance >= 4:
            print_pause("You slash the " + enemy + " and it stumbles back.")
            print_pause("With one final blow, it falls to the ground.")
            return True
        else:
            print_pause("The " + enemy + " is faster than you expected.")
            print_pause("It knocks the sword from your hand. You fall.")
            return False
    else:
        print_pause("You have no weapon. You try to run...")
        escape_chance = random.randint(1, 10)
        if escape_chance >= 7:
            print_pause("You manage to dodge past it and keep running!")
            print_pause("You collapse outside the forest."
                        " You survived... barely.")
            return True
        else:
            print_pause("The " + enemy + " catches you. It's over.")
            return False


def play_game():
    enemies = ["troll", "dark knight", "forest beast", "shadow wraith"]
    enemy = random.choice(enemies)

    has_sword = False

    intro(enemy)

    choice = get_input(
        "\nWhere do you go?\n1) Enter the cabin\n2) Take the path\n> ",
        ["1", "2"]
    )

    if choice == "1":
        won = cabin(has_sword, enemy)
    else:
        won = path(has_sword, enemy)

    print_pause("\n--- GAME OVER ---")
    if won:
        print_pause("You defeated the " + enemy +
                    " and escaped the forest!")
        print_pause("You win!")
    else:
        print_pause("The forest claimed another soul today.")
        print_pause("You lose.")

    again = get_input(
        "\nWould you like to play again? (y/n): ",
        ["y", "n"]
    )
    if again == "y":
        play_game()
    else:
        print("Hope you had fun!")


play_game()