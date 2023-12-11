from itertools import combinations

def dist(a, b):
    return int(abs(b[0] - a[0]) + abs(b[1] - a[1]))

def expand(galaxies, scale):
    new_galaxies = []
    for gx, gy in galaxies:
        gx += (scale - 1) * len([x for x in empty_x if x < gx])
        gy += (scale - 1) * len([y for y in empty_y if y < gy])
        new_galaxies.append((gx, gy))
    return new_galaxies

grid = [line.strip() for line in open('d11.txt')]
empty_x = [x for x, line in enumerate(list(zip(*grid))) if all(ch == '.' for ch in line)]
empty_y = [y for y, line in enumerate(grid) if all(ch == '.' for ch in line)]
galaxies = [(x, y) for y, line in enumerate(grid) for x, ch in enumerate(line) if ch == '#']

for scale in (2, 1_000_000):
    new_galaxies = expand(galaxies, scale)
    total = sum([dist(g1, g2) for g1, g2 in combinations(new_galaxies, 2)])
    print(total)