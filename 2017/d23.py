prog = [line.split() for line in open('d23.txt').read().splitlines()]
regs = {}
for c in 'abcdefgh': regs[c] = 0

def get(x):
    if x in regs: return regs[x]
    return int(x)

# P1
pos, m = 0, 0
while 0 <= pos < len(prog):
    ins = prog[pos]
    if ins[0] == 'set': regs[ins[1]] = get(ins[2])
    elif ins[0] == 'sub': regs[ins[1]] -= get(ins[2])
    elif ins[0] == 'mul':
        regs[ins[1]] *= get(ins[2])
        m += 1
    elif ins[0] == 'jnz':
        if get(ins[1]) != 0: pos += get(ins[2]) - 1
    pos += 1
print(m)

# P2 - manual analysis of the code can be simplified to the following for my input
h = 0
for b in range(105_700, 122_700 + 1, 17):
    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0:
            h += 1
            break
print(h)