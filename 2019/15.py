from intcode import IntCode
memory = [int(x) for x in open('15.txt').read().split(',')]

# P1
dirs = {1: 1j, 2: -1j, 3: -1, 4: 1}
walls, paths, start, oxigen = set(), set(), 0, None
robot = [IntCode(memory), start, 0]   # program, position, steps
paths.add(start)

front = [robot]
while front:
    current = front.pop(0)
    for inp, dir in dirs.items():
        new_robot = current[0].copy()
        new_pos = current[1] + dir
        new_steps = current[2] + 1

        if (new_pos in paths) or (new_pos in walls): continue
        res = new_robot.run(inp)
        
        if res == 0: walls.add(new_pos)
        elif res == 1:
            paths.add(new_pos)
            front.append([new_robot, new_pos, new_steps])
        elif res == 2:
            oxigen = [new_robot, new_pos, new_steps]

print(oxigen[2])

# P2
air, start = set(), oxigen[1]
air.add(start)

front = [[start, 0]]
while front:
    current = front.pop(0)
    for dir in dirs.values():
        new_pos = current[0] + dir
        if (new_pos in air) or (new_pos in walls): continue
        elif new_pos in paths:
            air.add(new_pos)
            new_steps = current[1] + 1
            front.append([new_pos, new_steps])
print(new_steps)