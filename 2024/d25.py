heights = open('d25.txt').read().split('\n\n')

keys, locks = [], []
for grid in heights:
    counter = [0, 0, 0, 0, 0]
    for line in grid.split('\n'):
        for i, c in enumerate(line):
            if c == '#':
                counter[i] += 1
    if grid[0] == '.':
        keys.append(counter)
    else:
        locks.append(counter)

p1 = 0
for key in keys:
    for lock in locks:
        overlap = [k + l for k, l in zip(key, lock)]
        if all(o <= 7 for o in overlap):
            p1 += 1
print(p1)