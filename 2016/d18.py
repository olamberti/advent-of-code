grid = []
grid.append(open('d18.txt').read())

safe = grid[0].count('.')
while len(grid) < 400_000:
    line, nline = '.' + grid[-1] + '.', ''
    for j in range(1, len(line) - 1):
        if line[j-1 : j+2] in ['^^.', '.^^', '^..','..^']:
            nline += '^'
        else:
            nline += '.'
            safe += 1
    grid.append(nline)
    if len(grid) == 40: print(safe)
print(safe)