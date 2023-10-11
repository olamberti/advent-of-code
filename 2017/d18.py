from collections import defaultdict
prog = [line.split() for line in open('d18.txt').read().splitlines()]

# P1
regs = defaultdict(int)
def get(x):
    if x.lstrip('-').isnumeric(): return int(x)
    return regs[x]

pos, sound, rec = 0, None, None
while 0 <= pos < len(prog):
    ins = prog[pos]
    if ins[0] == 'snd': sound = get(ins[1])
    elif ins[0] == 'set': regs[ins[1]] = get(ins[2])
    elif ins[0] == 'add': regs[ins[1]] += get(ins[2])
    elif ins[0] == 'mul': regs[ins[1]] *= get(ins[2])
    elif ins[0] == 'mod': regs[ins[1]] %= get(ins[2])
    elif ins[0] == 'rcv':
        if get(ins[1]) != 0:
            rec = sound
            break
    elif ins[0] == 'jgz':
        if get(ins[1]) > 0: pos += get(ins[2]) - 1
    pos += 1

print(rec)

# P2
class Prog():

    def __init__(self, num):
        self.regs = defaultdict(int)
        self.regs['p'] = num
        self.pos = 0
        self.queue = []
        self.halt = False
        self.sent = 0
    
    def get(self, x):
        if x.lstrip('-').isnumeric(): return int(x)
        return self.regs[x]
        
    def run(self):
        self.halt, pack = False, []
        while not self.halt:
            if self.pos < 0 or self.pos >= len(prog):
                self.halt = True
                break

            ins = prog[self.pos]
            if ins[0] == 'snd':
                pack.append(self.get(ins[1]))
                self.sent += 1
            elif ins[0] == 'rcv':
                if self.queue: self.regs[ins[1]] = self.queue.pop(0)
                else:
                    self.halt = True
                    break
            elif ins[0] == 'set': self.regs[ins[1]] = self.get(ins[2])
            elif ins[0] == 'add': self.regs[ins[1]] += self.get(ins[2])
            elif ins[0] == 'mul': self.regs[ins[1]] *= self.get(ins[2])
            elif ins[0] == 'mod': self.regs[ins[1]] %= self.get(ins[2])   
            elif ins[0] == 'jgz':
                if self.get(ins[1]) > 0: self.pos += self.get(ins[2]) - 1
            self.pos += 1
        return pack
    
progs, act = [Prog(0), Prog(1)], 0

while (progs[0].halt == False or progs[1].halt == False) or (len(progs[0].queue) + len(progs[1].queue) > 0):
    progs[1-act].queue.extend(progs[act].run())
    act = 1 - act

print(progs[1].sent)