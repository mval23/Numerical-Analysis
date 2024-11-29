import math as m


def fixed_point(x0, g, e, max = 100):
    for i in range(max):
        x = g(x0)
        if g(x) == x or abs(x-x0) <= e:
            return x
        x0 = x
    return 'Did not find root :('


def g(x):
    # |g'(x) <=k< 1
    return m.sqrt(m.exp(x)/3)


print(fixed_point(0, g, 1e-12))

def g(x):
    # |g'(x) <=k< 1
    return m.sqrt(m.exp(x)/3)

def g2(x):
    # |g'(x) <=k< 1
    return -m.sqrt(m.exp(x)/3)

print(fixed_point(0, g2, 1e-12))