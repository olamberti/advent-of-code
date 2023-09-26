import re

regs = {}
for line in open('08.txt').read().splitlines():
    r, com, v = re.findall(r'(\w+) (\w+) (-?\d+)', line)[0]
    pass

# TODO: P1 & P2