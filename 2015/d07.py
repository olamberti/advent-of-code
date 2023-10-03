import numpy as np
from collections import deque as dq

# Process bitwise operations
def sim(insts):
    insts, vals = dq(insts), {}
    while insts:
        curr = insts.popleft()
        # NOT
        if curr[0] == 'NOT':
            var, tar = curr[1], curr[-1]
            if var not in vals.keys():
                insts.append(curr)
                continue
            vals[tar] = ~vals[var]
        # LSHIFT / RSHIFT
        elif curr[1] == 'LSHIFT' or  curr[1] == 'RSHIFT':
            var, n, tar = curr[0], int(curr[2]), curr[-1]
            if var not in vals.keys():
                insts.append(curr)
                continue
            if curr[1] == 'LSHIFT': vals[tar] = vals[var] << n
            elif curr[1] == 'RSHIFT': vals[tar] = vals[var] >> n
        # AND / OR
        elif curr[1] == 'AND' or  curr[1] == 'OR':
            var1, var2, tar = curr[0], curr[2], curr[-1]
            if var1.isnumeric(): p1 = np.uint16(var1)
            elif var1 not in vals.keys():
                insts.append(curr)
                continue
            else: p1 = vals[var1]
            if var2.isnumeric(): p2 = np.uint16(var2)
            elif var2 not in vals.keys():
                insts.append(curr)
                continue
            else: p2 = vals[var2]
            if curr[1] == 'AND': vals[tar] = p1 & p2
            elif curr[1] == 'OR': vals[tar] = p1 | p2
        # EQUALITY
        elif curr[1] == '->':
            var, tar = curr[0], curr[-1]
            if var.isnumeric():
                vals[tar] = np.uint16(var)
                continue
            if var not in vals.keys():
                insts.append(curr)
                continue
            vals[tar] = vals[var]
    return vals

# P1
insts = []
for line in open('07.txt').readlines():
    line = line.strip().split(' ')
    insts.append(line)

vals = sim(insts)
p1 = vals['a']
print(p1)

# P2
insts = []
for line in open('07.txt').readlines():
    line = line.strip().split(' ')
    if line[-1] == 'b':
        line[0] = str(p1)
    insts.append(line)
insts = dq(insts)

vals = sim(insts)
p2 = vals['a']
print(p2)