grid = [line.strip() for line in open('d21.txt')]
rocks = {(x, y) for y, line in enumerate(grid) for x, ch in enumerate(line.strip()) if ch == '#'}
start = next((x, y) for y, line in enumerate(grid) for x, ch in enumerate(line.strip()) if ch == 'S')
height, width = len(grid), len(grid[0])
size = height if height == width else None

# Part 1 - BFS for creating distance map on original grid
front, steps, distmap = {start}, 0, {start: 0}
while front:
    steps += 1
    new_front = set()
    for x, y in front:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy 
            if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
            if (nx, ny) in rocks or (nx, ny) in distmap: continue
            distmap[(nx, ny)] = steps
            new_front.add((nx, ny))
    front = new_front
print(len([pos for pos, step in distmap.items() if step <= 64 and step % 2 == 0]))

# Part 2 - geometrical solution true after every 2nd step
N = 26501365
n = (N - (size - 1) // 2) // size
tile_odd = len([pos for pos, step in distmap.items() if step % 2 == 1])
tile_even = len([pos for pos, step in distmap.items() if step % 2 == 0])
triang_odd = len([pos for pos, step in distmap.items() if step > 65 and step % 2 == 1])
triang_even = len([pos for pos, step in distmap.items() if step > 65 and step % 2 == 0])
print((n + 1)**2 * tile_odd + n**2 * tile_even + n * triang_even - (n + 1) * triang_odd)