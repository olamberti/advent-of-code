p1, p2 = 0, 0
for line in open('d02.txt'):
    sizes = [int(x) for x in line.strip().split('x')]
    sizes.sort()
    a, b, c = sizes
    p1 += 2 * ((a * b) + (a * c) + (b * c)) + a * b
    p2 += 2 * (a + b) + a * b * c
print(p1)
print(p2)