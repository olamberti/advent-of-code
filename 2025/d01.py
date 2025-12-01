pos, p1 = 50, 0

for line in open('d01.txt').readlines():
    d, n = line[0], int(line[1:])
    if d == 'L':
        n = (100 - n)
    pos = (pos + n) % 100
    if pos == 0: p1 += 1

print(p1)