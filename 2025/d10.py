from itertools import product
from functools import cache

p1, p2 = 0, 0
for row in open('d10.txt').read().splitlines():
    dia, *buttons, jolts = row.split()
    dia = tuple(1 if c == '#' else 0 for c in dia[1:-1])
    buttons = [tuple(map(int,x[1:-1].split(','))) for x in buttons]
    jolts = tuple([int(x) for x in jolts[1:-1].split(',')])
    nm, nb = len(dia), len(buttons)

    pmin, options = nb, {}
    for pressed in product((0, 1), repeat=nb):
        js, n = [0] * nm, sum(pressed)
        for i, p in enumerate(pressed):
            if p == 0: continue
            for id in buttons[i]: js[id] += 1
        js = tuple(js)
        if js not in options: options[js] = n
        else: options[js] = min(options[js], n)
        # Part 1 solution
        lights = tuple(x % 2 for x in js)
        if lights == dia:
            pmin = min(sum(pressed), pmin)
    p1 += pmin

    @cache
    def presses(target):
        if all(x == 0 for x in target): return 0
        if any(x < 0 for x in target): return float('inf')

        total = float('inf')
        for diff, p in options.items():
            new_target = tuple((b - a) for a, b in zip(diff, target))
            if all(a % 2 == 0 for a in new_target):
                half_target = tuple(x // 2 for x in new_target)
                total = min(total, p + 2 * presses(half_target))
        return total
    
    p2 += presses(jolts)

print(p1)
print(p2)