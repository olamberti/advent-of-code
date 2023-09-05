import math
from itertools import combinations

# Init:
boss, player = [0, 0, 0], [100, 0, 0]
for line in open('21.txt').readlines():
    line = line.strip().split(' ')
    if line[0] == 'Hit': boss[0] = int(line[-1])
    elif line[0] == 'Damage:': boss[1] = int(line[-1])
    elif line[0] == 'Armor:': boss[2] = int(line[-1])

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5), (0, 0, 0)] # no armor as last item
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

def player_wins(player, boss):
    return math.ceil(boss[0] / max(player[1] - boss[2], 1)) <= math.ceil(player[0] / max(boss[1] - player[2], 1))

# P1
gears = []
for weap in weapons:
    for arm in armors:
        for n in [0, 1, 2]:
            for rs in combinations(rings, n):
                gear = [weap[0] + arm[0], weap[1], arm[2]]
                for r in rs:
                    gear[0] += r[0]
                    gear[1] += r[1]
                    gear[2] += r[2]
                gears.append(gear)
gears.sort()

for gear in gears:
    player[1], player[2] = gear[1], gear[2]
    if player_wins(player, boss):
        print(gear[0])
        break

# P2
gears.sort(reverse=True)
for gear in gears:
    player[1], player[2] = gear[1], gear[2]
    if not player_wins(player, boss):
        print(gear[0])
        break