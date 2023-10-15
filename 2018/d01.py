# P1
data, f = [], 0
for line in open('d01.txt').read().splitlines():
    data.append(int(line))
    f += data[-1]
print(f)

# P2
i, f, fs = 0, 0, set()
while f not in fs:
    fs.add(f)
    f += data[i]
    i = (i + 1) % len(data)
print(f)