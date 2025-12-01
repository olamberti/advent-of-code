pos, p1, p2 = 50, 0, 0

for line in open('d01.txt').readlines():
    d, n = line[0], int(line[1:])
    if d == 'L':
        pos = (100 - pos) % 100
    p2 += (pos + n) // 100
    pos = (pos + n) % 100
    if pos == 0:
        p1 += 1
    if d == 'L':
        pos = (100 - pos) % 100

print(p1)
print(p2)