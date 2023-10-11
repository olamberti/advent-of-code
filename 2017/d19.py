paths, pos = {}, None

for x, line in enumerate(open('d19.txt').read().splitlines()):
    for y, c in enumerate(line):
        if c == ' ': continue
        else:
            paths[x + y*1j] = c
            if not pos: pos = x + y*1j

# P1
key, steps, d = '', 1, 1

while True:
    if pos + d in paths:
        pos = pos + d
        steps += 1
        if paths[pos] in '|-+': continue
        key = key + paths[pos]
    else:
        if pos + d * 1j in paths: d = d * 1j
        elif pos + d * -1j in paths: d = d * -1j
        else: break

print(key)
print(steps)