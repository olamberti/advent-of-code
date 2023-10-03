data = open('d11.txt').read().split(',')

dirs = {'n':(1,-1,0), 'ne':(1,0,-1), 'se':(0,1,-1), 's':(-1,1,0), 'sw':(-1,0,1), 'nw':(0,-1,1)}
pos, p2 = (0,0,0), 0

def dist(p):
    return max([abs(x) for x in p])

for d in data:
    pos = (pos[0] + dirs[d][0],  pos[1] + dirs[d][1], pos[2] + dirs[d][2])
    p2 = max(p2, dist(pos))

print(dist(pos))
print(p2)