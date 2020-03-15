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
