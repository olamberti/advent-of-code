p1 = 0 
for line in open('d07.txt').read().splitlines():
    if 'S' in line:
        s = line.index('S')
        beams = {s: 1}
        continue
    elif '^' not in line:
        continue
    
    new_beams = dict()
    for b, n in beams.items():
        if line[b] == '.':
           if b in new_beams: new_beams[b] += n
           else: new_beams[b] = n
        else:
            p1 += 1
            for x in (b-1, b+1):
                if x in new_beams: new_beams[x] += n
                else: new_beams[x] = n
    beams = new_beams

print(p1)
print(sum(new_beams.values()))