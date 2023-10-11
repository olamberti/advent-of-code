prog = [line for line in open('d18.txt').read().splitlines()]


# P1
regs = {}
def get_val(x):
    if x.lstrip('-').isnumeric(): return int(x)
    if x in regs: return regs[x]
    regs[x] = 0
    return 0

pos, sound, rec = 0, None, None
while 0 <= pos < len(prog):
    ins = prog[pos].split()
    if ins[0] == 'snd': sound = get_val(ins[1])
    elif ins[0] == 'set':
        if ins[1] not in regs: regs[ins[1]] = 0
        regs[ins[1]] = get_val(ins[2])
    elif ins[0] == 'add':
        if ins[1] not in regs: regs[ins[1]] = 0
        regs[ins[1]] += get_val(ins[2])
    elif ins[0] == 'mul':
        if ins[1] not in regs: regs[ins[1]] = 0
        regs[ins[1]] *= get_val(ins[2])
    elif ins[0] == 'mod':
        if ins[1] not in regs: regs[ins[1]] = 0
        regs[ins[1]] %= get_val(ins[2])
    elif ins[0] == 'rcv':
        if get_val(ins[1]) != 0:
            rec = sound
            break
    elif ins[0] == 'jgz':
        if get_val(ins[1]) != 0: pos += get_val(ins[2]) - 1
    pos += 1

print(rec)

# P2
# TODO finish class and run two programs
class Prog():

    def __init__(self, prog, num):
        self.prog = prog
        self.regs = {'p': num}
        self.pos = 0
        self.queue = []
        self.halt = False
    
    def get_reg(self, x):
        if x.lstrip('-').isnumeric(): return int(x)
        if x in self.regs: return self.regs[x]
        self.regs[x] = 0
        return 0
        
    def run(self):
        self.halt, pack = False, []
        while not self.halt:
            if 0 <= self.pos < len(prog):
                self.halt = True
                break

            ins = prog[self.pos].split()
            if ins[0] == 'snd': pack.append(self.get_reg(ins[1]))
            elif ins[0] == 'rcv':
                if ins[1] not in self.regs: self.regs[ins[1]] = 0
                if self.queue: self.regs[ins[1]] = self.queue.pop(0)
                else:
                    self.halt = True
                    break
            elif ins[0] == 'set':
                if ins[1] not in self.regs: self.regs[ins[1]] = 0
                self.regs[ins[1]] = self.get_reg(ins[2])
            elif ins[0] == 'add':
                if ins[1] not in self.regs: self.regs[ins[1]] = 0
                self.regs[ins[1]] += self.get_reg(ins[2])
            elif ins[0] == 'mul':
                if ins[1] not in self.regs: self.regs[ins[1]] = 0
                self.regs[ins[1]] *= self.get_reg(ins[2])
            elif ins[0] == 'mod':
                if ins[1] not in self.regs: self.regs[ins[1]] = 0
                self.regs[ins[1]] %= self.get_reg(ins[2])   
            elif ins[0] == 'jgz':
                if self.get_reg(ins[1]) != 0: self.pos += self.get_reg(ins[2]) - 1
            self.pos += 1