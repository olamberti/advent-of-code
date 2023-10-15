import re

# Read in data and sort it
records = []
for line in open('d04.txt').read().splitlines():
    records.append(line)
records.sort()

# Process total sleep time (st) and sleeping minutes (sm) by guards
st, sm = {}, {}
for line in records:
    if 'Guard' in line:
        guard = int(re.findall(r'\d+',line)[-1])
        if guard not in st: st[guard] = 0
        if guard not in sm: sm[guard] = {}
    elif 'falls' in line:
        sleeps = int(re.findall(r'\d+',line)[-1])
    elif 'wakes'in line:
        wakes = int(re.findall(r'\d+',line)[-1])
        for m in range(sleeps, wakes):
            if m not in sm[guard]: sm[guard][m] = 0
            st[guard] += 1
            sm[guard][m] += 1 

# P1
p1t, p1n = 0, 0
for g, t in st.items():
    if t > p1t:
        p1g = g
        p1t = t
for m, n in sm[p1g].items():
    if n > p1n:
        p1n = n
        p1m = m
print(p1g * p1m)

# P2
p2n = 0
for g, data in sm.items():
    for m, n in data.items():
        if n > p2n:
            p2n = n
            p2m = m
            p2g = g
print(p2g * p2m)