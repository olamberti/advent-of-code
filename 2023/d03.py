import re

grid = open('d03.txt').read().splitlines()

def get_neighbors(x, y):
    neighbors = []
    for dx, dy in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < len(grid[0])) and (0 <= ny < len(grid)):
            neighbors.append((nx, ny))
    return neighbors

p1, gears = 0, {}
for y, line in enumerate(grid):
    for mtch in re.finditer(r'(\d+)', line):
        number, is_part_number, is_gear = int(mtch.group()), False, False 
        for x in range(mtch.start(), mtch.end()):
            for nx, ny in get_neighbors(x, y):
                ch = grid[ny][nx]
                if ch.isdigit() or ch == '.': continue
                is_part_number = True
                if ch == '*' and not is_gear:
                    if (nx, ny) not in gears: gears[nx, ny] = [number]
                    else: gears[nx, ny].append(number)
                    is_gear = True
        if is_part_number: p1 += number

p2 = 0
for nums in gears.values():
    if len(nums) == 2: p2 += nums[0] * nums[1]

print(p1)
print(p2)