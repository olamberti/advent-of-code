from collections import defaultdict

diskmap = [*map(int, open('d09.txt').read())]
blocks, files, free, pos = [], {}, defaultdict(list), 0
for i, x in enumerate(diskmap):
    id = i // 2 if i % 2 == 0 else None
    blocks += [id] * x
    if x:
        if i % 2 == 0:
            files[id] = (pos, x)
        else:
            free[x].append(pos)
        pos += x

# Part 1
checksum = 0
for i in range(sum([x for x in diskmap[0::2]])):
    if blocks[i] is None:
        while blocks[-1] is None:
            blocks.pop()
        checksum += blocks.pop() * i
    else:
        checksum += blocks[i] * i
print(checksum)

# Part 2
for id in sorted(list(files.keys()), reverse=True):
    start, size, pos = *files[id], float('inf')
    for length in range(size, 10):
        if free[length] and free[length][0] < pos:
            pos, space = free[length][0], length
    if pos < start:
        files[id], rem = (pos, size), space - size
        free[space].pop(0)
        if rem:
            free[rem].append(pos + size)
            free[rem].sort()

checksum = 0
for id, [pos, size] in files.items():
    checksum += id * size * (2 * pos + size - 1) // 2
print(checksum)