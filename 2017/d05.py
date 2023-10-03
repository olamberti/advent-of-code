from copy import deepcopy as dp
data = [int(x) for x in open('d05.txt').read().splitlines()]

def run(input, p2 = False):
    data = dp(input)
    i, steps = 0, 0
    while i < len(data):
        ni = i + data[i]
        if p2 and data[i] >= 3: data[i] -= 1
        else: data[i] += 1
        i = ni
        steps += 1
    return(steps)

print(run(data))
print(run(data, True))