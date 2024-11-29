import math as m


def f(x):
    return x - 2/5


def bisection(a, b, f, e, max = 100):
    p = a + (b-a)/2
    n = 0
    while f(p) != 0 and n < max:
        if f(a)*f(p) < 0:
           b = p
        else:
            a = p

        if (b-a)/2 < e:
            return p
        p = a + (b - a) / 2
        n +=1
        print("({},{}) xn = {}, {}".format(a,b,p, abs(0.4-p)))
    return p, n



print(bisection(0, 2, f, 10**-16))



