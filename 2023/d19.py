import re
import math

ws, ps = open('d19.txt').read().split('\n\n')
workflows = {}
for line in ws.split('\n'):
    name, rule = line.split('{')
    workflows[name] = rule[:-1].split(',')

# Part 1
def sortpart(x, m, a, s, workflow = 'in'):
    if workflow == 'R': return False
    if workflow == 'A': return True

    for rule in workflows[workflow]:
        if ':' in rule: 
            cond, tar = rule.split(':')
            if eval(cond): return sortpart(x, m, a, s, tar)
            else: continue
        else: return sortpart(x, m, a, s, rule)

p1 = 0
for part in ps.split('\n'):
    x, m, a, s = [int(x) for x in re.findall(r'(\d+)', part)]
    if sortpart(x, m, a, s): p1 += sum([x, m, a, s])
print(p1)

# Part 2
def sortrange(ranges, workflow = 'in'):
    if workflow == 'R': return 0
    if workflow == 'A': return math.prod(v[1] - v[0] + 1 for v in ranges.values())

    accepted = 0
    for rule in workflows[workflow]:
        if ':' in rule: 
            cond, tar = rule.split(':')
            var, rel, val = cond[0], cond[1], int(cond[2:])
            low, high = ranges[var]
            if rel == '<':
                okay = (low, val - 1)
                not_okay = (val, high)
            else:
                okay = (val + 1, high)
                not_okay = (low, val)
            new_ranges = dict(ranges)
            new_ranges[var] = okay
            accepted += sortrange(new_ranges, tar)
            ranges[var] = not_okay
        else: accepted += sortrange(ranges, rule)
    return accepted

ranges = {var: (1, 4000) for var in 'xmas'}
print(sortrange(ranges))