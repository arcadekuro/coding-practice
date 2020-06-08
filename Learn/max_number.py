
def bigger(num1, num2):
    if num1 > num2:
      return num1
    else:
        return num2

# Uncomment these function calls to test your 
def max_num (num1, num2, num3):
  if num1 == num2 or num2 == num3 or num1 == num3:
    return "It's a tie!"
  else:
    return bigger(bigger(num1, num2), num3)

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
#print(max_num(2, 3, 3))
# should print "It's a tie!"
