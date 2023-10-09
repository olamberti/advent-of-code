jump = int(open('d17.txt').read())

# P1
state, pos = [0], 0
for i in range(2017):
    pos = (pos + jump) % (i + 1) + 1
    state.insert(pos, i + 1)
print(state[state.index(2017) + 1])

# P2
pos, p2 = 0, 0
for i in range(50_000_000):
    pos = (pos + jump) % (i + 1) + 1
    if pos == 1: p2 = i + 1
print(p2)