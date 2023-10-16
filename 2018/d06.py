coords, mx, my, Mx, My = [], int(1e10), int(1e10), 0, 0
for i, line in enumerate(open('d06.txt').read().splitlines()):
    x, y = [int(x) for x in line.split(', ')]
    mx, my, Mx, My = min(x, mx), min(y, my), max(x, Mx), max(y, My)
    coords.append((x, y))

# P1
# TODO: code part 1

# P2
# TODO: code part 2