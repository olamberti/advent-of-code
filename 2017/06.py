data = [int(x) for x in open('06.txt').read().split()]

states, ndata, steps = {}, tuple(data), 0
while ndata not in states:
    states[ndata] = steps; steps += 1; ndata = list(ndata)
    m = max(ndata)
    i = ndata.index(m)
    ndata[i] = 0
    for _ in range(m):
        i = (i + 1) % len(ndata); ndata[i] += 1
    ndata = tuple(ndata)

print(len(states))
print(steps - states[ndata])