from collections import deque as dq

top, bottom = open('d24.txt').read().split('\n\n')
wires = {w: int(val) for w, val in (line.split(': ')
                     for line in top.splitlines())}
queue = dq([(a, op, b, t) for line in bottom.splitlines()
                          for a, op, b, _, t in [line.split(' ')]])

# Part 1
p1 = 0
while queue:
    a, op, b, t = queue.popleft()
    if a in wires and b in wires:
        if op == 'AND': res = wires[a] & wires[b]
        elif op == 'OR': res = wires[a] | wires[b]
        elif op == 'XOR': res = wires[a] ^ wires[b]
        wires[t] = res
        if t.startswith('z') and res: p1 += 2 ** int(t[1:])
    else:
        queue.append((a, op, b, t))
print(p1)

# Part 2
bits = len(top.splitlines()) // 2
rules = {(a, op, b, t) for line in bottom.splitlines()
                       for a, op, b, _, t in [line.split(' ')]}

wrong = set()
for rule in rules:
    a, op, b, t = rule
    
    match op:
        # Checking the OR gates
        case 'OR':
            if t.startswith('z') and int(t[1:]) != bits:
                wrong.add(t)
            else:             
                for a2, op2, b2, _ in rules:
                    if t in (a2, b2) and op2 == 'OR':
                        wrong.add(t)
        # Checking the AND gates
        case 'AND':
            if t.startswith('z'):
                wrong.add(t)             
            elif {a, b} == {'x00', 'y00'}:
                for a2, op2, b2, _ in rules:
                    if t in (a2, b2) and op2 == 'OR':
                        wrong.add(t)
            else:                   
                for a2, op2, b2, t2 in rules:
                    if t in (a2, b2) and op2 != 'OR':
                        wrong.add(t)
        # Checking the XOR gates
        case 'XOR':
            if t == 'z00' and {a[0], b[0]} == {'x00', 'y00'}:
                wrong.add(t)      
            elif {a[0], b[0]} == {'x', 'y'} and t.startswith('z') and t != 'z00':
                wrong.add(t)
            elif {a[0], b[0]} != {'x', 'y'} and not t.startswith('z'):
                wrong.add(t)
            else:
                for a2, op2, b2, _ in rules:
                    if t in (a2, b2) and op2 == 'OR':
                        wrong.add(t)
                        
print(','.join(sorted(list(wrong))))