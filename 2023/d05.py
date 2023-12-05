import re
input = open('d05.txt').read().split('\n\n')

for i, line in enumerate(input):
    if i == 0:
        numbers, ranges = [int(x) for x in re.findall(r'(\d+)', line)], []
        for n in range(len(numbers)//2):
            ranges.append((numbers[2*n], numbers[2*n] + numbers[2*n+1] - 1))
        continue

    rules, maps = [], line.splitlines()[1:]
    for rule in maps:
        rule = [int(x) for x in re.findall(r'(\d+)', rule)]
        rules.append((rule[1], rule[1] + rule[2] - 1, rule[0] - rule[1]))
    rules = sorted(rules)

    # Part 1
    for n in range(len(numbers)):
        for low, high, diff in rules:
            if low <= numbers[n] <= high:
                numbers[n] += diff
                break
    
    # Part 2
    cutted_ranges = []
    for n1, n2 in ranges:
        cuts = set()
        for r1, r2, diff in rules:
            if n1 <= r1 <= n2: cuts.add(r1)
            if n1 <= r2 <= n2: cuts.add(r2 + 1)
        if cuts:
            for c in sorted(list(cuts)):
                if c == 0: continue
                cutted_ranges.append((n1, c - 1))
                n1 = c
        cutted_ranges.append((n1, n2))
    ranges, new_ranges = sorted(cutted_ranges), []   
    for n1, n2 in ranges:
        for r1, r2, diff in rules:
            if n2 < r1 or r2 < n1: continue
            else:
                new_ranges.append((n1 + diff, n2 + diff))
                break
        else: new_ranges.append((n1, n2))
    ranges = sorted(new_ranges)

print(min(numbers))
print(ranges[0][0])