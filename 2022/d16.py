# Read input:
valves, tunnels = dict(), dict()
start_pos = 'AA'
for line in open('d16.txt', 'r'):
  words = [word.strip('rate=,;') for word in line.strip().split()]
  valves[words[1]] = int(words[4])
  tunnels[words[1]] = [words[i] for i in range(9, len(words))]
                                               
# Functions:
def calc_distance(P1, P2): # BFS distance founder
  visited, frontier = set(), set()
  frontier.add(P1)
  visited.add(P1)
  distance = 0
  while(P2 not in visited):
    distance += 1
    new_frontier = set()
    for point in frontier:
      for neighbour in tunnels[point]:
        if neighbour not in visited:
          visited.add(neighbour)
          new_frontier.add(neighbour)
    frontier = new_frontier
  return distance

def calc_combo_press(current_pos, time, pressure, valves_left):
  max_pressure = pressure
  for valve in valves_left:
    new_time = time + distances[(current_pos, valve)] + 1
    if new_time >= 30:
      continue
    new_valves_left = valves_left[:]
    new_valves_left.remove(valve)
    new_pressure = pressure + ((30 - new_time) * good_valves[valve])
    new_pressure = calc_combo_press(valve, new_time, new_pressure, new_valves_left)
    max_pressure = max(new_pressure, max_pressure)
  return max_pressure

def calc_combo_list(current_pos, time, pressure, valves_left, path):
  new_path = 'AA' if current_pos == 'AA' else (path + '-' + current_pos)
  path_list = dict()
  path_list[new_path] = pressure
  for valve in valves_left:
    new_time = time + distances[(current_pos, valve)] + 1 # calculate time at the end of the step
    if new_time >= 30:
      continue
    new_valves_left = valves_left[:]
    new_valves_left.remove(valve)
    new_pressure = pressure + ((30 - new_time) * good_valves[valve])
    new_path_list = calc_combo_list(valve, new_time, new_pressure, new_valves_left, new_path)
    for my_path, my_pressure in new_path_list.items():
      path_list[my_path] = my_pressure
  return path_list

def path_to_key(path):
  return '-'.join(sorted(path.split('-')))
  
# Look for the distances between all valves that has flow rates > 0 and starting pos:
good_valves, distances = dict(), dict()
for valve, flow_rate in valves.items():
  if flow_rate > 0:
    good_valves[valve] = flow_rate
for i in range(len(good_valves) - 1):
  for j in range(i + 1, len(good_valves)):
    p1, p2 = list(good_valves.keys())[i], list(good_valves.keys())[j]
    dist = calc_distance(p1, p2)
    distances[(p1, p2)] = dist
    distances[(p2, p1)] = dist
for valve in list(good_valves.keys()):
  dist = calc_distance(start_pos, valve)
  distances[(start_pos, valve)] = dist

# Part #1:
t, total_pressure = 0, 0
valves_open = list(good_valves.keys())
total_pressure  = calc_combo_press(start_pos, t, total_pressure, valves_open)
print(total_pressure)

# Part #2:
t, total_pressure = 4, 0
all_paths = calc_combo_list(start_pos, t, total_pressure, valves_open,'')
all_paths = dict(sorted(all_paths.items(), key=lambda item: item[1], reverse  = True))
path_combos = dict()
for my_path, my_pressure in all_paths.items():
  my_path = path_to_key(my_path)
  if my_path not in list(path_combos.keys()):
    path_combos[my_path] = my_pressure
  else:
    path_combos[my_path] = max(path_combos[my_path], my_pressure)

for my_path, my_pressure in path_combos.items():
  my_valves = set(my_path.strip('-').split('-'))
  for ele_path, ele_pressure in path_combos.items():
    different_paths = True
    ele_valves = set(ele_path.strip('AA').split('-'))
    if not my_valves.isdisjoint(ele_valves):
      different_paths = False
    if different_paths:
      total_pressure = max(total_pressure, my_pressure + ele_pressure)
      break
print(total_pressure)