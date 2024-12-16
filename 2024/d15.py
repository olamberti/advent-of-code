top, bottom = open('d15.txt').read().split('\n\n')
grid = {x + y * 1j: c for y, row in enumerate(top.splitlines())
                      for x, c in enumerate(row)}
moves = bottom.replace('\n', '')
dirs = {'>': 1, '<': -1, '^': -1j, 'v': 1j}
pos, = (p for p in grid if grid[p] == '@')

# Part 1
for move in moves:
    d = dirs[move]
    if grid[pos + d] == '#': continue
    if grid[pos + d] == 'O':
        npos = pos + d
        while grid[npos] == 'O': npos += d
        if grid[npos] == '#': continue
        grid[npos] = 'O'
    grid[pos], grid[pos + d] = '.', '@'
    pos += d

print(sum([int(pos.real) + int(pos.imag * 100)
           for pos in grid if grid[pos] == 'O']))

# Part 2
rules = {'#': '##', 'O': '[]', '@': '@.', '.': '..'}
top = top.translate(str.maketrans(rules)).splitlines()
grid = {x + y * 1j: c for y, row in enumerate(top)
                      for x, c in enumerate(row)}
pos, = (p for p in grid if grid[p] == '@')

for move in moves:
    d, can_move, todo = dirs[move], True, [pos]
    for c in todo:
        npos = c + d
        if npos in todo: continue
        if grid[npos] == '#':
            can_move = False
            break
        if grid[npos] in '[]':
            todo.append(npos)
            if grid[npos] == '[': todo.append(npos + 1)
            else: todo.append(npos - 1)
    if not can_move: continue
    copy = grid.copy()
    for c in todo: grid[c] = '.'
    for c in todo: grid[c + d] = copy[c]
    grid[pos], grid[pos + d] = '.', '@'
    pos += d

print(sum([int(pos.real) + int(pos.imag * 100)
           for pos in grid if grid[pos] == '[']))