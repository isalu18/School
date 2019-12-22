import math

def f(x):
    return x * math.log(x)

def trap(a, b, n, f):

    res = f(a) + f(b)
    h = (b - a) / n
    x = a
    for i in range(1, n):
        x = x + h
        res = res + (2 * (f(x)))
        print(res)

    return (h / 2) * res

print(trap(1., 2., 12, f))