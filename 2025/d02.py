input, p1 = open('d02.txt').read(), 0

ns = [(int(a), int(b)) for a, b in (x.split('-') for x in input.split(','))]

for a, b in ns:
    sa, sb = str(a), str(b)
    if len(sa) % 2 == 1 & len(sa) == len(sb):
        continue
    if len(sa) % 2 == 1:
        smin = ('1' + (len(sa) - 1) // 2 * '0') * 2
    else:
        smin = sa
    if len(sb) % 2 == 1:
        smax = '9' * (len(sb) - 1)
    else:
        smax = sb

    smin = [int(smin[:len(smin)//2]), int(smin[len(smin)//2:])]
    smax = [int(smax[:len(smax)//2]), int(smax[len(smax)//2:])]

    start = smin[0] if smin[0] >= smin[1] else smin[0] + 1
    stop = smax[0] if smax[0] <= smax[1] else smax[0] - 1

    if stop < start:
        continue
    for i in range(start, stop + 1):
        n = int(str(i) * 2)
        p1 += n

print(p1)