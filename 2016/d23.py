from copy import deepcopy as dp
import math

inst = []
for line in open('23.txt').read().splitlines():
    inst.append(line.split())

def get_val(x, regs):
    if x in regs: return regs[x]
    return int(x)

def run(regs, program):
    i, prog = 0, dp(program)
    while i < len(prog):
        p = prog[i]
        if p[0] == 'cpy' and p[2] in regs:
            regs[p[2]] = get_val(p[1], regs)
        elif p[0] == 'inc':
            regs[p[1]] += 1
        elif p[0] == 'dec':
            regs[p[1]] -= 1
        elif p[0] == 'jnz':
            x = get_val(p[1], regs)
            if x != 0: i += get_val(p[2], regs) - 1
        elif p[0] == 'tgl':
            if p[1] in regs: x = i + regs[p[1]]
            else: x = i + int(p[1])
            if x >= len(prog): pass
            elif prog[x][0] == 'jnz': prog[x][0] = 'cpy'
            elif prog[x][0] == 'cpy': prog[x][0] = 'jnz'
            elif prog[x][0] == 'inc': prog[x][0] = 'dec'
            else: prog[x][0] = 'inc'
        i += 1
    return(regs['a'])

# P1:
p1 = run({'a':7, 'b':0, 'c':0, 'd':0}, inst)
print(p1)
n = p1 - math.factorial(7)

# P2:
print(math.factorial(12) + n)