inp = open('01.txt').read()

# P1
print(inp.count('(') - inp.count(')'))

# P2
floor = 0
for i, c in enumerate(inp):
    if c == '(': floor += 1
    else: floor -= 1
    if floor == -1:
        print(i + 1)
        break