from functools import cache

outs = dict()
for row in open('d11.txt').read().splitlines():
    start, *ends = row.split(' ')
    outs[start[:-1]] = ends

@cache
def n(pos, dest):
    if pos == dest: return 1
    if pos == 'out': return 0
    return sum(n(out, dest) for out in outs[pos])

# Part 1
print(n('you', 'out'))

# Part 2:
o1 = n('svr','fft') * n('fft','dac') * n('dac','out')
o2 = n('svr','dac') * n('dac','fft') * n('fft','out')
print(o1 + o2)