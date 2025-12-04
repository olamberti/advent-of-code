rolls = set()                                                   # set for rolls
for y, line in enumerate(open('d04.txt').readlines()):          # read lines
    for x, e in enumerate(line.strip()):                        # read elements    
        if e == '@': rolls.add(x + y*1j)                        # add roll with complex coord        

def rem(rs):                                                    # remove rolls function  
    res = set()                                                 # result set
    for r in rs:                                                # loop through rolls
        ns = 0                                                  # neighbor count
        for a in (1, 1-1j, -1j, -1-1j, -1, -1+1j, 1j, 1+1j):    # adjacent coords
            if r + a in rs: ns += 1                             # count neighbors
        if ns < 4: res.add(r)                                   # add if < 4 neighbors
    return(res)                                                 # return result

gone, count = rem(rolls), 0                                     # initial removal & counter 
rolls -= gone                                                   # update rolls
count += len(gone)                                              # update count
print(count)                                                    # part 1 result

while len(gone) > 0:                                            # while rolls are removed      
    gone = rem(rolls)                                           # remove rolls
    rolls -= gone                                               # update rolls
    count += len(gone)                                          # update count
print(count)                                                    # part 2 result