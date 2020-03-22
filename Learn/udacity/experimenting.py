def stamps(n):
    a, b, c = 0, 0, 0
    while 5 * ( a + 1) <= n:
        a = a + 1
    while 2 * (b + 1 ) <= ( n - 5 * a):
        b = b + 1
    while (c + 1) <= (n - 5 * a - 2 * b):
        c = c + 1
    return (a, b, c)


print(stamps(8))