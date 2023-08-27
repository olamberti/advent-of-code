from collections import deque
from intcode import IntCode
memory = [int(x) for x in open('23.txt').read().split(',')]

progs, queues, packets, n = [], [], [], 50
for i in range(n):
    progs.append(IntCode((memory)))
    queues.append(deque([i]))

p1, idle = False, 0
natx, naty, lasty = None, None, None
while True:
    for i in range(n):
        if queues[i]:
            inp = queues[i].popleft()
        else: inp = -1
        da = progs[i].run(inp, True)
        if da == None: continue
        X = progs[i].run([], True)
        Y = progs[i].run([], True)
        if da == 255:
            if not p1:
                print(Y)
                p1 = True
            natx, naty = X, Y
        else: queues[da].extend([X, Y])
    if any(queues[i]): continue
    else: idle += 1
    if idle > 500:
        if naty == lasty:
            print(lasty)
            break
        lasty = naty
        idle = 0
        queues[0].extend([natx, naty])