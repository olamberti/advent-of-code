import re
import statistics

towers = {}
for line in open('d07.txt').read().splitlines():
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
def wsum(t):
    res = towers[t][0] + sum([wsum(ch) for ch in towers[t][2]])
    towers[t].append(res)
    return res

def balance(t, target = None):
    weights = [towers[ch][3] for ch in towers[t][2]]
    med = statistics.median(weights)
    for ch in towers[t][2]:
        if towers[ch][3] != med: return balance(ch, med)
    return towers[t][0] - (towers[t][3] - target)

wsum(tower)
print(balance(tower))