walls, paths, dirs = set(), {}, {'>': 1, 'v': 1j, '<': -1,'^': -1j}

for y, line in enumerate(open('d06t.txt').readlines()):
    for x, e in enumerate(line.strip()):
        if e == '#': walls.add(x + y*1j)
        elif e in dirs.keys(): 
            g_pos = x + y*1j
            g_dir = dirs[e]
H, W = y, x

while 0 <= g_pos.real <= W and 0 <= g_pos.imag <= H:
    if (g_pos + g_dir) not in walls:
        paths[g_pos] = g_dir
        g_pos += g_dir
    else:
        g_dir *= 1j

print(len(paths))

# part 2 missing, to be continued...