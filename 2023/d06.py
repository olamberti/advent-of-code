import re
import math

def solve(time, dist):
    det = math.sqrt(time ** 2 - 4 * dist)
    v1 = math.floor((time - det) / 2 + 1)
    v2 = math.ceil((time + det) / 2 - 1)
    return v2 - v1 + 1

data = []
for line in open('d06.txt').read().splitlines():
    data.append([int(x) for x in re.findall(r'(\d+)', line)])

# Part 1
wins = []
for i in range(len(data[0])):
    t, d = data[0][i], data[1][i]
    wins.append(solve(t, d)) 
print(math.prod(wins))

# Part 2
t = int(''.join(str(x) for x in data[0]))
d = int(''.join(str(x) for x in data[1]))
print(solve(t, d))