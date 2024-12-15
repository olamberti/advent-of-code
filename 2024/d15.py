grid, moves = open('d15.txt').read().split('\n\n')
grid, moves = grid.splitlines(), moves.replace('\n', '')
dirs = {'>': 1, '<': -1, '^': -1j, 'v': 1j}

walls, boxes = set(), set()
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == '#': walls.add(x + y * 1j)
        if cell == 'O': boxes.add(x + y * 1j)
        if cell == '@': pos = x + y * 1j

# Part 1
for move in moves:
    d = dirs[move]
    if pos + d in walls:
        continue
    elif pos + d in boxes:
        npos = pos + d
        while npos in boxes:
            npos += d
        if npos in walls:
            continue
        boxes.remove(pos + d)
        boxes.add(npos)
        pos += d        
    else:
        pos += d

print(sum(int(food.real) + int(food.imag * 100) for food in boxes))

# Part 2
grid2, rp = [], {'.': '..', 'O': '[]', '#': '##', '@': '@.'}
for line in grid:
    for old, new in rp.items():
        line = line.replace(old, new)
    grid2.append(line)

walls, boxes_left, boxes_right = set(), set(), set()
for y, row in enumerate(grid2):
    for x, cell in enumerate(row):
        if cell == '#': walls.add(x + y * 1j)
        elif cell == '[':
            boxes_left.add(x + y * 1j)
        elif cell == ']':
            boxes_right.add(x + y * 1j)
        elif cell == '@': pos = x + y * 1j

for move in moves:
    d = dirs[move]
    can_move = True
    to_check = [pos]
    for cell in to_check:
        new_pos = cell + d
        if new_pos in to_check:
            continue
        if new_pos in walls:
            can_move = False
            break
        if new_pos in boxes_left or new_pos in boxes_right:
            to_check.append(new_pos)
            if new_pos in boxes_left:
                to_check.append(new_pos + 1)
            elif new_pos in boxes_right:
                to_check.append(new_pos - 1)
    if not can_move:
        continue
    new_boxes_left, new_boxes_right = set(), set()
    for cell in to_check:
        if cell in boxes_left or cell in boxes_right:
            if cell in boxes_left:
                boxes_left.remove(cell)
                new_boxes_left.add(cell + d)
            elif cell in boxes_right:
                boxes_right.remove(cell)
                new_boxes_right.add(cell + d)
    boxes_left = boxes_left.union(new_boxes_left)
    boxes_right = boxes_right.union(new_boxes_right)
    pos += d
    
print(sum(int(box.real) + int(box.imag * 100) for box in boxes_left))