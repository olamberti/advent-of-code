def hash(s):
    val = 0
    for ch in s:
        val = (val + ord(ch)) * 17 % 256
    return val

# Part 1
seq = open('d15.txt').read().split(',')
print(sum(hash(x) for x in seq))

# Part 2
boxes, lenses = [[] for _ in range(256)], {}
for step in seq:
    label = step[:-1] if '-' in step else step[:-2]
    id = hash(label)
    if '=' in step:
        lenses[label] = int(step[-1])
        if label not in boxes[id]: boxes[id].append(label)
    else:
        if label in boxes[id]: boxes[id].remove(label)

print(sum(b * s * lenses[label] for b, box in enumerate(boxes, 1) for s, label in enumerate(box, 1)))