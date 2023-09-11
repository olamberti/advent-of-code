prog = []
for line in open('23.txt').readlines():
    prog.append(line.strip())

def run(prog, a, b):
    p, regs = 0, {'a': a, 'b': b}
    while p in range(len(prog)):
        inst, par = prog[p].split(' ', 1)
        if inst == 'hlf':
            regs[par] //= 2
            p += 1
        elif inst == 'tpl':
            regs[par] *= 3
            p += 1
        elif inst == 'inc':
            regs[par] += 1
            p += 1
        elif inst == 'jmp':
            p += int(par)
        elif inst == 'jie':
            par, off = par.split(', ')
            if regs[par] % 2 == 0: p += int(off)
            else: p  += 1
        elif inst == 'jio':
            par, off = par.split(', ')
            if regs[par] == 1: p += int(off)
            else: p  += 1
    return regs['b']

# P1
print(run(prog, 0, 0))

# P2
print(run(prog, 1, 0))