from functools import cache

codes = [x for x in open('d21.txt').read().split()]
num_pad, dir_pad = '789456123.0A', '.^A<v>'

@cache
def get_moves(start, end):
    if start == end: return 'A'
    pad = num_pad if (start.isnumeric() or end.isnumeric()) else dir_pad
    sx, sy = pad.index(start) %3, pad.index(start)//3
    ex, ey = pad.index(end)   %3, pad.index(end)  //3
    bx, by = pad.index('.')   %3, pad.index('.')  //3
    dx, dy = ex - sx, ey - sy
    moves = '<'*-dx + '^'*-dy + 'v'*dy + '>'*dx
    if ((moves[0] in '<>' and sy == by and ex == bx) or
        (moves[0] in '^v' and sx == bx and ey == by)):
        moves = moves[::-1] 
    return moves + 'A'

@cache
def get_length(code, lvl):
    if lvl == -1: return len(code)
    length = 0
    for i, c in enumerate(code):
        length += get_length(get_moves(code[i-1], c), lvl-1)
    return length

p1, p2 = 0, 0
for code in codes:
    p1 += get_length(code, 2) * int(code[:-1])
    p2 += get_length(code, 25) * int(code[:-1])

print(p1)
print(p2)