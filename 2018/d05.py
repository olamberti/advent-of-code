polymer = open('d05.txt').read()

def reduce(poly):
    old_poly = None
    while old_poly != poly:
        old_poly = poly
        for i in range(26):
            react = chr(ord('a') + i) + chr(ord('A') + i)
            poly = poly.replace(react, '')
            react = react.swapcase()
            poly = poly.replace(react, '')
    return len(poly)

# P1
p1 = reduce(polymer)
print(p1)

# P2
units, p2 = set(), p1
for c in polymer: units.add(c.lower())
for u in units:
    p = polymer.replace(u, '').replace(u.upper(), '')
    p2 = min(reduce(p), p2)
print(p2)