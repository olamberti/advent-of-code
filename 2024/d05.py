from collections import defaultdict
data, pages = open('d05.txt').read().split('\n\n')

rules = defaultdict(list)
for row in data.splitlines():
    a, b = row.split('|')
    rules[a].append(b)

def is_right(vals):
    for v in vals:
        for larger in rules[v]:
            if larger in vals and vals.index(larger) < vals.index(v):
                return False
    return True

p1, p2 = 0, 0
for page in pages.splitlines():
    page = page.split(',')
    if is_right(page):
        p1 += int(page[len(page)//2])
    else:
        while not is_right(page):
            for v in page:
                    for larger in rules[v]:
                        if larger in page and page.index(larger) < page.index(v):
                            page.remove(v)
                            page.insert(page.index(larger), v)
        p2 += int(page[len(page)//2])

print(p1)
print(p2)