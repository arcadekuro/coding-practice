"""Define a procedure is_friend, that takes a string as its input,
 and outputs a Boolean.
indicating if the input string is the name of a friend.
Assume I am friends with everyone whopse name starts with either D or N,
but no one else.
"""


def is_friend(name):
    if name[0] == 'D' or name[0] == 'N':
        return True


# Uncomment code below to test the function works
# print(is_friend('Diane'))
# print(is_friend('Nadine'))

# print(True or False)
# print(False or True)
# print(True or True)
# print(False or False)

""" The or function only evaluates what it needs to.
The below output will give True but printing the variable itself
will give an error.
the code only needs to evaluate the first operand.
"""
print(True or this_is_an_error)

"""
Define a procedure, biggest, that takes three
numbers as inputs and returns the largest of
those three numbers.
"""

# My try of doing it.

"""
def biggest(a, b, c):
    if a > b or c > b or c > a:
        print(a or b or c)
        return
"""

def biggest(a, b, c):
    if a > b:
        if a > c:
            return a
        else: 
            return c
    else:
        if b > c:
            return b
        else:
            return c
# The code is too cluttered and confusing.
# We can use the bigger statement instead or max


def bigger(a, b):
    if a > b:
        return a
    else:
        return b


def the_biggest(a, b, c):
    return bigger(bigger(a, b), c)


print(bigger(10, 20))


print(the_biggest(3, 6, 9))


# >>> 9

# print biggest(6, 9, 3)
# >>> 9

# print biggest(9, 3, 6)
# >>> 9

# print biggest(3, 3, 9)
# >>> 9

# print biggest(9, 3, 9)
# >>> 9

