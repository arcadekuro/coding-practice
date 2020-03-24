""" Another input method to pass variables to a script(py file).
when you typye python ex13.py to run the file, the ex13.py part is an "arugment"
"""

# import is how you add features to your script from python feature set.
# Python asks you to say what you plan to use
# This keeps the program small and acts as documentation for others.
from sys import argv

script, first, second, third = argv #argument variable

print("The script is called:", script)
print("Your first variable is:", first)
print("your firsy variable is:", second)
print("your third vartiable is:", third)

# To run this script you will have to run this in command line:
# python3 ex13.py first second third