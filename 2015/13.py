import itertools

# Read input
happ = {}
for line in open('13.txt').readlines():
    line = line.strip().split(' ')
    a, b, val = line[0][0], line[-1][0], int(line[3])
    if line[2] == 'lose': val *= -1
    if a not in happ: happ[a] = {}
    happ[a][b] = val

def hsum(c):
    h = 0
    for i in range(len(c) - 1):
        a, b = c[i], c[i + 1]
        h += happ[a][b]
        h += happ[b][a]
    h += happ[c[0]][c[-1]]
    h += happ[c[-1]][c[0]]
    return h

def happMax(happ):
    peo, combos, maxH = list(happ.keys()), set(), 0
    for perm in list(itertools.permutations(peo[1:])):
        c = peo[0] + ''.join([p for p in perm])
        if c[0] + c[-1:0:-1] in combos: continue
        combos.add(c)
    for c in combos:
        happiness = hsum(c)
        maxH = max(happiness, maxH)
    return maxH

# P1
print(happMax(happ))

# P2
happ['O'] = {}
for p in happ.keys():
    happ[p]['O'] = 0
    happ['O'][p] = 0
print(happMax(happ))
