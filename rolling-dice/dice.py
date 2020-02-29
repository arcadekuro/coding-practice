import random


def roll(sides=6):
    """ random.randint takes the random module and returns ranfom integers.
    1 is the lower interger and sides is the higher integer,
    This will return an integer between 1 and six. We then return the value
    assigned to num_rolled
    to whever it is called. I.e the main function """
    num_rolled = random.randint(1, sides)
    return num_rolled


def is_six_or_three(num_rolled):
    if num_rolled == 6 or num_rolled == 3:
        print("You lose!")


def is_ten(num_rolled1, num_rolled2):
    if num_rolled1 + num_rolled2 == 10:
        print("You win!")


def main():
    num_rolled1 = roll(6)
    num_rolled2 = roll(6)
    print("You rolled a", num_rolled1, num_rolled2)
    is_ten(num_rolled1, num_rolled2)


main()
