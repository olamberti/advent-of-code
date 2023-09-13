import re

# Read input
floors = []
for line in open('11.txt').read().splitlines():
    floor = []
    items = re.findall(r' (\w+|\w+-compatible) (microchip|generator)', line)
    for m, t in items:
        floor.append(m[0].upper() + m[1] + t[0].upper())
    floors.append(floor)

def create_status(elevator, floors):
    return (elevator, *tuple(tuple(f) for f in floors))

# P1
# TODO code for part 1