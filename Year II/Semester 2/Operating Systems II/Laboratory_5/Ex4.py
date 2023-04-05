import sys

def compute(a, b, c, d):
    if a > 10:
        print('a is too big')
    elif b > 10:
        print('b is too big')
    elif c > 10:
        print('c is too long')
    elif d > 10:
        print('d is too long')
    else:
        multiplication = int(b) * int(c)
        sum = int(a) + int(multiplication) + int(d)
    return "Result: " + str(sum)

try:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    d = int(input('d: '))
    print(compute(a, b, c, d))
except:
    print('Input is not a numeric value')
    sys.exit(1)
