inp = int(open('03.txt').read())

# P1
sq, p = 1, 0
while sq ** 2  < inp:
    sq += 2; p += 1 + 1j
n = sq ** 2

dirs = [-1, -1j, 1, 1j]
for d in dirs:
    for _ in range(1, sq):
        if n == inp:
            print(int(abs(p.real) + abs(p.imag)))
        n -= 1; p += d

# P2
# TODO: prog part 2