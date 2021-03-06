""" 1. Define a procedure, udacify, that takes as input a string, 
and outputs a string that is an uppercase 'U'
followed by the input string, 
print udacify('dacians') - Udacians
"""
def udacify1(name):
    return print('U' + name)
    

udacify1('dacians')

# My alternative code was:

def udacify2(name):
    add = 'U'
    new = add + name
    return new

print(udacify2('turn'))
print(udacify2('boat'))


""" Obfuscated Procedures
Which of the following have exactly the 
same behaviour as def proc.

For two procedures to have exactly 
the same behaviour, this means no matter what the inputs are
the caller couldn't tell the diff between the procedures.

In below 'test hasn't been defined. Assume test takes a number
as it;s input and out puts a boolean.
def proc(a,b):
    if test(a):
        return b
    return a 
"""



""" 
Define a procedure, median, that takes three
 numbers as its inputs, and returns the median
 of the three numbers.
 Make sure your procedure has a return statement.

"""

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)
     

print(median(1,2,3))
#>>> 2

#print(median(9,3,6))
#>>> 6

#print(median(7,8,7))
#>>> 7

"""
Define a procedure, countdown, 
that takes a positive whole number as its input, 
and prints out a coundown from that number to 1, followeed by Blast off!
This tests loops
"""

def countdown(n):
    while n > 0: # Define how long we cout down for 
        print(n)
        n = n - 1
        # What do we do after every count
    else: 
        return print('Blastoff!')

countdown(3)

"""
Define a procedure, find_last, that takes as input
two strings, a search string and a target string,
and returns the last position in the search string
where the target string appears, or -1 if there
are no occurrences.
Example: find_last('aaaa', 'a') returns 3
Make sure your procedure has a return statement.
"""

def find_last(search, target):
    last_pos = -1
    while True:
        pos = search.find(target, last_pos + 1)
        if pos == -1:
            return last_pos
        last_pos = pos





print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0

