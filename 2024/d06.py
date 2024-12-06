walls, paths, cache, dirs = set(), set(), set(), {'>': 1, 'v': 1j, '<': -1,'^': -1j}

for y, line in enumerate(open('d06.txt').readlines()):
    for x, e in enumerate(line.strip()):
        if e == '#': walls.add(x + y*1j)
        elif e in dirs.keys(): 
            pos = x + y*1j
            dir = dirs[e]
W, H = x, y

def in_bounds(p):
    return 0 <= p.real <= W and 0 <= p.imag <= H

obstacles = set()
while in_bounds(pos):
    paths.add(pos)
    cache.add((pos, dir))
    if (pos + dir) in walls:
        dir *= 1j
    else:
        obs = pos + dir
        if obs not in paths and in_bounds(obs):
            new_cache = cache.copy()
            n_pos, n_dir= pos, dir * 1j
            while in_bounds(n_pos):
                new_cache.add((n_pos, n_dir))
                if (n_pos + n_dir) in walls or (n_pos + n_dir) == obs:
                    n_dir *= 1j
                else:
                    n_pos += n_dir
                if (n_pos, n_dir) in new_cache:
                    obstacles.add(obs)
                    break
        pos += dir  

print(len(paths))
print(len(obstacles))