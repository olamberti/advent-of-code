data, pages = open('d05.txt').read().split('\n\n')

rules = set()
for line in data.splitlines():
    rules.add(tuple(line.split('|')))
    
def is_right(vals):
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            if (vals[j], vals[i]) in rules:
                return False
    return True

p1, p2 = 0, 0
for page in pages.splitlines():
    page = page.split(',')
    if is_right(page):
        p1 += int(page[len(page)//2])
        continue
    while not is_right(page):
        for i in range(len(page)):
            for j in range(i + 1, len(page)):
                if (page[j], page[i]) in rules:
                    page[i], page[j] = page[j], page[i]            
    p2 += int(page[len(page)//2])

print(p1)
print(p2)