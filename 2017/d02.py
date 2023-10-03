import re

p1, p2 = 0, 0
for line in open('d02.txt').read().splitlines():
    v = [int(x) for x in re.findall('\d+', line)]
    p1 += max(v) - min(v)
    for a in v:
        for b in v:
            if a == b: continue
            if a % b == 0: p2 += a // b
print(p1)
print(p2)