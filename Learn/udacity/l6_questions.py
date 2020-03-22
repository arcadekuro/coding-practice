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