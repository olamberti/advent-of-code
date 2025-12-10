# Read input point list
ps = [tuple(map(int, row.split(','))) for row in open('d09.txt')]

# Rectangle area (inclusive grid)
def area(a, b):
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)

# Normalized direction vector (only horizontal / vertical)
def nv(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    l = abs(dx) + abs(dy)
    return dx // l, dy // l

# Perimeter for polygon points (only horizontal / vertical edges)
def length(poly):
    ans = 0
    for i in range(len(poly)):
        a, b = poly[i], poly[i % len(poly)]
        ans += max(abs(b[0] - a[0]), abs(b[1] - a[1]))
    return ans

# Check if rectangle AB does not intersect any edges
def isinside(a, b, es):
    x1, x2 = sorted((a[0], b[0]))
    y1, y2 = sorted((a[1], b[1]))

    for (ex1, ey1), (ex2, ey2) in es:
        # bounding-box intersection test
        if not (max(ex1, ex2) < x1 or
                min(ex1, ex2) > x2 or
                max(ey1, ey2) < y1 or
                min(ey1, ey2) > y2):
            return False
    return True
     
# ------------------ PART 1 ------------------
p1 = 0
for i in range(len(ps)):
    for j in range(i + 1, len(ps)):
        p1 = max(p1, area(ps[i], ps[j]))

print(p1)

# ------------------ PART 2 ------------------

# Build bisector-shifted points
bs = []
for i in range(len(ps)):
    p1, p2, p3 = ps[i - 1], ps[i], ps[(i + 1) % len(ps)]
    n1, n2 = nv(p1, p2), nv(p2, p3)

    # Two possible bisector sides
    pb1 = (p2[0] + 0.1 * (n1[0] - n2[0]),
           p2[1] + 0.1 * (n1[1] - n2[1]))
    pb2 = (p2[0] + 0.1 * (n2[0] - n1[0]),
           p2[1] + 0.1 * (n2[1] - n1[1]))
    bs.append((pb1, pb2))

# Choose correct winding (b1 or b2) and build edges
b1, b2 = [bs[0][0]], [bs[0][1]]
for i in range(1, len(ps)):
    p1, p2 = bs[i]
    if p1[0] == b1[i-1][0] or p1[1] == b1[i-1][1]:
        b1.append(p1); b2.append(p2)
    else:
        b1.append(p2); b2.append(p1)

b = b1 if length(b1) > length(b2) else b2
edges = [(b[i], b[(i + 1) % len(b)]) for i in range(len(b))]

# Find max area rectangle inside boundary
p2 = 0
for i in range(len(ps)):
    for j in range(i + 1, len(ps)):
        a = area(ps[i], ps[j])
        if a >= p2 and isinside(ps[i], ps[j], edges):
            p2 = a

print(p2)