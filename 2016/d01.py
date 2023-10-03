todo = open('d01.txt').read().split(', ')
pos, dir, turn, locs, p2 = 0, 1j, {'L': 1j, 'R': -1j}, set(), None

def dist(x):
    return int(abs(x.real) + abs(x.imag))

for inst in todo:
    dir *= turn[inst[0]]
    for i in range(1, int(inst[1:]) + 1):
        pos += dir
        if pos in locs and p2 == None:
            p2 = pos
        else: locs.add(pos)

print(dist(pos))
print(dist(p2))