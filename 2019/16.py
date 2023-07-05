sig = open('16.txt').read()
base = [0, 1, 0, -1]

def fft(sig):
    out = ""
    for k in range(1, len(sig) + 1):
        pattern = sum([k * [n] for n in base], [])
        val = 0
        for i, x in enumerate(sig):
            w = pattern[(i + 1) % len(pattern)]
            val += int(x) * w
        out += str(abs(val) % 10)
    return out

#P1
p1 = sig
for _ in range(100):
    p1 = fft(p1)
print(p1[:8])

#P2
N = 10_000
offset = int(sig[:8])
print(offset)