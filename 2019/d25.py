from intcode import IntCode
import itertools
memory = [int(x) for x in open('d25.txt').read().split(',')]

def ascii(command):
    return [ord(c) for c in command] + [10]

prog = IntCode(memory)
text, inp = '', []
todo = ['north','north','take sand','south', 'south','south','take space heater','south','east','take loom',
        'west', 'north','west','take wreath','south','take space law space brochure','south','take pointer',
        'north','north','east','north','west','south','take planetoid','north','west','take festive hat',
        'south','west', 'north'] # hand-crafted based on playing manually
items, inv = [], []
for command in todo:
    if 'take' in command: items.append(command[5:])
options = []
for x in range(len(items) + 1):
    for subset in itertools.combinations(items, x):
        options.append(subset)
options = [('sand', 'wreath','pointer','planetoid')] # after winning the correct combo is available

while not prog.halt:
    text += chr(prog.run(inp))
    if 'airlock."\n' in text:
        print(text.split(' ')[-8])
        break
    if text [-2:] == 'd?':
        # print(text)
        if todo:
            command = todo.pop(0)
            if 'take' in command: inv.append(command[5:])
            elif 'drop' in command: inv.remove(command[5:])
            inp = ascii(command)
        elif options:
            for item in inv:
                todo.append('drop ' + item)
            option = options.pop(0)
            for item in option:
                todo.append('take ' + item)
            todo.append('north')
            inp = ascii('north\n')
        else:
            inp = ascii(input())
        text = ''