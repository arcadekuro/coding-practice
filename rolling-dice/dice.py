import random


def roll(sides):
    """ random.randint takes the random module and returns ranfom integers.
    1 is the lower interger and sides is the higher integer,
    This will return an integer between 1 and six. We then return the value
    assigned to num_rolled
    to whever it is called. I.e the main function """
    num_rolled = random.randint(1, sides)
    return num_rolled


def equals_total(num_rolled1, num_rolled2, total):
    if num_rolled1 + num_rolled2 == total:
        print("You win!")


def equals_exact(num_rolled1, exact):
    if num_rolled1 == exact:
        print("You win!")
    else:
        print("You Lose, sorry :(")


def equals_subtract(num_rolled, exact):
    if exact - 1:
        print


def main():
    exact = input("Choose a number: ")
    num_rolled1 = roll(3)
    print("You rolled a", num_rolled1)
    equals_exact(num_rolled1, int(exact))


main()

"""
Homework to be completed: for next session.
Harcode dice sides. After every roll take numb away from exact.
If exact = 0 - You win!
Can use a variable assigned to another variable exact = exact -1
Make a game function where each time user roles the dice then
you have three chances to get to 0 from 10?
"""
