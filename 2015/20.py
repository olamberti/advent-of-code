import sympy

tar = int(open('20.txt').read())

def presents(n):
    return sum(sympy.divisors(n)) * 10

# P1 - TODO optimize instead of BF
n = 1
while presents(n) < tar: n += 1
print(n)

# P2
# TODO code part 2

