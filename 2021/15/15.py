# Read input
risks = []
for line in open('15.txt','r'):
  row = [int(x) for x in line.strip()]
  risks.append(row)
h1, w1 = len(risks), len(risks[0])

# Expand risks
def wrap(x):
  return (x - 1) % 9 + 1
  
new_risks = [[0] * w1 * 5 for _ in range(h1 * 5)]
for r in range(len(new_risks)):
  for c in range(len(new_risks[r])):
    new_risks[r][c] = wrap(risks[r % h1][c % w1] + r // h1 + c // w1)
risks = new_risks.copy()

h, w = len(risks), len(risks[0])
costs = [[0] * len(row) for row in risks]

# BFS with costs map:
start = (0, 0)

front = set()
front.add(start)

while front:
  
  new_front = set()
  for r, c in front:
    cost = costs[r][c]
    
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      nr = r + dr
      nc = c + dc
      
      if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
      
      new_cost = cost + risks[nr][nc]
      
      if costs[nr][nc] == 0:
        costs[nr][nc] = new_cost
        new_front.add((nr, nc))
        
      elif new_cost < costs[nr][nc]:
        costs[nr][nc] = new_cost
        new_front.add((nr, nc))
      
  front = new_front
  
print(costs[h1-1][w1-1])
print(costs[h-1][w-1])