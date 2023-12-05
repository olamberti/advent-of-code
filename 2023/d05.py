import re

data = open('d05.txt').read().split('\n\n')
numbers = [int(x) for x in re.findall(r'(\d+)', data[0])]
ranges = list(zip(numbers[0::2], [sum(x)-1 for x in zip(numbers[0::2], numbers[1::2])]))

for line in data[1:]:
    # Input parsing
    mappings = []
    for mapping in line.splitlines()[1:]:
        vals = [int(x) for x in re.findall(r'(\d+)', mapping)]
        mappings.append((vals[1], vals[1] + vals[2] - 1, vals[0] - vals[1]))
    mappings = sorted(mappings)

    # Part 1
    for i, number in enumerate(numbers):
        for low, high, diff in mappings:
            if low <= number <= high:
                numbers[i] += diff
                break
    
    # Part 2
    cutted_ranges = []
    for r1, r2 in ranges:
        cuts = set()
        for m1, m2, diff in mappings:
            if r1 <= m1 <= r2: cuts.add(m1)
            if r1 <= m2 <= r2: cuts.add(m2 + 1)
        for cut in sorted(list(cuts)):
            if cut == 0: continue
            cutted_ranges.append((r1, cut - 1))
            r1 = cut
        cutted_ranges.append((r1, r2))
    
    ranges, new_ranges = sorted(cutted_ranges), []
    for r1, r2 in ranges:
        for m1, m2, diff in mappings:
            if r2 < m1 or m2 < r1: continue
            else:
                new_ranges.append((r1 + diff, r2 + diff))
                break
        else: new_ranges.append((r1, r2))
    ranges = sorted(new_ranges)

print(min(numbers))
print(ranges[0][0])