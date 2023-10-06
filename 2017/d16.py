moves = open('d16.txt').read().split(',')

progs = []
for i in range(16):
    progs.append(chr(97 + i))

# P1
for move in moves:
    if move[0] == 's':
        x = int(move[1:])
        progs = progs[-x:] + progs[:-x]
    else:
        pars = move[1:].split('/')
        if move[0] == 'x':
            p1, p2 = [int(x) for x in pars]
            progs[p1], progs[p2] = progs[p2], progs[p1]
        elif move[0] == 'p':
            p1, p2 = [progs.index(x) for x in pars]
            progs[p1], progs[p2] = progs[p2], progs[p1]
print(''.join(progs))

# P2
# TODO: prog p2 for 1_000_000_000 dances