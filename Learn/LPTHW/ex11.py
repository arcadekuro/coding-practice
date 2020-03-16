""" Python's input function handles input from a user
"""

print("How old are you?", )
age = input()
print("How tall are you?",)
height = input()
print("How much do you weigh?")
weight = input()

print("so, you're %r years old, %r tall and %r heavy." % (age, height, weight))

"""
There is another format that you use to handle input
"""
More_questions = input("How about some more questions?")
Favourite_colour = input("What is your favourite colour?")
Favourite_food = input("What is your favourite food?")
Pets_name = input("what is your pets name?")

print("so your favourite food is %r , your favourite colour is %r and you have a pet called %r?" % (Favourite_colour, Favourite_food, Pets_name))
