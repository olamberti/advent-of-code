dirs = {'^': 1j, 'v': -1j, '>': 1, '<': -1}

houses_p1, pos = set(), 0
houses_p2, pos1, pos2 = set(), 0, 0
houses_p1.add(0); houses_p2.add(0)
for i, d in enumerate(open('d03.txt').read()):
    pos += dirs[d]
    houses_p1.add(pos)
    if i % 2 == 0:
        pos1 += dirs[d]
        houses_p2.add(pos1)
    else:
        pos2 += dirs[d]
        houses_p2.add(pos2)
print(len(houses_p1))
print(len(houses_p2))