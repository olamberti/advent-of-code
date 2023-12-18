d1 = {'L':(-1, 0), 'R': (1, 0), 'U':(0, -1), 'D':(0, 1)} # part1
d2 = {'2':(-1, 0), '0': (1, 0), '3':(0, -1), '1':(0, 1)} # part2
v1, b1 = [(0, 0)], 0
v2, b2 = [(0, 0)], 0

for line in open('d18.txt'):
    d, steps, code = line.split()
    # Part 1
    x, y = v1[-1]
    dx, dy = d1[d]
    steps = int(steps)
    b1 += steps
    v1.append((x + dx * steps, y + dy * steps))
    # Part 2
    steps, d = int(code[2:-2], 16), code[-2]
    x, y = v2[-1]
    dx, dy = d2[d]
    b2 += steps
    v2.append((x + dx * steps, y + dy * steps))

def schoelace(edges): # Schoelace formula
    return abs(sum(edges[i][0] * (edges[(i+1)%len(edges)][1] - edges[(i-1)][1]) for i in range(len(edges)))) // 2

def pick(area, b): # Pick's theorem
    return area - b // 2 + 1

def solve(edges, b): # total area = interior + boundary
    return pick(schoelace(edges), b) + b

print(solve(v1, b1))
print(solve(v2, b2))