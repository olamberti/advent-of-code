import re

a, b = [int(x) for x in re.findall(r'\d+', open('d15.txt').read())]

def judge(x, y, rounds, p2 = False):
    res = 0
    for _ in range(rounds):
        if p2: m1 = 4; m2 = 8
        else: m1 = 1; m2 = 1
        x = 16807 * x % 2147483647
        while x % m1 != 0: x = 16807 * x % 2147483647
        y = 48271 * y % 2147483647
        while y % m2 != 0: y = 48271 * y % 2147483647
        xb = bin(x)[2:].zfill(16)[-16:]
        yb = bin(y)[2:].zfill(16)[-16:]
        if xb == yb: res += 1
    return res

# P1
print(judge(a, b, 40_000_000))

# P2
print(judge(a, b, 5_000_000, True))