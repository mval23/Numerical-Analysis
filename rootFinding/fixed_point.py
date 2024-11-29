import math as m


def fixed_point(x0, g, e, max = 100):
    for i in range(max):
        x = g(x0)
        if g(x) == x or abs(x-x0) <= e:
            return x, i
        x0 = x
    return 'Did not find root :('



def g(x):
    # |g'(x) <=k< 1
    return 2 / x -1


print(fixed_point(-3, g, 10**-16))