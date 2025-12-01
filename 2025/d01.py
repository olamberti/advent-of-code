pos, p1, p2 = 50, 0, 0

for line in open('d01.txt').readlines():
    d, n = line[0], int(line[1:])
    p2 += n // 100
    n = n % 100
    if d == 'R' and pos + n >= 100 and pos != 0:
        p2 += 1
    elif d == 'L' and pos - n <= 0 and pos != 0:
        p2 += 1
    if d == 'L':
        n = (100 - n)
    pos = (pos + n) % 100
    if pos == 0:
        p1 += 1

print(p1)
print(p2)