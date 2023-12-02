import re
import math

MAXES = {'red':12, 'green':13, 'blue':14}

p1, p2 = 0, 0
for id, line in enumerate(open('d02.txt').read().splitlines(), 1):
    pairs = [(int(n), c) for n, c in re.findall(r'(-?\d+) (\w+)', line)]
    mins = {'red':0, 'green':0, 'blue':0}
    valid = True
    for num, color in pairs:
        if num > MAXES[color]: valid = False
        mins[color] = max(num, mins[color])
    if valid: p1 += id
    p2 += math.prod(mins.values())

print(p1)
print(p2)