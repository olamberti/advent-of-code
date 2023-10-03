p1, prog = {'a':0, 'b':0, 'c':0, 'd':0}, []

for line in open('12.txt').read().splitlines():
    prog.append(line.split())

def run(regs):
    i = 0
    while i < len(prog):
        p = prog[i]
        if p[0] == 'cpy':
            if p[1] in regs: regs[p[2]] = regs[p[1]]
            else: regs[p[2]] = int(p[1])
        elif p[0] == 'inc':
            regs[p[1]] += 1
        elif p[0] == 'dec':
            regs[p[1]] -= 1
        elif p[0] == 'jnz':
            if p[1] in regs:
                if regs[p[1]] != 0: i += int(p[2]) - 1
            elif p[1] != 0:
                i += int(p[2]) - 1
        i += 1
    return(regs['a'])

# P1
print(run(p1))

# P2
p2 = {'a':0, 'b':0, 'c':1, 'd':0}
print(run(p2))