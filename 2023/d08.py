import re
import math

insts, rest = open('d08.txt').read().split('\n\n')

network, posis, dirs = {}, [], {'L':0, 'R':1}
for line in rest.splitlines():
    node, left, right = re.findall(r'[\w][\w][\w]', line)
    network[node] = (left, right)
    if node[-1] == 'A': posis.append(node)

# Part 1
pos, steps = 'AAA', 0
while pos != 'ZZZ':
    turn = dirs[insts[steps % len(insts)]]
    pos = network[pos][turn]
    steps += 1
print(steps)

# Part 2
memory, steps = [0] * len(posis), 0
while any([m == 0 for m in memory]):
    turn = dirs[insts[steps % len(insts)]]
    steps += 1
    for i, pos in enumerate(posis):
        posis[i] = network[pos][turn]
        if posis[i][-1] == 'Z' and memory[i] == 0:
            memory[i] = steps
             
print(math.lcm(*memory))