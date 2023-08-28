from intcode import IntCode
memory = [int(x) for x in open('21.txt').read().split(',')]

def ascii(inp):
    asci = []
    for com in inp:
        for c in com: asci.append(ord(c))
        asci.append(10)
    return asci

def run(code):
    prog, p = IntCode(memory), ''
    while not prog.halt:
        out = prog.run(ascii(code))
        if out and out > 127: p = out
        elif type(out) == int: p += chr(out)
    print(p)

# P1
part1 = ['NOT A T',
         'NOT C J',
         'OR T J',
         'AND D J',
         'WALK']
run(part1)

# P2
part2 = ['NOT A T',
         'NOT B J',
         'OR T J',
         'NOT C T',
         'OR T J',
         'AND D J',
         'NOT J T',
         'OR H T',
         'OR E T',
         'AND T J',
         'RUN']
run(part2)