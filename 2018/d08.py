from collections import deque as dq

input = dq([int(x) for x in open('d08.txt').read().split()])

def node(data):
    # Header
    chn = data.popleft()
    mde = data.popleft()
    total_sum, metadata, childs, val = 0, [], [], 0
    # Process child nodes
    for _ in range(chn):
        ms, chv = node(data)
        total_sum += ms
        childs.append(chv)
    # Proces metadata
    for _ in range(mde):
        metadata.append(data.popleft())
    total_sum += sum(metadata)
    # Calculate node value
    if chn == 0: return total_sum, sum(metadata)
    for m in metadata:
        if m - 1 in range(chn): val += childs[m - 1]
    return total_sum, val

p1, p2 = node(input)
print(p1)
print(p2)