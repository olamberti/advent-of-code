pos, r, p1, p2 = 50, 'R', 0, 0              # position, direction, part1, part2

for line in open('d01.txt').readlines():
    nr, d = line[0], int(line[1:])          # new direction, distance
    if nr!= r:                              # direction change
        pos = (100 - pos) % 100             # mirror position (0 remains 0)
        r = nr                              # update direction
    p2 += (pos + d) // 100                  # part2: count reaching 100's
    pos = (pos + d) % 100                   # update position
    if pos == 0: p1 += 1                    # part1: count ending at 0

print(p1)
print(p2)