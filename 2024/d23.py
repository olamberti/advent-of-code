network = {}

for line in open('d23.txt').read().splitlines():
    a, b = line.split('-')
    if a not in network: network[a] = set()
    if b not in network: network[b] = set()
    network[a].add(b)
    network[b].add(a)

threes = set()
for a in network:
    for b in network[a]:
        for c in network[b]:
            if c in network[a]:
                nodes = sorted([a, b, c])
                if any(x.startswith('t') for x in nodes):
                    threes.add(tuple(nodes))
print(len(threes))

queue = [set({a} | ns) for a, ns in network.items()]

while queue:
    clique = queue.pop(0)
    for a in clique:
        if not all(b in network[a] for b in clique - {a}):
            break
    else:
        print(','.join(sorted(list(clique))))
        break
    for a in clique:
        queue.append(clique - {a})