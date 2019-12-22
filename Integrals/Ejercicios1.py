import math

def f1(x):
    return x * math.log(x)

def f2(x):
    return (x + (2/x))**2

def f3(x):
    return x**2/math.sqrt(4-(x**2))

def f4(x):
    return 1 / math.sqrt(1-(x**2))

def f5(x):
    return math.cos(x) / math.e**x

def f6(x):
    return (1/3) * (x * x * x) + 1

def f7(x):
    return 4 * (math.sqrt(49 - (x * x)))

def trap(a, b, n, f):
    
    res = f(a) + f(b)
    h = (b - a) / n
    x = a
    for i in range(1, n):
        x = x + h
        res = res + (2 * (f(x)))
        #print(res)

    return (h / 2) * res

#Simpson 1/3
def simpson(a, b, n, f):

    res = f(a) + f(b)
    h = (b - a) / n

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            res = res + (2 * f(x))
            #print(res)
        else:
            res = res + (4 * f((x)))
            #print(res)

    return (h / 3) * res

#Simpson 3/8
def simpson2(a, b, n, f):

    res = f(a) + f(b)
    h = (b - a) / n

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            res = res + (2 * f(x))
            #print(res)
        else:
            res = res + (3 * f((x)))
            #print(res)

    return ((3 * h) / 8) * res

def eje5trap():
    return 1.86/2 * (2*(5.8+6.9+8.8+14.5+10.4+7.3+8.7+10.3+15))
def eje5simpson():
    
    return 1.86/3 * (2*(5.8+6.9+8.8+14.5+10.4) + 4*(7.3+8.7+10.3+15))
def prueba():
    return 100/3 * (2*(190+170+195+210+195) + 4*(180+175+185+205+200+170))

print('EJERICICIO 1a')
print(trap(1., 2., 6, f1))
print(simpson(1., 2., 6, f1))
print(simpson2(1., 2., 6, f1))
print()
print('EJERCICIO 1b')
print(trap(1., 2., 12, f2))
print(simpson(1., 2., 12, f2))
print(simpson2(1., 2., 12, f2))
print()
print('EJERCICIO 1c')
print(trap(-1., math.sqrt(3), 18, f3))
print(simpson(-1., math.sqrt(3), 18, f3))
print(simpson2(-1., math.sqrt(3), 18, f3))
print()
print('EJERCICIO 2a')
print(trap(-.99, .99, 36, f4))
print(simpson(-.99, .99, 18, f4))
print(simpson2(-.99, .99, 18, f4))
print()
print('EJERCICIO 2b')
print(trap(0., (5*math.pi)/4, 36, f5))
print(simpson(0., (5*math.pi/4), 18, f5))
print(simpson2(0., (5*math.pi/4), 18, f5))
print()
print('EJERCICIO 3')
print(trap(0., 1., 36, f6))
print(simpson(0., 1., 18, f6))
print(simpson2(0., 1., 18, f6))
print()
print(trap(2., 11/3, 20, f6))
print(simpson(2., 11/3, 20, f6))
print(simpson2(2., 11/3, 20, f6))
print()
print('EJERCICIO 4')
print(trap(0., 1.8525, 36, f7))
print(simpson(0., 1.8525, 18, f7))
print(simpson2(0., 1.8525, 18, f7))
print()
print('EJERCICIO 5')
print(eje5simpson())
print(eje5trap())
#print(prueba())