p1, p2 = 0, 0                                           # part1, part2                       

def jolt(n, b):                                         # max joltage with n digits from b
    if n == 1: return max(b)                            # base case
    n = n - 1                                           # reduce digit count                    
    m = max(b[:-n])                                     # finding max excluding last n digits                
    return m * 10 ** n + jolt(n, b[b.index(m)+1:])      # build number and recurse

for line in open('d03.txt').readlines():                # read each input line
    bs = [int(x) for x in line.strip()]                 # parse as list of integers 
    p1 += jolt(2, bs)                                   # part1: max 2-digit joltage    
    p2 += jolt(12, bs)                                  # part2: max 12-digit joltage

print(p1)
print(p2)