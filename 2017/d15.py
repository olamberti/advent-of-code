import re

a, b = [int(x) for x in re.findall(r'\d+', open('d15.txt').read())]

def getnext(x, mul, modulo):
    x = mul * x % 2147483647
    while x % modulo != 0: x = mul * x % 2147483647
    return x

def judge(x, y, rounds, p2 = False):
    res = 0
    for _ in range(rounds):
        if p2: m1 = 4; m2 = 8
        else: m1 = 1; m2 = 1
        x = getnext(x, 16807, m1)
        y = getnext(y, 48271, m2)
        xb = bin(x)[2:].zfill(16)[-16:]
        yb = bin(y)[2:].zfill(16)[-16:]
        if xb == yb: res += 1
    return res

# P1
print(judge(a, b, 40_000_000))

# P2
print(judge(a, b, 5_000_000, True))