from collections import defaultdict
from itertools import product
from functools import cache

p1, p2 = 0, 0
for row in open('d10.txt').read().splitlines():
    dia, *buttons, jolts = row.split()
    dia = tuple(1 if c == '#' else 0 for c in dia[1:-1])
    buttons = [tuple(map(int,x[1:-1].split(','))) for x in buttons]
    jolts = tuple([int(x) for x in jolts[1:-1].split(',')])

    ops, patterns = {}, defaultdict(list)
    for pressed in product((0, 1), repeat=len(buttons)):
        jolt = [0] * len(jolts)
        for i, p in enumerate(pressed):
            for j in buttons[i]: jolt[j] += p
        lights = tuple(x % 2 for x in jolt)
        ops[pressed] = jolt
        patterns[lights] += [pressed]
    p1 += min([sum(x) for x in patterns[dia]])

    @cache
    def presses(target):
        if all(x == 0 for x in target): return 0
        if any(x < 0 for x in target): return float('inf')
        
        total, lights = float('inf'), tuple(x % 2 for x in target)
        for pressed in patterns[lights]:
            diff = ops[pressed]
            new_target = tuple((b - a) // 2 for a, b in zip(diff, target))
            total = min(total, sum(pressed) + 2 * presses(new_target))
        return total 
    p2 += presses(jolts)

print(p1)
print(p2)