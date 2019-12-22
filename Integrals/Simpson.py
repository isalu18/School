import math
#import numpy as np

def f(x):
    return x * math.log(x)

def f2(x):
    return x**3

#Simpson 1/3
def simpson(a, b, n, f):

    res = f(a) + f(b)
    h = (b - a) / n

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            res = res + (2 * f(x))
            print(res)
        else:
            res = res + (4 * f((x)))
            print(res)

    return (h / 3) * res

print(simpson(1.0, 2.0, 6, f))
print()

#Simpson 3/8
def simpson2(a, b, n, f):

    res = f(a) + f(b)
    h = (b - a) / n

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            res = res + (2 * f(x))
            print(res)
        else:
            res = res + (3 * f((x)))
            print(res)

    return ((3 * h) / 8) * res


print(simpson2(1., 2., 6, f))

