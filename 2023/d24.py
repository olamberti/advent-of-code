import re
import sympy

low, high = 200000000000000, 400000000000000
hailstones = [tuple(int(x) for x in re.findall(r'(-?\d+)', line)) for line in open("d24.txt")]

# Part 1 - Line intersection of y1 = ax + c and y2 = bx + d
total = 0
for i, hs1 in enumerate(hailstones):
    for hs2 in hailstones[i+1:]:
        px1, py1, pz1, vx1, vy1, vz1 = hs1
        px2, py2, pz2, vx2, vy2, vz2 = hs2
        a, b = vy1 / vx1, vy2 / vx2
        c, d = py1 - a * px1, py2 - b * px2
        if a == b and c != d: continue # parallel, not equal
        x = (d - c) / (a - b)
        y = a * x + c
        if low <= x <= high and low <= y <= high: # in range and both positive time
            if (((x > px1 and vx1 > 0) or (x < px1 and vx1 < 0)) and # positive time for #1
                ((x > px2 and vx2 > 0) or (x < px2 and vx2 < 0))):   # positive time for #2
                total += 1
print(total)

# Part 2 - Setting up a system of equations for the first three stones (9 equations, 9 unknowns)
px0, py0, pz0, vx0, vy0, vz0 = hailstones[0]
px1, py1, pz1, vx1, vy1, vz1 = hailstones[1]
px2, py2, pz2, vx2, vy2, vz2 = hailstones[2]
pxr, pyr, pzr, vxr, vyr, vzr, t0, t1, t2 = sympy.symbols('pxr pyr pzr vxr vyr vzr t0 t1 t2')
# First stone
eq1 = sympy.Eq(pxr + vxr * t0, px0 + vx0 * t0)
eq2 = sympy.Eq(pyr + vyr * t0, py0 + vy0 * t0)
eq3 = sympy.Eq(pzr + vzr * t0, pz0 + vz0 * t0)
# Second stone
eq4 = sympy.Eq(pxr + vxr * t1, px1 + vx1 * t1)
eq5 = sympy.Eq(pyr + vyr * t1, py1 + vy1 * t1)
eq6 = sympy.Eq(pzr + vzr * t1, pz1 + vz1 * t1)
# Third stone
eq7 = sympy.Eq(pxr + vxr * t2, px2 + vx2 * t2)
eq8 = sympy.Eq(pyr + vyr * t2, py2 + vy2 * t2)
eq9 = sympy.Eq(pzr + vzr * t2, pz2 + vz2 * t2)
sol = sympy.solve([eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9], [pxr, pyr, pzr, vxr, vyr, vzr, t0, t1, t2])
print(sum(sol[0][:3]))