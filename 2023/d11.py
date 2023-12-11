from itertools import combinations

def dist(a, b):
    return int(abs(b[0] - a[0]) + abs(b[1] - a[1]))

def expand(galaxies, scale):
    new_galaxies = []
    mX = max([coord[0] for coord in galaxies])
    mY = max([coord[1] for coord in galaxies])
    empty_y = 0
    for j in range(mY + 1):
        if all([coord[1] != j for coord in galaxies]):
                empty_y += 1
                continue
        empty_x = 0
        for i in range(mX + 1):
            if all([coord[0] != i for coord in galaxies]):
                empty_x += 1
                continue
            for x, y in galaxies:
                if x == i and y == j:
                    new_galaxies.append((i + empty_x * (scale - 1), j + empty_y * (scale - 1)))
    return new_galaxies
    

galaxies = []
for y, line in enumerate(open('d11.txt')):
    for x, ch in enumerate(line):
        if ch == '#': galaxies.append((x, y))

new_galaxies = expand(galaxies, 2)
total = 0
for g1, g2 in combinations(new_galaxies, 2):
    total += dist(g1, g2)
print(total)

new_galaxies = expand(galaxies, 1_000_000)
total = 0
for g1, g2 in combinations(new_galaxies, 2):
    total += dist(g1, g2)
print(total)