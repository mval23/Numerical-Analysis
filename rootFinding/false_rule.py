import math as m


def f(x):
    return m.cos(x) + x**2 - 2


def false_rule(a, b, f, e, max = 100):
    x = b - f(b)*(b-a)/(f(b)-f(a))
    n = 0
    while f(x) != 0 and n < max:
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x

        if (b-a)/2 < e:
            return x, n
        x = b - f(b)*(b-a)/(f(b)-f(a))
        n +=1
    return x, n



print(false_rule(0, 2, f, 10**-16))
