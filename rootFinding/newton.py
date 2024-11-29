import math as m


def newton(x0, f, df, e, max = 100):
    for i in range(max):
        x = x0 - f(x0)/df(x0)
        if f(x) == 0 or abs(x-x0) <= e:
            return x, i
        x0 = x
    return 'Did not find root :('


def f(x):
    return x**3 - 2*x**2 + 4*x - 8

def df(x):
    return 3*x**2 - 4*x + 4


print(newton(2.5, f, df, 10**-16))


def f(x):
    return m.cos(x) + x**2 - 2

def df(x):
    return m.sin(x) + 2*x

print(newton(1, f, df, 10**-16))
