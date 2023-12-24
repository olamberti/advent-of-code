import re
import sympy

low, high = 200000000000000, 400000000000000
hailstones = [tuple(int(x) for x in re.findall(r'(-?\d+)', line)) for line in open("d24.txt")]

# Part 1 - Line intersection of y1 = ax + c and y2 = bx + d
total = 0
for i, (px1, py1, _, vx1, vy1, _) in enumerate(hailstones):
    for (px2, py2, _, vx2, vy2, _) in hailstones[i+1:]:
        a, b = vy1 / vx1, vy2 / vx2
        c, d = py1 - a * px1, py2 - b * px2
        if a == b and c != d: continue # parallel and not equal lines
        x = (d - c) / (a - b)
        y = a * x + c
        if low <= x <= high and low <= y <= high: # in range
            if (vx1 * (x - px1) > 0 and vx2 * (x - px2) > 0): # positive time for both stones
                total += 1
print(total)

# Part 2 - Setting up a system of equations for the first three stones (9 equations, 9 unknowns)
pxr, pyr, pzr, vxr, vyr, vzr, t0, t1, t2 = sympy.symbols('pxr pyr pzr vxr vyr vzr t0 t1 t2')
equations, t = [], [t0, t1, t2]
for i, (px, py, pz, vx, vy, vz) in enumerate(hailstones[:3]):
    equations.append(sympy.Eq(pxr + vxr * t[i], px + vx * t[i])) # x direction
    equations.append(sympy.Eq(pyr + vyr * t[i], py + vy * t[i])) # y direction
    equations.append(sympy.Eq(pzr + vzr * t[i], pz + vz * t[i])) # z direction
# Solve equation and calculate sum of position
sol = sympy.solve(equations, [pxr, pyr, pzr, vxr, vyr, vzr, t0, t1, t2])
print(sum(sol[0][:3]))