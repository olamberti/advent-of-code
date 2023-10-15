states = {}
for line in open('d25.txt').read().splitlines():
    if 'Begin' in line: st = line.strip('.').split()[-1]
    elif 'steps' in line: steps = int(line.split()[-2])
    elif 'In state' in line:
        state = line.strip(':').split()[-1]
        states[state] = {}
    elif 'current value' in line:
        cv = int(line.strip(':').split()[-1])
        states[state][cv] = []
    elif 'Write' in line:
        v = int(line.strip('.').split()[-1])
        states[state][cv].append(v)
    elif 'Move' in line:
        v = line.strip('.').split()[-1]
        if v == 'right': states[state][cv].append(1)
        elif v == 'left': states[state][cv].append(-1)
    elif 'Continue' in line:
        v = line.strip('.').split()[-1]
        states[state][cv].append(v)

pos, ones = 0, set()
for _ in range(steps):
    cv = 1 if pos in ones else 0
    wv, d, st = states[st][cv]
    if cv == 1 and wv == 0: ones.remove(pos)
    elif cv == 0 and wv == 1: ones.add(pos)
    pos += d
print(len(ones))