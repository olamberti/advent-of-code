antennas = {}
for y, line in enumerate(open('d08.txt').readlines()):
    for x, e in enumerate(line.strip()):
        if e != '.':
            if e not in antennas:
                antennas[e] = [(x, y)]
            else:
                antennas[e].append((x, y))
W, H = x, y

def calc_antinodes(antennas, p1 = True):
    antinodes = set()
    for freq in antennas.values():
        for i in range(len(freq)):
            for j in range(i + 1, len(freq)):
                a1, a2 = freq[i], freq[j]
                dx, dy = a2[0] - a1[0], a2[1] - a1[1]
                if not p1:
                    antinodes.add(freq[i])
                    antinodes.add(freq[j])  
                while 0 <= a1[0] - dx <= W and 0 <= a1[1] - dy <= H:
                    a1 = (a1[0] - dx, a1[1] - dy)
                    antinodes.add(a1)
                    if p1: break
                while 0 <= a2[0] + dx <= W and 0 <= a2[1] + dy <= H:
                    a2 = (a2[0] + dx, a2[1] + dy)
                    antinodes.add(a2)
                    if p1: break                  
    print(len(antinodes))

calc_antinodes(antennas)
calc_antinodes(antennas, False)