import re
import math

instructions, rest = open('d08.txt').read().split('\n\n')

network, dirs, posis = {}, {'L':0, 'R':1}, []
for line in rest.splitlines():
    node, left, right = re.findall(r'[\w][\w][\w]', line)
    network[node] = (left, right)
    if node[-1] == 'A': posis.append(node)

def next_pos(pos, steps):
    turn = dirs[instructions[steps % len(instructions)]]
    return network[pos][turn]

# Part 1
pos, steps = 'AAA', 0
while pos != 'ZZZ':
    pos = next_pos(pos, steps)
    steps += 1
print(steps)

# Part 2
memory, steps = [0] * len(posis), 0
while any([m == 0 for m in memory]):
    posis = [next_pos(pos, steps) for pos in posis]
    steps += 1
    for i, pos in enumerate(posis):
        if posis[i][-1] == 'Z' and memory[i] == 0: memory[i] = steps         
print(math.lcm(*memory))