import re

compass = {'e':1, 's':1j, 'w':-1, 'n':-1j}
facemap = {'|': {'n':'n', 's':'s'}, '-': {'e':'e', 'w':'w'},
           'L': {'s':'e', 'w':'n'}, 'J': {'s':'w', 'e':'n'},
           '7': {'n':'w', 'e':'s'}, 'F': {'n':'e', 'w':'s'}}

grid = {}
for y, line in enumerate(open('d10.txt')):
    for x, ch in enumerate(line.strip()):
        grid[x + y*1j] = ch
        if ch == 'S': start = x + y*1j
width, height = x, y

def get_next(pos, face):
    new_pos = pos + compass[face]
    new_face = facemap[grid[new_pos]][face]
    return new_pos, new_face

# Part 1 - BFS through pipe, state as (position, direction)
loop, front, startfaces, steps = set(), set(), set(), 0
loop.add(start)

for face, d in compass.items():
    new_pos = start + d
    if new_pos not in grid or grid[new_pos] == '.': continue
    if face in facemap[grid[new_pos]]: 
        front.add((start, face))
        startfaces.add(face)

for tile, turns in facemap.items():
    if set(turns.values()) == startfaces: grid[start] = tile

while front:
    new_front = set()
    for pos, face in front:
        new_pos, new_face = get_next(pos, face)
        if new_pos in loop: continue
        loop.add(new_pos)
        new_front.add((new_pos, new_face))
    front = new_front
    if front: steps += 1
print(steps)

# Part 2 - Inside or outside loop
for pos in grid:
    if pos not in loop: grid[pos] = '.'

total = 0
for y in range(height + 1):
    inside = False
    row = ''.join([grid[x + y*1j] for x in range(width + 1)])
    for elem in row:
        if elem in '|LJ': inside = not inside
        elif elem =='.' and inside: total += 1
print(total)