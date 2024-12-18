wall = [x + y*1j for r in open('d18.txt').readlines()
                 for x, y in [map(int, r.strip().split(','))]]
W, H, F = 70, 70, 1024

def bfs(cut):
    start, goal, steps = 0, W + H*1j, 0
    front, seen = {start}, {start}
    walls = set(wall[:cut])
    while front:
        new = set()
        steps += 1
        for pos in front:
            for d in [1, -1, 1j, -1j]:
                npos = pos + d
                if npos == goal:
                    return steps
                if not (0 <= npos.real <= W and 0 <= npos.imag <= H):
                    continue
                if npos in walls or npos in seen:
                    continue
                seen.add(npos)
                new.add(npos)
        front = new
    return 0

print(bfs(F))

low, high = F, len(wall)
while high - low > 1:
    i = (low + high) // 2
    if bfs(i): low = i
    else: high = i
print(int(wall[low].real), int(wall[low].imag), sep=',')