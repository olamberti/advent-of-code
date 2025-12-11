from functools import cache

outs = dict()
for row in open('d11.txt').read().splitlines():
    start, *ends = row.split(' ')
    outs[start[:-1]] = ends

@cache
def n(pos, fft, dac):
    if pos == 'out': return 1 * fft * dac
    elif pos == 'fft': fft = 1
    elif pos == 'dac': dac = 1
    return sum(n(out, fft, dac) for out in outs[pos])

print(n('you', 1, 1))
print(n('svr', 0, 0))