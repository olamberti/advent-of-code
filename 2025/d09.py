ps = [tuple(map(int, row.split(','))) for row in open('d09.txt')]

def area(a, b):
    (x1, y1), (x2, y2) = a, b
    return (abs(x2 - x1) + 1)*(abs(y2 - y1) + 1)

# Part 1
p1 = 0
for i in range(len(ps)):
    for j in range(i + 1, len(ps)):
        p1 = max(p1, area(ps[i], ps[j]))

print(p1)

# Part 2
# GL & HF :)