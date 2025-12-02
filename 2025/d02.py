input, p1, p2 = open('d02.txt').read(), 0, 0         # input, part1, part2   
ns = [(int(a), int(b)) for a, b in                   # parsing input 
      (x.split('-') for x in input.split(','))]

def p(a, b):                                         # count patterns in [a, b]                  
    sa, sb, p1, p2 = str(a), str(b), set(), set()    # strings, set for part1 & part2
    if len(sa) != len(sb):                           # we split the range if lengths differ
        p11, p21 = p(a, int('9' * len(sa)))          # first recursive part
        p12, p22 = p(int('1' + '0' * len(sa)), b)    # second recursive part
        return p11 + p12, p21 + p22                  # return combined results
    for i in range(1, 10**(len(sa)//2)):             # generate pattern elements
        if len(sa) % len(str(i)) != 0: continue      # skip if not fitting
        n = int(str(i) * (len(sa)//len(str(i))))     # construct number from pattern
        if a <= n <= b:                              # check if in range
            p2.add(n)                                # part2: add to set
            if len(sa)//len(str(i)) == 2: p1.add(n)  # part1: only patterns of half length              
    return sum(p1), sum(p2)                          # return sums of set values

for a, b in ns:                                      # process all ranges    
    p11, p21 = p(a, b)                               # get patterns for range
    p1 += p11                                        # accumulate part1              
    p2 += p21                                        # accumulate part2

print(p1)
print(p2)