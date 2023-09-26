import re

regs, coms, p2 = {}, {'inc': 1, 'dec': -1}, 0

def get_val(x):
    if x not in regs: regs[x] = 0
    return regs[x]

def inc_val(x, k):
    if x not in regs: regs[x] = k
    else: regs[x] += k

for line in open('08.txt').read().splitlines():
    r1, c, v, r2, cond = re.findall(r'(\w+) (\w+) (-?\d+) if (\w+)(.*)', line)[0]
    v = int(v) * coms[c]
    if eval(str(get_val(r2)) + cond): inc_val(r1, v)
    p2 = max(max(regs.values()), p2)

print(max(regs.values()))
print(p2)