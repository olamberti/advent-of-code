grid = [line for line in open('d04.txt').read().splitlines()]	
dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

p1, p2 = 0, 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        # Part 1
        if grid[r][c] == 'X':
            for dr, dc in dirs:
                letters = ['M', 'A', 'S']
                nr, nc = r, c
                for i in range(3):
                    nr, nc = nr + dr, nc + dc
                    if 0 > nr or len(grid) <= nr or 0 > nc or len(grid[0]) <= nc:
                        break
                    if grid[nr][nc] != letters.pop(0):
                        break
                else:
                    p1 += 1
        # Part 2
        if 0 < r < len(grid) - 1 and 0 < c < len(grid[0]) - 1 and grid[r][c] == 'A':
            for dr, dc in [(1, 1), (1, -1)]:
                dr1, dc1 = r + dr, c + dc
                dr2, dc2 = r - dr, c - dc
                if set([grid[dr1][dc1], grid[dr2][dc2]]) != {'M', 'S'}:
                    break
            else:
                p2 += 1

print(p1)
print(p2)