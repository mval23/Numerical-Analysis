import math as m


def secant(x0, x1, f, e, max = 100):

    for i in range(max):
        x = x1 - (f(x1)*(x1-x0)/(f(x1)-f(x0)))
        if abs(x-x1) <= e:
            return x, i
        if f(x1)-f(x0) == 0:
            return "f(x1)-f(x0) was very very small TT"
        x0, x1 = x1, x
        #print(x0, x1, x)
    return 'Did not find root :('



def f(x):
    return x**3 - x - 2


root = secant(1, 2, f, 1e-10, 100)
print(root)

def f(x):
    return m.cos(x) + x**2 - 2

root = secant(1.5, 2, f, 1e-10, 100)
print(root)