from collections import defaultdict

splits = 0 
for i, row in enumerate(open('d07.txt')):
    if i == 0:
        beams = {row.index('S'): 1}
        continue
    elif '^' not in row:
        continue
    
    new_beams = defaultdict(int)
    for b, n in beams.items():
        if row[b] == '.':
           new_beams[b] += n
        else:
            splits += 1
            new_beams[b-1] += n
            new_beams[b+1] += n
    beams = new_beams

print(splits)
print(sum(new_beams.values()))