import sympy
import math
import numpy as np

lim = int(open('20.txt').read())

# P1
def p1(n):
    return math.prod([int((pow(p, a + 1) - 1) / (p - 1)) for p, a in sympy.factorint(n).items()]) * 10

n = 1
while p1(n) < lim: n += 1
print(n)

# P2
def p2(n):
    res, divs = 1, sympy.divisors(n)
    for d in divs:
        if n / d > 50: continue
        res += d * 11
    return res

n = 1
while p2(n) < lim: n += 1
print(n)