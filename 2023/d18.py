d1 = {'L':(-1, 0), 'R': (1, 0), 'U':(0, -1), 'D':(0, 1)} # part1
d2 = {'2':(-1, 0), '0': (1, 0), '3':(0, -1), '1':(0, 1)} # part2
v1, b1 = [(0, 0)], 0
v2, b2 = [(0, 0)], 0

for line in open('d18.txt'):
    d, steps, code = line.split()
    # Part 1
    steps = int(steps)
    b1 += steps
    dx, dy = d1[d]
    x, y = v1[-1]
    v1.append((x + dx * steps, y + dy * steps))
    # Part 2
    steps, d = int(code[2:-2], 16), code[-2]
    b2 += steps
    dx, dy = d2[d]
    x, y = v2[-1]
    v2.append((x + dx * steps, y + dy * steps))

def schoelace(edges): # Schoelace formula for area of a polygon
    return abs(sum(edges[i][0] * (edges[(i+1)%len(edges)][1] - edges[(i-1)][1]) for i in range(len(edges)))) // 2

def pick(area, b): # Pick's theorem (A = i + b/2 - 1)
    return area - b // 2 + 1

def solve(edges, b): # Area = interior + boundary
    return pick(schoelace(edges), b) + b

print(solve(v1, b1))
print(solve(v2, b2))