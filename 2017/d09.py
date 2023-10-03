data = open('d09.txt').read()

i, lvl, garbage, p1, p2 = 0, 0, False, 0, 0
while i < len(data):
    if not garbage:
        if data[i] == '<': garbage = True
        elif data[i] == '{': lvl += 1
        elif data[i] == '}': p1 += lvl; lvl -= 1
    else:
        if data[i] == '!': i += 1
        elif data[i] == '>': garbage = False
        else: p2 += 1
    i += 1

print(p1)
print(p2)