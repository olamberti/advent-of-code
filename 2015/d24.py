import math
from itertools import combinations

presents = [int(x) for x in open('24.txt').readlines()]

def balance(n):
    s, t = 1, sum(presents) // n
    while True:
        q = [math.prod(x) for x in combinations(presents, s) if sum(x) == t]
        if q: return min(q)
        s += 1

print(balance(3))
print(balance(4))