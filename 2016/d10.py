import re
bots, rules, outputs = {}, {}, {}

for line in open('10.txt').read().splitlines():
    p = [int(x) for x in re.findall(r'\d+', line)]
    if 'value' in line:
        if p[1] in bots: bots[p[1]].append(p[0])
        else: bots[p[1]] = [p[0]]
    else:
        line = line.split()
        t1, t2 = line[5], line[10]
        rules[p[0]] = ((t1, p[1]), (t2, p[2]))

def active_bot(bots):
    for b, ch in bots.items():
        if len(ch) == 2: return b
    return None

while active_bot(bots):
    bot = active_bot(bots)
    chips = sorted(bots[bot])
    if chips == [17, 61]: print(bot)
    for i, chip in enumerate(chips):
        t, id = rules[bot][i]
        if t == 'bot':
            if id in bots: bots[id].append(chip)
            else: bots[id] = [chip]
        elif t == 'output':
           outputs[id] = chip
    bots[bot] = []
print(outputs[0] * outputs[1] * outputs[2])