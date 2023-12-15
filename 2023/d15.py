def hash(s):
    val = 0
    for ch in s:
        val = (val + ord(ch)) * 17 % 256
    return val

# Part 1
seq = open('d15.txt').read().split(',')
print(sum(hash(x) for x in seq))

# Part 2
boxes = [[] for _ in range(256)]
for step in seq:
    label = step[:-1] if '-' in step else step[:-2]
    id = hash(label)
    if '=' in step:
        foc = int(step[-1])
        for i, lens in enumerate(boxes[id]):
            if lens[0] == label:
                boxes[id][i][1] = int(foc)
                break
        else: boxes[id].append([label, int(foc)])
    else:
        for i, lens in enumerate(boxes[id]):
            if lens[0] == label: boxes[id].pop(i)

print(sum(b * s * lens[1] for b, box in enumerate(boxes, 1) for s, lens in enumerate(box, 1)))