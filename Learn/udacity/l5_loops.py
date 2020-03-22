# Initialise the variable i

i = 0

# As long as i is less than 10 - evaluates to true & run the block.
# The block prints i and then adds 1 to i

"""
while i < 10:
    print(i)
    i = i + 1
"""

# The below code will stop once the loop reaches 10 because i is equal to 10.
# Prints numbers from 1 - 10

"""
while i != 10:
    i = i + 1
    print(i)
"""
# The code below will run forever


# while i != 10:
#     i = i + 2
#     print(i)

"""
# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.
"""


def print_numbers(n):
    i = 0
    while i < n:
        i = i + 1
        print(i)


print_numbers(3)

# Another method is:


def print_numbers2(n):
    i = 1
    while i <= n:
        print(i)
        i = i + 1
