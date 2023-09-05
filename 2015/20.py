import sympy
import math
import numpy as np

lim = int(open('20.txt').read())

# Theory based on https://en.wikipedia.org/wiki/Divisor_function
def ub(n):
    return (pow(np.e, np.euler_gamma) * n * math.log(math.log(n))) * 10

start = 2
while ub(start) < lim: start += 1

# P1
def p1(n):
    return math.prod([int((pow(p, a + 1) - 1) / (p - 1)) for p, a in sympy.factorint(n).items()]) * 10

n = start
while p1(n) < lim: n += 1
print(n)

# P2
def p2(n):
    res, divs = 1, sympy.divisors(n)
    for d in divs:
        if n / d > 50: continue
        res += d * 11
    return res

n = start
while p2(n) < lim: n += 1
print(n)