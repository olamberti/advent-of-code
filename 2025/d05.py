rs, ids = open('d05.txt').read().split('\n\n')                 # read & split input
rs = [tuple(map(int, r.split('-'))) for r in rs.split('\n')]   # parse ranges
ids = [int(i) for i in ids.split('\n')]                        # parse ids

p1 = 0                                                         # part 1                                
for id in ids:                                                 # loop through ids
    for r1, r2 in rs:                                          # loop through ranges             
        if r1 <= id <= r2:                                     # if id is in range                   
            p1 += 1                                            # add to count  
            break                                              # avoid double counting
print(p1)

p2, last = 0, 0                                                # part 2 & last number counted
for r1, r2 in sorted(rs):                                      # loop through sorted ranges
    start = max(r1, last + 1)                                  # determine new start   
    if start <= r2:                                            # new numbers to count?
        p2 += r2 - start + 1                                   # add to count   
        last = r2                                              # update last number counted
print(p2)