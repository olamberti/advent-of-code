import math
from itertools import combinations

# Init:
boss = [0, 0, 0]
for line in open('21.txt').readlines():
    line = line.strip().split(' ')
    if line[0] == 'Hit': boss[0] = int(line[-1])
    elif line[0] == 'Damage:': boss[1] = int(line[-1])
    elif line[0] == 'Armor:': boss[2] = int(line[-1])

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5), (0, 0, 0)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3), (0, 0, 0), (0, 0, 0)]

gears = []
for w in weapons:
    for a in armors:
            for r1, r2 in combinations(rings, 2):
                gear = [w[0] + a[0] + r1[0] + r2[0], w[1] + r1[1] + r2[1], a[2] + r1[2] + r2[2]]
                gears.append(gear)

def player_wins(player):
    return math.ceil(boss[0] / max(player[1] - boss[2], 1)) <= math.ceil(player[0] / max(boss[1] - player[2], 1))

def get_cost(gears, win = True):
    for g in gears:
        if player_wins([100, g[1], g[2]]) == win: break
    return g[0]

# P1
gears.sort()
print(get_cost(gears))

# P2
gears.sort(reverse=True)
print(get_cost(gears, False))