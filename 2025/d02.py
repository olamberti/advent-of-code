input, p1, p2 = open('d02.txt').read(), 0, 0

ns = [(int(a), int(b)) for a, b in (x.split('-') for x in input.split(','))]

def patterns(a, b):
    sa, sb, p1, p2 = str(a), str(b), set(), set()
    if len(sa) != len(sb):
        p11, p21 = patterns(a, int('9' * len(sa)))
        p12, p22 = patterns(int('1' + '0' * len(sa)), b)
        return p11 + p12, p21 + p22
    for i in range(1, 10**(len(sa)//2)):
        if len(sa) % len(str(i)) != 0:
            continue
        n = int(str(i) * (len(sa)//len(str(i))))
        if a <= n <= b:
            p2.add(n)
            if len(sa)//len(str(i)) == 2:
                p1.add(n)
    return sum(p1), sum(p2)

for a, b in ns:
    p11, p21 = patterns(a, b)
    p1 += p11
    p2 += p21

print(p1)
print(p2)