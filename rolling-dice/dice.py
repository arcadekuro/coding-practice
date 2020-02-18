import random


def roll(sides=6):
    """ random.randint takes the random module and returns ranfom integers.
    1 is the lower interger and sides is the higher integer,
    This will return an integer between 1 and six. We then return the value
    assigned to num_rolled
    to whever it is called. I.e the main function """
    num_rolled = random.randint(1, sides)
    return num_rolled


def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? ENTER=Roll. Q=Quit. ")
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
        else:
            rolling = False

    print("Thanks for playing!")


main()
