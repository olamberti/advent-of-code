c, lengths = [i for i in range(256)], [int(x) for x in open('10.txt').read().split(',')]

# P1
i, ss = 0, 0
for l in lengths:
    if i + l <= len(c):
        c[i:i+l] = c[i:i+l][::-1]
    else:
        l1, l2 = len(c[i:]), len(c[:(i+l)-len(c)])
        cut = (c[i:] + c[:(i+l)-len(c)])[::-1]
        c[i:], c[:(i+l)-len(c)] = cut[:l1], cut[l1:]
    i = (i + l + ss) % len(c)
    ss += 1
print(c[0] * c[1])

# P2
# TODO