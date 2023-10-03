from copy import deepcopy as dp

sig = [int(x) for x in open('d16.txt').read()]
base = [0, 1, 0, -1]

# P1
def fft(inp):
    out = []
    for k in range(1, len(inp) + 1):
        pattern = sum([k * [n] for n in base], [])
        val = 0
        for i, x in enumerate(inp):
            w = pattern[(i + 1) % len(pattern)]
            val += x * w
        out.append(abs(val) % 10)
    return out

p1 = dp(sig)
for _ in range(100):
    p1 = fft(p1)
print(''.join(str(x) for x in p1[:8]))

# P2
def ffs(inp):
    out, val = [], 0
    for x in inp[::-1]:
        val = (val + x) % 10
        out.append(val)
    return out[::-1]

N = 10_000
offset, p2 = int(''.join(str(x) for x in sig[:7])), dp(sig) * N
p2 = p2[offset:]

for _ in range(100):
    p2 = ffs(p2)
print(''.join(str(x) for x in p2[:8]))