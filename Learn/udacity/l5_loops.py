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

while i != 10:
    i = i + 1
    print(i)

# The code below will run forever
i = 1
while i != 10:
    i = i + 2
    print(i)
