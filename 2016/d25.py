inst = []
for line in open('d25.txt').read().splitlines():
    inst.append(line.split())

def get_val(x, regs):
    if x in regs: return regs[x]
    return int(x)

def run(regs, prog):
    i, op = 0, []
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
        elif p[0] == 'out':
            op.append(get_val(p[1], regs))
            if sum(op[::2]) != 0 or sum(op[1::2]) != len(op[1::2]): return False
            elif len(op) == 100: return True
        i += 1
    return(regs['a'])

a = 1
while not run({'a':a, 'b':0, 'c':0, 'd':0}, inst):
    a += 1
print(a)