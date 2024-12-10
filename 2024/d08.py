from collections import defaultdict

antennas = defaultdict(list)
for y, line in enumerate(open('d08.txt')):
    for x, e in enumerate(line.strip()):
        if e != '.':
            antennas[e].append(x + y*1j)
W, H = x, y

def in_bounds(a):
    return 0 <= a.real <= W and 0 <= a.imag <= H

def calc_antinodes(antennas, p1 = True):
    antinodes = set()
    for pos in antennas.values():
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                a1, a2, d = pos[i], pos[j], pos[j] - pos[i]
                if not p1:
                    antinodes.add(a1), antinodes.add(a2)
                while in_bounds(a1 - d):
                    a1 = a1 - d
                    antinodes.add(a1)
                    if p1: break
                while in_bounds(a2 + d):
                    a2 = a2 + d
                    antinodes.add(a2)
                    if p1: break                  
    print(len(antinodes))

calc_antinodes(antennas)
calc_antinodes(antennas, False)