diskmap = [*map(int, open('d09.txt').read())]

blocks, files, free = [None] * sum(diskmap), {}, {}
pos = 0
for i in range(len(diskmap)):
    v = i // 2 if i % 2 == 0 else None
    if diskmap[i]:
        if i % 2 == 0:
            files[v] = [pos, diskmap[i]]
        else:
            free[pos] = diskmap[i]
        for n in range(diskmap[i]):
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
    if all(x < size for x in free.values()):
        continue
    for pos in sorted(free.keys()):
        if free[pos] >= size and pos < start:
            files[id] = [pos, size]
            rem = free.pop(pos) - size
            if rem:
                free[pos + size] = rem
            break

checksum = 0
for id, [pos, size] in files.items():
    for v in range(pos, pos + size):
        checksum += id * v
print(checksum)