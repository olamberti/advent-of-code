import re

N = 10000000000000
def solve(x1, y1, x2, y2, t1, t2, part2 = False):
    if part2:
        t1 += N
        t2 += N
    a = (t2 * x2 - t1 * y2) / (x2 * y1 - x1 * y2)
    b = (t2 * x1 - t1 * y1) / (x1 * y2 - x2 * y1)
    if (a != int(a) or b != int(b)) or (not part2 and (a > 100 or b > 100)):
        return 0
    return int(a * 3 + b)

p1, p2 = 0, 0
for s in open('d13.txt').read().split('\n\n'):
    data = [int(x) for x in re.findall(r'(\d+)', s)]
    p1 += solve(*data)
    p2 += solve(*data, True)

print(p1)
print(p2)