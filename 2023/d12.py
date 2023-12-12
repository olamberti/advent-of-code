cache = {}

def arrangements(blocks, counts):
    key = (tuple(blocks), tuple(counts))
    if key in cache: return cache[key]

    if not blocks:
        if counts: return 0
        if not counts: return 1
    if not counts:
        if all(ch == '?' for block in blocks for ch in block): return 1
        else: return 0
    if sum(counts) > sum([len(block) for block in blocks]): return 0

    x, block, fits = counts[0], blocks[0], 0
    if x > len(block):
        if all(ch == '?' for ch in block): fits = arrangements(blocks[1:], counts)
        else: fits = 0
    elif block[0] == '?':
        fits = arrangements([block[1:]] + blocks[1:], counts)
        fits += arrangements(['#' + block[1:]] + blocks[1:], counts)
    elif block[0] == '#' and len(block) == x:
        fits = arrangements(blocks[1:], counts[1:])
    elif block[0] == '#' and block[x] == '?':
        fits = arrangements([block[x+1:]] + blocks[1:], counts[1:])

    cache[key] = fits
    return fits

for p2 in (False, True):
    total = 0
    for line in open('d12.txt'):
        springs, counts = line.split()
        counts = [int(x) for x in counts.split(',')]
        if p2:
            springs = '?'.join(5 * [springs])
            counts = 5 *counts
        blocks = springs.replace('.', ' ').split()
        total += arrangements(blocks, counts)
    print(total)