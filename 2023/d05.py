import re

data = open('d05.txt').read().split('\n\n')
numbers = [int(x) for x in re.findall(r'(\d+)', data[0])]
ranges = list(zip(numbers[0::2], [sum(x)-1 for x in zip(numbers[0::2], numbers[1::2])]))

for i, line in enumerate(data[1:]):
    # Input parsing
    mappings = []
    for mapping in line.splitlines()[1:]:
        vals = [int(x) for x in re.findall(r'(\d+)', mapping)]
        mappings.append((vals[1], vals[1] + vals[2] - 1, vals[0] - vals[1]))
    mappings = sorted(mappings)

    # Part 1
    for j, number in enumerate(numbers):
        for low, high, diff in mappings:
            if low <= number <= high:
                numbers[j] += diff
                break
    
    # Part 2
    cutted_ranges = []
    for n1, n2 in ranges:
        cuts = set()
        for r1, r2, diff in mappings:
            if n1 <= r1 <= n2: cuts.add(r1)
            if n1 <= r2 <= n2: cuts.add(r2 + 1)
        for cut in sorted(list(cuts)):
            if cut == 0: continue
            cutted_ranges.append((n1, cut - 1))
            n1 = cut
        cutted_ranges.append((n1, n2))
    
    ranges, new_ranges = sorted(cutted_ranges), []   
    for n1, n2 in ranges:
        for r1, r2, diff in mappings:
            if n2 < r1 or r2 < n1: continue
            else:
                new_ranges.append((n1 + diff, n2 + diff))
                break
        else: new_ranges.append((n1, n2))
    ranges = sorted(new_ranges)

print(min(numbers))
print(ranges[0][0])