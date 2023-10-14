from copy import deepcopy as dp

cs = set()
for line in open('d24.txt').read().splitlines():
    cs.add(tuple([int(x) for x in line.split('/')]))

def build(bridge, comps, strength, length, longeststrength):
    p, ms, ml, mls = int(bridge.split('-')[-1]), strength, length, longeststrength
    for c1, c2 in comps:
        nb = None
        if c1 == p: nb = '-'.join([bridge, str(c1), str(c2)])
        elif c2 == p: nb = '-'.join([bridge, str(c2), str(c1)])
        if nb:
            nc = dp(comps)
            nc.remove((c1, c2))
            ns, nl, nls = build(nb, nc, strength + c1 + c2, length + 1, longeststrength + c1 + c2)
            ms = max(ms, ns)
            if nl == ml:
                mls = max(nls, mls)
            elif nl > ml:
                ml = nl
                mls = nls
    return ms, ml, mls
        
p1, _, p2 = build('0', cs, 0, 0, 0)
print(p1)
print(p2)