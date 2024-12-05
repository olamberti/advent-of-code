grid = [line for line in open('d04.txt').read().splitlines()]
H, W = len(grid), len(grid[0])

p1, p2 = 0, 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'X':
            for dr, dc in [(x, y) for x in(-1, 0, 1) for y in (-1, 0, 1) if x or y]:
                nr, nc = r, c
                for letter in ['M', 'A', 'S']:
                    nr, nc = nr + dr, nc + dc
                    if not (0 <= nr < H and 0 <= nc < W and grid[nr][nc] == letter):
                        break
                else:
                    p1 += 1
        if grid[r][c] == 'A' and 0 < r < H - 1 and 0 < c < W - 1:
            for dr, dc in [(1, 1), (1, -1)]:
                r1, c1, r2, c2 = r + dr, c + dc, r - dr, c - dc
                if set([grid[r1][c1], grid[r2][c2]]) != {'M', 'S'}:
                    break
            else:
                p2 += 1

print(p1)
print(p2)