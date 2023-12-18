dirs = {'L':(-1, 0), 'R': (1, 0), 'U':(0, -1), 'D':(0, 1), # part1
        '2':(-1, 0), '0': (1, 0), '3':(0, -1), '1':(0, 1)} # part2
v1, v2, b1, b2 = [(0, 0)], [(0, 0)], 0, 0

for line in open('d18.txt'):
    d, steps, code = line.split()
    # Part 1
    (x, y), (dx, dy) = v1[-1], dirs[d]
    steps = int(steps)
    b1 += steps
    v1.append((x + dx * steps, y + dy * steps))
    # Part 2
    steps, d = int(code[2:-2], 16), code[-2]
    (x, y), (dx, dy) = v2[-1], dirs[d]
    b2 += steps
    v2.append((x + dx * steps, y + dy * steps))

def schoelace(edges): # Schoelace formula for area
    return abs(sum(edges[i][0] * (edges[(i+1)%len(edges)][1] - edges[(i-1)][1]) for i in range(len(edges)))) // 2

def area(edges, b): # correction for the edges
    return schoelace(edges) + b // 2 + 1

print(area(v1, b1))
print(area(v2, b2))