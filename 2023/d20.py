from collections import deque as dq
from copy import deepcopy as dc
import math

class Module:
    def __init__(self, type, targets):
        self.type = type
        self.targets = targets
        if type == '%':
            self.memory = 'off'
        else:
            self.memory = {}

# Load input, create modules and collect memories for &-modules
modules = {}
for line in open('d20.txt'):
    name, targets = line.strip().split(' -> ')
    if name[0] in '%&':
        type, name = name[0], name[1:]
    else: type = None
    modules[name] = Module(type, targets.split(', '))

for name, module in modules.items():
    for target in module.targets:
        if target in modules and modules[target].type == '&':
            modules[target].memory[name] = 'low'
copy = dc(modules)

# Communication handler function
def communicate(pulse, sender, receiver):
    global pulses, modules
    module = modules[receiver]
    if receiver == 'broadcaster':
        for target in module.targets: pulses.append((pulse, receiver, target))
    elif module.type == '%':
        if pulse == 'high': return
        if module.memory == 'off':
            module.memory = 'on'
            for target in module.targets: pulses.append(('high', receiver, target))
        else: #'on'
            module.memory = 'off'
            for target in module.targets: pulses.append(('low', receiver, target))
    elif module.type == '&':
        module.memory[sender] = pulse
        message = 'low' if all(v == 'high' for v in module.memory.values()) else 'high'
        for target in module.targets: pulses.append((message, receiver, target))

# Part1
low, high = 0, 0
for _ in range(1000):
    pulses = dq([('low', 'button', 'broadcaster')])
    while pulses:
        pulse, sender, receiver = pulses.popleft()
        if pulse == 'low': low += 1
        else: high += 1
        if receiver not in modules: continue
        communicate(pulse, sender, receiver)
print(low * high)

# Part2
steps, modules = 0, copy
source = [name for name, module in modules.items() if 'rx' in module.targets][0]
required = {name: 0 for name, module in modules.items() if source in module.targets}

while any(v == 0 for v in required.values()):
    steps += 1
    pulses = dq([('low', 'button', 'broadcaster')])
    while pulses:
        pulse, sender, receiver = pulses.popleft()
        if receiver not in modules: continue
        if receiver == source and pulse == 'high':
            if required[sender] ==  0: required[sender] = steps
        communicate(pulse, sender, receiver)
print(math.lcm(*required.values()))