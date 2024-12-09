diskmap = [*map(int, open('d09.txt').read())]

blocks, files, free, pos = [None] * sum(diskmap), {}, [], 0
for i, x in enumerate(diskmap):
    v = i // 2 if i % 2 == 0 else None
    if x:
        if i % 2 == 0:
            files[v] = (pos, x)
        else:
            free.append((pos, x))
        for n in range(x):
            blocks[pos] = v
            pos += 1

# Part 1
checksum, last = 0, len(blocks) - 1
for i in range(sum([x for x in diskmap[0::2]])):
    if blocks[i] is None:
        while blocks[last] is None:
            last -= 1
        checksum += blocks[last] * i
        last -= 1
    else:
        checksum += blocks[i] * i
print(checksum)

# Part 2
for id in sorted(list(files.keys()), reverse=True):
    start, size = files[id]
    for i, (pos, length) in enumerate(free):
        if pos > start:
            free = free[:i]
            break
        if length >= size:
            files[id] = (pos, size)
            if size == length:
                free.pop(i)
            else:
                free[i] = (pos + size, length - size)
            break

checksum = 0
for id, [pos, size] in files.items():
    for v in range(pos, pos + size):
        checksum += id * v
print(checksum)