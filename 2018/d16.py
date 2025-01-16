import re
from copy import deepcopy as dp

top, bottom = open('d16.txt').read().split('\n\n\n\n')
samples = top.split('\n\n')

def exec(inp, inst):
    op, a, b, c = inst
    regs = dp(inp)
    match op:
        case 'addr': regs[c] = regs[a] + regs[b]
        case 'addi': regs[c] = regs[a] + b
        case 'mulr': regs[c] = regs[a] * regs[b]
        case 'muli': regs[c] = regs[a] * b
        case 'banr': regs[c] = regs[a] & regs[b]
        case 'bani': regs[c] = regs[a] & b
        case 'borr': regs[c] = regs[a] | regs[b]
        case 'bori': regs[c] = regs[a] | b
        case 'setr': regs[c] = regs[a]
        case 'seti': regs[c] = a
        case 'gtir': regs[c] = 1 if a > regs[b] else 0
        case 'gtri': regs[c] = 1 if regs[a] > b else 0
        case 'gtrr': regs[c] = 1 if regs[a] > regs[b] else 0
        case 'eqir': regs[c] = 1 if a == regs[b] else 0
        case 'eqri': regs[c] = 1 if regs[a] == b else 0
        case 'eqrr': regs[c] = 1 if regs[a] == regs[b] else 0
    return regs

def parse(samp):
    before, instr, after = samp.split('\n')
    before = list(map(int, re.findall(r'\d+', before)))
    instr = list(map(int, instr.split()))
    after = list(map(int, re.findall(r'\d+', after)))
    return before, instr, after

p1 = 0
oplist = 'addr addi mulr muli banr bani borr bori setr seti gtir gtri gtrr eqir eqri eqrr'.split()
opcodes = {i: set(oplist) for i in range(16)}
for samp in samples:
    before, instr, after = parse(samp)
    valid = 0
    for op in oplist:
        res = exec(before, [op] + instr[1:])
        if res == after:
            valid += 1
        else:
            opcodes[instr[0]].discard(op)
    if valid >= 3:
        p1 += 1
print(p1)

while any(len(v) > 1 for v in opcodes.values()):
    for i, ops in opcodes.items():
        if len(ops) == 1:
            for j in opcodes:
                if i != j:
                    opcodes[j] -= ops
opcodes = {k: v.pop() for k, v in opcodes.items()}

regs = [0, 0, 0, 0]
for line in bottom.splitlines():
    inst = list(map(int, line.split()))
    regs = exec(regs, [opcodes[inst[0]]] + inst[1:])
print(regs[0])