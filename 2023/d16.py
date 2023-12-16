mappings = {'.': {1:[1], -1:[-1], 1j:[1j], -1j:[-1j]},
            '|': {1:[1j, -1j], -1:[1j,-1j], 1j:[1j], -1j:[-1j]},
            '-': {1:[1], -1:[-1], 1j:[1, -1], -1j:[1, -1]},
            '\\':{1:[1j], -1:[-1j], 1j:[1], -1j:[-1]},
            '/': {1:[-1j], -1:[1j], 1j:[-1], -1j:[1]}}
grid = {}
for y, line in enumerate(open("d16.txt")):
    for x, ch in enumerate(line.strip()):
        grid[x + y*1j] = ch
width, height = x + 1, y + 1

def energy(pos, d):
    front, seen, lights = {(pos, d)}, set(), set()
    while front:
        new_front = set()
        for pos, d in front:
            if pos not in grid or (pos, d) in seen: continue
            seen.add((pos, d))
            lights.add(pos)
            for new_d in mappings[grid[pos]][d]:
                new_front.add((pos + new_d, new_d))
        front = new_front
    return(len(lights))

# Part 1
print(energy(0, 1))

# Part 2
p2 = 0
for x in range(width):
    p2 = max(p2, energy(x, 1j))
    p2 = max(p2, energy(x + height, -1j))
for y in range(height):
    p2 = max(p2, energy(y*1j, 1))
    p2 = max(p2, energy(y*1j + width, -1))
print(p2)