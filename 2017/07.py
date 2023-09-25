import re

towers = {}
for line in open('07.txt').read().splitlines():
    f, ch = re.findall(r'(\w+) \((\d+)', line)[0], re.findall(r' (\w+)', line)
    towers[f[0]] = [int(f[1]), None, ch]

for tower, elems in towers.items():
    for child in elems[2]:
        towers[child][1] = tower

# P1
for tower, elems in towers.items():
    if not elems[1]:
        print(tower)
        break

# P2
# TODO: balancing towers