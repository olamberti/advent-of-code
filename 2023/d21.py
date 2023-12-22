rocks = set()

for y, line in enumerate(open('d21.txt')):
    for x, ch in enumerate(line.strip()):
        if ch == '#':
            rocks.add((x, y))
            continue
        elif ch == 'S': start = ((x, y))
height, width = y + 1, x + 1
size = height if height == width else None

# Part 1
front = {start}
for step in range(64):
    new_front = set()
    for x, y in front:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy 
            if (nx, ny) in rocks: continue
            new_front.add((nx, ny))
    front = new_front
print(len(front))

# Part 2
front = {start}
seen, odd, v = set(), set(), []
for s in range(1, (size - 1) // 2 + 4 * size + 1):
    new_front = set()
    for x, y in front:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy 
            if (nx % size, ny % size) in rocks: continue
            if (nx, ny) in seen: continue
            new_front.add((nx, ny))
            seen.add((nx, ny))
            if s % 2 == 1: odd.add((nx, ny))
    front = new_front
    if (s - (size - 1) // 2) % (2 * size) == 0:
            v.append(len(odd))

N = 26501365
c = v[0]
b = 2 * v[1] - (v[2] + 3 * v[0]) // 2
a = (v[2] + v[0]) // 2 - v[1]
x = (N - (size - 1) // 2) // (2 * size)
print(a * (x ** 2)+ b * x + c)