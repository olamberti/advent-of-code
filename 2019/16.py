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

# P1
for _ in range(100):
    sig = fft(sig)
print(sig[:8])