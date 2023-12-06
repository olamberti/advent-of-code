import re
import math

def solve(time, dist):
    if time ** 2 - 4 * dist <= 0: return 0
    det = math.sqrt(time ** 2 - 4 * dist)
    v1 = math.floor((time - det) / 2 + 1)
    v2 = math.ceil((time + det) / 2 - 1)
    return v2 - v1 + 1

times, dists = [[int(x) for x in re.findall(r'(\d+)', line)] for line in open('d06.txt')]

# Part 1
wins = []
for t, d in zip(times, dists):
    wins.append(solve(t, d)) 
print(math.prod(wins))

# Part 2
t = int(''.join(str(x) for x in times))
d = int(''.join(str(x) for x in dists))
print(solve(t, d))